---
title: Inline source citations in AI-drafted prior authorization justifications
date: 2026-10-23
status: draft
decision_status: shipped
decision_status_source:
  - research/raw/2026-06-16-interview-utilization-review-nurse-case-scope/session-notes.md:27,31
  - research/raw/2026-09-17-interview-utilization-review-nurse-citation-checking/session-notes.md:27,30
date_decided: not recorded
decided_by: not recorded
superseded_by: ""
evidence:
  - source: research/raw/2025-04-08-usability-test-prior-auth-ai-v1/session-notes.md
    lines: "28,31,34-35,42"
  - source: research/raw/2025-04-08-usability-test-prior-auth-ai-v1/correction-2026-10-13.md
    lines: "27-30"
  - source: research/raw/2025-11-04-usability-test-prior-auth-ai-v2/session-notes.md
    lines: "21,30"
  - source: research/raw/2026-06-16-interview-utilization-review-nurse-case-scope/session-notes.md
    lines: "27,31"
  - source: research/raw/2026-09-17-interview-utilization-review-nurse-citation-checking/session-notes.md
    lines: "27,30"
  - source: research/findings/prior-authorization.md
    lines: "30-36,55-58"
tags:
  - prior-auth
  - utilization-management
  - trust-in-ai
  - project-prior-auth
related_findings:
  - prior-authorization.md
related_components:
  - prior-auth-drafting-panel
---

# Inline source citations in AI-drafted prior authorization justifications

## Decision
Add inline source citations (chart entry and date) for every claim in the AI-generated prior
authorization justification. This is the v1 test's Recommendation 2
(`research/raw/2025-04-08-usability-test-prior-auth-ai-v1/session-notes.md:42`).

Decision status: shipped, in the limited utilization review pilot only. The pilot has run since
early 2026 on straightforward cases only, and its panel shows inline citations to the chart
entries behind each part of the draft
(`research/raw/2026-06-16-interview-utilization-review-nurse-case-scope/session-notes.md:27`). A
pilot nurse opens the citations for the diagnosis and the date of the most recent supporting note
on every case (same file, `:31`). Another pilot nurse has never
used a draft without them
(`research/raw/2026-09-17-interview-utilization-review-nurse-citation-checking/session-notes.md:30`).
Citations were already in the build the v2 test used
(`research/raw/2025-11-04-usability-test-prior-auth-ai-v2/session-notes.md:21`).

## Alternatives considered
not recorded

## Rationale
**Evidence basis:** Observed. Each claim below is stated in the cited raw session lines.

The rationale on record is the v1 study's, not a decider's. In v1, participants wanted to see
which chart entries the AI pulled from, inline, rather than trust a black-box summary; 3 of 4
raised "show your work" unprompted
(`research/raw/2025-04-08-usability-test-prior-auth-ai-v1/session-notes.md:31`). In 2 of 4 cases
the draft cited outdated diagnosis codes, which participants said would likely cause a payer
denial (same file, `:28`). The utilization review nurse supervisor, P17, said: "Show me where it
got that info" (same file, `:34-35`; role per
`research/raw/2025-04-08-usability-test-prior-auth-ai-v1/correction-2026-10-13.md:27-30`).

In v2, 3 of 4 participants clicked into at least one citation before accepting a draft
(`research/raw/2025-11-04-usability-test-prior-auth-ai-v2/session-notes.md:30`).

## Conditions to revisit
not recorded

## Not recorded
- Who decided: not recorded.
- When it was decided: not recorded. The v2 test on 2025-11-04 used a build that already had
  citations (`research/raw/2025-11-04-usability-test-prior-auth-ai-v2/session-notes.md:21`), so it
  was before then.
- Alternatives considered: not recorded.
- How the pilot is performing (time, accuracy, claim denials): not recorded
  (`research/findings/prior-authorization.md:62-65`).
- Whether a submitted request keeps its citations: not recorded (same file, `:64-65`).
