# DSIR Article 3 recovery — Exp073Z2 radial PASS / exact DES angular frontier

**Checkpoint date:** 2026-08-30 Helsinki local date.  
**Strict scientific repository readiness:** **52%**.

This checkpoint supersedes Exp073V as the live recovery frontier but does not change any scientific gate. Exp073Z2 is a non-classifying prerequisite PASS; Exp073X angular pilot is still in progress at checkpoint creation.

## 1. Immutable scientific boundary

Never change post hoc:

- `0.295 <= z <= 2.33` inclusive;
- `0 < k <= 0.06664762008318016 Mpc^-1`;
- Layer-A broad-operator `f_invalid <= 0.05`;
- Layer-B invalid observation-row fraction `<=0.05`;
- minimum final retained observation dimension `15`;
- DES classifying route `nside=4096`;
- no effective ell/z/k scalarization;
- no fiducial-P support weighting;
- covariance/whitening/nuisance/relation/null/G8 forbidden during support selection.

G7/G8/G9 remain OPEN. Covariance remains BLOCKED until real Layer A and real Layer B pass on the same inherited authority.

## 2. Parent broad-row authority remains unchanged

Exp073U immutable 1410-row skeleton:

- run `33274852199`;
- job `99159670108`;
- artifact `9721184683`;
- digest `sha256:d44e628e9312fb5a919a6681b69d9e06e18418cdd299de641e6465e60dadfd68`;
- ordered ID SHA256 `bfaf582518cdbfd34b1e8392da83dac6b0885948bc31f2c29d4e48247c23af75`;
- order `Wm[780] -> WW[390] -> BOSS[240]`.

Exp073V broad-row schema QA remains PASS, 19/19 synthetic controls, and keeps observation rows distinct from physical support atoms.

## 3. BOSS frontier already stabilized

Exp073W established that the historical positive lower-k cutoff and current Article-3 `k>0` rule produce exactly the same frozen BOSS retained mask: `54/240` rows. Maximum change in per-row leakage was about `1.30e-6` and no row crossed the `0.05` threshold.

The BOSS third redshift bin remains hard support `0.5<z<0.75`, entirely inside Article-3 z support. Effective `z=0.61` is not a support coordinate.

No threshold was changed. BOSS is ready to enter the future pre-support finite-operator join, but this does not by itself score full Article-3 Layer A.

## 4. Exp073Y exact DES radial-input inventory

Hosted PASS:

- run `33277620469`;
- job `99167009794`;
- artifact `9721988957`;
- artifact digest `sha256:93f444feb01d00cc36088daeb246719e0cb24c6fcc97e2005c1c66401fc3f3cc`.

Both public DES radial products expose the same released midpoint grid:

- 400 nodes;
- nominal spacing `0.01`;
- `Z_MID = 0.0051 .. 3.9951`;
- logical Z SHA256 `b93b65adb24b98fd76a41486a1352978459af2836f533d0adadd0ca390dca89b`;
- no negative source or lens n(z) samples.

Source FITS SHA256 `b5d87138c35ae8bb4ecd02491972f544648398e606b3617039e6e54cb8ea943b`.
Lens/data-vector FITS SHA256 `114035179b5a8e41090751e9a6478536d185128581d37b5a510eff5722f417ca`.

## 5. Background geometry frozen before DES support output

Use the inherited Exp068B/G7 geometry only:

- `cmbant/CAMB@fa3f097343fbbe427cc04b4f5f0041c22c6ec764`;
- `H0=67`;
- `ombh2=0.0224`;
- `omch2=0.1200`;
- massless neutrinos, `nnu=3.046`;
- `TCMB=2.7255 K`, `YHe=0.24`, `tau=0`;
- `w=-1`, `wa=0`;
- physical Limber bookkeeping `k=(ell+0.5)/chi(z)`.

Article 3 does not inherit the old KiDS positive lower-k boundary.

## 6. Exp073Z v0.1 failure is numerical, not science

Run `33277788565`, job `99167465260` failed before any k/support evaluation.

Cause: the algebraic representation `g=T0-chi*T1` used tails formed as `total cumulative - prefix cumulative`; near the high-z vanishing tail this produced `min(g)=-1.4307726212042506e-10`, violating the pre-frozen `-1e-12` numerical guard.

No `f_invalid`, retained row, covariance, nuisance or G8 output existed. Preserve this run as `NUMERICAL_IMPLEMENTATION_FAILURE_NOT_SCIENCE`.

