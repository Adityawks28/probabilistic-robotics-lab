#!/usr/bin/env bash
# scripts/run_train.sh — wrap lerobot-train to fine-tune SmolVLA on LIBERO (P0.1).
#
# Only needed if no usable pretrained LIBERO checkpoint is available.
#
# Usage:
#   bash scripts/run_train.sh [TASK]
set -euo pipefail

TASK="${1:-libero_10}"

echo "[train] fine-tuning SmolVLA on ${TASK}"
lerobot-train \
  --policy.type=smolvla \
  --policy.load_vlm_weights=true \
  --dataset.repo_id=HuggingFaceVLA/libero \
  --env.type=libero \
  --env.task="${TASK}"
