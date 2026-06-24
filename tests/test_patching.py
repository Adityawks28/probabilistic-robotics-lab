"""★ Protect the patching pipeline.

The mandatory sanity checks (CLAUDE.md §4 hard-stop #3) live here. They stay SKIPPED
(not failing) until the hooks + patch primitives are built and validated interactively
with the human — at which point they become the gate that must pass before any sweep:

  * clean → clean patch recovers ~100%   (patching a clean donor into a clean run is a no-op)
  * corrupted → corrupted stays broken    (patching a corrupted donor changes nothing)
"""

import pytest


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
