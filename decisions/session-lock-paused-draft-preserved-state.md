---
title: A paused, draft-preserved state when the session locks during dictation
date: 2026-10-23
status: draft
decision_status: proposed
decision_status_source:
  - user-flows/ambient-scribe-session-lock-recovery.md:4
  - research/raw/2026-04-28-interview-nurse-practitioner-session-lock-shared-workstations/session-notes.md:34
date_decided: not recorded
decided_by: not recorded
superseded_by: ""
evidence:
  - source: research/raw/2026-02-17-session-lock-during-dictation/session-notes.md
    lines: "38-44,49-51,62-64,67-70,78-79"
  - source: research/raw/2026-02-17-session-lock-during-dictation/correction-2026-09-27.md
    lines: "40-43"
  - source: research/raw/2026-04-28-interview-nurse-practitioner-session-lock-shared-workstations/session-notes.md
    lines: "31-32,34,44-46"
  - source: research/findings/ambient-scribe-post-ga-refinements.md
    lines: "54-60"
  - source: research/findings/ambient-scribe.md
    lines: "113-119"
tags:
  - ambient-scribe
  - sso
  - mfa
  - clinician-workflow
  - project-ambient-scribe
related_findings:
  - ambient-scribe-post-ga-refinements.md
  - ambient-scribe.md
related_components:
  - encounter-view
  - ambient-scribe-widget
---

# A paused, draft-preserved state when the session locks during dictation

## Decision
Add an explicit "paused — draft preserved, re-authenticate to resume" state to the
`encounter-view` / `ambient-scribe-widget` lock interaction, replacing the silent freeze, and
leave the idle-timeout policy itself unchanged. These are the 2026-02-17 inquiry's
Recommendations 1 and 2
(`research/raw/2026-02-17-session-lock-during-dictation/session-notes.md:67-70`).

Decision status: proposed. The recovery flow that designs the state is in review
(`user-flows/ambient-scribe-session-lock-recovery.md:4`), and the paused state has not shipped
(`research/raw/2026-04-28-interview-nurse-practitioner-session-lock-shared-workstations/session-notes.md:34`;
`research/findings/ambient-scribe.md:118-119`). No record says it was accepted.

## Alternatives considered
- Change or extend the idle-timeout policy: recommended against. "Do not attempt to change or
  extend the idle-timeout policy itself — per IT Security, treat it as fixed and solve this
  entirely at the UI-messaging layer"
  (`research/raw/2026-02-17-session-lock-during-dictation/session-notes.md:69-70`). IT Security
  confirmed the 10-minute idle timeout is not adjustable per feature (same file, `:49-50`). The
  flow lists changing the timeout duration as out of scope
  (`user-flows/ambient-scribe-session-lock-recovery.md:45-47`).

## Rationale
**Evidence basis:** Observed. Each claim below is stated in the cited raw session and correction
lines.

The rationale on record is the 2026-02-17 inquiry's, not a decider's:
- A lock mid-recording froze the widget with no message, and all 4 clinicians assumed the draft
  was lost and started dictating again after they re-authenticated, although the draft survives
  server-side (`research/raw/2026-02-17-session-lock-during-dictation/session-notes.md:38-41`, as
  corrected by `research/raw/2026-02-17-session-lock-during-dictation/correction-2026-09-27.md:40-43`).
- There was no visual difference between recording, frozen because locked, and stopped
  (`research/raw/2026-02-17-session-lock-during-dictation/session-notes.md:42-44`).
- IT Security confirmed an explicit "paused, draft preserved" state is technically straightforward
  to add without changing the timeout policy (same file, `:49-51`), and said that what the screen
  tells the clinician during the timeout window "is entirely a product decision" (same file,
  `:62-64`).

A later interview adds a shared exam-room case. A nurse practitioner who is locked out at the exam
table doesn't know what happens to their draft if a colleague signs in, and stops the scribe
before leaving the room
(`research/raw/2026-04-28-interview-nurse-practitioner-session-lock-shared-workstations/session-notes.md:31-32`).

## Conditions to revisit
- Once the paused state ships, re-test whether it changes clinicians' behavior and not just their
  stated understanding
  (`research/raw/2026-02-17-session-lock-during-dictation/session-notes.md:78-79`).
- When it ships, re-test whether clinicians still stop the scribe before leaving a shared room
  (`research/raw/2026-04-28-interview-nurse-practitioner-session-lock-shared-workstations/session-notes.md:46`).
  The same session recommends that the message say whose draft is preserved (same file, `:45`).

## Not recorded
- Who decided: not recorded. The flow names a designer and a reviewer
  (`user-flows/ambient-scribe-session-lock-recovery.md:14-15`); neither is recorded as deciding.
- When it was decided, or whether it was accepted: not recorded.
- When it will ship: not recorded.
