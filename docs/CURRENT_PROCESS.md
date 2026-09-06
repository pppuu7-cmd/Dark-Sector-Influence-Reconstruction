# DSIR current-process ledger

Updated: 2026-09-06. Scope: DSIR only; RTK/RQIR excluded.

## Preserved authority

Wm_S1 Track-A exact PASS and admitted Wm_S2/Wm_S3 PASS remain preserved. `WW_S0_S0` remains admitted by Exp073EO v0.2 `34005373819 / 101411448176`. `WW_S0_S1` remains admitted by Exp073EZ `34017921734 / 101444964371`, token `PASS_EXP073EZ_WW_S0_S1_FILEBACKED_PROVENANCE_ADMISSION_V0_1`.

## Frontier

`WW_S0_S2`, frozen as Exp073FA, prereg blob `edc044792be8ac7b796c8469943924942ae91932`; ordered `(S0,S2)`, R1 indices `[0,2]`; source head `de83e20a68f79ccf25b89b0d33eb4206e294c757`; contract `b7845df5ce4bc2bd730461476b7ff0831512003ceb5b3558436005c9876bd251`; durable namespaces `checkpoints/exp073fa-ww-s0-s2-a-v0-1` and `checkpoints/exp073fa-ww-s0-s2-b-v0-1`; exact candidate token `PASS_EXP073FA_WW_S0_S2_FILEBACKED_AB_EXACT_REPEATABILITY_V0_1`. Candidate alone never creates authority.

## Authoritative current science process — Exp073FD / Exp073FA

- run **`34020756634`**;
- hosted audit job **`101452788638`** = terminal SUCCESS `+0/+0`;
- home science job **`101452805620`** = **IN_PROGRESS** inside the frozen S0-to-S2 A/B step;
- branch `main`, head **`894885b2c2b811954d1724c2733d2a810a486d70`**, start `2026-09-06T08:02:37Z`;
- checkpoint namespaces `checkpoints/exp073fa-ww-s0-s2-a-v0-1`, `checkpoints/exp073fa-ww-s0-s2-b-v0-1`;
- last durable checkpoint **`UNKNOWN_NOT_INSPECTED_WHILE_RUNNING`** by anti-bias policy.

**Runner ownership:** `DSIR-HOME-PC` is exclusively owned by job `101452805620`; no competing self-hosted DSIR task may launch. Live Actions reconciliation in the current iteration found exactly one in-progress run (`34020756634`) and zero queued runs.

## Exp073FE — restore-hardening support CLOSED

Before any terminal Exp073FA numerical output was inspected, static audit found that the wrapper's final `--replica AB` invocation re-enters `validated_finished()`, whose terminal restore checks only the terminal receipt and selected EE payload, not the complete six-stage chain/all prior payloads required by the Exp073FA checkpoint contract. This is implementation/provenance only and does not change frozen science.

Prospective hardening prereg blob `43ff6dfe8d1eb682202b142e6ed2408a4beb00f7`; terminal-receipt comparator blob `14841dc412d3989e6f86294072479424f26cec93`.

First Exp073FE hosted audit `34023253707 / 101459598645` remains immutable **INFRASTRUCTURE_DEPENDENCY_FAIL +0/+0** because the hosted image lacked NumPy before comparator testing. Minimal repair changed only the hosted audit environment.

Repaired Exp073FE **`34023325339 / 101459798149`** is terminal raw-verified exact support PASS `+0/+0`. Raw log contains `PASS_EXP073FE_EXP073FA_TERMINAL_COMPARE_RESTORE_HARDENING_V0_1`, `classification=SUPPORT_PLUS_0_PLUS_0`, `ww_s0_s2_authority_created=false`. Synthetic audit verifies exact PASS for identical arrays, exact scientific FAIL after a one-ULP mismatch, and fail-closed rejection of receipt tampering. No WW authority was created.

## Exp073FF — provenance admission prospectively frozen

While Exp073FA remains IN_PROGRESS and without reading any partial numerical output, the next authority-writing gate has been preregistered as `experiments/073ff_ww_s0_s2_filebacked_checkpoint_provenance_admission_v0_1_prereg.md`, blob `c6f1fd11c4a0dc68bb17669a58854979fe84869e`, creation commit `2e3425cae2d564bf368417123af48b2662730557`.

Exp073FF is **PREREGISTERED_NOT_ACTIVATED**. It deliberately leaves the future Exp073FA terminal artifact ID and digest unknown until terminal consumption. It preserves exact `(S0,S2)`, `[0,2]`, source/contract identities, both six-stage chains, `19,327,352,832`-byte file-backed MCM, canonical `<f8 [39,12288]` `EE<-EE`, exact SHA + `numpy.array_equal`, finiteness, Exp073FE restore-hardening provenance, and forbids tolerance/alternative-path rescue. Only exact token `PASS_EXP073FF_WW_S0_S2_FILEBACKED_PROVENANCE_ADMISSION_V0_1` may create `WW_S0_S2` authority.

On terminal Exp073FA: consume raw artifact/digest/provenance/checkpoint identities and exact A/B result. Exact mismatch remains scientific FAIL. A numerical match remains non-authoritative; if the complete checkpoint/provenance contract cannot be proven, classify provenance/infrastructure `+0/+0`, preserve valid evidence, and use the smallest repair. Only after independent ZIP SHA256 and full frozen checks may Exp073FF be activated.

Frozen global boundaries remain unchanged: `0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `<=0.05`; Layer-B `<=0.05`; retained dimension `>=15`; NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; exact-threshold ambiguity `numerically_unresolved`; no tolerance/rounding/smoothing/averaging/effective-coordinate/fiducial rescue.