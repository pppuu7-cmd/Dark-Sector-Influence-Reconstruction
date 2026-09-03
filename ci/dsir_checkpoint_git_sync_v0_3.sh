#!/usr/bin/env bash
set -euo pipefail

# DSIR checkpoint Git sync v0.3
# Transport-hardened successor to v0.2 after Exp073CO HTTPS/GnuTLS failures.
# Scientific/checkpoint payload semantics are unchanged.
#
# Usage:
#   dsir_checkpoint_git_sync_v0_3.sh push <checkpoint_dir> <branch> <label>
#   dsir_checkpoint_git_sync_v0_3.sh restore <checkpoint_dir> <branch> [expected_sha|ALLOW_ABSENT]

mode="${1:?mode push|restore}"
checkpoint_dir="${2:?checkpoint directory}"
branch="${3:?checkpoint branch}"
arg4="${4:-}"
repo_root="$(git rev-parse --show-toplevel)"
work="${RUNNER_TEMP:-/tmp}/dsir-checkpoint-v03-${GITHUB_RUN_ID:-local}-${RANDOM}-${RANDOM}"
query_attempts="${DSIR_CHECKPOINT_QUERY_ATTEMPTS:-7}"
fetch_attempts="${DSIR_CHECKPOINT_FETCH_ATTEMPTS:-7}"
push_attempts="${DSIR_CHECKPOINT_PUSH_ATTEMPTS:-7}"
git_timeout_seconds="${DSIR_CHECKPOINT_GIT_TIMEOUT_SECONDS:-120}"
export GIT_TERMINAL_PROMPT=0

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
  local delay=$((attempt * 3))
  if (( delay > 30 )); then delay=30; fi
  sleep "$delay"
}

git_net() {
  timeout --signal=TERM "$git_timeout_seconds" git -c http.version=HTTP/1.1 "$@"
}

# Globals on success: REMOTE_STATE=PRESENT|ABSENT, REMOTE_SHA exact for PRESENT.
query_remote_head() {
  local operation="$1"
  local out err rc attempt line sha ref expected_ref
  expected_ref="refs/heads/$branch"
  REMOTE_STATE=""; REMOTE_SHA=""
  for ((attempt=1; attempt<=query_attempts; attempt++)); do
    err="$(mktemp "${RUNNER_TEMP:-/tmp}/dsir-query-v03-err.XXXXXX")"
    set +e
    out="$(git_net ls-remote --heads origin "$expected_ref" 2>"$err")"
    rc=$?
    set -e
    if [[ $rc -ne 0 ]]; then
      echo "REMOTE_CHECKPOINT transport operation=$operation query_attempt=$attempt outcome=UNKNOWN_TRANSPORT_FAILURE rc=$rc" >&2
      rm -f "$err"
      if [[ $attempt -lt $query_attempts ]]; then sleep_backoff "$attempt"; fi
      continue
    fi
    rm -f "$err"
    if [[ -z "$out" ]]; then
      REMOTE_STATE="ABSENT"; REMOTE_SHA=""
      echo "REMOTE_CHECKPOINT transport operation=$operation query_attempt=$attempt outcome=ABSENT"
      return 0
    fi
    if [[ "$(printf '%s\n' "$out" | wc -l | tr -d ' ')" != "1" ]]; then
      echo "REMOTE_CHECKPOINT malformed remote-head response branch=$branch; fail closed" >&2
      return 20
    fi
    line="$out"; sha="${line%%[[:space:]]*}"; ref="${line#*[[:space:]]}"
    if [[ ! "$sha" =~ ^[0-9a-fA-F]{40}$ || "$ref" != "$expected_ref" ]]; then
      echo "REMOTE_CHECKPOINT malformed remote-head binding branch=$branch; fail closed" >&2
      return 21
    fi
    REMOTE_STATE="PRESENT"; REMOTE_SHA="${sha,,}"
    echo "REMOTE_CHECKPOINT transport operation=$operation query_attempt=$attempt outcome=PRESENT head=$REMOTE_SHA"
    return 0
  done
  echo "REMOTE_CHECKPOINT transport operation=$operation outcome=UNKNOWN_TRANSPORT_FAILURE exhausted=$query_attempts; fail closed" >&2
  return 22
}

fetch_exact_head() {
  local expected="${1,,}" attempt rc fetched
  for ((attempt=1; attempt<=fetch_attempts; attempt++)); do
    set +e
    git_net fetch --no-tags origin "refs/heads/$branch" >/dev/null 2>&1
    rc=$?
    set -e
    if [[ $rc -ne 0 ]]; then
      echo "REMOTE_CHECKPOINT transport operation=fetch fetch_attempt=$attempt outcome=UNKNOWN_TRANSPORT_FAILURE rc=$rc" >&2
      if [[ $attempt -lt $fetch_attempts ]]; then sleep_backoff "$attempt"; fi
      continue
    fi
    fetched="$(git rev-parse 'FETCH_HEAD^{commit}' 2>/dev/null | tr '[:upper:]' '[:lower:]')"
    if [[ ! "$fetched" =~ ^[0-9a-f]{40}$ ]]; then
      echo "REMOTE_CHECKPOINT fetched commit malformed observed=${fetched:-NONE}; fail closed" >&2
      return 23
    fi
    if [[ "$fetched" != "$expected" ]]; then
      echo "REMOTE_CHECKPOINT head changed during fetch expected=$expected fetched=$fetched; fail closed" >&2
      return 24
    fi
    if ! query_remote_head fetch_postcheck; then
      echo "REMOTE_CHECKPOINT fetch postcheck transport unknown attempt=$attempt" >&2
      if [[ $attempt -lt $fetch_attempts ]]; then sleep_backoff "$attempt"; continue; fi
      return 25
    fi
    if [[ "$REMOTE_STATE" != "PRESENT" || "$REMOTE_SHA" != "$expected" ]]; then
      echo "REMOTE_CHECKPOINT head changed after fetch expected=$expected observed_state=$REMOTE_STATE observed_head=${REMOTE_SHA:-NONE}; fail closed" >&2
      return 26
    fi
    git cat-file -e "$expected^{commit}" || { echo "REMOTE_CHECKPOINT fetched object absent expected=$expected; fail closed" >&2; return 27; }
    echo "REMOTE_CHECKPOINT transport operation=fetch fetch_attempt=$attempt outcome=EXACT head=$expected"
    return 0
  done
  echo "REMOTE_CHECKPOINT transport operation=fetch outcome=UNKNOWN_TRANSPORT_FAILURE exhausted=$fetch_attempts; fail closed" >&2
  return 28
}

