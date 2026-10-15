---
title: "Confidence-Highlighted Draft Review — Hi-Fi Mockup (GA Candidate)"
date: 2026-01-05
status: final
designer: Sam Okafor
tags: ["ambient-scribe", "trust-in-ai", "documentation", "project-ambient-scribe"]
related_findings: ["../research/findings/ambient-scribe.md"]
source_type: native
fidelity: "hi-fi"
figma_url: ""
---

## Overview
**Evidence basis:** Mixed. Observed (the GA-candidate round's result, from `raw/2026-01-13-usability-test-ambient-scribe-ga-release-candidate/session-notes.md:30,43`, and the underline's limits since GA, from `raw/2026-03-19-interview-primary-care-physician-incidental-content-at-sign-off/session-notes.md:32`, `raw/2026-06-30-interview-rheumatologist-medication-lines-in-scribe-drafts/session-notes.md:31`, `raw/2026-07-28-interview-orthopedics-physician-assistant-exam-findings-in-scribe-drafts/session-notes.md:29` and `raw/2026-09-22-interview-returning-internal-medicine-physician-edits-and-trust-over-time/session-notes.md:31`); illustrative (the treatment in Notes beyond the underline itself is the designer's spec, not recorded in the test).

Hi-fi visual design for per-line confidence highlighting in the draft-review surface, built for
the Jan 2026 GA-candidate round — the feature that produced the program's clearest
trust-calibration result to date. In that round, 4 of 6 participants said it let them skim
high-confidence lines for the first time across the whole testing history, the first session
where reduced line-by-line reading was observed (`:30`); the session's notes say the concept
"appears to be the trust-building lever the team was looking for since September" (`:43`).

As of 2026-09-22: "to date" means as of the 2026-01-13 round. Four later interviews, each one
clinician's account of their own practice, say the underline marks only where the scribe was
unsure what it heard, so problems in lines it heard clearly aren't underlined: incidental
content (2026-03-19 `:32`), medication dose schedules (2026-06-30 `:31`), which side an exam
finding is on (2026-07-28 `:29`) and the order of events in the history (2026-09-22 `:31`).

## Notes
Two-state treatment. The 2026-01-13 session notes record only that low-confidence transcription
was shown in a subtle underline (`:30`). The rest is the designer's spec and wasn't recorded in
the test: high-confidence lines render as default text with no marking (deliberately inviting
skimming), low-confidence lines also get an on-hover explanation, and there is no separate
medium-confidence tier.
Deliberately avoids color-only signaling, per the cross-cutting accessibility finding — flagged
lines are distinguishable by the underline itself, not color alone.
