"""Perturbation axes, with the two classes kept STRICTLY separate.

meaning_changing → the action SHOULD change (sensitivity expected).
nuisance         → the action SHOULD NOT change (invariance expected).

The memorization signal is the asymmetry between them; mixing the classes would
break construct validity (risk #2). The registry enforces the separation.
"""
