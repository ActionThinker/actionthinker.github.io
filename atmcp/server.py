"""ActionThinker MCP Server — AI agent tools for actionthinker.com.

FastMCP server that provides 6 tools for querying the site's knowledge base.
Reads content from the local Jekyll repo clone at startup.
"""

import logging
from fastmcp import FastMCP

from .config import resolve_repo_root, load_site_config, get_contact_info, PAGE_MAP, PAGE_WHITELIST
from .loader import load_all

logger = logging.getLogger(__name__)

mcp = FastMCP("actionthinker")

# Lazy-loaded content cache
CONTENT: dict | None = None


def _ensure_loaded():
    global CONTENT
    if CONTENT is None:
        repo_root = resolve_repo_root()
        CONTENT = load_all(repo_root)
        post_count = len(CONTENT.get("posts", []))
        faq_count = len(CONTENT.get("faq", []))
        page_count = len(CONTENT.get("pages", {}))
        logger.info(
            "ActionThinker MCP loaded: %d posts, %d faq items, %d pages from %s",
            post_count, faq_count, page_count, repo_root,
        )
    return CONTENT


# ── Tools ────────────────────────────────────────────────

@mcp.tool()
def search_content(query: str) -> list[dict]:
    """Search across all posts, pages, and FAQ for matching text.

    Performs token-based scoring across title, tags, and body.
    Returns results sorted by relevance.
    """
    content = _ensure_loaded()
    if not query:
        return []

    q = query.lower().strip()[:200]
    q_tokens = q.split()

    results = []

    # Search posts
    for post in content.get("posts", []):
        score = _score_match(q, q_tokens, post.title, post.body_text, post.tags)
        if score > 0:
            results.append({
                "id": post.slug,
                "title": post.title,
                "type": "post",
                "summary": post.subtitle or post.body_text[:200],
                "tags": post.tags,
                "url": post.url,
                "relevance": score,
            })

    # Search pages
    for name, page in content.get("pages", {}).items():
        score = _score_match(q, q_tokens, page.title, page.body_text, [])
        if score > 0:
            results.append({
                "id": page.path,
                "title": page.title,
                "type": "page",
                "summary": page.subtitle or page.body_text[:200],
                "tags": [],
                "url": page.url,
                "relevance": score,
            })

    # Search FAQ
    for faq in content.get("faq", []):
        score = _score_match(q, q_tokens, faq.question, faq.answer, [faq.topic])
        if score > 0:
            results.append({
                "id": f"faq-{faq.question[:30]}",
                "title": faq.question,
                "type": "faq",
                "summary": faq.answer[:200],
                "tags": [faq.topic] if faq.topic else [],
                "url": "",
                "relevance": score,
            })

    results.sort(key=lambda r: r["relevance"], reverse=True)
    return results[:20]


@mcp.tool()
def get_latest_posts(limit: int = 5) -> list[dict]:
    """Get the most recent blog posts.

    Args:
        limit: Number of posts to return (1-20, default 5).
    """
    content = _ensure_loaded()
    limit = max(1, min(limit, 20))
    posts = content.get("posts", [])[:limit]
    return [p.to_dict() for p in posts]


@mcp.tool()
def get_services() -> list[dict]:
    """Get all service offerings with descriptions and target audiences.

    Returns enterprise and personal services from the website.
    """
    service_pages = {
        "enterprise-ai": "企业AI落地",
        "enterprise-consulting": "企业知识资产化咨询",
        "enterprise-ai-training": "企业AI实战培训",
        "personal-brand": "个人品牌资产诊断",
        "knowledge-assetization": "知识资产化服务",
    }

    content = _ensure_loaded()
    services = []
    pages = content.get("pages", {})
    config = content.get("config", {})

    for path, name in service_pages.items():
        page = pages.get(path)
        if page:
            services.append({
                "id": path,
                "name": name,
                "subtitle": page.subtitle,
                "description": page.body_text[:500],
                "url": f"{config.get('url', '')}/{path}/",
            })
        else:
            services.append({
                "id": path,
                "name": name,
                "subtitle": "",
                "description": "",
                "url": f"{config.get('url', '')}/{path}/",
            })

    return services


