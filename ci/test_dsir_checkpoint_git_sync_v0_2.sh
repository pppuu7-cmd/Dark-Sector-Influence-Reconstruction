#!/usr/bin/env bash
set -euo pipefail

helper="$(cd "$(dirname "$0")" && pwd)/dsir_checkpoint_git_sync_v0_2.sh"
root="$(mktemp -d)"
trap 'rm -rf "$root"' EXIT
export DSIR_CHECKPOINT_QUERY_ATTEMPTS=1
export DSIR_CHECKPOINT_PUSH_ATTEMPTS=1
export RUNNER_TEMP="$root/tmp"
mkdir -p "$RUNNER_TEMP"

pass() { echo "TEST_PASS $1"; }
fail() { echo "TEST_FAIL $1" >&2; exit 90; }
expect_rc() {
  local want="$1"; shift
  set +e
  "$@"
  local got=$?
  set -e
  [[ "$got" == "$want" ]] || fail "expected_rc_${want}_got_${got}: $*"
}

new_fixture() {
  local name="$1"
  local remote="$root/$name-remote.git"
  local repo="$root/$name-repo"
  git init --bare "$remote" >/dev/null
  git init "$repo" >/dev/null
  git -C "$repo" config user.name test
  git -C "$repo" config user.email test@example.invalid
  git -C "$repo" remote add origin "$remote"
  printf 'seed\n' >"$repo/seed.txt"
  git -C "$repo" add seed.txt
  git -C "$repo" commit -m seed >/dev/null
  printf '%s\n%s\n' "$remote" "$repo"
}

# T1/T2/T4: verified ABSENT -> detached parentless checkpoint commit -> exact post-push verification.
mapfile -t fx < <(new_fixture absent)
remote="${fx[0]}"; repo="${fx[1]}"
branch="checkpoints/synthetic-v02"
mkdir -p "$repo/cp"
printf 'alpha\n' >"$repo/cp/payload.bin"
orig_sha="$(sha256sum "$repo/cp/payload.bin" | awk '{print $1}')"
(
  cd "$repo"
  out="$("$helper" push cp "$branch" first)"
  printf '%s\n' "$out"
  grep -q 'outcome=ABSENT' <<<"$out"
  grep -q 'post_push_exact=true' <<<"$out"
)
head1="$(git --git-dir="$remote" rev-parse "refs/heads/$branch")"
[[ "$(git --git-dir="$remote" rev-list --parents -n1 "$head1" | wc -w | tr -d ' ')" == "1" ]] || fail parentless_initial_commit
if git -C "$repo" show-ref --verify --quiet "refs/heads/$branch"; then fail persistent_local_checkpoint_ref; fi
pass absent_detached_postverify

# T3/T4: PRESENT advances exactly from discovered parent and verifies remote head.
printf 'beta\n' >"$repo/cp/payload.bin"
(
  cd "$repo"
  out="$("$helper" push cp "$branch" second)"
  printf '%s\n' "$out"
  grep -q 'outcome=PRESENT' <<<"$out"
  grep -q 'post_push_exact=true' <<<"$out"
)
head2="$(git --git-dir="$remote" rev-parse "refs/heads/$branch")"
[[ "$head2" != "$head1" ]] || fail present_did_not_advance
[[ "$(git --git-dir="$remote" rev-parse "$head2^")" == "$head1" ]] || fail wrong_parent_binding
if git -C "$repo" show-ref --verify --quiet "refs/heads/$branch"; then fail persistent_local_checkpoint_ref_after_present; fi
pass present_compare_and_push

# T5: exact pinned restore, payload bytes unchanged.
restore="$repo/restored"
(
  cd "$repo"
  "$helper" restore "$restore" "$branch" "$head2"
)
restored_sha="$(sha256sum "$restore/payload.bin" | awk '{print $1}')"
current_sha="$(sha256sum "$repo/cp/payload.bin" | awk '{print $1}')"
[[ "$restored_sha" == "$current_sha" ]] || fail restore_payload_sha
pass exact_pinned_restore_payload_unchanged

