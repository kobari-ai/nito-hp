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

import hashlib
import html
import math
import re
import sys
from datetime import date
from pathlib import Path

import markdown

ROOT = Path(__file__).resolve().parent.parent  # media/
TEMPLATE_DIR = ROOT / "_template"
POSTS_DIR = ROOT / "posts"

DEFAULT_AUTHOR = "岡村 希一"
DEFAULT_AUTHOR_ROLE = "nito代表"
DEFAULT_AUTHOR_BIO = (
    "サイバーエージェントで広告の新規事業開発、株式会社刀の選抜型マーケティングプログラムを経て nito を設立。"
    "累計300本以上のWeb記事の企画・執筆・効果測定を担当し、AI検索対策では支援開始3か月でAI経由のコンバージョンを3.8倍にした実績を持つ。"
    "自社の運営にAIエージェントを組み込んでおり、その仕組みを他社に移植するAIエージェント構築支援も行う。"
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


def convert_linkcard_blocks(md_text: str) -> str:
    """:::linkcard 〜 ::: を内部リンクの案内カードHTMLに変換する（テキストのみ、画像は使わない）。
    中身は url: / title: / desc: のkey:value形式（descは省略可）。"""
    def repl(m):
        fields = {}
        for line in m.group(1).strip().splitlines():
            if ":" in line:
                key, _, val = line.partition(":")
                fields[key.strip()] = val.strip()
        url = html.escape(fields.get("url", "#"))
        title = html.escape(fields.get("title", ""))
        desc = html.escape(fields.get("desc", ""))
        desc_html = f'<div class="in-link-card__desc">{desc}</div>' if desc else ""
        return (
            '<div class="in-link-card">'
            f'<a href="{url}">'
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
        # 番号は id から作る（s3 → 3、s3-2 → 3-2）。上位記事の目次と同じ「1｜」「1-1｜」の形
        num = hid[1:]
        cls = "toc-h3" if level == 3 else "toc-h2"
        lis.append(f'                    <li class="{cls}"><a href="#{hid}"><span class="toc__n">{num}</span>{text}</a></li>')
    # 長い目次は畳んで「もっと見る」。12行を超えたら畳む（実測: 上位記事は目次を10行前後で折り畳む）
    long_cls = " toc--long" if len(lis) > 12 else ""
    more_btn = ('\n                <button type="button" class="toc__more" aria-expanded="false">もっと見る</button>'
                if long_cls else "")
    toc_html = (
        f'            <nav class="toc{long_cls}">\n'
        '                <div class="toc__ttl">目次</div>\n'
        "                <ol>\n" + "\n".join(lis) + "\n                </ol>" + more_btn + "\n"
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


# ===== アイキャッチSVG生成 =====
# 画像を用意しなくても、記事タイトル等から 1200x628(1.91:1) のSVGを自動生成する。
# viewBox固定なので <img>/inline どちらでも比率は絶対に崩れない。
# 文字はSVG座標系に焼くため、端末幅・文字数に依らず一様に拡大縮小される。

def _ec_char_w(ch, fs):
    """SVGユーザー単位での概算文字幅。ASCII等の半角は0.6em、全角(CJK/全角記号)は1.0em。"""
    return fs * (0.6 if ord(ch) < 0x3000 else 1.0)


def _ec_text_w(s, fs):
    return sum(_ec_char_w(ch, fs) for ch in s)


# 行頭に置きたくない文字（句読点・閉じ括弧・小書き・長音など）
_KINSOKU_START = set("、。，．・）」』】〉》〕｝）】！？!?：；ーぁぃぅぇぉっゃゅょゎ…")


def _ec_wrap(s, fs, max_w):
    """max_w以内でバランス折り返し。まず必要な行数nを決め、各行の幅が均等に
    なるように分割する（最後の1文字だけ孤立するのを防ぐ）。さらに禁則処理で
    句読点・閉じ括弧が行頭に来ないよう前行へ送る。"""
    total = _ec_text_w(s, fs)
    if total <= max_w or len(s) <= 1:
        return [s]
    n = max(2, math.ceil(total / max_w))
    target = total / n
    lines, cur, cur_w = [], "", 0.0
    for ch in s:
        cw = _ec_char_w(ch, fs)
        cur += ch
        cur_w += cw
        # 目標幅に達し、かつ残り文字数が残り行数以上あるうちに改行
        if len(lines) < n - 1 and cur_w >= target:
            lines.append(cur)
            cur, cur_w = "", 0.0
    if cur:
        lines.append(cur)
    # 禁則：行頭に来てはいけない文字を前行末へ送る
    for i in range(1, len(lines)):
        while lines[i] and lines[i][0] in _KINSOKU_START:
            lines[i - 1] += lines[i][0]
            lines[i] = lines[i][1:]
    return [ln for ln in lines if ln]


def eyecatch_svg(headline, sub, tag, uid) -> str:
    """1200x628のブランドアイキャッチSVG（インライン）。sub=""ならサブ文言は描画しない。"""
    W, H, cx = 1200, 628, 600
    inner_w = 1000  # 見出しに使える最大幅（枠内padを考慮）
    # 見出しが2行以内に収まる最大フォントサイズを選ぶ（無理なら最小で3行まで）
    lines, fs = None, 44
    for cand in (76, 68, 60, 52, 46):
        wr = _ec_wrap(headline, cand, inner_w)
        if len(wr) <= 2:
            lines, fs = wr, cand
            break
    if lines is None:
        fs = 44
        lines = _ec_wrap(headline, fs, inner_w)[:3]
    lh = fs * 1.34

    tag_fs, sub_fs, brand_fs = 27, 34, 34
    sub_lines = _ec_wrap(sub, sub_fs, 940) if sub else []

    # 縦方向レイアウト（全体を中央寄せ）
    tb = 54          # タグバッジ高さ
    g1, g2, g3 = 30, 30, 36
    pu = 20          # 見出し下線までの余白
    head_h = len(lines) * lh
    sub_h = len(sub_lines) * (sub_fs * 1.4)
    total = tb + g1 + head_h + pu + ((g2 + sub_h) if sub_lines else 0) + g3 + brand_fs
    y = (H - total) / 2

    p = []
    gid = f"ecg-{uid}"
    p.append(f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" '
             f'aria-label="{html.escape(headline)}">')
    p.append(f'<defs><linearGradient id="{gid}" x1="0" y1="0" x2="1" y2="1">'
             '<stop offset="0" stop-color="#ff9f43"/>'
             '<stop offset="0.55" stop-color="#e67e22"/>'
             '<stop offset="1" stop-color="#cf6a12"/></linearGradient></defs>')
    p.append(f'<rect width="{W}" height="{H}" fill="url(#{gid})"/>')
    p.append(f'<rect x="40" y="40" width="{W-80}" height="{H-80}" rx="8" fill="none" '
             'stroke="#ffffff" stroke-opacity="0.55" stroke-width="3"/>')

    fam = "'Noto Sans JP',sans-serif"
    # タグバッジ
    tw = _ec_text_w(tag, tag_fs) + 56
    p.append(f'<rect x="{cx - tw/2:.1f}" y="{y:.1f}" width="{tw:.1f}" height="{tb}" '
             f'rx="{tb/2}" fill="#333333"/>')
    p.append(f'<text x="{cx}" y="{y + tb/2 + tag_fs*0.35:.1f}" text-anchor="middle" '
             f'font-family="{fam}" font-weight="700" font-size="{tag_fs}" fill="#ffffff">'
             f'{html.escape(tag)}</text>')
    y += tb + g1

    # 見出し
    longest = 0.0
    for i, ln in enumerate(lines):
        by = y + fs * 0.82 + i * lh
        p.append(f'<text x="{cx}" y="{by:.1f}" text-anchor="middle" font-family="{fam}" '
                 f'font-weight="700" font-size="{fs}" fill="#ffffff">{html.escape(ln)}</text>')
        longest = max(longest, _ec_text_w(ln, fs))
    y += head_h
    uw = min(longest, inner_w)
    p.append(f'<line x1="{cx - uw/2:.1f}" y1="{y + 4:.1f}" x2="{cx + uw/2:.1f}" y2="{y + 4:.1f}" '
             'stroke="#ffffff" stroke-opacity="0.85" stroke-width="4"/>')
    y += pu

    # サブ文言（任意）
    if sub_lines:
        y += g2
        for i, ln in enumerate(sub_lines):
            by = y + sub_fs * 0.82 + i * (sub_fs * 1.4)
            p.append(f'<text x="{cx}" y="{by:.1f}" text-anchor="middle" font-family="{fam}" '
                     f'font-weight="700" font-size="{sub_fs}" fill="#ffffff">{html.escape(ln)}</text>')
        y += sub_h

    # ブランド
    y += g3
    p.append(f'<text x="{cx}" y="{y + brand_fs*0.82:.1f}" text-anchor="middle" font-family="{fam}" '
             f'font-weight="700" font-size="{brand_fs}" fill="#ffffff" opacity="0.92" '
             'letter-spacing="3">nito</text>')

    p.append('</svg>')
    return "".join(p)


def eyecatch_html(meta) -> str:
    """アイキャッチ。image指定があれば写真、なければブランド固定デザインSVGを自動生成。"""
    img = meta.get("image", "")
    if img:
        return f'<div class="post-eyecatch"><img src="{html.escape(img)}" alt="{html.escape(meta["title"])}"></div>'
    headline, sub, tag = cover_texts(meta)
    uid = hashlib.md5(f"{headline}|{tag}".encode()).hexdigest()[:8]
    return f'<div class="post-eyecatch post-eyecatch--svg">{eyecatch_svg(headline, sub, tag, uid)}</div>'


def card_thumb(meta, cls="rel-card__thumb") -> str:
    """カードのサムネイル。image指定があれば写真、なければ固定デザインSVG（サブ文言なし）。"""
    img = meta.get("image", "")
    if img:
        return f'<div class="{cls}" style="background-image:url(\'{html.escape(img)}\')"></div>'
    headline, _sub, tag = cover_texts(meta)
    uid = hashlib.md5(f"{headline}|{tag}|c".encode()).hexdigest()[:8]
    return f'<div class="{cls} card-thumb--svg">{eyecatch_svg(headline, "", tag, uid)}</div>'



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


def og_image_url(meta, slug) -> str:
    """共有時のサムネイル。front matter の image → media/images/og/<slug>.jpg（gen_og.py で生成）→ サイト既定。
    2026-09-17 まで og:image が無く、Slack/X で共有すると画像なしのカードになっていた。"""
    if meta.get("image"):
        img = meta["image"]
        return img if img.startswith("http") else SITE + img
    if (ROOT / "images" / "og" / f"{slug}.jpg").exists():
        return f"{SITE}/media/images/og/{slug}.jpg"
    return f"{SITE}/media/images/og/_default.jpg"


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
        "{{OG_IMAGE}}": og_image_url(meta, post["slug"]),
    }
    for key, val in replacements.items():
        out = out.replace(key, val)
    return out


# 一覧の業種フィルタ: slug → 業種バケット。未登録の記事は「一般」（概念・ノウハウ）扱い。
INDUSTRY_MAP = {
    "real-estate-ai-search": "不動産・建設",
    "construction-ai-search": "不動産・建設",
    "ec-ai-search": "EC・通販",
    "clinic-ai-search": "医療・美容",
    "beauty-clinic-ai-search": "医療・美容",
    "restaurant-ai-search": "飲食・宿泊",
    "hotel-travel-ai-search": "飲食・宿泊",
    "cram-school-ai-search": "教育",
    "recruitment-ai-search": "採用・人材",
    "recruitment-agency-ai-search": "採用・人材",
    "manufacturing-ai-search": "製造・SaaS",
    "saas-ai-search": "製造・SaaS",
    "shigyo-ai-search": "士業・その他",
    "startup-ai-search": "士業・その他",
}
# フィルタボタンの表示順（存在するものだけ出す）
INDUSTRY_ORDER = [
    "一般", "不動産・建設", "EC・通販", "医療・美容", "飲食・宿泊",
    "教育", "採用・人材", "製造・SaaS", "士業・その他",
]


def build_list(posts, template: str) -> str:
    present = set(INDUSTRY_MAP.get(p["slug"], "一般") for p in posts)

    links = ['        <a href="#" data-ind="all" class="is-active">すべて</a>']
    for ind in INDUSTRY_ORDER:
        if ind in present:
            links.append(f'        <a href="#" data-ind="{html.escape(ind)}">{html.escape(ind)}</a>')

    cards = []
    for p in posts:
        m = p["meta"]
        ind = INDUSTRY_MAP.get(p["slug"], "一般")
        cards.append(
            f'        <a href="/media/{p["slug"]}/" class="rel-card" data-ind="{html.escape(ind)}">\n'
            f'            {card_thumb(m)}\n'
            f'            <div class="rel-card__date">{m["date"].replace("-", ".")} ・ {html.escape(m["category"])}</div>\n'
            f'            <div class="rel-card__ttl">{html.escape(m["title"])}</div>\n'
            "        </a>"
        )

    out = template
    out = out.replace("{{CATEGORIES}}", "\n".join(links))
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
STATIC_PAGES = ["/", "/ai-agent/", "/llmo/", "/media/", "/contact.html", "/privacy.html"]


def post_lastmod(p) -> str:
    """sitemap の lastmod。front matter の date と、md の最終コミット日の新しい方。
    公開後に直した記事が lastmod 固定のままだと再クロールの優先度が上がらない（2026-09-17 実測:
    9/13 に直した記事の最終クロールが 8/11 のまま）。git が無い／shallow の場合は date にフォールバック。"""
    import subprocess
    d = p["meta"]["date"]
    try:
        out = subprocess.run(["git", "log", "-1", "--format=%cs", "--", str(POSTS_DIR / f"{p['slug']}.md")],
                             capture_output=True, text=True, timeout=10, cwd=ROOT.parent).stdout.strip()
        if re.fullmatch(r"\d{4}-\d{2}-\d{2}", out) and out > d:
            return out
    except Exception:
        pass
    return d


def generate_sitemap(posts):
    """リポジトリ直下に sitemap.xml を生成する（固定ページ＋全記事）。"""
    root = ROOT.parent
    today = date.today().isoformat()
    urls = []
    for path in STATIC_PAGES:
        urls.append((f"{SITE}{path}", today))
    for p in posts:
        urls.append((f"{SITE}/media/{p['slug']}/", post_lastmod(p)))

    lines = ['<?xml version="1.0" encoding="UTF-8"?>',
             '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for loc, lastmod in urls:
        lines.append(f"  <url><loc>{loc}</loc><lastmod>{lastmod}</lastmod></url>")
    lines.append("</urlset>")
    (root / "sitemap.xml").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"✔ sitemap.xml （{len(urls)}URL）")


# AI感チェック（lint）: WRITING_GUIDEで禁止している表現を機械的に検出する。
# 「毎回同じ指摘」を防ぐための決定的チェック。ビルド時に必ず全記事をスキャンする。
AI_TELL_PATTERNS = [
    (r"——|――|―|─|—", "ダッシュ（——・―など）。読点や句点で文を区切る"),
    (r"いかがでした", "定型句「いかがでしたか」"),
    (r"本記事では.{0,12}(解説|紹介|まとめ)しました", "定型句「本記事では〜解説しました」"),
    (r"理由は明確です", "紋切り型「理由は明確です。」→ 地の文で書き下す"),
    (r"興味深いのは.{0,20}という点", "紋切り型「興味深いのは〜という点です」"),
    (r"これが示すのは.{0,20}ということ", "紋切り型「これが示すのは〜ということ」"),
    (r"正直に(言うと|書き|言えば)|正直なところ", "「正直に言うと」の類。前置きせず本題を書く"),
    (r"攻め筋", "「攻め筋」。言葉だけ強く中身が薄い。具体的な内容に置き換える"),
    (r"[\U0001F300-\U0001FAFF]", "絵文字"),
]


def lint_posts(md_files):
    """禁止表現を検出して警告を返す。ビルドは止めないが必ず目立たせる。"""
    warnings = []
    for f in md_files:
        text = f.read_text(encoding="utf-8")
        for lineno, line in enumerate(text.splitlines(), 1):
            for pat, desc in AI_TELL_PATTERNS:
                if re.search(pat, line):
                    snippet = line.strip()[:56]
                    warnings.append(f"  {f.name}:{lineno}  [{desc}]  {snippet}")
    return warnings


def main():
    article_tpl = (TEMPLATE_DIR / "article.html").read_text(encoding="utf-8")
    list_tpl = (TEMPLATE_DIR / "list.html").read_text(encoding="utf-8")

    md_files = sorted(POSTS_DIR.glob("*.md"))

    # FAQ構造化データの欠落チェック（2026-09-24）
    # 「## よくある質問」があるのに ### が無いと extract_faq が拾えず、
    # FAQPage/Question の JSON-LD が丸ごと出ない。9/21〜9/23 に15本で起きた。
    faq_broken = []
    for f in md_files:
        text = f.read_text(encoding="utf-8")
        m = re.search(r"^## .*よくある質問.*$", text, flags=re.M)
        if not m:
            continue
        block = text[m.end():]
        nxt = re.search(r"^## ", block, flags=re.M)
        block = block[: nxt.start()] if nxt else block
        if not re.search(r"^### ", block, flags=re.M):
            bold = len(re.findall(r"^\*\*.+\*\*$", block, flags=re.M))
            faq_broken.append(f"  {f.name}: よくある質問に ### が1つも無い"
                              + (f"（太字の行が{bold}件。### に直す）" if bold else ""))
    if faq_broken:
        print("=" * 60)
        print("⚠ FAQ構造化データが出ません（質問は ### で書く）")
        for w in faq_broken:
            print(w)
        print("=" * 60)
        print("")

    # AI感チェック（禁止表現の機械検出）
    lint_warnings = lint_posts(md_files)
    if lint_warnings:
        print("=" * 60)
        print("⚠ AI感チェック: 禁止表現が見つかりました（WRITING_GUIDE参照）")
        for w in lint_warnings:
            print(w)
        print("=" * 60)
        print("")

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
        body_md = convert_linkcard_blocks(body_md)
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

    # CSS のキャッシュ破り: media.css の内容ハッシュを ?v= に付ける。
    # 2026-09-17 実測: Cloudflare が media.css を max-age=14400 で保持し、テンプレート更新後も
    # 最大4時間古い CSS が配られた（HTML は新しいのに見た目が変わらない）。URL を変えれば即反映される。
    css_ver = hashlib.sha1((ROOT / "_template" / "media.css").read_bytes()).hexdigest()[:8]
    def bust(html_text: str) -> str:
        return html_text.replace('/media/_template/media.css"', f'/media/_template/media.css?v={css_ver}"')

    for p in posts:
        out_dir = ROOT / p["slug"]
        out_dir.mkdir(exist_ok=True)
        (out_dir / "index.html").write_text(bust(build_article(p, posts, article_tpl)), encoding="utf-8")
        print(f"✔ media/{p['slug']}/index.html")

    (ROOT / "index.html").write_text(bust(build_list(posts, list_tpl)), encoding="utf-8")
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
