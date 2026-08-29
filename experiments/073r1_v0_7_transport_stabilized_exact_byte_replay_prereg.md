# Exp073R1 v0.7 — transport-stabilized exact-byte replay preregistration

Date: 2026-08-29
Status: FROZEN BEFORE EXECUTION
Scope: reproduction/infrastructure recovery only; no G7/G8/G9 science scoring.

## Motivation

Exp073R1 v0.6 preserved the v0.5 frozen evaluator and whole-object/no-Range HTTP contract on a self-hosted runner, but two independent executions terminated because the authoritative DES server closed the response early. Attempt 1 and attempt 2 both passed immutable-parent/evaluator checks and failed only inside `read_exact` with premature EOF. These are infrastructure transport failures, not scientific FAILs.

A third identical direct-stream retry is not the preferred recovery because it repeats the same demonstrated upstream failure mode. v0.7 changes only the execution/transport staging layer.

## Frozen scientific/reproduction authority retained

The following remain unchanged and MUST be re-bound before execution:

- frozen evaluator: `ci/exp073r1_sequential_wholestream_v0_5.py`
- evaluator Git blob SHA1: `46fe1271d97ddd9e2164d24e7d79cf27bfda805d`
- authoritative metacal URL: `https://desdr-server.ncsa.illinois.edu/despublic/y1a1_files/shear_catalogs/mcal-y1a1-combined-riz-unblind-v4-matched.fits`
- metacal expected bytes: `84075649920`
- metacal expected SHA256: `39a7fe03e54d96b85cee2fb523ea108c2a548ba1584368203f0464ed6241ebc8`
- Stage-A source run/artifact lineage from Exp073R1 v0.5
- source whole SHA256: `491f623d9370d3e5657db67d410e7cfd0e89475827046e6cd82ef6b3dd88c7a5`
- source index SHA256: `dbb362b10c68825e775e7398b18eb77d37fe725ce80cfd5c07faec5cb5755628`
- Exp073R0 immutable parent lineage
- row count: `136930995`
- selection: `zbin_mcal == t AND dec >= -90 AND dec <= -35 AND flags_select == 0`
- mapper: NSIDE=4096, RING, coordinates C, `lonlat=True`
- terminal reproduction status required: `PASS_DESY1_FULL_ONEPASS_WEAK_LENSING_MASK_EXP073R1`
- no support-mask validity score, `f_invalid`, covariance, whitening, nuisance SVD/rank, quotient/relation/null, G8 or G9 quantity may be computed here.

No frozen acceptance criterion is relaxed or changed by this preregistration.

## v0.7 transport-staging contract

### A. Authoritative-object acquisition

The self-hosted runner SHALL acquire a local byte-for-byte copy of the authoritative metacal object using repeated independent **whole-object HTTP GET attempts**. Every remote attempt MUST satisfy all of the following:

1. request contains no `Range` header;
2. `Accept-Encoding: identity` is sent;
3. HTTP status is exactly 200;
4. `Content-Range` is absent;
5. if `Content-Length` is present, it equals `84075649920`;
6. the destination partial file is opened with truncation before each attempt, so every retry restarts from byte 0 rather than resuming;
7. any EOF/network exception, wrong byte count, or wrong SHA256 makes that attempt infrastructure FAIL and its partial file MUST be deleted before another attempt;
8. an object is authorized for replay only if final byte count is exactly `84075649920` and SHA256 is exactly `39a7fe03e54d96b85cee2fb523ea108c2a548ba1584368203f0464ed6241ebc8`.

No ranged resume, sparse reconstruction, multi-range assembly, or scientific transformation is permitted.

The acquisition stage SHALL write a provenance JSON containing attempt count, per-attempt outcome/observed bytes where available, final byte count/SHA256, authoritative URL, `http_range_requests: 0`, and `whole_object_attempts_from_zero: true`.

### B. Exact-byte local HTTP replay

After and only after the local object passes the exact byte-count and SHA256 checks, it SHALL be exposed to the unchanged frozen evaluator through a loopback HTTP endpoint. The endpoint must return ordinary HTTP 200 whole-object responses with the exact `Content-Length` and no `Content-Range` for the evaluator's no-Range request.

The frozen evaluator SHALL then run unchanged against that loopback URL. This replay is scientifically equivalent at the evaluator boundary because the input object is already cryptographically bound byte-for-byte to the authoritative remote object. It is explicitly a transport-stabilized reproduction route, not a new data product.

### C. Runtime provenance

The run SHALL record exact Python, pip, numpy, healpy, astropy, pyerfa, PyYAML, packaging and astropy-iers-data versions actually used. The current v0.6-observed numpy/healpy pair (`2.5.2`, `1.20.0`) should be retained if installable; deviations are runtime-variation metadata and do not alter scientific acceptance criteria.

## Terminal PASS conditions

v0.7 is a genuine Exp073R1 reproduction PASS only if all of the following are true:

1. immutable Stage-A and Exp073R0 metadata/artifacts re-bind exactly;
2. evaluator blob identity is exact;
3. remote acquisition provenance demonstrates zero Range requests and full-from-zero attempts only;
4. authorized local object has exactly 84075649920 bytes and the frozen metacal SHA256;
5. the unchanged evaluator itself terminates with `PASS_DESY1_FULL_ONEPASS_WEAK_LENSING_MASK_EXP073R1` and all original v0.6/v0.5 terminal assertions pass;
6. downstream science leakage flags remain false and gate state remains `G7=OPEN, G8=OPEN, G9=OPEN`.

## Failure classification

- Remote premature EOF / timeout / connection reset / disk-capacity failure / loopback server failure: `INFRASTRUCTURE_FAILURE`, never scientific FAIL.
- Wrong complete-object byte count or SHA256 from the authoritative URL: `REPRODUCTION_IDENTITY_FAIL` and stop fail-closed; do not proceed to mapper.
- Frozen evaluator completes but violates its preregistered Exp073R1 acceptance assertions: `REPRODUCTION_FAIL`; preserve negative result.
- No result from this experiment may be called a G7 scientific PASS or FAIL.

## Downstream firewall

Even after a genuine v0.7 Exp073R1 PASS, the required order remains:

validated physical forward/power-input bridges -> preregistered physical support-validity mask -> covariance restriction/whitening -> nuisance tangent rank/SVD -> quotient/relation/null control -> only then fresh G8 withheld family.
