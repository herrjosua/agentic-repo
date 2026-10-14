---
title: Care Coordination & Alert Triage
date: 2026-09-29
type: synthesis
status: synthesized
researcher: Priya Patel
tags:
  - alert-fatigue
  - alert-triage
  - ambient-scribe
  - baseline
  - care-coordination
  - chart-review
  - medication-safety
  - scheduling
  - training
  - usability
  - workflow
  - project-care-coordination
related_components:
  - alert-triage-queue
  - chart-review-summary-panel
related_findings:
  - clinician-experience-documentation-burden.md
---

# Care Coordination & Alert Triage

## Overview
Two sessions bookend this topic: a baseline contextual inquiry of manual chart review (Jan 2025,
before any AI concept existed) and a usability test of an AI-ranked alert triage queue (Aug 2025).

- **The baseline recommended a narrow scope.** Coordinators already distrusted the EHR's
  auto-generated after-visit summaries, having caught them omitting recently changed medications
  twice in the past quarter. One coordinator (P05) said: "If it could just tell me what changed
  since I last touched this chart, that alone would save me time. I don't need it to think for
  me." The session recommended scoping an early AI concept around 'what changed since last review'
  rather than full summarization.
- **The AI-ranked queue was faster, but most participants disagreed with its ranking.** In this
  simulated test, triage of a 20-item queue was faster with AI ranking present (avg 6.5 min) than
  with a chronological queue (avg 9 min), but 4 of 5 participants disagreed with the AI's top-3
  ranking on at least one of three test queues, generally because the model weighted recency more
  heavily than coordinators' own sense of clinical risk — echoing the alert-fatigue concern raised separately in the May
  clinician dashboard testing (see
  [clinician-experience-documentation-burden.md](clinician-experience-documentation-burden.md)).
  There was also no way to capture *why* a coordinator overrode a ranking, so that correction
  signal isn't captured anywhere for future model improvement. Separately, the supervisor (P79)
  worried that speed gains could mask a coordinator rubber-stamping the AI order without real
  judgment: "fast and wrong is worse than slow and right in this job." The study's own
  recommendation adds that override-reason capture would give coordinators a sense of agency the
  current design lacks.
- **This is also where the mobile accessibility touch-target finding lands** — the alert-triage icon
  set audited in November is the same feature tested here in August (see
  [accessibility-cross-cutting.md](accessibility-cross-cutting.md)).

Recommendation: add lightweight override-reason capture before further ranking-model tuning, and
share it with whoever owns the care-gap flagging model tuning, since it's likely the same underlying
problem.

## Since GA: 2026 Coordinator Interviews
Ten 1:1 interviews between March and September 2026 revisited both threads after the ambient
scribe went GA: eight with coordinators new to this research (P130–P137) and two with returning
participants, P05 from the January 2025 baseline and P81 from the August 2025 test. Neither the
AI-ranked queue nor the chart-review summary panel has been built, and the override-reason
wireflow is still in review, so reactions come from descriptions of the ranked queue and, in one
session, the wireflow screens. Coordinators read clinicians' signed notes, including scribe-drafted
ones, but don't use the scribe themselves (2026-03-03). Every figure below is an informal
participant estimate or recollection, not a count or a rate.

- **Float pool versus continuity.** Two float coordinators lack the patient history that team
  coordinators use to reorder alerts. P05 works the current chronological queue strictly in order
  when floating and leaves reprioritising to the team's own coordinators (2026-04-07, MEDIUM), and
  P136 would accept a ranked queue as a starting point while still checking it (2026-09-01,
  MEDIUM). On the other side, two team coordinators lean on knowing their patients: P81's August
  2025 comment about a patient's history, and P134 on a high-risk panel (2026-08-04, MEDIUM). That
  is two voices on each side: a contrast worth testing, not a pattern. P136 also switches between
  several team queues in a shift with no combined view (2026-09-01, HIGH).
- **The right ranking signal depends on the alert type.** For discharge alerts, a transitions of
  care coordinator said time since discharge *is* the clinical risk, because the first days at home
  are when a missed change matters most (2026-04-16, MEDIUM). This refines rather than contradicts
  the August 2025 finding that the model weighted recency more heavily than coordinators' sense of
  clinical risk: for this alert type, recency and risk point the same way.
- **Repeat alerts and volume.** For a complex care coordinator, the main noise is repeat alerts for
  the same patient, more than the order alerts arrive in, and they would group alerts by patient
  before any ranking is applied (2026-08-04, HIGH). A supervisor put heavy days at "maybe 30 to 60
  alerts" per coordinator, many of them administrative rather than clinical (informal estimate;
  2026-05-05, MEDIUM).
- **Override reasons.** Looking at the in-review wireflow, P81 said their most common reason for
  moving an alert, something the patient or a family member said on the phone that isn't in the
  chart yet, is missing from the reason list, so it would land in "other" (2026-07-07, HIGH). They
  would give a reason in one tap but not type free text on every override, and would stop giving
  reasons if they never saw any effect from them (2026-07-07, MEDIUM). A supervisor would use
  reasons for coaching as well as model tuning, and wants a record of the order each coordinator
  was shown and what they did with it (2026-05-05, HIGH). That raises who sees the reasons, which
  the wireflow doesn't settle: it logs them for model-tuning review, "not surfaced to other
  coordinators", and says nothing about supervisors.
