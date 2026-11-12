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

network_asset = re.compile(r"^(?:https?|wss?):|^(?:https?:)?//", re.IGNORECASE)
network_reference = re.compile(r"(?:https?|wss?)://|(?:@import|url|import)\s*(?:\(\s*)?['\"]?(?:https?:)?//", re.IGNORECASE)
runtime_api = re.compile(r"\b(?:fetch|XMLHttpRequest|WebSocket|EventSource|sendBeacon)\b")

for href in parser.links:
    # Repository links are navigation, not runtime assets, so they may be public URLs.
    if network_asset.match(href):
        continue
    if href.startswith("#") or href.startswith("?"):
        continue
    local = href.split("?", 1)[0]
    if not (ROOT / local).is_file():
        fail(f"missing local link target: {href}")

runtime_assets = parser.scripts + parser.styles
for href in runtime_assets:
    if network_asset.match(href):
        fail(f"network runtime asset is not allowed: {href}")
    local = href.split("?", 1)[0]
    path = ROOT / local
    if not path.is_file():
        fail(f"missing local runtime asset: {href}")
    source = path.read_text(encoding="utf-8")
    if network_reference.search(source):
        fail(f"network reference is not allowed in local runtime asset: {path.relative_to(ROOT)}")
    if path.suffix == ".js" and runtime_api.search(source):
        fail(f"network API is not allowed in local runtime asset: {path.relative_to(ROOT)}")

css_text = css.read_text(encoding="utf-8")
for token in ("--void: #050008", "--acid: #d7ff2f", "backdrop-filter: blur(18px) saturate(1.25)", "prefers-reduced-motion"):
    if token not in css_text:
        fail(f"required visual recipe is missing: {token}")

index_text = index.read_text(encoding="utf-8")
# Ignore navigational anchor destinations while retaining the no-network guard for HTML runtime content.
index_runtime_text = re.sub(r"(<a\b[^>]*\bhref\s*=\s*)(['\"]).*?\2", r"\1", index_text, flags=re.IGNORECASE | re.DOTALL)
if runtime_api.search(index_text) or network_reference.search(index_runtime_text):
    fail("index.html must not make network requests")

print("static source check: OK (source lint only; no build or runtime test)")
