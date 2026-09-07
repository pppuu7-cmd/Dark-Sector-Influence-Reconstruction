# DSIR recovery — Exp073GZ hosted audit PASS / FY active V23

Date: 2026-09-08. Scope: DSIR only. Never mix RTK or RQIR.

## Preserved scientific authority

Wm_S1 Track-A exact PASS and admitted Wm_S2/Wm_S3 remain preserved. WW admitted authority remains through `S2_S2`; `WW_S2_S3` is still NOT ADMITTED.

Exp073FW final authority remains run `34146468135`, artifact `10027835016`, digest `sha256:ef36ddafc5f30d33206fbf952deea5c0f58f5465370a9c8bd96c2b2d61b1ecef`, admitted by Exp073FX job `101819621240` with `PASS_EXP073FX_WW_S2_S2_FILEBACKED_PROVENANCE_ADMISSION_V0_1`.

## Authoritative heavy process unchanged

Exp073FY namespace-repair V0.3 run `34160898921`, head `b5c8a059a014bee5d318d6067f7a2fac37c5b173`, remains the sole authoritative heavy process.

- hosted launch audit job `101862362835`: SUCCESS;
- home-science job `101862390771`: IN_PROGRESS at this reconciliation;
- invalid historical S3-S3-labelled FY checkpoint retirement: SUCCESS;
- repaired frozen `WW_S2_S3` A/B gate: IN_PROGRESS;
- runner owner: single DSIR self-hosted runner `DSIR-HOME-PC-2`;
- valid checkpoint namespace: `checkpoints/exp073fy-ww-s2-s3-{a,b}-v0-1`;
- no competing heavy run exists and none was launched;
- partial numerical output was not inspected.

Frozen FY science remains ordered `[2,3]`, distinct `S2->S3`, DES NSIDE=4096, ell `0..12287`, 39 bands, canonical `<f8 [39,12288] EE<-EE`, exact 19,327,352,832-byte file-backed MCM proof, finiteness, SHA equality and `numpy.array_equal`. Only Exp073FZ token `PASS_EXP073FZ_WW_S2_S3_FILEBACKED_PROVENANCE_ADMISSION_V0_1` may create `WW_S2_S3` authority.

## Newly consumed independent result — Exp073GZ

A repository-authored workflow was added prospectively in commit `a4961a87432f53bc55a13c7f542a8775634b90bd` at `.github/workflows/exp073gz-c2-runtime-admission-receipt-static-audit-v0-1.yml`.

GitHub Actions run `34168323933`, head `a4961a87432f53bc55a13c7f542a8775634b90bd`, completed SUCCESS. Hosted job `101883674574` raw log independently shows exact terminal token:

`PASS_EXP073GZ_C2_RUNTIME_ADMISSION_RECEIPT_CONTRACT_STATIC_AUDIT_V0_1`

The workflow verified exact frozen contract blob `1c2e30e6563efe3976ee0b1825dfb250a902a529` and its fail-closed requirements: 28 packets, z-major/k-minor ordering, 64 bytes each / 1792 aggregate bytes, raw aggregate SHA-256 before decoding or mapping, producer run/job terminal identity, artifact identity/digest when applicable, `raw_record_set_admitted`, `decoded=false`, `mapped=false`, `prediction_ready=false`, and infrastructure/`INVALID_FOR_SCIENCE` handling for invalid provenance.

Classification is exactly `SUPPORT_PLUS_0_PLUS_0`. This is not scientific PASS, does not create C2 model authority, does not decode or map runtime bytes, and does not launch CLASS or a scientific prediction.

The former `BLOCKED_BY_AUDIT_EXECUTION_PATH` status for GZ is therefore closed. The next C2 transition is a real frozen 28-packet runtime producer/admission step, but it remains BLOCKED while FY owns the only home runner; no competing home job may be launched.

## Next actions

1. Continue watching FY run `34160898921` without duplication or partial-result tuning.
2. On terminal FY, consume logs/artifacts/checkpoints against the frozen FY/FZ contract in the same iteration.
3. Only after valid FY candidate plus FZ admission may Exp073GA `WW_S3_S3` run.
4. For C2, GZ prerequisite is now PASS; real 28-packet runtime generation/admission is permitted only after heavy-run exclusivity is clear and must retain the frozen provenance/receipt contract.
