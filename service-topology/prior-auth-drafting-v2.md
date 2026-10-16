---
title: "AI-Assisted Prior Authorization Drafting — Service Topology (v2)"
date: 2025-11-20
status: final
designer: Sam Okafor
tags: ["prior-auth", "utilization-management", "v2", "service-blueprint", "project-prior-auth"]
related_findings: ["../research/findings/prior-authorization.md"]
source_type: native
scope: "AI-drafted prior authorization justification, from encounter chart to UM submission"
version: "v2"
---

## Overview
**Evidence basis:** Mixed. Observed (the v2 results and recommendation, from `raw/2025-11-04-usability-test-prior-auth-ai-v2/session-notes.md:29-30,39`, and the as-of note, from `raw/2026-06-16-interview-utilization-review-nurse-case-scope/session-notes.md:30` and `raw/2026-09-17-interview-utilization-review-nurse-citation-checking/session-notes.md:30`); illustrative (the backend chain is the designer's illustration; no session describes the backend, and `raw/2025-04-08-usability-test-prior-auth-ai-v1/session-notes.md:46` left the cause of the v1 outdated-code issue open).

Maps the `prior-auth-drafting-panel` front end against the backend it actually depends on, drawn
up after v2 testing confirmed the citation feature is actively used rather than ignored as
friction.

## Map
The backend chain below is the designer's illustration; no research session describes the backend.
Encounter chart -> Chart-Data Service (pulls diagnosis/treatment history) -> Drafting Model
(generates justification text + inline citations back to specific chart spans) -> Payer-Rules
Lookup (validates against current, not cached, diagnosis codes) -> UM Review Queue (nurse
accepts/edits/rejects) -> Submission Service.
Citation links resolve to specific chart-text spans rather than section headers. In v2, 3 of 4
clicked into at least one citation before accepting.

As of 2026-09-17: in daily work a nurse may stop using the draft partway through a case and finish
it by hand (2026-06-16 `:30`), and "clicked into at least one citation" records that a citation
was opened, not what the nurse checked (2026-09-17 `:30`).

Recommendation status: supports the "pilot expansion" recommendation in
`prior-authorization.md`, within the straightforward-case scope (2025-11-04 `:39`).
