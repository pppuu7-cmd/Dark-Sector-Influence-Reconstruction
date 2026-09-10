# DSIR recovery — Exp073JL infrastructure shutdown and frozen rerun V79

Updated: 2026-09-10. Scope: **DSIR only**. Never mix RTK or RQIR.

## Preserved scientific authority
Repaired Exp073IR remains `NUMERICALLY_UNRESOLVED_EXP073IR`; original native production-vs-dense maximum `0.9998247463807295 > REL_TOL=1e-3`. Exp073JI remains validated full-support feasibility (107 retained, invalid fraction 0, shared-grid native kpd10-vs20 discrepancy 0.0). Exp073JJ remains validated support-only NOT_CONVERGED with maximum `0.037280144773915974`. Exp073JK remains validated support-only NOT_CONVERGED with maximum `0.016330535730270664`. Covariance restriction remains unauthorized; Wm_S3 remains unopened.

## Exp073JL attempt 1 — infrastructure failure +0/+0
Authoritative run `34497160814`, attempt 1 job `102938434376`, workflow/head `exp073jl-article3-layerb-common-grid-third-refinement-convergence-v0-1 / d556db87763637dd90ed919dbe5d85ef95b4beb1`.

Prospective contract/JK/JI lineage, frozen numerical/build stack, CAMB, exact pinned capacity-patched CLASS-IV build, DES payloads, inherited Layer-A/angular/Exp073IM authorities and frozen BOSS z3 operators all passed. During the frozen numerical step the GitHub-hosted runner received an external shutdown signal at `2026-09-10T15:56:49Z`; the operation was cancelled immediately afterward. No Exp073JL scientific result artifact was produced and upload-artifact was skipped.

Classification: **infrastructure failure +0/+0**. This is not CONVERGED, NOT_CONVERGED or a scientific FAIL. It activates neither conditional Exp073JM nor Exp073JN. No threshold, arithmetic, domain, interpolation, h, atomization or provenance rule changed.

## Minimal repair / resume
Live Actions was checked before resume and showed 0 queued and 0 in-progress DSIR runs. Because the first causal failure was external hosted-runner shutdown after all deterministic setup/input gates, the smallest non-scientific repair is a rerun of the exact same frozen JL job/run, rather than a new experiment or workflow modification. No valid numerical checkpoint existed inside the GitHub-hosted support-only job, so there is no durable numerical stage to restore.

Rerun request succeeded on the same run ID `34497160814`, run attempt 2. New authoritative job ID `102944693569`; same workflow/head `d556db87763637dd90ed919dbe5d85ef95b4beb1`; GitHub-hosted `ubuntu-24.04`; self-hosted ownership none; checkpoint N/A. Latest observed state: **IN_PROGRESS**, frozen stack installation after contract/lineage success.

## Frozen conditional branches remain unchanged
- Exp073JM prereg commit `440e430465b783365a66c715c7a08e8c1c3a45f8` is authorized only by a valid independently verified JL NOT_CONVERGED result.
- Exp073JN prereg commit `ee35861a7e383749288b61133bffaca333c60ced` is authorized only by a valid independently verified JL CONVERGED result.
- Infrastructure failure activates neither branch.

Exact next action: terminal-consume run `34497160814` attempt 2 / job `102944693569`; inspect raw logs and independently verify artifact ZIP/result/capacity hashes. Then instantiate only the matching already-frozen branch: JN on valid convergence, JM on valid non-convergence. If infrastructure fails again, diagnose the first causal failure and repair without scientific changes.

Global frozen boundaries remain unchanged: `0.295<=z<=2.33`; judged `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; `REL_TOL=1e-3`; `h=1e-4`; exact-threshold ambiguity `numerically_unresolved`; no tolerance/rounding/smoothing/averaging/effective-coordinate/fiducial-P rescue.
