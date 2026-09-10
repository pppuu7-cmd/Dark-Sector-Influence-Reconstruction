# DSIR recovery V60 — Exp073IW exact repeatability closed; Exp073IX instrumentation-neutrality running

Updated: 2026-09-10. Scope: **DSIR only**; RTK/RQIR excluded.

## Preserved scientific authority
All previously admitted DSIR authority remains unchanged. Repaired Exp073IR run/job `34432102035 / 102729564736`, artifact `10134905199`, remains `NUMERICALLY_UNRESOLVED_EXP073IR`: 0 invalid rows, `f_B=0`, retained 107, convergence maximum `0.9998247463807295 > 1e-3`, covariance restriction unauthorized. Exp073IV remains historical `SUPPORT_INVALID_PLUS_0_PLUS_0`; no tolerance rescue.

## Newly closed — Exp073IW
Workflow/run/job: `exp073iw-article3-layerb-exact-repeatability-diagnostic-v0-1 / 34439055218 / 102750048552`.
Head: `70cf145eae559c57cbc2c8105c9d4c05ce097fb1`.
Artifact: `10137307858`, API/independently downloaded ZIP SHA256 `836cd19ef5b0c1a1294b995712a16c30920e4beff1c0f5f5b820de8bed8ceac2`.
Inside artifact: `A.json` and `B.json` each SHA256 `6dea43dcc0eadaf91887f181732d20dceef04866d5687aa231b747312fec0cb1`; byte-identical. Both exact convergence maxima are `0.9998247463807295`. Raw log token: `PASS_EXP073IW_LAYERB_EXACT_REPEATABILITY_DIAGNOSTIC_V0_1`.
Classification: `REPEATABLE_EXACT_PLUS_0_PLUS_0`. Scientific effect `+0/+0`; no covariance/model authority.

The direct repaired producer is therefore exactly repeatable inside one pinned job. Parent Exp073IR and Exp073IW also reproduce the same exact maximum on the same visible hosted runner image/software lineage. The earlier Exp073IV tiny mismatch remains a support-diagnostic issue and must not be used to reinterpret the scientific gate.

## Prospectively frozen next diagnostic — Exp073IX
Preregistration: `docs/dsir4/prereg/EXP073IX_ARTICLE3_LAYERB_INSTRUMENTATION_NEUTRALITY_DIAGNOSTIC_V0_1.md`, commit `a4edfebfe3f416f41c2e1fcc119430aef35528c7`.
Workflow commit: `b657c96d4234aaa0df3b55f3ffa17cb9ab5a9015`.
Trigger/head: `b05ce738c904cc49e683570868edccf2cf3eb610`.
Workflow/run/job: `exp073ix-article3-layerb-instrumentation-neutrality-diagnostic-v0-1 / 34443359314 / 102762823702`.
Runner ownership: GitHub-hosted `ubuntu-24.04`; home/self-hosted ownership none.
Checkpoint namespace: N/A (hosted support diagnostic).
State at ledger update: IN_PROGRESS; frozen lineage passed and stack installation underway.

Exp073IX executes one uninstrumented repaired Exp073IR and one exact existing Exp073IV-wrapped Exp073IR in the same built environment with independent scratch directories and exact frozen inputs. It classifies only whether the previous IV mismatch is instrument-causal, neutral, environment drift, or invalid infrastructure. Every outcome is support-only `+0/+0`; `REL_TOL=1e-3`, `h=1e-4`, k sampling, domains, interpolation, atomization, row rules and covariance firewall remain unchanged.

## Exact next transitions
1. Terminal-consume run `34443359314`, raw job log and artifact; verify digest/provenance and direct/instrumented output hashes.
2. If `INSTRUMENTATION_CAUSAL_PLUS_0_PLUS_0`, record the IV wrapper as non-neutral under exact-bit diagnostics, retain IV as invalid support history, and prospectively freeze the smallest uninstrumented numerical-resolution mechanism experiment for the genuine Exp073IR convergence failure.
3. If `INSTRUMENTATION_NEUTRAL_PLUS_0_PLUS_0` or `ENVIRONMENT_DRIFT_PLUS_0_PLUS_0`, continue exact environment/build isolation before any numerical-resolution experiment.
4. Infrastructure invalid: repair only the diagnostic defect; never alter frozen science.

Global frozen boundaries remain unchanged: `0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; exact-threshold ambiguity `numerically_unresolved`; no tolerance, rounding, smoothing, averaging, effective ell/z/k, or fiducial-P rescue.