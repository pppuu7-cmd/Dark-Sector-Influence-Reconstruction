# Exp073BU selected-TE semantic support QA — Q2 numeric-only

Date: 2026-09-04
Scope: DSIR only; RTK/RQIR excluded.
Accounting: `+0/+0`; no Wm_S3 scientific authority.

## Frozen support contract

Preregistration: `experiments/073bu_support_selected_te_semantic_equivalence_v0_1_prereg.md`
Preregistration commit: `b31733b1047a39942118b409d63e4faa8d8c4b7a`
Helper commit: `bed56467b0d9f145ca9e1c5e896d92e02d5141fa`

The prospective support gate compared, on deterministic nontrivial synthetic spin-0 x spin-2 masks under PyMaster/NaMaster 2.7:

1. stock `NmtWorkspace.compute_coupling_matrix` -> full `get_bandpower_windows()` shape `[2,8,2,48]` -> select `[0,:,0,:]` (`TE <- TE`);
2. low-memory selected algebra `mask PCL -> get_general_coupling_matrix(pcl,0,2,0,2) -> fixed ascending band compression -> K -> np.linalg.solve(K,A)`.

Frozen Q1 required exact canonical SHA equality AND `numpy.array_equal`. Frozen Q2 was exact inequality with maximum absolute difference <= `1e-12`, explicitly non-authorizing for Exp073BU runtime substitution. All outcomes were `+0/+0`.

## First attempt — infrastructure incomplete

Historical run/job/head `33816536157` / `100849813933` / `9be393e6fb015ddfb4a262222866c879ede0c7f1` failed before NaMaster installation or numerical execution. First causal failure: shallow checkout depth 1 could not resolve the older prereg/helper commit tree used by the freeze step. Classification: Q4/infrastructure incomplete `+0/+0`.

Smallest prospective repair commit `a10ef5e664c4d1b20a668f080251ffdea98752a2` changed only source binding: freeze verification now checks the already-frozen Git blob IDs `04fc181fd3354a4a072d7b488e244486a096d3c0` (prereg) and `40e2a2c7a96032fcf3b5c7ff369a8cf416e33d1c` (helper). Synthetic domain, arithmetic and Q1-Q4 rules were unchanged.

## Repaired execution and raw result

Run/job/head: `33816670145` / `100850227684` / `a10ef5e664c4d1b20a668f080251ffdea98752a2`
Workflow conclusion: SUCCESS; raw receipt inspected.
PyMaster version: `2.7`
Raw support status: `Q2_NUMERIC_ONLY_SELECTED_TE_EQUIVALENCE`
Stock full shape: `[2,8,2,48]`
Selected shape/dtype: `[8,48]`, `<f8`
Stock selected SHA256: `dbc75e2d3977db6596a30c2fe204e2b68631ef6c9ce5b4cd1d8ba766b023a688`
Low-memory selected SHA256: `5047b92334b72e163059271310acd2fbbafc349dbd76bbec65edc6dc9b492e2e`
`numpy.array_equal`: `false`
SHA equality: `false`
Maximum absolute difference: `1.4710455076283324e-15`
Artifact: `9916798055`
Artifact digest: `sha256:2244e5ce5df5f48db40c51fca3dba1321fef1125424c7baea74edbaa4008f520`

## Classification

**Q2_NUMERIC_ONLY_SELECTED_TE_EQUIVALENCE, `+0/+0`, NON-AUTHORIZING.**

The low-memory selected algebra is numerically extremely close to stock NaMaster on this frozen synthetic case, but the exact gate failed. The `1e-12` support threshold is not a scientific tolerance and cannot rescue exact equality. Therefore Exp073BU may not silently substitute the existing selected low-memory finalizer for its preregistered full-stock-window semantics.

No historical outcome is reclassified. Exp073CR remains resource PASS `+0/+0`; Wm_S3 scientific authority remains absent.

## Exact next permitted gate

Inspect/freeze the exact NaMaster 2.7 stock operation order used by `NmtWorkspace.get_bandpower_windows()` and determine whether a memory-stable implementation can reproduce the complete stock component tensor and exact selected `TE<-TE` bits without changing the frozen science contract. Any prospective low-memory exact-stock emulator must first pass a new independent hosted exact-equivalence QA against stock, including full component shape/order, canonical bits and multiple deterministic synthetic masks. If exact stock semantics cannot be safely reproduced/checkpointed at full DES scale, classify Exp073BU execution as BLOCKED by the frozen full-window contract rather than weakening it.
