"""★ Causal-mediation framing — indirect effect of the backbone representation.

Activation patching is the tool; causal mediation is the lens that turns it into an
attribution. The backbone→expert conditioning is the MEDIATOR between the perturbation
(treatment) and task success (outcome). Patching the clean mediator into the corrupted
run estimates the indirect effect routed through that representation.

Report BOTH directions (necessity AND sufficiency), not just one:
  * Sufficiency — does restoring the clean conditioning RECOVER performance?
  * Necessity   — does corrupting an otherwise-clean run via the conditioning BREAK it?

This module composes activation_patch runs into those effect estimates. It stays a
stub until the patch primitives are validated — never report a mediation number from
an unverified pipeline.
"""

from __future__ import annotations

from typing import Any


def indirect_effect(model: Any, episode: Any, perturbation: Any, donor: Any) -> float:
    """Effect routed through the backbone conditioning (sufficiency direction)."""
    raise NotImplementedError("compose activation_patch runs once primitives are validated")


def natural_direct_effect(model: Any, episode: Any, perturbation: Any) -> float:
    """Effect NOT routed through the conditioning (the expert's own contribution)."""
    raise NotImplementedError
