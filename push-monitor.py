#!/usr/bin/env python3
"""
push-monitor.py — OPC L0 心跳层：pending-push 信号监控
=========================================================
Windows Task Scheduler 入口，每分钟轮询一次。

信号规范: OPC Agent 通信协议 v1.0 第四章
  发送方: Hermes 引擎2 (写入 _posts/.pending-push)
  接收方: ClaudeCode (检测 → git push → 清理)

用法:
  python push-monitor.py           # 单次检查 (Task Scheduler 用)
  python push-monitor.py --status  # 显示当前状态
  python push-monitor.py --loop    # 持续循环模式 (调试用)

信号文件格式 (_posts/.pending-push):
  YAML frontmatter (非必须) + 文件路径 (一行一个)
  或直接放入要推送的文件名

结果:
  成功 → 删除信号 + 写入 .push-success.json
  失败 → 重命名为 .pending-push.failed + 写入错误信息
"""

import json
import os
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent
SIGNAL_FILE = REPO_ROOT / "_posts" / ".pending-push"
SUCCESS_FILE = REPO_ROOT / ".push-success.json"
FAILED_FILE = REPO_ROOT / ".push-failed.json"
LOG_FILE = REPO_ROOT / ".push-history.jsonl"


def log(entry: dict):
    entry["logged_at"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")


def read_signal() -> list[str] | None:
    """Parse _posts/.pending-push. Returns list of file paths relative to repo root, or None."""
    if not SIGNAL_FILE.exists():
        return None
    try:
        raw = SIGNAL_FILE.read_text(encoding="utf-8").strip()
        if not raw:
            return None
        lines = raw.split("\n")
        files = []
        for line in lines:
            line = line.strip()
            if not line or line.startswith("---") or line.startswith("#"):
                continue
            # Extract filename from possible YAML frontmatter or markdown
            if line.startswith("_posts/") or line.startswith("post_file:"):
                fname = line.replace("post_file:", "").strip().strip('"').strip("'")
                files.append(fname if fname.startswith("_posts/") else f"_posts/{fname}")
            elif line.endswith(".md"):
                files.append(line if line.startswith("_posts/") else f"_posts/{line}")
        return files if files else None
    except OSError:
        return None


def fix_crlf(filepath: Path) -> bool:
    """Strip CR from file. Returns True if file was modified."""
    try:
        content = filepath.read_bytes()
        if b"\r\n" in content or b"\r" in content:
            cleaned = content.replace(b"\r\n", b"\n").replace(b"\r", b"\n")
            filepath.write_bytes(cleaned)
            return True
        return False
    except OSError:
        return False


def validate_post(filepath: Path) -> tuple[bool, str]:
    """Check that the post file exists and has basic frontmatter. Returns (ok, reason)."""
    if not filepath.exists():
        return False, f"File not found: {filepath}"
    try:
        content = filepath.read_text(encoding="utf-8")
        if not content.startswith("---"):
            return False, f"Missing YAML frontmatter in {filepath.name}"
        # Check closing ---
        parts = content.split("---", 2)
        if len(parts) < 2:
            return False, f"Malformed frontmatter in {filepath.name}"
        return True, "ok"
    except OSError as e:
        return False, f"Read error: {e}"


def extract_title(filepath: Path) -> str:
    """Extract title from frontmatter or filename."""
    try:
        content = filepath.read_text(encoding="utf-8")
        for line in content.split("\n")[1:]:
            if line.startswith("title:"):
                return line.split(":", 1)[1].strip().strip('"').strip("'")
    except OSError:
        pass
    return filepath.stem.replace("-", " ")


def git_push(files: list[str]) -> tuple[bool, str]:
    """Stage, commit, and push the given files. Returns (ok, message)."""
    try:
        titles = []
        for f in files:
            filepath = REPO_ROOT / f
            fix_crlf(filepath)
            ok, reason = validate_post(filepath)
            if not ok:
                return False, reason
            titles.append(extract_title(filepath))

        # git add
        result = subprocess.run(
            ["git", "add"] + files,
            cwd=str(REPO_ROOT), capture_output=True, text=True, timeout=30
        )
        if result.returncode != 0:
            return False, f"git add failed: {result.stderr.strip()}"

        # Check for staged changes
        result = subprocess.run(
            ["git", "diff", "--cached", "--quiet"],
            cwd=str(REPO_ROOT), capture_output=True, timeout=30
        )
        if result.returncode == 0:
            return False, "No changes to commit"

        # Commit
        title_str = titles[0] if len(titles) == 1 else f"{len(titles)} posts"
        result = subprocess.run(
            ["git", "commit", "-m", f"publish: {title_str}"],
            cwd=str(REPO_ROOT), capture_output=True, text=True, timeout=30
        )
        if result.returncode != 0:
            return False, f"git commit failed: {result.stderr.strip()}"

        # Push
        result = subprocess.run(
            ["git", "push", "origin", "master"],
            cwd=str(REPO_ROOT), capture_output=True, text=True, timeout=120
        )
        if result.returncode != 0:
            return False, f"git push failed: {result.stderr.strip()}"

        return True, f"Pushed: {title_str}"
    except subprocess.TimeoutExpired:
        return False, "Git operation timed out"
    except Exception as e:
        return False, f"Unexpected error: {e}"


def cleanup_signal(success: bool, message: str):
    """Follow OPC protocol 4.3: delete on success, rename to .failed on error."""
    if success:
        SIGNAL_FILE.unlink(missing_ok=True)
        result = {"success": True, "message": message,
                  "timestamp": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")}
        with open(SUCCESS_FILE, "w", encoding="utf-8") as f:
            json.dump(result, f, ensure_ascii=False, indent=2)
        if FAILED_FILE.exists():
            FAILED_FILE.unlink()
    else:
        failed_path = SIGNAL_FILE.with_suffix(SIGNAL_FILE.suffix + ".failed")
        result = {"success": False, "error": message,
                  "attempted_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
                  "retry_count": 0}
        with open(failed_path, "w", encoding="utf-8") as f:
            json.dump(result, f, ensure_ascii=False, indent=2)
        # Also write to repo root for visibility
        with open(FAILED_FILE, "w", encoding="utf-8") as f:
            json.dump(result, f, ensure_ascii=False, indent=2)


def process() -> bool:
    """Single check cycle. Returns True if push succeeded or no signal."""
    files = read_signal()
    if files is None:
        return True

    print(f"[{datetime.now().strftime('%H:%M:%S')}] Signal: {len(files)} file(s)")
    ok, message = git_push(files)
    cleanup_signal(ok, message)

    if ok:
        print(f"  PUSH OK → {message}")
        log({"event": "push_success", "files": files, "message": message})
    else:
        print(f"  PUSH FAIL: {message}")
        log({"event": "push_failed", "files": files, "error": message})
    return ok


def print_status():
    print("OPC Push Monitor Status")
    print("=" * 50)
    print(f"  Repo: {REPO_ROOT}")
    print(f"  Signal: {'PRESENT' if SIGNAL_FILE.exists() else 'none'}")
    print(f"  Last success: {'PRESENT' if SUCCESS_FILE.exists() else 'none'}")
    print(f"  Last failure: {'PRESENT' if FAILED_FILE.exists() else 'none'}")
    if FAILED_FILE.exists():
        with open(FAILED_FILE, "r", encoding="utf-8") as f:
            failed = json.load(f)
            print(f"  Failure: {failed.get('error', '?')}")


def main():
    if "--status" in sys.argv:
        print_status()
        return
    if "--loop" in sys.argv:
        interval = 60
        print(f"Push monitor loop (interval: {interval}s). Ctrl+C to stop.")
        try:
            while True:
                process()
                time.sleep(interval)
        except KeyboardInterrupt:
            print("\nStopped.")
        return
    # Default: single check for Task Scheduler
    process()


if __name__ == "__main__":
    main()
