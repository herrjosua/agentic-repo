---
title: Ambient Scribe — Session Lock Recovery
date: 2026-02-25
status: in-review
tags:
  - ambient-scribe
  - sso
  - mfa
  - user-flow
related_findings:
  - ../research/findings/ambient-scribe-post-ga-refinements.md
source_type: native
designer: Sam Okafor
reviewed_by: Jordan Lee
flow_name: Session lock during active ambient-scribe dictation, with explicit paused/resume state
screens_count: 3
---

# Ambient Scribe — Session Lock Recovery

## Description
Response to the 2026-02-17 contextual inquiry finding that a session lock mid-recording currently
reads as silent draft loss. Covers the `encounter-view`/`ambient-scribe-widget` interaction from
the moment the idle timeout fires through resumed dictation, replacing today's silent freeze with
an explicit state. Per IT Security (interviewed in that session), the 10-minute idle-timeout
policy itself is fixed and out of scope — this flow only changes what the UI communicates during
that window, not when it triggers.

## Details
1. **Recording (normal state)** — `ambient-scribe-widget` in `recording` state, `encounter-view`
   in `default` state, unchanged from today.
2. **Idle timeout fires → Paused (new state)** — `encounter-view` moves to `locked`;
   `ambient-scribe-widget` moves to a new `paused-preserved` state showing "Session paused — your
   draft is saved. Re-authenticate to resume." Recording audio stops; draft is not discarded
   client- or server-side. This replaces today's silent freeze, which 4 of 5 observed clinicians
   misread as data loss.
3. **Re-authenticate → Resume** — on successful SSO/MFA re-auth, `encounter-view` returns to
   `default`, `ambient-scribe-widget` returns to `recording` (if the clinician chooses to
   continue) or `reviewing-draft` (if they'd rather review what's captured so far first). The
   preserved draft is visible immediately on return — no re-dictation needed.
- **Explicitly out of scope:** changing the idle-timeout duration, or any cross-feature timeout
  behavior beyond ambient scribe (flagged as a follow-up question in the source session, not
  resolved here).
- **Framing note carried from research:** copy in step 2 should read as an expected safety
  behavior, not an unrelated login interruption — the source session found clinicians already
  numb to frequent unrelated re-auth prompts, which was part of why the current silent freeze
  reads as broken rather than as a deliberate pause.
