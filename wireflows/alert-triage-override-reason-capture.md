---
title: "Alert Triage Override — Reason-Capture Wireflow"
date: 2025-09-15
status: in-review
designer: Sam Okafor
tags: ["care-coordination", "alert-triage", "alert-fatigue", "wireflow", "workflow"]
related_findings: ["../research/findings/care-coordination-triage.md"]
source_type: native
flow_name: "Alert override with reason capture, addressing the missing override-reason gap"
---

## Overview
Combines the override-reason-capture flow logic with its screens, directly answering the Aug 2025
usability test's recommendation that overrides currently lose the "why" — both a
model-improvement signal and a sense of coordinator agency the study's supervisor specifically
flagged as a risk.

## Flow + screens
`alert-triage-queue` (ranked list) -> coordinator disagrees with a rank -> taps "Override" ->
reason-capture modal opens (short reason list: patient-history risk / recency not clinically
relevant / other + free text) -> confirm -> queue re-sorts, overridden item shows a small
"reviewed" marker -> reason logged for model-tuning review, not surfaced to other coordinators.
Skip-reason branch: coordinator dismisses the modal without selecting a reason -> override still
applies, but is flagged in the model-tuning log as "reason not captured" rather than silently
treated the same as a reasoned override.
