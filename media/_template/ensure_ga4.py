#!/usr/bin/env python3
"""サイト内の全HTMLにGA4スニペットが入っているか確認し、無ければ<head>直後に差し込む。
冪等（既に入っていればスキップ）。静的サイトに「全ページ共通GA4」を近似的に実現する。

使い方: python3 media/_template/ensure_ga4.py
"""
from pathlib import Path

GA_ID = "G-4LTJW13T70"
ROOT = Path(__file__).resolve().parent.parent.parent  # リポジトリ直下（nito-hp/）

SNIPPET = (
    "\n    <!-- Google Analytics 4 -->\n"
    f'    <script async src="https://www.googletagmanager.com/gtag/js?id={GA_ID}"></script>\n'
    "    <script>\n"
    "      window.dataLayer = window.dataLayer || [];\n"
    "      function gtag(){dataLayer.push(arguments);}\n"
    "      gtag('js', new Date());\n"
    f"      gtag('config', '{GA_ID}');\n"
    "    </script>"
)

# 対象外：テンプレート（プレースホルダ入り）は生成物側で処理済みなので触らない
EXCLUDE_DIRS = {".git", "node_modules"}
EXCLUDE_FILES = {"media/_template/article.html", "media/_template/list.html"}


def main():
    changed = 0
    skipped = 0
    for path in ROOT.rglob("*.html"):
        rel = path.relative_to(ROOT).as_posix()
        if any(part in EXCLUDE_DIRS for part in path.parts):
            continue
        if rel in EXCLUDE_FILES:
            continue
        html = path.read_text(encoding="utf-8")
        if GA_ID in html:
            skipped += 1
            continue
        if "<head>" not in html:
            continue
        html = html.replace("<head>", "<head>" + SNIPPET, 1)
        path.write_text(html, encoding="utf-8")
        print(f"＋GA4 追加: {rel}")
        changed += 1
    print(f"\n完了: 追加 {changed} / 既設 {skipped}")


if __name__ == "__main__":
    main()
