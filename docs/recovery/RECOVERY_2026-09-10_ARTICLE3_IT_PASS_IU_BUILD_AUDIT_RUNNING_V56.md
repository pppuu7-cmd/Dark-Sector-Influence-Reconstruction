# DSIR recovery V56 — Exp073IT PASS; Exp073IU d_m exposure patch build audit running

Date: 2026-09-10. Scope: DSIR only. Supersedes V55 as latest recovery pointer; V55 remains immutable history.

## Preserved science
All prior admitted DSIR scientific authority is unchanged. Exp073IQ Article-3 Layer-A remains PASS with 107 retained rows. Exp073IR run/job `34428699659 / 102719344981` remains `INVALID_FOR_SCIENCE_ARTICLE3_SUPPORT`, not a scientific FAIL, because its raw artifact `10133682066` (ZIP SHA256 `6d84e6ab94ea66d9b9f857727b7e6089cfb4cacc60e141660cd713e42d30a876`) lacked exact public `d_m` from pinned CLASS-IV. No Layer-B/covariance authority exists.

## Exp073IS historical support result
Run/job `34431475914 / 102727713276` rejected the hypothesis that pinned CLASS-IV already publicly exposes `d_m`: internal `index_tp_delta_m` exists, but public transfer titles/data contain `d_tot/index_tp_delta_tot`, not `d_m/index_tp_delta_m`. Classification is support-only `+0/+0`; never alias `d_tot` to `d_m`.

## Newly closed — Exp073IT
Prospective prereg commit `a46d3d8d04d3e94044e60a133f4583c7aa8ff2df`; workflow commit `4b3fbda81d220f214d0ba1f0324087ab09f197bf`; launch/head `cd8fb5e069bd8b404d15b04bea4c823e54ca90c8`.

Run/job `34431545882 / 102727918512` completed SUCCESS and raw log was inspected. Exact terminal evidence:
- `patch_target=index_tp_delta_m<-ppw->delta_m`;
- `forbidden_alias=index_tp_delta_tot/d_tot`;
- `classification=SUPPORT_PLUS_0_PLUS_0`;
- `cosmological_run_started=false`;
- `scientific_authority_created=false`;
- token `PASS_EXP073IT_CLASSIV_DM_INTERNAL_SOURCE_PATCH_TARGET_AUDIT_V0_1`.

Pinned source semantics are exact: `source/perturbations.c` blob `92a48331658c5941ed4eb43b0e98ee78e39b8385` calls `delta_m` the gauge-invariant total matter overdensity and assigns `_set_source_(ppt->index_tp_delta_m) = ppw->delta_m;`.

## Current support process — Exp073IU
Exp073IU prospectively freezes an implementation-only public-exposure patch/build audit:
- prereg commit `5a752298f4fa6bd6b6f0e832d5754e7bfe2c2ea8`;
- deterministic patch script commit `e2e36bcb81cf3f34ecb079f57b14c94ccbe590da`;
- initial workflow commit `179ae882dc390499380d218b1ae22bf69f496ae7`;
- workflow concurrency hardening commit `150dc1d22237079645e435650b28c6ff576ab896`;
- first launch head `34f5c9640cd87c68df68d573538e1fa18dceef76`, run `34431740917`;
- accidental registration-latency retrigger head `7c4be1d6652ac4324290bb1c508ddb37b61ff96b`, run `34431769157`.

Both are GitHub-hosted support/build jobs only; no cosmological Layer-B calculation is authorized. The retrigger occurred because the first run had not yet appeared in the live run list when checked. This is an orchestration duplication, not scientific duplication. Concurrency ownership has now been added prospectively for this workflow; do not create any further IU run. If both historical runs reach terminal state, accept at most one fully validated PASS as support authority and record the other as redundant `+0/+0` with no scientific consequence.

Frozen patch changes only: enable `has_source_delta_m` in ordinary density-transfer source flags, expose distinct public `d_m` title, expose distinct `tk[index_tp_delta_m]` data column, preserve `d_tot` separately. It does not alter `ppw->delta_m`, equations, cosmology, h=1e-4, interpolation, domains, thresholds or downstream firewall.

## Next transition
Consume terminal IU raw logs. A valid exact token `PASS_EXP073IU_CLASSIV_DM_PUBLIC_EXPOSURE_PATCH_BUILD_AUDIT_V0_1` plus successful pinned-source/hash/static/build checks authorizes a prospective implementation-only Exp073IR retry using exactly the audited patch. Until then, no Layer-B rerun.

Global frozen boundaries unchanged: `0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; exact-threshold ambiguity `numerically_unresolved`; no tolerance/rounding/smoothing/averaging/effective-coordinate/fiducial-P rescue.