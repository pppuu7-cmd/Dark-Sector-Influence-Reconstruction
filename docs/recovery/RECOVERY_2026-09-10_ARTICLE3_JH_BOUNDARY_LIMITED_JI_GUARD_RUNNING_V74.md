# DSIR recovery V74 — Exp073JH boundary-limited; Exp073JI guard-node feasibility running

Date: 2026-09-10. Scope: DSIR only. Never mix RTK or RQIR.

## Preserved scientific authority
All prior admitted DSIR scientific authority remains unchanged. Repaired Exp073IR run/job `34432102035 / 102729564736` remains `NUMERICALLY_UNRESOLVED_EXP073IR`: original retained 107 coordinate rows, `f_B=0`, atomic native production-vs-dense maximum `0.9998247463807295 > REL_TOL=1e-3`; covariance restriction unauthorized. Historical Exp073CM remains resource/performance `+0/+0`; Wm_S3 remains unopened.

Validated JF/JG support chain remains unchanged. Exp073JG established that at the two frozen worst probes centered-cubic interpolation on the shared N=512 requested physical-k lattice meets `REL_TOL=1e-3` against exact-k references and is exactly invariant between kpd10 and kpd20.

## Newly closed — Exp073JH
Validated support-only classification `FULL_SUPPORT_GRID_INVARIANT_NOT_FEASIBLE_PLUS_0_PLUS_0`. Workflow/run/job `exp073jh-article3-layerb-full-support-grid-invariant-feasibility-v0-1 / 34487047656 / 102903883547`, launch head `0834a45f5e767d411ce694d081069403ea6fd908`, raw token `PASS_EXP073JH_FULL_SUPPORT_GRID_INVARIANT_NOT_FEASIBLE_V0_1`.

Artifact `10156346630`; GitHub upload digest and independently downloaded ZIP SHA256 both `c89fbebde6e9a635614cdebe7a82b088d3224183d82c6361e8133c8923b04edd`; result JSON SHA256 `cb88bd2570b668ea751a4536392e3d8f80349db707f5efe90f24bda360222ed6`; capacity patch JSON SHA256 `f7d8d33232908f5f90f557ef42eeead4acc9dcc58a92f69629857aece2e1889b`. Durable JH authority creation commit `33e294932fd91fcf245db97f48b37a835e9c38ed`.

JH full-support convergence itself is exact on supported targets: maximum kpd10-vs20 relative component difference `0.0`; finite/nonzero status unchanged; row labels unchanged; BOSS dense-z disagreement false; convergence pass true at frozen `REL_TOL=1e-3`. Requested common-node coordinate mismatch is at most `1.6491595171051063e-16`.

JH non-feasibility is caused by finite-lattice stencil coverage: 3202 inherited target evaluations lack a complete centered-cubic stencil (1217 in kpd10 traversal, 1985 in kpd20 traversal). Unsupported targets are intentionally NaN, propagating to all 107 coordinate rows: invalid-row fraction 1.0, retained 0. This is an evaluation-support boundary failure, not evidence of same-k solver or shared-grid convergence failure.

Independent source-level boundary audit was frozen before JH terminated in commit `29f081089bd6ce174285446a266dbc59baeed15e`. It permits only a response-blind same-ratio guard-node extension preserving all original 512 common nodes and the judged physical domain; clipping, extrapolation, dropped atoms or post-hoc estimator switching remain forbidden.

## Current process — Exp073JI
Exp073JI tests the minimal geometry-derived guard-node repair. Phase A uses the unchanged Exp073IR traversal with dummy finite-positive placeholders solely to record inherited target-k geometry; no physical response values are consulted. It derives the smallest lower/upper whole-step guard counts on the exact original JH geometric ratio such that every inherited target has the unchanged centered-cubic stencil. All original 512 nodes must be bitwise preserved; total requested-node count is prospectively capped at 640.

Phase B then reruns the exact original 107-row Exp073IR atomic-support accounting with the same centered-cubic rule, same h=1e-4, same kpd10/20 pair, same judged z/k domain and same `REL_TOL=1e-3`. Feasibility requires zero unsupported targets, convergence pass, Layer-B invalid-row fraction <=0.05 and retained >=15. JI remains support-only `+0/+0` even if feasible.

Prospective preregistration commit `e11bfc91fda03303e12cf038b7cb19ca3c003acc`; implementation commit `99d38309e709eafb5cf2450e9f898ef2f1015dea`; workflow/launch head `0922a0a3c05015f4f9610ce2eca324cfbbc46483`.

Authoritative workflow/run/job: `exp073ji-article3-layerb-geometry-derived-guard-node-feasibility-v0-1 / 34488466425 / 102908710275`; GitHub-hosted `ubuntu-24.04`; checkpoint N/A; self-hosted ownership none. Last observed state IN_PROGRESS. Prospective contract/JH authority passed; numerical/build stack installation in progress.

Exact next action: terminal-consume run `34488466425`; first verify geometry-derived guard counts/range and that the original N=512 lattice is preserved bitwise, then inspect unsupported count, full atomic convergence and Layer-B accounting, and independently verify the artifact digest. If JI is feasible, only then design a separate prospectively frozen absolute-accuracy/calibration or scientific Layer-B convergence gate. If not feasible, preserve the failure and isolate the next mechanism without weakening thresholds.

Global frozen boundaries remain unchanged: `0.295<=z<=2.33`; judged `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; `REL_TOL=1e-3`; `h=1e-4`; exact-threshold ambiguity `numerically_unresolved`; no tolerance/rounding/smoothing/averaging/effective-coordinate/fiducial-P rescue.
