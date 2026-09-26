"""
research/scripts/reset_demo.sh — exercised against a throwaway local git remote standing in for
research-repo-demo, since the real thing only exists once the demo server is live (see
docs/demo-deploy.md). A no-op PYTHON_BIN stub isolates the git fetch/reset behavior under test
from build_index.py, which test_build_index.py already covers.
"""
import os
import subprocess

import conftest
import pytest

RESET_SCRIPT = conftest.REAL_SCRIPTS_DIR / "reset_demo.sh"

GIT_ENV = {
    **os.environ,
    "GIT_AUTHOR_NAME": "Test", "GIT_AUTHOR_EMAIL": "test@example.com",
    "GIT_COMMITTER_NAME": "Test", "GIT_COMMITTER_EMAIL": "test@example.com",
}


def git(*args, cwd):
    return subprocess.run(
        ["git", *args], cwd=cwd, env=GIT_ENV, capture_output=True, text=True,
        check=True, timeout=30,
    )


def head(cwd):
    return git("rev-parse", "HEAD", cwd=cwd).stdout.strip()


def write(root, rel, content):
    path = root / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return path


def make_demo_remote(tmp_path):
    """A bare repo ("origin") plus a "seed" work dir pushed to it, seeded with a copy of the
    real reset_demo.sh at research/scripts/ and tagged demo-baseline. Returns (bare, seed)."""
    bare = tmp_path / "origin.git"
    git("init", "--bare", "-b", "main", str(bare), cwd=tmp_path)

    seed = tmp_path / "seed"
    seed.mkdir()
    git("init", "-b", "main", cwd=seed)
    git("remote", "add", "origin", str(bare), cwd=seed)

    dest = write(seed, "research/scripts/reset_demo.sh", RESET_SCRIPT.read_text(encoding="utf-8"))
    dest.chmod(0o755)
    write(seed, "README.md", "baseline\n")
    git("add", "-A", cwd=seed)
    git("commit", "-m", "baseline", cwd=seed)
    git("tag", "demo-baseline", cwd=seed)
    git("push", "origin", "main", cwd=seed)
    git("push", "origin", "demo-baseline", cwd=seed)
    return bare, seed


def clone_checkout(tmp_path, bare):
    checkout = tmp_path / "checkout"
    git("clone", str(bare), str(checkout), cwd=tmp_path)
    return checkout


def sync(seed, changes):
    """Simulates a sync-demo.yml run: commits `changes` (rel path -> content) on top of `seed`,
    pushes to origin/main, and force-moves demo-baseline onto the new commit. Returns its sha."""
    for rel, content in changes.items():
        write(seed, rel, content)
    git("add", "-A", cwd=seed)
    git("commit", "-m", "sync", cwd=seed)
    git("push", "origin", "main", cwd=seed)
    git("tag", "-f", "demo-baseline", cwd=seed)
    git("push", "--force", "origin", "demo-baseline", cwd=seed)
    return head(seed)


def run_reset(checkout, python_stub):
    return subprocess.run(
        ["bash", "research/scripts/reset_demo.sh"], cwd=checkout,
        env={**os.environ, "PYTHON_BIN": str(python_stub)},
        capture_output=True, text=True, timeout=60,
    )


@pytest.fixture
def python_stub(tmp_path):
    """A no-op stand-in for build_index.py's interpreter, so these tests only exercise the
    fetch/reset step."""
    stub = tmp_path / "python_stub.sh"
    stub.write_text("#!/usr/bin/env bash\nexit 0\n", encoding="utf-8")
    stub.chmod(0o755)
    return stub


def test_stale_local_tag_is_updated_after_force_moved_sync(tmp_path, python_stub):
    bare, seed = make_demo_remote(tmp_path)
    checkout = clone_checkout(tmp_path, bare)

    new_sha = sync(seed, {"README.md": "updated\n"})
    assert head(checkout) != new_sha  # stale until the script fetches

    result = run_reset(checkout, python_stub)

    assert result.returncode == 0, result.stderr
    assert head(checkout) == new_sha


def test_sync_that_rewrites_reset_demo_sh_itself_still_completes(tmp_path, python_stub):
    bare, seed = make_demo_remote(tmp_path)
    checkout = clone_checkout(tmp_path, bare)

    rewritten = (seed / "research/scripts/reset_demo.sh").read_text(encoding="utf-8")
    rewritten += "\n# sync-demo.yml touched this file in the new commit\n"
    new_sha = sync(seed, {"research/scripts/reset_demo.sh": rewritten})
    assert head(checkout) != new_sha

    result = run_reset(checkout, python_stub)

    assert result.returncode == 0, result.stderr
    assert head(checkout) == new_sha
