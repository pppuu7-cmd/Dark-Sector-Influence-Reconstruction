# DSIR recovery V26 — WW_S2_S3 admitted; Exp073GA active

Date: 2026-09-08. Scope: **DSIR only**. Earlier recovery notes are immutable history.

## Current scientific authority

WW admitted authority now includes `S0_S0`, `S0_S1`, `S0_S2`, `S0_S3`, `S1_S1`, `S1_S2`, `S1_S3`, `S2_S2`, and **`S2_S3`**. `WW_S3_S3` remains **NOT_YET_ADMITTED** while its frozen heavy gate is active.

`WW_S2_S3` authority was created without rerunning the expensive FY computation. Source evidence remains Exp073FY run `34160898921`, home job `101862390771`, artifact `10040351900`, digest `sha256:ebd1800b9f2b179305d8c1a83208c146915c492f0c3ae614f6ded6ab3be35ad6`, frozen source head `de83e20a68f79ccf25b89b0d33eb4206e294c757`, contract fingerprint `b7845df5ce4bc2bd730461476b7ff0831512003ceb5b3558436005c9876bd251`.

## Recovery/admission chain

- HD run `34188871787`, job `101942632770`: missing NumPy on hosted comparator; `INFRASTRUCTURE/DEPENDENCY_FAILURE +0/+0`. Runtime pin repair commit `8fe0c6cc5bcfcabfd212ce73e2caf8016fd281f2`.
- HD recovery run `34188961637`, job `101942898124`: stale inherited FS source-count check (`{'s1':1,'s2':1}`) against correct FY S2->S3 evidence (`{'s2':1,'s3':1}`); `IMPLEMENTATION/PROVENANCE_FAILURE +0/+0`.
- HE comparator blob `7698487dd137ec4c2b4f3f2faa158aeb6846ef78`, prereg blob `7b47a9f6acd588c0dddd176784077332b66846ac`, workflow commit `cc95d0c0b9af9c912b97cdded5cc7abf6edbfd59`. HE run `34189083696`, job `101943248885`, established exact candidate `PASS_EXP073FY_WW_S2_S3_FILEBACKED_AB_EXACT_REPEATABILITY_V0_1`, selected A/B SHA `73dc92e39b043172fc1f917998187321e737b627af8a75b28e06aeaee43ea555`, exact equality and finiteness. Subsequent FZ wrapper pin/transform failure was provenance/implementation `+0/+0`.
- HF materialized verifier blob `ad1a43b216b67125ed473b74d95e362a4666aa04`, prereg blob `d48dd061661eb95b711cd3f42116a664a704d4bb`, workflow commit `1f17ee193472f890bf91dc5b699cde93a7545db8`. HF run `34189183845`, job `101943539978`, completed SUCCESS and emitted `PASS_EXP073FZ_WW_S2_S3_FILEBACKED_PROVENANCE_ADMISSION_V0_1`, `classification=SCIENTIFIC_AUTHORITY_ADMITTED`, and `ww_s2_s3_authority_created=true`.

Therefore `WW_S2_S3 = SCIENTIFIC_AUTHORITY_ADMITTED`. No scientific FAIL was created by HD/HE/FZ infrastructure/provenance failures.

## Current final heavy successor

The previous GA predecessor gate required a successful FY run by exact workflow name. That became stale once valid S2->S3 authority was prospectively created by hosted-only HF after the FY post-compute infrastructure failure. The predecessor handoff was changed only at orchestration level to require HF run `34189183845` plus the exact S2->S3 admission markers. Frozen GA/GB numerical drivers, contracts, thresholds, source ordering and hypothesis identities were unchanged.

First orchestration repair commit `a2638d900033092819d3bd984df06a83e8f18474` contained a one-character `PRUNER_BLOB` pin typo. Run `34189505842`, hosted job `101944481137`, stopped before any heavy work; home job `101944506715` and final admission `101944507082` were skipped. Classification: `INFRASTRUCTURE/IMPLEMENTATION_FAILURE +0/+0`.

Corrected GA workflow commit: `10e6fb67af7d6485fca3d1ecf2362e4622883417`. Frozen pruner pin restored to `24ee2408b4b66a17001fb734e9e46d008179c310`.

Current single heavy workflow: Exp073GA run **`34189540992`**, head SHA `10e6fb67af7d6485fca3d1ecf2362e4622883417`.

- hosted launch audit job `101944582891`: `SUCCESS`
- self-hosted home-science job `101944608861`: `IN_PROGRESS`
- active step: frozen `WW_S3_S3 A/B gate with durable checkpoints`

Global reconciliation after launch: exactly one `in_progress` workflow (run `34189540992`) and zero queued workflows. Do not launch a duplicate heavy target.

## Next allowed transition

Wait for terminal evidence from run `34189540992`. If and only if the frozen GA candidate succeeds, permit its frozen GB provenance admission. Infrastructure/implementation/provenance failure remains `+0/+0`; `INVALID_FOR_SCIENCE`, `NOT_YET_TESTABLE`, and `OUTSIDE_DOMAIN` remain distinct from scientific FAIL unless a frozen scientific gate explicitly supplies that classification.

Detailed incident log: `docs/research_log/RESEARCH_LOG_2026-09-08_AUTOGUARD_TURN11_FY_ADMITTED_HE_HF_GA_RESUME.md`, creation commit `8c36d4b461cb8a78f5d6923819e1841662062cdc`.
