# DSIR RECOVERY LATEST — authoritative live pointer

**Updated:** 2026-09-06
**Scope:** DSIR only; RTK/RQIR excluded.

Repository state, immutable recovery notes, validated Actions raw logs/artifacts and durable checkpoints outrank chat wording. Historical outcomes remain immutable. Frozen science boundaries remain unchanged.

## Preserved scientific authority
Wm_S1 Track-A exact PASS, admitted Wm_S2 and Wm_S3 exact scientific PASS remain preserved. Historical Exp073CM resource/performance FAIL `+0/+0`, Exp073BU runner-loss infrastructure `+0/+0`, and Exp073DT attempts 1–5 infrastructure/resource outcomes remain historical. Current scientific target remains `WW_S0_S0`.

Frozen frontier: `Wm_S1 -> Wm_S2 -> Wm_S3 -> WW_S0_S0 -> WW_S0_S1 -> WW_S0_S2 -> WW_S0_S3 -> WW_S1_S1 -> WW_S1_S2 -> WW_S1_S3 -> WW_S2_S2 -> WW_S2_S3 -> WW_S3_S3`.

## Exp073DT attempt 5 — terminal manual resource-safety cancellation, no science classification
Run `33940588308`, attempt 5; hosted preflight job `101374977192` SUCCESS; self-hosted science job `101374976626` terminal `failure` because the full science step was manually cancelled for resource safety. Frozen head `c450aef42d96eb0bfe0b4c78d5a0fdc850d9a2cd`; source authority `de83e20a68f79ccf25b89b0d33eb4206e294c757`; contract fingerprint `b7845df5ce4bc2bd730461476b7ff0831512003ceb5b3558436005c9876bd251`; durable root `$HOME/.cache/dsir/exp073dt-ww-s0-s0-ab-v0-1`.

The cancellation is infrastructure/resource `+0/+0`, not a WW arithmetic FAIL. `Upload terminal science evidence` was skipped and no terminal science receipt exists, so no `WW_S0_S0` authority was created.

### Measured full-resolution resource diagnosis
The home machine has about 7.68 GiB physical RAM. WSL is configured with 6 GiB memory and 16 GiB swap. At frozen WW geometry `ncls=4`, `nl=12288`, the unbinned MCM has `49152 x 49152` float64 values = exactly `19,327,352,832` bytes = `18 GiB` before field/GSL/Python overhead.

Attempt 5 telemetry established the causal resource bottleneck under the stock heap-backed NaMaster 2.7 path. During the full-resolution workspace build, WSL RAM reached approximately 5.7–5.8/5.8 GiB, available RAM fell as low as about 10 MiB, swap rose from about 4.6 GiB to 8.1 GiB, and the Python process alternated between running and uninterruptible I/O wait. After manual cancellation the science Python disappeared and memory recovered to about 490 MiB used with about 114 MiB swap. This directly binds the pressure to the stock full-resolution workspace construction rather than to a science comparison or downstream exactness check.

Do not re-run Exp073DT on stock heap-backed NaMaster 2.7 on DSIR-HOME-PC.

## Exp073EM — terminal exact-storage support PASS `+0/+0`
Preregistration: `experiments/073em_ww_namaster27_filebacked_mmap_unbinned_exact_storage_qualifier_v0_1_prereg.md`.

The storage-only patch moves only `nmt_workspace::coupling_matrix_unbinned` from heap/calloc storage to a regular-file-backed `mmap(MAP_SHARED)` region when explicitly enabled. MCM formulas, loop ordering, binning, GSL LU operations, FITS serialization and public BPW arithmetic remain unchanged.

The first hosted activation was BLOCKED before arithmetic because malformed patch hunk metadata prevented patch application; this is immutable infrastructure history `+0/+0`.

The corrected hosted qualifier is terminal PASS:
- run `33993395728`;
- job `101379508508`;
- frozen run head `6a91c0b23f0d9971aaff7fc9f127f0467eabe087`;
- artifact `9977333691`;
- artifact digest `sha256:0ece75e489b6f413d96e85a099e42db96b5d5acdc03c3ee6901273357762cda1`;
- token `PASS_EXP073EM_NAMASTER27_FILEBACKED_MMAP_EXACT_STORAGE_V0_1`;
- NaMaster tag `v2.7`, source commit `24365fa59a38c15732f4f37e8b29265b75c442d5`;
- patch SHA256 `9a80a756960afa8b4ddf61b5fbba7fba6ad5ed9ac919e093bb1365a636c789f0`.

For all frozen small-NSIDE cases `auto0`, `auto1`, `cross01`, stock vs patched results have exact WSP shape/value equality, exact full BPW equality, exact selected `EE<-EE` equality, equal canonical SHA256 and max absolute difference `0.0`. Regular-file mmap proof passed for every case. `science_gate_scored=false`; `ww_authority_created=false`; accounting `+0/+0`.

