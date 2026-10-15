---
title: Rollout & Change Management
date: 2026-08-18
type: synthesis
status: synthesized
researcher: Priya Patel
tags:
  - change-management
  - nursing
  - organizational-readiness
  - pulse
  - rollout
  - survey
  - training
  - year-end
  - project-cross-cutting
related_components:
  - patient-chatbot-widget
related_findings:
  - governance-and-phi.md
  - ambient-scribe.md
---

# Rollout & Change Management

## Overview
Two sessions, five weeks apart at year-end, look at how Compass AI features actually get adopted
once built: a training/change-management interview (Oct 2025) and an all-staff AI readiness pulse
survey (Dec 2025). A 2026 interview with a nurse manager (Aug 2026) adds the view of the person who
has to release staff for that training.

- **The training interview drew directly on a documented past failure.** The 2022 CDS alert
  rollout — referenced independently by executives back in January (see
  [governance-and-phi.md](governance-and-phi.md)) — is treated as the cautionary tale: a single
  20-minute training video with no hands-on practice, and adoption suffered. The Director of
  Training's recommendation is a "unit champion" model (1-2 respected staff per unit, trained early
  and deeply) plus mandatory hands-on practice time, and to avoid rolling out during flu season
  (Nov-Feb) given historical attendance patterns.
- **Practice time depends on the unit's staffing on the day.** A medical-surgical nurse manager
  agreed with the champion model in principle, but releasing a nurse means backfilling their
  assignment with a float nurse or overtime, and on a high-census or call-out day training is the
  first thing they cancel (2026-08-18, MEDIUM). What they said they would need: training dates
  known before they build the schedule, about six weeks out (their description of their own
  practice); backfill paid from a training budget rather than the unit's; night and weekend
  sessions; and champion time for supporting peers put on the schedule, not added to a full
  assignment (2026-08-18, MEDIUM). They also named flu season as their hardest months to release
  anyone. Their account draws on releasing nurses for other training, not on an AI rollout, and how
  often training is cancelled for staffing is not measured.
- **One returning nurse practitioner on what the scribe's champion training pilot did and didn't
  cover.** P118 (Nurse Practitioner), returning from 2026-01-13-usability-test-ambient-scribe-ga-release-candidate,
  said the pilot training prepared them for the controls, for correcting a single line in place and
  for what the underline means, but not for visits unlike the practice ones: several people
  talking, a visit interrupted partway through, or a patient raising a second problem at the door,
  which they learned to handle by using the scribe (2026-05-26, MEDIUM). Colleagues who started
  using the scribe after GA ask them informally how to correct a line or what the underline means
  (2026-05-26, LOW). This is one account, not a comparison with no training, and how clinicians who
  started after GA were trained is not recorded in the corpus.
- **The December pulse survey found an awareness gap that changes rollout sequencing for
  non-clinical features specifically**: only 34% of non-clinical/admin staff were aware Compass AI
  work was even underway, vs. 71% of clinical staff. This matters directly for the patient
  scheduling chatbot (see [patient-scheduling-chatbot.md](patient-scheduling-chatbot.md)), which is
  the first admin-facing, non-clinical feature nearing rollout — communications need to reach that
  audience before launch, not after.
- The survey's directional sentiment comparison to the February 2025 nursing attitudes survey is
  noted but flagged as not a clean apples-to-apples comparison (different question wording). The
  survey recommends re-running the exact February instrument if a clean trend is needed.

Recommendation: use the unit-champion training model for the ambient scribe GA rollout (avoiding
flu-season timing), and run a dedicated non-clinical-staff communications push before the
scheduling chatbot goes live. One nurse manager's account suggests that, for any later rollout that
reaches nurses, champion practice time and backfill should be agreed with unit managers before
their schedule is built (2026-08-18).

## Evidence Trail
- **2025-10-21** — [Interview — Training & Education Dept on Rollout/Change Management Planning](../raw/2025-10-21-interview-training-department-rollout-change-management/session-notes.md) *(`interview`)*
- **2025-12-02** — [Survey — All-Staff AI Readiness Pulse Survey](../raw/2025-12-02-survey-allstaff-ai-readiness-pulse/session-notes.md) *(`survey`)*
- **2026-05-26** — [Interview — Returning Nurse Practitioner on Champion Training and Review Habits](../raw/2026-05-26-interview-returning-nurse-practitioner-training-and-review-habits/session-notes.md) *(`interview`)*
- **2026-08-18** — [Interview — Nurse Manager on Unit Champions](../raw/2026-08-18-interview-nurse-manager-unit-champions/session-notes.md) *(`interview`)*

## Related Findings
- [AI Governance, PHI & Compliance](governance-and-phi.md)
- [Ambient AI Scribe](ambient-scribe.md)
