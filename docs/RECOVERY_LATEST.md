# DSIR RECOVERY LATEST — live pointer

**Updated:** 2026-08-30.  
**Strict Article-3 scientific repository readiness:** **52%**.

**Stable historical manual:** `docs/RECOVERY_MANUAL.md`

**Current detailed checkpoint:**
`recovery/2026-08-30_article3_exp073x_cancelled_exp073x2_split_repeatability_launched.md`

## Current headline state

- Exp073R1 v0.8 genuine hosted source-mask reproduction: **PASS**.
- Exp073P v0.5 hosted prerequisite receipt: **PASS**.
- Exp073U immutable 1410-row observation skeleton: **PASS / non-classifying**.
- Exp073V broad-row support schema: **PASS / non-classifying**, 19/19 controls.
- Exp073W BOSS current-k compatibility: **PASS / non-classifying**; historical/current lower-k conventions give the same `54/240` retained BOSS mask.
- Exp073Y exact DES released n(z) inventory: **PASS / non-classifying**.
- Exp073Z v0.1: **NUMERICAL IMPLEMENTATION FAILURE, NOT SCIENCE**; no support result was produced.
- Exp073Z2 stable-direct DES radial authority: **PASS / non-classifying**.
- Exp073AB row-to-operator mapping: **PASS / non-classifying**; retained as the mapping authority, not a science classification.
- Exp073AD exact 5%-boundary numerical classifier QA: **HOSTED SYNTHETIC PASS / non-scientific**; exact-boundary ambiguity maps to `numerically_unresolved`, never false PASS/FAIL. This does not raise readiness.
- Exp073X exact `nside=4096` Wm_S0 pilot: **INCOMPLETE — HOSTED CANCELLATION / NO AUTHORITY REUSE**. Neither scientific PASS nor scientific FAIL.
- Exp073X2 split exact repeatability repair: **PROSPECTIVELY FROZEN + HOSTED RUN LAUNCHED; AUTHORITY PENDING**.
- Exp073AA generic exact angular task runner remains preregistered/frozen; production expansion is **NOT YET AUTHORIZED** until hosted X2 aggregator PASS exists.
- Layer A broad operator-support leakage: **OPEN**.
- Layer B common-response validity: **OPEN**.
- covariance/whitening: **BLOCKED**.
- G7/G8/G9: **OPEN**.

## Frozen scientific boundaries

Never change post hoc:

- `0.295 <= z <= 2.33` inclusive;
- `0 < k <= 0.06664762008318016 Mpc^-1`;
- Layer-A `operator_f_invalid <= 0.05` inclusive;
- Layer-B invalid observation-row fraction `<=0.05` inclusive;
- minimum final retained observation dimension `15`;
- DES classifying route `nside=4096`;
- positive absolute operator/window envelope only for support bookkeeping; measured Wm stays signed;
- no effective ell/z/k shortcut;
- no fiducial-P weighting;
- no covariance, whitening, nuisance SVD/rank, quotient/relation/null or G8 information during support selection;
- numerical ambiguity at an exact threshold must remain unresolved rather than being rounded into PASS or FAIL.

## Stable exact radial authority — Exp073Z2

- prereg `1bca74786885ec6f4af3496f5446cfc2bf4c5ced`;
- implementation `92a204e96f5008683684b849c85fdeeaf14c4e70`;
- workflow `56d0be58a8a9830624346438aa9c04e9803d956a`;
- workflow freeze `30a78013bc1c1807977e57a2d826e26ebfb1fdec`;
- trigger/head `530da3c2c9aef9e8308086df24c10abb3e06ed4f`;
- run `33279208949`, job `99171355322`;
- artifact `9722468056`;
- artifact digest `sha256:3eb8b025711e8df6d5452a3a57002f36c9d7de2b9116734b71d15d6822dd20be`;
- token `PASS_EXP073Z2_DES_RADIAL_KERNEL_STABLE_DIRECT_V0_2`.

No negative clipping was used. Direct-vs-independent reverse-tail identity errors are at machine precision; frozen coarse/fine normalization tolerance `5e-4` passed for Wm and WW.

## Angular frontier — Exp073X -> Exp073X2

