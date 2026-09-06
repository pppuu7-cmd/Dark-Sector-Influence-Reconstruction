#!/usr/bin/env bash
set -euo pipefail
: "${GITHUB_WORKSPACE:?}" "${PATCH_BLOB:?}"
BASE="$GITHUB_WORKSPACE/ci/exp073ey_home_filebacked_fullres_v0_1.sh"
READ_PATCH="$GITHUB_WORKSPACE/patches/namaster-v2.7-dsir-filebacked-mcm-read-v0.2.patch"
EXPECTED_BASE_BLOB='e48453e71970eecabdc6dec33facb26b77bb9e4e'
EXPECTED_READ_PATCH_BLOB='d534b698f9131688d263eedcef27260386c58641'

test "$(git rev-parse HEAD:ci/exp073ey_home_filebacked_fullres_v0_1.sh)" = "$EXPECTED_BASE_BLOB"
test "$(git rev-parse HEAD:patches/namaster-v2.7-dsir-filebacked-mcm-read-v0.2.patch)" = "$EXPECTED_READ_PATCH_BLOB"
test "$PATCH_BLOB" = "$EXPECTED_READ_PATCH_BLOB"
grep -F 'diff --git a/src/nmt_io.c b/src/nmt_io.c' "$READ_PATCH" >/dev/null
grep -F 'dsir_nmt_alloc_unbinned(w,(int)n_el,0);' "$READ_PATCH" >/dev/null

# The frozen v0.1 envelope is retained verbatim except for its storage-patch path.
# Git blob identity above makes this transformation prospective and fail-closed.
TMP="${RUNNER_TEMP:-/tmp}/exp073ey_home_filebacked_fullres_v0_2_effective.sh"
sed 's#patches/namaster-v2.7-dsir-filebacked-mcm-v0\.1\.patch#patches/namaster-v2.7-dsir-filebacked-mcm-read-v0.2.patch#g' "$BASE" > "$TMP"
chmod +x "$TMP"
# v0.1 uses SHA256 only as a build-cache marker/check after already verifying PATCH_BLOB.
# Derive it from the exact frozen Git-blob-qualified file; this does not select science logic.
export PATCH_SHA256="$(sha256sum "$READ_PATCH" | awk '{print $1}')"
exec bash "$TMP"
