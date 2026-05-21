#!/usr/bin/env python3
"""
Action Thinker — WeChat Official Account article sync.
用法: python sync-to-wechat.py <html-template-file>

从 HTML 模板文件直接推送到公众号草稿箱。
模板中的 <style> 块会保留为微信内联样式。
"""

import json, os, re, sys, time, urllib.request, urllib.error
from pathlib import Path

APPID = "wx78c3e464f4b0f0b9"
APPSECRET = "286a9c8234e9374536dccae2d0dafe19"

WECHAT_BASE = "https://api.weixin.qq.com/cgi-bin"


def get_token():
    url = f"{WECHAT_BASE}/token?grant_type=client_credential&appid={APPID}&secret={APPSECRET}"
    resp = json.loads(urllib.request.urlopen(url).read())
    if "access_token" not in resp:
        raise Exception(f"Token error: {resp}")
    return resp["access_token"]


def _api_post(token, endpoint, payload):
    """POST JSON to WeChat API, return parsed response."""
    data = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    url = f"{WECHAT_BASE}/{endpoint}?access_token={token}"
    req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"})
    try:
        return json.loads(urllib.request.urlopen(req).read())
    except urllib.error.HTTPError as e:
        return json.loads(e.read())


def upload_permanent_image(token, filepath):
    """Upload image as permanent material, return media_id or None."""
    filename = os.path.basename(filepath)
    ext = filename.rsplit(".", 1)[-1].lower()
    mime_map = {"jpg": "image/jpeg", "jpeg": "image/jpeg", "png": "image/png", "gif": "image/gif"}
    content_type = mime_map.get(ext, "image/png")

    with open(filepath, "rb") as f:
        img_data = f.read()

    boundary = "----WX" + str(int(time.time() * 1000))
    body = (
        f"--{boundary}\r\n"
        f'Content-Disposition: form-data; name="media"; filename="{filename}"\r\n'
        f"Content-Type: {content_type}\r\n\r\n"
    ).encode() + img_data + f"\r\n--{boundary}--\r\n".encode()

    url = f"{WECHAT_BASE}/material/add_material?access_token={token}&type=image"
    req = urllib.request.Request(url, data=body)
    req.add_header("Content-Type", f"multipart/form-data; boundary={boundary}")
    resp = json.loads(urllib.request.urlopen(req).read())
    return resp.get("media_id")


def upload_content_image(token, filepath):
    """Upload image for in-article use (returns url), or None."""
    filename = os.path.basename(filepath)
    ext = filename.rsplit(".", 1)[-1].lower()
    mime_map = {"jpg": "image/jpeg", "jpeg": "image/jpeg", "png": "image/png", "gif": "image/gif"}
    content_type = mime_map.get(ext, "image/png")

    with open(filepath, "rb") as f:
        img_data = f.read()

    boundary = "----WX" + str(int(time.time() * 1000))
    body = (
        f"--{boundary}\r\n"
        f'Content-Disposition: form-data; name="media"; filename="{filename}"\r\n'
        f"Content-Type: {content_type}\r\n\r\n"
    ).encode() + img_data + f"\r\n--{boundary}--\r\n".encode()

    url = f"{WECHAT_BASE}/media/uploadimg?access_token={token}"
    req = urllib.request.Request(url, data=body)
    req.add_header("Content-Type", f"multipart/form-data; boundary={boundary}")
    resp = json.loads(urllib.request.urlopen(req).read())
    return resp.get("url")


