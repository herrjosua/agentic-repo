# Demo deploy

A public demo of the CRUD UI runs on top of this repo's content at
https://ux-research.joshuabock.com. Visitors can edit it, but their
edits don't last: an hourly reset discards them and puts the content back to the last synced
baseline. The decision behind this setup is
[decision 11 in `decisions.md`](decisions.md#11-demo-isolation-a-separate-repo-and-a-scoped-sync-workflow).

The demo runs against `research-repo-demo`, a separate, private repo kept in sync with this repo's
`research/`, `design-tokens/`, and `analytics/` content (plus the 20 deliverable folders and
`requirements.txt`) — see AGENTS.md → "Demo repo sync" for the full sync mechanics.

- **Sync:** `.github/workflows/sync-demo.yml` runs on a schedule (every 6 hours) and on
  `workflow_dispatch`. On success it force-moves a fixed tag, `demo-baseline`, onto the synced
  commit.
- **Access:** the demo server pulls `research-repo-demo` with its own read-only deploy key on that
  repo — separate from the `DEMO_REPO_PAT` repo secret, which the sync workflow uses for push
  access and isn't reused here.
- **Reset:** an hourly job on the demo host fetches tags, hard-resets the checkout to the
  `demo-baseline` tag and rebuilds the index, so the demo can't accumulate visitor edits.
  `research/scripts/reset_demo.sh` documents the same steps (`git fetch --tags --force origin`,
  `git reset --hard demo-baseline`, then `build_index.py` run with `PYTHON_BIN`, default
  `python3`), but the scheduled job runs them inline rather than calling the script. To set up
  the reset on a host with a checkout of `research-repo-demo`, run these steps hourly through the
  host's scheduler, either by calling `reset_demo.sh` or inline, and set `PYTHON_BIN` to the
  host's virtualenv Python if `python3` on `PATH` isn't right.

For local setup of this repo, see [`SETUP.md`](SETUP.md).