## 7. Exp073Z2 stable-direct radial authority — PASS

Prospective repair froze a positivity-preserving direct quadrature before its repaired output:

`g_i(z)=integral_z^infinity n_i(z_s) [chi(z_s)-chi(z)]/chi(z_s) dz_s`.

No negative clipping is allowed. Geometric factors are evaluated as `(chi_s-chi)/chi_s`.

Freeze chain:

- prereg commit `1bca74786885ec6f4af3496f5446cfc2bf4c5ced`;
- implementation commit `92a204e96f5008683684b849c85fdeeaf14c4e70`;
- workflow commit `56d0be58a8a9830624346438aa9c04e9803d956a`;
- workflow-freeze commit `30a78013bc1c1807977e57a2d826e26ebfb1fdec`;
- trigger/head `530da3c2c9aef9e8308086df24c10abb3e06ed4f`.

Hosted authority:

- run `33279208949`;
- job `99171355322`;
- artifact `9722468056`;
- artifact digest `sha256:3eb8b025711e8df6d5452a3a57002f36c9d7de2b9116734b71d15d6822dd20be`;
- internal JSON SHA256 `3cb25beed23193a94e10d590296349713d1d83f92771215b72c10ea2e6f82c1a`;
- positive token `PASS_EXP073Z2_DES_RADIAL_KERNEL_STABLE_DIRECT_V0_2`.

Numerical result:

- fine/coarse minimum `g = 0.0`, with no clipping;
- direct-vs-independent reverse-tail raw-node relative differences: `3.36e-16 .. 6.79e-16`, far below frozen `5e-12` identity tolerance;
- max Wm coarse/fine normalization delta `2.3576587734425064e-4`;
- max WW coarse/fine normalization delta `1.1587446957811764e-4`;
- both pass frozen `5e-4` tolerance.

Canonical fine authorities:

- `chi_Mpc` SHA256 `e1f9a72fbe35140b984a56fc9e3b6f659082de9f9b45fc1a2e7e557e30783987`, shape `[2001]`;
- `H_km_s_Mpc` SHA256 `b782612550debe3363211260870b7a0a59988e4eee784bbb699ec8bb1afd112f`, shape `[2001]`;
- source efficiency SHA256 `a9b7b1b8c3e3f9f926e2d7786b13490109caf0aeff359dd3230f924955efd2ac`, shape `[4,2001]`;
- Wm radial SHA256 `414f47620071c1df6c23abe25d45312796af53a37102c34e1d844308d915efe1`, shape `[20,2001]`;
- WW radial SHA256 `56edaaf9ef6b03d00e7b83f158b204fc27171bef34a6a7bf3afbd8c71ed5cc0e`, shape `[10,2001]`.

This closes the current DES radial prerequisite only. Readiness remains 52%.

## 8. Exact DES angular semantics established

Pinned Cosmotheka confirms:

- `MapperDESY1wl._get_mask()` is an unweighted object-count map from selected source positions;
- `MapperDESY1gc._get_mask()` uses the public redMaGiC mask, maps UNSEEN to zero and keeps original weights only where `mask>0.5`;
- therefore the 84-GB metacal signal catalog need not be downloaded again for the angular workspace: exact R1 pixel records reproduce the source count masks.

R1 source-bin authorities:

| bin | rows | pixel-record SHA256 | unique pixels | occupancy SHA256 |
|---|---:|---|---:|---|
| S0 | 7,705,486 | `5b507215ca961c09b82786e61e681a0178c29e9b593c17b588e366722a021f15` | 4,305,774 | `b6ed74f31540d4041267f94e2f7cdb70b7040d943ba22a4aa7eab62418f8cb32` |
| S1 | 7,851,711 | `752f585125e413c7bd40cc5174cf7ef98e95f970022a351c5d91206f371d2241` | 4,339,193 | `fed1ffdf2ef7a7ae88e42615bd08e207e039239c44fa20b7994258f147a739f1` |
| S2 | 8,238,547 | `259295a1f5a23ad9e5c6b46842bcf612b0eb13dc701ab6d54eb15f0d7bb0105f` | 4,401,919 | `9e2bfb92289ca4a3abb11efabf7ac8d59bb7c68eb63a7104c2b247267733b24d` |
| S3 | 4,196,641 | `3996f2bacf29d46278773530058d4f5666c0d590bf6cebc06459659166bc60ec` | 2,943,132 | `21e3776111de305c108463b02b0e3fd5e138cc97817d37e7b05330132d058094` |

