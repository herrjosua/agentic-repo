---
title: "Care Coordinators' Mental Model of Alert Ranking"
date: 2025-09-05
status: final
designer: Sam Okafor
tags: ["care-coordination", "alert-triage", "alert-fatigue", "workflow"]
related_findings: ["../research/findings/care-coordination-triage.md"]
source_type: native
scope: "Alert triage ranking in the care-coordination queue"
---

## Overview
Covers how care coordinators conceptualize "ranking" in the alert-triage queue versus how the
ranking model actually works, drawn from the Aug 2025 usability test's override-disagreement
pattern.

## Model
Coordinators think of ranking as "the system should defer to my sense of this patient's
history-driven risk" — an experience-weighted judgment call built from things the model doesn't
see. The model actually ranks by recency-weighted signals. Neither model is visible to the other:
the queue doesn't surface its ranking basis, and there's no way for a coordinator's override to
feed back into it. This mismatch, not raw ranking accuracy, is why 4 of 5 participants disagreed
with at least one ranking decision even though the tool was objectively faster than manual review.
