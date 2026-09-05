# DSIR current-process ledger

Updated: 2026-09-06
Scope: DSIR only; RTK/RQIR excluded.

## Preserved authority
Wm_S1 Track-A exact PASS, admitted Wm_S2 and Wm_S3 exact scientific PASS remain preserved. Historical negative/resource/infrastructure outcomes remain immutable. Current scientific target is `WW_S0_S0`.

## Authoritative heavy process — Exp073EN retry-safe file-backed WW_S0_S0
- workflow: `Exp073EN WW_S0_S0 file-backed A/B science network-retry v0.2`;
- run `33994398927`, attempt `1`;
- hosted preflight job `101382210840`: SUCCESS;
- self-hosted science job `101382229273`: **IN_PROGRESS** at latest live reconciliation;
- activation head `4d1cbd504067a64a94b038292793e5e8bffba911`;
- frozen Exp073EN science source authority `de83e20a68f79ccf25b89b0d33eb4206e294c757`;
- contract fingerprint `b7845df5ce4bc2bd730461476b7ff0831512003ceb5b3558436005c9876bd251`;
- durable science root `$HOME/.cache/dsir/exp073en-ww-s0-s0-filebacked-ab-v0-1`;
- checkpoint root `$HOME/.cache/dsir/exp073en-ww-s0-s0-filebacked-ab-v0-1/checkpoints`;
- replica checkpoint namespaces remain `checkpoints/exp073dq-ww-s0-s0-a-v0-1` and `checkpoints/exp073dq-ww-s0-s0-b-v0-1` inside the frozen durable driver;
- expected terminal science-candidate token `PASS_EXP073EN_WW_S0_S0_FILEBACKED_AB_EXACT_REPEATABILITY_8CORE_V0_1`;
- last durable checkpoint: not inferable from partial output; partial numerical output MUST NOT be inspected or used for tuning while the run is active;
- on terminal candidate PASS: consume raw compact artifact, verify artifact digest/identities/exact A/B evidence, then activate only the prospectively preregistered Exp073EO checkpoint-provenance admission gate; no WW authority before EO PASS;
- on scientific exact FAIL after all storage/provenance qualification: preserve immutable negative science and continue to the next scientifically allowed branch;
- on infrastructure/resource failure: diagnose the first causal failure, preserve all verified durable checkpoints and resume only prospectively without changing frozen arithmetic.

**DSIR-HOME-PC RESERVED BY Exp073EN run `33994398927`, job `101382229273`. No competing self-hosted DSIR heavy task may launch.**

## Superseded Exp073EN attempts 1-2 — immutable network/infrastructure `+0/+0`
Original run `33993889263` reached hosted preflight SUCCESS but home jobs `101380820499` and `101381512953` failed before disk gate, local Exp073EM qualifier, NaMaster build, R1 validation or full-resolution arithmetic because the live-exclusivity API call encountered SSL EOF/network failure. No science artifact or `WW_S0_S0` authority was created.

The repair is infrastructure-only: `ci/exp073en_live_exclusivity_curl_retry_v0_2.sh` adds retry-safe `curl --retry 8 --retry-all-errors`, and `ci/exp073en_home_filebacked_fullres_v0_2.sh` replaces only the live-exclusivity transport block while inheriting the frozen science code unchanged. This repair was committed before activation of current run `33994398927`.

## File-backed storage qualification — Exp073EM terminal exact support PASS
Hosted run/job `33993395728 / 101379508508`, artifact `9977333691`, digest `sha256:0ece75e489b6f413d96e85a099e42db96b5d5acdc03c3ee6901273357762cda1`, token `PASS_EXP073EM_NAMASTER27_FILEBACKED_MMAP_EXACT_STORAGE_V0_1`. Small-NSIDE stock vs patched WSP/full-BPW/selected-EE comparisons were exact for auto0/auto1/cross01; support-only `+0/+0`, no WW authority.

## Direct cross-workspace adapter closure — Exp073EK support PASS
Run/job `33988956806 / 101367596573`, artifact `9976033816`, digest `sha256:f39351cddec695559686126fc15e212556eea370fe3eeab73d5f20f80c288c06`, token `PASS_EXP073EK_DIRECT_PUBLIC_BPW_ADAPTER_EXACT_V0_1`. Direct serialized-workspace reload + public PyMaster 2.7 `get_bandpower_windows()` is the sole currently exact distinct-field adapter candidate. Support-only `+0/+0`.

## Exp073ER FITS-read storage closure — terminal exact support PASS
Run/job `33997539503 / 101390573286`, activation head `b5b6d75aa569473e5e0770ba1d718f93bf286c86`, artifact `9978528214`, digest and independently verified ZIP SHA256 `1e0c3516de041e773eca030d9488f7af7d38455033ae5b97ba1151820eb22267`, token `PASS_EXP073ER_FILEBACKED_FITS_READ_PUBLIC_BPW_EXACT_V0_1`, classification `FILEBACKED_FITS_READ_PUBLIC_BPW_EXACT`, accounting `+0/+0`, no WW authority. Patched fresh FITS reload A/B proved regular-file mmap backing of exactly `294912` bytes and exact public-BPW equality to stock for full `[4,8,4,48]` and selected `EE<-EE [8,48]`, using SHA equality, `numpy.array_equal=true`, and max absolute difference `0.0`, with no tolerance rescue. Immutable note: `docs/recovery/RECOVERY_2026-09-06_EXP073ER_TERMINAL_EXACT_EN_RUNNING.md`.

## Prepared next gates
- `experiments/073eo_ww_s0_s0_filebacked_checkpoint_provenance_admission_v0_1_prereg.md` prospectively committed at `65c8e8d4f68c6d81c5a139fbb93f5b59467761a9` while Exp073EN was still running. Status `PREREGISTERED_NOT_ACTIVATED`. It independently audits the terminal compact artifact plus complete six-stage A/B durable checkpoint chain and is the only gate allowed to admit `WW_S0_S0` authority.
- Exp073EL remains preregistered/inactive for the ordered distinct-field full-resolution resource path. It may activate only after valid `WW_S0_S0` authority and while respecting single-home-runner ownership. Exp073ER is now exact support evidence for the serialized FITS-read public-BPW storage path but does not itself satisfy Exp073EL or admit any science authority.
- Exp073DV remains prepared but blocked on valid `WW_S0_S0` plus Exp073EL readiness PASS.

Frozen frontier: `Wm_S1 -> Wm_S2 -> Wm_S3 -> WW_S0_S0 -> WW_S0_S1 -> WW_S0_S2 -> WW_S0_S3 -> WW_S1_S1 -> WW_S1_S2 -> WW_S1_S3 -> WW_S2_S2 -> WW_S2_S3 -> WW_S3_S3`.
