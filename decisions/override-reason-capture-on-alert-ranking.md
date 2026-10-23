---
title: Capture why a care coordinator overrides the AI alert ranking
date: 2026-10-23
status: draft
decision_status: proposed
decision_status_source:
  - wireflows/alert-triage-override-reason-capture.md:4
  - research/findings/care-coordination-triage.md:63-65
date_decided: not recorded
decided_by: not recorded
superseded_by: ""
evidence:
  - source: research/raw/2025-08-26-usability-test-alert-triage-ai-care-coordination/session-notes.md
    lines: "28-29,37-38,41,45"
  - source: research/raw/2026-07-07-interview-care-coordinator-override-reason-capture/session-notes.md
    lines: "30-32"
  - source: research/raw/2026-05-05-interview-care-coordinator-supervisor-queue-oversight/session-notes.md
    lines: "31"
  - source: research/findings/care-coordination-triage.md
    lines: "46-51,56-58,63-65,119-123"
tags:
  - care-coordination
  - alert-triage
  - alert-fatigue
  - project-care-coordination
related_findings:
  - care-coordination-triage.md
related_components:
  - alert-triage-queue
---

# Capture why a care coordinator overrides the AI alert ranking

## Decision
Add a lightweight "why did you reprioritize" capture on override, both to improve the model and to
give coordinators a sense of agency
(`research/raw/2025-08-26-usability-test-alert-triage-ai-care-coordination/session-notes.md:41`).
The finding recommends adding it before further ranking-model tuning
(`research/findings/care-coordination-triage.md:56-58`).

Decision status: proposed. The reason-capture wireflow is in review
(`wireflows/alert-triage-override-reason-capture.md:4`). Neither the AI-ranked queue nor the
chart-review summary panel has been built, and the wireflow is still in review
(`research/findings/care-coordination-triage.md:63-65`).

## Alternatives considered
not recorded. A returning coordinator said they would give a reason in one tap but would not type
free text on every override
(`research/raw/2026-07-07-interview-care-coordinator-override-reason-capture/session-notes.md:31`).
That is a participant's preference about the design, not an alternative the team is recorded as
considering.

## Rationale
**Evidence basis:** Observed. Each claim below is stated in the cited raw session lines.

The rationale on record is the 2025-08-26 study's, not a decider's:
- 4 of 5 participants disagreed with the AI's top-3 ranking on at least one test queue
  (`research/raw/2025-08-26-usability-test-alert-triage-ai-care-coordination/session-notes.md:28`).
- When they disagreed, there was no way to note why they reprioritized, so that correction signal
  isn't captured for model improvement (same file, `:29`).
- P81: "I wanted to tell it 'no, this one's more urgent because I know this patient's history,'
  but there was nowhere to put that" (same file, `:37-38`).

Later interviews add detail. A returning coordinator's most common reason for moving an alert
isn't in the wireflow's reason list, and they would stop giving reasons if they never saw an effect
(`research/raw/2026-07-07-interview-care-coordinator-override-reason-capture/session-notes.md:30,32`).
A supervisor would want a record of the order each coordinator was shown and what they did with
each alert
(`research/raw/2026-05-05-interview-care-coordinator-supervisor-queue-oversight/session-notes.md:31`).

## Conditions to revisit
not recorded

## Not recorded
- Who decided: not recorded.
- When it was decided, or whether it was accepted: not recorded.
- Whether supervisors see the reasons coordinators give: not recorded. The wireflow logs them for
  model-tuning review and doesn't surface them to other coordinators, but doesn't say whether
  supervisors see them
  (`research/raw/2026-05-05-interview-care-coordinator-supervisor-queue-oversight/session-notes.md:31`).
- Whether the override-capture idea reached the data-science team, as the 2025-08-26 session
  suggested
  (`research/raw/2025-08-26-usability-test-alert-triage-ai-care-coordination/session-notes.md:45`):
  not recorded (`research/findings/care-coordination-triage.md:122-123`).
