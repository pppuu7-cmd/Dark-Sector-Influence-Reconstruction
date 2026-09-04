# Exp073DI — restored adapter runtime-provenance validation v0.1

Date: 2026-09-04. Scope: DSIR only. Support/infrastructure `+0/+0`; no Wm_S3 authority.

## Trigger
After Exp073DH closed cumulative mask/workspace lineage, the terminal launcher contract was audited for every possible interrupted stage. If `selected_te_complete` is valid but `replica_receipt_complete` is absent, the inherited production driver correctly avoids recomputing the expensive adapter, but its newly written replica receipt uses a generic restored status and does not carry `downstream_parallelism`. The frozen launcher therefore cannot prove that the already-computed full-window payload was produced by the certified 8-thread adapter.

The exact adapter itself persistently writes `exact_route/receipt.json` before the driver commits the full-window and selected-TE checkpoint manifests. That receipt contains source head, contract fingerprint, checkpoint namespace, workspace/full/selected SHA identities and the OpenMP-8 `downstream_parallelism` proof.

## Prospective minimal repair
A resume-only launcher validator may use the persisted adapter receipt as a fallback runtime-provenance source **only** when the replica receipt lacks downstream parallelism. It must independently verify all of:
- adapter receipt source head = frozen historical science head;
- contract fingerprint and checkpoint namespace equal the replica's frozen values;
- `historical_wm_s3_numerical_import` is false and `no_tolerance_rescue` is true;
- adapter workspace SHA equals the replica/workspace checkpoint SHA;
- adapter full-window SHA equals the verified `full_window_complete` payload SHA and actual file SHA;
- adapter selected-TE SHA equals the verified `selected_te_complete` payload SHA and actual file SHA;
- exact full/selected shapes remain `[2,39,2,12288]` and `[39,12288]`;
- `downstream_parallelism` is exactly workers=8, runtime_team_verified=true, scalar_accumulation_order_preserved=true.

If the persisted adapter receipt is missing or any field/hash differs, resume is fail-closed/BLOCKED; it may not infer or recreate historical runtime proof. A legacy final replica receipt that already contains valid downstream parallelism continues through the original validator without fallback.

No comparator, scientific arithmetic, data, banding, TE semantics, checkpoint boundaries or tolerance policy may change.

PASS token: `PASS_EXP073DI_RESTORED_ADAPTER_RUNTIME_PROVENANCE_V0_1`.
Only raw hosted PASS permits the self-hosted checkpoint resume orchestration.
