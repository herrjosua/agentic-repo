---
title: Ambient Scribe — Sound-Alike Medication Flag
date: 2026-02-24
status: in-review
tags:
  - ambient-scribe
  - medication-safety
  - wireframe
  - project-ambient-scribe
related_findings:
  - ../research/findings/ambient-scribe-post-ga-refinements.md
source_type: native
designer: Sam Okafor
fidelity: lo-fi
flow_ref:
---

# Ambient Scribe — Sound-Alike Medication Flag

## Description
**Evidence basis:** Mixed. Observed (the 2026-02-10 concept-test results, from `raw/2026-02-10-ambient-scribe-medication-flag-concept/session-notes.md:36-48,51-52,62-64,70`); illustrative (the layout, the hover/tap copy and the tip's wording are the designer's spec, not recorded in the test).

Lo-fi layout for the distinct sound-alike-medication flag tested in the 2026-02-10 concept
test, which calls for a larger-N validation pass before a build-ready spec. Applies to the `ambient-scribe-widget` component's draft-review surface, inside the
`encounter-view` screen. Separate from the existing generic `confidence-highlighted` variant —
this flag reads specifically as "check this drug name," not "low confidence generally."

## Details
- **Placement:** inline, immediately after the medication name — tested 5:1 over a right-hand
  margin badge, since participants didn't want to look away from the text.
- **Visual treatment:** small amber pill-shaped badge, distinct in shape and color from the
  existing subtle low-confidence underline, so the two signals are never visually conflated.
- **Copy:** short on-hover/on-tap label — "Possible sound-alike medication name — verify before
  signing" — worded to prompt verification, not to assert an error.
- **Adjacent messaging (new):** a one-time inline tip, shown the first time a clinician encounters
  the flag, stating that lines *without* this flag still warrant normal review — directly
  addressing the over-trust-on-unflagged-lines risk found in 2 of 6 concept-test participants.
- **Open item:** in the 2026-02-10 test, one deliberately seeded false positive was accepted by
  all 6 participants as "worth a second look, not annoying" — final
  threshold tuning is an engineering/detection decision, not a layout decision, and is out of
  scope for this wireframe.
