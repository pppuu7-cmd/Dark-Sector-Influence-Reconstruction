#!/usr/bin/env bash
set -euo pipefail

# Usage:
#   dsir_checkpoint_git_sync_v0_1.sh push <checkpoint_dir> <branch> <label>
#   dsir_checkpoint_git_sync_v0_1.sh restore <checkpoint_dir> <branch>
#
# Checkpoints live on a dedicated branch, never on the scientific main history.
# The workflow must grant contents: write for push mode.

mode="${1:?mode push|restore}"
checkpoint_dir="${2:?checkpoint directory}"
branch="${3:?checkpoint branch}"
label="${4:-checkpoint}"
repo_root="$(git rev-parse --show-toplevel)"
remote_url="$(git remote get-url origin)"
work="${RUNNER_TEMP:-/tmp}/dsir-checkpoint-worktree-${GITHUB_RUN_ID:-local}-${RANDOM}"

cleanup() {
  git -C "$repo_root" worktree remove --force "$work" >/dev/null 2>&1 || true
  rm -rf "$work" >/dev/null 2>&1 || true
}
trap cleanup EXIT

if [[ "$mode" == "restore" ]]; then
  rm -rf "$checkpoint_dir"
  mkdir -p "$checkpoint_dir"
  if git ls-remote --exit-code --heads origin "$branch" >/dev/null 2>&1; then
    git fetch --no-tags origin "$branch:refs/remotes/origin/$branch"
    git worktree add --detach "$work" "refs/remotes/origin/$branch" >/dev/null
    if [[ -d "$work/checkpoint" ]]; then
      cp -a "$work/checkpoint/." "$checkpoint_dir/"
      echo "REMOTE_CHECKPOINT restored branch=$branch"
    else
      echo "REMOTE_CHECKPOINT branch=$branch exists but checkpoint directory absent; fail closed" >&2
      exit 4
    fi
  else
    echo "REMOTE_CHECKPOINT none found branch=$branch; starting fresh"
  fi
  exit 0
fi

if [[ "$mode" != "push" ]]; then
  echo "unknown mode: $mode" >&2
  exit 2
fi

if [[ ! -d "$checkpoint_dir" ]]; then
  echo "checkpoint directory missing: $checkpoint_dir" >&2
  exit 3
fi

git config user.name "dsir-checkpoint-bot"
git config user.email "dsir-checkpoint-bot@users.noreply.github.com"

# Build an orphan worktree when no remote checkpoint branch exists; otherwise
# update from the latest remote checkpoint. A completed band is immutable at
# the application layer because the Python validator binds its SHA and contract.
if git ls-remote --exit-code --heads origin "$branch" >/dev/null 2>&1; then
  git fetch --no-tags origin "$branch:refs/remotes/origin/$branch"
  git worktree add --detach "$work" "refs/remotes/origin/$branch" >/dev/null
else
  git worktree add --detach "$work" HEAD >/dev/null
  git -C "$work" checkout --orphan "$branch" >/dev/null
  git -C "$work" rm -rf . >/dev/null 2>&1 || true
fi

rm -rf "$work/checkpoint"
mkdir -p "$work/checkpoint"
cp -a "$checkpoint_dir/." "$work/checkpoint/"

git -C "$work" add checkpoint
if git -C "$work" diff --cached --quiet; then
  echo "REMOTE_CHECKPOINT unchanged branch=$branch"
  exit 0
fi

git -C "$work" commit -m "checkpoint: $label" >/dev/null

# Retry transient network failures; do not claim durability until push succeeds.
for attempt in 1 2 3 4 5; do
  if git -C "$work" push origin "HEAD:refs/heads/$branch"; then
    sha="$(git -C "$work" rev-parse HEAD)"
    echo "REMOTE_CHECKPOINT pushed branch=$branch commit=$sha label=$label"
    exit 0
  fi
  echo "REMOTE_CHECKPOINT push attempt $attempt failed; retrying" >&2
  sleep $((attempt * 5))
  # Rebase-like restart is deliberately not attempted: concurrent checkpoint
  # writers are forbidden by the experiment contract.
done

echo "REMOTE_CHECKPOINT durability failure after retries; stopping computation" >&2
exit 5
