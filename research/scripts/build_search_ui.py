#!/usr/bin/env python3
"""
build_search_ui.py — generate research/search.html: a self-contained, offline-capable
search-and-filter interface over research/raw/, research/findings/,
design-tokens/components/, analytics/summaries/, and (feature-002) the 20 top-level
deliverable folders (research-plans/, personas/, wireframes/, ..., style-guide/ — see
DELIVERABLE_FOLDERS, imported from build_index.py so the two scripts can't drift apart on
which folders count as "the repo").

Why this exists: AGENTS.md already makes the repo queryable via any agent (Claude Code,
etc.) doing structured search over findings/ first, falling back to raw/. This script is
for the times you want to browse/filter visually instead — no agent, no server, just a
double-clickable HTML file with the whole corpus embedded in it.

Design note: markdown -> HTML conversion happens here at BUILD time (in Python), not in the
browser. The generated HTML/JS has zero markdown-parsing logic — it only filters and
displays pre-rendered content. This keeps the runtime side dumb and easy to trust, and
keeps all the parsing logic in one place (this file) rather than duplicated in JS.

Requires: pip install python-frontmatter

Usage:
    python build_search_ui.py            # writes research/search.html
    python build_search_ui.py --check    # exit 1 if search.html would change; write nothing
"""
import argparse
import glob
import json
import re
import sys
from pathlib import Path

try:
    import frontmatter
except ImportError:
    sys.exit("This script requires python-frontmatter: pip install python-frontmatter")

sys.path.insert(0, str(Path(__file__).resolve().parent))
from md_render import render_markdown  # noqa: E402  (local helper, see md_render.py)
from build_index import DELIVERABLE_FOLDERS  # noqa: E402  (shared source of truth for the 20 folders)

SCRIPT_DIR = Path(__file__).resolve().parent
RESEARCH_ROOT = SCRIPT_DIR.parent          # research/
REPO_ROOT = RESEARCH_ROOT.parent           # agentic-repo/
RAW_ROOT = RESEARCH_ROOT / "raw"
FINDINGS_ROOT = RESEARCH_ROOT / "findings"
COMPONENTS_ROOT = REPO_ROOT / "design-tokens" / "components"
ANALYTICS_ROOT = REPO_ROOT / "analytics"
ANALYTICS_SUMMARIES_ROOT = ANALYTICS_ROOT / "summaries"
OUTPUT_FILE = RESEARCH_ROOT / "search.html"

TYPE_LABELS = {
    "usability-test": "Usability test",
    "interview": "Interview",
    "survey": "Survey",
    "contextual-inquiry": "Contextual inquiry",
    "accessibility-audit": "Accessibility audit",
    "analytics": "Analytics",
    "analytics-summary": "Analytics summary",
    "synthesis": "Synthesis",
    # feature-002 deliverable folders double as their record's `type` value (see
    # build_deliverable_records) so they're filterable the same way research-method types are.
    "research-plans": "Research plan",
    "facilitation-guides": "Facilitation guide",
    "topline-summaries": "Topline summary",
    "research-readouts": "Research readout",
    "heuristic-evaluations": "Heuristic evaluation",
    "accessibility-screenings": "Accessibility screening",
    "service-topology": "Service topology",
    "personas": "Persona",
    "mental-models": "Mental model",
    "mindsets": "Mindset",
    "journey-maps": "Journey map",
    "thumbnails": "Thumbnail",
    "wireframes": "Wireframe",
    "user-flows": "User flow",
    "wireflows": "Wireflow",
    "storyboards": "Storyboard",
    "mockups": "Mockup",
    "prototypes": "Prototype",
    "design-system": "Design system",
    "style-guide": "Style guide",
}


def _str(value):
    return str(value) if value is not None else ""


