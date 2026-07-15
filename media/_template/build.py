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
DEFAULT_AUTHOR_ROLE = "nito代表 / AI検索対策（LLMO）コンサルタント"
DEFAULT_AUTHOR_BIO = (
    "AI検索対策（LLMO）を中心に、マーケティング戦略から実行まで幅広く経験。"
    "サイバーエージェントで培ったデジタルマーケティングや、株式会社刀の戦略設計を武器に、"
    "「いいモノが自然に広まる仕組みづくり」を支援。"
)
DEFAULT_AUTHOR_IMAGE = "/profile_okamura.jpg"

AUTHORS = {
    "岡村 希一": {"role": DEFAULT_AUTHOR_ROLE, "bio": DEFAULT_AUTHOR_BIO, "image": "/profile_okamura.jpg"},
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


def convert_takeaways_blocks(md_text: str) -> str:
    """:::takeaways 〜 ::: を「この記事のポイント」ボックスに変換する（Key Takeaways用）"""
    def repl(m):
        inner = markdown.markdown(m.group(1).strip(), extensions=["sane_lists"])
        return (
            '<div class="takeaways">'
            '<div class="takeaways__ttl">この記事のポイント</div>'
            f'<div class="takeaways__body">{inner}</div>'
            "</div>"
        )

    return re.sub(r"^:::takeaways\s*\n(.*?)\n:::\s*$", repl, md_text, flags=re.DOTALL | re.MULTILINE)


def convert_linkcard_blocks(md_text: str, meta_by_slug: dict) -> str:
    """:::linkcard 〜 ::: を内部リンクの案内カードHTMLに変換する。
    中身は url: / title: / desc: のkey:value形式（descは省略可）。
    urlのslugが分かれば、そのページのアイキャッチをサムネイルとして表示する。"""
    def repl(m):
        fields = {}
        for line in m.group(1).strip().splitlines():
            if ":" in line:
                key, _, val = line.partition(":")
                fields[key.strip()] = val.strip()
        url_raw = fields.get("url", "#")
        url = html.escape(url_raw)
        title = html.escape(fields.get("title", ""))
        desc = html.escape(fields.get("desc", ""))
        desc_html = f'<div class="in-link-card__desc">{desc}</div>' if desc else ""
        slug = url_raw.strip("/").split("/")[-1]
        target_meta = meta_by_slug.get(slug)
        thumb_html = card_thumb(target_meta, cls="in-link-card__thumb") if target_meta else ""
        return (
            '<div class="in-link-card">'
            f'<a href="{url}">'
            f'{thumb_html}'
            '<div class="in-link-card__body">'
            '<div class="in-link-card__eyebrow">✓ あわせて読みたい</div>'
            f'<div class="in-link-card__ttl">{title}</div>'
            f'{desc_html}'
            "</div></a></div>"
        )

    return re.sub(r"^:::linkcard\s*\n(.*?)\n:::\s*$", repl, md_text, flags=re.DOTALL | re.MULTILINE)


def expand_blogparts(body_html: str) -> str:
    """[blogparts:NAME] を _template/blogparts/NAME.html の中身に置換する。
    共通PRパートを1ファイルで管理し、更新すれば全記事に反映される。
    markdownが <p>[blogparts:NAME]</p> と段落化するので、その形も受ける。"""
    def repl(m):
        name = m.group(1).strip()
        part = TEMPLATE_DIR / "blogparts" / f"{name}.html"
        if not part.exists():
            raise ValueError(f"ブログパーツ blogparts/{name}.html が見つかりません")
        return part.read_text(encoding="utf-8").strip()

    # 1パスで置換する（re.subは挿入した内容を再スキャンしないので、
    # パーツ内に別トークンがあっても二重展開されない）。任意で <p> ラッパを飲み込む。
    pattern = r"(?:<p>\s*)?\[blogparts:([a-z0-9\-_]+)\](?:\s*</p>)?"
    return re.sub(pattern, repl, body_html)


def add_heading_ids_and_toc(body_html: str):
    """h2/h3にid付与し、目次HTMLを生成する"""
    toc_items = []
    counters = {"h2": 0}
    state = {"in_faq": False}  # FAQ配下のH3は目次に載せない

    def repl(m):
        tag, inner = m.group(1), m.group(2)
        text = re.sub(r"<[^>]+>", "", inner)
        if tag == "h2":
            counters["h2"] += 1
            hid = f"s{counters['h2']}"
            state["in_faq"] = "よくある質問" in text
            toc_items.append((2, hid, text))
        else:
            h3n = sum(1 for t in toc_items if t[0] == 3 and t[1].startswith(f"s{counters['h2']}-")) + 1
            hid = f"s{counters['h2']}-{h3n}"
            # FAQの質問は目次に出さない（見出しidは付与して本文アンカーは残す）
            toc_items.append((3, hid, text, state["in_faq"]))
        return f'<{tag} id="{hid}">{inner}</{tag}>'

    body_html = re.sub(r"<(h[23])>(.*?)</\1>", repl, body_html, flags=re.DOTALL)

    if not toc_items:
        return body_html, ""

    lis = []
    for item in toc_items:
        level, hid, text = item[0], item[1], item[2]
        in_faq = item[3] if len(item) > 3 else False
        if in_faq:
            continue  # FAQの質問は目次から除外
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


def cover_texts(meta):
    """アイキャッチ用の文言。front matterで指定、無ければタイトルにフォールバック。
    cover_headline: 目立たせる短いフレーズ（タイトルそのままにしない）
    cover_sub:      補足の一行（任意）
    cover_tag:      吹き出しタグ（任意・既定はカテゴリ）"""
    headline = meta.get("cover_headline") or meta["title"]
    sub = meta.get("cover_sub", "")
    tag = meta.get("cover_tag") or meta["category"]
    return headline, sub, tag


def eyecatch_html(meta) -> str:
    """アイキャッチ。image指定があれば写真、なければブランド固定デザイン（文言だけ差し替え）。"""
    img = meta.get("image", "")
    if img:
        return f'<div class="post-eyecatch"><img src="{html.escape(img)}" alt="{html.escape(meta["title"])}"></div>'
    headline, sub, tag = cover_texts(meta)
    sub_html = f'<span class="ec-sub">{html.escape(sub)}</span>' if sub else ""
    return (
        '<div class="post-eyecatch post-eyecatch--designed">'
        '<div class="ec-frame">'
        f'<span class="ec-tag">{html.escape(tag)}</span>'
        f'<span class="ec-headline">{html.escape(headline)}</span>'
        f'{sub_html}'
        '<span class="ec-brand">nito</span>'
        "</div></div>"
    )


def card_thumb(meta, cls="rel-card__thumb") -> str:
    """カードのサムネイル。image指定があれば写真、なければ固定デザイン（headlineだけ表示）。"""
    img = meta.get("image", "")
    if img:
        return f'<div class="{cls}" style="background-image:url(\'{html.escape(img)}\')"></div>'
    headline, _sub, tag = cover_texts(meta)
    return (
        f'<div class="{cls} card-thumb--designed">'
        '<div class="ec-frame ec-frame--mini">'
        f'<span class="ec-tag">{html.escape(tag)}</span>'
        f'<span class="ec-headline">{html.escape(headline)}</span>'
        '<span class="ec-brand">nito</span>'
        "</div></div>"
    )


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
        cards.append(
            f'            <a href="/media/{p["slug"]}/" class="rel-card">\n'
            f'                {card_thumb(m)}\n'
            f'                <div class="rel-card__date">{m["date"].replace("-", ".")}</div>\n'
            f'                <div class="rel-card__ttl">{html.escape(m["title"])}</div>\n'
            "            </a>"
        )
    return "\n".join(cards)


def extract_faq(body_md: str):
    """本文mdの「## よくある質問」配下の ### Q. 〜 と回答を(質問, 回答)で返す。"""
    faqs = []
    lines = body_md.splitlines()
    in_faq = False
    q = None
    ans = []
    for line in lines:
        if line.startswith("## "):
            in_faq = "よくある質問" in line
            if q:
                faqs.append((q, " ".join(ans).strip())); q, ans = None, []
            continue
        if not in_faq:
            continue
        if line.startswith("### "):
            if q:
                faqs.append((q, " ".join(ans).strip())); ans = []
            q = re.sub(r"^###\s*(Q\.?\s*)?", "", line).strip()
        elif q is not None and line.strip():
            ans.append(line.strip())
    if q:
        faqs.append((q, " ".join(ans).strip()))
    return [(q, a) for q, a in faqs if q and a]


def build_jsonld(post) -> str:
    """記事ページ用のJSON-LD（Article / FAQPage / BreadcrumbList）を生成する。"""
    import json as _json
    meta = post["meta"]
    url = f"{SITE}/media/{post['slug']}/"
    publisher = {"@type": "Organization", "name": "nito", "url": f"{SITE}/"}
    author_name = meta.get("author", DEFAULT_AUTHOR)
    author_profile = AUTHORS.get(author_name, {"role": DEFAULT_AUTHOR_ROLE, "bio": DEFAULT_AUTHOR_BIO})
    author_person = {
        "@type": "Person",
        "name": author_name,
        "jobTitle": author_profile.get("role", DEFAULT_AUTHOR_ROLE),
        "description": author_profile["bio"],
        "worksFor": publisher,
    }

    article = {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": meta["title"],
        "description": meta["description"],
        "datePublished": meta["date"],
        "dateModified": meta["date"],
        "author": author_person,
        "publisher": publisher,
        "mainEntityOfPage": {"@type": "WebPage", "@id": url},
        "articleSection": meta["category"],
        "inLanguage": "ja",
    }
    if meta.get("image"):
        article["image"] = meta["image"] if meta["image"].startswith("http") else SITE + meta["image"]

    breadcrumb = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "ホーム", "item": f"{SITE}/"},
            {"@type": "ListItem", "position": 2, "name": "コラム", "item": f"{SITE}/media/"},
            {"@type": "ListItem", "position": 3, "name": meta["title"]},
        ],
    }

    blocks = [article, breadcrumb]

    faqs = post.get("faqs") or []
    if faqs:
        blocks.append({
            "@context": "https://schema.org",
            "@type": "FAQPage",
            "mainEntity": [
                {"@type": "Question", "name": q,
                 "acceptedAnswer": {"@type": "Answer", "text": a}}
                for q, a in faqs
            ],
        })

    return "\n".join(
        f'<script type="application/ld+json">{_json.dumps(b, ensure_ascii=False)}</script>'
        for b in blocks
    )


