# DSIR research checkpoint — Exp069B FAIL — 2026-08-26

Exp069B is permanently recorded as `FAIL_C5_EXPLICIT_EFT_PYTHON_POWER_BRIDGE_V0_1`.

Run: `33012245685`; job: `98321238662`; artifact: `9623153120`; artifact ZIP SHA256: `8d26cf91a7ccb6923a5a7bbb15b78fb3bd3a818f6a9bb6bfb197be460d818688`; preregistration commit: `9c0c3d990367bfe8663e25a187e2a71d33134a83`.

## What Exp069B resolved

Unlike Exp069A, the corrective Python path demonstrably activates the pinned designer EFT state. For every designer point the frozen checks read back `EFTflag=3`, `DesignerEFTmodel=1`, `EFTCAMB_model_is_designer=true`, `model_name='Designer f(R)'`, the requested `EFTB0`, and `EFTCAMB_skip_stability=false`. The pinned `CAMBdata_SetParams` source runs `EFTCAMB_Stability_Check` when stability is not skipped, and all solver calls completed normally.

Production nondegeneracy also passed decisively. The maximum absolute log responses grow from about `1.316e-2` at `B0=1e-6` to about `3.699e-1` at `B0=1e-3`, so the no-op EFT mechanism that invalidated Exp069A is removed.

Physical-unit roundtrip, finite signed direct `P_mm/P_Wm/P_WW`, signed single-mode coherence, and the missing-k^2 negative control all pass.

## Why Exp069B still fails

The only failed hard test is the preregistered exact designer `B0=0` versus standard-GR limit, threshold `5e-6`:

- `P_mm`: `5.306426059592383e-6`;
- `P_Wm`: `5.289846757230358e-6`;
- `P_WW`: `5.3517542934318244e-6`.

All three are only modestly above the frozen threshold, but the threshold is binding. It is not relaxed or reinterpreted after output.

The similar fractional discrepancy in all three blocks suggests a common normalization/background/zero-limit numerical mechanism rather than a failed Weyl sign or cross-spectrum convention. This is only a diagnostic hypothesis; no corrective C5 PASS is claimed.

## Required next C5 work

Before any Exp069C-style corrective experiment, perform a mechanism audit that is descriptive and does not alter Exp069B:

1. localize the B5 residual over the frozen `(z,k)` grid for all three blocks;
2. inspect whether the residual is nearly common-mode or concentrated in specific cells;
3. compare the explicitly initialized designer `B0=0` state with prior pinned native-executable designer-zero and standard-GR controls;
4. audit precision/default differences capable of producing a few-parts-in-10^6 offset;
5. use existing historical exact-B0/GR-limit experiments before introducing any new threshold or solver setting.

A future corrective experiment may change only a mechanism justified by this audit and must be preregistered before new evaluable output. Simply loosening `5e-6` is prohibited.

## Parallel G7 path

C3/GDM remains an independent required provider bridge. Its read-only `D_m` source audit is now canonical, and Exp070A is prospectively preregistered before patch execution. Advancing C3 does not depend on making Exp069B pass.

Top-level state remains G7/G8/G9 OPEN. The sequence remains physical provider bridges -> common ACT physical-support mask -> covariance restriction/re-whitening -> nuisance SVD -> quotient/training law/null control -> fresh G8 withheld family.