def build_raw_records():
    records = []
    for session_path in sorted(glob.glob(str(RAW_ROOT / "*" / "session-notes.md"))):
        folder = Path(session_path).parent
        post = frontmatter.load(session_path)
        meta = post.metadata
        body_html = render_markdown(post.content)

        participants_path = folder / "participants.md"
        if participants_path.exists():
            p_post = frontmatter.load(participants_path)
            body_html += "<h2>Participants</h2>" + render_markdown(p_post.content)

        rel_path = f"raw/{folder.name}/session-notes.md"
        records.append(dict(
            id=f"raw:{folder.name}",
            kind="raw",
            title=meta.get("title", folder.name),
            date=_str(meta.get("date", "")),
            type=meta.get("type", ""),
            status=meta.get("status", ""),
            tags=meta.get("tags", []),
            related_components=meta.get("related_components", []),
            severity=meta.get("severity_summary", {}),
            path=rel_path,
            html=body_html,
        ))
    return records


def build_findings_records():
    records = []
    for path in sorted(glob.glob(str(FINDINGS_ROOT / "*.md"))):
        if Path(path).name == "tags.md":
            continue
        post = frontmatter.load(path)
        meta = post.metadata
        body_html = render_markdown(post.content)
        rel_path = f"findings/{Path(path).name}"
        records.append(dict(
            id=f"finding:{Path(path).stem}",
            kind="finding",
            title=meta.get("title", Path(path).stem),
            date=_str(meta.get("date", "")),
            type=meta.get("type", "synthesis"),
            status=meta.get("status", ""),
            tags=meta.get("tags", []),
            related_components=meta.get("related_components", []),
            severity={},
            path=rel_path,
            html=body_html,
        ))
    return records


def build_component_records():
    records = []
    if not COMPONENTS_ROOT.exists():
        return records
    for path in sorted(glob.glob(str(COMPONENTS_ROOT / "*.md"))):
        post = frontmatter.load(path)
        meta = post.metadata
        body_html = render_markdown(post.content)
        rel_path = f"../design-tokens/components/{Path(path).name}"
        records.append(dict(
            id=f"component:{Path(path).stem}",
            kind="component",
            title=meta.get("title", Path(path).stem),
            date=meta.get("generated_from", ""),  # components don't carry a date; show provenance instead
            type="component",
            status=meta.get("status", ""),
            tags=[],
            related_components=[],
            severity={},
            path=rel_path,
            html=body_html,
        ))
    return records


def build_analytics_records():
    records = []
    if not ANALYTICS_SUMMARIES_ROOT.exists():
        return records
    for path in sorted(glob.glob(str(ANALYTICS_SUMMARIES_ROOT / "*.md"))):
        post = frontmatter.load(path)
        meta = post.metadata
        body_html = render_markdown(post.content)
        rel_path = f"../analytics/summaries/{Path(path).name}"
        records.append(dict(
            id=f"analytics:{Path(path).stem}",
            kind="analytics",
            title=meta.get("title", Path(path).stem),
            date=_str(meta.get("date", "")),
            type=meta.get("type", "analytics-summary"),
            status=meta.get("status", ""),
            tags=meta.get("tags", []),
            related_components=[],
            severity={},
            path=rel_path,
            html=body_html,
        ))
    return records


def build_deliverable_records():
    """feature-002: one record per *.md (excluding _index.md) in each of the 20 top-level
    deliverable folders. `kind` is the single shared bucket 'deliverable' (so the sidebar's
    coarse Kind filter stays a short list); `type` is set to the folder name so the existing
    Type filter — already a flat, mixed vocabulary across the other kinds — doubles as the
    per-folder filter, no new UI concept needed."""
    records = []
    for folder in DELIVERABLE_FOLDERS:
        folder_root = REPO_ROOT / folder
        if not folder_root.exists():
            continue
        for path in sorted(glob.glob(str(folder_root / "*.md"))):
            if Path(path).name == "_index.md":
                continue
            post = frontmatter.load(path)
            meta = post.metadata
            body_html = render_markdown(post.content)
            rel_path = f"../{folder}/{Path(path).name}"
            records.append(dict(
                id=f"deliverable:{folder}/{Path(path).stem}",
                kind="deliverable",
                title=meta.get("title") or Path(path).stem,
                date=_str(meta.get("date", "")),
                type=folder,
                status=meta.get("status", ""),
                tags=meta.get("tags", []) or [],
                related_components=[],
                severity={},
                path=rel_path,
                html=body_html,
            ))
    return records


