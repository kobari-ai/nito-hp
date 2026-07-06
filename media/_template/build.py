#!/usr/bin/env python3
"""nito media ビルドスクリプト

media/posts/*.md を読み込み、記事HTML（media/<slug>/index.html）と
一覧ページ（media/index.html）を生成する。

使い方:
    python3 media/_template/build.py

必要パッケージ: markdown  (pip install markdown)

mdファイルの形式:
    ---
    title: 記事タイトル
    date: 2026-07-06
    category: AI検索対策
    description: メタディスクリプション（120字目安）
    image: /media/images/xxx.png   ← 任意（アイキャッチ）
    author: 岡村 希一               ← 任意（省略時デフォルト）
    ---

    導入文（最初のh2より前がリード文になる）

    ## 見出し
    本文 **強調はマーカー表示になる**

    :::point
    ポイント枠の中身
    :::
"""

import html
import re
import sys
from datetime import date
from pathlib import Path

import markdown

ROOT = Path(__file__).resolve().parent.parent  # media/
TEMPLATE_DIR = ROOT / "_template"
POSTS_DIR = ROOT / "posts"

DEFAULT_AUTHOR = "岡村 希一"
DEFAULT_AUTHOR_BIO = (
    "nito / マーケティング。「いいモノが自然に広まる仕組み」をテーマに、"
    "AI検索対策とブランド戦略の領域で企業の成長を支援している。"
)
DEFAULT_AUTHOR_IMAGE = "/profile_okamura.png"

AUTHORS = {
    "岡村 希一": {"bio": DEFAULT_AUTHOR_BIO, "image": "/profile_okamura.png"},
    # 著者を増やす場合はここに追記
}


def parse_front_matter(text: str):
    """front matter (--- ... ---) と本文を分離する"""
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    if not m:
        raise ValueError("front matter (--- で囲むメタ情報) がありません")
    meta = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            key, _, val = line.partition(":")
            meta[key.strip()] = val.strip().strip('"').strip("'")
    body = text[m.end():]
    required = ["title", "date", "category", "description"]
    missing = [k for k in required if not meta.get(k)]
    if missing:
        raise ValueError(f"front matter に {missing} がありません")
    return meta, body


def convert_point_blocks(md_text: str) -> str:
    """:::point 〜 ::: をPOINT枠HTMLに変換する"""
    def repl(m):
        inner = markdown.markdown(m.group(1).strip(), extensions=["tables", "sane_lists"])
        return (
            '<div class="box-point">'
            '<span class="box-point__ttl">POINT</span>'
            f'<div class="box-point__body">{inner}</div>'
            "</div>"
        )

    return re.sub(r"^:::point\s*\n(.*?)\n:::\s*$", repl, md_text, flags=re.DOTALL | re.MULTILINE)


def add_heading_ids_and_toc(body_html: str):
    """h2/h3にid付与し、目次HTMLを生成する"""
    toc_items = []
    counters = {"h2": 0}

    def repl(m):
        tag, inner = m.group(1), m.group(2)
        if tag == "h2":
            counters["h2"] += 1
            hid = f"s{counters['h2']}"
            toc_items.append((2, hid, re.sub(r"<[^>]+>", "", inner)))
        else:
            hid = f"s{counters['h2']}-{sum(1 for t in toc_items if t[0] == 3 and t[1].startswith('s' + str(counters['h2']) + '-')) + 1}"
            toc_items.append((3, hid, re.sub(r"<[^>]+>", "", inner)))
        return f'<{tag} id="{hid}">{inner}</{tag}>'

    body_html = re.sub(r"<(h[23])>(.*?)</\1>", repl, body_html, flags=re.DOTALL)

    if not toc_items:
        return body_html, ""

    lis = []
    for level, hid, text in toc_items:
        cls = ' class="toc-h3"' if level == 3 else ""
        lis.append(f'                    <li{cls}><a href="#{hid}">{text}</a></li>')
    toc_html = (
        '            <nav class="toc">\n'
        '                <div class="toc__ttl">目次</div>\n'
        "                <ol>\n" + "\n".join(lis) + "\n                </ol>\n"
        "            </nav>"
    )
    return body_html, toc_html


def split_lead(body_html: str):
    """最初のh2より前をリード文として分離する"""
    idx = body_html.find("<h2")
    if idx == -1:
        return "", body_html
    return body_html[:idx].strip(), body_html[idx:].strip()


def eyecatch_html(meta) -> str:
    img = meta.get("image", "")
    if img:
        return f'<div class="post-eyecatch"><img src="{html.escape(img)}" alt="{html.escape(meta["title"])}"></div>'
    return '<div class="post-eyecatch">nito Column</div>'


def thumb_style(meta) -> str:
    img = meta.get("image", "")
    return f' style="background-image:url(\'{html.escape(img)}\')"' if img else ""


