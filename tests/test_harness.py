"""Sanity checks on the test harness itself: the fake repo is isolated and runnable."""
import conftest


def test_fake_repo_is_outside_real_repo(fake_repo):
    assert conftest.REAL_REPO_ROOT not in fake_repo.parents


def test_script_copies_resolve_to_fake_repo(run_script, fake_repo):
    result = run_script("export_records.py", "--summary")
    assert result.returncode == 0, result.stderr
    assert str(conftest.REAL_REPO_ROOT) not in result.stdout


def test_patch_roots_redirects_modules(patch_roots):
    import build_search_ui

    assert build_search_ui.RAW_ROOT == patch_roots / "research" / "raw"
