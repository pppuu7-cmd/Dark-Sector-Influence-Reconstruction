# DSIR authoritative recovery — latest

Updated: 2026-09-10. Scope: **DSIR only**. Never mix RTK or RQIR.

Newest immutable authority note: `docs/recovery/RECOVERY_2026-09-10_ARTICLE3_JL_ATTEMPT2_NUMERIC_JM_PREFLIGHT_PASS_V80.md`, creation commit `cde89c3e0df959694b1c6b23007eb1c7fc497151`. Earlier notes remain immutable history.

## Preserved authority
Repaired Exp073IR remains `NUMERICALLY_UNRESOLVED_EXP073IR` with original native-grid maximum `0.9998247463807295 > REL_TOL=1e-3`. Exp073JI preserves full shared-grid support: all 107 retained rows, invalid fraction 0, native-kpd10-vs20 shared-grid discrepancy 0.0. Exp073JJ remains valid support-only NOT_CONVERGED at `0.037280144773915974`. Exp073JK remains valid support-only NOT_CONVERGED at `0.016330535730270664`, authority commit `bfa641eab5050fb891a3e754fed8eb30ef12586f`. Covariance restriction remains unauthorized; Wm_S3 remains unopened.

## Current process — Exp073JL attempt 2
JL prospectively compares guarded base N=2048 (2049 requested) against N=4096 (4097 requested), preserving exact Exp073IR support/traversal, pinned CLASS-IV/public `d_m`, native kpd=20 for both suites, centered-cubic ln(k), `h=1e-4`, `REL_TOL=1e-3`, masks and physical domain. Preregistration `608fbf5fd9912b9f0244283d940a7adfecc41ac8`; implementation `43e1d74e8216c1ff66bfe4d0eed372673d0e5b1b`; workflow/head `d556db87763637dd90ed919dbe5d85ef95b4beb1`; run `34497160814`.

Attempt 1 / job `102938434376` is infrastructure/process +0/+0 after external hosted-runner shutdown during numerical step 10; no scientific artifact/result was produced. Attempt 2 / job `102944693569`, same frozen head, is the sole authoritative active JL heavy computation. Latest verified state: steps 1-9 PASS; frozen numerical step 10 IN_PROGRESS; artifact upload pending. Do not cancel, rerun or duplicate while active. Infrastructure-only capacities remain 4608 k-values / parser 131072.

## Pre-result branches and static readiness
Decision-neutral future argmax diagnostic standard is frozen at commit `35282a723840c256168b752a86f54666c0cbb4e0`; it cannot change the metric, atom inclusion, denominator treatment or tolerance.

Two mutually exclusive post-JL branches were frozen before any JL numerical result:
- Exp073JM prereg `440e430465b783365a66c715c7a08e8c1c3a45f8`, activated only by a valid independently verified JL NOT_CONVERGED. It freezes base N=4096 vs N=8192 (4097 vs 8193 requested), same cubic/kpd20/h/tolerance, infra capacities 9216/262144.
- Exp073JN prereg `ee35861a7e383749288b61133bffaca333c60ced`, activated only by a valid independently verified JL CONVERGED. It prospectively repeats exact JL 2049->4097 architecture under a fresh science-authorizing Layer-B contract; support-only JL cannot be promoted retroactively.

JM implementation commit `3be509b3ac2ca325b8e2c099e91ef59bfbdd8a18`. First static preflight failed infrastructure-only because NumPy was absent; minimal dependency-only repair commit `36c5132cbed6b63a09c664478bdb13f8e01215fb`. Replacement static run/job `34499322858 / 102945799113` PASS with exact geometry `(0,1,4097)/(0,1,8193)`, serialized k-output lengths 89928/179788 < parser 262144, and exact metric-neutral argmax unit check. Token `PASS_EXP073JM_STATIC_PREFLIGHT_V0_1`. This does not activate JM science.

## Exact next action
Terminal-consume JL attempt 2 `34497160814 / 102944693569`; on success independently verify artifact ZIP/result/capacity hashes and classify against frozen JL. Valid CONVERGED -> durable JL authority then only JN. Valid NOT_CONVERGED -> durable JL negative authority then only JM. Infrastructure/process failure -> neither branch; diagnose and repair same frozen JL. No tolerance rescue.

Global frozen boundaries remain unchanged: `0.295<=z<=2.33`; judged `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; `REL_TOL=1e-3`; `h=1e-4`; exact-threshold ambiguity `numerically_unresolved`; no tolerance/rounding/smoothing/averaging/effective-coordinate/fiducial-P rescue.
