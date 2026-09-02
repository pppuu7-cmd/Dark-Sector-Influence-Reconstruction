#!/usr/bin/env bash
set -euo pipefail

# DSIR checkpoint Git sync v0.2
# Infrastructure-only transport/state durability repair.
# Scientific/checkpoint payload semantics are intentionally untouched.
#
# Usage:
#   dsir_checkpoint_git_sync_v0_2.sh push <checkpoint_dir> <branch> <label>
#   dsir_checkpoint_git_sync_v0_2.sh restore <checkpoint_dir> <branch> [expected_sha|ALLOW_ABSENT]
#
# Restore policy:
#   expected_sha  -> PRESENT is mandatory and must equal exactly expected_sha.
#   ALLOW_ABSENT  -> prospectively-new namespaces may start fresh if verified ABSENT.
#   omitted       -> PRESENT restores; verified ABSENT fails closed.

mode="${1:?mode push|restore}"
checkpoint_dir="${2:?checkpoint directory}"
branch="${3:?checkpoint branch}"
arg4="${4:-}"
repo_root="$(git rev-parse --show-toplevel)"
work="${RUNNER_TEMP:-/tmp}/dsir-checkpoint-v02-${GITHUB_RUN_ID:-local}-${RANDOM}-${RANDOM}"
query_attempts="${DSIR_CHECKPOINT_QUERY_ATTEMPTS:-5}"
push_attempts="${DSIR_CHECKPOINT_PUSH_ATTEMPTS:-5}"

