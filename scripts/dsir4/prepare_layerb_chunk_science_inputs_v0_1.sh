#!/usr/bin/env bash
set -euo pipefail
: "${GITHUB_REPOSITORY:?}" "${GH_TOKEN:?}" "${MANIFEST:?}" "${WM_S3_OVERRIDE:?}" "${PYTHON_BIN:?}"
mkdir -p external inputs/parent inputs/angular inputs/expim

mkdir -p external/camb
git -C external/camb init -q
git -C external/camb remote add origin https://github.com/cmbant/CAMB.git
git -C external/camb fetch -q --depth 1 origin fa3f097343fbbe427cc04b4f5f0041c22c6ec764
git -C external/camb checkout -q --detach FETCH_HEAD
test "$(git -C external/camb rev-parse HEAD)" = fa3f097343fbbe427cc04b4f5f0041c22c6ec764
"$PYTHON_BIN" -m pip install ./external/camb >/dev/null

mkdir -p external/des_nz
curl --fail --location --retry 3 -sS -o external/des_nz/source.fits 'https://desdr-server.ncsa.illinois.edu/despublic/y1a1_files/redshift_bins/y1_redshift_distributions_v1.fits'
curl --fail --location --retry 3 -sS -o external/des_nz/lens.fits 'https://desdr-server.ncsa.illinois.edu/despublic/y1a1_files/chains/2pt_NG_mcal_1110.fits'
echo 'b5d87138c35ae8bb4ecd02491972f544648398e606b3617039e6e54cb8ea943b  external/des_nz/source.fits' | sha256sum -c -
echo '114035179b5a8e41090751e9a6478536d185128581d37b5a510eff5722f417ca  external/des_nz/lens.fits' | sha256sum -c -

get_artifact () {
  local id="$1" digest="$2" dest="$3" zip="${3}.zip" actual expected
  mkdir -p "$dest"
  gh api -H 'Accept: application/vnd.github+json' "/repos/${GITHUB_REPOSITORY}/actions/artifacts/${id}/zip" > "$zip"
  actual="$(sha256sum "$zip" | awk '{print $1}')"; expected="${digest#sha256:}"
  test "$actual" = "$expected"
  unzip -q "$zip" -d "$dest"
}
get_artifact 10131794281 'sha256:ac959926639d3b46ecfe114e396ce03cb20a0763ef2781db454408d8ad0759df' inputs/parent
while IFS=$'\t' read -r slot id digest; do
  get_artifact "$id" "$digest" "inputs/angular/$slot"
done < <(jq -r '.angular[] | [.slot, (.artifact_id|tostring), .artifact_digest] | @tsv' "$MANIFEST")
id="$(jq -r '.artifact_id' "$WM_S3_OVERRIDE")"
mkdir -p inputs/angular/Wm_S3/transport_override
gh api -H 'Accept: application/vnd.github+json' "/repos/${GITHUB_REPOSITORY}/actions/artifacts/${id}/zip" > inputs/angular/Wm_S3/transport_override.zip
unzip -q inputs/angular/Wm_S3/transport_override.zip -d inputs/angular/Wm_S3/transport_override
expected="$(jq -r '.required_each_canonical_sha256' "$WM_S3_OVERRIDE")"; nbytes="$(jq -r '.required_each_nbytes' "$WM_S3_OVERRIDE")"
for f in inputs/angular/Wm_S3/transport_override/A/selected_te.bin inputs/angular/Wm_S3/transport_override/B/selected_te.bin; do
  test "$(stat -c%s "$f")" = "$nbytes"; test "$(sha256sum "$f" | awk '{print $1}')" = "$expected"
done
cmp -s inputs/angular/Wm_S3/transport_override/A/selected_te.bin inputs/angular/Wm_S3/transport_override/B/selected_te.bin
get_artifact 10130241439 'sha256:3325bab0faa821c5ca3b13b4cd64d3d58c323e56a6f3e44952be84bfbc477156' inputs/expim

mkdir -p external/exp073w_boss
base='https://fbeutler.github.io/hub'
curl --fail --location --retry 3 -sS -o external/exp073w_boss/W_NGC_z3.gz "$base/W_BOSS_DR12_NGC_z3_V6C_1_1_1_1_1_10_200_2000_averaged_v1.matrix.gz"
curl --fail --location --retry 3 -sS -o external/exp073w_boss/W_SGC_z3.gz "$base/W_BOSS_DR12_SGC_z3_V6C_1_1_1_1_1_10_200_2000_averaged_v1.matrix.gz"
curl --fail --location --retry 3 -sS -o external/exp073w_boss/M_NGC_z3.gz "$base/M_BOSS_DR12_NGC_z3_V6C_1_1_1_1_1_1200_2000.matrix.gz"
curl --fail --location --retry 3 -sS -o external/exp073w_boss/M_SGC_z3.gz "$base/M_BOSS_DR12_SGC_z3_V6C_1_1_1_1_1_1200_2000.matrix.gz"
for f in external/exp073w_boss/*.gz; do gzip -t "$f"; gzip -dc "$f" > "${f%.gz}"; done
echo 'a308dc562d1a7224cefcf91d32580877929e0daa33806517e0d2d53710236827  external/exp073w_boss/W_NGC_z3' | sha256sum -c -
echo '2a542a2d48f3e8c8299f58a885d5273238e4ade32c0f0de020d8b9f23afe7759  external/exp073w_boss/W_SGC_z3' | sha256sum -c -
echo '3ac30e68f79deee59963c5c52f7585e0cde495393963210a3922c1c62513a042  external/exp073w_boss/M_NGC_z3' | sha256sum -c -
echo '3ac30e68f79deee59963c5c52f7585e0cde495393963210a3922c1c62513a042  external/exp073w_boss/M_SGC_z3' | sha256sum -c -

echo LAYERB_CHUNK_SCIENCE_INPUTS_PREPARED_PLUS_0_PLUS_0
