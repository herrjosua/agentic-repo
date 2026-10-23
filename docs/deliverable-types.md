# Deliverable Types Reference

Reference for the 20 notional deliverable folders added in `feature-002`. See
each folder's `_index.md` for its file list, and [`decisions.md`](decisions.md)
(entries 6–8) for the rationale behind the choices below. `docs/` is not a
deliverable folder; it holds the repo's documentation (see
[`README.md`](README.md) for the full list).

## Why these folders exist

Before `feature-002`, the repo only modeled one kind of research artifact:
a `finding` in `research/findings/`. In practice, a UX team produces many
other kinds of deliverable — research plans, personas, wireframes, and so
on — and none of those fit the `finding` shape. Rather than force everything
into one type, each distinct deliverable type got its own top-level folder,
sibling to `research/`, `design-tokens/`, and `analytics/`. This keeps each
type independently queryable and filterable (an agent or a human can ask
"show me all heuristic evaluations" without wading through unrelated files),
and matches the pattern the repo already used for `design-tokens/` and
`analytics/` — different content, different cadence, its own folder.

## The stub pattern (why most folders hold real content, but `prototypes/` doesn't)

Most deliverable types are things you'd actually write in Markdown — a
research plan, a persona, a heuristic evaluation. Those folders hold real
content directly (`source_type: native` in the frontmatter).

`prototypes/` is the one exception. Click-through prototypes live in Figma;
coded prototypes live in a GitHub repo. Neither has a real file that belongs
in *this* repo — duplicating either one would just create a second, stale
copy of something that already has a proper home elsewhere. So every file in
`prototypes/` is a **stub**: frontmatter plus a couple of sentences of
description, with a `url` field pointing at the real thing. That's why
`prototypes/` defaults to `source_type: figma-link` instead of `native`, and
why it's the only folder marked "Stub-only: Yes" in the reference below.

This same stub pattern is meant to extend to other externally-owned content
later — e.g. a Confluence-native Research Plan at a client site — via the
`confluence-link` / `docx-link` values already reserved in `source_type`,
even though nothing uses them yet.

### `source_type` values

