---
title: Ambient scribe released to GA, with sound-alike medication errors monitored after release
date: 2026-10-23
status: draft
decision_status: shipped
decision_status_source:
  - research/raw/2026-03-17-interview-clinic-nurse-reading-scribe-drafted-notes/session-notes.md:21
date_decided: not recorded
decided_by: not recorded
superseded_by: ""
evidence:
  - source: research/raw/2026-01-13-usability-test-ambient-scribe-ga-release-candidate/session-notes.md
    lines: "30-31,43-44,48"
  - source: research/raw/2026-03-17-interview-clinic-nurse-reading-scribe-drafted-notes/session-notes.md
    lines: "21"
  - source: research/raw/2025-10-21-interview-training-department-rollout-change-management/session-notes.md
    lines: "28,38"
  - source: research/findings/ambient-scribe.md
    lines: "36-39,46-47"
tags:
  - ambient-scribe
  - ga-release
  - medication-safety
  - rollout
  - project-ambient-scribe
related_findings:
  - ambient-scribe.md
  - rollout-and-change-management.md
related_components:
  - ambient-scribe-widget
---

# Ambient scribe released to GA, with sound-alike medication errors monitored after release

## Decision
Release the ambient scribe to GA, and track sound-alike medication errors as a post-GA metric
instead of delaying release. These are the GA release candidate test's Recommendations 1 and 2
(`research/raw/2026-01-13-usability-test-ambient-scribe-ga-release-candidate/session-notes.md:43-44`).
They are a research recommendation; no record states the approval itself.

Decision status: shipped. The ambient scribe "went GA in January 2026"
(`research/raw/2026-03-17-interview-clinic-nurse-reading-scribe-drafted-notes/session-notes.md:21`).

## Alternatives considered
- Delay release until sound-alike medication errors are fixed: recommended against. The session
  recommends tracking them "as a post-GA metric rather than delaying release further for a
  low-frequency, now-flagged issue"
  (`research/raw/2026-01-13-usability-test-ambient-scribe-ga-release-candidate/session-notes.md:44`),
  and treating them as "an ongoing monitoring item post-GA rather than a pre-GA blocker" (same file,
  `:31`).

## Rationale
**Evidence basis:** Observed. Each claim below is stated in the cited raw session lines.

The rationale on record is the GA-candidate session's recommendation, not an approver's:
- The critical and high findings across the tool's testing history are resolved or actively
  monitored, and the confidence indicator appears to be the trust-building lever the team was
  looking for
  (`research/raw/2026-01-13-usability-test-ambient-scribe-ga-release-candidate/session-notes.md:43`).
- 4 of 6 participants said per-line confidence highlighting let them skim high-confidence lines
  (same file, `:30`).
- Sound-alike medication errors were still present in 1 of 6 sessions (same file, `:31`).

An unresolved tension on rollout timing: in October 2025 the training department said rolling out
during flu season (Nov–Feb) has historically correlated with poor training attendance and should
be avoided if possible for the GA rollout, and recommended avoiding flu-season timing
(`research/raw/2025-10-21-interview-training-department-rollout-change-management/session-notes.md:28,38`).
GA came in January 2026
(`research/raw/2026-03-17-interview-clinic-nurse-reading-scribe-drafted-notes/session-notes.md:21`).
No record says how the timing was chosen or whether that advice was weighed.

## Conditions to revisit
not recorded. The session's follow-up was to set up a post-GA monitoring dashboard for the
sound-alike medication error rate
(`research/raw/2026-01-13-usability-test-ambient-scribe-ga-release-candidate/session-notes.md:48`).
The finding says the 2026-02-10 session still refers to that dashboard as recommended
(`research/findings/ambient-scribe.md:37-39`). Whether it was set up is not recorded.

## Not recorded
- Who approved GA: not recorded.
- When GA was approved: not recorded. GA itself was in January 2026.
- Why GA was timed for January, given the flu-season advice: not recorded.
- Whether the post-GA monitoring dashboard exists: not recorded.
