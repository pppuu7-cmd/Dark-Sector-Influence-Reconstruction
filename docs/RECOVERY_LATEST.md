# DSIR RECOVERY LATEST — live pointer

**Updated:** 2026-08-30 Helsinki local date.  
**Strict Article-3 scientific repository readiness:** **52%**.

**Stable historical manual:** `docs/RECOVERY_MANUAL.md`

**Current detailed checkpoint:**
`recovery/2026-08-30_article3_exp073z2_radial_pass_angular_frontier.md`

## Current headline state

- Exp073R1 v0.8 genuine hosted source-mask reproduction: **PASS**.
- Exp073P v0.5 hosted prerequisite receipt: **PASS**.
- Exp073U immutable 1410-row observation skeleton: **PASS / non-classifying**.
- Exp073V broad-row support schema: **PASS / non-classifying**, 19/19 controls.
- Exp073W BOSS current-k compatibility: **PASS / non-classifying**; historical/current lower-k conventions give the same `54/240` retained BOSS mask.
- Exp073Y exact DES released n(z) inventory: **PASS / non-classifying**.
- Exp073Z v0.1: **NUMERICAL IMPLEMENTATION FAILURE, NOT SCIENCE**; no support result was produced.
- Exp073Z2 stable-direct DES radial authority: **PASS / non-classifying**.
- Exp073X exact `nside=4096` Wm_S0 NaMaster repeatability pilot: **IN PROGRESS** at this pointer update.
- Exp073AA generic exact angular task runner: preregistration + implementation **FROZEN BEFORE Exp073X OUTPUT**; production trigger not yet authorized.
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
- no covariance, whitening, nuisance SVD/rank, quotient/relation/null or G8 information during support selection.

## Exact newest authority — Exp073Z2

Prospective stable-direct repair after the non-scientific Exp073Z numerical failure:

- prereg commit `1bca74786885ec6f4af3496f5446cfc2bf4c5ced`;
- implementation commit `92a204e96f5008683684b849c85fdeeaf14c4e70`;
- workflow commit `56d0be58a8a9830624346438aa9c04e9803d956a`;
- workflow-freeze commit `30a78013bc1c1807977e57a2d826e26ebfb1fdec`;
- trigger/head `530da3c2c9aef9e8308086df24c10abb3e06ed4f`;
- run `33279208949`;
- job `99171355322`;
- artifact `9722468056`;
- artifact digest `sha256:3eb8b025711e8df6d5452a3a57002f36c9d7de2b9116734b71d15d6822dd20be`;
- internal JSON SHA256 `3cb25beed23193a94e10d590296349713d1d83f92771215b72c10ea2e6f82c1a`;
- token `PASS_EXP073Z2_DES_RADIAL_KERNEL_STABLE_DIRECT_V0_2`.

Key numerical checks:

- no negative clipping; fine/coarse minimum source efficiency `g=0`;
- direct-vs-independent reverse-tail identity error `3.36e-16 .. 6.79e-16` relative;
- Wm coarse/fine max relative normalization delta `2.3576587734425064e-4`;
- WW max `1.1587446957811764e-4`;
- frozen tolerance is `5e-4`.

Canonical fine arrays:

- `chi_Mpc`: `e1f9a72fbe35140b984a56fc9e3b6f659082de9f9b45fc1a2e7e557e30783987`;
- `H`: `b782612550debe3363211260870b7a0a59988e4eee784bbb699ec8bb1afd112f`;
- source `g`: `a9b7b1b8c3e3f9f926e2d7786b13490109caf0aeff359dd3230f924955efd2ac`;
- 20 Wm radial kernels: `414f47620071c1df6c23abe25d45312796af53a37102c34e1d844308d915efe1`;
- 10 WW radial kernels: `56edaaf9ef6b03d00e7b83f158b204fc27171bef34a6a7bf3afbd8c71ed5cc0e`.

## Exact angular frontier

Pinned Cosmotheka confirms the source mask is the selected-object **count map**, not binary occupancy, and the lens mask is the public redMaGiC HEALPix mask with original weights retained only for `mask>0.5`.

Frozen 14-task manifest commit:
`d99f1af2edd4f0b2b1c6286124b0c0b4c1c4bd76`.

Prospective Exp073X Wm_S0 reuse rule, frozen while X was still in progress:
`ffdaf0255ccd9cc78b9eef585f6c16931d41be6b`.

If X PASSes, its first exact Wm_S0 workspace becomes production task Wm_S0 and production computes only the remaining 13 unique workspaces. If X does not PASS, reuse is forbidden.

Exp073AA production executor was also frozen before X output:

- prereg commit `14b79794ab5dc1b8cc8a0fa769ab50cac99f45d9`;
- implementation commit `45ed8d8d1e90cdaf314e0384b6f3cdfef369925b`.

Do **not** create/trigger the final 13-task production workflow until exact Exp073X PASS artifact identity is available and bound.

## Exp073X currently running

- run `33277263287`;
- job `99166064222`;
- trigger/head `62c66faec2123a05a2a8bc83b34a758737b33539`;
- setup, NaMaster 2.7, R1 authority, public lens-mask authority and runner-memory inventory passed;
- current step at pointer update: computing exact Wm_S0 TE<-TE workspace twice;
- no support/science output exists yet.

## Authorized order from here

`Exp073X exact Wm_S0 pilot`

`-> bind exact PASS artifact`

`-> freeze + trigger Exp073AA 13-task parallel angular production`

`-> join X Wm_S0 + 13 task outputs into ordered 14-window authority`

`-> join 14 angular windows + Exp073Z2 radial authority + Exp073W BOSS into immutable full pre-support finite-operator candidate manifest`

`-> real Layer A broad support`

`-> freeze S_op in inherited Exp073U order`

`-> real Layer B common-response validity`

`-> only after Layer A + Layer B PASS: covariance restriction/Cholesky whitening`

`-> nuisance tangent SVD/rank -> signed quotient/relation/null -> fresh G8`.

## Recovery read order

1. `docs/RECOVERY_MANUAL.md`
2. `docs/RECOVERY_LATEST.md`
3. `recovery/2026-08-30_article3_exp073z2_radial_pass_angular_frontier.md`
4. `docs/ARTICLE3_DES_ANGULAR_14_TASK_MANIFEST_2026-08-30.md`
5. `docs/ARTICLE3_DES_ANGULAR_EXP073X_PILOT_REUSE_AMENDMENT_2026-08-30.md`
6. `experiments/073aa_article3_des_angular_task_runner_v0_1_prereg.md`
7. `ci/exp073aa_article3_des_angular_task_runner_v0_1.py`
8. `experiments/073z2_article3_des_radial_kernel_stable_direct_v0_2_prereg.md`
9. `ci/exp073z2_article3_des_radial_kernel_stable_direct_v0_2.py`
10. `recovery/2026-08-30_article3_exp073v_broad_row_schema_pass.md`

DSIR remains independent of RTK and RQIR. Preserve scientific FAILs, numerical implementation failures, infrastructure failures, provenance failures and PASSes as distinct categories.
