# Layer-B post-16385 exact response-atom hotspot localization V0.1

Status: **DORMANT / NOT EXECUTION-AUTHORIZED**. This contract is frozen before terminal consumption of the active broad-quantile localization run.

## Purpose
If the active 15-quantile broad support stage is insufficient to explain/localize the already-authoritative full-traversal plateau `0.012484060640679777`, localize that plateau on the exact frozen shared response-call geometry without changing any scientific numerical parameter.

## Frozen inputs and identities
- authoritative 8193 canonical node payload SHA256 `6d35a9d79aa8826554e8e39315ab12a8be1675d32d25a86ec04c978c7723a515`;
- authoritative 16385 canonical node payload SHA256 `3e10cea6e46a6d0c07eac825a4e508829727914c8690d42b187ef894eaa2c975`;
- exact response-blind request-plan authority coarse/common SHA256 `505716116cc385d5700e455017d8e541c5bba7774fa6647298392495c83ecfe0` and fine+GL128 SHA256 `0f7ce2e5fa459e15954268dfd46045eaa0ab6356dfdab5a2e282514e7a34ae4e`;
- frozen IR source blob `6ef2516dfcae8a8ae92f5b7dbe792274138c0f6f`;
- frozen recovered response engine blob `5f8475b961db20bef5f4b8a2eb7c99d9f7c722e2`;
- same CLASS-IV source commit, execution-only history suppression, baseline, precision, `h=1e-4`, native `k_per_decade_for_pk=20`, centered-cubic interpolation, physical domain and lookup tolerance as the authoritative 8193->16385 run.

## Frozen request selection
Run the response-blind PlannerSuite exactly once. It must produce slot/count sequence `[10,10,20,20] / [377,64,441,128]`.

For localization compare only the exact 441 response calls shared by the coarse and fine scientific convergence calculation:
- calls 0..376: DES request calls;
- calls 377..440: BOSS GL64 request calls.

The fine-only GL128 128-call block is excluded from the numerical convergence hotspot scan because in the frozen IR it is a separate dense-z support/label gate and does not enter `max_relative_component_difference`.

Before any solver construction, every one of the 441 shared calls must match bitwise between the coarse plan (`PlannerSuite[0]+PlannerSuite[1]`) and the fine common plan (`PlannerSuite[2]`): binary64 z and every target binary64 value, including target-vector length/order.

## Frozen execution and comparison
Evaluate canonical 8193 and canonical 16385 independently with exactly four role-major CLASS constructions per lattice, max one live instance, roles `reference`, `alpha_minus`, `beta_plus`, `beta_minus`, same-process finite-difference combination and frozen `h=1e-4`.

For each shared call, target and response component, compute only when finite/nonzero status agrees:
`abs(coarse-fine) / max(abs(coarse), abs(fine))`.

Record:
- global maximum and its exact `(call index, DES/BOSS block, z binary64, target index, target k binary64, component)`;
- top 64 response atoms by the same relative difference with deterministic tie-break `(relative difference desc, call index asc, target index asc, component asc)`;
- one maximum receipt for each of the 441 calls;
- counts of finite/nonzero status changes;
- unsupported and lookup receipts;
- execution lifecycle.

The diagnostic global maximum is expected to reproduce the already-authoritative `0.012484060640679777` only as a provenance/localization consistency check. A mismatch is a diagnostic/infrastructure issue, not permission to alter tolerance, h, grids, interpolation, masks or the original classification.

## Scientific authority
This experiment is support-only `+0/+0`. It does **not** rerun or replace the 107-row scientific classification, cannot authorize 32769, cannot authorize covariance restriction, and cannot open Wm_S3. It exists solely to identify the response atom(s) responsible for the already-closed NOT_CONVERGED result.

## Activation
No automatic activation is granted by this file. Numerical execution may be launched only after the active broad-quantile artifacts are terminal and independently consumed, and after repository recovery records that exact hotspot localization remains a justified nonduplicating next diagnostic. Preparing/static-auditing the implementation before then is permitted because it does not read the active broad output.
