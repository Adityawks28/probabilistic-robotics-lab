#!/usr/bin/env bash
# scripts/run_eval.sh — wrap lerobot-eval for the SmolVLA LIBERO baseline (P0.1).
#
# VERIFY (human): confirm the baseline lands near the published ~90%+ on at least one
# suite. If it doesn't, the harness is broken — fix that before anything else.
#
# Usage:
#   bash scripts/run_eval.sh [POLICY_PATH]
set -euo pipefail

POLICY_PATH="${1:-lerobot/smolvla_base}"
SUITES="libero_spatial,libero_object,libero_goal,libero_10"

echo "[eval] policy=${POLICY_PATH} suites=${SUITES}"
lerobot-eval \
  --policy.path="${POLICY_PATH}" \
  --env.type=libero \
  --env.task="${SUITES}"