if [[ "$mode" == "restore" ]]; then
  expected="$arg4"
  query_remote_head restore || exit $?
  rm -rf "$checkpoint_dir"; mkdir -p "$checkpoint_dir"
  if [[ "$REMOTE_STATE" == "ABSENT" ]]; then
    if [[ "$expected" == "ALLOW_ABSENT" ]]; then
      echo "REMOTE_CHECKPOINT verified_absent branch=$branch policy=ALLOW_ABSENT starting_fresh"
      exit 0
    fi
    echo "REMOTE_CHECKPOINT verified_absent branch=$branch restore_not_authorized; fail closed" >&2
    exit 29
  fi
  if [[ -n "$expected" && "$expected" != "ALLOW_ABSENT" ]]; then
    expected="${expected,,}"
    if [[ ! "$expected" =~ ^[0-9a-f]{40}$ || "$REMOTE_SHA" != "$expected" ]]; then
      echo "REMOTE_CHECKPOINT restore head mismatch expected=$expected observed=$REMOTE_SHA; fail closed" >&2
      exit 30
    fi
  fi
  fetch_exact_head "$REMOTE_SHA"
  git worktree add --detach "$work" "$REMOTE_SHA" >/dev/null
  if [[ ! -d "$work/checkpoint" ]]; then
    echo "REMOTE_CHECKPOINT branch=$branch head=$REMOTE_SHA checkpoint directory absent; fail closed" >&2
    exit 31
  fi
  cp -a "$work/checkpoint/." "$checkpoint_dir/"
  echo "REMOTE_CHECKPOINT restored branch=$branch head=$REMOTE_SHA exact_pinned=true"
  exit 0
fi

if [[ "$mode" != "push" ]]; then echo "unknown mode: $mode" >&2; exit 2; fi
if [[ ! -d "$checkpoint_dir" ]]; then echo "checkpoint directory missing: $checkpoint_dir" >&2; exit 3; fi

git config user.name "dsir-checkpoint-bot"
git config user.email "dsir-checkpoint-bot@users.noreply.github.com"
query_remote_head push_preflight || exit $?
old_state="$REMOTE_STATE"; old_sha="$REMOTE_SHA"
if [[ "$old_state" == "PRESENT" ]]; then
  fetch_exact_head "$old_sha"
  git worktree add --detach "$work" "$old_sha" >/dev/null
else
  git worktree add --detach "$work" HEAD >/dev/null
fi

find "$work" -mindepth 1 -maxdepth 1 ! -name .git -exec rm -rf {} +
mkdir -p "$work/checkpoint"; cp -a "$checkpoint_dir/." "$work/checkpoint/"
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

for ((attempt=1; attempt<=push_attempts; attempt++)); do
  echo "REMOTE_CHECKPOINT transport operation=push push_attempt=$attempt expected_state=$old_state"
  set +e
  git_net push --force-with-lease="$lease" origin "$new_sha:refs/heads/$branch"
  rc=$?
  set -e
  if query_remote_head push_postcheck; then
    if [[ "$REMOTE_STATE" == "PRESENT" && "$REMOTE_SHA" == "$new_sha" ]]; then
      echo "REMOTE_CHECKPOINT durable branch=$branch commit=$new_sha label=$arg4 post_push_exact=true push_rc=$rc"
      exit 0
    fi
    if [[ "$old_state" == "PRESENT" ]]; then
      if [[ "$REMOTE_STATE" != "PRESENT" || "$REMOTE_SHA" != "$old_sha" ]]; then
        echo "REMOTE_CHECKPOINT stale_lease_or_race expected_old=$old_sha observed_state=$REMOTE_STATE observed_head=${REMOTE_SHA:-NONE}; fail closed" >&2
        exit 32
      fi
    else
      if [[ "$REMOTE_STATE" != "ABSENT" ]]; then
        echo "REMOTE_CHECKPOINT stale_lease_or_race expected_old=ABSENT observed_state=$REMOTE_STATE observed_head=${REMOTE_SHA:-NONE}; fail closed" >&2
        exit 32
      fi
    fi
  else
    echo "REMOTE_CHECKPOINT post-push remote state unknown on attempt=$attempt; retry only against original bound state" >&2
  fi
  if [[ $attempt -lt $push_attempts ]]; then sleep_backoff "$attempt"; fi
done

echo "REMOTE_CHECKPOINT durability failure after push retries=$push_attempts; stopping computation" >&2
exit 33
