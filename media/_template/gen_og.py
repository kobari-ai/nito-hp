#!/usr/bin/env python3
"""OG画像（共有時のサムネイル）を生成する。ローカル専用（CI では動かさない）。

各記事のアイキャッチ SVG（build.py の eyecatch_svg）を headless Chrome で 1200x628 の JPEG に描画し、
media/images/og/<slug>.jpg に置く。`image:` を持つ記事は対象外（その画像を OG に使う）。
既に jpg がある記事は --force のときだけ作り直す。

使い方: cd nito-hp && python3 media/_template/gen_og.py [--force] [slug ...]
（python-markdown が要る: pip install markdown）
"""
import subprocess, sys, tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build as B  # noqa: E402

OG_DIR = B.ROOT / "images" / "og"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
FONT = "https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@700&display=swap"


def page_html(svg: str) -> str:
    return (f'<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="{FONT}">'
            '<style>html,body{margin:0;background:#fff;overflow:hidden}svg{display:block;width:1200px;height:628px}</style>'
            f'</head><body>{svg}</body></html>')


def render(post, out: Path):
    headline, sub, tag = B.cover_texts(post["meta"])
    svg = B.eyecatch_svg(headline, sub, tag, "og")
    with tempfile.TemporaryDirectory() as d:
        html_path = Path(d) / "og.html"
        html_path.write_text(page_html(svg), encoding="utf-8")
        png = Path(d) / "og.png"
        subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
                        "--force-device-scale-factor=1", "--window-size=1200,628",
                        "--virtual-time-budget=4000",  # webfont の読み込みを待つ
                        f"--screenshot={png}", f"file://{html_path}"],
                       capture_output=True, timeout=60)
        subprocess.run(["sips", "-s", "format", "jpeg", "-s", "formatOptions", "88", str(png), "--out", str(out)],
                       capture_output=True)


def main():
    force = "--force" in sys.argv
    slugs = [a for a in sys.argv[1:] if not a.startswith("--")]
    OG_DIR.mkdir(parents=True, exist_ok=True)
    for md in sorted(B.POSTS_DIR.glob("*.md")):
        meta, _ = B.parse_front_matter(md.read_text(encoding="utf-8"))
        slug = md.stem
        if meta.get("image") or (slugs and slug not in slugs):
            continue
        out = OG_DIR / f"{slug}.jpg"
        if out.exists() and not force:
            continue
        render({"slug": slug, "meta": meta}, out)
        print("✔", out.relative_to(B.ROOT.parent))


if __name__ == "__main__":
    main()
