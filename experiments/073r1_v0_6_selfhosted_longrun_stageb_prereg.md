# Exp073R1 v0.6 — self-hosted long-run Stage-B execution preregistration

**Frozen:** 2026-08-29, before any v0.6 execution output.

## Purpose

Exp073R1 v0.6 is an **infrastructure-only execution-substrate replacement** for the frozen Exp073R1 v0.5 sequential whole-object reconstruction. It is introduced because the authoritative GitHub-hosted v0.5 Stage-B job reached the hosted 360-minute runtime boundary after processing only `54,525,952 / 136,930,995` metacal rows. That cancellation is infrastructure/runtime-limit, not scientific FAIL.

v0.6 does not alter the science question, DES object identities, parent lineage, row order, selection, mapper, mask serialization, repeatability checks, support threshold, covariance policy, or G7/G8/G9 rules.

## Reused immutable Stage-A authority

Do not repeat Stage A. Reuse only the already completed and independently verified v0.5 Stage-A artifact:

- workflow run: `33175886694`;
- workflow head SHA: `2926f1866fed4f0767ce3d1ec797f6e6ed4f4f2c`;
- artifact ID: `9688707039`;
- artifact name: `exp073r1-v05-source-index-2926f1866fed4f0767ce3d1ec797f6e6ed4f4f2c`;
- artifact ZIP digest: `sha256:366aad6468046e6964edc9cd2bfd299960d5dadf1856a30ec608e9ae191c1582`;
- artifact expired flag must be false at execution;
- internal source-summary status must equal `PASS_EXP073R1_V05_SOURCE_WHOLE_STREAM_INDEX_BINDING`;
- internal source whole-object SHA256 must equal `491f623d9370d3e5657db67d410e7cfd0e89475827046e6cd82ef6b3dd88c7a5`;
- internal source-index byte length must equal `273861990`;
- internal source-index SHA256 must equal `dbb362b10c68825e775e7398b18eb77d37fe725ce80cfd5c07faec5cb5755628`.

Any mismatch is `INVALID_FOR_SCIENCE` / reproduction-infrastructure failure. It is not a support or dark-sector result.

## Immutable Exp073R0 parent

Stage B must re-bind exactly:

- Exp073R0 run `33103083736`;
- required workflow `.github/workflows/exp073r0-desy1-raw-row-healpix-equivalence-v0-1.yml`;
- required head SHA `94b05d307295d5e9263646983ece9514f9fa2e88`;
- required internal classification `PASS_RAW_ROW_HEALPIX_EQUIVALENCE_EXP073R0`;
- all frozen parent hard checks must be true.

## Frozen metacal identity and Stage-B semantics

Authoritative metacal object remains:

`mcal-y1a1-combined-riz-unblind-v4-matched.fits`

with:

- expected bytes: `84075649920`;
- authoritative SHA256: `39a7fe03e54d96b85cee2fb523ea108c2a548ba1584368203f0464ed6241ebc8`;
- table data start: byte `17280`;
- row bytes: `614`;
- `ra`: `>f8` at row offset `566`;
- `dec`: `>f8` at row offset `574`;
- `flags_select`: `>i4` at row offset `594`;
- row count: `136930995`.

The execution must call the **unchanged v0.5 evaluator** `ci/exp073r1_sequential_wholestream_v0_5.py` in `metacal-map` mode. No v0.6 science evaluator is permitted.

The frozen transport remains one ordinary whole-object HTTP GET with `Accept-Encoding: identity`, no `Range` header, HTTP 200, exact byte count, and exact full-object SHA256.

The frozen selection remains exactly:

`zbin_mcal == t AND dec >= -90 AND dec <= -35 AND flags_select == 0`

for `t in {0,1,2,3}`.

The frozen mapper remains exactly:

- `nside=4096`;
- `ordering=RING`;
- celestial coordinates `C`;
- `lonlat=True`;
- `healpy.ang2pix`;
- selected coordinates finite;
- emitted pixel indices little-endian uint32 in parent-row order;
- masks serialized with the already frozen little-endian `np.packbits` convention;
- independent reconstruction repeatability required for every bin.

## Execution-substrate change only

The sole admitted architectural change is the job substrate and allowed runtime:

- run Stage B on a GitHub Actions **self-hosted Linux runner** rather than a GitHub-hosted runner;
- set a long timeout sufficient for the frozen 84 GB whole-stream transport, without changing any science acceptance criterion;
- no resume/Range requests, no changed DES mirror, no row sharding, no partial-file scientific classification.

Runner CPU, memory, filesystem location and internal read-block timing have no science semantics. A runner/network interruption before deterministic completion is infrastructure `INCOMPLETE_EXP073R1` and must never be relabeled scientific FAIL.

## Terminal PASS contract

v0.6 can establish `PASS_DESY1_FULL_ONEPASS_WEAK_LENSING_MASK_EXP073R1` only if the unchanged v0.5 evaluator finishes and the post-execution assertion verifies all of the following:

1. exact experiment/status identifiers;
2. no-Range whole-object transport declaration;
3. exact `84075649920` metacal bytes;
4. exact metacal SHA256 above;
5. exact authoritative source SHA256 `491f623...` via immutable Stage A;
6. exact Stage-A source-index byte length and SHA;
7. exact source-index and metacal row count `136930995`;
8. exact frozen selection and mapper;
9. zero out-of-range pixels;
10. all four bins nonempty;
11. every independent mask repeatability check true;
12. every Exp073R0 parent check true;
13. `science_gate_scored=false` and `f_invalid_computed=false`;
14. `covariance_read=false` and `G8_read=false`;
15. `gate_state={G7: OPEN, G8: OPEN, G9: OPEN}`.

An Actions job marked `success` without this internal PASS is insufficient.

## Explicit forbidden operations

- no change to `ci/exp073r1_sequential_wholestream_v0_5.py` after this prereg for the v0.6 execution;
- no Range requests or resumable partial-object semantics;
- no alternate DES object or mirror;
- no changed source/metacal identity;
- no changed row order, selection, declination cut, flags rule, NSIDE, ordering or coordinate convention;
- no post-hoc mask edits;
- no physical-support fraction during R1;
- no covariance, inverse covariance, whitening, nuisance SVD/rank, quotient, relation/null, p-value, G7 classification or G8 read;
- no weakening of downstream Exp073P thresholds to accommodate this transport route.

## Authorization after PASS

A genuine v0.6 R1 PASS closes only the Article-3 **exact DES-Y1 reproduction prerequisite**. It does not itself PASS Exp073P physical support and does not authorize G7.

Only after immutable R1 PASS may Exp073P execute under its already frozen physical-support contract. Only an explicit Exp073P support PASS may authorize covariance restriction/whitening.

## Gate state at preregistration

- G7: OPEN
- G8: OPEN
- G9: OPEN
- Exp073R1: reproduction prerequisite not yet PASS
- Exp073P real physical support: BLOCKED
- covariance/whitening: BLOCKED
- nuisance quotient: BLOCKED
