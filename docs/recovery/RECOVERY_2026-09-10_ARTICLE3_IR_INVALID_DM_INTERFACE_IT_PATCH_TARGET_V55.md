# DSIR recovery V55 — Article-3 Exp073IR INVALID; exact d_m interface cause isolated; Exp073IT queued

Date: 2026-09-10. Scope: DSIR only. This note supersedes V54 as recovery pointer while preserving all earlier authorities and historical results.

## Preserved scientific authority
All prior DSIR admitted authority remains unchanged. In particular Wm_S1 Track-A exact PASS, admitted Wm_S2/Wm_S3 and admitted WW_S3_S3 remain preserved. Article-3 Exp073IQ Layer-A is authoritative PASS: run/job `34423479633 / 102703685034`, head `20d428daef65a4c0d052b7526a4469f9b52f24af`, artifact `10131794281`, digest `sha256:ac959926639d3b46ecfe114e396ce03cb20a0763ef2781db454408d8ad0759df`, retained set 107 with retained-id SHA256 `44b57c6c910bc3612310ce415d773c8c180497528bfc5fc2927ce61da6ad40d7`.

## Exp073IR terminal result — INVALID_FOR_SCIENCE, not scientific FAIL
Frozen Exp073IR Article-3 Layer-B run `34428699659`, job `102719344981`, head `dac55828f7d1e1e033769d9fd4e43079d224758b` completed at the workflow level but its raw result is `INVALID_FOR_SCIENCE_ARTICLE3_SUPPORT`.

Artifact `10133682066`, GitHub/independently matched ZIP SHA256 `6d84e6ab94ea66d9b9f857727b7e6089cfb4cacc60e141660cd713e42d30a876`, contains exact causal error:

`AssertionError: expected exact d_m key, got ['k (h/Mpc)', 'd_g', 'd_b', 'd_cdm', 'd_idm_iv', 'd_ur', 'd_tot', 'phi', 'psi']`.

Therefore no Layer-B PASS/FAIL, no covariance restriction authority and no downstream scientific authority were created. The earlier isolated classy-install problem was infrastructure-only and was repaired before this run; the first causal failure of this terminal run is the source-interface mismatch above.

## Exp073IS support audit — frozen hypothesis rejected, +0/+0
Exp073IS was prospectively frozen at commit `71bbcf6417ed990831f523838759cfaf70733810` to test whether the exact pinned CLASS-IV public transfer writer exposes the already-defined gauge-invariant `index_tp_delta_m` as `d_m`.

Run `34431475914`, job `102727713276`, head `e3594cc3de2a55a6120e95e0eb5287ebe2a94576` failed its static scientific-interface hypothesis, which is a support result `+0/+0`, not a Layer-B scientific FAIL. Raw checks established:
- `index_tp_delta_m` and `index_tp_delta_tot` are distinct;
- number-count density enables `has_source_delta_m`;
- both indices are defined;
- pinned public transfer writer has `d_tot/index_tp_delta_tot`;
- pinned public transfer writer has no `d_m/index_tp_delta_m` title/data column.

This forbids aliasing `d_tot` to `d_m` merely to make IR pass.

## Exact upstream semantic anchor
At pinned `kaeonikc/class_iv@ac627d54e9ce196a08878d1ba33999819925d19c`, `source/perturbations.c` blob `92a48331658c5941ed4eb43b0e98ee78e39b8385` explicitly labels the `delta_m` source as `total matter overdensity (gauge-invariant, defined as in arXiv:1307.1459)` and assigns `_set_source_(ppt->index_tp_delta_m) = ppw->delta_m;` when the source is enabled.

Thus the next admissible repair target is implementation-only exposure of this same existing source, never substitution by `d_tot`, raw species density or a second gauge correction.

## Current process — Exp073IT
Prospective patch-target static audit:
- prereg commit `a46d3d8d04d3e94044e60a133f4583c7aa8ff2df`;
- workflow commit `4b3fbda81d220f214d0ba1f0324087ab09f197bf`;
- launch/head `cd8fb5e069bd8b404d15b04bea4c823e54ca90c8`;
- workflow/run: `exp073it-classiv-dm-internal-source-patch-target-audit-v0-1 / 34431545882`;
- job ID: not yet assigned at ledger write;
- runner: GitHub-hosted `ubuntu-24.04` when assigned;
- checkpoint namespace: N/A;
- state: QUEUED;
- expected token: `PASS_EXP073IT_CLASSIV_DM_INTERNAL_SOURCE_PATCH_TARGET_AUDIT_V0_1`;
- classification on PASS: `SUPPORT_PLUS_0_PLUS_0` only;
- home/self-hosted ownership: none.

### Exact next transitions
SUCCESS: consume raw log; verify exact pinned source/blob and PASS token; then prospectively freeze a minimal CLASS-IV public-exposure patch/build audit that only exposes `index_tp_delta_m <- ppw->delta_m` and enables that source for the transfer request. Do not rerun numerical Layer B until that patch passes hosted build/static audit.

FAIL/BLOCKED: diagnose the first exact source/static-audit mismatch; do not modify any Layer-B science or substitute `d_tot`.

Global frozen DSIR boundaries remain unchanged: `0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; exact-threshold ambiguity `numerically_unresolved`; no tolerance, rounding, smoothing, averaging, effective ell/z/k or fiducial-P shortcut.