# Pinned restore must reject any other head.
expect_rc 26 bash -c 'cd "$1" && "$2" restore "$3" "$4" "$5"' _ "$repo" "$helper" "$repo/badrestore" "$branch" "$head1"
pass restore_head_mismatch_fail_closed

# T6: UNKNOWN query transport failure must not masquerade as ABSENT.
mapfile -t fxq < <(new_fixture queryfail)
qrepo="${fxq[1]}"
git -C "$qrepo" remote set-url origin "$root/does-not-exist.git"
expect_rc 22 bash -c 'cd "$1" && "$2" restore "$3" "$4" ALLOW_ABSENT' _ "$qrepo" "$helper" "$qrepo/restore" checkpoints/query-fail
pass query_transport_unknown_fail_closed

# T7: push transport/server rejection is retried/bounded and never called durable.
mapfile -t fxp < <(new_fixture pushfail)
premote="${fxp[0]}"; prepo="${fxp[1]}"
cat >"$premote/hooks/pre-receive" <<'HOOK'
#!/usr/bin/env bash
exit 1
HOOK
chmod +x "$premote/hooks/pre-receive"
mkdir -p "$prepo/cp"; printf 'x\n' >"$prepo/cp/payload"
expect_rc 29 bash -c 'cd "$1" && "$2" push cp checkpoints/push-fail reject' _ "$prepo" "$helper"
if git --git-dir="$premote" show-ref --verify --quiet refs/heads/checkpoints/push-fail; then fail rejected_push_became_durable; fi
pass push_failure_not_durable

# T8: deterministic stale lease/race. A git shim advances the remote immediately before helper push.
mapfile -t fxr < <(new_fixture race)
rremote="${fxr[0]}"; rrepo="${fxr[1]}"
rbranch="checkpoints/race"
mkdir -p "$rrepo/cp"; printf 'v1\n' >"$rrepo/cp/payload"
(cd "$rrepo" && "$helper" push cp "$rbranch" base >/dev/null)
old="$(git --git-dir="$rremote" rev-parse "refs/heads/$rbranch")"
tree="$(git --git-dir="$rremote" show -s --format=%T "$old")"
export GIT_AUTHOR_NAME=racer GIT_AUTHOR_EMAIL=racer@example.invalid GIT_COMMITTER_NAME=racer GIT_COMMITTER_EMAIL=racer@example.invalid
competitor="$(printf 'competing checkpoint\n' | git --git-dir="$rremote" commit-tree "$tree" -p "$old")"
unset GIT_AUTHOR_NAME GIT_AUTHOR_EMAIL GIT_COMMITTER_NAME GIT_COMMITTER_EMAIL
shimdir="$root/shim"; mkdir -p "$shimdir"
real_git="$(command -v git)"
cat >"$shimdir/git" <<'SHIM'
#!/usr/bin/env bash
set -euo pipefail
for a in "$@"; do
  if [[ "$a" == "push" && ! -e "$RACE_MARKER" ]]; then
    "$REAL_GIT" --git-dir="$RACE_REMOTE" update-ref "refs/heads/$RACE_BRANCH" "$RACE_SHA"
    : >"$RACE_MARKER"
    break
  fi
done
exec "$REAL_GIT" "$@"
SHIM
chmod +x "$shimdir/git"
printf 'v2\n' >"$rrepo/cp/payload"
export REAL_GIT="$real_git" RACE_REMOTE="$rremote" RACE_BRANCH="$rbranch" RACE_SHA="$competitor" RACE_MARKER="$root/race-fired"
old_path="$PATH"; export PATH="$shimdir:$PATH"
expect_rc 28 bash -c 'cd "$1" && "$2" push cp "$3" candidate' _ "$rrepo" "$helper" "$rbranch"
export PATH="$old_path"
[[ "$(git --git-dir="$rremote" rev-parse "refs/heads/$rbranch")" == "$competitor" ]] || fail race_overwritten
pass stale_lease_race_fail_closed

echo "CHECKPOINT_SYNC_V0_2_SYNTHETIC_NONCLASSIFYING_PASS"
echo "readiness_delta=+0/+0"
