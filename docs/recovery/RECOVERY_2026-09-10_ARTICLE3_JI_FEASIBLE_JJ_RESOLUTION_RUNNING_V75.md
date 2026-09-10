# DSIR recovery V75 — Exp073JI full-support feasible; Exp073JJ shared-grid resolution convergence running

Date: 2026-09-10. Scope: **DSIR only**. Never mix RTK or RQIR.

## Preserved scientific authority
All prior admitted DSIR scientific authority remains unchanged. Repaired Exp073IR run/job `34432102035 / 102729564736` remains `NUMERICALLY_UNRESOLVED_EXP073IR`: original retained 107 coordinate rows, atomic native production-vs-dense maximum `0.9998247463807295 > REL_TOL=1e-3`; covariance restriction unauthorized. Historical Exp073CM remains resource/performance `+0/+0`; Wm_S3 remains unopened.

## Newly validated support authority — Exp073JI
Exp073JI run/job `34488466425 / 102908710275`, launch head `0922a0a3c05015f4f9610ce2eca324cfbbc46483`, is validated support-only `GUARD_NODE_FULL_SUPPORT_FEASIBLE_PLUS_0_PLUS_0`. Artifact `10156878354`; GitHub artifact digest and independent downloaded ZIP SHA256 both `f8492ca04ff3b159ffe28003d28c3756e428e9851f4a3af56e6f343666d1b0de`; result JSON SHA256 `c076af1fd5207d69c3fdc00f944ca2099aa4a4e82e31d0d0ce2877f3b679310a`; capacity-patch JSON SHA256 `c7d12d091c7112649e8273f567a17b10d89bd78ef2346aed1d429ac1c9a894e7`. Durable JI authority commit `bba2701467e8fce6bf41369c23e64be4d16f78f9`.

JI response-blind geometry authority: inherited target range `[0.00033800000000000003, 0.06664596609379447] Mpc^-1`, geometry stream SHA256 `79bae6f3015ccf524402d7f0f357070a903126bfa8d3bd3f4cac5902afef093a`, base N=512 lattice preserved bitwise, lower guards 0, upper guards 1, total requested nodes 513, extended k max `0.067501067828166`. Full-support accounting has zero unsupported target evaluations, kpd10-vs20 maximum relative component difference `0.0`, zero invalid rows, invalid-row fraction `0.0`, and all 107 rows retained. JI is +0/+0 only and does not authorize covariance or Wm_S3.

## Current process — Exp073JJ
A separate prospective shared-grid resolution-refinement gate was frozen after JI validation and before any JJ response output. Preregistration commit `aaf5ccb8860b95310bb19450cf5af533383e897b`; implementation commit `f9b4ddf8fd778098c9874469ea328c6b93a56149`; workflow/launch head `f47683ebda4f00e536c2e630930d3e3b76fed80f`.

JJ freezes native CLASS `k_per_decade_for_pk=20` for both suites and remaps the inherited IR comparison slots to two guarded shared physical-k lattices: coarse base N=512 + one upper guard = 513 nodes; fine base N=1024 + one upper guard = 1025 nodes. Both use the unchanged centered-cubic Lagrange interpolation in ln(k), the original 107-row support, h=1e-4, REL_TOL=1e-3, same judged z/k domain and exact original atom traversal/accounting. Capacity-only CLASS patch is 30->1152 and parser 1024->32768; no equations or scientific thresholds change.

Authoritative workflow/run/job: `exp073jj-article3-layerb-common-grid-resolution-refinement-convergence-v0-1 / 34492300395 / 102921844345`; GitHub-hosted `ubuntu-24.04`; checkpoint N/A; self-hosted ownership none. Last observed state IN_PROGRESS. Prospective JJ contract and exact JI authority enforcement passed; frozen numerical/build-stack installation was in progress.

JJ is support-only +0/+0 in every valid outcome. `COMMON_GRID_RESOLUTION_REFINEMENT_CONVERGED_PLUS_0_PLUS_0` requires zero unsupported targets, no finite/nonzero or row-label change, no BOSS dense-z disagreement, maximum atomic coarse-vs-fine relative component difference `<1e-3`, coarse Layer-B invalid-row fraction `<=0.05`, retained dimension `>=15`, and requested-node coordinate mismatch `<=1e-12`. A valid non-converged result remains +0/+0 and requires further mechanism isolation. Infrastructure failure requires smallest causal repair only.

Exact next action: terminal-consume run `34492300395`; inspect raw job logs and exact failure step if any, independently download/verify artifact digest and result/capacity hashes, classify strictly against the frozen JJ contract, update authority/recovery/current-process, and immediately dispatch the next prospectively permitted nonduplicating gate. A JJ convergence PASS permits only design of a separate prospectively frozen scientific Layer-B numerical rerun; it does not itself retroactively PASS Exp073IR or authorize covariance/Wm_S3.

Global frozen boundaries remain unchanged: `0.295<=z<=2.33`; judged `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; `REL_TOL=1e-3`; `h=1e-4`; exact-threshold ambiguity `numerically_unresolved`; no tolerance/rounding/smoothing/averaging/effective-coordinate/fiducial-P rescue.
