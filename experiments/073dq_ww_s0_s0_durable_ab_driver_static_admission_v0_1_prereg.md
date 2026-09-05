# Exp073DQ — WW_S0_S0 durable A/B driver static admission v0.1

Frozen 2026-09-05 after independently validated Exp073DP exact-equivalence PASS and before any full-resolution WW_S0_S0 production output is computed.

Scope: implementation/checkpoint governance `+0/+0` only. Exp073DQ cannot create WW scientific authority and does not authorize home execution by itself.

Parent Exp073DP: repaired run/job `33938446310 / 101230897808`, head `b2dc8a395991963885d47a964d44c50c3ef2927e`, artifact `9960969007`, GitHub and independent ZIP SHA256 `e34b545b21fc93f8948ad328084afd405885c1045313d7162b553a45583af7a8`, raw token `PASS_EXP073DP_WW_EXACT_ADAPTER_SMALLNSIDE_EQUIVALENCE_V0_1`, NaMaster source commit `24365fa59a38c15732f4f37e8b29265b75c442d5`.

## Frozen full-resolution WW target

- task exactly `WW_S0_S0`;
- source authority only from Exp073R1 S0 record/count-map semantics through the already-frozen Exp073AA `validate_r1` and `source_count_map(root,0)` logic;
- no redMaGiC lens mask argument/read;
- DES NSIDE=4096, ell=0..12287, 39 frozen band edges;
- exactly one spin-2 `NmtField(source,None,spin=2)` reused as both sides of `compute_coupling_matrix(f,f,b)`;
- full stock WW component space `[4,39,4,12288]` persisted through the Exp073DO exact adapter with `ncls=4` before selecting `wins[0,:,0,:]=EE<-EE`;
- canonical selected payload `<f8 [39,12288]`, file `selected_ee.bin`;
- PyMaster lineage exactly 2.7.x; no 2.6/3.x fallback.

## Durable checkpoint contract

Independent namespaces:
- A: `checkpoints/exp073dq-ww-s0-s0-a-v0-1`
- B: `checkpoints/exp073dq-ww-s0-s0-b-v0-1`

Complete-stage order:
1. `fresh_s0_mask_complete`
2. `fresh_workspace_mcm_complete`
3. `mcm_fits_verified`
4. `full_window_complete`
5. `selected_ee_complete`
6. `replica_receipt_complete`

Every manifest must bind replica, namespace, frozen source head, contract fingerprint, payload SHA256 and `historical_ww_numerical_import=false`, `other_replica_output_read=false`. Restore must fail closed on identity, missing payload, SHA mismatch, shape/dtype mismatch or gapped stage semantics. Atomic persistence is required. A completed replica receipt may be reused only after exact receipt and selected-EE SHA verification.

A/B comparator must read only final canonical A/B `selected_ee.bin`, require exact selected SHA equality and `numpy.array_equal`, and contain no tolerance/allclose/rounding/ULP/smoothing/averaging rescue. Static admission must verify the comparator token is a provisional driver token only; later scientific activation must prospectively freeze its own authority token and workflow binding.

## Resource boundary

This preregistration does not declare resource readiness merely because the driver is syntactically valid. A later activation audit must bind the already-qualified deterministic 8-core downstream, prove actual runtime `DSIR_OMP_TEAM=8`, nested BLAS/MKL/OpenBLAS/NumExpr=1, and determine prospectively whether the full stock workspace stage can safely satisfy the repository canonical heavy-compute/checkpoint standard without changing arithmetic. If it cannot, home execution is BLOCKED pending a separately audited exact resource architecture.

## PASS token

`PASS_EXP073DQ_WW_S0_S0_DURABLE_AB_DRIVER_STATIC_ADMISSION_V0_1` is support `+0/+0` and requires a hosted source-only audit proving the exact target, dedicated stages/namespaces, fail-closed restore, no lens/Wm/TE semantics, Exp073DO adapter use with `ncls=4`, and exact A/B comparator.

PASS authorizes only the next activation/resource audit. It does not launch or authorize a self-hosted scientific run.