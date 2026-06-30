"""Content loader for ActionThinker MCP server.

Parses the Jekyll website repo to extract structured data from:
- _posts/*.md (Markdown with YAML frontmatter)
- faq.html (HTML Q&A sections)
- Key HTML pages (about, services, etc.)
"""

import re
import logging
from pathlib import Path
from dataclasses import dataclass, field

import yaml
from bs4 import BeautifulSoup

logger = logging.getLogger(__name__)


@dataclass
class Post:
    slug: str
    title: str
    subtitle: str
    date: str
    tags: list[str] = field(default_factory=list)
    url: str = ""
    body_text: str = ""

    def to_dict(self):
        return {
            "slug": self.slug,
            "title": self.title,
            "subtitle": self.subtitle,
            "date": self.date,
            "tags": self.tags,
            "url": self.url,
            "summary": self.body_text[:300] if self.body_text else "",
        }


@dataclass
class FaqItem:
    question: str
    answer: str
    topic: str = ""

    def to_dict(self):
        return {"question": self.question, "answer": self.answer, "topic": self.topic}


@dataclass
class Page:
    path: str
    title: str
    subtitle: str
    body_text: str = ""
    url: str = ""

    def to_dict(self):
        return {
            "path": self.path,
            "title": self.title,
            "subtitle": self.subtitle,
            "content": self.body_text,
            "url": self.url,
        }


# ── Helpers ──────────────────────────────────────────────

def _parse_yaml_frontmatter(text: str) -> tuple[dict, str]:
    """Split YAML frontmatter from body. Returns (metadata, body)."""
    text = text.lstrip()
    if not text.startswith("---"):
        return {}, text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}, text
    try:
        meta = yaml.safe_load(parts[1]) or {}
    except yaml.YAMLError:
        meta = {}
    return meta, parts[2].strip()


def _strip_html(text: str) -> str:
    """Remove HTML tags, return plain text."""
    soup = BeautifulSoup(text, "html.parser")
    return soup.get_text(separator=" ", strip=True)


def _strip_markdown(text: str) -> str:
    """Reduce markdown formatting for searchable text."""
    text = re.sub(r"#{1,6}\s+", "", text)
    text = re.sub(r"\*{1,3}(.+?)\*{1,3}", r"\1", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"!\[([^\]]*)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"`{1,3}[^`]*`{1,3}", "", text)
    text = re.sub(r"[-*+]\s+", "", text)
    text = re.sub(r"\n{2,}", "\n", text)
    text = re.sub(r"^>.+$", "", text, flags=re.MULTILINE)
    text = re.sub(r"---+", "", text)
    return text.strip()


def _clean_text(text: str, max_chars: int = 2000) -> str:
    """Strip HTML + markdown, collapse whitespace, truncate."""
    text = _strip_html(text)
    text = _strip_markdown(text)
    text = re.sub(r"\s+", " ", text)
    return text[:max_chars].strip()


# ── Loaders ──────────────────────────────────────────────

def load_posts(repo_root: Path, site_url: str) -> list[Post]:
    """Parse _posts/*.md into Post objects sorted by date descending."""
    posts_dir = repo_root / "_posts"
    if not posts_dir.exists():
        return []

    posts = []
    for md_file in sorted(posts_dir.glob("*.md"), reverse=True):
        filename = md_file.name
        if filename.startswith(".~"):
            continue

        try:
            with open(md_file, "r", encoding="utf-8") as f:
                content = f.read()
        except Exception:
            continue

        meta, body = _parse_yaml_frontmatter(content)
        if not meta:
            continue

        title = meta.get("title", filename)
        subtitle = meta.get("subtitle", "")
        tags = meta.get("tags", [])
        if isinstance(tags, str):
            tags = [t.strip() for t in tags.split(",") if t.strip()]

        date_str = str(meta.get("date", ""))
        if not date_str and re.match(r"^(\d{4})-(\d{2})-(\d{2})", filename):
            date_str = filename[:10]

        # Build slug from filename: strip date prefix and .md
        slug = re.sub(r"^\d{4}-\d{2}-\d{2}-", "", filename).replace(".md", "")
        post_url = f"{site_url}/{slug}/"

        body_text = _clean_text(body)
        post = Post(
            slug=slug,
            title=str(title),
            subtitle=str(subtitle) if subtitle else "",
            date=date_str,
            tags=tags,
            url=post_url,
            body_text=body_text,
        )
        posts.append(post)

    return posts


def load_faq(repo_root: Path, site_url: str) -> list[FaqItem]:
    """Parse faq.html into FaqItem objects grouped by topic section."""
    faq_path = repo_root / "faq.html"
    if not faq_path.exists():
        return []

    with open(faq_path, "r", encoding="utf-8") as f:
        content = f.read()

    soup = BeautifulSoup(content, "html.parser")
    items = []

    # FAQ sections are h2 headings, followed by faq-item divs with h3+p
    sections = soup.find_all("h2")
    for section in sections:
        topic = section.get_text(strip=True)
        current = section.find_next_sibling()

        while current and current.name != "h2":
            if current.name == "div" and "faq-item" in current.get("class", []):
                h3 = current.find("h3")
                p = current.find("p")
                if h3 and p:
                    question = h3.get_text(strip=True)
                    answer = p.get_text(strip=True)
                    items.append(
                        FaqItem(question=question, answer=answer, topic=topic)
                    )
            current = current.find_next_sibling()

    return items


def load_pages(repo_root: Path, site_url: str) -> dict[str, Page]:
    """Parse key HTML pages with YAML frontmatter into Page objects."""
    from .config import PAGE_MAP

    pages = {}
    for logical_name, filename in PAGE_MAP.items():
        file_path = repo_root / filename
        if not file_path.exists():
            continue

        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
        except Exception:
            continue

        meta, body = _parse_yaml_frontmatter(content)
        title = meta.get("title", logical_name)
        subtitle = meta.get("subtitle", "")
        body_text = _clean_text(body, max_chars=5000)
        page_url = f"{site_url}/{logical_name}/" if logical_name != "index" else site_url

        pages[logical_name] = Page(
            path=logical_name,
            title=str(title),
            subtitle=str(subtitle) if subtitle else "",
            body_text=body_text,
            url=page_url,
        )

    return pages


def load_all(repo_root: Path) -> dict:
    """Load all content sources. Returns dict with posts, faq, pages."""
    from .config import load_site_config

    site_config = load_site_config(repo_root)
    site_url = site_config["url"]

    posts = load_posts(repo_root, site_url)
    faq = load_faq(repo_root, site_url)
    pages = load_pages(repo_root, site_url)

    return {
        "config": site_config,
        "posts": posts,
        "faq": faq,
        "pages": pages,
    }
