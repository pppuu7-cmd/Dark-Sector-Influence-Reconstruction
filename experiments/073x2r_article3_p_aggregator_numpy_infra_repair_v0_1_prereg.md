# Exp073X2R — Article 3 primary P aggregator-only NumPy infrastructure repair v0.1

**Frozen:** 2026-08-30 after Exp073X2 Chain P replicas A/B completed and persisted immutable hosted artifacts, after the original P aggregator terminated before comparison with `ModuleNotFoundError: No module named 'numpy'`, while Chain Q is still active, and before reading/downloading the numerical contents or canonical selected-window hashes of either P replica artifact in this repair path.

## Classification of the triggering failure

Primary Exp073X2 run `33300997298` produced two successful independently persisted real-DES exact replicas:

- A artifact `9730411514`, artifact digest `sha256:34530157cddf594c93728d5e092ab937d16a653665623f00513f4fd58df17555`;
- B artifact `9730409129`, artifact digest `sha256:36358663fb1980ad75cb71f7ca7149d06d357cf7de8b29feca4273f4f88c89e5`.

The original aggregate job `99242068393` failed at Python import, before `load_replica`, metadata comparison, canonical-hash comparison, or `numpy.array_equal` executed:

`ModuleNotFoundError: No module named 'numpy'`.

Therefore the original aggregate result is frozen as:

`INCOMPLETE_INFRASTRUCTURE_MISSING_NUMPY_BEFORE_REPEATABILITY_CLASSIFICATION`.

It is neither repeatability PASS nor repeatability/scientific FAIL.

## Purpose

Exp073X2R repairs **only** the missing NumPy runtime in the lightweight aggregator. It must not recompute either expensive workspace and must use the exact existing P replica artifacts above.

The comparator source remains exactly the already-frozen file:

`ci/exp073x2_compare_replicas_v0_1.py`

last modified at commit `8ec6f94ea9ddf3cc0a4c98e5af696d28d995b2b3`.

No comparator logic, tolerance, equality rule, mask contract, angular contract, threshold, or scientific accounting may change.

## Exact allowed repair

The hosted repair workflow may only:

1. checkout the prospective frozen repair head;
2. verify this prereg and workflow freeze identities;
3. install a pinned NumPy runtime sufficient to execute the unchanged comparator;
4. download exact P replica artifacts `9730411514` and `9730409129` from run `33300997298` by exact artifact names/run binding;
5. verify the GitHub artifact digests above before relying on them;
6. execute the unchanged comparator once;
7. if and only if the comparator returns its existing PASS token, persist the comparator JSON as a hosted non-classifying authority receipt;
8. preserve any comparator assertion mismatch as a real repeatability failure under the frozen X2 governance; do not retry with changed tolerances or alternate artifacts.

## Frozen comparator contract

The unchanged comparator requires:

- exact replica identities A and B;
- exact completion PASS tokens for each replica;
- `NSIDE=4096`, `NPIX=201326592`;
- true ell `0..12287`, count `12288`;
- 39 frozen bandpowers and exact frozen edges;
- spin-0 x spin-2 component semantics `TE <- TE`;
- G7/G8/G9 OPEN;
- Article-3 readiness exactly `52`;
- anti-leakage firewall false fields;
- selected array exactly finite `<f8 [39,12288]`;
- each NPZ canonical SHA equal to its own JSON metadata SHA;
- exact equality of frozen metadata across replicas;
- canonical SHA equality across replicas;
- `numpy.array_equal(A,B) == True`.

No numerical tolerance is permitted for repeatability.

## Authority/governance interaction

This repair belongs to **Chain P**, not to Q and not to a new alternative scientific branch. It only completes the classification step that P failed to execute for an infrastructure reason.

- If Exp073X2R comparator PASSes, that hosted receipt is the repaired P repeatability authority for applying the already-frozen P/Q governance.
- If the unchanged comparator executes and reports any metadata/hash/array mismatch, classify P as `SCIENTIFIC_REPEATABILITY_FAIL`; Q cannot rescue it.
- If this repair itself fails for a new infrastructure reason before comparator classification, preserve that new infrastructure-INCOMPLETE state; do not infer PASS/FAIL.

Chain Q remains independently governed by the already-frozen prospective P/Q rules. Exp073AF release control still blocks production until the required Q state is resolved.

## Anti-leakage and readiness firewall

Exp073X2R must not read or evaluate radial kernels, physical support, retained coordinates, fiducial P, covariance/whitening, nuisance geometry/SVD/rank, relation/null quantities, or G8.

A repeatability PASS is a real hosted **non-classifying angular-authority PASS**, not a scientific model/gate PASS. It contributes `+0` Article-3 scientific-readiness points. Strict readiness remains `52%`; G7/G8/G9 remain OPEN.

## Required successful token

The unchanged comparator token remains:

`PASS_EXP073X2_DES_N4096_WM0_MASK_ONLY_REPEATABILITY_V0_1`

No new success criterion is introduced by Exp073X2R.
