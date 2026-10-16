"""
Guard against re-creating the retired Fernway onboarding sample thread (docs/decisions.md
section 21). It was removed once before and came back through scaffolding, so this test fails if
a retired name shows up in any tracked file's path or content, or if a retired path is tracked
again.

The check is a pure function over in-memory data (find_violations); the last test runs it on the
real repo's tracked files (git ls-files), reading only, so the conftest snapshot guard holds.
"""
import subprocess
from collections.abc import Iterable, Mapping
from pathlib import Path

from conftest import REAL_REPO_ROOT

# Matched case-insensitively as substrings, against both file contents and file paths.
RETIRED_TERMS = (
    "fernway",
    "dana-overwhelmed-new-admin",
    "2026-01-19-onboarding-usability-test",
    "onboarding-carousel",
)

# The 24 files removed in RR-195. None may be tracked again.
RETIRED_PATHS = frozenset({
    "research/findings/onboarding.md",
    "analytics/summaries/onboarding-funnel-dropoff.md",
    "research/raw/2026-01-19-onboarding-usability-test/session-notes.md",
    "research/raw/2026-01-19-onboarding-usability-test/participants.md",
    "research-plans/onboarding-usability-study-q1.md",
    "facilitation-guides/onboarding-usability-guide.md",
    "topline-summaries/example-topline-summary.md",
    "research-readouts/onboarding-flow-q1-readout.md",
    "heuristic-evaluations/example-heuristic-evaluation.md",
    "accessibility-screenings/example-accessibility-screening.md",
    "service-topology/example-service-topology.md",
    "personas/dana-overwhelmed-new-admin.md",
    "mental-models/example-mental-model.md",
    "mindsets/example-mindset.md",
    "journey-maps/example-journey-map.md",
    "thumbnails/example-thumbnail.md",
    "wireframes/workspace-setup-step4-invite-team.md",
    "user-flows/onboarding-flow.md",
    "wireflows/example-wireflow.md",
    "storyboards/example-storyboard.md",
    "mockups/example-mockups.md",
    "prototypes/example-prototype.md",
    "style-guide/foundations-v3.md",
    "design-system/example-design-system.md",
})

RAW_ID = "2026-01-19-onboarding-usability-test"

# File -> the retired terms it may contain. Kept to the minimum; an entry whose term no longer
# occurs in that file fails as stale.
ALLOWLIST: dict[str, frozenset[str]] = {
    # This guard's own term and path lists.
    "tests/test_retired_names.py": frozenset(RETIRED_TERMS),
    # The synthetic test corpus reuses the raw folder name as a fixture name; no real data.
    "tests/conftest.py": frozenset({RAW_ID}),
    # Decision 8 (name-collision history) and decision 21 (the retirement itself).
    "docs/decisions.md": frozenset({"fernway", "dana-overwhelmed-new-admin", RAW_ID}),
    # Point-in-time audit; its existing lines are never edited.
    "docs/ask-audit-2026-09-27.md": frozenset({RAW_ID}),
    # Point-in-time audit plus its RR-195 entry recording the removal.
    "docs/synthesis-audit-2026-09-29.md": frozenset({"fernway", "dana-overwhelmed-new-admin", RAW_ID}),
    # The instruction not to re-create the thread.
    "AGENTS.md": frozenset({"fernway"}),
}


