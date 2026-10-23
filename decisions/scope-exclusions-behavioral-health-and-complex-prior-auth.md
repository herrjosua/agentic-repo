---
title: Behavioral health and complex prior-auth cases kept out of scope
date: 2026-10-23
status: draft
decision_status: accepted
decision_status_source:
  - research/raw/2025-12-16-stakeholder-interview-executive-steering-committee-retro/session-notes.md:30
  - research/raw/2026-06-16-interview-utilization-review-nurse-case-scope/session-notes.md:27
date_decided: not recorded
decided_by: not recorded
superseded_by: ""
evidence:
  - source: research/raw/2025-10-07-contextual-inquiry-behavioral-health-sensitive-notes/session-notes.md
    lines: "28-29,33-37,40,44"
  - source: research/raw/2025-04-08-usability-test-prior-auth-ai-v1/session-notes.md
    lines: "37-38,43"
  - source: research/raw/2025-11-04-usability-test-prior-auth-ai-v2/session-notes.md
    lines: "31,39"
  - source: research/raw/2025-12-16-stakeholder-interview-executive-steering-committee-retro/session-notes.md
    lines: "30"
  - source: research/raw/2026-06-16-interview-utilization-review-nurse-case-scope/session-notes.md
    lines: "27"
  - source: research/findings/scope-boundaries-and-workflow-fit.md
    lines: "38-43,85-88"
  - source: research/findings/prior-authorization.md
    lines: "37-41"
tags:
  - behavioral-health
  - 42-cfr-part-2
  - sensitive-notes
  - ambient-scribe
  - prior-auth
  - project-cross-cutting
related_findings:
  - scope-boundaries-and-workflow-fit.md
  - prior-authorization.md
related_components: []
---

# Behavioral health and complex prior-auth cases kept out of scope

## Decision
Two scope exclusions, which the December 2025 retro names together:
- Exclude behavioral health and substance use encounters from any ambient scribe pilot scope
  until a dedicated legal/consent review is completed
  (`research/raw/2025-10-07-contextual-inquiry-behavioral-health-sensitive-notes/session-notes.md:40`).
- Limit the prior-auth pilot to "straightforward" cases and leave complex cases out
  (`research/raw/2025-04-08-usability-test-prior-auth-ai-v1/session-notes.md:43`;
  `research/raw/2025-11-04-usability-test-prior-auth-ai-v2/session-notes.md:39`).

Decision status: accepted. At the year-end retro, the VP Clinical Informatics "specifically
praised the decision to keep behavioral health and complex prior-auth cases out of scope for 2025"
(`research/raw/2025-12-16-stakeholder-interview-executive-steering-committee-retro/session-notes.md:30`).
The prior-auth half is in effect: the pilot has run since early 2026 on straightforward cases only
(`research/raw/2026-06-16-interview-utilization-review-nurse-case-scope/session-notes.md:27`).
Whether the behavioral health half is in effect is not recorded beyond the retro's remark.

## Alternatives considered
not recorded

## Rationale
**Evidence basis:** Observed. Each claim below is stated in the cited raw session lines.

The rationale on record is the studies', not a decider's.

Behavioral health:
- Any AI tool listening to or drafting behavioral health session notes raises consent and 42 CFR
  Part 2 questions, and there is still no structured way to flag a note as Part 2-protected in the
  EHR
  (`research/raw/2025-10-07-contextual-inquiry-behavioral-health-sensitive-notes/session-notes.md:28-29`).
- A Behavioral Health Clinician (P95) objected to AI listening to a session about substance use
  "before we've even figured out how to flag that note as protected", and a charge nurse (P97) said
  the unit would need "a completely separate conversation with legal" before any pilot (same file,
  `:33-37`).

Complex prior-auth cases:
- In v1, a utilization review nurse (P19) said: "Just don't let it near the complicated ones yet"
  (`research/raw/2025-04-08-usability-test-prior-auth-ai-v1/session-notes.md:37-38`).
- In v2, the tool still struggled on the 2 complex cases
  (`research/raw/2025-11-04-usability-test-prior-auth-ai-v2/session-notes.md:31`).

The retro named only these two exclusions. It did not discuss the ED intake, SSO/MFA or ROI
redaction boundaries in the same finding (`research/findings/scope-boundaries-and-workflow-fit.md:38-43`),
which are not part of this record.

## Conditions to revisit
- Behavioral health: once a dedicated legal/consent review is completed
  (`research/raw/2025-10-07-contextual-inquiry-behavioral-health-sensitive-notes/session-notes.md:40`).
- Complex prior-auth cases: not without a separate, dedicated round of model work and testing
  (`research/raw/2025-11-04-usability-test-prior-auth-ai-v2/session-notes.md:39`).

## Not recorded
- Who decided: not recorded. The retro records a VP praising the decision, not making it.
- When it was decided: not recorded.
- A document that records the exclusions: not recorded. The finding recommends documenting its
  four exclusions in the 2026 roadmap
  (`research/findings/scope-boundaries-and-workflow-fit.md:85-88`); those include behavioral health
  but not complex prior-auth cases, which the finding says are not part of it (same file,
  `:40-41`). No such roadmap is in the corpus.
- Whether the legal/consent review has started or is on a timeline: not recorded. The 2025-10-07
  session left it as a follow-up
  (`research/raw/2025-10-07-contextual-inquiry-behavioral-health-sensitive-notes/session-notes.md:44`).
