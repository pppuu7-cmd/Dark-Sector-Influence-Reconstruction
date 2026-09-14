# DSIR current-process ledger

Updated: 2026-09-14. Scope: **DSIR only**; RTK/RQIR/KMQGB/KMDSB excluded.

## Closed numerical-runtime chain through V0.23

V0.18R/V0.19 false-invalid intervention outcomes were traced to the wrong NumPy validation observable: raw non-dispatch AVX-512 `__cpu_features__` bits were incorrectly treated as runtime-dispatch state. V0.19D diagnosed the defect; V0.20 response-free validated the correct NumPy 1.26.4 mask; V0.21 causally established `NUMPY_AVX512_DISPATCH_INTERVENTION_SUPPORTED`.

V0.22 terminal authority: `docs/dsir4/authority/LAYERB_BETA_FORCED_BASELINE_CROSS_HOST_REPRODUCIBILITY_V0_22.json`, creation commit `2b3cb46863fb85e6456a5a11e30183acf3b6de10`. Classification `FORCED_NUMPY_BASELINE_CROSS_HOST_REPRODUCIBILITY_SUPPORTED`, effect `+0/+0`. All 32 hosted lanes were eligible; the forced NumPy non-AVX512 baseline collapsed the frozen witness cross-host branch to zero spread across both native dispatch classes.

V0.23 terminal authority: `docs/dsir4/authority/LAYERB_BETA_FORCED_BASELINE_PRODUCTION_H_REPLAY_REVALIDATION_V0_23.json`, creation commit `2aa8ff62a47c1aa367f102032bdb7b2267a9fa94`.
Run `34878651714` terminal success; invariant job `104092079570`; decision job `104107495389`; decision artifact `10364150389`; digest `sha256:f787799c177bba95e0630206108a1448169b6e76b17a36b20f4439f7b58a17cd`.
Classification `FORCED_NUMPY_BASELINE_PRODUCTION_H_REPLAY_REVALIDATED`, effect `+0/+0`.
All 32 candidate lanes were eligible. Native classes: 12 AVX512-active / 20 AVX512-inactive. The complete frozen V0.12 production-h pure-common-grid replay object (five grids × three targets = 15 cells at `h=1e-4`) passed: every cell had cross-host maximum pairwise relative spread `0.0` and native-class mean separation `0.0`. Both original V0.13 production-h replay failures were repaired. Maximum requested-node coordinate mismatch was `1.6564666256119906e-16`, below the frozen `1e-12` binding tolerance. Binary and software control key counts were both one.

This closes the original production-h hosted replay reproducibility blocker for the exact 15-cell V0.12 production-h object under the validated forced NumPy baseline. It does **not** by itself re-establish the V0.12 interpolation-mechanism conclusion, validate the full two-h 30-cell V0.12 object, validate full Layer-B, or establish dark-sector evidence.

A workflow-hardening omission was found outcome-blind during V0.23: `replay-lane` lacked an explicit YAML `needs: invariant-audit` edge. In the actual authoritative run the invariant completed successfully before any substantive lane execution began, so V0.23 is retained. Every successor substantive workflow must include an explicit invariant-to-substantive DAG dependency.

## Authorized next stage

V0.23 authorizes exactly:
`PROSPECTIVELY_FROZEN_FORCED_BASELINE_PRODUCTION_H_COMMON_GRID_INTERPOLATION_REASSESSMENT_AUDIT`.

The reassessment must be prospectively frozen before substantive execution, must preserve the exact V0.12 interpolation object/thresholds relevant to the reassessment, must force and response-free validate the V0.20 NumPy baseline before substantive solves, and must not silently import historical unforced numerical branches as PASS/FAIL references where runtime branch identity is ambiguous.

## Frozen boundaries

Production `h=1e-4`; five-h ladder `[4e-4,2e-4,1e-4,5e-5,2.5e-5]`; scientific response threshold `<1e-3`; technical replay/intervention/reproducibility threshold `<1e-5`; exact binding `<=1e-12`; native `k_per_decade_for_pk=20`; production sampling `0.00035`; `tol_perturb_integration=1e-12`. Full 107-row Layer-B, covariance, whitening, nuisance, relation-null, `Wm_S3`, global 65537 and all physical-science gates remain closed. Frozen readiness remains `ARTICLE3_REPOSITORY_READINESS: 68%`; scientific frontier `67%`.
