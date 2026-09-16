# DSIR-I v0.2 reproducible build baseline

Date: 2026-08-27

This record freezes the first complete end-to-end paper build in which the deterministic manuscript audit and all six main publication figures completed successfully from repository evidence.

## Successful build

- paper branch: `paper/dsir-i-observable-response-geometry`
- source commit: `3ec77ea804db6198e072a5da5461b4db59e558ac`
- GitHub Actions workflow: `DSIR-I paper build v0.2`
- workflow run: `33032395387`
- job: `98387650580`
- conclusion: `SUCCESS`

Every substantive build step passed:

1. deterministic manuscript audit and v0.2 assembly — PASS;
2. Figure 1 operator architecture — PASS;
3. Figure 2 additive-core failure — PASS;
4. Figure 3 finite-amplitude hierarchy — PASS;
5. Figure 4 channel-conditional degeneracy — PASS;
6. Figure 5 curvature and localization — PASS;
7. Figure 6 failure-resistant science — PASS;
8. output SHA256 manifest generation — PASS;
9. build artifact upload — PASS.

## Immutable build artifact

- artifact id: `9630730946`
- artifact name: `dsir1-paper-v0-2-3ec77ea804db6198e072a5da5461b4db59e558ac`
- artifact digest: `sha256:7c98b5933346e2b3ee1feaab6f7f9651c7b03a1fb03413ceb4631a09b1fe42c7`
- artifact size: `1260407` bytes
- GitHub retention expiry reported for this artifact: `2026-11-25T02:09:23Z`

The artifact contains the generated `manuscript_v0_2.md`, the claims/provenance/author/figure metadata, publication-ready figure captions, Figures 1–6 in PDF/PNG/SVG, per-figure provenance JSON files, `SHA256SUMS.txt`, and the build-environment record.

## Scientific meaning of this baseline

This baseline establishes **reproducible paper assembly**, not closure of an open physics gate. In particular:

- `G7=OPEN`;
- `G8=OPEN`;
- `G9=OPEN`;
- theory-response angles remain distinct from survey-level detection significance;
- the F27 prospective common-centroid relation remains falsified;
- original C3 Exp070A and C5 Exp069B failures remain permanent provenance even though later separately frozen provider contracts pass.

Future manuscript versions may supersede this build, but they must not erase this historical baseline. Any change to scientific inputs, masks, thresholds, normalizations, orientation conventions, or claim boundaries must be explicitly versioned and re-audited.