# Project tags

Every record in the repo belongs to exactly one project, recorded as a `project-*` tag in the
record's `tags` list. Records that belong to no single project are tagged
`project-cross-cutting`. This exists so a project filter means something: the Research Repo CRUD
UI's `POST /api/ask` filters by tag (`record.tags.includes(project)`), because records have no
separate project field.

This is deliberately thin structure on top of the existing tags, not a tagging redesign. Topic tags
like `ambient-scribe` or `onboarding` stay as they are and can still span projects; only the
`project-*` tag is guaranteed to be single-valued.

## The project list

The machine-readable source is [`research/projects.yml`](../research/projects.yml) (it lives under
`research/` so `sync-demo.yml` copies it to the demo repo). Each id is also defined in
[`research/findings/tags.md`](../research/findings/tags.md).

| Tag | Label | Records |
|---|---|---|
| `project-ambient-scribe` | Ambient AI Scribe | 19 |
| `project-onboarding` | Onboarding | 21 |
| `project-care-coordination` | Care Coordination & Alert Triage | 8 |
| `project-design-system` | Design System | 6 |
| `project-prior-auth` | AI-Assisted Prior Authorization | 5 |
| `project-him` | HIM Coding, Billing & Release of Information | 5 |
| `project-patient-chatbot` | Patient Scheduling Chatbot | 5 |
| `project-clinician-dashboard` | Clinician Dashboard | 3 |
| `project-cross-cutting` | Cross-cutting (no single project) | 25 |
| | **Total** | **97** |

Counts are as of 2026-09-28, from `export_records.py` output. To recount:

```
python research/scripts/export_records.py --summary | python -c "import json,sys,collections; \
print(collections.Counter(t for r in json.load(sys.stdin) for t in r['tags'] if t.startswith('project-')))"
```

The CRUD UI's mock project ids (`checkout`, `onboarding`, `mobile-nav`, `design-system`) are
placeholders. Only onboarding and design-system correspond to real content here, as
`project-onboarding` and `project-design-system`; the Ask tab wiring maps its ids to these tags.

## Where each record's project tag lives

| Record kind | Where the `project-*` tag comes from |
|---|---|
| Findings (`research/findings/`) | The file's own `tags:` frontmatter |
| Analytics summaries (`analytics/summaries/`) | The file's own `tags:` frontmatter |
| Deliverables (the 20 feature-002 folders) | The file's own `tags:` frontmatter |
| Raw sessions (`research/raw/`) | The `raw:` map in `research/projects.yml`, keyed by session folder |
| Components (`design-tokens/components/`) | The `components:` map in `research/projects.yml`, keyed by component slug |

Raw sessions can't carry the tag themselves because `raw/` is append-only, and component files are
generated output. For those two kinds `build_search_ui.py` (and so `export_records.py` and
`search.html`) adds the mapped tag when it loads the record. `projects.yml` is the only source for
them: any `project-*` tag already in a raw session's own frontmatter is replaced by the mapped one,
so every record ends up with exactly one.

## How a project was assigned

Each record's project comes from what the record itself is about, using its linked findings only
to break ties. So a record can land in a different project from the finding it cites. For example,
the 2025-07-01 design system component audit is `project-design-system` even though its only
finding is the cross-cutting accessibility one. A record that spans several projects (the Skeptical
Verifier mindset, the status-indicator screening) is cross-cutting.

## Adding a record

- **Finding, analytics summary, or deliverable:** include exactly one `project-*` tag in `--tags`
  (or in the frontmatter).
- **Raw session:** `new_research_session.py` (and so the CRUD UI's New session button) adds the
  new folder to the `raw:` map as `project-cross-cutting` automatically, by inserting one line —
  the rest of the file is left as is. Change it there once the session's project is known.
  A folder created any other way needs its line added by hand.
- **Component:** add a line for it to the `components:` map in `research/projects.yml`.
- **New project:** add it under `projects:` in `research/projects.yml` *and* to
  `research/findings/tags.md`, then update the table above.

Until a raw session or component is mapped, the loaders fall back to `project-cross-cutting` and
print a warning to stderr. The record is never dropped and the export never fails because of it.
`build_index.py` also only warns about an unmapped raw session or component in a normal run (the
one the CRUD UI reruns after every edit), and fails on it only under `--check`, the CI gate.

`build_index.py` fails in every mode on:

- an entry in `projects.yml` for a raw session folder or component that doesn't exist;
- an entry pointing at a project id that isn't listed under `projects:`;
- a project id that doesn't start with `project-` or isn't in `tags.md`, or a missing
  `project-cross-cutting`;
- a finding, analytics summary, or deliverable with zero or more than one `project-*` tag, or one
  that isn't listed in `projects.yml`.

If `research/projects.yml` doesn't exist in a checkout (for example the throwaway test corpora),
project tagging is off: nothing is added and nothing is validated.

## Caveat: editing raw sessions in the CRUD UI

The CRUD UI's edit form pre-fills `tags` from the exported record and its `PUT` merges them into
the file. For a raw session, the exported tags include the `project-*` tag added from
`projects.yml`, so saving an edit would write that tag into the session's `raw/` frontmatter. The
loader tolerates this (the mapped tag replaces it, so the record still has exactly one), but it is
still a write into `raw/` that `projects.yml` is meant to avoid. **The CRUD UI should strip
`project-*` tags from a raw session's `tags` before saving an edit.**
