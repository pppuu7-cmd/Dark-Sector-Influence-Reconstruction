# DSIR recovery — Article III JL attempt-2 numerical / JM static preflight PASS — V80

Date: 2026-09-10. Scope: **DSIR only**. Never mix RTK or RQIR.

## Preserved authority
Repaired Exp073IR remains `NUMERICALLY_UNRESOLVED_EXP073IR` with original native production-vs-dense maximum `0.9998247463807295 > REL_TOL=1e-3`. Exp073JI remains validated full-support feasibility with 107 retained rows, zero invalid rows and zero native-kpd10-vs20 shared-grid response discrepancy. Exp073JJ remains valid support-only NOT_CONVERGED at `0.037280144773915974`. Exp073JK remains valid support-only `COMMON_GRID_SECOND_REFINEMENT_NOT_CONVERGED_PLUS_0_PLUS_0` at `0.016330535730270664`; authority commit `bfa641eab5050fb891a3e754fed8eb30ef12586f`. Covariance restriction remains unauthorized and Wm_S3 remains unopened.

## Exp073JL active authority process
JL prospectively compares guarded base N=2048 (2049 requested) against base N=4096 (4097 requested), preserving exact Exp073IR atom traversal/support, pinned CLASS-IV/public `d_m`, native kpd=20 for both suites, centered-cubic interpolation in ln(k), `h=1e-4`, `REL_TOL=1e-3`, masks and physical domain.

Preregistration commit `608fbf5fd9912b9f0244283d940a7adfecc41ac8`; implementation `43e1d74e8216c1ff66bfe4d0eed372673d0e5b1b`; workflow/head `d556db87763637dd90ed919dbe5d85ef95b4beb1`; run `34497160814`.

Attempt 1 / job `102938434376` is preserved as infrastructure/process `+0/+0`: an external hosted-runner shutdown interrupted numerical step 10 and produced no scientific artifact. It activates neither downstream branch.

Attempt 2 / job `102944693569`, same frozen head, is the sole authoritative active heavy JL process. Latest verified state: steps 1-9 all completed successfully (prospective contract and JK/JI authority, frozen numerical stack, CAMB, pinned capacity-patched CLASS-IV, DES payloads, exact inherited authorities, frozen BOSS inputs); step 10 `Execute frozen common-grid third-refinement convergence audit` is IN_PROGRESS; artifact upload remains pending. Do not cancel, rerun or duplicate this job while active.

JL infrastructure-only capacities remain `_MAX_NUMBER_OF_K_FILES_=4608` and `_ARGUMENT_LENGTH_MAX_=131072`; no scientific parameter, threshold or arithmetic changed.

## Pre-result conditional branches remain frozen
Before any JL numerical output was inspected, two mutually exclusive branches were frozen:
- Exp073JM prereg commit `440e430465b783365a66c715c7a08e8c1c3a45f8`, authorized only by a valid independently verified JL NOT_CONVERGED result. It freezes base 4096->8192, requested 4097->8193, unchanged cubic/kpd20/h/tolerance and infra capacities 9216/262144.
- Exp073JN prereg commit `ee35861a7e383749288b61133bffaca333c60ced`, authorized only by a valid independently verified JL CONVERGED result. It prospectively repeats the exact JL 2049->4097 architecture under a fresh science-authorizing Layer-B contract; support-only JL cannot be promoted retroactively.

The decision-neutral future argmax diagnostic standard remains frozen at commit `35282a723840c256168b752a86f54666c0cbb4e0` and cannot alter atom inclusion, denominator treatment, relative-error metric or `REL_TOL=1e-3`.

## Exp073JM static readiness
JM implementation was prepared response-blind at commit `3be509b3ac2ca325b8e2c099e91ef59bfbdd8a18`.

Initial static preflight `34499055755 / 102944880115` failed before geometry/metric validation solely because NumPy was absent in the minimal hosted environment (`ModuleNotFoundError: No module named 'numpy'`). The smallest infrastructure-only repair added frozen `numpy==1.26.4`, commit `36c5132cbed6b63a09c664478bdb13f8e01215fb`.

Replacement static preflight `34499322858 / 102945799113` completed SUCCESS. It proved:
- coarse guard geometry exactly `(0,1,4097)`;
- fine guard geometry exactly `(0,1,8193)`;
- serialized coarse `k_output_values` length `89928` characters;
- serialized fine length `179788` characters, both below parser capacity `262144`;
- the decision-neutral diagnostic accumulator reproduces exactly the unchanged frozen relative maximum on its unit test;
- token `PASS_EXP073JM_STATIC_PREFLIGHT_V0_1`.

This static PASS creates no scientific authority and does not activate JM before a valid JL NOT_CONVERGED authority exists.

## Exact next action
1. Terminal-consume JL attempt 2 `34497160814 / 102944693569`; do not duplicate it.
2. If terminal SUCCESS, inspect raw log and independently verify the uploaded artifact ZIP SHA256 plus contained result/capacity JSON hashes before any classification.
3. On valid JL CONVERGED, create durable JL authority and instantiate/run only the already-frozen Exp073JN science rerun; JM is forbidden.
4. On valid JL NOT_CONVERGED, create durable JL negative authority and instantiate/run only the already-frozen Exp073JM; JN is forbidden.
5. On another infrastructure/process failure, neither branch activates; diagnose the first causal failure and resume the same frozen JL science without changing thresholds or arithmetic.

## Frozen global boundaries
`0.295<=z<=2.33`; judged `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; `REL_TOL=1e-3`; `h=1e-4`; exact-threshold ambiguity `numerically_unresolved`; no tolerance/rounding/smoothing/averaging/effective-coordinate/fiducial-P rescue.
