# DSIR recovery — Exp073EP/Exp073EQ reconciled while Exp073EN remains active

Date: 2026-09-06
Scope: DSIR only; RTK/RQIR excluded.

## Live heavy authority
At reconciliation, authoritative heavy process remains Exp073EN network-retry v0.2:
- workflow run `33994398927`;
- hosted preflight job `101382210840`: SUCCESS;
- self-hosted science job `101382229273`: IN_PROGRESS;
- activation head `4d1cbd504067a64a94b038292793e5e8bffba911`;
- durable root `$HOME/.cache/dsir/exp073en-ww-s0-s0-filebacked-ab-v0-1`;
- expected candidate token `PASS_EXP073EN_WW_S0_S0_FILEBACKED_AB_EXACT_REPEATABILITY_8CORE_V0_1`.

No competing self-hosted DSIR workload was launched. Partial numerical output was not inspected and the current durable stage was not guessed.

## Exp073EP — terminal composed support PASS +0/+0
Repository research log commit `ce98014cd33a611994a7169d2d54fd4e58a08a78` records:
- run/job `33994782890 / 101383307890`;
- artifact `9977735941`;
- GitHub artifact digest `sha256:4007fa89e678f4585cd73641ff26054a9c939c3f0e679581202cdf2154a39ed5`;
- token `PASS_EXP073EP_FILEBACKED_CROSS_PUBLIC_BPW_COMPOSITION_EXACT_V0_1`;
- classification `COMPOSED_STORAGE_PUBLIC_BPW_EXACT`;
- accounting `+0/+0`, no WW authority.

This closes only the composition support risk between file-backed MCM storage and serialized distinct-field public-BPW semantics. It does not advance the ordered science frontier.

## Exp073EQ — terminal static authority-contract PASS +0/+0
Repository research log commit `74d2aa0389b271ba2eca0f6a903e29268fe9dbe8` records:
- run/job `33997161393 / 101389591224`;
- activation head `cbb306f32d1ddaaf0a70f00a6aa101854ae3de33`;
- artifact `9978399252`;
- GitHub artifact digest `sha256:063ca99330de8040e1b019a26bbbf9ab030f50aba3eaaf726fdc4febc1d016e9`;
- token `PASS_EXP073EQ_EN_EO_STATIC_AUTHORITY_CONTRACT_V0_1`;
- classification `STATIC_AUTHORITY_CONTRACT_EXACT`;
- accounting `+0/+0`, no WW authority.

EQ confirms prospectively, before Exp073EN terminal numerical evidence, that EN workflow/prereg and EO prereg agree on source authority, contract fingerprint, R1 artifact/digest, NaMaster source commit, file-backed patch identity, hosted Exp073EM identity, exact-only policy and critical geometry. This removes a static EN→EO contract-consistency risk but cannot admit `WW_S0_S0`.

## Authority consequence
`WW_S0_S0` remains pending terminal Exp073EN exact A/B candidate evidence and then Exp073EO six-stage provenance admission. Exp073EO remains preregistered and inactive until terminal Exp073EN evidence exists. `WW_S0_S1` remains blocked on valid `WW_S0_S0` plus the distinct-field resource/readiness path.
