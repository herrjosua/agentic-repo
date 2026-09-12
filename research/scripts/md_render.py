import re
import html as html_lib


def render_markdown(md: str) -> str:
    """Convert the specific Markdown subset used in this repo to HTML.
    Supports: headings (#, ##, ###), bold, italic, inline code, links, blockquotes,
    unordered lists (-), ordered lists (1.), pipe tables, paragraphs.
    Not a general-purpose Markdown parser — matches only what this repo's own
    generators (build_repo.py, build_findings.py, build_components.py) actually emit.
    """
    lines = md.replace("\r\n", "\n").split("\n")
    html_parts = []
    i = 0
    n = len(lines)

    def inline(text):
        text = html_lib.escape(text, quote=False)
        text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
        text = re.sub(r"(?<!\*)\*([^*\n]+?)\*(?!\*)", r"<em>\1</em>", text)
        text = re.sub(r"`([^`]+?)`", r"<code>\1</code>", text)
        text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', text)
        return text

    def is_table_row(line):
        return line.strip().startswith("|") and line.strip().endswith("|")

    def is_table_separator(line):
        return bool(re.match(r"^\s*\|?[\s:|-]+\|?\s*$", line)) and "-" in line

    while i < n:
        line = lines[i]
        stripped = line.strip()

        if not stripped:
            i += 1
            continue

        # Headings
        m = re.match(r"^(#{1,4})\s+(.*)$", stripped)
        if m:
            level = len(m.group(1))
            html_parts.append(f"<h{level}>{inline(m.group(2))}</h{level}>")
            i += 1
            continue

        # Blockquote (collect contiguous > lines; render each non-empty line as its own <p>
        # so a quote and its "— Attribution" line stay visually distinct)
        if stripped.startswith(">"):
            quote_lines = []
            while i < n and lines[i].strip().startswith(">"):
                content = re.sub(r"^\s*>\s?", "", lines[i]).strip()
                if content:
                    quote_lines.append(content)
                i += 1
            inner = "".join(f"<p>{inline(p)}</p>" for p in quote_lines)
            html_parts.append(f"<blockquote>{inner}</blockquote>")
            continue

        # Tables
        if is_table_row(stripped) and i + 1 < n and is_table_separator(lines[i + 1]):
            header_cells = [c.strip() for c in stripped.strip("|").split("|")]
            i += 2
            rows = []
            while i < n and is_table_row(lines[i].strip()):
                rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")])
                i += 1
            thead = "".join(f"<th>{inline(c)}</th>" for c in header_cells)
            tbody = "".join(
                "<tr>" + "".join(f"<td>{inline(c)}</td>" for c in row) + "</tr>" for row in rows
            )
            html_parts.append(f"<table><thead><tr>{thead}</tr></thead><tbody>{tbody}</tbody></table>")
            continue

        # Unordered list
        if re.match(r"^[-*]\s+", stripped):
            items = []
            while i < n and re.match(r"^[-*]\s+", lines[i].strip()):
                items.append(re.sub(r"^[-*]\s+", "", lines[i].strip()))
                i += 1
            html_parts.append("<ul>" + "".join(f"<li>{inline(it)}</li>" for it in items) + "</ul>")
            continue

        # Ordered list
        if re.match(r"^\d+\.\s+", stripped):
            items = []
            while i < n and re.match(r"^\d+\.\s+", lines[i].strip()):
                items.append(re.sub(r"^\d+\.\s+", "", lines[i].strip()))
                i += 1
            html_parts.append("<ol>" + "".join(f"<li>{inline(it)}</li>" for it in items) + "</ol>")
            continue

        # Paragraph — collect contiguous non-empty, non-special lines
        para_lines = []
        while i < n and lines[i].strip() and not re.match(r"^(#{1,4})\s+", lines[i].strip()) \
                and not lines[i].strip().startswith(">") \
                and not re.match(r"^[-*]\s+", lines[i].strip()) \
                and not re.match(r"^\d+\.\s+", lines[i].strip()) \
                and not is_table_row(lines[i].strip()):
            para_lines.append(lines[i].strip())
            i += 1
        if para_lines:
            html_parts.append(f"<p>{inline(' '.join(para_lines))}</p>")

    return "\n".join(html_parts)


if __name__ == "__main__":
    sample = """## Key Findings
- **[CRITICAL]** *(phi-handling)* Something bad happened.
- **[HIGH]** *(accuracy)* Something else.

## Representative Quotes
> "I love what it got right, but I have to read every word anyway."
> — Physician, Internal Medicine, P09

## Recommendations
1. Do the first thing.
2. Do the second thing, with `inline code` and a [link](https://example.com).

| Topic | Tags |
|---|---|
| Ambient Scribe | ambient-scribe, usability |
| Prior Auth | prior-auth |
"""
    print(render_markdown(sample))
