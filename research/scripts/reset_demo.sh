#!/usr/bin/env bash
# Resets a research-repo-demo checkout back to the demo-baseline tag and rebuilds its
# index, so the public CRUD UI demo can't accumulate edits between resets.
#
# NOT YET SCHEDULED ANYWHERE. This is written ahead of the demo server's own deployment
# (the CRUD UI's webhost deployment isn't live yet as of 2026-09-22) so it's ready the
# moment a server exists and a cron job can be pointed at it. See docs/demo-deploy.md
# for what's still unwired before that can happen.
set -euo pipefail

# Wrapped in main(), called only after the whole file is parsed: this script runs from inside
# the clone it resets, so `git reset --hard` below can rewrite this very file mid-run, and an
# unwrapped script would have bash reading those rewritten bytes partway through.
main() {
  cd "$(dirname "$0")/../.."

  # --tags --force: demo-baseline is force-moved on GitHub on every demo sync, and a plain
  # fetch will not update a local tag that already exists, so this script would silently keep
  # resetting to a stale commit. This is intentionally different from research-repo-crud-ui's
  # scripts/deploy.sh, which must NOT force-fetch tags.
  git fetch --tags --force origin
  git reset --hard demo-baseline

  PYTHON_BIN="${PYTHON_BIN:-python3}"
  "$PYTHON_BIN" research/scripts/build_index.py
}

main "$@"
