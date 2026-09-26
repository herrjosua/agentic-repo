# Demo deploy

A public, read-only demo is live at https://ux-research.joshuabock.com.

It runs against `research-repo-demo`, a separate, private repo kept in sync with this repo's
`research/`, `design-tokens/`, and `analytics/` content (plus the 20 deliverable folders and
`requirements.txt`) — see AGENTS.md → "Demo repo sync" for the full sync mechanics.

- **Sync:** `.github/workflows/sync-demo.yml` runs on a schedule (every 6 hours) and on
  `workflow_dispatch`. On success it force-moves a fixed tag, `demo-baseline`, onto the synced
  commit.
- **Access:** the demo server pulls `research-repo-demo` with its own read-only deploy key on that
  repo — separate from the `DEMO_REPO_PAT` repo secret, which the sync workflow uses for push
  access and isn't reused here.
- **Reset:** the demo resets hourly so it can't accumulate visitor edits. To wire this up on any
  host with a checkout of `research-repo-demo`: schedule `research/scripts/reset_demo.sh` to run
  hourly via cron, setting `PYTHON_BIN` in that cron entry's environment to the host's virtualenv
  Python if `python3` on `PATH` isn't the right interpreter. The script force-fetches tags, resets
  the checkout to `demo-baseline`, and rebuilds `research/_index.md`.
