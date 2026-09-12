---
title: Contextual Inquiry — Health Information Management (Release of Information)
date: 2025-07-15
type: contextual-inquiry
status: raw
tags:
  - him
  - release-of-information
  - phi
  - workflow
  - compliance
related_components:
  - roi-redaction-tool
related_findings:
  - ../../findings/him-coding-and-billing.md
---

# Contextual Inquiry — Health Information Management (Release of Information)

## Objective
Understand the current release-of-information (ROI) workflow to evaluate whether AI could help identify and redact PHI in records being released, without introducing compliance risk.

## Method
- **Method:** In-person shadowing, 2 sessions x 2 hours
- **Researcher:** M. Okafor
- **Full participant roster:** see `participants.md` in this folder

## Key Findings
- **[HIGH]** *(liability sensitivity)* Staff described ROI as the single area where a mistake (releasing the wrong record, or failing to redact substance-use or behavioral-health notes protected under stricter rules) has caused real incidents in the past and is treated with extreme caution — any AI assistance here would need an unusually high accuracy bar and human final sign-off, no exceptions.
- **[HIGH]** *(42 CFR Part 2 awareness)* Specialists manually flag behavioral health and substance use disorder notes for a stricter, separate redaction process (per 42 CFR Part 2), a distinction that isn't currently represented as structured data anywhere in the EHR — it lives in staff training and memory.
- **[MEDIUM]** *(volume)* ROI requests have grown ~18% year over year per the supervisor's informal tracking, driving interest in any tool that reduces manual redaction time, but not at the cost of the accuracy bar above.

## Representative Quotes
> "This is the department where a mistake doesn't just look bad, it can be a federal violation. I need to see exactly what an AI redacted and why before I'd ever trust it."
> — HIM Supervisor, P67

> "Nothing in the system tells you 'hey, this note needs Part 2 handling.' You just have to know. That's scary when we train someone new."
> — HIM Specialist, P69

## Recommendations
1. If AI redaction assistance is pursued, scope it as a 'suggest and highlight for human review' tool only, never auto-redact-and-release, given the stated risk tolerance.
2. Separately from AI: recommend flagging 42 CFR Part 2-protected note types as structured metadata in the EHR, which would benefit this workflow regardless of any AI tool and reduce reliance on institutional memory.

## Follow-ups / Open Questions
- Get actual (not informal) ROI volume and error/incident trend data from HIM leadership.
- Check whether 42 CFR Part 2 flagging as structured metadata is already on any other team's roadmap.

## Related
- Synthesized into: [him-coding-and-billing.md](../../findings/him-coding-and-billing.md)