Lens mask SHA256 `a519b8522f899e4c33267bb0749f9734f8b7fa760d195636456d370f809a3d55`, bytes `104595840`.

Exp073T component order remains:

- spin0 x spin2 `[TE,TB]`;
- spin2 x spin2 `[EE,EB,BE,BB]`.

Selected physical angular windows are TE<-TE for Wm and EE<-EE for WW; full mode coupling is still computed.

## 9. 14 unique angular tasks and prospective Exp073X reuse

Frozen manifest commit `d99f1af2edd4f0b2b1c6286124b0c0b4c1c4bd76`.

Exactly:

- 4 Wm tasks: common lens mask x S0..S3;
- 10 unordered WW tasks: source pairs `i<=j`.

Prospective pilot-reuse amendment commit `ffdaf0255ccd9cc78b9eef585f6c16931d41be6b` was frozen while Exp073X was still in progress.

If and only if Exp073X PASSes exact repeatability, its first Wm_S0 workspace becomes production task Wm_S0; its second copy remains QA only. Then production computes the remaining 13 tasks. If Exp073X does not PASS, no reuse is authorized.

## 10. Exp073X current status at this checkpoint

- run `33277263287`;
- job `99166064222`;
- trigger/head `62c66faec2123a05a2a8bc83b34a758737b33539`;
- exact `nside=4096` Wm_S0 TE<-TE workspace computed twice for repeatability;
- setup, NaMaster 2.7 install, R1 binding, lens binding and memory inventory passed;
- current step: exact double workspace calculation still `in_progress` at checkpoint creation;
- no support/science output is available or authorized yet.

Do not launch production 13-task angular execution unless X completes with its frozen PASS token and immutable artifact.

## 11. Exp073AA production executor frozen before X output

- prereg commit `14b79794ab5dc1b8cc8a0fa769ab50cac99f45d9`;
- implementation commit `45ed8d8d1e90cdaf314e0384b6f3cdfef369925b`.

The executor recognizes all 14 unique task identities but the future production matrix, under successful X reuse, must run exactly the 13 remaining identities. Every task reconstructs and verifies the exact R1 source count mask, computes one NaMaster workspace, selects only `[39,12288]` TE<-TE or EE<-EE, hashes the canonical logical window and emits no support output.

Final production workflow/trigger must be frozen only after the exact Exp073X artifact identity is known and bound.

## 12. Exact next order

`Exp073X exact Wm_S0 pilot`

`-> if PASS, bind exact pilot artifact and freeze Exp073AA 13-task matrix`

`-> run 13 remaining exact nside4096 workspaces in parallel`

`-> join X Wm_S0 + 13 Exp073AA windows into ordered 14-window authority`

`-> bind Exp073Z2 radial authority + 14 angular authority + BOSS Exp073W into immutable full pre-support candidate manifest`

`-> only then evaluate real Layer A broad support`

`-> freeze S_op in inherited Exp073U order`

`-> real Layer B common-response validity`

`-> only after A+B PASS: covariance restriction/Cholesky whitening`

`-> nuisance tangent SVD/rank -> signed quotient/relation/null -> fresh G8`.

## 13. Read first when resuming

1. `docs/RECOVERY_LATEST.md`
2. this checkpoint
3. `docs/ARTICLE3_DES_ANGULAR_14_TASK_MANIFEST_2026-08-30.md`
4. `docs/ARTICLE3_DES_ANGULAR_EXP073X_PILOT_REUSE_AMENDMENT_2026-08-30.md`
5. `experiments/073aa_article3_des_angular_task_runner_v0_1_prereg.md`
6. `ci/exp073aa_article3_des_angular_task_runner_v0_1.py`
7. `experiments/073z2_article3_des_radial_kernel_stable_direct_v0_2_prereg.md`
8. `ci/exp073z2_article3_des_radial_kernel_stable_direct_v0_2.py`
9. `docs/ARTICLE3_BROAD_ROW_LAYERB_SCHEMA_AMENDMENT_2026-08-30.md`
10. `recovery/2026-08-30_article3_exp073v_broad_row_schema_pass.md`

DSIR remains independent of RTK and RQIR. Preserve negative scientific results, numerical implementation failures, infrastructure failures, provenance failures and successful gates as distinct classes.