def build_search_text(record):
    """Flat lowercase text blob used for the client-side substring search."""
    parts = [
        record["title"],
        " ".join(record["tags"]),
        " ".join(record["related_components"]),
        re.sub(r"<[^>]+>", " ", record["html"]),
    ]
    return re.sub(r"\s+", " ", " ".join(parts)).strip().lower()


HTML_TEMPLATE = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Compass AI Research Archive</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Source+Serif+4:opsz,wght@8..60,400;8..60,500;8..60,600;8..60,700&family=IBM+Plex+Mono:wght@400;500;600&display=swap" rel="stylesheet">
<style>
  :root {
    --bg: #F7F8F9;
    --surface: #FFFFFF;
    --text-primary: #1C1F23;
    --text-secondary: #454B52;
    --border: #C7CCD1;
    --border-subtle: #EDEFF1;
    --accent: #1F52B3;
    --accent-hover: #173F8A;
    --accent-tint: #EBF3FE;
    --kind-raw: #1F52B3;
    --kind-finding: #146B64;
    --kind-component: #9A5E0D;
    --kind-analytics: #6B4FA0;
    --kind-deliverable: #2F7D4F;
    --sev-critical: #C33A2E;
    --sev-high: #C77B12;
    --sev-medium: #2B6CE0;
    --sev-low: #767E87;
    --serif: 'Source Serif 4', Georgia, 'Times New Roman', serif;
    --mono: 'IBM Plex Mono', ui-monospace, 'SF Mono', Menlo, monospace;
  }
  * { box-sizing: border-box; }
  html, body {
    margin: 0; padding: 0; background: var(--bg); color: var(--text-primary);
    font-family: var(--serif); font-size: 16px; line-height: 1.55;
  }
  a { color: var(--accent); }
  a:focus-visible, button:focus-visible, input:focus-visible, [tabindex]:focus-visible {
    outline: 2px solid var(--accent); outline-offset: 2px;
  }

  header {
    padding: 28px 32px 20px; border-bottom: 1px solid var(--border);
    background: var(--surface);
  }
  header h1 {
    margin: 0 0 4px; font-size: 26px; font-weight: 600; letter-spacing: -0.01em;
  }
  header p.tagline {
    margin: 0; color: var(--text-secondary); font-size: 14px; font-family: var(--mono);
  }

  .search-bar { padding: 16px 32px; background: var(--surface); border-bottom: 1px solid var(--border); }
  .search-bar input[type="search"] {
    width: 100%; max-width: 640px; padding: 10px 14px; font-size: 15px;
    font-family: var(--serif); border: 1px solid var(--border); border-radius: 4px;
    background: var(--bg); color: var(--text-primary);
  }
  .search-bar input[type="search"]::placeholder { color: var(--text-secondary); }

  .layout { display: grid; grid-template-columns: 260px 1fr; min-height: calc(100vh - 130px); }

  aside {
    padding: 24px; border-right: 1px solid var(--border); background: var(--surface);
  }
  aside h2 {
    font-family: var(--mono); font-size: 12px; font-weight: 600; letter-spacing: 0.02em;
    color: var(--text-secondary); margin: 20px 0 8px;
  }
  aside h2:first-child { margin-top: 0; }
  .filter-row {
    display: flex; align-items: center; gap: 8px; padding: 3px 0;
    font-family: var(--mono); font-size: 13px; cursor: pointer;
  }
  .filter-row input[type="checkbox"] { accent-color: var(--accent); }
  .filter-row .count { color: var(--text-secondary); margin-left: auto; }

  .tag-cloud { display: flex; flex-wrap: wrap; gap: 6px; }
  .tag-chip {
    font-family: var(--mono); font-size: 12px; padding: 3px 9px; border-radius: 999px;
    border: 1px solid var(--border); background: var(--bg); color: var(--text-secondary);
    cursor: pointer; line-height: 1.4;
  }
  .tag-chip.active { background: var(--accent); border-color: var(--accent); color: #fff; }

  #reset-filters {
    margin-top: 20px; font-family: var(--mono); font-size: 12px; color: var(--accent);
    background: none; border: none; cursor: pointer; padding: 0; text-decoration: underline;
  }

  main { padding: 24px 32px; }
  .result-count { font-family: var(--mono); font-size: 13px; color: var(--text-secondary); margin-bottom: 14px; }

  ul.results { list-style: none; margin: 0; padding: 0; border-top: 1px solid var(--border-subtle); }
  .result-row {
    border-bottom: 1px solid var(--border-subtle); padding: 14px 4px; cursor: pointer;
    display: grid; grid-template-columns: 130px 1fr; gap: 16px; align-items: start;
  }
  .result-row:hover { background: var(--accent-tint); }
  .result-meta { font-family: var(--mono); font-size: 12px; color: var(--text-secondary); padding-top: 2px; }
  .result-meta .kind-dot {
    display: inline-block; width: 8px; height: 8px; border-radius: 50%; margin-right: 6px;
    vertical-align: middle; position: relative; top: -1px;
  }
  .sev-dots { margin-top: 6px; display: flex; gap: 4px; }
  .sev-dots span { display: inline-block; width: 7px; height: 7px; border-radius: 50%; }
  .result-title { font-size: 17px; font-weight: 500; margin: 0 0 4px; }
  .result-tags { font-family: var(--mono); font-size: 12px; color: var(--text-secondary); }
  .result-tags .type-label { color: var(--text-primary); font-weight: 600; margin-right: 8px; }

  .result-detail {
    grid-column: 1 / -1; padding: 16px 0 4px 0; max-width: 720px;
    overflow: hidden; max-height: 0; transition: max-height 0.25s ease;
  }
  .result-detail.open { max-height: 4000px; }
  .result-detail-inner { padding-top: 8px; border-top: 1px dashed var(--border); }
  .result-detail h1 { font-size: 20px; }
  .result-detail h2 { font-size: 16px; margin-top: 20px; }
  .result-detail blockquote {
    margin: 12px 0; padding: 4px 16px; border-left: 3px solid var(--border); color: var(--text-secondary);
  }
  .result-detail table { border-collapse: collapse; font-size: 14px; margin: 12px 0; }
  .result-detail th, .result-detail td { border: 1px solid var(--border); padding: 6px 10px; text-align: left; }
  .result-detail code { font-family: var(--mono); background: var(--bg); padding: 1px 4px; border-radius: 3px; }
  .source-link { display: inline-block; margin-top: 12px; font-family: var(--mono); font-size: 12px; }

  .empty-state { padding: 40px 4px; color: var(--text-secondary); max-width: 520px; }
  .empty-state h3 { font-family: var(--serif); font-size: 18px; color: var(--text-primary); margin-bottom: 6px; }

  @media (prefers-reduced-motion: reduce) {
    .result-detail { transition: none; }
  }
  @media (max-width: 800px) {
    .layout { grid-template-columns: 1fr; }
    aside { border-right: none; border-bottom: 1px solid var(--border); }
    .result-row { grid-template-columns: 1fr; }
    .result-meta { display: flex; gap: 10px; }
  }
