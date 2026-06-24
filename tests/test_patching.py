"""★ Protect the patching pipeline.

The mandatory sanity checks (CLAUDE.md §4 hard-stop #3) live here. They stay SKIPPED
(not failing) until the hooks + patch primitives are built and validated interactively
with the human — at which point they become the gate that must pass before any sweep:

  * clean → clean patch recovers ~100%   (patching a clean donor into a clean run is a no-op)
  * corrupted → corrupted stays broken    (patching a corrupted donor changes nothing)
"""

import pytest

from vlamem.patching.causal_mediation import necessity_share, sufficiency_share


# ── Pure mediation arithmetic (necessity AND sufficiency) ───────────────────────────


def test_sufficiency_full_recovery_is_one():
    # Patching clean conditioning into corrupted fully recovers → 1.0 (backbone-localized).
    assert sufficiency_share(perf_clean=1.0, perf_corrupted=0.0, perf_clean_patch=1.0) == 1.0


def test_sufficiency_no_recovery_is_zero():
    assert sufficiency_share(perf_clean=1.0, perf_corrupted=0.0, perf_clean_patch=0.0) == 0.0


def test_necessity_full_break_is_one():
    # Patching corrupted conditioning into a clean run breaks it fully → 1.0.
    assert necessity_share(perf_clean=1.0, perf_corrupted=0.0, perf_corrupt_patch=0.0) == 1.0


def test_necessity_no_break_is_zero():
    assert necessity_share(perf_clean=1.0, perf_corrupted=0.0, perf_corrupt_patch=1.0) == 0.0


def test_mediation_raises_without_cliff():
    with pytest.raises(ValueError):
        sufficiency_share(perf_clean=0.9, perf_corrupted=0.9, perf_clean_patch=0.9)
    with pytest.raises(ValueError):
        necessity_share(perf_clean=0.9, perf_corrupted=0.9, perf_corrupt_patch=0.9)


# ── Model-running sanity checks (stay SKIPPED until hooks validated) ─────────────────


@pytest.mark.skip(reason="P0.4: implement + validate hooks before trusting this (CLAUDE.md §4)")
def test_clean_to_clean_recovers_fully():
    # Patching a clean backbone activation into a clean run must be a no-op (~100%).
    raise NotImplementedError


@pytest.mark.skip(reason="P0.4: implement + validate hooks before trusting this (CLAUDE.md §4)")
def test_corrupted_to_corrupted_stays_broken():
    # Patching a corrupted donor into a corrupted run must not recover performance.
    raise NotImplementedError


@pytest.mark.skip(reason="P0.4: implement after hook points are confirmed (P0.3)")
def test_patched_run_uses_donor_activation():
    raise NotImplementedError
