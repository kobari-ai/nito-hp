"""記事ページの CTA 部品（2026-10-17 希一さん OK。spec は brain の drafts/design/media-cta_spec.md）

記事の主題で文面と行き先を切り替える。**既定は AI 検索対策（AIO）**（2026-10-17 夜 希一さん「本当は aio 側に流したい。aio と関連なさそうなのはエージェントで良い」）
- llmo: AI 検索対策の記事と、AI ツールの使い方・困りごとの記事。行き先は /llmo/
- ai_agent: 会社で AI を導入・管理・開発する記事（管理者の設定・法人プラン・請求書・料金・Claude Code・MCP など）。行き先は /ai-agent/
front matter で上書きできる:
    cta: llmo | ai_agent         主題の判定を上書き
    cta_eyebrow / cta_title / cta_text   本文中の CTA の文面を上書き
    fork_q / fork_go / fork_href 目的で選ぶ3行の1行目（この記事の続きを読む）を上書き
"""
import html
import re

ADMIN_WORDS = ("admin", "team", "business", "enterprise", "license", "invoice", "work-plans", "pricing", "work-iq")
# 会社で AI を導入・管理・開発する記事（ここに当たるものだけ AIエージェント構築へ送る）
AGENT_WORDS = ADMIN_WORDS + ("workspace", "claude-code", "codex", "mcp", "ai-agent", "cowork", "gemini-cli",
                             "jev", "company-memory", "connectors")


def theme_of(meta, body_html, slug=""):
    t = (meta.get("cta") or "").strip()
    if t in ("llmo", "ai_agent"):
        return t
    if 'class="bp-cta"' in body_html:
        return "llmo"
    return "ai_agent" if any(w in slug for w in AGENT_WORDS) else "llmo"


def product_of(slug):
    s = slug
    if "-vs-" in s:  # 比較記事は片方の製品に寄せない（2026-10-25 希一さん）
        return "AI"
    if s.startswith("chatgpt"):
        return "ChatGPT"
    if s.startswith("claude"):
        return "Claude"
    if s.startswith("copilot"):
        return "Copilot"
    if s.startswith(("gemini", "google-workspace", "gmail", "notebooklm")):
        return "Gemini"
    return "AI"


def is_admin(slug):
    return any(w in slug for w in ADMIN_WORDS)


def _e(s):
    return html.escape(s, quote=True)


def byline(author, role, image):
    return (f'<div class="byline"><img src="{image}" alt="" width="32" height="32">'
            f'<span>執筆 <b>{_e(author)}</b>（{_e(role)}）</span></div>')


def fork(meta, slug, theme):
    q = meta.get("fork_q") or "このまま手順を読みたい"
    go = meta.get("fork_go") or "本文へ"
    p = product_of(slug)
    href = meta.get("fork_href") or "#s1"
    first = f'<a href="{_e(href)}"><span class="fork__q">{_e(q)}</span><span class="fork__go">{_e(go)}</span></a>'
    agent_q = (f"会社で {p} を使っていて毎日の作業ごと AI に任せたい" if p != "AI"
               else "会社の毎日の作業を AI に任せたい")
    agent = f'<a href="/ai-agent/"><span class="fork__q">{_e(agent_q)}</span><span class="fork__go">AIエージェント構築</span></a>'
    llmo = ('<a href="/llmo/"><span class="fork__q">AI に自社がどう紹介されているか知りたい</span>'
            '<span class="fork__go">AI検索対策</span></a>')
    rows = [first, llmo, agent] if theme == "llmo" else [first, agent, llmo]
    return '<div class="fork">\n<div class="fork__ttl">目的に合わせて読む</div>\n' + "\n".join(rows) + "\n</div>"


