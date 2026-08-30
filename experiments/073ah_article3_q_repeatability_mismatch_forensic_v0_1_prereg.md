# Exp073AH — Article 3 Q exact-repeatability mismatch forensic localization v0.1

**Frozen:** 2026-08-30 after Exp073X2 Chain Q run `33301058260` completed its exact comparator with a mismatch, and before any forensic hosted output from Exp073AH. This gate is diagnostic only and is forbidden to rescue, soften, or supersede the frozen exact-repeatability failure.

## Frozen upstream facts

### Primary P authority already established independently

Canonical P `Wm_S0` SHA256:

`6ec29f6dbbcf0c29d7af9d6eb98d271bcd06e00d28cebe658b5e266f7ef18d0f`

P remains a valid hosted non-classifying within-chain repeatability authority. Its existence does not override a later Q mismatch under the frozen cross-chain governance.

### Q immutable hosted artifacts

Run `33301058260`, head `730ae4951ab8cd8e1dd2c392e991c3120345678a`.

Replica A:
- job `99229177604`;
- artifact `9730452251`;
- artifact name `exp073x2-replica-a-730ae4951ab8cd8e1dd2c392e991c3120345678a`;
- artifact digest `sha256:6fab306a14d76b6819820454eb2d56035c2ce74b126d2ac1a70eb94cbb5dac27`.

Replica B:
- job `99229177540`;
- artifact `9730346824`;
- artifact name `exp073x2-replica-b-730ae4951ab8cd8e1dd2c392e991c3120345678a`;
- artifact digest `sha256:a969aa3d04b2d2278d16e84e14ec2fbc046fc79c5bd1c63615e01c783592ce95`.

Frozen Q comparator job `99242395532` executed the exact comparison and failed because canonical SHA equality, `numpy.array_equal`, and frozen workspace-result metadata equality were false. This is **not** an infrastructure failure before classification.

## Binding classification before forensics

For the current prospectively frozen route, Q is:

`SCIENTIFIC_REPEATABILITY_FAIL`

where “scientific” refers to the frozen operator-repeatability criterion, **not** a dark-sector model-physics failure.

Exp073AF therefore maps current `P PASS + Q SCIENTIFIC_REPEATABILITY_FAIL` to:

`BLOCK_PRODUCTION`.

No tolerance, rounding, ULP allowance, near-equality rule, majority vote, or P-matching preference may change this classification retrospectively.

## Purpose

Use only the two immutable Q artifacts to localize the mismatch and distinguish:

1. input/provenance drift;
2. workspace-output-only numerical divergence;
3. unresolved other divergence.

No exact workspace is recomputed.

## Required forensic checks

- verify immutable artifact IDs/names/digests/run/head through GitHub API;
- load exactly one `metadata.json` and one `wm0_te_window.npz` per artifact;
- require NPZ key `wm0_te_window`, shape `[39,12288]`, dtype canonicalizable to `<f8`, finite values;
- compute canonical little-endian float64 C-order SHA256 for A and B;
- compare each to frozen P canonical SHA;
- evaluate exact `numpy.array_equal(A,B)`;
- count mismatched entries and mismatch fraction;
- compute maximum, mean, and median-nonzero absolute difference;
- report argmax coordinate and A/B values;
- report affected-band count, mismatch count by band, and maximum absolute difference by band;
- recursively compare metadata and report exact differing paths;
- classify `WORKSPACE_OUTPUT_ONLY_NUMERICAL_DIVERGENCE` only if all metadata differences are confined to `workspace.absolute_response_norms[*]` and `workspace.selected_window_authority.sha256`, while all upstream/input/provenance metadata are equal.

## Expected frozen diagnostic assertions from pre-hosted artifact inspection

These values are frozen as forensic expectations, not as acceptance thresholds:

- A canonical SHA: `6ec29f6dbbcf0c29d7af9d6eb98d271bcd06e00d28cebe658b5e266f7ef18d0f`;
- B canonical SHA: `8ac59fc0c81b2c3ce60f5a5d13424ffba1dda3148f1d35dff4d338124f9b9220`;
- A matches P canonical: true;
- B matches P canonical: false;
- exact A/B array equality: false;
- mismatched entries: `449676 / 479232`;
- affected bands: `39 / 39`;
- maximum absolute difference: `2.0816681711721685e-17`;
- mean absolute difference: `1.2536708729507546e-19`;
- median nonzero absolute difference: `4.0657581468206416e-20`;
- max-difference coordinate `[0,33]`;
- A at max: `0.028513752074989018`;
- B at max: `0.028513752074988997`;
- metadata differing paths count: `40`, restricted to 39 `workspace.absolute_response_norms` entries plus `workspace.selected_window_authority.sha256`.

If hosted forensic reproduction differs from these expectations, Exp073AH must fail closed; it may not edit expectations after seeing hosted output.

## Interpretation boundary

If the expected pattern is hosted-reproduced, the strongest permitted interpretation is:

> The Q disagreement is localized to tiny floating-point differences in the workspace numerical output with no detected input/provenance drift in the frozen metadata.

It is permissible to say this is **consistent with** runtime/hardware/thread floating-point nondeterminism. It is forbidden to claim a root cause has been proven unless separately isolated prospectively.

The exact-repeatability FAIL remains binding even though the numerical differences are tiny and Q-A matches P exactly.

## Anti-leakage and accounting firewall

Exp073AH must not read radial kernels, physical support, retained coordinates, fiducial P, covariance, whitening, nuisance geometry/SVD/rank, quotient/relation/null results, or G8. It must not launch Exp073AA production and must not claim a scientific model PASS.

Article-3 scientific readiness remains `52%`; readiness increment is `0`; G7/G8/G9 remain OPEN.

## Required hosted forensic token

`PASS_EXP073AH_Q_REPEATABILITY_MISMATCH_FORENSIC_V0_1`

This token means only that immutable hosted artifacts reproduce the preregistered forensic localization. It does not convert Q to PASS and does not authorize production.
