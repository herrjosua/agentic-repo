---
title: "Alert Triage Override — Reason-Capture Wireflow"
date: 2025-09-15
status: in-review
designer: Sam Okafor
tags: ["care-coordination", "alert-triage", "alert-fatigue", "wireflow", "workflow", "project-care-coordination"]
related_findings: ["../research/findings/care-coordination-triage.md"]
source_type: native
flow_name: "Alert override with reason capture, addressing the missing override-reason gap"
---

## Overview
**Evidence basis:** Mixed. Observed (the problem the flow answers, from `raw/2025-08-26-usability-test-alert-triage-ai-care-coordination/session-notes.md:28-29,31,37,41`, and the as-of notes, from `raw/2026-07-07-interview-care-coordinator-override-reason-capture/session-notes.md:30-32`, `raw/2026-04-16-interview-care-coordinator-transitions-medication-changes/session-notes.md:32` and `raw/2026-05-05-interview-care-coordinator-supervisor-queue-oversight/session-notes.md:31`); illustrative (the flow and screens are the designer's response; no session observed them in use).

Combines the override-reason-capture flow logic with its screens, directly answering the Aug 2025
usability test's recommendation that overrides currently lose the "why". The study recommended
capturing it both to improve the model and to give coordinators a sense of agency the current
design lacks. The study's supervisor raised a separate concern: that speed gains could mask
coordinators rubber-stamping the AI order without real judgment.

## Flow + screens
`alert-triage-queue` (ranked list) -> coordinator disagrees with a rank -> taps "Override" ->
reason-capture modal opens (short reason list: patient-history risk / recency not clinically
relevant / other + free text) -> confirm -> queue re-sorts, overridden item shows a small
"reviewed" marker -> reason logged for model-tuning review, not surfaced to other coordinators.
Skip-reason branch: coordinator dismisses the modal without selecting a reason -> override still
applies, but is flagged in the model-tuning log as "reason not captured" rather than silently
treated the same as a reasoned override.

As of 2026-07-07: the reason list lacks P81's most common reason, something the patient or a
family member said on the phone that isn't in the chart yet (2026-07-07 `:30`), and for discharge
alerts, time since discharge is the clinical risk (2026-04-16 `:32`). P81 would give a reason in
one tap, not free text, and expected to skip the modal on a busy day (2026-07-07 `:31`). Who sees
the reasons, and what coordinators get back, is unsettled: a supervisor would use them for
coaching (2026-05-05 `:31`), and P81 would stop giving reasons without seeing an effect
(2026-07-07 `:32`).
