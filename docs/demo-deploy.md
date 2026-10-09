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
  `demo-baseline` tag and reruns `build_index.py`, which rebuilds all the indexes
  (`research/_index.md`, `analytics/_index.md` and each deliverable folder's `_index.md`), so the
  demo can't accumulate visitor edits.
  `research/scripts/reset_demo.sh` documents the same steps (`git fetch --tags --force origin`,
  `git reset --hard demo-baseline`, then `build_index.py` run with `PYTHON_BIN`, default
  `python3`), but the scheduled job runs them inline rather than calling the script. To set up
  the reset on a host with a checkout of `research-repo-demo`, run these steps hourly through the
  host's scheduler, either by calling `reset_demo.sh` or inline, and set `PYTHON_BIN` to the
  host's virtualenv Python if `python3` on `PATH` isn't right.

## Merge-to-live chain

A corpus change reaches the demo through seven steps. Only step 3 follows automatically from the
one before it; every other step waits on a schedule or a person.

| # | Step | Runs on | Trigger |
|---|---|---|---|
| 1 | A PR merges to `main` in this repo, with `research/search.html` regenerated in it (`python research/scripts/build_search_ui.py`). CI's `build_search_ui.py --check` fails the PR otherwise. | Local machine (regenerate), GitHub (CI, merge) | Manual |
| 2 | `sync-demo.yml` runs. A push to `main` doesn't trigger it: it runs every 6 hours, or by hand from the Actions tab (`workflow_dispatch`). | GitHub | Schedule or manual |
| 3 | `research-repo-demo`'s `main` is updated and the `demo-baseline` tag moves onto it. | GitHub | Automatic, inside the sync (only if its `build_index.py --check` passes) |
| 4 | The demo host resets its checkout to `demo-baseline` and rebuilds the indexes. | Web host | Hourly scheduled job |
| 5 | Re-point the `agentic-repo-dev` clone at the new commit (`git fetch`, then reset to `origin/main`), rerun the CRUD UI's evaluation harness for a new baseline, then recapture, review and publish the static Ask answers. | Local machine (needs a local Ollama) | Manual |
| 6 | Open a CRUD UI PR with the new `answers.json`, cut a release tag, and approve the production environment. | GitHub (CRUD UI repo) | Manual |
| 7 | Run the CRUD UI's `capture-static-answers.js verify` against a checkout of the corpus, the demo's or the local clone. Nothing runs it after a sync or a reset. | The CRUD UI repo's backend, against a local or demo checkout | Manual |

**Until steps 5–7 are done, the demo serves the new corpus next to static answers captured
against the old one.** Their citations can point at text that no longer exists in the form they
quote.

Two gaps in the automated part of the chain:

- **The sync doesn't check `search.html`.** Its guard runs `build_index.py --check` only, not
  `build_search_ui.py --check`, so a stale `research/search.html` would be copied to the demo
  as is. It relies on CI having passed on the PR that changed the corpus.
- **The reset doesn't run `git clean`.** `git reset --hard` restores tracked files only, so a file
  that isn't tracked in git survives the hourly reset.

For local setup of this repo, see [`SETUP.md`](SETUP.md).
