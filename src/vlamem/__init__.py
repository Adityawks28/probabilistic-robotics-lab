"""vlamem — Localizing memorization in efficient VLA models.

Backbone (vision-language) vs. flow-matching action expert: when an efficient VLA
fails under a meaning-changing perturbation, which module is to blame? Answered via
causal-mediation (activation-patching) interventions, quantified as ``BackboneShare``.

This is research code. It never fabricates results: unbuilt pipelines raise
``NotImplementedError`` rather than returning a plausible-looking number. The human
owns every gate decision and verifies anything that feeds a conclusion (see CLAUDE.md).
"""

__version__ = "0.0.1"
