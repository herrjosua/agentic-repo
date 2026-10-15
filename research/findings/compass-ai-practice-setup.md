---
title: Compass AI Practice Setup
date: 2026-02-24
type: synthesis
status: synthesized
researcher: Priya Patel
tags:
  - onboarding
  - usability
  - funnel
  - scheduling
  - phi
  - privacy
  - rollout
  - training
  - project-onboarding
related_components: []
related_findings:
  - rollout-and-change-management.md
  - governance-and-phi.md
related_analytics:
  - compass-ai-practice-setup-funnel
---

# Compass AI Practice Setup

## Overview
Three early-2026 sessions look at how an administrator sets Compass AI up for a practice: a
dashboard review of setups (Jan 2026), a moderated usability test of the setup flow with 4
Practice Administrators and 2 IT Administrators (Feb 2026), and an interview with an IT
Administrator who approves access requests across practices (Feb 2026). This is about admin setup
of Compass AI, not staff training; elsewhere in the corpus "onboarding" can mean training copy for
clinicians (`raw/2026-02-10-ambient-scribe-medication-flag-concept/session-notes.md:62`).

The setup flow has five steps, all required in the build studied: 1 Sign in with Meridian SSO (the
existing badge-tap or manual MFA sign-in, `design-tokens/components/sso-mfa-login.md:13-14`), 2
Practice details, 3 Connect calendar (read access to the practice's appointment schedule), 4 Invite
your team (gives clinicians and staff access and sends them an email), 5 Review & finish
(`raw/2026-02-03-usability-test-compass-ai-practice-setup-flow/session-notes.md:33-37`). At session
setup, the designer stated that the calendar step is required because the scribe attaches
recordings to scheduled encounters (same file, `:38`). That is the designer's stated rationale; no
session tested it.

- **Setups stop most at Connect calendar, then at Invite your team.** Of 24 setups started
  2025-12-01 to 2026-01-16, 12 had finished and 12 were still open on 2026-01-20: 7 at Connect
  calendar (open 4 to 41 days, median 16), 3 at Invite your team (6, 11 and 19 days), 1 at Practice
  details and 1 at Review & finish
  (`raw/2026-01-20-dashboard-review-compass-ai-practice-setup-completion/session-notes.md:41-48`,
  `:51-59`; HIGH and MEDIUM). The dashboard can't show why (same file, `:72-74`). See
  [compass-ai-practice-setup-funnel](../../analytics/summaries/compass-ai-practice-setup-funnel.md).
- **Practice Administrators don't think the calendar is theirs to approve.** 3 of 4 Practice
  Administrators stopped at Connect calendar because it gives Compass AI access to patient
  appointments and they did not think they could approve that; the fourth asked the moderator
  whether it was theirs to approve (2026-02-03, HIGH; `session-notes.md:51`). "That's patient names
  and visit reasons. That's not my call — that's IT's." (P154, `:58-59`). All 4 went on only because
  the moderator let them continue on a sandbox calendar, a test accommodation, so their completing
  the step is not a result (`:43-45`).
- **IT Administrators connect it, but want to know what is read.** Both IT Administrators in the
  test connected the calendar only after asking which fields are read; the screen doesn't list them
  (2026-02-03, MEDIUM; `:52`).
- **Schedule access needs a privacy review that only IT can request.** The IT Administrator
  interviewed said any new system that reads the appointment schedule needs a privacy review request
  first, and Practice Administrators can't start one (2026-02-24, HIGH;
  `raw/2026-02-24-interview-it-administrator-schedule-access-and-staff-invites/session-notes.md:29`).
  They called scheduling the lowest-risk data on the CMIO's PHI ordering but still PHI, consistent
  with that ordering, not a contradiction of it (same file, `:30`; the ordering is in
  `raw/2025-08-12-interview-cmio-ai-generated-content-governance/session-notes.md:29` and
  [governance-and-phi.md](governance-and-phi.md)). This is one IT Administrator's account of the
  process, not a review of its records.
