# DSIR recovery V67 — Exp073JD exact-k mechanism observed; Exp073JE shared-grid scaling running

Date: 2026-09-10. Scope: DSIR only. Never mix RTK or RQIR.

## Preserved scientific authority
All earlier admitted DSIR scientific authority remains unchanged. Repaired Exp073IR run/job `34432102035 / 102729564736` remains `NUMERICALLY_UNRESOLVED_EXP073IR`: 0 invalid rows, `f_B=0`, retained 107, exact native production-vs-dense maximum `0.9998247463807295 > REL_TOL=1e-3`; covariance restriction unauthorized. No tolerance rescue.

Exp073IR's 107 retained objects are coordinate rows, not 107 individual `(z,k)` atoms. The frozen implementation evaluates many atomic response samples inside each retained coordinate: DES uses the Limber k grid over 2001 reconstructed redshift samples and BOSS uses matrix-supported k samples over 64 Gauss-Legendre redshifts. The unresolved criterion is evaluated on atomic production-vs-dense response differences and finite/nonzero/label status before the row-level `f_B`/retained decision.

Historical Exp073CM remains resource/performance `+0/+0`, not Wm_S3 scientific arithmetic authority. Wm_S3 remains unopened pending its separately prospectively versioned resource gate and lawful science path.

## Closed support mechanism — Exp073JD
Validated support-only classification `EXACT_K_ORIGINAL_PAIR_OBSERVED_PLUS_0_PLUS_0`. Run/job `34472918931 / 102856790715`, head `00994fba5f77100a3ffff11f205abb3be5e1a1dc`, token `PASS_EXP073JD_EXACT_K_ORIGINAL_PAIR_OBSERVED_V0_1`. Artifact `10150322510`; independently verified ZIP SHA256 `1eb87185c6015277eeae72e3dd9017f48df03e8b166c05cde514330667189478`; result JSON SHA256 `2f395819980381fa8004e0f928283ada664e974ef6576455857f65bad191c70a`.

At alpha-left `(z,k)=(0.7000000000000001,0.002502504647141259 Mpc^-1)`, exact internal-k response is `11.514018402323245` at both native kpd 10 and 20; relative discrepancy `0.0`. At beta-symmetric `(0.9351,0.01860440444314368 Mpc^-1)`, exact response is `1.9210920856949087` at both kpd 10 and 20; relative discrepancy `0.0`. Every injected coordinate mismatch is `0.0`.

Interpretation: the catastrophic original-pair failure at the two historical worst probes is localized to model-dependent k-grid/interpolation/evaluation architecture, not the same-physical-k finite-difference response. This does not retroactively PASS Exp073IR.

## Scaling constraint discovered
Pinned CLASS-IV `ac627d54e9ce196a08878d1ba33999819925d19c` defines `_MAX_NUMBER_OF_K_FILES_ 30`. Direct exact injection of every DES atomic Limber k is therefore not a viable unmodified production architecture. A scalable repair must use a shared model-invariant fixed physical-k support grid and interpolate only between those common nodes, or another prospectively justified architecture; it must not return to model-dependent native-grid interpolation.

## Current process — Exp073JE
Purpose: determine whether shared fixed physical-k grids with `N={64,128,256}` converge to the Exp073JD exact-k responses at the two historical worst probes, while remaining invariant between native `k_per_decade_for_pk={10,20}`. The historical targets are explicitly forbidden from being inserted into the fixed grids, so the test exercises interpolation rather than repeating exact-k injection.

Shared fixed domain `[1e-4, 0.06664762008318016] Mpc^-1`. Frozen `REL_TOL=1e-3`, finite-difference `h=1e-4`. The only CLASS capacity change is a prospectively declared infrastructure enlargement of `_MAX_NUMBER_OF_K_FILES_` from 30 to 512, with pre/post source SHA recorded at execution; no equations or transfer definitions may change.

Prospective preregistration commit `2cb38664443bd17dfc2d304c1ecb21ed32b0e1dd`; implementation commit `67ce16ca1e92adbb98117dd5786fd179e793c929`; workflow/launch head `257ef3295e09870df02e681275f828c9bceab8bf`.

Authoritative workflow/run/job: `exp073je-article3-layerb-shared-fixed-k-grid-scaling-v0-1 / 34474514433 / 102861967751`. GitHub-hosted `ubuntu-24.04`; checkpoint N/A; self-hosted ownership none. Last observed state IN_PROGRESS; prospective contract/JD lineage passed, environment installation in progress.

Exp073JE is support-only `+0/+0` regardless of outcome. A grid N is only a scaling candidate if alpha and beta, for both kpd values, have relative error to exact JD `<1e-3` and kpd10-vs20 discrepancy `<1e-3`. A candidate can only nominate a later full atomic-support audit; it cannot authorize covariance restriction or Layer-B science.

Exact next action: terminal-consume run `34474514433`; verify capacity patch provenance, raw token, node-coordinate provenance and artifact digest. If a scaling candidate exists, prospectively design the full atomic-support shared-grid feasibility/audit preserving the exact Exp073IR atomic criterion. If none exists, continue scaling/mechanism isolation without tolerance rescue.

Global frozen DSIR boundaries remain unchanged: `0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; `REL_TOL=1e-3`; `h=1e-4`; exact-threshold ambiguity `numerically_unresolved`; no tolerance/rounding/smoothing/averaging/effective-coordinate/fiducial-P rescue.
