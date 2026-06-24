"""(Phase 3) Targeted interventions — fix the located module, watch the problem shrink.

Only run AFTER the cheap baselines (augmentation, dropout) are recorded: a fix only
counts if it BEATS them (risk #7). The fix kind is chosen by where Phase 2 localized
the failure: consistency_loss (expert) or representation_align (backbone).
"""
