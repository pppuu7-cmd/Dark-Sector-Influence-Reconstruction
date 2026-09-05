# DSIR immutable recovery — Exp073DX complete; Exp073DY solver-backend diagnostic activated

Date: 2026-09-05
Scope: DSIR only. RTK/RQIR excluded.

## Preserved heavy authority
Exp073DT attempt 4 remains the sole authoritative self-hosted WW_S0_S0 process: run `33940588308`, hosted preflight `101288015425` SUCCESS, home science job `101288014666` QUEUED at this reconciliation. Frozen head `c450aef42d96eb0bfe0b4c78d5a0fdc850d9a2cd`; durable root `$HOME/.cache/dsir/exp073dt-ww-s0-s0-ab-v0-1`; DSIR-HOME-PC remains reserved. No competing self-hosted work was launched.

## Exp073DX terminal diagnostic
Run/job `33967888245 / 101311110512` completed SUCCESS. Raw log emitted `COMPLETE_EXP073DX_WW_CROSSFIELD_MCM_STORAGE_ORIENTATION_AUDIT_V0_1` with `classification=DIAGNOSTIC_COMPLETE`, `science_gate_scored=false`, `ww_authority_created=false`, accounting `+0/+0`.

Artifact `9970022236`, GitHub SHA256 `de883a5bb915c26573e4fb8efe6913dad80638f13b188b6e7a9aef82fc6f02c8`.

Frozen observations:
- W00 raw FITS WSP_PRIMARY equals official reloaded logical matrix exactly; transpose does not.
- W01 raw equals official reloaded logical matrix exactly; transpose does not.
- W10 raw equals official reloaded logical matrix exactly; transpose does not.
- W11 raw equals official reloaded logical matrix exactly; transpose does not.
- W01 equals W10 exactly; W01 does not equal W10 transpose.

Therefore the Exp073DU/Exp073DW exact cross-adapter mismatch is not explained by FITS storage orientation or transpose handling. This is diagnostic support only `+0/+0` and changes no scientific authority.

## Exp073DY prospective diagnostic
Preregistered before output in `experiments/073dy_ww_crossfield_solver_backend_diagnostic_v0_1_prereg.md`, prereg blob `7e23a1daf217c50d4506594c9b5b754350ae19fb`, prereg commit `98df7a122ee7450de1374bcf881ff3105e67f024`.
Implementation `ci/exp073dy_ww_crossfield_solver_backend_diagnostic_v0_1.py`, blob `25a196f298d5d030a0d303162e780e1d50936157`, commit `a2836bda48c10a55da828a73d5b63efffef66343`.
Workflow added commit `5513b96826b48ec18ef4664bf51e38f766d7ab30` and activated by research-log head `18316043727cace7749e92b4c069f7921cc93624`.

Hosted run `33970593677`, job `101318281168`, was QUEUED at dispatch. It compares official reloaded PyMaster 2.7 bandpower windows to the workspace's own `_bin_mcm` products reconstructed by official `np.linalg.inv` + `np.dot`, diagnostic `np.linalg.solve`, and the frozen GSL production-adapter downstream path. Classification is frozen as `SOLVER_BACKEND_LOCALIZED` only if rebuilt binned MCM and official inv+dot are bitwise exact while the adapter is not; otherwise `POSTPROC_RECONSTRUCTION_NOT_LOCALIZED`. No tolerance rescue and no WW authority.

## Exact next actions
1. Consume Exp073DY immediately when terminal; inspect raw log and artifact, not workflow conclusion alone.
2. If `SOLVER_BACKEND_LOCALIZED`, prospectively design an exact cross-workspace adapter preserving official PyMaster 2.7 post-processing arithmetic/backend semantics; do not modify DU/DW history.
3. If not localized, freeze a narrower post-processing diagnostic before testing any new candidate.
4. Keep Exp073DT attempt 4 as sole self-hosted owner. When terminal, consume raw DT artifact and then required Exp073EB checkpoint-provenance closure before any WW_S0_S0 authority.