- **Practice Administrators don't want staff emailed before training is booked.** 3 of 4 Practice
  Administrators hesitated at Invite your team: unsure whether the email goes out at that step or at
  Review & finish, and unwilling to email staff before champion training is booked (2026-02-03,
  HIGH; `raw/2026-02-03-usability-test-compass-ai-practice-setup-flow/session-notes.md:53`, quote
  P157 `:64-65`). The unit-champion training model is described in
  [rollout-and-change-management.md](rollout-and-change-management.md) (`:36-38`). One IT Administrator asked
  whether invites create accounts or rely on existing SSO groups, which no record answers
  (2026-02-03, MEDIUM; `:54`).
- No issues at Sign in or Practice details: 6 of 6 participants completed both (2026-02-03, LOW;
  `:55`).

Recommendation (from the 2026-02-03 and 2026-02-24 sessions): list the fields read on Connect
calendar; add a "Send to IT for approval" path there for an administrator who can't approve the
access; say on Invite your team when the email is sent; and let administrators schedule the invite
email for a date, so it can go out once training is booked
(`raw/2026-02-03-usability-test-compass-ai-practice-setup-flow/session-notes.md:74-79`;
`raw/2026-02-24-interview-it-administrator-schedule-access-and-staff-invites/session-notes.md:40-41`).

## What this does and doesn't show
- It shows where setups stopped in one seven-week window and, for 6 test participants and 1
  interviewee, the reasons they gave at the calendar and invite steps. It doesn't show that those are
  the reasons the 24 dashboard setups stopped: the dashboard doesn't record who ran each setup or
  why it stopped. The analytics summary reports only where setups stopped and for how long, and
  isn't independent evidence for these reasons.
- It doesn't test whether the calendar step needs to be required. The only rationale on record is
  the designer's statement at session setup (`2026-02-03 session-notes.md:38`).
- The counts are small: 4 Practice Administrators, 2 IT Administrators, 1 interviewee, 24 setups.

## Gaps
- How Compass AI was rolled out practice by practice, and whether the setup flow is used beyond the
  setups and sessions recorded here, isn't recorded in the corpus.
- How Compass AI access is provisioned (through SSO groups, through these invites, or both) isn't
  recorded; neither the moderator nor the IT Administrator interviewed knew
  (`raw/2026-02-03-usability-test-compass-ai-practice-setup-flow/session-notes.md:46-48`;
  `raw/2026-02-24-interview-it-administrator-schedule-access-and-staff-invites/session-notes.md:45`).
- When this build sends the invite email isn't recorded (2026-02-03 `session-notes.md:46-47`).
- Whether the legacy ExtJS admin console that the March 2025 audit assessed
  (`raw/2025-03-10-accessibility-audit-legacy-extjs-admin-console/session-notes.md:21`) was
  replaced, and how it relates to this setup flow, isn't recorded.
- Which scheduling system holds the appointment schedule isn't recorded (2026-02-24
  `session-notes.md:26`).
- Whether GA timing followed the training department's advice to avoid flu season (Nov-Feb;
  [rollout-and-change-management.md](rollout-and-change-management.md), `:36-38`) isn't recorded.
- Whether a privacy review request for Compass AI's schedule access has been filed isn't known
  (2026-02-24 `session-notes.md:29`, `:44`).

## Evidence Trail
- **2026-01-20** — [Dashboard review — Compass AI practice setup completion](../raw/2026-01-20-dashboard-review-compass-ai-practice-setup-completion/session-notes.md) *(`analytics`)*
- **2026-02-03** — [Usability Test — Compass AI Practice Setup Flow](../raw/2026-02-03-usability-test-compass-ai-practice-setup-flow/session-notes.md) *(`usability-test`)*
- **2026-02-24** — [Interview — IT Administrator on Schedule Access and Staff Invites](../raw/2026-02-24-interview-it-administrator-schedule-access-and-staff-invites/session-notes.md) *(`interview`)*

## Related Findings
- [Rollout & Change Management](rollout-and-change-management.md)
- [AI Governance, PHI & Compliance](governance-and-phi.md)

## Related Analytics
- [Compass AI practice setup — where setups stop](../../analytics/summaries/compass-ai-practice-setup-funnel.md)