UI_FRAGMENT = '''<div class="mcta__ui" aria-hidden="true">
<div class="ui-msg"><div class="ui-av">田</div><div><div class="ui-name">田中<span>9:12</span></div>A社との商談メモ、Driveに上げました。次回は来週火曜です。</div></div>
<div class="ui-msg"><div class="ui-av ui-av--ai">AI</div><div><div class="ui-name">nito AI<span>22:00</span></div>提案1枚と想定質問を仕上げました。朝に確認だけお願いします。
<div class="ui-card"><b>次回商談の準備（自動作成）</b>前回の宿題3件の進捗<br>物流部門向けの提案1枚<br>想定質問と回答</div></div></div>
</div>'''


def mid_cta(meta, slug):
    p = product_of(slug)
    if is_admin(slug):
        eyebrow = f"会社で {p} を導入する方へ" if p != "AI" else "会社で AI を導入する方へ"
        title = "導入したあと毎日の業務で使われる形まで決まっていますか"
        text = ("ライセンスを配っただけでは、毎日の業務のどこで使うかが決まりません。"
                "nito は業務の棚卸しから、指示しなくても動く AI エージェントの構築まで一緒に進めます。")
    else:
        eyebrow = f"会社で {p} を使っている方へ" if p != "AI" else "会社で AI を使っている方へ"
        title = "毎日くり返す作業を毎回チャットで頼んでいませんか"
        text = ("日報の集計や議事録の整理のように毎日くり返す作業は、チャットで頼まなくても動く AI エージェントにできます。"
                "nito は業務の棚卸しから構築・運用まで一緒に進めます。")
    eyebrow = meta.get("cta_eyebrow") or eyebrow
    title = meta.get("cta_title") or title
    text = meta.get("cta_text") or text
    return (f'<div class="mcta">\n<div class="mcta__body">\n'
            f'<p class="mcta__eyebrow">{_e(eyebrow)}</p>\n'
            f'<p class="mcta__ttl">{_e(title)}</p>\n'
            f'<p class="mcta__txt">{_e(text)}</p>\n'
            '<div class="mcta__actions"><a class="mcta__btn" href="/ai-agent/">AIエージェント構築の進め方を見る</a>'
            '<a class="mcta__link" href="/contact.html">無料で業務棚卸しを相談</a></div>\n'
            f'</div>\n{UI_FRAGMENT}\n</div>')


LLMO_UI = '''<div class="mcta__ui" aria-hidden="true">
<div class="ui-q">従業員50人の会社に合う勤怠管理システムのおすすめは？</div>
<div class="ui-msg"><div class="ui-av ui-av--ai">AI</div><div>条件に合いそうなのは次の3つです。
<div class="ui-card"><b>A社の勤怠クラウド</b>人数別の料金が公開されていて比べやすい</div>
<div class="ui-card"><b>B勤怠</b>機能が多く、拠点が多い会社向け</div>
<div class="ui-card ui-card--none"><b>自社の名前はない</b></div></div></div>
</div>'''


def ai_name(slug):
    p = product_of(slug)
    if p in ("ChatGPT", "Gemini", "Claude", "Copilot"):
        return p
    if slug.startswith(("ai-mode", "ai-overviews", "google", "chrome", "circle")):
        return "AIモード"
    return "AI"


def mid_cta_llmo(meta, slug):
    n = ai_name(slug)
    eyebrow = meta.get("cta_eyebrow") or "会社のサイトを担当している方へ"
    title = meta.get("cta_title") or (f"{n} に自社がどう紹介されているか調べてみませんか" if n != "AI"
                                      else "AI のおすすめに自社の名前が挙がるか調べてみませんか")
    text = meta.get("cta_text") or ("調べものに ChatGPT などの AI 検索を使う人は、1年3か月で21.3%から52.3%に増えました（サイバーエージェント GEOラボ調べ）。"
                                    "nito は ChatGPT・Gemini・AIモードの回答を実際のチャット画面で集め、自社の名前が挙がるかを無料の現状分析レポートで数字にします。")
    return (f'<div class="mcta">\n<div class="mcta__body">\n'
            f'<p class="mcta__eyebrow">{_e(eyebrow)}</p>\n'
            f'<p class="mcta__ttl">{_e(title)}</p>\n'
            f'<p class="mcta__txt">{_e(text)}</p>\n'
            '<div class="mcta__actions"><a class="mcta__btn" href="/llmo/">無料の現状分析レポートを見る</a>'
            '<a class="mcta__link" href="/contact.html">無料で相談する</a></div>\n'
            f'</div>\n{LLMO_UI}\n</div>')


