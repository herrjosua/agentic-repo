---
title: Scope Boundaries & Workflow Fit
date: 2026-09-08
type: synthesis
status: synthesized
researcher: Priya Patel
tags:
  - 42-cfr-part-2
  - authentication
  - baseline
  - behavioral-health
  - clinician-workflow
  - ed
  - high-acuity
  - intake
  - mfa
  - nursing
  - phi
  - security
  - sensitive-notes
  - sso
  - workflow
  - project-cross-cutting
related_components:
  - ambient-scribe-widget
  - ed-intake-form
  - sso-mfa-login
related_findings:
  - governance-and-phi.md
---

# Scope Boundaries & Workflow Fit

## Overview
Three 2025 sessions, plus two 2026 HIM interviews that refine a release-of-information (ROI)
boundary first set in the July 2025 HIM research and two 2026 ED nurse interviews that revisit the
ED intake boundary, are grouped here because their common output was
a "don't build this yet, or don't build it here" conclusion. The December executive retro praised this kind of
scope discipline in general ("The stuff you told us not to build yet mattered as much as the stuff
you told us to build"), but the only exclusions it named were behavioral health (covered below)
and complex prior-auth cases (not part of this finding). It did not discuss the ED intake or
SSO/MFA boundaries, or the ROI redaction boundary below, which dates from the July 2025 HIM
research; only the 2026 evidence added to that boundary postdates the retro.

- **ED intake (contextual inquiry, Apr 2025; revisited Apr and May 2026):** peak-hour interruption frequency (every 2-4 minutes)
  makes any AI tool requiring sustained review attention a poor fit for ED intake nurses
  specifically during peak windows. The one positive signal — insurance-card-photo pre-fill for
  registration clerks — was carved out as a smaller, separate, lower-risk candidate instead.
  In April 2026 the intake nurse shadowed in 2025 described the interruptions as unchanged (their
  account, not a re-measurement) and would accept help that needs no review, but nothing they
  would have to read and approve between interruptions (2026-04-14, HIGH). They start the paper
  triage sheet at the top of every peak shift, so anything scoped here has to work alongside paper
  and survive re-entry from it; the 2025 notes don't say when staff started it, so this isn't
  evidence of a change (2026-04-14, MEDIUM). An ED charge nurse agreed the boundary holds at peak,
  for charge work too, but not across the whole shift: after peak they could see an assist pulling
  together the end-of-shift handoff for them to check ("twenty minutes on a bad night" by hand,
  informal; an expectation, nothing shown; 2026-05-19, MEDIUM). The boundary is peak-specific, not
  ED-wide. Whether the insurance-card pre-fill has been piloted is not recorded.
- **SSO/MFA modernization (interview, May 2025):** independent of any AI feature, a planned
  15-minute forced re-authentication conflicts with clinical ops' expectation of a 4-hour session —
  and nobody had yet defined what happens to an in-progress ambient scribe recording session if a
  forced re-auth interrupts it mid-visit. This was flagged as an unhandled edge case for the
  ambient scribe team (see [ambient-scribe.md](ambient-scribe.md)) rather than something to solve
  in this session. The 15-minute figure was a *planned* policy that was still disputed as of May
  2025. By Feb 2026, IT Security confirmed the 10-minute idle timeout is not adjustable per feature
  (2026-02-17-session-lock-during-dictation/session-notes.md:49-50; see
  [ambient-scribe-post-ga-refinements.md](ambient-scribe-post-ga-refinements.md)). The raw notes
  don't say whether that settles this dispute or is a separate idle-lock setting.
- **Behavioral health (contextual inquiry, Oct 2025):** reiterated, independently, the same "no
  structured way to flag a 42 CFR Part 2-protected note" platform gap first identified in the July
  HIM research (see [him-coding-and-billing.md](him-coding-and-billing.md)), which HIM found
  unchanged in March 2026 (2026-03-31, HIGH) — and added a harder
  constraint on top: any AI tool listening to or drafting behavioral health notes needs a dedicated
  legal/consent review that hasn't started yet. This population was formally excluded from the
  near-term ambient scribe rollout as a result.
- **ROI redaction (HIM research, Jul 2025; refined Mar and Sep 2026):** the suggest-only boundary
  set in July 2025 (see [him-coding-and-billing.md](him-coding-and-billing.md)) held in 2026: a
  person redacts and a person releases every record. Within it, an ROI specialist would accept
  batch pre-highlighting only for low-risk requests where patients ask for their own records;
  attorney, insurer and possible Part 2 requests are excluded from batch handling and stay one at a
  time (2026-09-08, HIGH). An HIM supervisor said the backlog sits in the second-level Part 2
  review queue rather than first-pass redaction, so any redaction assistance should be designed
  around that queue (2026-03-31, MEDIUM).

Recommendation: keep these four exclusions as explicit, documented scope boundaries in the 2026
roadmap rather than informal assumptions that could quietly erode. This is this finding's
recommendation, not a retro action item — the retro's own recommendations were a formal metrics
document and a cross-cutting findings section.

## Evidence Trail
- **2025-04-22** — [Contextual Inquiry — Emergency Department Intake Shadowing](../raw/2025-04-22-contextual-inquiry-ed-intake-shadowing/session-notes.md) *(`contextual-inquiry`)*
- **2025-05-20** — [Interview — IT Security on SSO/MFA Modernization Impact](../raw/2025-05-20-interview-it-security-sso-mfa-modernization/session-notes.md) *(`interview`)*
- **2025-10-07** — [Contextual Inquiry — Behavioral Health Unit, Sensitive Note Handling](../raw/2025-10-07-contextual-inquiry-behavioral-health-sensitive-notes/session-notes.md) *(`contextual-inquiry`)*
- **2025-12-16** — [Executive Steering Committee — Year-End Retro & 2026 Roadmap Input](../raw/2025-12-16-stakeholder-interview-executive-steering-committee-retro/session-notes.md) *(`interview`)* — cited for the scope-discipline praise only
- **2026-02-17** — [Contextual Inquiry — Session Lock During Active Ambient Scribe Dictation](../raw/2026-02-17-session-lock-during-dictation/session-notes.md) *(`contextual-inquiry`)* — cited for the 10-minute idle timeout not being adjustable per feature (session-notes.md:49-50) only
- **2026-03-31** — [Interview — HIM Supervisor on ROI Volume and Part 2 Handling](../raw/2026-03-31-interview-him-supervisor-roi-volume-and-part-2/session-notes.md) *(`interview`)*
- **2026-04-14** — [Interview — Returning ED Intake Nurse on Interruptions and Downtime](../raw/2026-04-14-interview-ed-intake-nurse-interruptions-and-downtime/session-notes.md) *(`interview`)*
- **2026-05-19** — [Interview — ED Charge Nurse on Shift Oversight](../raw/2026-05-19-interview-ed-charge-nurse-shift-oversight/session-notes.md) *(`interview`)*
- **2026-09-08** — [Interview — HIM Specialist on ROI Request Turnaround](../raw/2026-09-08-interview-him-specialist-roi-request-turnaround/session-notes.md) *(`interview`)*

## Related Findings
- [AI Governance, PHI & Compliance](governance-and-phi.md)
