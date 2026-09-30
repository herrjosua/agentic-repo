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

Every folder holds at least one filled-in sample file. 13 folders have an
`example-*.md`; the other 7 (`research-plans/`, `facilitation-guides/`,
`research-readouts/`, `personas/`, `wireframes/`, `user-flows/`,
`style-guide/`) have none, and their samples use descriptive names instead
(e.g. `personas/dana-overwhelmed-new-admin.md`, which other files link to by
that name). These are meant to be replaced by real content over time, not
kept as permanent fixtures, but they show what a fully-specified file in each
folder looks like rather than an empty shell.

### Two fictional frames

The sample corpus uses two separate fictional frames. They are not one story,
and nothing here should be read as connecting them:

- **Fernway** — a fictional workspace product. Its Q1 onboarding-flow
  redesign, centered on the persona Dana (a first-time workspace admin), runs
  through the deliverables tagged `project-onboarding` (most of the
  `example-*.md` files, plus files such as
  `research-plans/onboarding-usability-study-q1.md` and
  `personas/dana-overwhelmed-new-admin.md`), the onboarding v2 design-system
  snapshot and style guide (`design-system/example-design-system.md`,
  `style-guide/foundations-v3.md`), and the participant notes of
  `research/raw/2026-01-19-onboarding-usability-test/`.
- **Meridian Health Network / Compass AI** — a fictional healthcare
  organization and its AI modernization program. The README describes the
  dataset under this frame, and it covers the ambient scribe, prior
  authorization, care coordination, HIM, governance and rollout work,
  including deliverables such as `personas/physician-longitudinal-scribe-user.md`
  and `design-system/v4-1-status-indicator-component.md`.

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
