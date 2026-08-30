# DSIR recovery checkpoint — Exp073AF release-control hosted PASS, X2 still running

**Date:** 2026-08-30  
**Project:** Dark-Sector Influence Reconstruction (DSIR)

## Scientific-accounting state

- Article-2 repository-for-writing readiness: **100%** for declared scope; not G7/G8/G9 closure.
- Strict Article-3 scientific repository readiness: **52%**.
- G7/G8/G9: **OPEN**.
- Layer A/B: **OPEN**.
- covariance/whitening: **BLOCKED**.
- Exp073AE and Exp073AF are hosted synthetic/governance QA and each adds **0** scientific-readiness points.

## Chronology since the preceding checkpoint

### Recovery provenance correction

Fresh commit-log verification established that the real commit creating
`docs/DSIR_CROSS_CHAT_AUTHORITY_CONSOLIDATION_2026-08-30.md`
is:

`fcb5aa4c7081a5db698797fba2fa340e897e3b1a`.

The preceding recovery checkpoint had temporarily recorded a wrong SHA. It was corrected prospectively in-place at commit:

`35c48e16d308c3052d980441345633f5bfdbd4a6`.

No scientific result, threshold, authority selection, or readiness value changed in this provenance correction.

### Exp073AA supersession audit

The original Exp073AA preregistration predates the final Exp073X infrastructure outcome and therefore still literally says production requires the old Exp073X run `33277263287` PASS. That historical text is preserved, but it has already been superseded by:

- `docs/ARTICLE3_EXP073X2_PARALLEL_AUTHORITY_SELECTION_2026-08-30.md`;
- `docs/ARTICLE3_DES_ANGULAR_14_TASK_MANIFEST_X2_SUCCESSION_AMENDMENT_2026-08-30.md`.

To prevent accidental use of the obsolete literal prerequisite, a new non-scientific release controller was frozen before any X2 result existed.

## Exp073AF — X2 -> Exp073AA release-control gate

### Frozen chain

- preregistration `experiments/073af_article3_x2_to_exp073aa_release_control_v0_1_prereg.md`
  - commit `91e9f3f25fa34cab3a33d927d47afa10e5f1cc29`;
- implementation `ci/exp073af_article3_x2_to_exp073aa_release_control_v0_1.py`
  - commit `2d772bff1971f81b8cdc94e5e2ca0d52290bfa8d`;
- workflow `.github/workflows/exp073af-article3-x2-to-exp073aa-release-control-v0-1.yml`
  - commit `25397615a824c972330fc1a98043761991bfe744`;
- workflow freeze `experiments/073af_article3_x2_to_exp073aa_release_control_v0_1_workflow_freeze.md`
  - commit `6b503250cde5d2372a3fabcff609127c52159cf6`;
- trigger/head `ci/exp073af_article3_x2_to_exp073aa_release_control_v0_1.trigger`
  - commit `d7bbf3554b760b714ac73da45980dfe3ba3c30a5`.

All were frozen/committed while real X2 chains P and Q were still computing exact workspaces.

### Hosted synthetic authority

- run `33302029344`;
- run started `2026-08-30T08:37:10Z`;
- run completed success `2026-08-30T08:37:18Z`;
- job `99231856970`;
- artifact `9729246776`;
- artifact digest `sha256:adae6a7c4688674f41e32a0865971b1e92b5fac452371684376c07f5463b77a2`;
- required token `PASS_EXP073AF_X2_TO_EXP073AA_RELEASE_CONTROL_SYNTHETIC_V0_1`.

Classification:

`HOSTED_SYNTHETIC_PASS_NON_SCIENTIFIC_PLUS_0_READINESS`.

The hosted workflow passed prospective-freeze enforcement, Python compilation, the 18-case frozen synthetic state matrix, non-scientific accounting checks, and artifact persistence.

## Binding release rule now machine-tested

Exp073AF can release exactly the remaining 13 Exp073AA tasks only under the frozen P/Q governance:

- P PASS + Q PASS with identical canonical SHA -> release, P canonical;
- P PASS + Q infrastructure-INCOMPLETE -> release, P canonical;
- P infrastructure-INCOMPLETE + Q PASS -> release Q only as prospectively authorized fallback;
- all other tested pending/scientific-disagreement/mismatch/double-infrastructure states -> block.

Conservatively, P PASS while Q is still PENDING is blocked until Q resolves, because the already-frozen rule says a later nominal Q PASS with a different canonical hash blocks production. This prevents launching 13 expensive tasks before cross-chain consistency is known.

Released production list is exactly:

`Wm_S1, Wm_S2, Wm_S3, WW_S0_S0, WW_S0_S1, WW_S0_S2, WW_S0_S3, WW_S1_S1, WW_S1_S2, WW_S1_S3, WW_S2_S2, WW_S2_S3, WW_S3_S3`.

`Wm_S0` is excluded and can come only from the valid canonical X2 authority.

## Anti-leakage status

Exp073AF reads no real X2 receipt during hosted synthetic QA and does not read radial kernels, support, retained coordinates, fiducial P, covariance, whitening, nuisance geometry, relation/null outputs or G8. It cannot claim a scientific PASS.

## Heavy X2 state at this checkpoint

Latest job inspection still showed all four real exact replicas inside their workspace computation:

### P primary — run `33300997298`

- job A `99229007616`: exact replica computation IN PROGRESS;
- job B `99229007666`: exact replica computation IN PROGRESS.

### Q contingency/redundant — run `33301058260`

- job A `99229177604`: exact replica computation IN PROGRESS;
- job B `99229177540`: exact replica computation IN PROGRESS.

No third X2 and no Exp073AA production task was launched.

## Authorized next order

1. re-check P/Q hosted jobs and artifacts;
2. classify immutable P/Q outcomes under the already-frozen authority rule;
3. apply the now-hosted-tested Exp073AF release controller;
4. if release is authorized, execute exactly 13 remaining Exp073AA angular tasks;
5. bind canonical X2 Wm_S0 + the 13 into the ordered 14-window authority;
6. perform the strict real pre-support authority join under Exp073AE;
7. only after the complete immutable 1410-row finite-operator candidate manifest exists may real Layer A begin.

Until then Article-3 scientific readiness remains **52%**.
