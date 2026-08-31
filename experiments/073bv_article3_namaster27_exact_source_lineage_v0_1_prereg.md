# Exp073BV — Article-3 NaMaster-2.7 exact source-lineage diagnostic v0.1 — preregistration

**Project:** DSIR only.  
**Classification:** NONCLASSIFYING source-lineage / implementation-provenance diagnostic.  
**Accounting:** `+0 Verified / +0 Draft-data` for every outcome.

Frozen prospectively on 2026-08-31 after Exp073BU run `33420089328` terminal `BU_Q5_PARTIAL_DIAGNOSTIC_INCOMPLETE` and before any BV hosted result.

## Immutable predecessor state

- Exp073BJ run `33379013167` remains terminal Track-A exact authority PASS.
- Exp073AQ remains the permanent hosted exact-repeatability scientific FAIL.
- Exp073BD remains `P3 PROVISIONAL_INCOMPLETE_NO_DOWNSTREAM_USE` and is forbidden as downstream Wm_S2 authority.
- Exp073BU run `33420089328`, artifact `9768579019`, digest `sha256:4f181aef054b8447503a94459d66f70fa0b2f9c75bee16572118a5426597f9dc`, is terminal `BU_Q5_PARTIAL_DIAGNOSTIC_INCOMPLETE`.
- BU established `pymaster` version `2.7` and completed an installed-text search with no `drc3jj` hit, but its extension probe was incomplete because it attempted `pymaster._nmtlib`, which does not exist in that package layout.
- The prior BR/BS/BU diagnostic implementation remains immutable at commit `8a70892c9533206e4011eee041914ca89bae2290`; BV does not reinterpret its Q1–Q5 outcome post hoc.

## New upstream evidence frozen before BV execution

The official `LSSTDESC/NaMaster` tag `v2.7` resolves to immutable commit:

`24365fa59a38c15732f4f37e8b29265b75c442d5`.

At that snapshot, the source topology to be checked by BV is:

1. `pymaster/field.py` imports `from pymaster import nmtlib as lib`;
2. `pymaster/nmtlib.py` imports the low-level extension as top-level `import _nmtlib`;
3. `setup.py` builds an extension named `_nmtlib` and links `./_deps/lib/libnmt.a` into it;
4. `Makefile.am` includes `src/utils.c` in `libnmt_la_SOURCES`;
5. `src/utils.c` contains the implementation `int drc3jj(...)`.

This explains why `pymaster._nmtlib` is not the correct import target, but this source observation alone is not treated as runtime proof until the prospectively frozen BV checks execute.

## Sole purpose

Bind the hosted-successful Exp073BJ conda-forge NaMaster-2.7 runtime layout to the immutable official NaMaster v2.7 source topology strongly enough to identify the correct Wigner implementation source for a later, separately preregistered exact numerical-equivalence QA.

BV is not itself a streaming-kernel validation and is not Wm_S2/WW scientific authority.

## Frozen environment

Use the already hosted-successful BJ environment lineage on `ubuntu-24.04`:

```bash
conda create -y -p "${RUNNER_TEMP}/nmt27" -c conda-forge python=3.11 namaster=2.7 healpy astropy numpy
echo "NMT_PY=${RUNNER_TEMP}/nmt27/bin/python" >> "${GITHUB_ENV}"
```

Separately check out `LSSTDESC/NaMaster` at exact commit `24365fa59a38c15732f4f37e8b29265b75c442d5` into `upstream_namaster_v27/`.

## Frozen probes

The receipt must record, independently:

1. installed `pymaster` version and package path;
2. import/path for top-level `_nmtlib`;
3. import/path for `pymaster.nmtlib` and whether its `_nmtlib` object resolves to the same loaded extension object;
4. SHA256 of the installed `pymaster/nmtlib.py` and upstream-v2.7 `pymaster/nmtlib.py`, plus byte equality;
5. exact upstream Git HEAD and exact file-presence checks;
6. source-topology predicates for the five frozen links listed above;
7. best-effort `nm -a`, `nm -D`, and `readelf -Ws` search for `drc3jj` in the runtime `_nmtlib` binary. Symbol-table visibility is evidence only and is not required for source-lineage PASS because static linking/stripping may suppress a dynamic or printable symbol.

Every probe must be captured in one durable JSON receipt.

## Frozen outcome labels

Exactly one label:

- `BV_Q1_EXACT_SOURCE_LINEAGE_CONFIRMED`: installed version is 2.7; top-level `_nmtlib` and `pymaster.nmtlib` imports resolve; `pymaster.nmtlib._nmtlib` is the same extension object; upstream HEAD is exact; all five source-topology predicates pass; and installed/upstream `pymaster/nmtlib.py` bytes are exactly equal.
- `BV_Q2_SOURCE_TOPOLOGY_CONFIRMED_WRAPPER_BYTES_DIFFER`: runtime imports resolve and all five exact upstream source-topology predicates pass, but installed/upstream `pymaster/nmtlib.py` bytes differ. This is useful provenance evidence but does not establish exact installed-wrapper identity.
- `BV_Q3_RUNTIME_LAYOUT_INCOMPLETE`: exact upstream topology predicates pass but the hosted runtime `_nmtlib` / wrapper relationship cannot be fully resolved.
- `BV_Q4_UPSTREAM_TOPOLOGY_MISMATCH`: exact checked-out upstream commit is correct but one or more frozen source-topology predicates fail.
- `BV_Q5_DIAGNOSTIC_INCOMPLETE`: environment, checkout, hashing, or other essential evidence is incomplete so Q1–Q4 cannot be assigned.

## Interpretation firewall

- Q1 identifies a precise source-lineage implementation candidate for later exact numerical-equivalence QA. It does **not** by itself prove that a future extracted/streaming implementation is numerically or byte-exact equivalent.
- Q2/Q3 require a later prospectively frozen provenance diagnostic before numerical-equivalence authority can rely on exact installed-source identity.
- Q4 is a genuine source-topology contradiction to the preregistered chain and must not be rescued post hoc.
- Q5 is incomplete only; diagnose narrowly and preregister any successor.
- Dynamic/local symbol visibility may be recorded but cannot override these frozen classifications.

## Article-3 / G7 firewalls

- No tolerance, ULP, rounding, averaging, majority vote, preferred-replica or post-hoc rescue.
- No use of Exp073BD provisional Wm_S2 as downstream authority.
- No covariance/whitening/nuisance/quotient/relation/null/G8 read or claim from BV.
- Required G7 order remains unchanged.
- No G8 jump.
- Every result has `scientific_readiness_increment=0` and `draft_data_readiness_increment=0`.

**Readiness remains:** `Verified 52.0% | Draft/data 53.7%`.
