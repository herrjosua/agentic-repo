---
title: "Onboarding Flow — Step 3 Wireflow"
date: 2026-02-21
status: draft
designer: Sam Okafor
tags: ["onboarding", "wireflow"]
related_findings: []
source_type: native
flow_name: "Step 3 invite-team, with branch for skip attempt"
---

## Overview
Combines the step 3 flow logic with its wireframe, including the branch
where a user tries to skip and sees the "required" messaging instead.

## Flow + screens
Step 2 complete -> Step 3 loads (draft list empty) -> user adds email(s) ->
"Draft — not sent" tag appears -> user clicks Next -> Step 4. Skip attempt
branch: user clicks "Skip" -> inline message explains why it can't be
skipped -> returns to Step 3.
