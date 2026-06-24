"""Evaluation harness + sweep runner.

``harness`` runs a single (model × perturbation × seed) cell and returns metrics;
``runner`` orchestrates the full grid (model × intervention × axis × seed). All logic
lives here so experiments/ entrypoints stay thin.
"""