Pinned Cosmotheka semantics remain unchanged: source masks are selected-object **count maps**, while the public redMaGiC HEALPix lens mask retains original positive weights above the frozen `0.5` threshold.

Frozen 14-task manifest commit:
`d99f1af2edd4f0b2b1c6286124b0c0b4c1c4bd76`.

The old Exp073X reuse amendment already states that Wm_S0 may be reused only after a PASS. Because Exp073X did not PASS and has no reusable final artifact, **reuse is forbidden**.

Exp073X record:

- run `33277263287`;
- job `99166064222`;
- trigger/head `62c66faec2123a05a2a8bc83b34a758737b33539`;
- final interpretation: `INCOMPLETE_INFRASTRUCTURE_RESOURCE_CANCELLED_NO_AUTHORITY_REUSE`.

Exp073X2 repairs only execution/persistence topology. The exact scientific/angular contract remains real DES Y1, `NSIDE=4096`, NaMaster 2.7, 39 frozen bandpowers, ell 0..12287, spin-0 x spin-2, selected `TE <- TE` response.

Prospective X2 chain:

- prereg `efe8a4e17638dfd9568fa710e24f56cd10526c6a`;
- single-workspace replica code `df2eecd73ed0d8de080348ba155a2f1a3e84d7e1`;
- strict aggregator code `8ec6f94ea9ddf3cc0a4c98e5af696d28d995b2b3`;
- workflow `a14047090d46e024965d1bd76b60830ef21616e9`;
- workflow freeze `5bd0ba084b00d963c670db6d04b1db6ea53e8f36`;
- trigger/head `2403d9680e1d08a3853084034eb2878faa52b4e0`;
- hosted run `33300997298`;
- state at this pointer update: authority pending; **NO X2 PASS CLAIM YET**.

Replica A and B independently reconstruct masks, compute exactly one workspace, and immediately persist JSON+NPZ. The aggregator may PASS only after both artifacts exist and frozen metadata, canonical SHA-256 and `numpy.array_equal` all agree. X2 PASS alone adds **0 readiness points**.

## Authorized order from here

`Exp073X2 hosted replicas A/B + exact aggregator`

`-> if and only if hosted aggregator PASS: bind exact replacement Wm_S0 authority`

`-> freeze/trigger remaining 13 exact angular tasks using the already preregistered Exp073AA semantics`

`-> join Wm_S0 + 13 task outputs into ordered 14-window authority`

`-> join 14 angular windows + Exp073Z2 radial authority + Exp073AB row mapping + Exp073W BOSS authority into immutable full pre-support 1410-row candidate-operator manifest`

`-> real Layer A broad support`

`-> freeze S_op in inherited Exp073U order`

`-> real Layer B common-response validity`

`-> only after Layer A + Layer B PASS: covariance restriction/Cholesky whitening`

`-> nuisance tangent SVD/rank -> signed quotient/relation/null -> fresh G8`.

While run `33300997298` is active, do **not** launch duplicate X2. Parallel work is limited to non-conflicting audits/prerequisites; no production angular trigger before hosted X2 authority.

## Recovery read order

1. `docs/RECOVERY_MANUAL.md`
2. `docs/RECOVERY_LATEST.md`
3. `recovery/2026-08-30_article3_exp073x_cancelled_exp073x2_split_repeatability_launched.md`
4. `experiments/073x2_article3_des_n4096_wm0_maskonly_repeatability_v0_1_prereg.md`
5. `experiments/073x2_article3_des_n4096_wm0_maskonly_repeatability_v0_1_workflow_freeze.md`
6. `.github/workflows/exp073x2-article3-des-n4096-wm0-maskonly-repeatability-v0-1.yml`
7. `docs/ARTICLE3_DES_ANGULAR_14_TASK_MANIFEST_2026-08-30.md`
8. `experiments/073aa_article3_des_angular_task_runner_v0_1_prereg.md`
9. `ci/exp073aa_article3_des_angular_task_runner_v0_1.py`
10. `experiments/073z2_article3_des_radial_kernel_stable_direct_v0_2_prereg.md`

DSIR remains independent of RTK and RQIR. Preserve scientific FAILs, numerical implementation failures, infrastructure failures/cancellations, provenance failures, synthetic QA PASSes and real hosted authority PASSes as distinct categories.
