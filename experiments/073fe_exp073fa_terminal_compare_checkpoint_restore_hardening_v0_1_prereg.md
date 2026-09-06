# Exp073FE — Exp073FA terminal-compare checkpoint/restore hardening v0.1 preregistration

Date: 2026-09-06. Scope: DSIR only; RTK/RQIR excluded.

## Motivation discovered prospectively while Exp073FA is still running

Static audit of the already-frozen Exp073FA implementation found a governance/checkpoint defect independent of any numerical result. `ci/exp073fa_home_filebacked_fullres_v0_1.sh` runs replica A, prunes superseded large payloads after `replica_receipt_complete`, runs replica B, prunes likewise, and then invokes the science driver again with `--replica AB`. The v0.1 driver's `validated_finished()` terminal restore validates only `replica_receipt.json` and the selected EE payload, then returns the terminal receipt. It does not revalidate the full ordered six-stage chain and every stage payload before that restore. The Exp073FA preregistration states that complete stages may be restored only after exact identity and payload verification.

This issue was identified before terminal Exp073FA output was inspected. It therefore cannot be used to tune or rescue any numerical result.

## Frozen classification boundary

This is an implementation/provenance issue only. It does not alter ordered `(S0,S2)`, R1 indices `[0,2]`, source head, contract fingerprint, NSIDE, ell range, banding, NaMaster arithmetic, public serialized BPW route, `EE<-EE`, canonical `<f8 [39,12288]`, exact SHA/`numpy.array_equal`, finiteness, or any acceptance threshold.

The running Exp073FA job must not be duplicated or modified in place. Its terminal artifact must still be consumed. Any completed replica/checkpoint evidence remains preservable evidence. Workflow SUCCESS or the candidate token alone cannot create authority.

## Prospective repair

The repaired terminal comparison must never call `run_replica()` or otherwise restore a completed replica merely to compare A and B. It must consume only the two completed terminal replica receipts plus their selected EE payloads and fail closed on:

- replicas exactly A and B;
- source pair exactly `S0->S2` and ordered indices exactly `[0,2]`;
- source head and contract fingerprint equal the frozen Exp073FA identities;
- dedicated checkpoint namespaces exactly `checkpoints/exp073fa-ww-s0-s2-a-v0-1` and `checkpoints/exp073fa-ww-s0-s2-b-v0-1`;
- public route exactly `public_get_bandpower_windows_after_filebacked_fits_read`;
- `same_field_object_handoff=false`;
- `historical_ww_numerical_import=false` and `other_replica_output_read=false`;
- selected payloads exactly `<f8 [39,12288]` and SHA256-equal to their receipts;
- exact A/B SHA equality and `numpy.array_equal(A,B)==true`;
- all finite;
- no tolerance, rounding, smoothing, averaging or manual-reconstruction rescue.

A separate provenance admission must additionally inspect the raw terminal artifact's complete six-stage manifest chains. This support repair by itself is `+0/+0` and can never create `WW_S0_S2` authority.

## Result handling

If the running Exp073FA artifact proves a frozen scientific mismatch, that remains a genuine scientific FAIL. If its numerical arrays match but the frozen checkpoint/provenance contract cannot be proven, classify the authority path as provenance/infrastructure `+0/+0`, preserve all valid completed evidence, and use the smallest prospective repair without recomputing a verified expensive stage unnecessarily.

Frozen support token for the repaired comparator static audit, if/when run:
`PASS_EXP073FE_EXP073FA_TERMINAL_COMPARE_RESTORE_HARDENING_V0_1`.

Status: `PREREGISTERED_WHILE_EXP073FA_RUNNING`; `ww_s0_s2_authority_created=false`.