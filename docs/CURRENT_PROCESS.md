# DSIR current-process ledger

Updated: 2026-09-14. Scope: **DSIR only**; RTK/RQIR/KMQGB/KMDSB excluded.

## Current authoritative frontier — V0.14 terminal

Terminal authority: `docs/dsir4/authority/LAYERB_BETA_SAME_RUN_SOLVER_DETERMINISM_V0_14.json`, creation commit `1a752a42223043b6efed79dd1294406532d2b48e`.

Run `34787822995`, head `e02c2645ce5c74d23145bb2e8d9735695583c448`; invariant, all four frozen grid/profile lanes and decision are terminal `success`. Decision job `103810023014`; decision artifact `10327458719`, SHA256 `12e9ea528dfbb12d2041ae927be6f551e84abff8478c74e19508e7b5e3345576`.

Classification: `SAME_RUN_REPEATED_SOLVER_DETERMINISM_SUPPORTED`, effect `+0/+0`.

All exact V0.13 diagnostic cells are stable across three sequential identical repeats inside one hosted runner/process in both `PURE_PAIR` and `INTERLEAVED` profiles. Every within-profile repeat spread is `0.0`; anchors pass; all values are finite; max requested-node mismatch `1.6527975532062504e-16`.

Therefore the V0.13 cross-job numerical spread is not reproduced as a same-run solver/process-state defect at the unchanged `<1e-5` threshold. The remaining blocker is scoped to cross-job/runner/environment variation. This result is reproducibility-localization only and does not validate Layer-B science or any physical dark-sector signal.

## Authorized successor

V0.14 authorizes exactly:

`PROSPECTIVELY_FROZEN_CROSS_HOST_ENVIRONMENT_FINGERPRINT_REPRODUCIBILITY_AUDIT`.

The next gate must be prospectively frozen before new substantive compute and must preserve the exact diagnostic cells, technical threshold, TOL300, production h/sampling, CLASS commit and source/extraction identities.

High-information design: independent GitHub-hosted jobs should record a normalized host fingerprint built from stable hardware/software fields (runner OS/arch, image version, kernel, CPU vendor/family/model/stepping/microcode/model name, glibc, compiler/Fortran, Python/NumPy/SciPy/BLAS identities) while excluding ephemeral runner/job IDs and dynamic CPU MHz from the scientific fingerprint. The frozen classifier must distinguish:

- cross-job responses reproducibly stratified by recorded fingerprint;
- variation persisting among jobs with the same recorded fingerprint;
- V0.13 cross-job variation not reproduced;
- mixed/underpowered fingerprint evidence;
- invariant/control failure -> inconclusive.

## Frozen boundaries

Production `h=1e-4`; scientific response threshold `<1e-3`; replay/determinism threshold `<1e-5`; production sampling `0.00035`; `tol_perturb_integration=1e-12`; exact binding `<=1e-12`. No full 107-row Layer-B traversal, covariance/whitening/nuisance/relation-null, `Wm_S3`, global 65537 or science gate is authorized.

Frozen readiness remains `ARTICLE3_REPOSITORY_READINESS: 68%` and scientific frontier `67%`; numerical reproducibility work changes neither by itself.

## Anti-duplication

Do not rerun V0.14. Open only one prospectively frozen cross-host fingerprint gate from the terminal V0.14 authority. If such a gate is already active on current main/Actions, do not duplicate it.