def related_cards(current_slug, posts) -> str:
    """関連記事: 同カテゴリ優先で最新3件"""
    current = next(p for p in posts if p["slug"] == current_slug)
    others = [p for p in posts if p["slug"] != current_slug]
    same_cat = [p for p in others if p["meta"]["category"] == current["meta"]["category"]]
    rest = [p for p in others if p not in same_cat]
    picks = (same_cat + rest)[:3]
    cards = []
    for p in picks:
        m = p["meta"]
        thumb_inner = "" if m.get("image") else "nito Column"
        cards.append(
            f'            <a href="/media/{p["slug"]}/" class="rel-card">\n'
            f'                <div class="rel-card__thumb"{thumb_style(m)}>{thumb_inner}</div>\n'
            f'                <div class="rel-card__date">{m["date"].replace("-", ".")}</div>\n'
            f'                <div class="rel-card__ttl">{html.escape(m["title"])}</div>\n'
            "            </a>"
        )
    return "\n".join(cards)


def build_article(post, posts, template: str) -> str:
    meta = post["meta"]
    author = meta.get("author", DEFAULT_AUTHOR)
    profile = AUTHORS.get(author, {"bio": DEFAULT_AUTHOR_BIO, "image": DEFAULT_AUTHOR_IMAGE})

    title_short = meta["title"][:20] + ("…" if len(meta["title"]) > 20 else "")

    out = template
    replacements = {
        "{{TITLE}}": html.escape(meta["title"]),
        "{{TITLE_SHORT}}": html.escape(title_short),
        "{{DESCRIPTION}}": html.escape(meta["description"]),
        "{{SLUG}}": post["slug"],
        "{{CATEGORY}}": html.escape(meta["category"]),
        "{{DATE}}": meta["date"].replace("-", "."),
        "{{EYECATCH}}": eyecatch_html(meta),
        "{{LEAD}}": post["lead"],
        "{{TOC}}": post["toc"],
        "{{BODY}}": post["body"],
        "{{RELATED}}": related_cards(post["slug"], posts),
        "{{AUTHOR}}": html.escape(author),
        "{{AUTHOR_BIO}}": html.escape(profile["bio"]),
        "{{AUTHOR_IMAGE}}": profile["image"],
    }
    for key, val in replacements.items():
        out = out.replace(key, val)
    return out


def build_list(posts, template: str) -> str:
    cats = []
    for p in posts:
        c = p["meta"]["category"]
        if c not in cats:
            cats.append(c)

    cat_links = ['        <a href="#" data-cat="all" class="is-active">すべて</a>']
    for c in cats:
        cat_links.append(f'        <a href="#" data-cat="{html.escape(c)}">{html.escape(c)}</a>')

    cards = []
    for p in posts:
        m = p["meta"]
        thumb_inner = "" if m.get("image") else "nito Column"
        cards.append(
            f'        <a href="/media/{p["slug"]}/" class="rel-card" data-cat="{html.escape(m["category"])}">\n'
            f'            <div class="rel-card__thumb"{thumb_style(m)}>{thumb_inner}</div>\n'
            f'            <div class="rel-card__date">{m["date"].replace("-", ".")} ・ {html.escape(m["category"])}</div>\n'
            f'            <div class="rel-card__ttl">{html.escape(m["title"])}</div>\n'
            "        </a>"
        )

    out = template
    out = out.replace("{{CATEGORIES}}", "\n".join(cat_links))
    out = out.replace("{{POSTS}}", "\n".join(cards))
    return out


def main():
    article_tpl = (TEMPLATE_DIR / "article.html").read_text(encoding="utf-8")
    list_tpl = (TEMPLATE_DIR / "list.html").read_text(encoding="utf-8")

    md_files = sorted(POSTS_DIR.glob("*.md"))

    posts = []
    errors = []
    for f in md_files:
        try:
            meta, body_md = parse_front_matter(f.read_text(encoding="utf-8"))
            date.fromisoformat(meta["date"])  # 形式チェック
        except ValueError as e:
            errors.append(f"{f.name}: {e}")
            continue
        body_md = convert_point_blocks(body_md)
        body_html = markdown.markdown(body_md, extensions=["tables", "sane_lists"])
        body_html, toc = add_heading_ids_and_toc(body_html)
        lead, body_html = split_lead(body_html)
        posts.append({
            "slug": f.stem,
            "meta": meta,
            "lead": lead,
            "toc": toc,
            "body": body_html,
        })

    if errors:
        print("エラーのあった記事（スキップ）:", file=sys.stderr)
        for e in errors:
            print(f"  - {e}", file=sys.stderr)

    # 新しい順
    posts.sort(key=lambda p: p["meta"]["date"], reverse=True)

    for p in posts:
        out_dir = ROOT / p["slug"]
        out_dir.mkdir(exist_ok=True)
        (out_dir / "index.html").write_text(build_article(p, posts, article_tpl), encoding="utf-8")
        print(f"✔ media/{p['slug']}/index.html")

    (ROOT / "index.html").write_text(build_list(posts, list_tpl), encoding="utf-8")
    print("✔ media/index.html （一覧）")

    # mdが削除された記事のディレクトリを掃除（非公開化に対応）
    keep = {p["slug"] for p in posts} | {"_template", "posts", "images"}
    for d in ROOT.iterdir():
        if d.is_dir() and d.name not in keep and (d / "index.html").exists():
            import shutil
            shutil.rmtree(d)
            print(f"✘ media/{d.name}/ を削除（対応するmdなし）")

    print(f"\n完了: {len(posts)}記事")

    if errors:
        sys.exit(1)


if __name__ == "__main__":
    main()
