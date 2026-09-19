---
title: Accessibility (Cross-Cutting)
date: 2025-11-18
type: synthesis
status: synthesized
researcher: Priya Patel
tags:
  - accessibility
  - components
  - design-system
  - extjs
  - legacy
  - low-vision
  - mobile
  - motor-impairment
  - section-508
  - wcag
related_components:
  - admin-console-grid
  - alert-triage-queue
  - design-system-form-field
  - design-system-modal
  - mobile-app-alert-list
related_findings: []
---

# Accessibility (Cross-Cutting)

## Overview
Three independent WCAG 2.1 AA audits across the year — the legacy ExtJS admin console (Mar 2025),
the new design system component library (Jul 2025), and the mobile clinician app (Nov 2025) —
turned up one recurring pattern worth calling out on its own, separate from each audit's other
findings.

- **The same color-only status indicator (red/yellow/green dots, no text/pattern alternative)
  appears in all three surfaces audited this year.** This was flagged as a likely single shared root
  component rather than three separate bugs, and the CIO cited it at the December executive retro as
  the example of what a "cross-cutting findings" reporting category should look like going forward
  (see [governance-and-phi.md](governance-and-phi.md)).
- **Progress is visible surface-by-surface even though the pattern repeats**: the modal
  keyboard-trap issue found in the legacy console (Mar) was already fixed by the time the new
  design system's modal component was audited (Jul), though that same audit surfaced a *new* issue
  (form-field error association) not present in the legacy system.
- **The mobile app audit (Nov) connects directly to a live Compass AI feature**: undersized touch
  targets (32×32px vs. the 44×44px minimum) were found specifically on the alert-triage icon set,
  which is the same feature usability-tested in August — see
  [care-coordination-triage.md](care-coordination-triage.md). This is a case where an accessibility
  defect and a usability finding land on the exact same component from two different research
  methods.

Recommendation: treat the color-only status pattern as a single design-system-level fix rather than
three surface-level tickets, and confirm whether a shared component is in fact the common root cause.

## Evidence Trail
- **2025-03-10** — [Accessibility Audit — Legacy Admin Console (ExtJS)](../raw/2025-03-10-accessibility-audit-legacy-extjs-admin-console/session-notes.md) *(`accessibility-audit`)*
- **2025-07-01** — [Accessibility Audit — New Design System Component Library](../raw/2025-07-01-accessibility-audit-new-design-system-components/session-notes.md) *(`accessibility-audit`)*
- **2025-11-18** — [Accessibility Audit — Mobile Clinician App (Low Vision & Motor Impairment Focus)](../raw/2025-11-18-accessibility-audit-mobile-clinician-app/session-notes.md) *(`accessibility-audit`)*

## Related Findings
- (none currently linked)
