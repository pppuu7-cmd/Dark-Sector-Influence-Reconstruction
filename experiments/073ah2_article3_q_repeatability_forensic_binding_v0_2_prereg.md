# Exp073AH2 — Article 3 Q exact-repeatability forensic binding v0.2

**Frozen:** 2026-08-30 after Exp073AH v0.1 failed due a forensic transcription/implementation error and before any hosted Exp073AH2 output.

## Historical preservation

Exp073AH v0.1 run `33308601529`, job `99249462973` is preserved as:

`FORENSIC_IMPLEMENTATION_TRANSCRIPTION_FAILURE_NO_SCIENCE_RECLASSIFICATION`.

Its artifact binding steps succeeded, but its forensic script failed before producing an authority because a manually transcribed expected B canonical SHA was wrong. No scientific/repeatability classification changed and no production was released.

## Binding upstream classification

Q run `33301058260` already failed its frozen exact comparator after both replicas completed. Q therefore remains:

`SCIENTIFIC_REPEATABILITY_FAIL`

for the current operator-repeatability route. This is a reproducibility criterion failure, not a dark-sector model-physics failure.

Exp073AF consequently keeps `P PASS + Q SCIENTIFIC_REPEATABILITY_FAIL -> BLOCK_PRODUCTION`.

Exp073AH2 is forbidden to rescue or soften Q.

## Immutable artifacts

Q-A: job `99229177604`, artifact `9730452251`, digest `sha256:6fab306a14d76b6819820454eb2d56035c2ce74b126d2ac1a70eb94cbb5dac27`.

Q-B: job `99229177540`, artifact `9730346824`, digest `sha256:a969aa3d04b2d2278d16e84e14ec2fbc046fc79c5bd1c63615e01c783592ce95`.

Run/head: `33301058260` / `730ae4951ab8cd8e1dd2c392e991c3120345678a`.

Primary P canonical diagnostic reference already established independently:
`6ec29f6dbbcf0c29d7af9d6eb98d271bcd06e00d28cebe658b5e266f7ef18d0f`.

## v0.2 design rule

Unlike v0.1, AH2 does **not** preregister manually copied numerical difference metrics as pass criteria.

It prospectively freezes only structural/self-consistency criteria:

1. GitHub artifact IDs/names/digests/run/head must match exactly.
2. Each artifact must contain exactly one `metadata.json` and one `wm0_te_window.npz` with key `wm0_te_window`.
3. Each array must be finite `[39,12288]` and canonical little-endian float64.
4. Computed canonical array SHA must exactly equal that artifact metadata's `workspace.te_window_authority.sha256`.
5. Metadata must agree outside the explicitly allowed output/replica-identity paths:
   - `replica`;
   - `saved_npz_sha256`;
   - `workspace.absolute_response_norms[*]`;
   - `workspace.te_window_authority.sha256`.
6. Any difference outside those paths -> `INPUT_OR_CONTRACT_PROVENANCE_DRIFT`.
7. If arrays differ exactly and all metadata differences remain only in those paths -> `WORKSPACE_OUTPUT_ONLY_NUMERICAL_DIVERGENCE`.
8. If arrays are unexpectedly exactly equal -> AH2 fails closed because that contradicts the already-hosted frozen Q comparator outcome and requires a separate provenance investigation.

The numerical mismatch count/fraction, absolute-difference metrics, per-band diagnostics, exact hashes and comparison to P are outputs, not acceptance thresholds.

## Interpretation firewall

A hosted `WORKSPACE_OUTPUT_ONLY_NUMERICAL_DIVERGENCE` establishes localization only. It may support wording “consistent with low-level floating-point/runtime nondeterminism,” but does not prove hardware, threading, BLAS, compiler, or NaMaster as the root cause.

No tolerance/rounding/ULP rule is allowed to convert Q to PASS.

## Anti-leakage/accounting

No workspace recomputation. No radial kernel, support, retained rows, fiducial P, covariance, whitening, nuisance geometry/SVD/rank, quotient/relation/null, or G8 access. No Exp073AA launch.

Article-3 scientific readiness stays 52%; increment 0; G7/G8/G9 OPEN.

## Required hosted token

`PASS_EXP073AH2_Q_REPEATABILITY_FORENSIC_BINDING_V0_2`

This is forensic/non-classifying authority only.
