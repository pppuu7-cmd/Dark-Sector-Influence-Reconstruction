# DSIR current-process ledger

Updated: 2026-09-14. Scope: **DSIR only**; RTK/RQIR/KMQGB/KMDSB excluded.

## Current authoritative frontier — V0.13 terminal

Terminal authority: `docs/dsir4/authority/LAYERB_BETA_REPLAY_SEQUENCING_V0_13.json`, creation commit `e62158ab101f3da7ff334d39afbfd75520a82699`.

Run `34773514342`, head `7c0a10a24f38966f830b7fc2438d8c134e6b5853`; all 12 profile lanes, invariant and decision completed successfully. Decision job `103769308584`; decision artifact `10322573705`, digest `sha256:b04db83d530c36e03f2b80ad33fb4be80747817bd08cb2b001d5c8c6375fd202`.

Classification: `HOSTED_RUN_REPLAY_NONDETERMINISM_SUPPORTED`, effect `+0/+0`.

The three frozen replay-failure cells show same-profile independent hosted-job spreads `1.5506392790000525e-4`, `2.4934371090895516e-5`, and `1.0478978062540487e-5`, all at/above the unchanged technical replay threshold `1e-5`. Both anchors remain valid (`0` and `1.0945880590564914e-6`). The failure cells switch between parent-like and V0.12-like values.

This is a reproducibility diagnosis, not Layer-B science. It does not show a dark-sector effect, does not validate the full response object, and does not open covariance/whitening/nuisance/relation-null, `Wm_S3`, global 65537, or full 107-row traversal.

## Authorized successor

V0.13 authorizes exactly:

`PROSPECTIVELY_FROZEN_SAME_RUN_REPEATED_SOLVER_DETERMINISM_AUDIT`.

The successor must test repeated **identical** solver constructions within one hosted run/process on the same diagnostic cells. Cross-profile differences must not be counted as repeat nondeterminism. The immutable `<1e-5` threshold, production `h`, sampling, TOL300, grids, CLASS commit, baseline/precision identities and source extraction code remain frozen.

Prospective classifier must distinguish at minimum:

- same-run repeated-solver nondeterminism supported;
- same-run repeated-solver determinism supported, implying V0.13 variability is cross-job/runner scoped;
- invariant/control failure -> inconclusive/no promotion.

## Closed parent — V0.12 interpolation audit

Authority `docs/dsir4/authority/LAYERB_BETA_PRODUCTION_H_COMMON_GRID_INTERPOLATION_V0_12.json`; run `34749034836`; classification `PRODUCTION_H_COMMON_GRID_INTERPOLATION_AUDIT_INCONCLUSIVE`, effect `+0/+0`. Cubic interpolation was supported at all three actual offending cells, but replay-invariant failure prevented promotion.

## Frozen boundaries

Production `h=1e-4`; scientific response threshold `<1e-3`; technical replay/determinism threshold `<1e-5`; production sampling `0.00035`; stabilized `tol_perturb_integration=1e-12`; exact requested-node binding `<=1e-12`. No full 107-row Layer-B traversal, covariance/whitening/nuisance/relation-null, `Wm_S3`, global 65537 or science gate is authorized.

## Recovery/readiness

Frozen readiness remains `ARTICLE3_REPOSITORY_READINESS: 68%` and funnel-freeze/scientific frontier `67%`; numerical diagnostic progress alone does not raise either value. Article-II real G5 ACT×unWISE remains a separate unresolved publication gate.
