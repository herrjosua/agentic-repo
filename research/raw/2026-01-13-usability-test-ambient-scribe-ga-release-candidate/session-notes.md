---
title: Usability Test — Ambient AI Scribe GA Release Candidate (Final Validation)
date: 2026-01-13
type: usability-test
status: raw
tags:
  - ambient-scribe
  - usability
  - documentation
  - ga-release
  - longitudinal
related_components:
  - ambient-scribe-widget
  - encounter-view
related_findings:
  - ../../findings/ambient-scribe.md
---

# Usability Test — Ambient AI Scribe GA Release Candidate (Final Validation)

## Objective
Final validation pass on the ambient scribe before GA release, testing the v0.3 confidence-indicator concept (from September's recommendation) and confirming readiness against the full history of prior findings.

## Method
- **Method:** Moderated usability test, simulated + 2 real (consented) low-acuity encounters, 45 min/session
- **Researcher:** M. Okafor
- **Full participant roster:** see `participants.md` in this folder

## Key Findings
- **[LOW]** *(confidence indicator (positive))* The new per-line confidence highlighting (low-confidence transcription shown in a subtle underline) was well received and, notably, 4 of 6 participants said it let them skim high-confidence lines for the first time across the whole testing history — the first session where reduced line-by-line reading was observed.
- **[MEDIUM]** *(sound-alike medication errors)* Still present in 1 of 6 sessions despite the pronunciation dictionary work referenced in September; team should treat this as an ongoing monitoring item post-GA rather than a pre-GA blocker, given the confidence indicator now flags it for review anyway.
- **[MEDIUM]** *(training readiness)* Participants who'd been through the champion-model style training pilot (per October's recommendation) reported higher initial comfort than those who hadn't, though this wasn't a controlled comparison.
- **[LOW]** *(phi-handling (confirmed stable))* Draft-retention/auto-expiry behavior (fixed in v0.2) remains stable and correctly documented for audit purposes; no new PHI-handling issues found.

## Representative Quotes
> "This is the first time I actually skimmed a section instead of reading every word, because it showed me exactly where to look instead."
> — Physician, Internal Medicine, P09 (returning from v0.1 and v0.2)

> "I went through the champion training last month and honestly walked in already comfortable. That part worked."
> — Nurse Practitioner, P118 (new participant)

## Recommendations
1. Approve for GA release; the critical (Feb) and high (Feb, Sept) findings across this tool's full testing history are resolved or actively monitored, and the confidence-indicator concept appears to be the trust-building lever the team was looking for since September.
2. Continue tracking sound-alike medication errors as a post-GA metric rather than delaying release further for a low-frequency, now-flagged issue.
3. Use this session as the evidence base for the CIO's requested 'documentation time saved' 2026 headline metric baseline measurement.

## Follow-ups / Open Questions
- Set up post-GA monitoring dashboard for sound-alike medication error rate.
- Feed this session's time data into the formal 2026 metrics document (per December retro action item).

## Related
- Synthesized into: [ambient-scribe.md](../../findings/ambient-scribe.md)