def build_article(post, posts, template: str) -> str:
    meta = post["meta"]
    author = meta.get("author", DEFAULT_AUTHOR)
    profile = AUTHORS.get(author, {"role": DEFAULT_AUTHOR_ROLE, "bio": DEFAULT_AUTHOR_BIO, "image": DEFAULT_AUTHOR_IMAGE})

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
        "{{JSONLD}}": build_jsonld(post),
        "{{AUTHOR}}": html.escape(author),
        "{{AUTHOR_ROLE}}": html.escape(profile.get("role", DEFAULT_AUTHOR_ROLE)),
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
        cards.append(
            f'        <a href="/media/{p["slug"]}/" class="rel-card" data-cat="{html.escape(m["category"])}">\n'
            f'            {card_thumb(m)}\n'
            f'            <div class="rel-card__date">{m["date"].replace("-", ".")} ・ {html.escape(m["category"])}</div>\n'
            f'            <div class="rel-card__ttl">{html.escape(m["title"])}</div>\n'
            "        </a>"
        )

    out = template
    out = out.replace("{{CATEGORIES}}", "\n".join(cat_links))
    out = out.replace("{{POSTS}}", "\n".join(cards))
    return out


def update_top_page(posts):
    """トップページの COLUMN マーカー間に最新3記事を挿入する（0件なら空にする）"""
    top = ROOT.parent / "index.html"
    if not top.exists():
        return
    s = top.read_text(encoding="utf-8")
    start_mark = "<!-- COLUMN:START 最新記事はbuild.pyが自動挿入（手で編集しない） -->"
    end_mark = "<!-- COLUMN:END -->"
    if start_mark not in s or end_mark not in s:
        return

    if posts:
        rows = []
        for p in posts[:3]:
            m = p["meta"]
            rows.append(
                f'                <a href="/media/{p["slug"]}/" class="news-row">\n'
                f'                    <span class="news-date">{m["date"].replace("-", ".")}</span>\n'
                f'                    <span class="news-cat">{html.escape(m["category"])}</span>\n'
                f'                    <span class="news-ttl">{html.escape(m["title"])}</span>\n'
                '                    <span class="news-arrow">→</span>\n'
                "                </a>"
            )
        section = (
            '\n    <div class="divider"></div>\n\n'
            '    <div class="container">\n'
            '        <!-- Column Section -->\n'
            '        <section id="column" class="section">\n'
            '            <div class="section-header ani-show-up">\n'
            '                <div class="sec-subtitle">コラム</div>\n'
            '                <h2 class="sec-title">Column</h2>\n'
            "            </div>\n"
            '            <div class="news-list ani-fade-bottom">\n'
            + "\n".join(rows) + "\n"
            "            </div>\n"
            '            <p class="news-more"><a href="/media/" class="btn-more">コラム一覧へ</a></p>\n'
            "        </section>\n"
            "    </div>\n    "
        )
    else:
        section = "\n    "

    before = s[: s.index(start_mark) + len(start_mark)]
    after = s[s.index(end_mark):]
    top.write_text(before + section + after, encoding="utf-8")
    print(f"✔ index.html （トップのコラム欄: {min(len(posts), 3)}件）")


