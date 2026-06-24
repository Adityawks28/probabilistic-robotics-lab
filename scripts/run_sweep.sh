#!/usr/bin/env bash
# scripts/run_sweep.sh — launch an experiment-grid sweep via a phase entrypoint.
#
# Validate the underlying pipeline interactively FIRST; only queue overnight once the
# §4 sanity checks pass (CLAUDE.md: validate before automate).
#
# Usage:
#   bash scripts/run_sweep.sh experiments/phase2_localization.py configs/experiments/phase2_localization.yaml
set -euo pipefail

ENTRYPOINT="${1:?usage: run_sweep.sh <entrypoint.py> <config.yaml>}"
CONFIG="${2:?usage: run_sweep.sh <entrypoint.py> <config.yaml>}"

echo "[sweep] ${ENTRYPOINT} --config ${CONFIG}"
python "${ENTRYPOINT}" --config "${CONFIG}"
