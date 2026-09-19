---
title: Ambient Scribe — Sound-Alike Medication Flag
date: 2026-02-24
status: in-review
tags:
  - ambient-scribe
  - medication-safety
  - wireframe
related_findings:
  - ../research/findings/ambient-scribe-post-ga-refinements.md
source_type: native
designer: Sam Okafor
fidelity: lo-fi
flow_ref:
---

# Ambient Scribe — Sound-Alike Medication Flag

## Description
Lo-fi layout for the distinct sound-alike-medication flag validated in the 2026-02-10 concept
test. Applies to the `ambient-scribe-widget` component's draft-review surface, inside the
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
- **Open item:** false-positive tolerance testing (2026-02-10) suggests the underlying detection
  threshold can run looser than strict-precision defaults without frustrating clinicians — final
  threshold tuning is an engineering/detection decision, not a layout decision, and is out of
  scope for this wireframe.
