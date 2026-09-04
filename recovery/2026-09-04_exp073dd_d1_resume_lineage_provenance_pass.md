# Exp073DD v0.1 — D1 resume-lineage provenance PASS

Date: 2026-09-04
Scope: DSIR only. Support/readiness `+0/+0`; no Wm_S3 scientific authority created.

## Frozen purpose
Exp073DD prospectively audited the resume-lineage bookkeeping defect identified while the already-frozen Exp073BU science process continued uninterrupted at source head `a2f14dfd5a9e54a30fb467f6d0e717bd4f00bd35`. Exp073DD did not alter, restart, cancel, inspect partial numerical output from, or write to that process or its durable checkpoint namespaces.

## Prospective repair
`ci/exp073bu_wm_s3_fresh_ab_production_v0_2.py` delegates science execution and the exact A/B comparator to frozen v0.1 and changes provenance bookkeeping only. It separates invocation-new reconstruction counts from cumulative immutable lineage. A fresh invocation is `{lens:1,source:1}` / cumulative `{1,1}`; a verified resume may be invocation `{0,0}` while cumulative remains exactly `{1,1}`. Missing, malformed, non-integer, or wrong cumulative lineage fails closed. Legacy final receipts without explicit v0.2 lineage fail closed rather than being silently migrated.

No DES/Wm_S3 science arithmetic, band edges, NSIDE, ell domain, `TE<-TE`, canonical dtype/shape, exact SHA256 + `numpy.array_equal` comparator, 8-worker policy, six-stage checkpoint order, or no-tolerance rule changed.

## Validated hosted result
- token: `D1_RESUME_LINEAGE_PROVENANCE_PASS`
- classification: support/readiness PASS `+0/+0`
- run/job: `33892969489 / 101088831684`
- workflow activation/head commit: `fbe6156d95cafdca3630c058808d74ac139cce46`
- prereg commit: `0e7f1fc8036395ba3faaedaa61f2ef4841565b83`
- prospective repair commit: `0b6f0bc909ae4d596dfa5d9af1828d26d6a2b221`
- regression commit: `4e0e81eb35caefd50ca8c011870489c8002e3679`
- artifact ID: `9944582651`
- independently downloaded ZIP SHA256: `06c971ec7b97fae34b0fa1e113fb449d0bffc9b0e126f0045a9660eb1f6a1056`

Raw receipt confirms all frozen checks true, including `delegates_frozen_science_to_v01`, `delegates_replica_science`, `delegates_exact_ab_comparator`, `no_new_science_arithmetic_in_v02`, frozen 39-band edges, frozen six-stage order, frozen 8 outer workers, frozen TE selection, frozen exact comparator, frozen no-tolerance rescue, dynamic exact `{1,1}` and `{0,0}` acceptance where appropriate, and fail-closed rejection of missing/malformed/wrong cumulative lineage. `science_gate_scored=false` and `historical_wm_s3_numerical_import=false`.

## Authority consequence
D1 validates only a prospective provenance-safe resume repair. It does not retroactively alter the frozen source of the currently running Exp073BU science process and does not create scientific authority. If the current run completes uninterrupted, its frozen terminal artifact is classified under the original Exp073BU contract. If a future infrastructure interruption requires resume, v0.2 must first be explicitly bound prospectively by the applicable activation/orchestration authority; no silent source substitution is permitted.
