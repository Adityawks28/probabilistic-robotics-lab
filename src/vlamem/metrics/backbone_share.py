"""★ BackboneShare — the headline attribution ratio.

    BackboneShare = (Perf[corrupted+patch] − Perf[corrupted])
                    ────────────────────────────────────────
                    (Perf[clean]          − Perf[corrupted])

Interpretation:
  * ≈ 1.0 → patching the clean backbone conditioning RECOVERS clean performance:
            the failure was localized to the BACKBONE representation.
  * ≈ 0.0 → patching does nothing: the ACTION EXPERT had memorized; a correct
            conditioning can't save it.
  * ≈ 0.5 → entangled / noise — the GATE 0 failure case.

This is a PURE function — no model, no IO — so it is provably correct in isolation.
A hand-checked case is unit-tested in tests/test_metrics.py. It FAILS LOUD on a
degenerate denominator (no perturbation cliff): a ratio with no cliff is meaningless,
and silently returning a number there is exactly the confident-wrong failure mode the
project guards against.
"""

from __future__ import annotations

# If |Perf[clean] − Perf[corrupted]| is below this, there is no cliff to attribute.
MIN_CLIFF = 1e-9


def backbone_share(perf_clean: float, perf_corrupted: float, perf_patched: float) -> float:
    """Compute the BackboneShare mediation ratio.

    Args:
        perf_clean: Performance on the unperturbed (clean) input.
        perf_corrupted: Performance under the meaning-changing perturbation.
        perf_patched: Performance on the corrupted input with the clean backbone
            activation patched in.

    Returns:
        The fraction of the clean→corrupted performance gap recovered by patching.

    Raises:
        ValueError: if there is no measurable cliff (clean ≈ corrupted), making the
            ratio undefined.
    """
    cliff = perf_clean - perf_corrupted
    if abs(cliff) < MIN_CLIFF:
        raise ValueError(
            "BackboneShare undefined: no perturbation cliff "
            f"(perf_clean={perf_clean}, perf_corrupted={perf_corrupted}). "
            "Confirm the perturbation actually drops success before attributing."
        )
    return (perf_patched - perf_corrupted) / cliff
