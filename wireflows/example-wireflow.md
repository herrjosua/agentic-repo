---
title: "Onboarding Flow — Step 4 (Invite Your Team) Wireflow"
date: 2026-02-21
status: draft
designer: Sam Okafor
tags: ["onboarding", "wireflow"]
related_findings: []
source_type: native
flow_name: "Step 4 invite-team, with branch for skip attempt"
---

## Overview
Combines the step 4 ("Invite your team") flow logic with its wireframe, including the branch
where a user tries to skip and sees the "required" messaging instead.

## Flow + screens
Step 3 complete -> Step 4 loads (draft list empty) -> user adds email(s) ->
"Draft — not sent" tag appears -> user clicks Next -> Step 5. Skip attempt
branch: user clicks "Skip" -> inline message explains why it can't be
skipped -> returns to Step 4.