def generate_cover_image(title, subtitle, output_path):
    """Generate a magazine-style cover PNG. Returns path or None."""
    try:
        from PIL import Image, ImageDraw, ImageFont
    except ImportError:
        return None

    w, h = 900, 500
    img = Image.new("RGB", (w, h), (26, 26, 46))

    # Accent bar
    draw = ImageDraw.Draw(img)
    draw.rectangle([(0, 0), (w, 6)], fill=(233, 69, 96))

    # Font
    font_paths = [
        "C:/Windows/Fonts/msyh.ttc",
        "C:/Windows/Fonts/simhei.ttf",
    ]
    title_font = None
    sub_font = None
    for fp in font_paths:
        if os.path.exists(fp):
            try:
                title_font = ImageFont.truetype(fp, 44)
                sub_font = ImageFont.truetype(fp, 22)
                break
            except Exception:
                pass

    if title_font is None:
        title_font = ImageFont.load_default()
        sub_font = ImageFont.load_default()

    # Title wrapping
    max_w = 800
    wrapped = []
    for line in title.replace("？", "?\n").replace("，", ",\n").replace("。", ".\n").split("\n"):
        line = line.strip()
        if not line:
            continue
        if title_font.getbbox(line)[2] <= max_w:
            wrapped.append(line)
        else:
            current = ""
            for char in line:
                if title_font.getbbox(current + char)[2] > max_w:
                    wrapped.append(current)
                    current = char
                else:
                    current += char
            if current:
                wrapped.append(current)

    y = 140
    for line in wrapped[:3]:
        bbox = title_font.getbbox(line)
        x = (w - bbox[2]) // 2
        draw.text((x, y), line, fill=(255, 255, 255), font=title_font)
        y += 60

    # Subtitle
    if sub_font:
        sub = subtitle[:40] + ("..." if len(subtitle) > 40 else "")
        bbox = sub_font.getbbox(sub)
        x = (w - bbox[2]) // 2
        draw.text((x, y + 16), sub, fill=(160, 160, 170), font=sub_font)

    # Brand
    try:
        brand_font = ImageFont.truetype(font_paths[0], 16)
        brand = "ACTION THINKER"
        bbox = brand_font.getbbox(brand)
        draw.text(((w - bbox[2]) // 2, h - 48), brand, fill=(120, 120, 130), font=brand_font)
    except Exception:
        pass

    img.save(output_path, "PNG")
    return output_path


def extract_meta(html_content):
    """Extract title and digest from HTML template."""
    title_m = re.search(r'<h1[^>]*class="at-title"[^>]*>(.*?)</h1>', html_content, re.DOTALL)
    title = re.sub(r'<[^>]+>', '', title_m.group(1)).strip() if title_m else "ActionThinker"

    dek_m = re.search(r'<p[^>]*class="at-dek"[^>]*>(.*?)</p>', html_content, re.DOTALL)
    digest = re.sub(r'<[^>]+>', '', dek_m.group(1)).strip() if dek_m else title[:100]

    # Clean up title — remove <br> tags
    title = re.sub(r'<br\s*/?>', ' ', title).strip()
    return title, digest


def create_draft(token, title, author, digest, content_html, source_url, thumb_media_id=None):
    """Create WeChat draft. Returns media_id or None."""
    article = {
        "title": title,
        "author": author,
        "digest": (digest or title)[:120],
        "content": content_html,
        "content_source_url": source_url,
        "need_open_comment": 1,
        "only_fans_can_comment": 0,
    }
    if thumb_media_id:
        article["thumb_media_id"] = thumb_media_id

    resp = _api_post(token, "draft/add", {"articles": [article]})
    if resp.get("media_id"):
        return resp["media_id"]
    print(f"  Draft error: {resp}", file=sys.stderr)
    return None


def clean_test_drafts(token):
    """Remove test drafts from debugging sessions."""
    import urllib.request as ur
    # Get draft list
    payload = json.dumps({"offset": 0, "count": 20, "no_content": 1}, ensure_ascii=False).encode('utf-8')
    req = ur.Request(f"{WECHAT_BASE}/draft/batchget?access_token={token}", data=payload, headers={"Content-Type": "application/json"})
    resp = json.loads(ur.urlopen(req).read())
    test_ids = []
    for item in resp.get("item", []):
        media_id = item.get("media_id", "")
        title = item.get("content", {}).get("news_item", [{}])[0].get("title", "")
        # Remove our test drafts
        if title in ("Test", "T", "Test Full Article", "Test First Half", "Test Second Half",
                     "Tag Test Article", "More Tag Tests", "Section Tag Test",
                     "Trunc 3000 test", "Trunc 3500 test", "Trunc 3800 test",
                     "Chunk 1 of second half", "Chunk 2 of second half",
                     "Chunk 3 of second half", "Chunk 4 of second half", "S3100", "S3250", "S3400"):
            test_ids.append(media_id)
    for mid in test_ids:
        payload = json.dumps({"media_id": mid}).encode('utf-8')
        req = ur.Request(f"{WECHAT_BASE}/draft/delete?access_token={token}", data=payload, headers={"Content-Type": "application/json"})
        ur.urlopen(req)
        print(f"  Deleted test draft: {mid}")
    return len(test_ids)


def main():
    if len(sys.argv) < 2:
        print(f"用法: python {sys.argv[0]} <wechat-html-template>")
        print(f"示例: python {sys.argv[0]} wechat-template.html")
        sys.exit(1)

    template_path = sys.argv[1]
    if not os.path.exists(template_path):
        print(f"文件不存在: {template_path}")
        sys.exit(1)

    with open(template_path, "r", encoding="utf-8") as f:
        html_content = f.read()

    title, digest = extract_meta(html_content)
    author = "ActionThinker"
    source_url = "https://actionthinker.com"

    print(f"同步到公众号草稿箱")
    print(f"  标题: {title}")
    print(f"  摘要: {digest[:60]}...")
    print(f"  HTML: {len(html_content)} chars, {len(html_content.encode('utf-8'))} bytes")

    # Get token
    print("  获取 access_token...")
    try:
        token = get_token()
    except Exception as e:
        print(f"  Token 获取失败: {e}")
        sys.exit(1)

    # Clean test drafts from debugging
    n = clean_test_drafts(token)
    if n:
        print(f"  清理了 {n} 个测试草稿")

    # Generate cover image
    cover_path = os.path.join(os.path.dirname(os.path.abspath(template_path)) or ".", "_wechat_cover.png")
    cover_id = None
    if generate_cover_image(title, digest, cover_path):
        print("  上传封面图...")
        cover_id = upload_permanent_image(token, cover_path)
        if cover_id:
            print(f"  封面 media_id: {cover_id}")
        os.remove(cover_path)
    else:
        print("  封面生成跳过 (PIL不可用)")

    # Create draft
    print("  创建草稿...")
    media_id = create_draft(token, title, author, digest, html_content, source_url, cover_id)

    if media_id:
        print(f"\n  草稿创建成功!")
        print(f"  media_id: {media_id}")
        print(f"  登录 mp.weixin.qq.com → 草稿箱 → 预览 → 发布")
    else:
        print(f"\n  草稿创建失败。请检查错误信息。")
        sys.exit(1)


if __name__ == "__main__":
    main()
