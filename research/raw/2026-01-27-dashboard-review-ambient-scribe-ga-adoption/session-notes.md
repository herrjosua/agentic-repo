---
title: "Dashboard review — Ambient scribe GA candidate adoption"
date: 2026-01-27
type: analytics
status: raw
tags:
  - ambient-scribe
  - ga-release
  - dashboard
related_components:
  - ambient-scribe-widget
related_findings:
  - ../../findings/ambient-scribe.md
related_analytics: []
---

# Dashboard review — Ambient scribe GA candidate adoption

## Objective
Manually review the internal usage dashboard for the ambient scribe GA release candidate to see
whether adoption and engagement patterns in real usage match what the GA-candidate usability round
found — particularly whether the per-line confidence highlighting is actually changing reviewing
behavior at scale, not just in the moderated session.

## Method
- **Method:** Manual dashboard review (no moderated session, no participants) — internal analytics
  dashboard covering the first 4 weeks of GA-candidate rollout
- **Researcher:** J. Bock
- **Full participant roster:** none — this is an analytics review, not a research session; see
  `participants.md` in this folder for why

## Key Findings
- **[MEDIUM]** *(trust)* Clinicians who were shown confidence highlighting skim high-confidence
  lines at roughly double the rate of the pre-highlighting cohort — directionally consistent with
  the usability round's finding that visible uncertainty, not raw accuracy, changes reviewing
  behavior.
- **[LOW]** *(adoption)* Adoption is uneven by role: attending physicians are opting in at a
  noticeably higher rate than residents in the same departments, worth understanding qualitatively
  rather than assuming it's a training gap.

## Recommendations
1. Feed this dashboard pattern back into `findings/ambient-scribe.md` as corroborating evidence for
   the confidence-highlighting result, rather than treating it as a separate finding.
2. Consider a short follow-up interview round specifically on the physician/resident adoption gap.

## Follow-ups / Open Questions
- Is the physician/resident adoption gap explained by workflow differences, trust, or something
  else entirely? Dashboard data alone can't answer this.

## Related
- Synthesized into: [ambient-scribe.md](../../findings/ambient-scribe.md)
