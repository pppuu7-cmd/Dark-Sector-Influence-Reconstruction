# DSIR authoritative recovery — latest

Updated: 2026-09-06. Scope: **DSIR only**. Never mix RTK or RQIR.

## Preserved authority

Wm_S1 Track-A exact PASS and admitted Wm_S2/Wm_S3 exact scientific PASS remain preserved. Historical negative/resource/infrastructure outcomes remain immutable.

`WW_S0_S0` remains admitted by Exp073EO v0.2 run/job `34005373819 / 101411448176`, artifact `9980754356`, digest `sha256:0e1a4cff3b761fecc65d8e07df9e56f8109fd221fb4454746caa8c7d0f2fb4be`.

`WW_S0_S1` remains admitted by Exp073EZ `34017921734 / 101444964371`, token `PASS_EXP073EZ_WW_S0_S1_FILEBACKED_PROVENANCE_ADMISSION_V0_1`. Its Exp073EY candidate is `34010599584 / 101425638857`, artifact `9983630139`, independently verified ZIP SHA256 `12291c1c9f6100ebfb03a6db1e613f422bd48bc6c02720f89ee613c8646cf9d6`, selected exact A/B SHA `49af7a3d165daaf7cc6781e2286e45cd5baa0042ed9770800588bced7d700e79`.

`WW_S0_S2` remains admitted by Exp073FF `34032384956 / 101484177968`, token `PASS_EXP073FF_WW_S0_S2_FILEBACKED_PROVENANCE_ADMISSION_V0_1`. Preserved lineage includes source head `de83e20a68f79ccf25b89b0d33eb4206e294c757`, contract `b7845df5ce4bc2bd730461476b7ff0831512003ceb5b3558436005c9876bd251`, R1 artifact `9720335366`, digest `sha256:ff87d8fc7d53b16b786a4eb3d6ffeb103676efb8a548223a187b9f59689f8abd`.

## Current science frontier — WW_S0_S3 / Exp073FG

Preregistration: `experiments/073fg_ww_s0_s3_filebacked_full_resolution_ab_science_v0_1_prereg.md`, blob `50c64a3f7e341f0a180b9c8dbc83a074f6cae150`.

Frozen target: ordered `(S0,S3)`, authoritative R1 `[0,3]`, two independently reconstructed source count maps and distinct spin-2 fields. Numerical/storage semantics remain DES NSIDE=4096; ell `0..12287`; 39 bands; PyMaster/NaMaster 2.7 lineage; serialized workspace `read_from(...,read_unbinned_MCM=True)` then public `get_bandpower_windows()`; one regular-file-backed unbinned MCM exactly `19,327,352,832` bytes with `/proc/self/maps` proof; full BPW `[4,39,4,12288]`; selected `EE<-EE`, canonical `<f8 [39,12288]`; exact A/B SHA plus `numpy.array_equal`; all finite; no tolerance/allclose/rounding/smoothing/averaging/manual reconstruction/effective-coordinate/fiducial rescue.

Candidate token remains `PASS_EXP073FG_WW_S0_S3_FILEBACKED_AB_EXACT_REPEATABILITY_V0_1`. Candidate alone creates no authority; separate provenance admission remains mandatory.

Historical pre-science wrapper failures `34033970885 / 101488568727` and `34034127464 / 101488993099` remain infrastructure `+0/+0`, never scientific FAILs.

Frozen current implementation blobs: `ci/exp073fg_ww_s0_s3_durable_ab_production_v0_1.py` `d919da63ad5ccd1b94255d9e45face1c922c4f44`; v0.2 `8749c20f41e5259787307bbd5d556cb772ceba18`; home wrapper `77e7f7dafc91ee79767eb31a288633ca1285c66e`; prune verifier `d925840c60035b30ed1375657585967ec2644e0d`; terminal comparator `74a1a2f8d3b44eaab66e834d69156e1810b75a8e`.

Current authoritative workflow/run **`34034377795`**, head **`4a02952ee3bcb368a088d87608f61243cd9f7056`**. Hosted lineage job `101489652912` = SUCCESS; hosted code/checkpoint audit `101489652945` = SUCCESS. Home science job **`101489679508`** on `DSIR-HOME-PC` is **IN_PROGRESS** in the frozen S0-to-S3 A/B step at latest live reconciliation. Do not inspect or interpret partial numerical output and do not launch any competing self-hosted DSIR workload. Exact durable checkpoint stage remains `UNKNOWN_NOT_INSPECTED_WHILE_RUNNING`.

