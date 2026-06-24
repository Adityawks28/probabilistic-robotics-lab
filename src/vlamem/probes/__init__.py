"""Converging localization probes (M1, M2, M4) that triangulate the patching headline.

No single method is airtight, so four should agree (CLAUDE.md Phase 2):
  M1 representation_sensitivity — does the backbone feature move under a meaning edit?
  M2 oracle_conditioning        — feed the expert a correct z under a perturbed world.
  M3 activation patching        — the headline (lives in patching/).
  M4 cross_swap                 — clean backbone + perturbed-exposed expert, and vice versa.
Agreement = trust; disagreement is itself a clue.
"""
