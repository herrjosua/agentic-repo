---
title: Interview — Coding Auditor on Override Tracking and Audit Trail
date: 2026-04-21
type: interview
status: raw
researcher: Priya Patel
tags:
  - him
  - coding
  - audit-trail
  - compliance
  - governance
related_components:
  - coding-suggestion-panel
related_findings:
  - ../../findings/him-coding-and-billing.md
  - ../../findings/governance-and-phi.md
---

# Interview — Coding Auditor on Override Tracking and Audit Trail

## Objective
Follow up on the July 2025 recommendation to bring Compliance into the audit-log design for the AI coding-suggestion concept: understand what an internal coding auditor would need in order to audit, and defend, codes produced with AI assistance. The concept has not been built or piloted; the participant responded to the July 2025 screens and the accept/override tracking described there.

## Method
- **Method:** 1:1 interview, 45 min
- **Researcher:** Priya Patel
- **Full participant roster:** see `participants.md` in this folder
- **Context:** Participant does internal retrospective coding audits (sample-based review of coded encounters) and supports responses to external audits and claim denials.

## Key Findings
- **[CRITICAL]** *(audit trail)* The auditor said they could not defend a code in an external audit, or on a claim denial appeal, without a per-code record of what the tool suggested, what the coder accepted, what the coder overrode and what they changed it to, and who did it and when. A flag saying "AI assistance was used" on the encounter isn't enough. Without the per-code record they would recommend Compliance not sign off on the tool going live.
- **[HIGH]** *(governance)* Wants generation metadata (the suggestion, the source text it cited, the model version and, for the note itself, which parts were scribe-drafted) visible to coding auditors, not internal-only in the sense of "only IT can pull it". They had no objection to keeping it off the permanent chart, in line with the CMIO's attestation model, but said "internal" has to include the people who audit the codes.
- **[MEDIUM]** *(sampling)* For at least the first year they would audit AI-accepted codes at a higher rate than codes the coder entered themselves, as an informal starting point "maybe double the usual sample". They would focus on suggestions accepted without any edit and on unspecified codes. They would also compare acceptance and override rates across coders: someone who accepts nearly everything would be a reason to look closer, not a sign of efficiency.

## Representative Quotes
> "When I pull a chart the question is always the same: who picked this code, and why. If the answer is 'the system suggested it and somebody clicked accept,' I can't stand behind that in front of anyone."
> — Coding Auditor, P122

> "I don't need it on the chart. I need it somewhere I can actually see it. 'Internal' can't mean only IT can get to it."
> — Coding Auditor, P122

## Recommendations
1. Make the per-code suggested / accepted / overridden record (with user and timestamp) a release-blocking requirement for the coding-suggestion concept, and spec it jointly with Compliance and coding audit.
2. Add the question of who can access the internal audit log to the still-pending Legal/Compliance ratification of the CMIO's attestation model. The model says where the metadata lives, not who can read it.
3. Design the audit log so it can be filtered by acceptance status (accepted as suggested, edited, overridden) to support targeted sampling.

## Follow-ups / Open Questions
- Who owns access to the internal audit log the CMIO's model describes, and does it already exist for scribe-drafted notes?
- Confirm with Compliance whether a higher audit rate for AI-accepted codes would need to be written into coding audit policy.

## Related
- Synthesized into: [him-coding-and-billing.md](../../findings/him-coding-and-billing.md), [governance-and-phi.md](../../findings/governance-and-phi.md)
