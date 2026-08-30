# Exp073AM — Article 3 Exp073AI aggregator-only environment-path repair v0.1

**Frozen:** 2026-08-30 after Exp073AI run `33310888983` became terminal and after its aggregator log established a `FileNotFoundError` before any numerical comparison, but before any repaired comparison is executed.

## Classification of the original Exp073AI terminal run

The original Exp073AI run is **not** a scientific/repeatability FAIL. Both exact single-thread replica jobs completed successfully and persisted immutable artifacts, but the aggregator failed before reading the environment receipts or comparing the angular arrays because the workflow passed a non-existent nested environment path.

Under the already-hosted-tested Exp073AK2 completion firewall, retain the original run as:

`INCOMPLETE_INFRASTRUCTURE_AGGREGATOR_ENV_PATH_ERROR_BEFORE_REPEATABILITY_CLASSIFICATION`

This record is permanent and must not be rewritten after the repair.

## Immutable inputs reused

Exp073AM must reuse exactly these Exp073AI replica artifacts from run `33310888983`, head `fdfb0eae9ea799b4a185a059a0d1b9dfca17b31d`:

- replica A artifact `9734480133`, digest `sha256:aa9f09e3dc8812341ad049ed39f5dea6da9249cf849417c60e825a7e48f93bc7`;
- replica B artifact `9734849638`, digest `sha256:f965b7cc120359d41246eccaa3d70a711485e75641252afe4d79813a061e5aee`.

No workspace may be recomputed.

## Frozen comparator

Use the unchanged Exp073AI comparator at commit:

`98e1518c34e30b0a7e59724ae60b7586f8c52f9c`

file:

`ci/exp073ai_compare_single_thread_replicas_v0_1.py`.

No tolerance, rounding, ULP allowance, majority voting, or numerical rule change is permitted.

## Sole allowed repair

After `actions/download-artifact@v4` extracts the original artifacts into `external/a` and `external/b`, pass the environment receipts at the artifact-root paths:

- `external/a/exp073ai_env_a_v0_1.json`;
- `external/b/exp073ai_env_b_v0_1.json`.

The replica JSON/NPZ files remain discovered recursively by the frozen comparator and therefore require no path or code change.

No other scientific, numerical, provenance, threshold, or accounting modification is allowed.

## Valid repaired outcomes

Only the unchanged comparator tokens are valid:

- `PASS_EXP073AI_SINGLE_THREAD_EXACT_REPRODUCIBILITY_V0_1` iff exact canonical SHA equality and `numpy.array_equal(A,B)==True`;
- `SCIENTIFIC_REPEATABILITY_FAIL_EXP073AI_SINGLE_THREAD_EXACT_V0_1` iff both complete immutable authorities are valid and disagree under that exact criterion.

A workflow/receipt/artifact failure in Exp073AM remains infrastructure-INCOMPLETE and may not be promoted to repeatability FAIL.

## Firewall/accounting

Exp073AM is non-classifying with respect to dark-sector physics. It must not read or compute radial support, physical k, retained coordinates, fiducial P, covariance, whitening, nuisance geometry, quotient/relation/null quantities, or G8.

Regardless of exact repeatability outcome:

- production release = false;
- future successor amendment remains required even if PASS;
- readiness increment = 0;
- Article-3 scientific readiness remains 52%;
- G7/G8/G9 remain OPEN;
- no scientific model PASS may be claimed.
