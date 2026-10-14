---
title: Interview — Transitions-of-Care Coordinator on Medication Changes after Discharge
date: 2026-04-16
type: interview
status: raw
researcher: Priya Patel
tags:
  - care-coordination
  - medication-safety
  - chart-review
  - alert-triage
  - workflow
related_components:
  - alert-triage-queue
related_findings:
  - ../../findings/care-coordination-triage.md
---

# Interview — Transitions-of-Care Coordinator on Medication Changes after Discharge

## Objective
Understand how a transitions-of-care coordinator, who follows patients from an inpatient discharge to home, handles medication changes on post-discharge calls, given the January 2025 baseline's finding that coordinators distrust the EHR's after-visit summaries for missing changed medications. A second question was how discharge alerts fit the alert queue, given the August 2025 finding that the AI ranking weighted recency more heavily than coordinators' sense of clinical risk.

## Method
- **Method:** 1:1 interview, 45 min
- **Researcher:** Priya Patel
- **Full participant roster:** see `participants.md` in this folder
- **Context:** The participant makes follow-up calls to patients after an inpatient discharge. Discharge alerts reach them through the same chronological queue other coordinators use; the AI-ranked queue tested in August 2025 hasn't been built. They did not take part in any earlier session. They read the discharge note and the clinicians' signed notes, some of them scribe-drafted since GA, but don't use the scribe.

## Key Findings
- **[HIGH]** *(medication changes)* On post-discharge calls, the discharge paperwork the patient has and the current medication list sometimes disagree. When they do, the coordinator reads the discharge note itself and calls the clinic to confirm before going through medications with the patient. They recalled the after-visit summary leaving out a medication change "a few times this year", but they kept no log, couldn't say how many and couldn't say how many summaries were correct. This is a recollection, not a rate, and it doesn't answer the baseline's question of how often the AVS misses medication changes.
- **[MEDIUM]** *(alert timing)* For discharge alerts, they said time since discharge *is* the clinical risk: the first days at home are when a missed medication change or a missed follow-up matters most, so a recent discharge should rise to the top. This refines rather than contradicts the August 2025 finding that the model weighted recency more heavily than coordinators' sense of clinical risk: for this alert type, recency and risk point the same way, so the right ranking signal depends on the alert type.

## Representative Quotes
> "If the paperwork and the med list don't match, I don't pick one. I read the discharge note and I call the clinic, and then I call the patient."
> — Care Coordinator (transitions of care), P131

> "For a discharge, newer is worse. The first few days home are when things go wrong."
> — Care Coordinator (transitions of care), P131

## Recommendations
1. Don't treat recency as a single global weight in any ranking model: test whether coordinators' risk judgement differs by alert type, with discharge alerts as one case where recency and risk line up.
2. Keep the medication reconciliation step human on post-discharge calls; nothing here supports summarising medication changes for coordinators without the discharge note alongside.

## Follow-ups / Open Questions
- How often the AVS misses medication changes is still not known. This interview adds a recollection, not a rate; closing it needs incident or complaint logs, or a chart audit comparing summaries with reconciled medication lists.
- Which other alert types, if any, behave like discharge alerts? Not covered in this session.

## Related
- Synthesized into: [care-coordination-triage.md](../../findings/care-coordination-triage.md)
