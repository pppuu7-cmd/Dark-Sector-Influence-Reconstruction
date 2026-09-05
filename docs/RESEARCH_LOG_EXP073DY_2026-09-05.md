# DSIR research log — Exp073DX consumption and Exp073DY activation — 2026-09-05

Scope: DSIR only; RTK/RQIR excluded.

## Exp073DX terminal consumption
Hosted run/job `33967888245 / 101311110512` completed SUCCESS. Raw job log emitted `COMPLETE_EXP073DX_WW_CROSSFIELD_MCM_STORAGE_ORIENTATION_AUDIT_V0_1` and a diagnostic-only `DIAGNOSTIC_COMPLETE +0/+0` receipt. Artifact ID `9970022236`; GitHub artifact SHA256 `de883a5bb915c26573e4fb8efe6913dad80638f13b188b6e7a9aef82fc6f02c8`.

Frozen observations: for W00, W01, W10 and W11, raw FITS `WSP_PRIMARY` is exactly `numpy.array_equal` to the official serialized→reloaded `get_coupling_matrix()` matrix. Raw transpose is not equal to logical for any case. W01 and W10 are exactly equal, while W01 is not equal to W10 transpose. Therefore the Exp073DU/Exp073DW exact adapter mismatch is not caused by FITS storage orientation or transpose handling. No WW scientific authority is created; accounting remains `+0/+0`.

## Exp073DY prospective continuation
Before any Exp073DY output, `experiments/073dy_ww_crossfield_solver_backend_diagnostic_v0_1_prereg.md` froze the next diagnostic. Exp073DY isolates the post-MCM solver/backend path by comparing the official reloaded PyMaster 2.7 bandpower windows against the workspace's own `_bin_mcm` products reconstructed with the official `np.linalg.inv` + `np.dot` algebra, a diagnostic `np.linalg.solve` alternative, and the existing frozen GSL production-adapter downstream route.

Exp073DY is hosted-only, diagnostic/support-only `+0/+0`, cannot create WW authority, and forbids tolerance/allclose/rounding/smoothing/averaging or post-hoc permutation rescue.

The authoritative heavy process remains Exp073DT attempt 4 run/job `33940588308 / 101288014666`; no competing self-hosted work is launched.