def insert_mid(body_html, cta_html):
    """読者の問題が解けた直後に置く。3つ目の h2 の前（h2 が4つ以上あるとき）、無ければ「よくある質問」の前。"""
    h2s = [m.start() for m in re.finditer(r'<h2 id="s\d+"', body_html)]
    faq = re.search(r'<h2 id="s\d+">[^<]*よくある質問', body_html)
    if len(h2s) >= 4:
        pos = h2s[2]
        if faq and faq.start() < pos:
            pos = faq.start()
    elif faq:
        pos = faq.start()
    elif len(h2s) >= 2:
        pos = h2s[-1]
    else:
        return body_html
    return body_html[:pos] + cta_html + "\n\n" + body_html[pos:]


def end_cta(slug, theme):
    if theme == "llmo":
        return ('<div class="ecta">\n<div class="ecta__label">CONTACT</div>\n'
                '<div class="ecta__ttl">AI のおすすめに自社の名前が挙がるかを無料で調べます</div>\n'
                '<p class="ecta__desc">ChatGPT・Gemini・AIモードの回答を実際のチャット画面で集め、いまの見え方を数字で出します。</p>\n'
                '<div class="ecta__btns"><a class="pri" href="/contact.html">無料で現状分析レポートを申し込む</a>'
                '<a class="sec" href="/llmo/">支援内容を見る</a></div>\n'
                '<p class="ecta__sub">会社の業務に AI を組み込みたい方は <a href="/ai-agent/">AIエージェント構築支援</a> をご覧ください。</p>\n</div>')
    p = product_of(slug)
    ttl = f"{p} を会社の業務に組み込む相談を受けています"
    return ('<div class="ecta">\n<div class="ecta__label">CONTACT</div>\n'
            f'<div class="ecta__ttl">{_e(ttl)}</div>\n'
            '<p class="ecta__desc">どの作業を AI に任せるかの棚卸しから一緒に進めます。相談は無料です。</p>\n'
            '<div class="ecta__btns"><a class="pri" href="/contact.html">無料で業務棚卸しを相談</a>'
            '<a class="sec" href="/ai-agent/">進め方を見る</a></div>\n'
            '<p class="ecta__sub">AI 検索で自社がどう紹介されているかを知りたい方は <a href="/llmo/">AI検索対策（AIO）</a> をご覧ください。</p>\n</div>')


def rail(toc_html, theme):
    items = re.findall(r'<li class="toc-h2"><a href="#(s\d+)"><span class="toc__n">\d+</span>(.*?)</a></li>', toc_html)
    links = "".join(f'<a href="#{i}">{t}</a>' for i, t in items[:8])
    if theme == "llmo":
        cta = ('<div class="rail__cta"><b>AI での見え方を無料で調べる</b>'
               '<p>ChatGPT・Gemini・AIモードで自社の名前が挙がるかを数字で出します。</p>'
               '<a href="/llmo/">現状分析レポート</a></div>')
    else:
        cta = ('<div class="rail__cta"><b>会社での AI 活用の相談</b>'
               '<p>どの作業を AI に任せるかの棚卸しから一緒に進めます。</p>'
               '<a href="/contact.html">無料で相談する</a></div>')
    toc = f'<div class="rail__toc"><p>目次</p>{links}</div>' if links else ""
    return f'<aside class="rail">{toc}{cta}</aside>'
