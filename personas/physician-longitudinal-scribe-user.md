---
title: The Longitudinal Physician — Ambient Scribe
date: 2026-02-26
status: final
tags:
  - ambient-scribe
  - persona
  - longitudinal
  - trust-in-ai
  - project-ambient-scribe
related_findings:
  - ../research/findings/ambient-scribe.md
  - ../research/findings/ambient-scribe-post-ga-refinements.md
source_type: native
designer: Sam Okafor
segment: Physician, regular ambient-scribe user across multiple release cycles
based_on:
  - ambient-scribe.md
  - ambient-scribe-post-ga-refinements.md
---

# The Longitudinal Physician — Ambient Scribe

## Summary
**Evidence basis:** Observed (v0.1 to GA candidate, from P09 in `raw/2025-02-25-usability-test-ambient-scribe-v01/session-notes.md:36-37`, `raw/2025-09-23-usability-test-ambient-scribe-v02/session-notes.md:36-37` and `raw/2026-01-13-usability-test-ambient-scribe-ga-release-candidate/session-notes.md:36-37`); inferred (post-GA stage, second and third goals and both frustrations, from other participants in `raw/2026-02-10-ambient-scribe-medication-flag-concept/session-notes.md:51-57` and `raw/2026-02-17-session-lock-during-dictation/session-notes.md:54-60`).

Modeled on P09 (Internal Medicine), one of the 3 participants who returned from v0.1 for v0.2, and
the one confirmed in all three ambient-scribe testing rounds — v0.1 (Feb 2025), v0.2 (Sep 2025),
and the GA candidate (Jan 2026). Represents the
clinician whose relationship with the tool has actually changed over a year of iteration, not a
first-time impression.

## Goals
- Trust the tool enough to stop reading every generated line, without trusting it blindly. *(P09,
  v0.1 to GA candidate)*
- Catch the specific error types that matter clinically (medication names) rather than treating
  all uncertainty as equally worth flagging. *(Inferred from P22, 2026-02-10; not observed for
  P09)*
- Not lose work to session/security interruptions that are unrelated to the clinical task.
  *(Inferred from P31 and P33, 2026-02-17; not observed for P09)*

## What changed for this persona, round over round
- **v0.1 → v0.2:** Accuracy improved, but reading behavior didn't — still read every line, despite
  fewer errors to catch.
- **v0.2 → GA candidate:** The first behavior change came from *visible uncertainty* (per-line
  confidence highlighting), not from further accuracy gains — this persona began skimming
  high-confidence lines for the first time.
- **Post-GA (Feb 2026, inferred from other participants):** The next trust lever is specificity,
  not just visibility — a distinct medication-safety flag reads as more actionable than generic low
  confidence, but risks over-trusting anything left unflagged if that distinction isn't actively
  managed in the UI. This is not P09's observed experience: it comes from P22 and P24 in the
  2026-02-10 concept test.

## Frustrations
- Generic "low confidence" signals don't tell this persona *what kind* of thing to double-check.
  *(Inferred from P22, 2026-02-10)*
- Session locks during dictation currently look identical to data loss, which erodes trust in the
  tool independent of transcription accuracy itself. *(Inferred from P31 and P33, 2026-02-17)*

## Based on
P09's sessions in the three ambient-scribe test rounds (2025-02-25, 2025-09-23, 2026-01-13). The
post-GA stage, the second and third goals and both frustrations come from other participants in the
2026-02-10 medication-flag concept test and the 2026-02-17 session-lock contextual inquiry; no raw
session places P09 in either.