def find_violations(
    files: Mapping[str, str | None],
    retired_terms: Iterable[str] = RETIRED_TERMS,
    retired_paths: Iterable[str] = RETIRED_PATHS,
    allowlist: Mapping[str, Iterable[str]] = ALLOWLIST,
) -> list[str]:
    """Return one message per problem. `files` maps each tracked path to its text, or None for a
    binary or unreadable file (its path is still checked, its content isn't)."""
    terms = [t.lower() for t in retired_terms]
    allowed = {path: {t.lower() for t in ts} for path, ts in allowlist.items()}
    problems: list[str] = []

    for path in sorted(set(retired_paths) & files.keys()):
        problems.append(f"{path}: retired path is tracked")

    for path in sorted(files):
        lowered_path = path.lower()
        for term in terms:
            if term in lowered_path:
                problems.append(f"{path}: path contains retired term {term!r}")

        text = files[path]
        if text is None:
            continue
        ok = allowed.get(path, set())
        for lineno, line in enumerate(text.splitlines(), start=1):
            lowered = line.lower()
            for term in terms:
                if term in lowered and term not in ok:
                    problems.append(f"{path}:{lineno}: retired term {term!r}")

    for path in sorted(allowed):
        text = files.get(path)
        lowered = text.lower() if text is not None else ""
        for term in sorted(allowed[path]):
            if term not in lowered:
                problems.append(f"{path}: stale allowlist entry {term!r} (term no longer in file)")

    return problems


def read_tracked_files(root: Path = REAL_REPO_ROOT) -> dict[str, str | None]:
    listed = subprocess.run(["git", "ls-files", "-z"], cwd=root, capture_output=True, check=True)
    files: dict[str, str | None] = {}
    for rel in listed.stdout.decode("utf-8").split("\0"):
        if not rel:
            continue
        path = root / rel
        text: str | None = None
        if path.is_file():
            data = path.read_bytes()
            if b"\0" not in data:
                try:
                    text = data.decode("utf-8")
                except UnicodeDecodeError:
                    text = None
        files[rel] = text
    return files


# ---------------------------------------------------------------------------------------------
# Unit tests (in-memory)
# ---------------------------------------------------------------------------------------------

TERMS = ("fernway", "old-slug")


def test_term_in_unlisted_file_fails_with_file_line_and_term():
    files = {"docs/a.md": "intro\nThe Fernway product\n"}
    assert find_violations(files, TERMS, (), {}) == ["docs/a.md:2: retired term 'fernway'"]


def test_term_not_listed_for_an_allowlisted_file_fails():
    files = {"docs/a.md": "fernway\nold-slug\n"}
    assert find_violations(files, TERMS, (), {"docs/a.md": {"fernway"}}) == [
        "docs/a.md:2: retired term 'old-slug'",
    ]


def test_allowlisted_use_passes():
    files = {"docs/a.md": "Retired: FERNWAY\n", "docs/b.md": "clean\n"}
    assert find_violations(files, TERMS, (), {"docs/a.md": {"fernway"}}) == []


def test_tracked_retired_path_fails():
    files = {"personas/gone.md": "clean\n"}
    assert find_violations(files, TERMS, {"personas/gone.md"}, {}) == [
        "personas/gone.md: retired path is tracked",
    ]


def test_retired_term_in_path_fails_even_for_binary_file():
    files = {"assets/Old-Slug.png": None}
    assert find_violations(files, TERMS, (), {}) == [
        "assets/Old-Slug.png: path contains retired term 'old-slug'",
    ]


def test_stale_allowlist_entry_fails():
    files = {"docs/a.md": "fernway\n"}
    assert find_violations(files, TERMS, (), {"docs/a.md": {"fernway", "old-slug"}}) == [
        "docs/a.md: stale allowlist entry 'old-slug' (term no longer in file)",
    ]


def test_allowlist_entry_for_untracked_file_is_stale():
    assert find_violations({}, TERMS, (), {"docs/gone.md": {"fernway"}}) == [
        "docs/gone.md: stale allowlist entry 'fernway' (term no longer in file)",
    ]


def test_binary_content_is_not_scanned():
    assert find_violations({"img.png": None}, TERMS, (), {}) == []


# ---------------------------------------------------------------------------------------------
# Real repo
# ---------------------------------------------------------------------------------------------

def test_real_repo_has_no_retired_names_or_paths():
    problems = find_violations(read_tracked_files())
    assert not problems, "Retired Fernway names or paths found:\n" + "\n".join(problems)