- **What "what changed" is anchored on.** Two coordinators moved the reference point away from
  "since I last touched this chart". P130 anchored it on their own last outreach call rather than
  the patient's last visit (2026-03-03, MEDIUM), and P05, now floating, on the team's last contact
  with the patient, whoever made it, because on a covering shift they have often never touched the
  chart (2026-04-07, MEDIUM). A referral follow-up coordinator said it has to cover appointments and
  results, not just medications (2026-09-29, MEDIUM).
- **Workarounds, learning the role and the legacy scheduling tool.** Conventions such as the shared
  spreadsheet's colours and which alerts can wait are still passed on by word of mouth. A newer
  coordinator learned them by shadowing, with nothing written down, and said newer coordinators
  might gain most from a ranked queue but be least able to tell when it is wrong (2026-08-20,
  HIGH); a remote coordinator learned the colours by asking colleagues and keeps a private key
  (2026-06-09, MEDIUM). Chart review took the newer coordinator "closer to 20 minutes at first"
  (informal recollection; 2026-08-20, MEDIUM). Coordinators still cross-check the same 3 to 4
  systems before a call, and from home the legacy scheduling tool is the slowest of them
  (2026-06-09, HIGH). Confirming there whether a referred appointment happened is the biggest time
  sink for a referral follow-up coordinator, and overdue-referral alerts are often already resolved
  (2026-09-29, HIGH). Scribe-drafted notes are longer, so coordinators skip to the plan and
  medication list, at "a couple of extra minutes" on complex patients (informal; 2026-03-03, HIGH).
- **After-visit summaries.** A transitions of care coordinator recalled the after-visit summary
  leaving out a medication change "a few times this year", with no log and no count of correct
  summaries (2026-04-16, HIGH). That is an anecdote, not a rate.

Still open after the 2026 interviews: how often the after-visit summary misses changes; whether the
2025 queue showed coordinators what its ranking was based on; how accurate the ranking is;
real-world triage speed; how often coordinators follow a ranked order without judgement (no
measurement of rubber-stamping); and whether the override-capture idea reached the data-science
team.

## Evidence Trail
- **2025-01-29** — [Contextual Inquiry — Manual Chart Review Baseline (Care Coordinators)](../raw/2025-01-29-contextual-inquiry-chart-review-baseline/session-notes.md) *(`contextual-inquiry`)*
- **2025-08-26** — [Usability Test — AI Alert Triage for Care Coordination](../raw/2025-08-26-usability-test-alert-triage-ai-care-coordination/session-notes.md) *(`usability-test`)*
- **2025-11-18** — [Accessibility Audit — Mobile Clinician App (Low Vision & Motor Impairment Focus)](../raw/2025-11-18-accessibility-audit-mobile-clinician-app/session-notes.md) *(`accessibility-audit`)*
- **2026-03-03** — [Interview — Care Coordinator on Chart Review of Scribe-Drafted Notes](../raw/2026-03-03-interview-care-coordinator-chart-review-scribe-notes/session-notes.md) *(`interview`)*
- **2026-04-07** — [Interview — Float-Pool Care Coordinator on System Familiarity](../raw/2026-04-07-interview-care-coordinator-float-pool-system-familiarity/session-notes.md) *(`interview`)*
- **2026-04-16** — [Interview — Transitions-of-Care Coordinator on Medication Changes after Discharge](../raw/2026-04-16-interview-care-coordinator-transitions-medication-changes/session-notes.md) *(`interview`)*
- **2026-05-05** — [Interview — Care Coordinator Supervisor on Queue Oversight](../raw/2026-05-05-interview-care-coordinator-supervisor-queue-oversight/session-notes.md) *(`interview`)*
- **2026-06-09** — [Interview — Remote Care Coordinator on Telephonic Outreach](../raw/2026-06-09-interview-care-coordinator-remote-outreach/session-notes.md) *(`interview`)*
- **2026-07-07** — [Interview — Returning Care Coordinator on Override-Reason Capture](../raw/2026-07-07-interview-care-coordinator-override-reason-capture/session-notes.md) *(`interview`)*
- **2026-08-04** — [Interview — Complex Care Coordinator on Alert Volume](../raw/2026-08-04-interview-care-coordinator-complex-care-alert-volume/session-notes.md) *(`interview`)*
- **2026-08-20** — [Interview — New Care Coordinator on Learning the Queue](../raw/2026-08-20-interview-care-coordinator-new-hire-shadowing/session-notes.md) *(`interview`)*
- **2026-09-01** — [Interview — Float Pool Care Coordinator on Covering Several Teams](../raw/2026-09-01-interview-care-coordinator-float-pool-coverage/session-notes.md) *(`interview`)*
- **2026-09-29** — [Interview — Specialty Clinic Care Coordinator on Referral Follow-up](../raw/2026-09-29-interview-care-coordinator-referral-follow-up/session-notes.md) *(`interview`)*

## Related Findings
- [Clinician Experience & Documentation Burden](clinician-experience-documentation-burden.md)
