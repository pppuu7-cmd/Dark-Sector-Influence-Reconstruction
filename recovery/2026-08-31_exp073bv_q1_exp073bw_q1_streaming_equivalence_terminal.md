# DSIR recovery — Exp073BV Q1 source lineage and Exp073BW Q1 exact streaming equivalence terminal

**Date:** 2026-08-31  
**Scope:** DSIR only; RTK/RQIR excluded.  
**Article-3 readiness:** **Verified 52.0% | Draft/data 53.7%**.

Repository state and immutable hosted artifacts outrank chat wording. All source-lineage / implementation-equivalence / performance QA in this checkpoint is nonclassifying and `+0/+0`.

## Preserved scientific authority and firewalls

- Exp073BJ run `33379013167` remains terminal Track-A exact Wm_S1 authority PASS; final authority artifact `9758841785`, digest `sha256:a7d5b30e0a8ba4ce6d8437db82982f69f41c01ac6a58c6cb121d4cbbb2c4f008`, remains authoritative.
- Exp073AQ remains the permanent historical hosted exact-repeatability scientific FAIL.
- Exp073BD remains `P3 PROVISIONAL_INCOMPLETE_NO_DOWNSTREAM_USE` and is forbidden downstream.
- No tolerance, ULP, rounding, averaging, majority vote or preferred-replica rescue is admitted.
- Frozen Article-3 support boundaries and required G7 order remain unchanged. No G8 jump.

## Exp073BV terminal source-lineage result

Hosted run: `33420824723`  
Job: `99582473539`  
Head: `6010f094782a277017cbf0bb2a9af63331bb3282`  
Artifact: `9768866582`  
Artifact digest: `sha256:33f013a8c7c06ce2f5f68e62a324b80f2b1911ff2a3cd3ff89a6af4add179cc5`

Frozen terminal label:

`BV_Q1_EXACT_SOURCE_LINEAGE_CONFIRMED`

Immutable receipt establishes:

- installed `pymaster` version exactly `2.7`;
- top-level `_nmtlib` exists and is the same extension object wrapped by `pymaster.nmtlib`;
- official upstream NaMaster v2.7 HEAD is exactly `24365fa59a38c15732f4f37e8b29265b75c442d5`;
- all frozen source-topology predicates pass;
- installed and upstream `pymaster/nmtlib.py` are byte-identical, SHA256 `3c82b229231debf224b1e2206e6e7490d1e274b1d7df3803a17f2ce3fb3a4c6d`;
- runtime symbol-table probes find global `drc3jj` in the loaded `_nmtlib` binary.

BV is provenance/source-lineage only and contributes `+0/+0`.

## Exp073BW terminal exact implementation-equivalence result

Frozen preregistration:

`experiments/073bw_article3_streaming_general_coupling_exact_equivalence_v0_1_prereg.md`

Hosted terminal run: `33435082122`  
Head: `bdb10b6647661dabc14d24f995dfd8808e86beda`  
Artifact: `9774112002`  
Artifact digest: `sha256:67b929eac0cbfe168b0a55410afcc2665c1d2e437abb602b992ca3a1a83bf536`

Frozen terminal label:

`BW_Q1_FULL_AND_STREAM_COMPRESSED_EXACT_EQUIVALENCE_PASS`

The immutable receipt contains 18 frozen cases = 3 scientific spin signatures × 3 sizes × 2 deterministic PCL families:

- signatures: Wm `(0,2,0,2)`, WW same-parity `(2,2,2,2)`, WW flip-parity `(2,-2,2,-2)`;
- `lmax`: `24`, `63`, `127`;
- PCL families: `signed_dyadic`, `positive_dyadic`.

For all 18 cases:

- helper full matrix vs stock `pymaster.get_general_coupling_matrix`: exact `numpy.array_equal=True` and canonical `<f8` SHA equality;
- helper streaming-compressed result vs stock full matrix followed by frozen DSIR row compression: exact array and SHA equality;
- helper 1-thread vs 2-thread and repeated 2-thread outputs: exact array and SHA equality;
- all diagnostic `max_abs_diff` values for these classifying comparisons are exactly `0.0`.

Therefore the exact low-memory streaming helper lineage has passed the preregistered implementation-equivalence gate at the frozen QA scales. BW remains NONCLASSIFYING and contributes `+0 Verified / +0 Draft-data`.

## Independent self-hosted performance evidence

Nonclassifying self-hosted Wigner scaling run `33437417184` completed successfully on head `254bb890cf305d8c946fbc72ee6f1de21d373d3c`.

Artifact: `9775001946`  
Digest: `sha256:a2132539a8c5dd144fdb513415e538d25ee71deb3c90351c47b1c04fdb4ea520`

At `lmax=308`, Wm signature `(0,2,0,2)`, all tested thread counts `1,2,4,6,8,10` produced the exact same canonical output SHA `f60183677c496a68611bf3f8d5bb1b9b6d5383585a558ad49c4fdcdbe0481eee`. Observed wall times were approximately `0.4392, 0.2466, 0.2170, 0.2012, 0.1924, 0.2447` seconds respectively. Peak observed speedup was `2.2828x` at 8 threads; the benchmark recommends 8 threads at its frozen 97%-of-peak rule.

This is performance QA only and does not authorize scientific authority or alter BW/BJ/AQ classifications.

## Interpretation

The prior multi-hour bottleneck is now technically addressable without changing the frozen element-wise source algorithm: BV established the exact runtime/source lineage and BW demonstrated exact equivalence of the streaming-compressed helper to the stock full-matrix path at all frozen QA cases, including thread repeatability. The self-hosted benchmark additionally shows moderate parallel scaling while preserving exact output.

This is sufficient only to admit a separately prospectively frozen **full-scale execution-feasibility / Track-A successor architecture gate** using the exact BW helper lineage. It is not permission to consume Exp073BD, declare Wm_S2/WW authority, enter Layer A/B, or advance to G8.

## Exact next gate

Prospectively preregister a full-scale execution-feasibility successor bound to:

1. immutable BV artifact `9768866582` and `BV_Q1_EXACT_SOURCE_LINEAGE_CONFIRMED`;
2. immutable BW artifact `9774112002` and `BW_Q1_FULL_AND_STREAM_COMPRESSED_EXACT_EQUIVALENCE_PASS`;
3. exact BW helper/code lineage and frozen compilation flags;
4. full scientific DES geometry (`NSIDE=4096`, true ell `0..12287`, 39 bands) without use of Exp073BD as comparator or authority;
5. exact repeatability between prospectively frozen independent replicas before any downstream authority use.

The successor must separately preregister how infrastructure timeout/incomplete is distinguished from exact scientific repeatability mismatch. No tolerance rescue is allowed.

Required G7 order remains:

`validated physical forward/power-input bridges -> preregistered physical support-validity mask -> Layer A/Layer B prerequisites -> covariance restriction/whitening -> nuisance tangent rank/SVD -> quotient/relation/null control -> actual G7 authorization -> fresh G8 withheld family`.

**Verified: 52.0% | Draft/data: 53.7%**
