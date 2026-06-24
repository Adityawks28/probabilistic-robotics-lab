"""★ Activation patching — clean / corrupted / patched runs.

The surgical move that assigns blame between backbone and expert:

  * CLEAN run     — unperturbed input. The backbone produces a "correct" conditioning.
  * CORRUPTED run — meaning-changing perturbation applied. Performance drops.
  * PATCHED run   — run the CORRUPTED input but splice the CLEAN backbone activation
                    into the corrupted forward pass (via models.hooks.patch_activation),
                    then measure how much performance recovers.

Recovery → the backbone's representation was the locus (fix it and the expert behaves).
No recovery → the expert had already memorized; a correct conditioning doesn't help.

MANDATORY sanity checks before trusting any output (run in tests/test_patching.py and
re-run on the full pipeline in Phase 2):
  * clean → clean patch recovers ~100% (patching a clean donor into a clean run is a no-op).
  * corrupted → corrupted stays broken (patching a corrupted donor changes nothing).
If either fails, the hook points or the patch logic are wrong — STOP, do not sweep.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass
class PatchResult:
    """Performance under each run, the inputs to BackboneShare."""

    perf_clean: float
    perf_corrupted: float
    perf_patched: float


def run_clean(model: Any, episode: Any) -> float:
    """Evaluate the model on the unperturbed episode; return a performance scalar."""
    raise NotImplementedError


def run_corrupted(model: Any, episode: Any, perturbation: Any) -> float:
    """Evaluate the model on the meaning-changing-perturbed episode."""
    raise NotImplementedError


def run_patched(model: Any, episode: Any, perturbation: Any, donor: Any) -> float:
    """Evaluate the corrupted episode with the clean backbone activation patched in."""
    raise NotImplementedError


def activation_patch(model: Any, episode: Any, perturbation: Any, donor: Any) -> PatchResult:
    """Run all three conditions on one episode and return their performances."""
    return PatchResult(
        perf_clean=run_clean(model, episode),
        perf_corrupted=run_corrupted(model, episode, perturbation),
        perf_patched=run_patched(model, episode, perturbation, donor),
    )
