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
- self-hosted science job `101382229273` **IN_PROGRESS** at latest live reconciliation, now beyond two hours and therefore well beyond the historical ~64-minute DT shutdown point;
- durable root `$HOME/.cache/dsir/exp073en-ww-s0-s0-filebacked-ab-v0-1`;
- checkpoint root `$HOME/.cache/dsir/exp073en-ww-s0-s0-filebacked-ab-v0-1/checkpoints`;
- expected terminal candidate token `PASS_EXP073EN_WW_S0_S0_FILEBACKED_AB_EXACT_REPEATABILITY_8CORE_V0_1`.

Partial numerical output is forbidden for adaptive decisions and was not inspected. The exact current durable checkpoint stage cannot be inferred safely from GitHub live step summaries and must not be guessed. Surviving past the former ~64-minute failure point is infrastructure evidence only; it is not science PASS.

**DSIR-HOME-PC is reserved exclusively for Exp073EN run `33994398927`, job `101382229273`. Do not launch competing self-hosted DSIR work.**

## Exp073EO — prospectively preregistered WW_S0_S0 provenance/admission gate
Preregistration `experiments/073eo_ww_s0_s0_filebacked_checkpoint_provenance_admission_v0_1_prereg.md`, prospectively frozen while Exp073EN was still running. It is `PREREGISTERED_NOT_ACTIVATED`.

EO may run only after terminal Exp073EN evidence exists. It must independently verify the compact artifact/digest, exact frozen identities, local/hosted file-backed storage qualification, full-resolution mmap proof, and the complete ordered six-stage durable chain for A and B: `fresh_s0_mask_complete`, `fresh_workspace_mcm_complete`, `mcm_fits_verified`, `full_window_complete`, `selected_ee_complete`, `replica_receipt_complete`. Verified post-receipt pruning of huge intermediates is allowed only if the pre-pruning hashes/provenance are bound by complete receipts. Missing/malformed provenance is BLOCKED `+0/+0`, not science FAIL. Only `PASS_EXP073EO_WW_S0_S0_FILEBACKED_PROVENANCE_ADMISSION_V0_1` may admit valid `WW_S0_S0` authority.

Latest architecture audit shows EO can be hosted-only after EN completion: the EN compact artifact already copies all JSON checkpoint/provenance manifests, A/B selected payloads, A/B driver logs, local Exp073EM activation records and component identities. The frozen EN wrapper itself requires successful mmap cleanup before it can advance to the terminal candidate receipt. EO should therefore verify the hash chain `workspace-stage -> verified-stage -> replica receipt -> prune receipt`, recompute selected A/B SHA and exact array equality, and bind the original EN run/head/workflow through GitHub metadata. No heavy numerical recomputation is required for admission.

## Distinct-field exact-adapter investigation — Exp073EK
Historical support chain remains immutable: DU/DW qualifier FAIL; DX excluded FITS orientation; ED excluded low-level/public BPW tensor layout; EE/EF/EG/EH/EI/EJ localized why manual/public-composition reconstruction is not bitwise identical to public BPW.

Exp073EK run/job `33988956806 / 101367596573`, artifact `9976033816`, digest `sha256:f39351cddec695559686126fc15e212556eea370fe3eeab73d5f20f80c288c06`, token `PASS_EXP073EK_DIRECT_PUBLIC_BPW_ADAPTER_EXACT_V0_1`, support-only `+0/+0`. Two independent reloads of one serialized distinct S0->S1 workspace followed only by public PyMaster 2.7 `get_bandpower_windows()` are exact. No WW authority was created.

## Latest independent support closures — Exp073EP, Exp073EQ and Exp073ER
Exp073EP terminal hosted support PASS:
- run/job `33994782890 / 101383307890`;
- artifact `9977735941`, digest `sha256:4007fa89e678f4585cd73641ff26054a9c939c3f0e679581202cdf2154a39ed5`;
- token `PASS_EXP073EP_FILEBACKED_CROSS_PUBLIC_BPW_COMPOSITION_EXACT_V0_1`;
- classification `COMPOSED_STORAGE_PUBLIC_BPW_EXACT`, accounting `+0/+0`, no WW authority.
It exactly closes the composition support risk between Exp073EM file-backed MCM storage and Exp073EK serialized distinct-field public-BPW semantics; all frozen exact comparisons passed with `numpy.array_equal`, canonical SHA equality and max absolute difference `0.0`.

