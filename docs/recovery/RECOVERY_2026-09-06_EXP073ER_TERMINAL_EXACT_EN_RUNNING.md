# DSIR immutable recovery — Exp073ER terminal exact support PASS while Exp073EN remains active

Date: 2026-09-06
Scope: DSIR only; RTK/RQIR excluded.

## Authority reconciliation
Repository recovery/current-process authority was read before this note. The authoritative heavy science process remains Exp073EN network-retry v0.2 run `33994398927`, self-hosted job `101382229273`, activation head `4d1cbd504067a64a94b038292793e5e8bffba911`. At this reconciliation GitHub still reports that self-hosted job IN_PROGRESS in its frozen science step. No partial numerical output was inspected and no competing home workload was launched.

## Exp073ER terminal result
Prospective preregistration: `experiments/073er_filebacked_fits_read_public_bpw_exact_qualifier_v0_1_prereg.md`, blob `3a3642189d33a1a2185f6b3b0aad86c6870b18a2`.

Terminal hosted run/job: `33997539503 / 101390573286`.
Activation head: `b5b6d75aa569473e5e0770ba1d718f93bf286c86`.
Artifact: `9978528214`.
GitHub artifact digest: `sha256:1e0c3516de041e773eca030d9488f7af7d38455033ae5b97ba1151820eb22267`.
Independently downloaded ZIP SHA256: `1e0c3516de041e773eca030d9488f7af7d38455033ae5b97ba1151820eb22267`.
Frozen terminal token: `PASS_EXP073ER_FILEBACKED_FITS_READ_PUBLIC_BPW_EXACT_V0_1`.
Classification: `FILEBACKED_FITS_READ_PUBLIC_BPW_EXACT`.
Accounting: `+0/+0`; `science_gate_scored=false`; `ww_authority_created=false`.

The run used exact PyMaster/NaMaster 2.7 source authority and one immutable stock-constructed serialized ordered `S0 -> S1` workspace. Stock fresh reload A/B and patched file-backed fresh reload A/B all used public `NmtWorkspace.read_from(read_unbinned_MCM=True) -> get_bandpower_windows()`.

Patched reload A and B each proved an active regular-file `MAP_SHARED` backing of exactly `294912` bytes for the unbinned MCM, with cleanup complete and no surviving mmap file after destruction.

All prospectively frozen exact comparisons passed for both full BPW `[4,8,4,48]` and selected `EE<-EE [8,48]`:
- stock A == stock B;
- patched A == patched B;
- stock A == patched A;
- stock B == patched B;
- canonical SHA256 equality;
- `numpy.array_equal=true`;
- max absolute difference `0.0`;
- no tolerance/allclose/rounding/smoothing/averaging rescue.

Full BPW SHA256: `bf656c5f0493dc44d6c42b31b804f04f6893b7fc4895e92b99cefc356b10b884`.
Selected EE SHA256: `336a0b57fe734a2f17a4a0844db1a18fc43887abf7556fb63009ee4a3de5f607`.

## Scientific effect
Exp073ER is support-only and does not advance the WW science frontier by itself. It closes the specific full-resolution serialized-read RAM structural risk prospectively identified for the EK-qualified public-BPW distinct-field path: when enabled, the v0.2 storage patch can back the FITS-read unbinned MCM with a regular file without changing public BPW numerical semantics on the frozen qualifier.

This result does not alter active Exp073EN v0.1 science identity and must not be retrofitted into its running result. `WW_S0_S0` remains unadmitted until terminal Exp073EN candidate evidence is consumed and Exp073EO independently passes its six-stage provenance/admission contract.

After valid `WW_S0_S0`, the ordered `WW_S0_S1` resource/readiness path may use Exp073ER as support evidence together with the already preserved EK/EP exact-adapter/storage evidence, subject to the prospectively frozen Exp073EL gate and any explicit recovery supersession.

## Next action
1. Keep DSIR-HOME-PC exclusively owned by Exp073EN `33994398927 / 101382229273` while it is active.
2. On terminal Exp073EN, consume raw artifact/digest/identities/mmap/A-B/token before any science classification.
3. On candidate PASS, activate only preregistered Exp073EO; EO PASS is required to admit `WW_S0_S0`.
4. Do not launch Exp073EL or ordered WW cross science before valid `WW_S0_S0` authority and home-runner availability.
