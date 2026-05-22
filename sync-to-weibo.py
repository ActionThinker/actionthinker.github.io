#!/usr/bin/env python3
"""
sync-to-weibo.py — 从知识库洞察卡生成并发布微博
===============================================
从 wiki-知识库/insights-洞察卡/ 选取最新未发布的洞察卡，
格式化为人设化短内容，通过微博API发布。

用法:
  python sync-to-weibo.py                    # 发布1条最新洞察
  python sync-to-weibo.py --dry-run           # 预览不发布
  python sync-to-weibo.py --count 2           # 发布2条

依赖:
  pip install requests pyyaml
"""

import json, os, sys, random, re
from datetime import datetime
from pathlib import Path
from typing import Optional
import yaml

# ─── 路径配置 ───
REPO_ROOT = Path(__file__).resolve().parent
INSIGHTS_DIR = REPO_ROOT.parent / "AI知识资产化" / "wiki-知识库" / "insights-洞察卡"
CONFIG_FILE = REPO_ROOT / ".weibo-config.json"
HISTORY_FILE = REPO_ROOT / ".weibo-history.jsonl"

# ─── 人设配置 ───
PERSONA = {
    "name": "陈露 / ActionThinker",
    "title": "AI知识资产化引领者",
    "voice": {
        "style": "专业但有温度，不说教，用真实体感说话",
        "principles": [
            "每条都要有自己的判断，不只是转述新闻",
            "多用第一人称'我'，少用'我们'",
            "可以质疑主流观点，但要给理由",
            "不卖课，不引流，先输出价值",
            "适当自曝其短——说自己还在探索的领域",
        ],
        "opening_templates": [
            "最近在实践{话题}，有几点体感：",
            "看到一个有意思的信号：{核心观点}。我的判断是：",
            "很多人问我对{话题}怎么看。直接说结论：",
            "今天跟Hermes agent讨论{话题}，达成一个共识：",
            "在帮客户做{话题}时发现一个反直觉的事：",
            "不是标题党，{话题}这件事真的在发生：",
        ],
    },
    "hashtags": ["AI知识资产化", "智能体", "AI认知", "知识管理"],
    "signature": "\n—— 陈露，专注AI知识资产化"
}

# 默认话题标签池 —— 每次随机选2-3个
TOPIC_TAGS = {
    "Agent": ["AI Agent", "智能体", "Agent经济"],
    "知识": ["知识资产化", "知识管理", "隐性知识"],
    "AI开发": ["AI开发速度", "软件工程", "LLM迭代"],
    "企业培训": ["企业AI培训", "AI认知", "人机协作"],
    "品牌": ["个人品牌", "Build in Public", "创始人IP"],
    "趋势": ["AI趋势", "技术观察", "未来工作"],
}


