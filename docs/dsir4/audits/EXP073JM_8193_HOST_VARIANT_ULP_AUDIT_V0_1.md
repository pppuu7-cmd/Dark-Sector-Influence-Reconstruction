# Exp073JM — 8193 host-variant ULP audit v0.1

Date: 2026-09-11. Scope: response-blind DSIR Article III reproducibility only. Effect `+0/+0`.

This audit was completed while recovered Exp073JL retry `34544293038` was still in its frozen numerical step. No JL scientific response or verdict was used.

## Observation

The first four-replica no-CLASS JM-8193 materialization attempt intentionally required each runner to reproduce the already-authoritative Exp073JT 4097 lattice before accepting any 8193 candidate. Two replicas reproduced the anchor and two did not, despite the same Ubuntu runner image, Python and NumPy 1.26.4 contract. This was correctly treated as no canonical result.

The prospectively repaired eight-replica anchor-selection run `34544561155` emitted every candidate regardless of anchor status and applied a fixed rule only at aggregate time: at least four replicas must bit-match the pre-existing authoritative 4097 anchor, and all anchor-matched 8193 candidates must be byte-identical.

Six of eight replicas matched the authoritative 4097 anchor: replicas 2, 4, 5, 6, 7, 8. Replicas 1 and 3 produced the same non-authoritative 4097 host variant. All six anchor-matched replicas produced byte-identical 8193 candidates.

Authoritative-anchor 8193 candidate:

- decoded `<f8` SHA256 `6d35a9d79aa8826554e8e39315ab12a8be1675d32d25a86ec04c978c7723a515`;
- u64hex SHA256 `90b9aee9e01784a4af89ab0aa1bd5cbf1e95061f2d412d7a0e1b8ee5332ba7d6`.

Observed non-anchor host variant:

- 4097 anchor-variant decoded SHA256 `80d5a13c9fa32e77a248b5a835ecf210b9e6afdda27decaffba27b829c261a92`;
- 8193 candidate decoded SHA256 `5009074d460a71943acf0d543e3891174a9548bc1c94bf1092eac6d87f6e0410`;
- 8193 candidate u64hex SHA256 `efda6ee2edd342c66a69f88feb2b7ef0464a9cb13c8250a6ee85a5a270c2371a`.

Independent byte/numeric comparison of an anchor-matched replica and a host-variant replica finds exactly **2275 differing nodes out of 8193**. Every differing binary64 word differs by exactly **1 ULP**. Maximum relative numeric difference over the differing nodes is approximately `2.2173306769102395e-16`.

## Interpretation

This is not a scientific uncertainty and does not alter any physical grid definition, tolerance or convergence criterion. It is a reproducibility/provenance issue at the binary64 construction level. A host-regenerated `np.geomspace` lattice can be mathematically equivalent yet byte-different on nominally identical hosted environments.

Therefore:

1. JN must consume the already-committed Exp073JT canonical 2049/4097 byte streams rather than regenerate them;
2. JM, if later activated, must consume the response-blind canonical 4097/8193 byte streams once the 8193 materialization is committed and independently verified;
3. host-generated variants may be recorded diagnostically but must not be selected after seeing any scientific response;
4. no 1-ULP host variant may be used as a numerical-rescue mechanism or treated as a separate scientific resolution.

This strengthens the repository's exact-reproducibility contract but does not change `ARTICLE3_REPOSITORY_READINESS=68%` or funnel-freeze readiness `=67%`.
