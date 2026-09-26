---
title: "AI-Assisted Prior Authorization Drafting — Service Topology (v2)"
date: 2025-11-20
status: final
designer: Sam Okafor
tags: ["prior-auth", "utilization-management", "v2", "service-blueprint"]
related_findings: ["../research/findings/prior-authorization.md"]
source_type: native
scope: "AI-drafted prior authorization justification, from encounter chart to UM submission"
version: "v2"
---

## Overview
Maps the `prior-auth-drafting-panel` front end against the backend it actually depends on, drawn
up after v2 testing confirmed the citation feature is actively used rather than ignored as
friction.

## Map
Encounter chart -> Chart-Data Service (pulls diagnosis/treatment history) -> Drafting Model
(generates justification text + inline citations back to specific chart spans) -> Payer-Rules
Lookup (validates against current, not cached, diagnosis codes — the fix that closed the v1
data-freshness bug) -> UM Review Queue (nurse accepts/edits/rejects) -> Submission Service.
Citation links resolve to specific chart-text spans rather than section headers, which is why
nurses could meaningfully check at least one citation before accepting in v2.

Recommendation status: supports the "pilot expansion" recommendation in
`prior-authorization.md` — the data-freshness fix is now a tracked backend dependency, not just a
UI note, and should stay visible as one before expanding beyond straightforward cases.
