# Exp073CH terminal recovery — historical B reproduced by native BLAS dispatch

Date: 2026-09-02

## Terminal classification

`EXP073CH_DIAG_HISTORICAL_B_SHA_REPRODUCED_BY_DISPATCH`

Class: `DIAGNOSTIC_NONCLASSIFYING_PLUS0_PLUS0`
Scientific authority: `false`
Readiness delta: `+0/+0`

Exp073CF finalizer exact scientific FAIL remains permanent historical authority and is not rescued or reclassified.

## Immutable run provenance

- run: `33645970816`
- head / trigger commit: `063ab1ee804d0a4b4d36f843a5ae29e252f2db0d`
- preregistration commit: `fe66db14ed621f2018ed64f43d11a0c713fee99d`
- helper commit: `79299e0e07f9993ef346a6d36a36dbd0bb789cac`
- workflow commit: `debf53af671ea51ab6c429c56a91b31836285b76`
- binding commit: `8450ee934af9bf4c43026d2a8f4fd7a290bea9d8`
- authorize job: `100300676816` — success
- R1 job: `100300734239` — success
- R2 job: `100300734241` — success
- R3 job: `100300734189` — success
- R4 job: `100300734176` — success
- aggregate comparator job: `100301228825` — success

Aggregate authority artifact:
- artifact id: `9852842831`
- digest: `sha256:49528a12126cf0c9b83828f54d6b5543f82ee56dbbe0a477d8cd218cea766136`

Worker artifacts:
- R1 `9852829945`, digest `sha256:328bf96f0c7b6388f1c901e2895b2fa35a7b8f338bef4098557cd8544361754d`
- R2 `9852826552`, digest `sha256:d1545b7cff4f14998563b671e54d55c073f3597aec00a28f44e4fb541eeee41c`
- R3 `9852820492`, digest `sha256:cabf4206d732d9a0f4287986f44751106952048fdeab77021f1e9bb36e1c6a7d`
- R4 `9852827421`, digest `sha256:6ccb4d2b07c5cbf0ed602dd4c785d60653cc01a25c6626e682bc9d1a2a05210b`

## Exact result

Immutable compact input remained canonical `<f8 [39,12288]` SHA:
`963dfd79bd49119d2c3124de3507330b3c47637b41dcbd7b9536f617186ef7bd`.

K construction was exact in every successful regime and worker:
`c24456b19e7248cc7ad68502fc78d6f75b885665641d662b1d9c789cf473f795`.

Historical final W hashes:
- Exp073CF A: `fc94c71f8e004fe3340d7ab3df79a70b93d0236902e7f8d72f7387c33829de84`
- Exp073CF B: `bed762740b625f932f016d0988be17500a2583daee08bee9a5da550de786193e`

R1 CPU: `AMD EPYC 7763 64-Core Processor`; native OpenBLAS `Core: Zen`; W = historical A SHA.
R2 CPU: `AMD EPYC 9V74 80-Core Processor`; native OpenBLAS `Core: Zen`; W = historical A SHA.
R3 CPU: `INTEL(R) XEON(R) PLATINUM 8573C`; native OpenBLAS `Core: Cooperlake`; W = **historical B SHA exactly**.
R4 CPU: `AMD EPYC 9V74 80-Core Processor`; native OpenBLAS `Core: Zen`; W = historical A SHA.

Each worker had three fresh-process repeats per regime and was internally exact.

Forced dispatch results were cross-worker exact for each named core but intentionally differed across core types:
- `OPENBLAS_CORETYPE=Nehalem`: W SHA `96248e7699a5a12945854db2c9af150affcfe13f4f9dc0bfcbb87b99f92ff087`
- `OPENBLAS_CORETYPE=Sandybridge`: W SHA `85195fade822de2218a21840835c7b950a90eb1493fd42568e33ff4f36ed2f6a`
- `OPENBLAS_CORETYPE=Haswell`: W SHA `fc94c71f8e004fe3340d7ab3df79a70b93d0236902e7f8d72f7387c33829de84`

Thus the same exact K and compact input can yield different final W bit patterns solely through the OpenBLAS solve kernel dispatch. In particular, the Cooperlake native path reproduced the historical B bit pattern exactly, while native Zen reproduced historical A.

## Interpretation boundary

This isolates the historical finalizer divergence to CPU-dependent/native OpenBLAS linear-solve dispatch at the exact-bit level. It rules out compact input mismatch and K construction mismatch as the cause of the historical A/B divergence. Broad package-version or Azure-region labels alone are not sufficient explanations.

This is NOT a rescue of Exp073CF: that experiment required exact A/B finalizer equality under its frozen contract and failed it. The green diagnostic workflow is infrastructure only; Exp073CH is diagnostic +0/+0.

## Exact next permitted gate

A NEW prospectively versioned deterministic-finalizer experiment may now be preregistered before execution. It must freeze a single explicit BLAS dispatch contract (rather than native CPU dispatch), use immutable compact inputs, run multiple independent hosted workers/fresh processes, demand exact equality with no tolerance, and preserve Exp073CF FAIL permanently. A conservative fixed core should be selected prospectively from architectural/reproducibility considerations, not from a post-hoc preference for historical A or B.