SITE = "https://nito-0210.com"
# サイトマップに含める固定ページ（トップ・サービス・コラム一覧・問い合わせ・プライバシー）
STATIC_PAGES = ["/", "/llmo/", "/media/", "/contact.html", "/privacy.html"]


def generate_sitemap(posts):
    """リポジトリ直下に sitemap.xml を生成する（固定ページ＋全記事）。"""
    root = ROOT.parent
    today = date.today().isoformat()
    urls = []
    for path in STATIC_PAGES:
        urls.append((f"{SITE}{path}", today))
    for p in posts:
        urls.append((f"{SITE}/media/{p['slug']}/", p["meta"]["date"]))

    lines = ['<?xml version="1.0" encoding="UTF-8"?>',
             '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for loc, lastmod in urls:
        lines.append(f"  <url><loc>{loc}</loc><lastmod>{lastmod}</lastmod></url>")
    lines.append("</urlset>")
    (root / "sitemap.xml").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"✔ sitemap.xml （{len(urls)}URL）")


def main():
    article_tpl = (TEMPLATE_DIR / "article.html").read_text(encoding="utf-8")
    list_tpl = (TEMPLATE_DIR / "list.html").read_text(encoding="utf-8")

    md_files = sorted(POSTS_DIR.glob("*.md"))

    # linkcard用: 全記事のfront matterを先読みしてslug→metaの対応を作る
    meta_by_slug = {}
    for f in md_files:
        try:
            meta, _ = parse_front_matter(f.read_text(encoding="utf-8"))
            meta_by_slug[f.stem] = meta
        except ValueError:
            continue

    posts = []
    errors = []
    for f in md_files:
        try:
            meta, body_md = parse_front_matter(f.read_text(encoding="utf-8"))
            date.fromisoformat(meta["date"])  # 形式チェック
        except ValueError as e:
            errors.append(f"{f.name}: {e}")
            continue
        faqs = extract_faq(body_md)
        body_md = convert_takeaways_blocks(body_md)
        body_md = convert_point_blocks(body_md)
        body_md = convert_linkcard_blocks(body_md, meta_by_slug)
        body_html = markdown.markdown(body_md, extensions=["tables", "sane_lists"])
        body_html = expand_blogparts(body_html)
        body_html, toc = add_heading_ids_and_toc(body_html)
        lead, body_html = split_lead(body_html)
        posts.append({
            "slug": f.stem,
            "meta": meta,
            "lead": lead,
            "toc": toc,
            "body": body_html,
            "faqs": faqs,
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

    update_top_page(posts)
    generate_sitemap(posts)

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
