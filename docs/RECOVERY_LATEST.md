# DSIR RECOVERY LATEST — authoritative live pointer

**Updated:** 2026-09-06
**Scope:** DSIR only; RTK/RQIR excluded.

Repository state, immutable recovery notes, validated Actions raw logs/artifacts and durable checkpoints outrank chat wording. Historical outcomes remain immutable. Frozen science boundaries remain unchanged.

## Preserved scientific authority
Wm_S1 Track-A exact PASS, admitted Wm_S2 and Wm_S3 exact scientific PASS remain preserved. Historical Exp073CM resource/performance FAIL `+0/+0`, Exp073BU runner-loss infrastructure `+0/+0`, and Exp073DT attempts 1–5 infrastructure/resource outcomes remain historical. Current scientific target remains `WW_S0_S0`.

Frozen frontier: `Wm_S1 -> Wm_S2 -> Wm_S3 -> WW_S0_S0 -> WW_S0_S1 -> WW_S0_S2 -> WW_S0_S3 -> WW_S1_S1 -> WW_S1_S2 -> WW_S1_S3 -> WW_S2_S2 -> WW_S2_S3 -> WW_S3_S3`.

## Exp073DT attempt 5 — terminal resource-safety cancellation, no science classification
Run `33940588308`, attempt 5; hosted preflight `101374977192` SUCCESS; self-hosted science job `101374976626` was manually cancelled for resource safety. Stock heap-backed NaMaster 2.7 required an unbinned `49152 x 49152` float64 MCM = exactly `19,327,352,832` bytes (`18 GiB`) before overhead on a WSL environment with 6 GiB memory. Telemetry directly localized pressure to full-resolution stock workspace construction. Outcome is infrastructure/resource `+0/+0`, not WW arithmetic FAIL. No terminal science artifact or `WW_S0_S0` authority exists. Do not rerun stock heap-backed Exp073DT on DSIR-HOME-PC.

## Exp073EM — terminal exact-storage support PASS `+0/+0`
Preregistration: `experiments/073em_ww_namaster27_filebacked_mmap_unbinned_exact_storage_qualifier_v0_1_prereg.md`.

Corrected hosted qualifier:
- run/job `33993395728 / 101379508508`;
- frozen head `6a91c0b23f0d9971aaff7fc9f127f0467eabe087`;
- artifact `9977333691`;
- digest `sha256:0ece75e489b6f413d96e85a099e42db96b5d5acdc03c3ee6901273357762cda1`;
- token `PASS_EXP073EM_NAMASTER27_FILEBACKED_MMAP_EXACT_STORAGE_V0_1`;
- NaMaster v2.7 source `24365fa59a38c15732f4f37e8b29265b75c442d5`;
- patch SHA256 `9a80a756960afa8b4ddf61b5fbba7fba6ad5ed9ac919e093bb1365a636c789f0`.

The patch moves only `nmt_workspace::coupling_matrix_unbinned` from heap/calloc to a regular-file-backed `mmap(MAP_SHARED)` region when explicitly enabled. Small-NSIDE stock-vs-patched `auto0`, `auto1`, `cross01` WSP/full-BPW/selected-EE results are exact by shape, canonical SHA256 and `numpy.array_equal`, with max absolute difference `0.0`; file-backed mapping proof passed. Support-only `+0/+0`; no WW authority.

## Exp073EN — current authoritative file-backed full-resolution WW_S0_S0 process
Preregistration: `experiments/073en_ww_s0_s0_filebacked_full_resolution_ab_science_v0_1_prereg.md`.

Frozen science identity remains:
- source authority `de83e20a68f79ccf25b89b0d33eb4206e294c757`;
- contract fingerprint `b7845df5ce4bc2bd730461476b7ff0831512003ceb5b3558436005c9876bd251`;
- R1 artifact `9720335366`, digest `sha256:ff87d8fc7d53b16b786a4eb3d6ffeb103676efb8a548223a187b9f59689f8abd`;
- NSIDE=4096, ell `0..12287`, 39 bands, spin-2 auto `S0 -> S0`, selected `EE<-EE <f8 [39,12288]`, exact A/B equality only;
- full-resolution mapped MCM proof must be exactly `19327352832` bytes / `49152` rows for each newly computed replica;
- exact 8-CPU execution and fail-closed durable A/B checkpoints are mandatory.

### Immutable Exp073EN attempts 1-2 — network/infrastructure `+0/+0`
Original run `33993889263` had hosted preflight SUCCESS, but home jobs `101380820499` and `101381512953` failed before disk gate, local Exp073EM qualifier, NaMaster build, R1 validation or full-resolution arithmetic because the live-exclusivity GitHub API transport encountered SSL EOF/network failures. No science artifact and no WW authority were produced.

