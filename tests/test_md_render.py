"""
md_render.py — renders every record's body to the `html` field the CRUD UI displays, so its
escaping is the XSS boundary. Pure function, tested directly.
"""
import re

import pytest
from md_render import render_markdown


def anchors(html):
    return re.findall(r"<a\b[^>]*>", html)


# --- regression v0.5.7: link XSS ---------------------------------------------------------------

@pytest.mark.parametrize("url", [
    "javascript:alert(1)",
    "JavaScript:alert(1)",
    "JAVASCRIPT:alert(document.cookie)",
    "data:text/html;base64,PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pg==",
    "vbscript:msgbox(1)",
    " javascript:alert(1)",
    "java\tscript:alert(1)",
    "&#106;avascript:alert(1)",
    "javascript&colon;alert(1)",
])
def test_unsafe_link_schemes_render_as_inert_text(url):
    html = render_markdown(f"[click]({url})")
    assert anchors(html) == []
    assert "href" not in html


def test_quote_in_url_cannot_break_out_of_href():
    payload = """[hover](http://x.test/" onmouseover="location='http://evil.test'")"""
    html = render_markdown(payload)
    (a,) = anchors(html)
    # Exactly one attribute on the anchor, and the quote was entity-encoded inside it.
    assert re.fullmatch(r'<a href="[^"]*">', a), a
    assert "&quot;" in a


def test_single_quote_in_url_is_encoded():
    (a,) = anchors(render_markdown("[x](http://x.test/' onclick='alert(1))"))
    assert "'" not in a


def test_label_is_escaped():
    html = render_markdown('[<img src=x onerror=alert(1)>](https://example.com)')
    assert "<img" not in html
    assert "&lt;img" in html


@pytest.mark.parametrize("md", [
    "<script>alert(1)</script>",
    "# <script>alert(1)</script>",
    "- <script>alert(1)</script>",
    "1. <script>alert(1)</script>",
    "> <script>alert(1)</script>",
    "| <script>alert(1)</script> | b |\n|---|---|\n| <script>x</script> | d |",
    "**<script>alert(1)</script>**",
    "`<script>alert(1)</script>`",
])
def test_raw_html_is_escaped_in_every_block_type(md):
    html = render_markdown(md)
    assert "<script" not in html
    assert "&lt;script&gt;" in html


@pytest.mark.parametrize("md", [
    '<img src=x onerror="alert(1)">',
    '<svg onload=alert(1)>',
    '<a href="javascript:alert(1)">x</a>',
    '<iframe src="https://evil.test"></iframe>',
])
def test_raw_html_tags_never_survive(md):
    html = render_markdown(md)
    assert not re.search(r"<(img|svg|iframe|a)\b", html)


@pytest.mark.parametrize("url", [
    "https://example.com/path?q=1",
    "http://example.com",
    "mailto:someone@example.com",
    "/absolute/path.md",
    "#anchor",
    "./sibling.md",
    "../findings/onboarding.md",
    "//evil.test",  # protocol-relative: accepted by design (off-site link, not XSS)
])
def test_safe_link_schemes_render_as_anchors(url):
    html = render_markdown(f"[label]({url})")
    assert anchors(html) == [f'<a href="{url}">']
    assert html == f'<p><a href="{url}">label</a></p>'


def test_ampersand_in_url_is_entity_encoded():
    html = render_markdown("[x](https://example.com/?a=1&b=2)")
    assert '<a href="https://example.com/?a=1&amp;b=2">' in html


# --- formatting --------------------------------------------------------------------------------

@pytest.mark.parametrize("level", [1, 2, 3, 4])
def test_headings(level):
    assert render_markdown("#" * level + " Title") == f"<h{level}>Title</h{level}>"


def test_five_hashes_is_not_a_heading():
    assert render_markdown("##### Title") == "<p>##### Title</p>"


def test_inline_formatting():
    html = render_markdown("**bold** and *italic* and `code`")
    assert html == "<p><strong>bold</strong> and <em>italic</em> and <code>code</code></p>"


def test_paragraph_lines_are_joined():
    assert render_markdown("one\ntwo\n\nthree") == "<p>one two</p>\n<p>three</p>"


def test_crlf_is_normalized():
    assert render_markdown("# A\r\n\r\ntext\r\n") == render_markdown("# A\n\ntext\n")


def test_blockquote_lines_become_separate_paragraphs():
    html = render_markdown('> "Quote here."\n> — Physician, P09')
    assert html == '<blockquote><p>&quot;Quote here.&quot;</p><p>— Physician, P09</p></blockquote>'


def test_unordered_list_with_lazy_continuation():
    html = render_markdown("- first item\nwraps here\n- second")
    assert html == "<ul><li>first item wraps here</li><li>second</li></ul>"


def test_ordered_list_with_lazy_continuation():
    html = render_markdown("1. first\nwraps\n2. second")
    assert html == "<ol><li>first wraps</li><li>second</li></ol>"


def test_list_ends_at_new_block_type():
    html = render_markdown("- item\n# Heading")
    assert html == "<ul><li>item</li></ul>\n<h1>Heading</h1>"


def test_table():
    html = render_markdown("| Topic | Tags |\n|---|---|\n| A | x, y |\n| B | z |")
    assert html == (
        "<table><thead><tr><th>Topic</th><th>Tags</th></tr></thead>"
        "<tbody><tr><td>A</td><td>x, y</td></tr><tr><td>B</td><td>z</td></tr></tbody></table>"
    )


def test_empty_input():
    assert render_markdown("") == ""
    assert render_markdown("\n\n  \n") == ""
