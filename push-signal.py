#!/usr/bin/env python3
"""
push-signal.py — Claude × Hermes 文件即消息协议：监控端
========================================================
Hermes 写入 .pending-push.json → Claude 监控执行 git push

用法:
  python push-signal.py              # 处理所有待推送信号
  python push-signal.py --watch      # 持续监控模式（按间隔轮询）
  python push-signal.py --once       # 单次检查（适合 cron / Hermes 触发）

信号格式 (.pending-push.json):
  {
    "post_file": "_posts/2026-05-22-slug.md",
    "title": "文章标题",
    "author": "ActionThinker",
    "timestamp": "2026-05-22T10:00:00",
    "source": "hermes-engine-2"
  }

结果:
  成功 → 删除信号文件 + 写入 .push-success.json
  失败 → 保留信号文件 + 写入 .push-failed.json（含错误信息）
"""

import json, os, sys, subprocess, time
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent
# Hermes writes to _posts/.pending-push (simple format: just the filename)
HERMES_SIGNAL = REPO_ROOT / "_posts" / ".pending-push"
# Claude also supports JSON format at repo root for tool-chain use
JSON_SIGNAL = REPO_ROOT / ".pending-push.json"
SUCCESS_FILE = REPO_ROOT / ".push-success.json"
FAILED_FILE = REPO_ROOT / ".push-failed.json"
LOG_FILE = REPO_ROOT / ".push-history.jsonl"


