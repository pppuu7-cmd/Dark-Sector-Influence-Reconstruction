# DSIR authoritative recovery — latest

Updated: 2026-09-10. Scope: **DSIR only**. Never mix RTK or RQIR.

Newest immutable authority note: `docs/recovery/RECOVERY_2026-09-10_ARTICLE3_JL_INFRA_SHUTDOWN_RERUN_V79.md`, creation commit `523309bb176633f93a7a721e0220454b4093fdf1`. Earlier notes remain immutable history.

## Preserved authority
Repaired Exp073IR remains `NUMERICALLY_UNRESOLVED_EXP073IR`; its original atomic native production-vs-dense maximum remains `0.9998247463807295 > REL_TOL=1e-3`. Exp073JI remains validated full-support feasibility with all 107 rows, invalid fraction 0 and native-kpd10-vs20 shared-grid discrepancy 0.0. Exp073JJ remains validated support-only `COMMON_GRID_RESOLUTION_REFINEMENT_NOT_CONVERGED_PLUS_0_PLUS_0`, maximum `0.037280144773915974`. Covariance restriction remains unauthorized; Wm_S3 remains unopened.

## Exp073JK validated not converged
Run/job `34495159732 / 102931623100`, head `6490000bd63b68f651c328382a36db03c42c8ccc`, is validated support-only `COMMON_GRID_SECOND_REFINEMENT_NOT_CONVERGED_PLUS_0_PLUS_0`. Artifact `10160083225`; independently verified ZIP SHA256 `a58bedd36365bf8d7a99627b1a39d2bc83f3dae41e3d9a6d3351617caa00dd99`; result JSON SHA256 `53aeb88118c004be659755cf1cffa49bed347fe02193f3ef6c2729e102e31181`; capacity patch SHA256 `a0646cff6e8b18814646c9b82ec571c93fc687db62e54e9f71c7333c78f19035`; durable authority commit `bfa641eab5050fb891a3e754fed8eb30ef12586f`.

JK compared guarded base N=1024 (1025 requested) versus base N=2048 (2049 requested), native CLASS kpd=20 fixed for both. Maximum atomic relative component difference is `0.016330535730270664 > 1e-3`; JJ-to-JK reduction factor `2.2828488538078164`, interpretation-level empirical order ~`1.1899964460080732`. All 107 rows remain valid, unsupported targets 0, finite/nonzero/row-label/BOSS status unchanged and requested-node coordinate mismatch <=`1.6531028205966003e-16`. This is valid numerical non-convergence, not infrastructure failure.

## Exp073JL attempt 1 infrastructure failure; attempt 2 running
Exp073JL prospectively tests guarded base N=2048 (2049 requested) versus base N=4096 (4097 requested), preserving exact Exp073IR support/traversal, pinned CLASS-IV/public `d_m`, native kpd=20 for both suites, centered-cubic ln(k), `h=1e-4`, `REL_TOL=1e-3`, masks and physical domain.

Preregistration commit `608fbf5fd9912b9f0244283d940a7adfecc41ac8`; implementation `43e1d74e8216c1ff66bfe4d0eed372673d0e5b1b`; workflow/launch head `d556db87763637dd90ed919dbe5d85ef95b4beb1`.

Run `34497160814` attempt 1 / job `102938434376` is infrastructure failure `+0/+0`: after contract/lineage, frozen stack, CAMB, exact pinned CLASS-IV, DES, inherited authority and BOSS input gates all passed, the GitHub-hosted runner received a shutdown signal at `2026-09-10T15:56:49Z` during the frozen numerical step. No JL scientific result artifact was produced; upload-artifact was skipped. This activates neither JM nor JN.

Live Actions then showed 0 queued / 0 in-progress. The smallest causal repair was to rerun the exact same frozen job, because no durable numerical checkpoint existed inside this hosted support-only audit and no scientific code/configuration change was warranted. Rerun request succeeded as run `34497160814` attempt 2 / job `102944693569`, same head `d556db87763637dd90ed919dbe5d85ef95b4beb1`; GitHub-hosted `ubuntu-24.04`; self-hosted ownership none; checkpoint N/A. Latest observed state: IN_PROGRESS in frozen stack installation after contract/lineage success.

Response-blind capacities remain `_MAX_NUMBER_OF_K_FILES_=4608`, `_ARGUMENT_LENGTH_MAX_=131072`; no scientific quantity or threshold changed.

A response-blind future diagnostic standard remains frozen at `docs/dsir4/methods/LAYERB_CONVERGENCE_ARGMAX_DIAGNOSTIC_STANDARD_V0_1.md`, commit `35282a723840c256168b752a86f54666c0cbb4e0`.

Two mutually exclusive next branches remain prospectively frozen:
- `docs/dsir4/prereg/EXP073JM_ARTICLE3_LAYERB_COMMON_GRID_FOURTH_REFINEMENT_CONVERGENCE_V0_1.md`, commit `440e430465b783365a66c715c7a08e8c1c3a45f8`, authorized only if JL is valid independently verified NOT_CONVERGED.
- `docs/dsir4/prereg/EXP073JN_ARTICLE3_LAYERB_SHARED_GRID_SCIENTIFIC_CLOSURE_RERUN_V0_1.md`, commit `ee35861a7e383749288b61133bffaca333c60ced`, authorized only if JL is valid independently verified CONVERGED.
Infrastructure failure activates neither branch.

JL remains support-only +0/+0 in every valid outcome. Exact next action: terminal-consume `34497160814` attempt 2 / `102944693569`, inspect raw logs, independently verify artifact ZIP/result/capacity hashes and classify against the frozen JL contract. Then instantiate only the matching pre-frozen branch: JN on valid convergence, JM on valid non-convergence. If infrastructure fails again, diagnose and repair without scientific changes. No tolerance rescue.

Global frozen boundaries remain unchanged: `0.295<=z<=2.33`; judged `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; `REL_TOL=1e-3`; `h=1e-4`; exact-threshold ambiguity `numerically_unresolved`; no tolerance/rounding/smoothing/averaging/effective-coordinate/fiducial-P rescue.