</style>
</head>
<body>

<header>
  <h1>Compass AI Research Archive</h1>
  <p class="tagline">Meridian Health Network — fictional sample dataset</p>
</header>

<div class="search-bar">
  <input type="search" id="search-input" placeholder="Search titles, tags, findings…" autocomplete="off">
</div>

<div class="layout">
  <aside>
    <h2>Kind</h2>
    <div id="kind-filters"></div>

    <h2>Type</h2>
    <div id="type-filters"></div>

    <h2>Tags</h2>
    <div class="tag-cloud" id="tag-filters"></div>

    <button id="reset-filters">Clear all filters</button>
  </aside>

  <main>
    <div class="result-count" id="result-count"></div>
    <ul class="results" id="results-list"></ul>
    <div class="empty-state" id="empty-state" style="display:none;">
      <h3>No matches</h3>
      <p>Nothing fits the current search and filters. Try clearing a filter in the sidebar, or broadening the search text.</p>
    </div>
  </main>
</div>

<script id="research-data" type="application/json">__DATA_JSON__</script>
<script>
(function () {
  const records = JSON.parse(document.getElementById('research-data').textContent);
  const TYPE_LABELS = __TYPE_LABELS_JSON__;
  const KIND_LABELS = { raw: 'Sessions', finding: 'Findings', component: 'Components', analytics: 'Analytics', deliverable: 'Deliverables' };
  const KIND_COLORS = { raw: 'var(--kind-raw)', finding: 'var(--kind-finding)', component: 'var(--kind-component)', analytics: 'var(--kind-analytics)', deliverable: 'var(--kind-deliverable)' };
  const SEV_COLORS = { critical: 'var(--sev-critical)', high: 'var(--sev-high)', medium: 'var(--sev-medium)', low: 'var(--sev-low)' };

  const state = {
    query: '',
    kinds: new Set(['raw', 'finding', 'component', 'analytics', 'deliverable']),
    types: new Set(),
    tags: new Set(),
    openId: null,
  };

  const allKinds = ['raw', 'finding', 'component', 'analytics', 'deliverable'];
  const allTypes = [...new Set(records.map(r => r.type).filter(Boolean))].sort();
  const allTags = [...new Set(records.flatMap(r => r.tags))].sort();
  state.types = new Set(allTypes);

  function countFor(predicate) {
    return records.filter(predicate).length;
  }

  function renderKindFilters() {
    const el = document.getElementById('kind-filters');
    el.innerHTML = allKinds.map(k => {
      const count = countFor(r => r.kind === k);
      const checked = state.kinds.has(k) ? 'checked' : '';
      return `<label class="filter-row"><input type="checkbox" data-kind="${k}" ${checked}>${KIND_LABELS[k]}<span class="count">${count}</span></label>`;
    }).join('');
    el.querySelectorAll('input[data-kind]').forEach(input => {
      input.addEventListener('change', () => {
        const k = input.getAttribute('data-kind');
        if (input.checked) state.kinds.add(k); else state.kinds.delete(k);
        render();
      });
    });
  }

  function renderTypeFilters() {
    const el = document.getElementById('type-filters');
    el.innerHTML = allTypes.map(t => {
      const count = countFor(r => r.type === t);
      const checked = state.types.has(t) ? 'checked' : '';
      return `<label class="filter-row"><input type="checkbox" data-type="${t}" ${checked}>${TYPE_LABELS[t] || t}<span class="count">${count}</span></label>`;
    }).join('');
    el.querySelectorAll('input[data-type]').forEach(input => {
      input.addEventListener('change', () => {
        const t = input.getAttribute('data-type');
        if (input.checked) state.types.add(t); else state.types.delete(t);
        render();
      });
    });
  }

  function renderTagFilters() {
    const el = document.getElementById('tag-filters');
    el.innerHTML = allTags.map(tag => {
      const active = state.tags.has(tag) ? 'active' : '';
      return `<button type="button" class="tag-chip ${active}" data-tag="${tag}">${tag}</button>`;
    }).join('');
    el.querySelectorAll('.tag-chip').forEach(btn => {
      btn.addEventListener('click', () => {
        const tag = btn.getAttribute('data-tag');
        if (state.tags.has(tag)) state.tags.delete(tag); else state.tags.add(tag);
        render();
      });
    });
  }

  function matches(record) {
    if (!state.kinds.has(record.kind)) return false;
    if (record.type && allTypes.includes(record.type) && !state.types.has(record.type)) return false;
    if (state.tags.size > 0 && ![...state.tags].every(t => record.tags.includes(t))) return false;
    if (state.query && !record.searchText.includes(state.query)) return false;
    return true;
  }

  function severityDots(sev) {
    if (!sev) return '';
    const order = ['critical', 'high', 'medium', 'low'];
    const dots = order.filter(k => sev[k] > 0).map(k => `<span title="${sev[k]} ${k}" style="background:${SEV_COLORS[k]}"></span>`);
    return dots.length ? `<div class="sev-dots">${dots.join('')}</div>` : '';
  }

  function renderResults() {
    const filtered = records.filter(matches).sort((a, b) => (b.date || '').localeCompare(a.date || ''));
    const list = document.getElementById('results-list');
    const emptyState = document.getElementById('empty-state');
    document.getElementById('result-count').textContent = `${filtered.length} of ${records.length}`;

    if (filtered.length === 0) {
      list.innerHTML = '';
      emptyState.style.display = 'block';
      return;
    }
    emptyState.style.display = 'none';

    list.innerHTML = filtered.map(r => {
      const isOpen = state.openId === r.id;
      return `
        <li>
          <div class="result-row" data-id="${r.id}">
            <div class="result-meta">
              <span class="kind-dot" style="background:${KIND_COLORS[r.kind]}"></span>${r.date || ''}
              ${severityDots(r.severity)}
            </div>
            <div>
              <p class="result-title">${r.title}</p>
              <div class="result-tags">
                ${r.type ? `<span class="type-label">${TYPE_LABELS[r.type] || r.type}</span>` : ''}
                ${r.tags.join(', ')}
              </div>
            </div>
            <div class="result-detail ${isOpen ? 'open' : ''}" id="detail-${cssEscape(r.id)}">
              <div class="result-detail-inner">
                ${isOpen ? r.html : ''}
                ${isOpen ? `<a class="source-link" href="${r.path}">Open source file: ${r.path}</a>` : ''}
              </div>
            </div>
          </div>
        </li>`;
    }).join('');

    list.querySelectorAll('.result-row').forEach(row => {
      row.addEventListener('click', (e) => {
        if (e.target.closest('a')) return; // let source-file links navigate normally
        const id = row.getAttribute('data-id');
        state.openId = state.openId === id ? null : id;
        render();
        if (state.openId) {
          const el = document.getElementById(`detail-${cssEscape(state.openId)}`);
          if (el && typeof el.scrollIntoView === 'function') {
            el.scrollIntoView({ block: 'nearest', behavior: 'smooth' });
          }
        }
      });
    });
  }

  function cssEscape(s) { return s.replace(/[^a-zA-Z0-9_-]/g, '_'); }

  function render() {
    renderKindFilters();
    renderTypeFilters();
    renderTagFilters();
    renderResults();
  }

  document.getElementById('search-input').addEventListener('input', (e) => {
    state.query = e.target.value.trim().toLowerCase();
    render();
  });

  document.getElementById('reset-filters').addEventListener('click', () => {
    state.query = '';
    state.kinds = new Set(allKinds);
    state.types = new Set(allTypes);
    state.tags = new Set();
    state.openId = null;
    document.getElementById('search-input').value = '';
    render();
  });

  render();
})();
</script>
</body>
</html>
"""


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    records = (
            build_raw_records()
            + build_findings_records()
            + build_component_records()
            + build_analytics_records()
            + build_deliverable_records()
    )
    for r in records:
        r["searchText"] = build_search_text(r)

    data_json = json.dumps(records, ensure_ascii=False)
    data_json = data_json.replace("</script", "<\\/script").replace("</Script", "<\\/Script")

    html = HTML_TEMPLATE.replace("__DATA_JSON__", data_json)
    html = html.replace("__TYPE_LABELS_JSON__", json.dumps(TYPE_LABELS))

    old = OUTPUT_FILE.read_text(encoding="utf-8") if OUTPUT_FILE.exists() else None

    if args.check:
        if html != old:
            print(f"❌ {OUTPUT_FILE} is out of date. Run without --check to regenerate.", file=sys.stderr)
            sys.exit(1)
        print(f"✅ {OUTPUT_FILE} is up to date ({len(records)} records)")
        return

    OUTPUT_FILE.write_text(html, encoding="utf-8")
    print(f"✅ Wrote {OUTPUT_FILE} ({len(records)} records: "
          f"{sum(1 for r in records if r['kind']=='raw')} sessions, "
          f"{sum(1 for r in records if r['kind']=='finding')} findings, "
          f"{sum(1 for r in records if r['kind']=='component')} components, "
          f"{sum(1 for r in records if r['kind']=='analytics')} analytics summaries, "
          f"{sum(1 for r in records if r['kind']=='deliverable')} deliverables)")


if __name__ == "__main__":
    main()