@mcp.tool()
def get_about() -> dict:
    """Get detailed info about 陈露 (ActionThinker): background, methodology, contact."""
    content = _ensure_loaded()
    pages = content.get("pages", {})
    config = content.get("config", {})
    about = pages.get("about")

    if not about:
        return {
            "name": "陈露",
            "brand": "ActionThinker",
            "title": config.get("title", ""),
        }

    text = about.body_text
    return {
        "name": "陈露",
        "brand": "ActionThinker",
        "title": about.title,
        "subtitle": about.subtitle,
        "summary": text[:300],
        "career_highlights": [
            "前NPLUS首席知识官",
            "CAPE全球青年实践网络联合创始人",
            "TEDxBohaiBay演讲者",
            "15年知识管理实践，经历博客→移动互联网→AI三次媒介革命",
        ],
        "methodology": {
            "framework": "O+P+C — Open（开口表达）+ Practice（亲身实践）+ Company（一人公司）",
            "knowledge_system": "五卡体系：案例卡 + 方法论卡 + 决策卡 + 风险卡 + 偏好卡",
            "core_insight": "连接≠编译——把散乱信息变成AI可调用的结构化知识网络",
        },
        "services_summary": [
            "企业AI落地：场景发现→快速验证→落地迭代",
            "知识资产化：专家经验萃取→五卡知识体系→AI可调用",
            "个人品牌：六维诊断→定位象限→三步链路",
        ],
        "contact": get_contact_info(config),
        "url": about.url,
        "full_text": text,
    }


@mcp.tool()
def get_faq(topic: str = None) -> list[dict]:
    """Get FAQ answers from the site.

    Args:
        topic: Optional filter. Valid values: "企业AI落地", "知识资产化",
               "个人品牌定位", "一人公司". If omitted, returns all FAQs.
    """
    content = _ensure_loaded()
    items = content.get("faq", [])
    if topic:
        items = [i for i in items if topic in i.topic]
    return [i.to_dict() for i in items]


@mcp.tool()
def get_page(path: str) -> dict | None:
    """Get full content of a specific page by name.

    Args:
        path: Page identifier, e.g. "about", "service", "enterprise-ai",
              "enterprise-consulting", "personal-brand", "knowledge-assetization",
              "opclab", "self-check", "faq".
    """
    if path not in PAGE_WHITELIST:
        available = sorted(PAGE_MAP.keys())
        return {
            "error": f"Unknown page: {path}",
            "available_pages": available,
        }

    # Normalize: if given a filename, convert to logical name
    logical = path.replace(".html", "")
    if logical not in PAGE_MAP:
        return {"error": f"Unknown page: {path}"}

    content = _ensure_loaded()
    pages = content.get("pages", {})
    page = pages.get(logical)
    if page:
        return page.to_dict()
    return {"error": f"Page not loaded: {logical}"}


# ── Search helpers ───────────────────────────────────────

def _score_match(
    query: str, tokens: list[str],
    title: str, body: str, tags: list[str],
) -> float:
    """Score a content item against query. Returns 0.0–1.0."""
    title_l = title.lower()
    body_l = body.lower()[:500]
    tags_l = " ".join(tags).lower()

    score = 0.0

    if query in title_l:
        score += 50
    for t in tokens:
        if t and t in title_l:
            score += 10

    if query in tags_l:
        score += 20
    for t in tokens:
        if t and t in tags_l:
            score += 5

    if query in body_l:
        score += 15
    for t in tokens:
        if t and t in body_l:
            score += 3

    # Normalize to 0–1 range (max plausible score ~150)
    return min(score / 100.0, 1.0)


def main():
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