`new_research_session.py` accepts exactly these values (its `SOURCE_TYPES`
allowlist, kept in sync by hand with the CRUD UI's backend validation):

| Value | Meaning |
|---|---|
| `native` | The file holds the real content. Default for every folder except `prototypes/`. |
| `figma-link` | Stub pointing at a Figma file. Default for `--proto-type clickthrough`. |
| `github-link` | Stub pointing at a GitHub repo. Default for `--proto-type coded`. |
| `confluence-link` | Stub pointing at a Confluence page. Reserved; unused today. |
| `docx-link` | Stub pointing at a Word document. Reserved; unused today. |
| `figma-export` | Allowed by the scaffold script; purpose not recorded. |

Any value other than `native` makes the generated body a stub (the script
treats `source_type != native` the same as a stub-only folder).

## The Evidence basis line

The Evidence basis line is a one-line statement of how a deliverable's
claims trace back to raw evidence. The format, from
[`synthesis-audit-2026-09-29.md`](synthesis-audit-2026-09-29.md#evidence-basis-line)
(where it was introduced), is:

`**Evidence basis:** <Observed | Inferred | Illustrative | Mixed>. <the raw path(s) and lines>.`

It goes as the first line of the record's first section. The audit doc's
format line writes "mixed" in lower case; it and "Mixed" are the same label.
The audit doc gives the format only. The labels were defined on 2026-10-15:

- **Observed:** the claims are stated in raw sessions, and each cites its
  lines.
- **Inferred:** the record's own reasoning from raw evidence. The evidence is
  cited, but no session states the conclusion.
- **Illustrative:** a built example or scenario, not a record of what
  happened.
- **Mixed:** some of each, with the record saying which sections are which.

For how they're used in practice, see the records that carry the line
today: `personas/physician-longitudinal-scribe-user.md`,
`mental-models/care-coordinator-alert-ranking.md` and
`user-flows/ambient-scribe-session-lock-recovery.md`.

**Visual artifacts.** The repo holds a Markdown record that describes and
points to the visual, not the visual itself: `prototypes/` files are
stubs with `source_type: figma-link` (or `github-link`) and a `url`, and
`mockups/` files carry a `figma_url`. On such a record the Evidence basis
line covers the claims the Markdown makes, not the pixels in Figma or Adobe.

**Scope.** Evidence basis lines belong on working records that need to
trace back to raw evidence; a client-style summary carries highlights plus a
pointer to the research store instead.

## The frontmatter, and why it's split this way

Every file in every folder starts with the same base block:

```yaml
title: ""                  # the file's own title
date: YYYY-MM-DD           # when the file was written/last meaningfully updated
status: draft               # draft | in-review | final | superseded
tags: []                    # validated repo-wide against research/findings/tags.md
related_findings: []        # cross-links into research/findings/
source_type: native         # native | figma-link | github-link | confluence-link | docx-link | figma-export
```

On top of that, each folder adds a small number of type-specific fields (for
example, `research-plans/` adds `method` and `study_dates`; `personas/` adds
`segment` and `based_on`). The base fields are what make every deliverable
type queryable the same way, regardless of what it is; the extra fields
capture what's actually distinct about that type. See each folder's entry
below for its specific additions, or a filled-in file inside the folder for
an illustration.

### Extra fields per folder

From `DELIVERABLE_SCHEMAS` in `research/scripts/new_research_session.py`, in
prompt order. The default is what `--no-prompt` writes. Two fields are not in
the schema because flags set them: `designer` (`--designer`, every folder
except `heuristic-evaluations/`) and, for `prototypes/` only, `type`
(`--proto-type clickthrough|coded`).

| Folder | Extra fields (default) |
|---|---|
| `research-plans/` | `method` (""), `study_dates` ({start: "", end: ""}), `related_guide` ("") |
| `facilitation-guides/` | `related_plan` ("") |
| `topline-summaries/` | `related_plan` (""), `session_dates` ([]) |
| `research-readouts/` | `related_analytics` ([]), `presented_to` ([]) |
| `heuristic-evaluations/` | `method` ("heuristic-evaluation"), `evaluator` (""), `scope` (""), `severity_scale` ("") |
| `accessibility-screenings/` | `wcag_level` (""), `scope` (""), `issues_found` (0) |
| `service-topology/` | `scope` (""), `version` ("") |
| `personas/` | `segment` (""), `based_on` ([]) |
| `mental-models/` | `scope` ("") |
| `mindsets/` | `segment` ("") |
| `journey-maps/` | `persona_ref` (""), `scope` ("") |
| `thumbnails/` | `concept` (""), `related_wireframes` ([]) |
| `wireframes/` | `fidelity` ("lo-fi"), `flow_ref` ("") |
| `user-flows/` | `flow_name` (""), `screens_count` (0) |
| `wireflows/` | `flow_name` ("") |
| `storyboards/` | `scenario` ("") |
| `mockups/` | `fidelity` ("hi-fi"), `figma_url` ("") |
| `prototypes/` | `url` (""), `stack` ("") |
| `design-system/` | `version` (""), `related_style_guide` ("") |
| `style-guide/` | `version` ("") |

## What each folder contains right now

`_index.md` in every folder is generated by `research/scripts/build_index.py`
(extended in `feature-002` to walk all 20 deliverable folders, not just
`research/findings/`) — a flat table of title, status, tags, source type,
last updated, and related findings for every file in that folder. Never
hand-edit it; re-run `build_index.py` after adding or changing a deliverable
file, and use `--check` to catch drift or a dangling cross-link (a
`persona_ref`, `flow_ref`, `related_plan`, etc. that points at a file that
doesn't exist) in CI.

No folder is required to hold a record. An empty deliverable folder is fine:
do not create sample, placeholder or invented-product records to fill one.
Every record in these folders is real corpus content and is read by search,
the CRUD UI and Ask the same way as any other record.

### The fictional frame

The whole corpus uses one fictional frame:

- **Meridian Health Network / Compass AI** — a fictional healthcare
  organization and its AI modernization program. The README describes the
  dataset under this frame, and it covers the ambient scribe, prior
  authorization, care coordination, HIM, the patient scheduling chatbot, the
  clinician dashboard, Compass AI practice setup (onboarding), the design
  system, and governance and rollout work, including deliverables such as
  `personas/physician-longitudinal-scribe-user.md`,
  `personas/practice-administrator-compass-ai-setup.md` and
  `design-system/v4-1-status-indicator-component.md`.

`research/projects.yml` and each file's `project-*` tag show which project a
record belongs to.

---

### `research-plans/`
**Research Plans** — Research

Pre-study artifacts: objectives, method, screener, timeline.

Holds real content.

---

### `facilitation-guides/`
**Facilitation / Conversation Guides** — Research

The discussion guide or script used to run a research session.

Holds real content.

---

### `topline-summaries/`
**Topline Summaries** — Research

Quick-turn, pre-synthesis takeaways, often written the same day as sessions.

Holds real content.

---

### `research-readouts/`
**Research Readouts** — Research

The polished, presented synthesis of one or more findings/analytics.

Holds real content.

---

### `heuristic-evaluations/`
**Heuristic / Usability Evaluations** — Research

Expert-review method — not moderated research.

Holds real content.

---

### `accessibility-screenings/`
**Accessibility Screenings** — Research

Audit-style evaluation against WCAG criteria.

Holds real content.

---

### `service-topology/`
**Subway Map / Service Topology** — Design

A service blueprint drawn like a transit map.

Holds real content.

---

### `personas/`
**Personas / Models / Mindsets** — Design

Fictional user archetypes grounded in research.

Holds real content.

---

### `mental-models/`
**Mental Models** — Design

How users conceptually think about a system, independent of the UI.

Holds real content.

---

### `mindsets/`
**Mindsets** — Design

Segmentation by attitude/motivation, not identity.

Holds real content.

---

### `journey-maps/`
**Journey Maps** — Design

End-to-end user journey across touchpoints.

Holds real content.

---

### `thumbnails/`
**Thumbnails** — Design

Rapid, low-fidelity sketches exploring many layout ideas fast, before a wireframe is chosen.

Holds real content.

---

### `wireframes/`
**Wireframes** — Design

Structured layout, low-fidelity.

Holds real content.

---

### `user-flows/`
**User Flows** — Design

The sequence/logic between screens.

Holds real content.

---

### `wireflows/`
**Wireflows** — Design

Flow diagram combined with screen wireframes.

Holds real content.

---

### `storyboards/`
**Storyboards** — Design

Narrative, often hand-drawn, showing a user's situational context.

Holds real content.

---

### `mockups/`
**Mockups** — Design

High-fidelity visual design.

Holds real content.

---

### `prototypes/`
**Prototypes (Click-through + Coded)** — Design

Stub-only folder — both click-through (Figma) and coded (GitHub) prototypes point to external tools rather than duplicating content.

Stub-only.

---

### `design-system/`
**Design System** — Design

The canonical component/pattern library.

Holds real content.

---

### `style-guide/`
**Style Guide / Micro-code** — Design

A lightweight design system subset — colors, type, spacing basics.

Holds real content.

---

## Decision records (`decisions/`)

A decision record answers "why was this decided?" months later, with its evidence. It is its own
record kind (`kind: decision`, id `decision:<slug>`), decided on 2026-10-04 (RR-153 decision 4)
and built in RR-157. It is not a deliverable: `decisions/` is not one of the 20 folders above, has
no `DELIVERABLE_SCHEMAS` entry and no `source_type` or `designer`.

**Not the same as [`docs/decisions.md`](decisions.md).** `decisions/` holds decisions about the
product the corpus studies (Compass AI), backed by research records. `docs/decisions.md` is the log
of decisions about this repo and its tooling. Both use "not recorded" the same way.

### Frontmatter

```yaml
title: ""                      # the decision, as a short name
date: YYYY-MM-DD               # when this record was written or last meaningfully updated
status: draft                  # the document's status: draft | in-review | final | superseded
decision_status: proposed      # the decision's: proposed | accepted | shipped | reversed | superseded | not-decided
decision_status_source:        # the lines that support decision_status, as path:lines
  - research/raw/<session>/session-notes.md:27,31
date_decided: not recorded     # YYYY-MM-DD, or exactly "not recorded"
decided_by: not recorded       # a person, role or forum, or exactly "not recorded"
superseded_by: ""              # decisions/<slug>.md; set if and only if decision_status is superseded
evidence:                      # raw sessions and findings, with the lines relied on
  - source: research/raw/<session>/session-notes.md
    lines: "31,42"
  - source: research/findings/<topic>.md
    lines: "30-36"
tags: []                       # glossary tags plus exactly one project-* tag
related_findings: []           # findings/*.md filenames
related_components: []         # design-tokens/components/*.md slugs
```

`status` stays the document status so the CRUD UI's edit validation, which only accepts the
document statuses, keeps working. The decision's own state goes in `decision_status`:

- **proposed:** recommended or designed; no record says it was adopted.
- **accepted:** a record says it was adopted, but not that it is live.
- **shipped:** a record says it is in use.
- **reversed** and **superseded:** a record says so; `superseded_by` names the replacement.
- **not-decided:** the question is on record, and no decision is.

### Body

Five `##` sections, in this order: `Decision`, `Alternatives considered`, `Rationale`,
`Conditions to revisit`, `Not recorded`. A section the corpus can't fill says `not recorded`.
`Rationale` starts with an [Evidence basis line](#the-evidence-basis-line). Write citations as
`` `path/to/record.md:31,42` `` (repo-relative), or `` `:31,42` `` for the file cited in full just
before it.

Writing rules:
- Every field and claim is sourced from a named record's lines, or written as `not recorded`. Never
  invent an owner, a date, a decider or a status.
- Write `not recorded` exactly: lower case, no "unknown", "N/A" or "TBD", so Ask can quote it.
- Designers, evaluators and researchers named on a record are not deciders unless a record says
  they decided.
- Only write that an alternative was "rejected" if a record says so; otherwise write "recommended
  against" and cite the line.
- Where a raw session has a correction file, cite the correction and use its corrected figures.

### Evidence, and how it reaches the CRUD UI

`evidence:` must cite at least one raw session directly, not only findings. The CRUD UI's
provenance links (`backend/ask/provenance.js`) are read from a record's html, never from its
frontmatter, and don't follow a finding to its raw sessions.

`build_search_ui.py` (and so `export_records.py` and `search.html`) opens each decision record's
html with a generated block: the decision status, date decided and decided by, the status sources,
and every evidence link with its method, n and date. Method and date come from the cited session's
frontmatter, and n from `**Count:**` in its `participants.md`, so they are never typed by hand.
Ask the Repo retrieves that block with the body. The same fields are in the exported record's
`decision` key, which is `null` on every other kind.

### Validation

`build_index.py` (and `--check`) fails on:
- a missing required field;
- a `status` or `decision_status` outside its list;
- a near-miss spelling of `not recorded`;
- a `date_decided` that isn't a date;
- a `superseded_by` that doesn't match `decision_status` or doesn't resolve;
- an evidence entry, status source or body citation that points at a missing file or past its last
  line;
- evidence with no raw session;
- a missing or empty section, or a `Rationale` without an Evidence basis line;
- an unknown tag, a missing or extra `project-*` tag, or a dangling `related_findings` /
  `related_components`.

It also writes `decisions/_index.md`. There is no scaffolder: write the file by hand, then run
`build_index.py`.
