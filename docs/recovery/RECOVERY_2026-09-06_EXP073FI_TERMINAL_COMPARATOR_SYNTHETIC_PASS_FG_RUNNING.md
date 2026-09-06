# DSIR immutable recovery — Exp073FI terminal comparator synthetic PASS while Exp073FG runs

Date: 2026-09-06. Scope: DSIR only. Never mix RTK/RQIR.

## Live authority reconciliation

Repository `docs/RECOVERY_LATEST.md` remains the scientific source of truth. Admitted `WW_S0_S0`, `WW_S0_S1`, and `WW_S0_S2` authorities remain preserved. Current scientific frontier remains `WW_S0_S3 / Exp073FG`.

Authoritative heavy run: workflow `34034377795`, head `4a02952ee3bcb368a088d87608f61243cd9f7056`; hosted lineage job `101489652912` SUCCESS; hosted code/checkpoint job `101489652945` SUCCESS; home science job `101489679508` IN_PROGRESS on `DSIR-HOME-PC` in frozen `S0->S3` A/B science. Durable checkpoint stage remains `UNKNOWN_NOT_INSPECTED_WHILE_RUNNING`; no partial numerical output was inspected and no competing self-hosted run was launched. Live queued DSIR runs: 0.

## Exp073FI terminal support result

Hosted workflow `34034555778`, job `101490139309`, head `e7159f685f8e848a27bd41e1db9a1f95076d36bb` completed SUCCESS. Raw job log, not workflow status alone, contains exact token:

`PASS_EXP073FI_EXP073FG_TERMINAL_COMPARE_SYNTHETIC_HARDENING_V0_1`

and exact classifications:

`classification=SUPPORT_PLUS_0_PLUS_0`

`ww_s0_s3_authority_created=false`

Frozen comparator blob checked by the workflow: `ci/exp073fg_compare_terminal_receipts_v0_1.py` = `74a1a2f8d3b44eaab66e834d69156e1810b75a8e`.
Synthetic audit blob: `ci/exp073fi_synthetic_test_exp073fg_terminal_compare_v0_1.py` = `3823687f61cd04489431e3d480c2fae8805bac0d`.

The hosted audit compiled both files, explicitly rejected `np.allclose`, `np.isclose`, rounding/smoothing/averaging rescue patterns, installed only the synthetic-test dependency NumPy, then verified exact PASS, one-ULP exact FAIL, and tamper rejection. This is support/governance evidence only: +0/+0, no scientific scoring and no WW authority.

## Next exact action

Do not duplicate Exp073FG while `101489679508` remains queued/in-progress. On terminal Exp073FG, consume raw compact evidence/artifact, independently verify ZIP SHA256, complete six-stage/prune provenance, source/contract/R1/driver/patch identities, mmap proof, canonical `<f8 [39,12288]` `EE<-EE`, exact A/B SHA and `numpy.array_equal`, finiteness, and no rescue. Candidate PASS still requires a separate prospectively frozen provenance-admission gate before `WW_S0_S3` authority can be created. Exact mismatch is a scientific FAIL; malformed/checkpoint/provenance failure is infrastructure/provenance +0/+0 with smallest-causal repair.
