#!/usr/bin/env python3
"""Small source lint for the no-build design kit; this is not an application test."""
from html.parser import HTMLParser
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]


class PageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()
        self.links = []
        self.scripts = []
        self.styles = []
        self.has_title = False
        self.has_lang = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "html" and attrs.get("lang"):
            self.has_lang = True
        if tag == "title":
            self.has_title = True
        if attrs.get("id"):
            self.ids.add(attrs["id"])
        if tag == "a" and attrs.get("href"):
            self.links.append(attrs["href"])
        if tag == "script" and attrs.get("src"):
            self.scripts.append(attrs["src"])
        if tag == "link" and attrs.get("rel") == "stylesheet" and attrs.get("href"):
            self.styles.append(attrs["href"])


def fail(message):
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


index = ROOT / "index.html"
css = ROOT / "css" / "unhinged.css"
if not index.is_file() or not css.is_file():
    fail("index.html and css/unhinged.css are required")

parser = PageParser()
parser.feed(index.read_text(encoding="utf-8"))
if not parser.has_lang or not parser.has_title:
    fail("HTML needs a language and title")
if len(parser.ids) < 4:
    fail("HTML should contain the gallery's labelled IDs")

for href in parser.links + parser.scripts + parser.styles:
    if re.match(r"^(https?:)?//", href):
        fail(f"network asset is not allowed: {href}")
    if href.startswith("#") or href.startswith("?"):
        continue
    local = href.split("?", 1)[0]
    if not (ROOT / local).is_file():
        fail(f"missing local asset: {href}")

css_text = css.read_text(encoding="utf-8")
for token in ("--void: #050008", "--acid: #d7ff2f", "backdrop-filter: blur(18px) saturate(1.25)", "prefers-reduced-motion"):
    if token not in css_text:
        fail(f"required visual recipe is missing: {token}")

if re.search(r"(?:fetch|XMLHttpRequest|https?://)", index.read_text(encoding="utf-8")):
    fail("index.html must not make network requests")

print("static source check: OK (source lint only; no build or runtime test)")
