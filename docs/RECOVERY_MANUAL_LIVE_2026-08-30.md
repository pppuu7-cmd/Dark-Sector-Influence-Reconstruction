# DSIR RECOVERY MANUAL — live 2026-08-30 overlay

This file is the current-state overlay to the stable historical `docs/RECOVERY_MANUAL.md`. Read the historical manual for derivations and long-lived methodology, then this overlay and `docs/RECOVERY_LATEST.md` for the active Article-3 frontier.

## Active scientific state

Strict Article-3 scientific repository readiness: **52%**.

G7 = OPEN. G8 = OPEN. G9 = OPEN.

Covariance/whitening remains blocked until both real Layer A and real Layer B have passed under the frozen anti-leakage ordering.

No synthetic/infrastructure QA result may increase scientific readiness.

## Frozen support boundaries

- redshift support: `0.295 <= z <= 2.33`, inclusive;
- wavenumber support: `0 < k <= 0.06664762008318016 Mpc^-1`;
- Layer-A operator invalid fraction: `<= 0.05`, inclusive;
- Layer-B invalid observation-row fraction: `<= 0.05`, inclusive;
- minimum retained observation dimension: `15`;
- classifying DES angular route: `NSIDE=4096`;
- use positive absolute operator/window envelopes only for support bookkeeping; measured Wm is signed;
- no effective ell/z/k shortcut;
- no fiducial-P weighting;
- no covariance/whitening, nuisance SVD/rank, quotient/relation/null, or G8 information during support selection;
- exact-threshold numerical ambiguity must remain `numerically_unresolved`, never rounded into PASS/FAIL.

## Current authority chain

Already established non-classifying authorities include:

- Exp073R1 hosted real DES source-mask reproduction;
- Exp073U immutable 1410-row observation skeleton;
- Exp073V broad-row support schema;
- Exp073W BOSS k-compatibility authority;
- Exp073Y exact DES released n(z) inventory;
- Exp073Z2 stable-direct DES radial authority;
- Exp073AB row-to-operator mapping authority.

Exp073AD is hosted synthetic boundary-classifier QA only. It verifies that ambiguous exact-5% cases become `numerically_unresolved`; it is not a science PASS and adds zero readiness.

## Angular authority frontier

Exp073X attempted Wm_S0 exact real-DES repeatability by computing two full workspaces sequentially in one hosted job and persisting only after both. Hosted run `33277263287`, job `99166064222`, did not yield a reusable final authority. Preserve it as:

`INCOMPLETE_INFRASTRUCTURE_RESOURCE_CANCELLED_NO_AUTHORITY_REUSE`.

Do not reinterpret it as scientific FAIL and do not reuse a partial Wm_S0 calculation.

Exp073X2 is the prospectively frozen repair. It preserves the exact angular contract and changes only execution/persistence topology:

- prereg: `efe8a4e17638dfd9568fa710e24f56cd10526c6a`;
- replica code: `df2eecd73ed0d8de080348ba155a2f1a3e84d7e1`;
- aggregator code: `8ec6f94ea9ddf3cc0a4c98e5af696d28d995b2b3`;
- workflow: `a14047090d46e024965d1bd76b60830ef21616e9`;
- workflow freeze: `5bd0ba084b00d963c670db6d04b1db6ea53e8f36`;
- execution trigger/head: `2403d9680e1d08a3853084034eb2878faa52b4e0`;
- hosted run: `33300997298`.

Replica A and B must independently reconstruct masks and compute one exact `NSIDE=4096`, NaMaster-2.7, 39-band, `TE <- TE` Wm_S0 window each. Each immediately persists JSON+NPZ. The aggregator requires exact frozen-metadata equality, canonical `<f8` SHA equality, and `numpy.array_equal` before issuing the X2 non-classifying PASS token.

X2 PASS alone adds zero scientific-readiness points and leaves G7/G8/G9 open.

## Successor ordering

Do not duplicate X2 while its hosted run is active.

If and only if hosted X2 aggregator PASS exists:

1. bind the exact X2 Wm_S0 replacement authority;
2. freeze and run the remaining 13 exact DES angular tasks under the already preregistered Exp073AA task semantics;
3. join all 14 ordered angular windows;
4. join those windows with Exp073Z2 radial authority, Exp073AB mapping and Exp073W BOSS authority;
5. freeze the complete 1410-row pre-support finite-operator candidate manifest;
6. only then run real Layer A broad support;
7. freeze `S_op` in inherited Exp073U order;
8. run real Layer B common-response validity;
9. only after both support layers PASS may covariance restriction and Cholesky whitening begin;
10. nuisance tangent SVD/rank, signed quotient/relation/null and fresh G8 remain later stages.

If X2 is cancelled or fails infrastructure, preserve the exact failure class and repair infrastructure without changing the scientific/angular contract post hoc.

## Separation rule

DSIR is independent of RTK and RQIR. Do not import their theory assumptions, gates, priors, code authority, or readiness accounting into DSIR.

## Recovery read order for the active frontier

1. `docs/RECOVERY_MANUAL.md` — stable derivations and long-term rules;
2. `docs/RECOVERY_MANUAL_LIVE_2026-08-30.md` — this live overlay;
3. `docs/RECOVERY_LATEST.md` — shortest current pointer;
4. `recovery/2026-08-30_article3_exp073x_cancelled_exp073x2_split_repeatability_launched.md` — exact chronology and identifiers;
5. `experiments/073x2_article3_des_n4096_wm0_maskonly_repeatability_v0_1_prereg.md`;
6. `experiments/073x2_article3_des_n4096_wm0_maskonly_repeatability_v0_1_workflow_freeze.md`;
7. `.github/workflows/exp073x2-article3-des-n4096-wm0-maskonly-repeatability-v0-1.yml`.
