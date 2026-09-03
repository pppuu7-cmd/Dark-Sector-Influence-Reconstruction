# Wm_S3 scientific authority successor after resource PASS — research draft v0.1

**Status:** NON-AUTHORITATIVE RESEARCH DRAFT ONLY  
**Scientific/resource credit:** `+0/+0`  
**No experiment number is assigned.**  
**Promotion to preregistration is forbidden until a prospectively frozen Wm_S3 resource architecture actually PASSes.**

## 1. Historical boundary

- Historical Exp073AA Wm_S3 production never obtained authority because Exp073AF blocked the 13-task route.
- Exp073AQ and other historical exact-repeatability FAILs remain permanent and are not rescued or reinterpreted.
- Exp073CM/CN/CQ/resource successors are resource/checkpoint/performance experiments. Their compact target is not the final Wm_S3 bandpower window and their results are `+0/+0` unless a separately frozen ledger states otherwise.
- A resource PASS authorizes only execution architecture selection; it cannot itself establish Wm_S3 scientific authority.

## 2. Frozen physical/angular contract to inherit

The scientific successor must preserve the established Article-3 Wm contract:

- DES Y1 `NSIDE=4096`, RING, coordinates C;
- true ell `0..12287`, `L=12288`;
- band edges exactly `[0,30,60,90,120,150,180,210,240,272,309,351,398,452,513,582,661,750,852,967,1098,1247,1416,1608,1826,2073,2354,2673,3035,3446,3914,4444,5047,5731,6508,7390,8392,9529,10821,12288]`;
- exactly 39 bands;
- Wm source bin 3;
- NaMaster/PyMaster 2.7 lineage;
- spin-0 lens x spin-2 source semantics;
- selected component `TE <- TE`;
- canonical compact/general-coupling array `<f8 [39,12288]`;
- canonical final window `<f8 [39,12288]`;
- all entries finite and every final band has strictly positive `sum(abs(W[b,:]))`;
- no effective ell/z/k, centroid/midpoint, fiducial-P weighting or signal-amplitude shortcut;
- no support/covariance/whitening/nuisance/relation/null/G8 read during this angular-authority experiment.

Frozen source-bin-3 authority from the established R1/AZ lineage:

- metacal bytes `84,075,649,920`;
- metacal SHA256 `39a7fe03e54d96b85cee2fb523ea108c2a548ba1584368203f0464ed6241ebc8`;
- selected rows `4,196,641`;
- pixel-record bytes `16,786,564`;
- pixel-record SHA256 `3996f2bacf29d46278773530058d4f5666c0d590bf6cebc06459659166bc60ec`;
- unique occupied pixels `2,943,132`;
- occupancy SHA256 `21e3776111de305c108463b02b0e3fd5e138cc97817d37e7b05330132d058094`.

Frozen Wm lens mask:

- `DES_Y1A1_3x2pt_redMaGiC_MASK_HPIX4096RING.fits`;
- bytes `104,595,840`;
- SHA256 `a519b8522f899e4c33267bb0749f9734f8b7fa760d195636456d370f809a3d55`;
- RING field 0 as float64; `UNSEEN -> 0`; retain original weights only for `mask>0.5`, otherwise zero.

## 3. Mandatory fresh-independent PCL replicas

Scientific compact replicas **A** and **B** must be independent computational lanes. They may bind the same immutable input artifacts, but they MUST NOT import or reuse a PCL payload, compact payload, worker checkpoint, or numerical intermediate from each other or from a resource qualification run.

Each lane must independently:

1. restore/download and byte-verify the frozen R1 source authority and lens-mask authority;
2. reconstruct the dense source-bin-3 object-count map from the exact little-endian uint32 pixel record;
3. verify selected-row count, unique occupied pixels and bitpacked occupancy SHA;
4. reconstruct the exact lens mask transformation;
5. create the frozen NaMaster 2.7 spin-0 and spin-2 mask fields;
6. compute the Wm mask PCL fresh from those masks;
7. canonicalize to `<f8 [12288]`, verify finite, store SHA/provenance and durably checkpoint the complete PCL stage under a replica-specific namespace;
8. never read the other replica's PCL.

A pre-existing resource-lineage PCL SHA `ec34ee34311f3b02a16e118113b5b1acd1b961859caccd2c4387c0ae529cd72d` may be frozen at promotion time as a **provenance checksum only**, because it predates this scientific experiment. Fresh replicas must never import those bytes. If a fresh PCL disagrees with the prospectively frozen input checksum, the lane is provenance-ineligible and scientific compact comparison must not run.

Before compact computation, A/B fresh PCLs must themselves satisfy exact canonical SHA equality and `numpy.array_equal`. A complete valid A/B PCL mismatch is a preregistered exact-repeatability scientific failure of the fresh-PCL authority stage. Missing/corrupt input, timeout, transport or resource exhaustion before two valid PCLs is infrastructure/provenance incomplete instead.

## 4. Resource-qualified compact computation

The compact stage computes the established Wm general-coupling algebra from each replica's own fresh PCL, followed by frozen fixed-order band compression:

