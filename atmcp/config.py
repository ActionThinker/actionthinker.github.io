"""Path resolution and site metadata for ActionThinker MCP server."""

import os
from pathlib import Path
import yaml
import json


def resolve_repo_root() -> Path:
    """Find the actionthinker.github.io repo root.

    Resolution order:
    1. ACTIONTHINKER_REPO_PATH env var
    2. Walk up from this file's directory looking for _config.yml
    3. Hard-coded fallbacks for common locations
    """
    env_path = os.environ.get("ACTIONTHINKER_REPO_PATH")
    if env_path:
        p = Path(env_path)
        if (p / "_config.yml").exists():
            return p.resolve()

    here = Path(__file__).resolve().parent
    for parent in [here] + list(here.parents):
        if (parent / "_config.yml").exists():
            return parent

    fallbacks = [
        Path("D:/OPC/actionthinker.github.io"),
    ]
    for p in fallbacks:
        if (p / "_config.yml").exists():
            return p

    raise FileNotFoundError(
        "Cannot find actionthinker.com repo root. "
        "Set ACTIONTHINKER_REPO_PATH environment variable to the repo path."
    )


def load_site_config(repo_root: Path) -> dict:
    """Load site metadata from _config.yml."""
    config_path = repo_root / "_config.yml"
    if not config_path.exists():
        return {"url": "http://ActionThinker.com", "title": "ActionThinker", "description": ""}

    with open(config_path, "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)

    return {
        "url": config.get("url", "http://ActionThinker.com").rstrip("/"),
        "title": config.get("title", "ActionThinker"),
        "description": config.get("description", ""),
        "author_name": config.get("author", {}).get("name", "陈露"),
        "author_email": config.get("author", {}).get("email", "chenlu@opclab.cn"),
    }


# Mapping from logical page names to HTML files
PAGE_MAP = {
    "about": "about.html",
    "service": "service.html",
    "enterprise-ai": "enterprise-ai.html",
    "enterprise-consulting": "enterprise-consulting.html",
    "enterprise-ai-training": "enterprise-ai-training.html",
    "personal-brand": "personal-brand.html",
    "knowledge-assetization": "knowledge-assetization.html",
    "opclab": "opclab.html",
    "self-check": "self-check.html",
    "diagnostic": "diagnostic.html",
    "faq": "faq.html",
}

# Pages that get_page() can serve
PAGE_WHITELIST = set(PAGE_MAP.keys()) | set(PAGE_MAP.values())


def get_contact_info(site_config: dict) -> dict:
    return {
        "email": site_config.get("author_email", "chenlu@opclab.cn"),
        "wechat": "ActionThinker",
        "github": "https://github.com/ActionThinker",
        "linkedin": "https://linkedin.com/in/chenluaihr",
    }
