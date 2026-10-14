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
**Evidence basis:** Mixed. Observed (what coordinators said about ranking and patient history, from P81 in `raw/2025-08-26-usability-test-alert-triage-ai-care-coordination/session-notes.md:37` and `raw/2026-07-07-interview-care-coordinator-override-reason-capture/session-notes.md:30-38`, P134 in `raw/2026-08-04-interview-care-coordinator-complex-care-alert-volume/session-notes.md:30-37`, and the float-pool counterpoint from P05 in `raw/2026-04-07-interview-care-coordinator-float-pool-system-familiarity/session-notes.md:33` and P136 in `raw/2026-09-01-interview-care-coordinator-float-pool-coverage/session-notes.md:31,37`); inferred (the model itself, built from the ranking disagreements and override gap in `raw/2025-08-26-usability-test-alert-triage-ai-care-coordination/session-notes.md:28-30,37`; how coordinators think about ranking is the designer's reading, not something participants were asked).

Covers how care coordinators conceptualize "ranking" in the alert-triage queue versus what they saw
it do, drawn from the Aug 2025 usability test's override-disagreement pattern.

## Model
The designer's paraphrase of the coordinator view: the system should defer to the coordinator's
sense of a patient's history-driven risk — an experience-weighted judgment call. In 2025 this rested on one coordinator, P81: "I wanted to tell it 'no, this one's
more urgent because I know this patient's history,' but there was nowhere to put that." It now rests on two team coordinators. In 2026, P81 said their most common reason
for moving an alert is something the patient or a family member said on the phone that isn't in
the chart yet, and P134, on a complex care team with a high-risk panel, said "half of deciding
who's at risk is knowing what happened to them last winter" (both observed: what they said, not
measured).
Participants saw the ranking weight recency more heavily than their own sense of clinical risk;
4 of 5 disagreed with the AI's top-3 ranking on at least one of three test queues. There's no way
for a coordinator's override to feed back into the ranking. Triage of a 20-item queue was still
faster with the AI ranking than with a chronological queue in this simulated test (avg 6.5 min vs.
9 min).

## Float-pool counterpoint
The model assumes the coordinator has a patient's history to weigh against the ranking. Float
coordinators often don't. P05, floating in 2026, works the current chronological queue strictly in
order and leaves reprioritising to the team's own coordinators, and P136 would accept a ranked queue
as a starting point because they lack that history, while still checking it (both observed: what
they said about their own practice). Inferred: for float coordinators the ranking may stand in for
the history-driven judgement this model describes, rather than compete with it. That is two voices
on each side (P81 and P134 against P05 and P136), so it is a contrast worth testing, not a pattern.
