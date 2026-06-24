"""★ Causal-mediation framing — necessity AND sufficiency of the backbone representation.

Activation patching is the tool; causal mediation is the lens that turns it into an
attribution. The backbone→expert conditioning is the MEDIATOR between the perturbation
(treatment) and task success (outcome). Report BOTH directions, never just one:

  * SUFFICIENCY — patch the CLEAN conditioning into a CORRUPTED run. How much does
    performance RECOVER? (This is exactly metrics.backbone_share.)
        sufficiency = (perf[corrupted+clean_patch] − perf[corrupted])
                      ───────────────────────────────────────────────
                      (perf[clean]                 − perf[corrupted])

  * NECESSITY — patch the CORRUPTED conditioning into a CLEAN run. How much does
    performance BREAK?
        necessity   = (perf[clean] − perf[clean+corrupt_patch])
                      ──────────────────────────────────────────
                      (perf[clean] − perf[corrupted])

Both ≈ 1 → the backbone conditioning is the locus (restoring it fixes, corrupting it
breaks). Both ≈ 0 → the expert dominates. Split values are themselves informative.

The ARITHMETIC below is PURE and unit-tested. The functions that actually run the
model to produce these performances stay stubs until hooks are validated — a mediation
number from an unverified pipeline is exactly the confident-wrong failure mode (§4).
"""

from __future__ import annotations

from typing import Any

from vlamem.metrics.backbone_share import MIN_CLIFF


def sufficiency_share(perf_clean: float, perf_corrupted: float, perf_clean_patch: float) -> float:
    """Fraction of the clean→corrupted gap RECOVERED by patching the clean conditioning in.

    Identical to ``metrics.backbone_share.backbone_share`` (re-exported here for the
    mediation framing). Raises ``ValueError`` if there is no perturbation cliff.
    """
    cliff = perf_clean - perf_corrupted
    if abs(cliff) < MIN_CLIFF:
        raise ValueError(
            "sufficiency undefined: no perturbation cliff "
            f"(perf_clean={perf_clean}, perf_corrupted={perf_corrupted})."
        )
    return (perf_clean_patch - perf_corrupted) / cliff


def necessity_share(perf_clean: float, perf_corrupted: float, perf_corrupt_patch: float) -> float:
    """Fraction of the clean→corrupted gap REPRODUCED by patching the corrupted conditioning in.

    Args:
        perf_clean: Performance on the clean run.
        perf_corrupted: Performance under the meaning-changing perturbation.
        perf_corrupt_patch: Performance on a CLEAN run with the CORRUPTED conditioning
            patched in (the necessity intervention).

    Raises:
        ValueError: if there is no perturbation cliff (clean ≈ corrupted).
    """
    cliff = perf_clean - perf_corrupted
    if abs(cliff) < MIN_CLIFF:
        raise ValueError(
            "necessity undefined: no perturbation cliff "
            f"(perf_clean={perf_clean}, perf_corrupted={perf_corrupted})."
        )
    return (perf_clean - perf_corrupt_patch) / cliff


# ── Model-running layer (stubs until hooks validated) ──────────────────────────────


def indirect_effect(model: Any, episode: Any, perturbation: Any, donor: Any) -> float:
    """Run the sufficiency intervention on the model, then call ``sufficiency_share``."""
    raise NotImplementedError("compose activation_patch runs once primitives are validated")


def natural_direct_effect(model: Any, episode: Any, perturbation: Any) -> float:
    """Effect NOT routed through the conditioning (the expert's own contribution)."""
    raise NotImplementedError
