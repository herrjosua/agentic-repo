#!/usr/bin/env bash
# Resets a research-repo-demo checkout back to the demo-baseline tag and rebuilds its
# index, so the public CRUD UI demo can't accumulate edits between resets.
#
# NOT YET SCHEDULED ANYWHERE. This is written ahead of the demo server's own deployment
# (the CRUD UI's webhost deployment isn't live yet as of 2026-09-22) so it's ready the
# moment a server exists and a cron job can be pointed at it. See docs/demo-deploy.md
# for what's still unwired before that can happen.
set -euo pipefail

cd "$(dirname "$0")/../.."

git fetch origin
git reset --hard demo-baseline

python3 research/scripts/build_index.py