def log(entry: dict):
    """Append to push history log."""
    entry["logged_at"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")


def read_signal() -> dict | None:
    """Read and parse signal files. Returns None if no signal.
    Supports two formats:
    1. Hermes native: _posts/.pending-push (just the filename on one line)
    2. JSON format: .pending-push.json (structured, for tool chains)
    """
    # Check Hermes native format first
    if HERMES_SIGNAL.exists():
        try:
            raw = HERMES_SIGNAL.read_text(encoding="utf-8").strip()
            if raw:
                return {
                    "post_file": f"_posts/{raw}",
                    "title": raw.replace(".md", "").replace("-", " "),
                    "source": "hermes-engine-2",
                    "signal_format": "hermes-native",
                }
        except OSError:
            pass

    # Check JSON format
    if JSON_SIGNAL.exists():
        try:
            with open(JSON_SIGNAL, "r", encoding="utf-8") as f:
                signal = json.load(f)
                signal["signal_format"] = "json"
                return signal
        except (json.JSONDecodeError, OSError) as e:
            return {"error": str(e), "raw": JSON_SIGNAL.read_text(encoding="utf-8")[:200]}

    return None


def validate_signal(signal: dict) -> tuple[bool, str]:
    """Validate signal has required fields and post file exists. Returns (ok, reason)."""
    required = ["post_file", "title"]
    for field in required:
        if field not in signal:
            return False, f"Missing required field: {field}"

    post_path = REPO_ROOT / signal["post_file"]
    if not post_path.exists():
        return False, f"Post file not found: {signal['post_file']}"

    return True, "ok"


def git_push(signal: dict) -> tuple[bool, str]:
    """Execute git add + commit + push. Returns (ok, message)."""
    post_file = signal["post_file"]
    title = signal.get("title", "untitled")
    author = signal.get("author", "ActionThinker")

    try:
        # git add
        result = subprocess.run(
            ["git", "add", post_file],
            cwd=str(REPO_ROOT), capture_output=True, text=True, timeout=30
        )
        if result.returncode != 0:
            return False, f"git add failed: {result.stderr.strip()}"

        # Check if there are staged changes
        result = subprocess.run(
            ["git", "diff", "--cached", "--quiet"],
            cwd=str(REPO_ROOT), capture_output=True, timeout=30
        )
        if result.returncode == 0:
            return False, "No changes to commit (file may already be committed)"

        # git commit
        commit_msg = f"post: {title}\n\nSource: {signal.get('source', 'unknown')}"
        result = subprocess.run(
            ["git", "commit", "-m", commit_msg],
            cwd=str(REPO_ROOT), capture_output=True, text=True, timeout=30
        )
        if result.returncode != 0:
            return False, f"git commit failed: {result.stderr.strip()}"

        # git push
        result = subprocess.run(
            ["git", "push", "origin", "master"],
            cwd=str(REPO_ROOT), capture_output=True, text=True, timeout=60
        )
        if result.returncode != 0:
            return False, f"git push failed: {result.stderr.strip()}"

        return True, f"Pushed: {title}"
    except subprocess.TimeoutExpired:
        return False, "Git operation timed out"
    except Exception as e:
        return False, f"Unexpected error: {e}"


def write_result(success: bool, signal: dict, message: str):
    """Write result file and archive signal."""
    result = {
        "success": success,
        "title": signal.get("title", "untitled"),
        "post_file": signal.get("post_file", ""),
        "timestamp": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "message": message,
    }

    # Determine which signal file to clean up
    signal_format = signal.get("signal_format", "json")
    signal_path = HERMES_SIGNAL if signal_format == "hermes-native" else JSON_SIGNAL

    if success:
        with open(SUCCESS_FILE, "w", encoding="utf-8") as f:
            json.dump(result, f, ensure_ascii=False, indent=2)
        if FAILED_FILE.exists():
            FAILED_FILE.unlink()
        # Archive the signal (move to timestamped copy)
        archive_name = f".push-success-{datetime.now().strftime('%Y%m%d-%H%M%S')}"
        signal_path.rename(signal_path.parent / archive_name)
        print(f"  PUSH SUCCESS: {signal.get('title')} → actionthinker.com")
    else:
        result["retry_hint"] = "Fix the issue, then re-run: python push-signal.py"
        with open(FAILED_FILE, "w", encoding="utf-8") as f:
            json.dump(result, f, ensure_ascii=False, indent=2)
        print(f"  PUSH FAILED: {message}")


def process_signal() -> bool:
    """Process a single pending push signal. Returns True if push succeeded."""
    signal = read_signal()
    if signal is None:
        print("  No pending signal.")
        return True  # Nothing to do = success

    if "error" in signal:
        print(f"  SIGNAL CORRUPT: {signal['error']}")
        log({"event": "corrupt_signal", "error": signal["error"]})
        return False

    print(f"  Signal detected: {signal.get('title', 'untitled')}")

    ok, reason = validate_signal(signal)
    if not ok:
        print(f"  VALIDATION FAILED: {reason}")
        write_result(False, signal, reason)
        log({"event": "validation_failed", "reason": reason, "signal": signal})
        return False

    ok, message = git_push(signal)
    write_result(ok, signal, message)
    log({"event": "push_completed", "success": ok, "message": message, "title": signal.get("title")})
    return ok


def print_status():
    """Print current signal system status."""
    has_hermes = HERMES_SIGNAL.exists()
    has_json = JSON_SIGNAL.exists()
    print("Push Signal System Status")
    print("=" * 40)
    print(f"  Repo: {REPO_ROOT}")
    print(f"  Hermes Signal (_posts/.pending-push): {'PRESENT' if has_hermes else 'none'}")
    print(f"  JSON Signal (.pending-push.json): {'PRESENT' if has_json else 'none'}")
    print(f"  Last Success: {'PRESENT' if SUCCESS_FILE.exists() else 'none'}")
    print(f"  Last Failure: {'PRESENT' if FAILED_FILE.exists() else 'none'}")

    signal = read_signal()
    if signal and "error" not in signal:
        print(f"  Pending: {signal.get('title', '?')} ({signal.get('post_file', '?')})")

    if FAILED_FILE.exists():
        with open(FAILED_FILE, "r", encoding="utf-8") as f:
            failed = json.load(f)
            print(f"  Failure: {failed.get('message', '?')}")


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Claude × Hermes push signal handler")
    parser.add_argument("--watch", action="store_true", help="Continuous watch mode")
    parser.add_argument("--once", action="store_true", help="Single check (non-interactive)")
    parser.add_argument("--status", action="store_true", help="Show status only")
    parser.add_argument("--interval", type=int, default=30, help="Watch interval in seconds")

    args = parser.parse_args()

    if args.status:
        print_status()
        return

    if args.watch:
        print(f"Watching for .pending-push.json (interval: {args.interval}s)...")
        try:
            while True:
                if SIGNAL_FILE.exists():
                    print(f"\n[{datetime.now().strftime('%H:%M:%S')}] Signal detected!")
                    process_signal()
                time.sleep(args.interval)
        except KeyboardInterrupt:
            print("\nWatch stopped.")
        return

    # Default: process once
    process_signal()


if __name__ == "__main__":
    main()
