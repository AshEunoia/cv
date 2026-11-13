# 2026-11-13-01-47-11
"""Build the CV: cv.md to HTML with cv.css, then to an A4 PDF with Playwright's Chromium, and
check the PDF. It must fit on two pages, use the CV's own typeface, and hold the same text as the
Markdown in the same order, which is how screening software will read it.

    uv run build.py            build Ash-Eunoia-CV.pdf and check it
    uv run build.py --links    also check that every link in the CV answers
"""

import argparse
import html
import re
import sys
import unicodedata
import urllib.error
import urllib.request
from pathlib import Path

from fontTools.ttLib import TTFont
from fontTools.varLib import instancer
from markdown_it import MarkdownIt
from playwright.sync_api import sync_playwright
from pypdf import PdfReader

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "cv.md"
STYLES = HERE / "cv.css"
PAGE = HERE / "build" / "cv.html"
OUTPUT = HERE / "Ash-Eunoia-CV.pdf"
MAX_PAGES = 2
FONT = "Bricolage Grotesque"
VARIABLE_FONT = HERE / "fonts" / "bricolage-grotesque-latin.woff2"
# Chromium prints a variable font as Type 3 glyphs, which some parsers read badly, so the PDF uses
# fixed instances instead: each weight the CV uses, at the optical size (in pixels) of its main use.
INSTANCES = {400: 14, 600: 16, 700: 15, 800: 35}
# Answers that mean a site turned the checker away, not that the page is missing
REFUSED = {401, 403, 429, 999}


def static_fonts():
    """Make the fixed instances of the typeface, and return the CSS that loads them."""
    rules = []
    for weight, size in INSTANCES.items():
        path = PAGE.parent / "fonts" / f"bricolage-grotesque-{weight}.ttf"
        if not path.exists() or path.stat().st_mtime < VARIABLE_FONT.stat().st_mtime:
            path.parent.mkdir(parents=True, exist_ok=True)
            font = instancer.instantiateVariableFont(TTFont(VARIABLE_FONT), {"wght": weight, "opsz": size})
            font.flavor = None
            font.save(path)
        rules.append(f'@font-face {{ font-family: "{FONT}"; src: url("{path.as_uri()}"); font-weight: {weight}; }}')
    return "\n".join(rules)


def render():
    """Write the HTML page and return it."""
    markdown = SOURCE.read_text(encoding="utf-8")
    name = re.search(r"^# (.+)$", markdown, re.MULTILINE).group(1)
    body = MarkdownIt("commonmark").render(markdown)
    # Wrap each entry, from its heading to the next heading, so the stylesheet can keep it on one page
    body = "".join(
        f'<div class="entry">\n{part}</div>\n' if part.startswith("<h3") else part
        for part in re.split(r"(?=<h[1-3]>)", body)
    )
    page = f"""<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<title>{html.escape(name)}: CV</title>
<style>
{static_fonts()}
</style>
<link rel="stylesheet" href="{STYLES.as_uri()}">
</head>
<body>
{body}</body>
</html>
"""
    PAGE.parent.mkdir(exist_ok=True)
    PAGE.write_text(page, encoding="utf-8")
    return page


def launch(playwright):
    """Playwright's own Chromium, or Microsoft Edge where that isn't installed."""
    try:
        return playwright.chromium.launch()
    except Exception:
        return playwright.chromium.launch(channel="msedge")


def tokens(text):
    """The words and numbers in a text, ignoring punctuation, bullets and spacing."""
    return re.findall(r"\w+", unicodedata.normalize("NFKC", text))


def print_pdf():
    """Print the page to PDF and return the text the browser laid out."""
    with sync_playwright() as playwright:
        browser = launch(playwright)
        page = browser.new_page()
        page.goto(PAGE.as_uri())
        page.evaluate("document.fonts.ready")
        if not page.evaluate(f"document.fonts.check('11pt \"{FONT}\"')"):
            sys.exit(f"{FONT} didn't load, so the PDF would use a fallback font")
        page.pdf(path=OUTPUT, prefer_css_page_size=True, print_background=True, tagged=True, outline=True)
        text = page.evaluate("document.body.innerText")
        browser.close()
    return text


def check_pdf(laid_out):
    """Problems with the PDF: too many pages, or text missing or out of order."""
    problems = []
    reader = PdfReader(OUTPUT)
    pages = len(reader.pages)
    if pages > MAX_PAGES:
        problems.append(f"{pages} pages, more than {MAX_PAGES}")
    expected = tokens(laid_out)
    found = tokens("\n".join(page.extract_text() for page in reader.pages))
    if expected != found:
        at = next((i for i, (a, b) in enumerate(zip(expected, found)) if a != b), min(len(expected), len(found)))
        problems.append(
            "the PDF's text differs from the CV's at word "
            f"{at}: expected {' '.join(expected[at : at + 8])!r}, found {' '.join(found[at : at + 8])!r}"
        )
    return pages, len(found), problems


def check_links(page):
    """Problems with the CV's links: any web address that doesn't answer."""
    problems = []
    for url in sorted(set(re.findall(r'href="(https?://[^"]+)"', page))):
        request = urllib.request.Request(url, headers={"User-Agent": "cv-link-check"})
        try:
            with urllib.request.urlopen(request, timeout=20) as response:
                status = response.status
        except urllib.error.HTTPError as error:
            status = error.code
        except OSError as error:
            problems.append(f"{url}: {error}")
            continue
        if status in REFUSED:
            print(f"  {url}: {status}, the site turns automated checks away, so check it by hand")
        elif status >= 400:
            problems.append(f"{url}: {status}")
        else:
            print(f"  {url}: {status}")
    return problems


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--links", action="store_true", help="also check that every link answers")
    arguments = parser.parse_args()

    page = render()
    pages, words, problems = check_pdf(print_pdf())
    if arguments.links:
        problems += check_links(page)
    print(f"{OUTPUT.name}: {pages} page{'s' if pages != 1 else ''}, {words} words")
    if problems:
        sys.exit("Problems:\n" + "\n".join(f"- {problem}" for problem in problems))


if __name__ == "__main__":
    main()
