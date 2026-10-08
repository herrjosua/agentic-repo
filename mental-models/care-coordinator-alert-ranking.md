---
title: "Care Coordinators' Mental Model of Alert Ranking"
date: 2025-09-05
status: final
designer: Sam Okafor
tags: ["care-coordination", "alert-triage", "alert-fatigue", "workflow", "project-care-coordination"]
related_findings: ["../research/findings/care-coordination-triage.md"]
source_type: native
scope: "Alert triage ranking in the care-coordination queue"
---

## Overview
**Evidence basis:** Inferred. Built from the ranking disagreements and override gap in `raw/2025-08-26-usability-test-alert-triage-ai-care-coordination/session-notes.md:28-30,37`; how coordinators think about ranking is the designer's reading, not something participants were asked.

Covers how care coordinators conceptualize "ranking" in the alert-triage queue versus what they saw
it do, drawn from the Aug 2025 usability test's override-disagreement pattern.

## Model
The designer's paraphrase of the coordinator view: the system should defer to the coordinator's
sense of a patient's history-driven risk — an experience-weighted judgment call. This rests on one coordinator, P81: "I wanted to tell it 'no, this one's
more urgent because I know this patient's history,' but there was nowhere to put that."
Participants saw the ranking weight recency more heavily than their own sense of clinical risk;
4 of 5 disagreed with the AI's top-3 ranking on at least one of three test queues. There's no way
for a coordinator's override to feed back into the ranking. Triage of a 20-item queue was still
faster with the AI ranking than with a chronological queue in this simulated test (avg 6.5 min vs.
9 min).