## Exp073EN — current authoritative full-resolution file-backed WW_S0_S0 attempt
Preregistration: `experiments/073en_ww_s0_s0_filebacked_full_resolution_ab_science_v0_1_prereg.md`.

Frozen activation head `284d89a47caee708bca4f648d94058ca49eac54f`. Workflow `.github/workflows/exp073en-ww-s0-s0-filebacked-full-resolution-ab-science-v0-1.yml`.

Current run:
- run `33993889263`;
- hosted preflight job `101380801213` SUCCESS;
- self-hosted job `101380820499` **QUEUED** awaiting `DSIR-HOME-PC`;
- hosted preflight verified the immutable Exp073EM artifact/digest, frozen source/component identities, patch SHA/blob, prereg blob, shell syntax and absence of competing self-hosted DSIR work.

Exp073EN preserves the frozen Exp073DT science identity: source authority `de83e20a68f79ccf25b89b0d33eb4206e294c757`, contract fingerprint `b7845df5ce4bc2bd730461476b7ff0831512003ceb5b3558436005c9876bd251`, R1 artifact `9720335366` with digest `sha256:ff87d8fc7d53b16b786a4eb3d6ffeb103676efb8a548223a187b9f59689f8abd`, NSIDE=4096, ell `0..12287`, 39 frozen bands, spin-2 auto `S0 -> S0`, selected `EE<-EE <f8 [39,12288]`, exact A/B equality only.

Before full-resolution computation the home job must independently rerun the stock-vs-patched Exp073EM qualifier on the exact home stock runtime and its dedicated patched clone. Any bit difference blocks science. It then requires >=70 GiB free in WSL and on Windows C:, captures RAM/swap/mapped-file telemetry, and requires the full-resolution mapped backing proof `19327352832` bytes / `49152` rows for each newly computed replica.

Replica A and B run in separate processes under durable checkpoints. After each reaches `replica_receipt_complete`, only the verified huge workspace FITS and canonical MCM intermediate may be pruned; their hashes are retained in receipts. This prevents simultaneous accumulation of two ~36-GiB temporary sets. Selected authority candidates and all checkpoint manifests remain.

Expected terminal candidate token: `PASS_EXP073EN_WW_S0_S0_FILEBACKED_AB_EXACT_REPEATABILITY_8CORE_V0_1`. Even on terminal candidate PASS, `ww_s0_s0_authority_created=false` until the compact uploaded artifact and complete A/B checkpoint provenance are independently consumed/admitted by Exp073EO, which replaces the provenance-admission role previously reserved for Exp073EB on the superseded DT route.

**DSIR-HOME-PC is now reserved for Exp073EN run `33993889263`, job `101380820499`. Do not launch any competing self-hosted DSIR heavy task.**

## Distinct-field exact-adapter investigation — Exp073EK
Historical support-only chain remains: Exp073DU/DW qualifier FAIL; Exp073DX excluded FITS orientation; Exp073ED excluded low-level/public BPW tensor layout; Exp073EE established formula mismatch; Exp073EF localized mismatch before solve; Exp073EG established manual P/bin mismatch while Q/unbin was exact; Exp073EH showed official P/Q plus NumPy inversion still not exact; Exp073EI showed NumPy inverse differs bitwise from official decoupling operator; Exp073EJ showed columnwise public `decouple_cell` composition still differs bitwise from public `get_bandpower_windows()`.

Exp073EK run/job `33988956806 / 101367596573`, artifact `9976033816`, terminal token `PASS_EXP073EK_DIRECT_PUBLIC_BPW_ADAPTER_EXACT_V0_1`, support-only `+0/+0`. Two independent reloads of the same serialized distinct S0->S1 workspace followed only by public PyMaster 2.7 `get_bandpower_windows()` are exact. No WW authority was created.

Exp073EL remains preregistered and inactive until valid `WW_S0_S0` authority and file-backed full-resolution readiness exist.

## Frozen science/execution boundaries
`0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A invalid `<=0.05`; Layer-B invalid-row `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; no effective ell/z/k or fiducial-P shortcut; exact-threshold ambiguity `numerically_unresolved`; no tolerance/rounding/smoothing/averaging rescue.

## Exact next gates
1. Start only `DSIR-HOME-PC` runner so queued Exp073EN job `101380820499` can bind; do not dispatch another heavy run.
2. Consume the local Exp073EM activation result before full-resolution arithmetic. Any local stock-vs-patched mismatch is support/infrastructure FAIL `+0/+0`, never a science FAIL.
3. If Exp073EN reaches terminal candidate PASS, download/verify the compact artifact and run Exp073EO provenance/admission. Only Exp073EO may set valid `WW_S0_S0` authority.
4. After valid WW_S0_S0 authority, activate Exp073EL for the ordered distinct-field full-resolution resource path under the EK-qualified public-BPW semantics.
