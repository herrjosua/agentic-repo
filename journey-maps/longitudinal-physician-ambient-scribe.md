---
title: "The Longitudinal Physician — Ambient Scribe Journey (v0.1 to Post-GA)"
date: 2026-02-27
status: final
designer: Sam Okafor
tags: ["ambient-scribe", "persona", "journey-map", "longitudinal", "trust-in-ai", "project-ambient-scribe"]
related_findings: ["../research/findings/ambient-scribe.md", "../research/findings/ambient-scribe-post-ga-refinements.md"]
source_type: native
persona_ref: "personas/physician-longitudinal-scribe-user.md"
scope: "v0.1 (Feb 2025) through post-GA refinements (Feb 2026)"
---

## Overview
**Evidence basis:** Mixed. Observed (stages 1–3, from P09 and the round results in `raw/2025-02-25-usability-test-ambient-scribe-v01/session-notes.md:30,36-37`, `raw/2025-09-23-usability-test-ambient-scribe-v02/session-notes.md:31-32,36-37` and `raw/2026-01-13-usability-test-ambient-scribe-ga-release-candidate/session-notes.md:30-31,36-37,48`); inferred (stage 4, which isn't recorded as P09's, from `raw/2026-02-10-ambient-scribe-medication-flag-concept/session-notes.md:36-42,71-72`, `raw/2026-02-10-ambient-scribe-medication-flag-concept/participants.md:27`, `raw/2026-02-17-session-lock-during-dictation/session-notes.md:38-41,54` and `raw/2026-02-17-session-lock-during-dictation/correction-2026-09-27.md:41-43`).

Follows the longitudinal physician persona, modeled on participant P09 in the three ambient-scribe
test rounds (v0.1, v0.2, GA candidate). The post-GA stage isn't recorded as P09's: it is
inferred from participants in the 2026-02-10 and 2026-02-17 sessions.

## Stages
1. **v0.1 (Feb 2025)** — Skeptical, reads every generated line: "I have to read every word anyway
   right now, so where's the time savings?" Across the round, medication dosages were missed or
   garbled in 3 of 5 sessions, which physicians called disqualifying for direct sign-off.
2. **v0.2 (Sep 2025)** — Errors drop, but reading behavior doesn't — still reads every line
   despite the accuracy gain: "It's better, no question. But I still read every line, same as last
   time. Getting it right once doesn't mean I trust it yet."
3. **GA Candidate (Jan 2026)** — Per-line confidence highlighting introduces the first behavior
   change: begins skimming high-confidence lines for the first time. Sound-alike medication names
   are still a known gap, recommended for post-GA monitoring.
4. **Post-GA (Feb 2026, inferred from participants)** — The dedicated medication-safety flag
   was recognized as different from generic confidence highlighting (5 of 6) — but only if unflagged lines
   don't get over-trusted as a result. Session lock during dictation remains a trust risk entirely
   unrelated to transcription quality: clinicians assumed their draft was lost when it wasn't
   ("I genuinely thought I'd lost it").