def load_config() -> dict:
    """加载微博API配置。"""
    if not CONFIG_FILE.exists():
        return {}
    with open(CONFIG_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def get_posted_history() -> set:
    """获取已发布的洞察卡UID列表，避免重复发布。"""
    if not HISTORY_FILE.exists():
        return set()
    posted = set()
    with open(HISTORY_FILE, "r", encoding="utf-8") as f:
        for line in f:
            try:
                entry = json.loads(line.strip())
                if "uid" in entry:
                    posted.add(entry["uid"])
            except json.JSONDecodeError:
                continue
    return posted


def scan_insight_cards() -> list[dict]:
    """扫描洞察卡目录，按创建时间排序返回未发布的卡片。"""
    if not INSIGHTS_DIR.exists():
        print(f"  [WARN] 洞察卡目录不存在: {INSIGHTS_DIR}")
        return []

    posted = get_posted_history()
    cards = []

    for f in sorted(INSIGHTS_DIR.glob("*.md"), key=lambda p: p.stat().st_mtime, reverse=True):
        uid = f.stem
        if uid in posted:
            continue

        card = parse_insight_card(f)
        if card:
            card["uid"] = uid
            card["file_path"] = str(f)
            cards.append(card)

    return cards


def parse_insight_card(filepath: Path) -> Optional[dict]:
    """解析洞察卡markdown文件，提取核心字段。"""
    try:
        text = filepath.read_text(encoding="utf-8")
    except Exception:
        return None

    # 提取 frontmatter
    fm_match = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    fm = {}
    if fm_match:
        try:
            fm = yaml.safe_load(fm_match.group(1)) or {}
        except yaml.YAMLError:
            pass

    # 提取核心洞察（h1或引用块后的第一段）
    core_insight = ""
    insight_match = re.search(r"核心洞察[：:]\s*\n>\s*(.+?)(?:\n|$)", text)
    if insight_match:
        core_insight = insight_match.group(1).strip()
    else:
        # fallback: 取h1后的第一段
        h1_match = re.search(r"^#\s+(.+?)$", text, re.MULTILINE)
        if h1_match:
            after_h1 = text[h1_match.end():].strip()
            para_match = re.search(r"^(.+?)(?:\n\n|\n---)", after_h1, re.DOTALL)
            if para_match:
                core_insight = para_match.group(1).strip()

    # 提取启示/分析段落
    analysis = ""
    analysis_match = re.search(r"(?:启示|分析|背后的逻辑)[：:]\s*\n(.+?)(?:\n\n|\n##|\n---)", text, re.DOTALL)
    if analysis_match:
        analysis = analysis_match.group(1).strip()[:200]

    # 提取标签
    tags = fm.get("tags", [])
    business_line = fm.get("business_line", fm.get("business_lines", []))
    priority = fm.get("priority_score", 5)
    created = fm.get("created", "")

    return {
        "title": fm.get("title", filepath.stem),
        "core_insight": core_insight,
        "analysis": analysis,
        "tags": tags if isinstance(tags, list) else [tags],
        "business_line": business_line if isinstance(business_line, list) else [business_line],
        "priority": priority if isinstance(priority, (int, float)) else 5,
        "created": created,
        "raw_text": text,
    }


def generate_weibo_post(card: dict) -> str:
    """将洞察卡格式化为带人设的微博内容。"""
    core = card.get("core_insight", "")
    title = card.get("title", "")
    analysis = card.get("analysis", "")

    if not core:
        core = title

    # 确定话题分类
    all_tags = card.get("tags", []) + card.get("business_line", [])
    topic = "AI趋势"
    for tag_str in all_tags:
        for topic_key, topic_tags in TOPIC_TAGS.items():
            for t in topic_tags:
                if t in str(tag_str):
                    topic = topic_key
                    break

    # 选择开场白模板
    templates = PERSONA["voice"]["opening_templates"]
    opening = random.choice(templates).format(
        话题=topic,
        核心观点=core[:30] + "…" if len(core) > 30 else core,
    )

    # 构建正文
    paragraphs = []

    # 开场
    paragraphs.append(opening)

    # 核心洞察（精简到100字以内）
    core_short = core[:120] if len(core) > 120 else core
    if core_short:
        paragraphs.append(core_short)

    # 个人判断（如果分析内容存在）
    if analysis:
        paragraphs.append(analysis[:150])

    # 结尾引导互动
    endings = [
        "\n你怎么看？",
        "\n这条你认同吗？",
        "\n有没有类似的体感？",
        "\n这是我最近的观察，欢迎讨论。",
        "\n持续观察中，有新的判断再分享。",
        "\n你在实践中有遇到过类似情况吗？",
    ]
    paragraphs.append(random.choice(endings))

    # 话题标签（随机选2个）
    selected_tags = random.sample(
        PERSONA["hashtags"],
        min(2, len(PERSONA["hashtags"]))
    )
    # 加1个关联标签
    if card.get("tags"):
        extra_tag = random.choice(card["tags"])
        if isinstance(extra_tag, str) and len(extra_tag) < 20:
            selected_tags.append(extra_tag.replace("_", "").replace("-", ""))

    tag_line = " " + " ".join(f"#{t}#" for t in selected_tags if t)

    # 签名
    full = "\n\n".join(paragraphs) + "\n" + tag_line + PERSONA["signature"]

    return full


def post_to_weibo(text: str, config: dict) -> bool:
    """通过微博API发布内容。"""
    app_key = config.get("app_key", os.environ.get("WEIBO_APP_KEY", ""))
    app_secret = config.get("app_secret", os.environ.get("WEIBO_APP_SECRET", ""))
    access_token = config.get("access_token", os.environ.get("WEIBO_ACCESS_TOKEN", ""))

    if not access_token:
        print("  [ERROR] 未配置微博 access_token。请先完成 OAuth 授权。")
        print("  [HELP] 运行 python sync-to-weibo.py --auth 查看授权指引。")
        return False

    # 微博API端点：statuses/share (需要 HTTPS)
    url = "https://api.weibo.com/2/statuses/share.json"

    # 微博有字数限制（2000字），超出需要截断
    if len(text) > 1990:
        text = text[:1980] + "…" + PERSONA["signature"]

    import requests
    try:
        resp = requests.post(url, data={
            "access_token": access_token,
            "status": text,
        }, timeout=15)
        result = resp.json()

        if "error_code" in result:
            print(f"  [FAIL] 微博API错误 {result['error_code']}: {result.get('error', '未知')}")
            return False

        print(f"  [OK] 发布成功：https://weibo.com/{result.get('id', '')}")
        return True

    except requests.exceptions.Timeout:
        print("  [FAIL] 请求超时")
        return False
    except requests.exceptions.RequestException as e:
        print(f"  [FAIL] 网络错误: {e}")
        return False
    except Exception as e:
        print(f"  [FAIL] 未知错误: {e}")
        return False


def record_history(uid: str, text: str, success: bool):
    """记录发布历史。"""
    entry = {
        "uid": uid,
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "success": success,
        "text_preview": text[:80],
    }
    with open(HISTORY_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")


def show_auth_guide():
    """显示微博开发者授权指引。"""
    config = load_config()
    app_key = config.get("app_key", os.environ.get("WEIBO_APP_KEY", ""))
    app_secret = config.get("app_secret", os.environ.get("WEIBO_APP_SECRET", ""))

    if not app_key or not app_secret:
        print("=" * 60)
        print("  微博开放平台接入指引")
        print("=" * 60)
        print()
        print("  第1步：访问 https://open.weibo.com/ 注册开发者账号")
        print("  第2步：创建「微应用」→ 获取 AppKey 和 AppSecret")
        print("  第3步：将信息写入配置文件 .weibo-config.json：")
        print()
        print('    {')
        print('      "app_key": "你的AppKey",')
        print('      "app_secret": "你的AppSecret",')
        print('      "access_token": "获取的AccessToken"')
        print('    }')
        print()
        print("  第4步：OAuth2.0 授权（获取 access_token）")
        print("  在浏览器中访问以下URL（将APP_KEY替换为你的AppKey）：")
        print()
        print("  https://api.weibo.com/oauth2/authorize?client_id=APP_KEY&response_type=code&redirect_uri=https://api.weibo.com/oauth2/default.html")
        print()
        print("  授权后获取 code → 换取 access_token")
        print("  (可将 access_token 也写入 .weibo-config.json)")
        print()
        print("  完成后运行 python sync-to-weibo.py 测试发布")
        print("=" * 60)
        return

    if not config.get("access_token"):
        print("  AppKey 和 AppSecret 已配置，缺少 access_token。")
        print("  请访问以下URL完成 OAuth 授权：")
        auth_url = f"https://api.weibo.com/oauth2/authorize?client_id={app_key}&response_type=code&redirect_uri=https://api.weibo.com/oauth2/default.html"
        print(f"\n  {auth_url}\n")
        return

    print("  微博API配置已完成。运行 sync-to-weibo.py 发布内容。")


def main():
    import argparse
    parser = argparse.ArgumentParser(description="同步洞察卡到微博")
    parser.add_argument("--dry-run", action="store_true", help="预览不发布")
    parser.add_argument("--count", type=int, default=1, help="发布条数")
    parser.add_argument("--auth", action="store_true", help="显示授权指引")
    parser.add_argument("--card", type=str, default="", help="指定卡片UID")
    args = parser.parse_args()

    if args.auth:
        show_auth_guide()
        return

    # 扫描洞察卡
    cards = scan_insight_cards()
    if not cards:
        print("  [INFO] 没有新的洞察卡需要发布。")
        return

    # 选择要发布的卡片
    selected = cards[:args.count]
    if args.card:
        selected = [c for c in cards if c["uid"] == args.card]
        if not selected:
            print(f"  [ERROR] 未找到指定卡片: {args.card}")
            return

    print(f"\n  准备发布 {len(selected)} 条微博\n")

    for card in selected:
        post = generate_weibo_post(card)

        print("  ── " + "─" * 50)
        print(f"  卡片: {card.get('title', card['uid'])}")
        print("  ── " + "─" * 50)
        print()
        print(post)
        print()
        print(f"  字数: {len(post)}")
        print()

        if args.dry_run:
            print("  [DRY RUN] 不发布\n")
            record_history(card["uid"], post, success=True)
            continue

        config = load_config()
        if not config.get("access_token"):
            print("  [SKIP] 未配置 access_token。使用 --dry-run 预览或 --auth 查看授权指引。\n")
            continue

        success = post_to_weibo(post, config)
        record_history(card["uid"], post, success)

        if success:
            print(f"  ✅ 已发布: {card.get('title', card['uid'])}\n")


if __name__ == "__main__":
    main()
