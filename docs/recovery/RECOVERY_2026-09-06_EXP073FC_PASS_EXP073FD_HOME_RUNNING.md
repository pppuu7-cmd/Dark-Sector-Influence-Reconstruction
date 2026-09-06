# DSIR recovery — Exp073FC PASS; Exp073FD audited Exp073FA home science running

Date: 2026-09-06. Scope: DSIR only; RTK/RQIR excluded.

## Preserved authority

All authority in the prior `docs/RECOVERY_LATEST.md` remains preserved. In particular `WW_S0_S0` is admitted by Exp073EO v0.2 and `WW_S0_S1` is admitted by Exp073EZ. Current frontier is only `WW_S0_S2` / Exp073FA.

## Exp073FC terminal support result

Exp073FC run/job `34018341064 / 101446155067` is terminal SUCCESS. Raw job log was consumed, not inferred from workflow status. Required token `PASS_EXP073FC_EXP073FA_COMMITTED_DRIVER_BINDING_V0_1` and `classification=SUPPORT_PLUS_0_PLUS_0` were present. This is exact implementation/governance support `+0/+0`; it creates no WW authority.

It preserves the byte-for-byte binding of committed Exp073FA drivers to the repaired Exp073FB generated artifact: driver Git blobs v0.1 `5c5d6aff574b8ed2679e345903d5f4447e5d5c18`, v0.2 `9bde1f5de584e3378a1fe365e7a9771146fe08b5`; byte SHA256s v0.1 `fe354b95e9aeefe0772f4c7eecbba6e1944fb1f4955fceb3e9e72ed1c06b293a`, v0.2 `77f321e22c923d8d5996105487cae9afb6eecc5863174d849b092164a26824ba`.

## Exp073FD prospective home envelope

A dedicated fail-closed home execution envelope was frozen after FC PASS:

- prereg `experiments/073fd_exp073fa_home_execution_envelope_v0_1_prereg.md`, Git blob `6636766b565956d6af28ae04bcdeec1a410259a1`;
- home envelope `ci/exp073fa_home_filebacked_fullres_v0_1.sh`, Git blob `309c464bbfbe4896bd560165985ee7f643d9ee22`;
- Exp073FA science prereg blob `edc044792be8ac7b796c8469943924942ae91932`;
- frozen source head `de83e20a68f79ccf25b89b0d33eb4206e294c757`;
- contract fingerprint `b7845df5ce4bc2bd730461476b7ff0831512003ceb5b3558436005c9876bd251`;
- qualified FITS-read patch blob `d534b698f9131688d263eedcef27260386c58641`;
- R1 artifact `9720335366`, digest `sha256:ff87d8fc7d53b16b786a4eb3d6ffeb103676efb8a548223a187b9f59689f8abd`;
- durable checkpoint namespaces `checkpoints/exp073fa-ww-s0-s2-a-v0-1` and `checkpoints/exp073fa-ww-s0-s2-b-v0-1`.

Frozen science is unchanged: ordered `(S0,S2)` / indices `[0,2]`; NSIDE=4096; ell 0..12287; 39 bands; public FITS reload plus `get_bandpower_windows()`; regular-file-backed unbinned MCM exactly 19,327,352,832 bytes; selected `EE<-EE <f8 [39,12288]`; exact SHA + `numpy.array_equal`; all finite; no tolerance/rounding/smoothing/averaging/manual-reconstruction rescue; six-stage durable checkpoint chain; no historical WW numerical import and no other-replica numerical output read.

## First Exp073FD attempt — infrastructure/static only

Run `34020704615`, hosted audit job `101452648911`, failed before home science was allowed. The first causal defect was transport/parsing only: the workflow saved GitHub's job-log response as `fc_logs.zip` and attempted `unzip -p`, while this endpoint delivered plain text in that execution. Home science was skipped. Classification is `INFRASTRUCTURE_STATIC_LOG_TRANSPORT_FAIL +0/+0`; no science was run and no checkpoint exists from this attempt.

Minimal repair changed only FC log transport parsing to direct textual grep (`fc_logs.txt`, `grep -aF`). Frozen science, preregistration, drivers, home envelope, source head, contract, patch, R1 authority and acceptance rules were not changed.

## Repaired authoritative process

Repaired Exp073FD workflow run `34020756634`, workflow `Exp073FD Exp073FA audited home envelope and science v0.1`, head `894885b2c2b811954d1724c2733d2a810a486d70`, branch `main`.

Hosted audit job `101452788638` is terminal SUCCESS. Its raw log was consumed and contains exactly:

- `PASS_EXP073FD_EXP073FA_HOME_ENVELOPE_STATIC_AUDIT_V0_1`;
- `classification=SUPPORT_PLUS_0_PLUS_0`;
- `ww_s0_s2_authority_created=false`.

The dependent home science job `101452805620` is currently `IN_PROGRESS` inside `Run frozen ordered S0-to-S2 A/B gate with durable checkpoints`. `DSIR-HOME-PC` is exclusively owned by this job. No competing home task is permitted.

By policy no partial numerical output is inspected while it runs. Therefore the last durable checkpoint is deliberately recorded as `UNKNOWN_NOT_INSPECTED_WHILE_RUNNING`, not guessed from partial logs. The exact candidate token remains `PASS_EXP073FA_WW_S0_S2_FILEBACKED_AB_EXACT_REPEATABILITY_V0_1`; candidate PASS alone cannot create `WW_S0_S2` authority.

## Exact next action

When `34020756634 / 101452805620` becomes terminal, consume it immediately: inspect terminal job steps/logs and compact artifact; independently verify artifact ZIP SHA256 against GitHub digest; verify source/contract/driver/patch/R1 identities; verify restored/new checkpoint provenance and both complete six-stage chains; verify 19,327,352,832-byte regular-file mmap proof; verify exact canonical A/B `EE<-EE` SHA equality, `numpy.array_equal`, finiteness and frozen token.

If candidate PASS: prospectively freeze and run a dedicated hosted provenance admission bound to the exact terminal run/job/artifact/digest; only that admission PASS may create `WW_S0_S2` authority. If exact A/B mismatch under the frozen contract: record genuine scientific FAIL and proceed only to the next prospectively allowed branch. If infrastructure/software failure: diagnose the first causal defect and resume from validated complete checkpoints without changing science or recomputing verified expensive stages.