`G02 = get_general_coupling_matrix(PCL, 0, 2, 0, 2)`

conceptually, with the already-validated exact streaming implementation allowed **only after** a prospectively frozen resource gate has established the exact execution backend.

For every band `b`:

`A[b,:] = sum_{ell=edge[b]}^{edge[b+1]-1} G02[ell,:] / (edge[b+1]-edge[b])`

using the frozen ascending accumulation order. Canonical compact output is `<f8 [39,12288]`.

At promotion time exactly one backend must be chosen and frozen; this draft leaves it unresolved deliberately:

- **Route C:** complete-band backend, only if Exp073CQ v0.2 (or a later prospectively equivalent complete-band gate) resource-PASSes; or
- **Route S:** exact-safe ll3-sharded backend, only if a NEW prospectively preregistered shard gate first proves bitwise equivalence and resource-PASSes.

No post-output backend switching is allowed.

Each scientific compact lane uses a distinct durable checkpoint namespace. If Route S is selected, complete ll3 shards are checkpoint units and assembly is placement/concatenation only; no arithmetic reduction across shards.

## 5. Compact A/B authority comparator

Only two complete valid compact lanes enter classification. Compact PASS requires simultaneously:

- fresh PCL A/B exact equality already PASSed;
- both compact arrays dtype `<f8`, shape `[39,12288]`, C-contiguous and finite;
- `numpy.array_equal(A_A,A_B) == True`;
- canonical byte-SHA256 equality;
- identical frozen band edges, ell axis, source/lens provenance, NaMaster lineage, signature `(0,2,0,2)`, component semantics and selected resource-qualified backend;
- no forbidden downstream/science-firewall field was read.

A complete valid exact compact mismatch is a permanent scientific repeatability FAIL for that new version. No tolerance, ULP, rounding, smoothing, averaging, majority vote or preferred-replica rescue exists.

Only exact compact PASS admits the common canonical compact `A` to finalization. Neither A nor B is designated the preferred replica; equality makes the admitted bytes common authority.

## 6. Frozen Wm finalizer algebra

Reuse the established `ci/exp073az_article3_low_memory_general_coupling_v0_1.py` Wm algebra without modification.

Given admitted compact `A`, build `K` in the existing fixed order:

```text
for ib,(lo,hi) in bands:
    acc = zeros(39)
    for ell in lo..hi-1 ascending:
        acc += A[:,ell]
    K[:,ib] = acc
```

Then compute exactly:

`W = numpy.linalg.solve(K, A)`

No pseudoinverse, regularization, jitter, clipping, rounding or rescue.

## 7. Deterministic finalizer execution contract

Inherit the accepted Exp073CI numerical-dispatch principle prospectively for Wm_S3:

- hosted-only finalizer workers on a frozen Linux image;
- `OPENBLAS_CORETYPE=Nehalem`;
- `OPENBLAS_NUM_THREADS=1`;
- `OMP_NUM_THREADS=1`;
- `MKL_NUM_THREADS=1`;
- `NUMEXPR_NUM_THREADS=1`;
- `BLIS_NUM_THREADS=1`;
- `OMP_DYNAMIC=FALSE`;
- freeze exact Python/NumPy/OpenBLAS build lineage before execution;
- verify OpenBLAS reports `Core: Nehalem` inside every solve process.

Recommended promotion contract: four independent finalizer workers R1..R4. Every worker receives both exact-equal compact artifact lanes A and B, runs at least three fresh-process solves per lane, and records canonical K/W hashes.

Final PASS requires:

- compact A/B input bytes remain exact-equal;
- within every worker and every fresh process, K is exact-repeatable;
- W is exact-repeatable;
- both compact provenance lanes produce exact-equal K and W;
- all R1..R4 produce exact-equal K and W;
- final `W` is `<f8 [39,12288]`, finite, with strictly positive per-band absolute-response normalization;
- all science-firewall flags remain false.

A complete valid finalizer exact mismatch is a permanent scientific repeatability FAIL for the new finalizer contract. Infrastructure failure before complete comparator inputs remains infrastructure incomplete `+0/+0`.

## 8. Authority token and readiness — unresolved until promotion

This draft deliberately does not assign PASS/FAIL token names or a readiness increment. Those values must be prospectively frozen only after:

1. the current Wm_S3 resource frontier is terminally consumed;
2. exactly one compact backend Route C or Route S is resource-authorized;
3. implementation files and checkpoint namespaces are finalized;
4. a hosted post-implementation static/provenance audit PASSes;
5. an immutable binding freezes all input authorities, code commits, backend contract, checkpoint policy and finalizer dispatch.

A green GitHub workflow is never sufficient authority by itself.

## 9. Post-authority downstream boundary

Even a successful Wm_S3 angular authority does not directly score Layer A/B. It first completes one missing DES angular component and must be joined with the other 13 angular authorities plus the frozen DES radial authority, deterministic 1170-row mapping, BOSS broad operator, factorized evaluator, domain/threshold/firewall metadata and required factorization QA into the pre-support candidate manifest before real combined support scoring.

G7/G8/G9 ordering remains unchanged; no G8 jump.