case "$branch" in
  checkpoints/*) ;;
  *) echo "REMOTE_CHECKPOINT invalid branch namespace=$branch; fail closed" >&2; exit 2 ;;
esac

cleanup() {
  git -C "$repo_root" worktree remove --force "$work" >/dev/null 2>&1 || true
  rm -rf "$work" >/dev/null 2>&1 || true
}
trap cleanup EXIT

sleep_backoff() {
  local attempt="$1"
  sleep $((attempt * 2))
}

# Globals set on success:
#   REMOTE_STATE = PRESENT|ABSENT
#   REMOTE_SHA   = exact SHA for PRESENT, empty for ABSENT
# UNKNOWN_TRANSPORT_FAILURE never returns success.
query_remote_head() {
  local operation="$1"
  local out err rc attempt line sha ref expected_ref
  expected_ref="refs/heads/$branch"
  REMOTE_STATE=""
  REMOTE_SHA=""

  for ((attempt=1; attempt<=query_attempts; attempt++)); do
    err="$(mktemp "${RUNNER_TEMP:-/tmp}/dsir-query-err.XXXXXX")"
    set +e
    out="$(git ls-remote --heads origin "$expected_ref" 2>"$err")"
    rc=$?
    set -e
    if [[ $rc -ne 0 ]]; then
      echo "REMOTE_CHECKPOINT transport operation=$operation query_attempt=$attempt outcome=UNKNOWN_TRANSPORT_FAILURE" >&2
      rm -f "$err"
      if [[ $attempt -lt $query_attempts ]]; then sleep_backoff "$attempt"; fi
      continue
    fi
    rm -f "$err"

    if [[ -z "$out" ]]; then
      REMOTE_STATE="ABSENT"
      REMOTE_SHA=""
      echo "REMOTE_CHECKPOINT transport operation=$operation query_attempt=$attempt outcome=ABSENT"
      return 0
    fi

    if [[ "$(printf '%s\n' "$out" | wc -l | tr -d ' ')" != "1" ]]; then
      echo "REMOTE_CHECKPOINT malformed remote-head response branch=$branch; fail closed" >&2
      return 20
    fi
    line="$out"
    sha="${line%%[[:space:]]*}"
    ref="${line#*[[:space:]]}"
    if [[ ! "$sha" =~ ^[0-9a-fA-F]{40}$ || "$ref" != "$expected_ref" ]]; then
      echo "REMOTE_CHECKPOINT malformed remote-head binding branch=$branch; fail closed" >&2
      return 21
    fi
    REMOTE_STATE="PRESENT"
    REMOTE_SHA="${sha,,}"
    echo "REMOTE_CHECKPOINT transport operation=$operation query_attempt=$attempt outcome=PRESENT head=$REMOTE_SHA"
    return 0
  done

  echo "REMOTE_CHECKPOINT transport operation=$operation outcome=UNKNOWN_TRANSPORT_FAILURE exhausted=$query_attempts; fail closed" >&2
  return 22
}

fetch_exact_head() {
  local expected="$1" fetched
  git fetch --no-tags --no-write-fetch-head origin "refs/heads/$branch" >/dev/null
  fetched="$(git ls-remote --heads origin "refs/heads/$branch" | awk 'NR==1 {print tolower($1)}')"
  if [[ "$fetched" != "$expected" ]]; then
    echo "REMOTE_CHECKPOINT head changed during fetch expected=$expected observed=${fetched:-NONE}; fail closed" >&2
    return 23
  fi
  # Fetch the exact object after the ref binding above; no persistent checkpoint ref is created.
  git fetch --no-tags origin "$expected" >/dev/null 2>&1 || {
    # Some servers disallow want-by-SHA; branch fetch above still guarantees FETCH_HEAD/object availability.
    git cat-file -e "$expected^{commit}" || return 24
  }
  git cat-file -e "$expected^{commit}"
}

if [[ "$mode" == "restore" ]]; then
  expected="$arg4"
  query_remote_head restore || exit $?
  rm -rf "$checkpoint_dir"
  mkdir -p "$checkpoint_dir"

  if [[ "$REMOTE_STATE" == "ABSENT" ]]; then
    if [[ "$expected" == "ALLOW_ABSENT" ]]; then
      echo "REMOTE_CHECKPOINT verified_absent branch=$branch policy=ALLOW_ABSENT starting_fresh"
      exit 0
    fi
    echo "REMOTE_CHECKPOINT verified_absent branch=$branch restore_not_authorized; fail closed" >&2
    exit 25
  fi

  if [[ -n "$expected" && "$expected" != "ALLOW_ABSENT" ]]; then
    expected="${expected,,}"
    if [[ ! "$expected" =~ ^[0-9a-f]{40}$ || "$REMOTE_SHA" != "$expected" ]]; then
      echo "REMOTE_CHECKPOINT restore head mismatch expected=$expected observed=$REMOTE_SHA; fail closed" >&2
      exit 26
    fi
  fi

  fetch_exact_head "$REMOTE_SHA"
  git worktree add --detach "$work" "$REMOTE_SHA" >/dev/null
  if [[ ! -d "$work/checkpoint" ]]; then
    echo "REMOTE_CHECKPOINT branch=$branch head=$REMOTE_SHA checkpoint directory absent; fail closed" >&2
    exit 27
  fi
  cp -a "$work/checkpoint/." "$checkpoint_dir/"
  echo "REMOTE_CHECKPOINT restored branch=$branch head=$REMOTE_SHA exact_pinned=true"
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

query_remote_head push_preflight || exit $?
old_state="$REMOTE_STATE"
old_sha="$REMOTE_SHA"

if [[ "$old_state" == "PRESENT" ]]; then
  fetch_exact_head "$old_sha"
  git worktree add --detach "$work" "$old_sha" >/dev/null
else
  # Detached construction only. No local ref named checkpoints/... is created.
  git worktree add --detach "$work" HEAD >/dev/null
fi

# Make the candidate tree contain only checkpoint/, as in the frozen v0.1 checkpoint branch history.
find "$work" -mindepth 1 -maxdepth 1 ! -name .git -exec rm -rf {} +
mkdir -p "$work/checkpoint"
cp -a "$checkpoint_dir/." "$work/checkpoint/"
git -C "$work" add -A

new_tree="$(git -C "$work" write-tree)"
if [[ "$old_state" == "PRESENT" ]]; then
  old_tree="$(git -C "$work" show -s --format=%T "$old_sha")"
  if [[ "$new_tree" == "$old_tree" ]]; then
    echo "REMOTE_CHECKPOINT unchanged branch=$branch head=$old_sha post_push_verification=not_needed"
    exit 0
  fi
  new_sha="$(printf '%s\n' "checkpoint: $arg4" | git -C "$work" commit-tree "$new_tree" -p "$old_sha")"
  lease="refs/heads/$branch:$old_sha"
else
  new_sha="$(printf '%s\n' "checkpoint: $arg4" | git -C "$work" commit-tree "$new_tree")"
  lease="refs/heads/$branch:"
fi
new_sha="${new_sha,,}"

# Push retries are safe only while the remote remains exactly in the bound old state.
for ((attempt=1; attempt<=push_attempts; attempt++)); do
  echo "REMOTE_CHECKPOINT transport operation=push push_attempt=$attempt expected_state=$old_state"
  set +e
  git push --force-with-lease="$lease" origin "$new_sha:refs/heads/$branch"
  rc=$?
  set -e

  # Independently query after every push attempt. This handles both successful pushes
  # and response-loss cases without trusting the push exit code alone.
  if query_remote_head push_postcheck; then
    if [[ "$REMOTE_STATE" == "PRESENT" && "$REMOTE_SHA" == "$new_sha" ]]; then
      echo "REMOTE_CHECKPOINT durable branch=$branch commit=$new_sha label=$arg4 post_push_exact=true push_rc=$rc"
      exit 0
    fi

    if [[ "$old_state" == "PRESENT" ]]; then
      if [[ "$REMOTE_STATE" != "PRESENT" || "$REMOTE_SHA" != "$old_sha" ]]; then
        echo "REMOTE_CHECKPOINT stale_lease_or_race expected_old=$old_sha observed_state=$REMOTE_STATE observed_head=${REMOTE_SHA:-NONE}; fail closed" >&2
        exit 28
      fi
    else
      if [[ "$REMOTE_STATE" != "ABSENT" ]]; then
        echo "REMOTE_CHECKPOINT stale_lease_or_race expected_old=ABSENT observed_state=$REMOTE_STATE observed_head=${REMOTE_SHA:-NONE}; fail closed" >&2
        exit 28
      fi
    fi
  else
    echo "REMOTE_CHECKPOINT post-push remote state unknown on attempt=$attempt; fail closed for this attempt" >&2
  fi

  if [[ $attempt -lt $push_attempts ]]; then sleep_backoff "$attempt"; fi
done

echo "REMOTE_CHECKPOINT durability failure after push retries=$push_attempts; stopping computation" >&2
exit 29