Exp073EQ terminal hosted static contract PASS:
- run/job `33997161393 / 101389591224`;
- activation head `cbb306f32d1ddaaf0a70f00a6aa101854ae3de33`;
- artifact `9978399252`, digest `sha256:063ca99330de8040e1b019a26bbbf9ab030f50aba3eaaf726fdc4febc1d016e9`;
- token `PASS_EXP073EQ_EN_EO_STATIC_AUTHORITY_CONTRACT_V0_1`;
- classification `STATIC_AUTHORITY_CONTRACT_EXACT`, accounting `+0/+0`, no WW authority.
EQ prospectively confirms EN workflow/prereg and EO prereg are consistent on source authority, contract fingerprint, R1 artifact/digest, NaMaster source, file-backed patch, Exp073EM identity, exact-only policy and critical geometry. It closes static EN→EO contract risk only.

Exp073ER terminal hosted support PASS:
- preregistration blob `3a3642189d33a1a2185f6b3b0aad86c6870b18a2`;
- run/job `33997539503 / 101390573286`;
- activation head `b5b6d75aa569473e5e0770ba1d718f93bf286c86`;
- artifact `9978528214`;
- GitHub digest and independently verified ZIP SHA256 `sha256:1e0c3516de041e773eca030d9488f7af7d38455033ae5b97ba1151820eb22267`;
- token `PASS_EXP073ER_FILEBACKED_FITS_READ_PUBLIC_BPW_EXACT_V0_1`;
- classification `FILEBACKED_FITS_READ_PUBLIC_BPW_EXACT`, accounting `+0/+0`, no WW authority.
Patched fresh FITS reload A/B each proved a regular mapped backing file of exactly `294912` bytes with complete cleanup. Stock A/B and patched A/B public `read_from(read_unbinned_MCM=True) -> get_bandpower_windows()` outputs were exact for full BPW `[4,8,4,48]` and selected `EE<-EE [8,48]`: SHA equality, `numpy.array_equal=true`, max absolute difference `0.0`, no tolerance rescue. Full BPW SHA `bf656c5f0493dc44d6c42b31b804f04f6893b7fc4895e92b99cefc356b10b884`; selected EE SHA `336a0b57fe734a2f17a4a0844db1a18fc43887abf7556fb63009ee4a3de5f607`.

Immutable reconciliation notes: `docs/recovery/RECOVERY_2026-09-06_EXP073EP_EQ_RECONCILED_EN_RUNNING.md` and `docs/recovery/RECOVERY_2026-09-06_EXP073ER_TERMINAL_EXACT_EN_RUNNING.md`.

Exp073EL remains preregistered/inactive for the full-resolution ordered distinct-field resource path; Exp073ER now closes the FITS-read storage exactness prerequisite for that future route, but Exp073EL itself remains unpassed. Exp073DV remains blocked until valid `WW_S0_S0` authority plus Exp073EL readiness PASS.

## Frozen science/execution boundaries
`0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A invalid `<=0.05`; Layer-B invalid-row `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; no effective ell/z/k or fiducial-P shortcut; exact-threshold ambiguity `numerically_unresolved`; no tolerance/rounding/smoothing/averaging rescue.

## Exact next gates
1. Do not duplicate current Exp073EN run `33994398927 / 101382229273`; keep DSIR-HOME-PC exclusively owned by it.
2. When terminal, consume the raw compact artifact in the same research iteration. Verify digest, source/contract identities, local Exp073EM qualifier, mmap proof, exact A/B evidence and terminal token; workflow SUCCESS alone is insufficient.
3. On candidate PASS, activate Exp073EO as a hosted-only independent provenance/admission audit. Only EO PASS creates `WW_S0_S0` authority.
4. On infrastructure/resource failure, diagnose the first causal failure and preserve verified checkpoints; never weaken arithmetic or re-run completed expensive stages unnecessarily.
5. After valid `WW_S0_S0`, activate Exp073EL for the EK/EP/ER-qualified ordered distinct-field full-resolution resource path; then WW_S0_S1 may proceed only under the frozen frontier.
