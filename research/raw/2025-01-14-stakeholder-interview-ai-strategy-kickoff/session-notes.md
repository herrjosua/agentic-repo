---
title: AI Strategy Kickoff — Executive Alignment Interview
date: '2025-01-14'
type: interview
status: raw
tags:
  - ai-strategy
  - governance
  - phi
  - executive
  - kickoff
related_components: []
related_findings:
  - ../../findings/governance-and-phi.md
last_edited_by: Josh Bock
last_edited_at: '2026-09-16T17:43:46.576Z'
---
## AI Strategy Kickoff — Executive Alignment Interview

## Objective

Understand executive priorities, risk tolerance, and success criteria for the Compass AI modernization program before any tools are scoped.

## Method

* **Method:** 1:1 stakeholder interview (60 min, recorded w/ consent, transcript scrubbed)
* **Researcher:** Priya Patel
* **Full participant roster:** see `participants.md` in this folder

## Key Findings

* **\[HIGH]**_(risk tolerance)_ Both stakeholders want AI pilots to start in low-PHI-exposure workflows (scheduling, intake) before touching clinical documentation, citing HIPAA audit exposure as the top concern.
* **\[MEDIUM]**_(success criteria)_ VP Clinical Informatics defines success as 'reduced documentation time,' while CIO defines success as 'reduced vendor sprawl' — the two are not currently reconciled in a shared metric.
* **\[MEDIUM]**_(governance)_ Neither stakeholder could name who owns model-output accuracy sign-off; assumed it would 'probably fall to compliance.'
* **\[LOW]**_(change management)_ Both anticipate clinician skepticism based on a prior failed CDS (clinical decision support) alert rollout in 2022.

## Representative Quotes

> "We can't be the org that leaks PHI through some vendor's training pipeline. That's the headline we're trying to avoid, not chase."
> — Chief Information Officer, P01

> "If a doctor spends less time typing and more time looking at the patient, I don't care what's under the hood."
> — VP Clinical Informatics, P02

## Recommendations

1. Facilitate a follow-up session to align on 2-3 shared, measurable success metrics before scoping any pilot.
2. Document a RACI for AI-output review/sign-off; surface the gap to Compliance directly.
3. Reference the 2022 CDS alert rollout retro in early clinician-facing research to avoid repeating known failure modes.

## Follow-ups / Open Questions

* Who in Compliance should own model-output sign-off? Schedule follow-up interview.
* Request access to 2022 CDS alert rollout post-mortem if it exists.

## Related

* Synthesized into: [governance-and-phi.md](../../findings/governance-and-phi.md)
