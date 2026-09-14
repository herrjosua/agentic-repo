---
title: "Onboarding & Account Provisioning — Service Topology"
date: 2026-02-10
status: in-review
tags: ["onboarding", "service-blueprint"]
related_findings: []
source_type: native
scope: "Signup through first workspace creation"
version: "v1"
---

## Overview
Maps the onboarding wizard's front-end steps against the backend services
they trigger: account creation, workspace provisioning, and calendar OAuth.

## Map
Signup form -> Account Service (sync) -> Workspace Provisioning (async, ~8s
average) -> Calendar OAuth (external, Google/Outlook) -> Invite Service
(sends on submit, not on step completion — this is the source of the step-3
"does this send now?" confusion identified in the usability study).
