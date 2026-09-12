---
title: Patient Scheduling Chatbot
date: 2025-06-17
type: synthesis
status: synthesized
tags:
  - chatbot
  - patient-experience
  - scheduling
  - survey
  - trust
  - usability
related_components:
  - patient-chatbot-widget
  - scheduling-widget
related_findings:
  - rollout-and-change-management.md
---

# Patient Scheduling Chatbot

## Overview
A patient-facing scheduling chatbot was scoped narrowly based on a trust survey (Jun 2025) and then
usability tested against that scope (Jun 2025, two weeks later).

- **The survey drew a sharp, useful line.** 67% of patients were comfortable with an AI chatbot for
  scheduling/rescheduling, but comfort dropped to 22% when extended to symptom-related questions.
  This directly shaped the decision to scope the chatbot to logistics only and explicitly exclude
  symptom Q&A from v1 — a scope decision the usability test then validated by not needing to test
  symptom-handling at all.
- **The "talk to a human" escape hatch, identified as a trust prerequisite in the survey (41% of
  open-ended responses asked for it), failed discoverability testing.** 3 of 8 usability test
  participants couldn't find it — it existed only as a small text link. This is a case where a
  clearly-identified requirement from the survey wasn't sufficiently weighted in the initial design.
- Secondary findings: rescheduling had a lower task-success rate than new bookings (appointment-ID
  friction), and the bot's "overly cheerful" tone was mismatched for patients scheduling around
  illness.

Recommendation: redesign the escape hatch as a persistent, prominent control (not a link) and
re-test discoverability specifically before wider rollout. This chatbot would also be the
non-clinical rollout most likely to run into the awareness gap noted in
[rollout-and-change-management.md](rollout-and-change-management.md).

## Evidence Trail
- **2025-06-03** — [Survey — Patient Trust in AI Chatbot for Scheduling](../raw/2025-06-03-survey-patient-portal-ai-chatbot-trust/session-notes.md) *(`survey`)*
- **2025-06-17** — [Usability Test — Patient Scheduling Chatbot Prototype](../raw/2025-06-17-usability-test-patient-chatbot-prototype/session-notes.md) *(`usability-test`)*

## Related Findings
- [Rollout & Change Management](rollout-and-change-management.md)