Infrastructure-only repair v0.2 changes only the live-exclusivity transport: `ci/exp073en_live_exclusivity_curl_retry_v0_2.sh` uses retry-safe curl and `ci/exp073en_home_filebacked_fullres_v0_2.sh` replaces only that marker-delimited block while inheriting the v0.1 science path unchanged. Immutable recovery: `recovery/2026-09-06_exp073en_attempt1_2_network_ssl_blocked_retry_v0_2.md`.

### Current authoritative Exp073EN retry-safe run
- workflow `Exp073EN WW_S0_S0 file-backed A/B science network-retry v0.2`;
- run `33994398927`;
- activation head `4d1cbd504067a64a94b038292793e5e8bffba911`;
- hosted preflight job `101382210840` SUCCESS;
- self-hosted science job `101382229273` **IN_PROGRESS** at latest live reconciliation;
- durable root `$HOME/.cache/dsir/exp073en-ww-s0-s0-filebacked-ab-v0-1`;
- checkpoint root `$HOME/.cache/dsir/exp073en-ww-s0-s0-filebacked-ab-v0-1/checkpoints`;
- expected terminal candidate token `PASS_EXP073EN_WW_S0_S0_FILEBACKED_AB_EXACT_REPEATABILITY_8CORE_V0_1`.

Partial numerical output is forbidden for adaptive decisions and was not inspected. The exact current durable checkpoint stage cannot be inferred safely from GitHub live step summaries and must not be guessed.

**DSIR-HOME-PC is reserved exclusively for Exp073EN run `33994398927`, job `101382229273`. Do not launch competing self-hosted DSIR work.**

## Exp073EO — prospectively preregistered WW_S0_S0 provenance/admission gate
Preregistration `experiments/073eo_ww_s0_s0_filebacked_checkpoint_provenance_admission_v0_1_prereg.md`, commit `65c8e8d4f68c6d81c5a139fbb93f5b59467761a9`. It was frozen while Exp073EN was still running and is `PREREGISTERED_NOT_ACTIVATED`.

EO may run only after terminal Exp073EN evidence exists. It must independently verify the compact artifact/digest, exact frozen identities, local/hosted file-backed storage qualification, full-resolution mmap proof, and the complete ordered six-stage durable chain for A and B: `fresh_s0_mask_complete`, `fresh_workspace_mcm_complete`, `mcm_fits_verified`, `full_window_complete`, `selected_ee_complete`, `replica_receipt_complete`. Verified post-receipt pruning of huge intermediates is allowed only if the pre-pruning hashes/provenance are bound by complete receipts. Missing/malformed provenance is BLOCKED `+0/+0`, not science FAIL. Only `PASS_EXP073EO_WW_S0_S0_FILEBACKED_PROVENANCE_ADMISSION_V0_1` may admit valid `WW_S0_S0` authority.

## Distinct-field exact-adapter investigation — Exp073EK
Historical support chain remains immutable: DU/DW qualifier FAIL; DX excluded FITS orientation; ED excluded low-level/public BPW tensor layout; EE/EF/EG/EH/EI/EJ localized why manual/public-composition reconstruction is not bitwise identical to public BPW.

Exp073EK run/job `33988956806 / 101367596573`, artifact `9976033816`, digest `sha256:f39351cddec695559686126fc15e212556eea370fe3eeab73d5f20f80c288c06`, token `PASS_EXP073EK_DIRECT_PUBLIC_BPW_ADAPTER_EXACT_V0_1`, support-only `+0/+0`. Two independent reloads of one serialized distinct S0->S1 workspace followed only by public PyMaster 2.7 `get_bandpower_windows()` are exact. No WW authority was created.

Exp073EL remains preregistered/inactive for the full-resolution ordered distinct-field resource path; Exp073DV remains blocked until valid `WW_S0_S0` authority plus Exp073EL readiness PASS.

## Frozen science/execution boundaries
`0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A invalid `<=0.05`; Layer-B invalid-row `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; no effective ell/z/k or fiducial-P shortcut; exact-threshold ambiguity `numerically_unresolved`; no tolerance/rounding/smoothing/averaging rescue.

## Exact next gates
1. Do not duplicate current Exp073EN run `33994398927 / 101382229273`; keep DSIR-HOME-PC exclusively owned by it.
2. When terminal, consume the raw compact artifact in the same research iteration. Verify digest, source/contract identities, local Exp073EM qualifier, mmap proof, exact A/B evidence and terminal token; workflow SUCCESS alone is insufficient.
3. On candidate PASS, activate Exp073EO and independently audit the complete A/B six-stage durable provenance. Only EO PASS creates `WW_S0_S0` authority.
4. On infrastructure/resource failure, diagnose the first causal failure and preserve verified checkpoints; never weaken arithmetic or re-run completed expensive stages unnecessarily.
5. After valid `WW_S0_S0`, activate Exp073EL for the EK-qualified ordered distinct-field full-resolution resource path; then WW_S0_S1 may proceed only under the frozen frontier.