On terminal state: consume compact artifact and raw job evidence immediately; independently verify ZIP SHA256, complete six-stage/prune provenance, frozen source/contract/R1/driver/patch identities, `19,327,352,832`-byte mmap proof, canonical `<f8 [39,12288]` `EE<-EE`, exact A/B SHA and `numpy.array_equal`, finiteness and no rescue. Exact numerical mismatch is a scientific FAIL. Infrastructure/provenance/software failure requires smallest prospective repair and checkpoint-preserving resume.

## Closed hosted support — future WW_S1_S1

The frozen 14-task manifest places `WW_S1_S1` immediately after `WW_S0_S3`. Exp073FH `34034445222` closed same-field architecture support `+0/+0`; Exp073FJ `34034662798` closed the remaining six WW semantic cells `+0/+0`; Exp073FK `34037855604 / 101499105572` closed the same-field transformation contract `+0/+0`. These support gates create no scientific authority and cannot start competing home science.

Exp073FL preregistration `experiments/073fl_ww_s1_s1_driver_generation_static_audit_v0_1_prereg.md`, blob `e578cac17048f73193ff73c97ca38cb1d644d202`, creation commit `8b59dd08cd79af594198b038bd96bd69910cab5f`, freezes a hosted-only qualification of deterministic S1S1 driver generation: exact `[1,1]`, one authoritative S1 reconstruction, one spin-2 field object, exact same-object coupling handoff, dedicated future S1S1 checkpoint namespaces, hardened complete-stage/prune semantics, public file-backed BPW route and no tolerance/rescue.

Historical first Exp073FL run/job **`34043934290 / 101515496355`**, head `25ef2ecccac9e79a3de1395b31cf7402e52c6277`, failed before science on an over-strict textual-format assertion against immutable Exp073FK. Classification: `IMPLEMENTATION_STATIC_FAIL_PLUS_0_PLUS_0`; no workspace, self-hosted computation or authority. Minimal repair commit **`37180c62451731e87bf7e1f2ea17892da5d28070`** changed only the exact textual binding; scientific semantics were untouched. Reactivation head: **`cdbcf0019df9ef6ec9b71abc32dc12bee2ff0579`**.

Repaired Exp073FL run/job **`34043987159 / 101515646656`** completed SUCCESS. Raw job log contains exact token `PASS_EXP073FL_WW_S1_S1_DRIVER_GENERATION_STATIC_AUDIT_V0_1`, `classification=SUPPORT_PLUS_0_PLUS_0`, `ww_s1_s1_authority_created=false`, `self_hosted_science_started=false`. It compiled the hosted-only deterministic contract skeleton, checked one S1 reconstruction, one field construction, exact same-object handoff, forbidden stale/tolerance semantics, and synthetically rejected an equal-but-distinct second field. Immutable recovery note: `docs/recovery/RECOVERY_2026-09-06_EXP073FL_STATIC_PASS_FG_RUNNING.md`.

No heavy `WW_S1_S1` computation is authorized while Exp073FG owns the home runner. After Exp073FG is terminal and fully consumed, an exact S1S1 production driver and fail-closed home envelope may be committed/audited under FH/FJ/FK/FL, but those support steps still create no S1S1 scientific authority.

## Frozen publication architecture

`docs/DSIR_PUBLICATION_ARCHITECTURE_2026-09-06.md`, creation commit `fce46eb74aad797285e2a3fd89d01e41633e76f0`, blob `4661b4c9c796094a57e3e5f33e3fd8a25c186eb5`, remains frozen. Sequence: **DSIR-1 Framework -> DSIR-2 inverse reconstruction/mathematical machinery -> DSIR-3 observational implementation + complete funnel -> DSIR-4 Existing-Model Funnel Matrix -> conditional DSIR-5 DSIR-derived new dark-sector model -> conditional DSIR-6 independent predictions/external falsification tests**. Existing models are tested through the prospectively frozen funnel before a new model is claimed necessary; future model construction must remain anti-circular with design and blind/external validation separated.

## Frozen global boundaries

Unless prospectively superseded: `0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; exact-threshold ambiguity `numerically_unresolved`; no tolerance, rounding, smoothing, averaging, effective ell/z/k or fiducial-P shortcut.
