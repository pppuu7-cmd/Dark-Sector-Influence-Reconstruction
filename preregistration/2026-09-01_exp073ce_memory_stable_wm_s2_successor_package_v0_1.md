# Exp073CE — memory-stable Wm_S2 successor implementation package v0.1

Date: 2026-09-01
Classification: infrastructure/methodology QA only; `+0/+0`; no Article-3 readiness credit.

## Purpose

Prospectively freeze a narrow memory-lifetime successor for the Exp073CA Wm_S2 PCL stage, using the already-frozen scientific inputs and arithmetic while reducing simultaneous map/field/ALM residency. This package does not authorize any self-hosted execution while the overnight home-runner lock is active.

## Authority preserved

- Exp073BJ terminal Track-A exact Wm_S1 authority: PASS.
- Exp073AQ permanent historical exact-repeatability: scientific FAIL.
- Exp073BD: provisional/incomplete and forbidden downstream.
- Exp073BV source-lineage: PASS.
- Exp073BW exact streaming-equivalence: PASS.
- Exp073BZ checkpoint/failover: PASS.
- Exp073CA attempt3 run `33448843621`: `INFRASTRUCTURE_EXECUTION_INCOMPLETE_NO_SCIENTIFIC_CLASSIFICATION_EXP073CA`, `+0/+0`.
- Exp073CC: corrected-lifetime exact-equivalence QA PASS, synthetic/nonclassifying.
- Exp073CD: first-mask-ALM spill/reload exact-equivalence QA PASS, synthetic/nonclassifying.
- Article-3 readiness remains Verified 52.0%, Draft/data 53.7% absent an explicit frozen ledger change.

## Frozen production semantics

The successor MUST preserve the production Wm scientific construction from `ci/exp073az_article3_low_memory_general_coupling_v0_1.py`:

1. lens map and source map authority/validation are unchanged;
2. lens field constructor remains exactly `nmt.NmtField(a, None, spin=0)`;
3. source field constructor remains exactly `nmt.NmtField(b, None, spin=2)`;
4. no explicit `lmax`, `lmax_mask`, purification, beam, templates, weighting, smoothing, rounding, tolerance, or alternate field option may be introduced;
5. before lens-field release, capture `pcl_lmax = int(fa.ainfo_mask.lmax)`;
6. at full production NSIDE=4096, fail closed unless `pcl_lmax == 12287`;
7. final PCL arithmetic remains exactly `hp.alm2cl(first_mask_alm, second_mask_alm, lmax=pcl_lmax)`;
8. final PCL canonicalization remains contiguous canonical `<f8>` and shape `(12288,)` with finite entries;
9. compact/general-coupling, finalizer, checkpoint authority, comparator, and thread policy remain unchanged.

A literal replacement `lmax=12287` without first capturing and validating the runtime field receipt is forbidden.

## Allowed memory-only lifetime change

For Wm only:

1. build lens map `a`;
2. build `fa = nmt.NmtField(a, None, spin=0)`;
3. capture and validate `pcl_lmax` from `fa.ainfo_mask.lmax`;
4. obtain first mask ALM;
5. serialize first mask ALM canonically as little-endian complex128 (`<c16>`) to local scratch with exact shape/dtype/SHA-256 receipt;
6. write temp file in the same filesystem, flush, `fsync`, atomic `os.replace`, then verify final file size and SHA before releasing the in-memory first ALM;
7. release first ALM, lens field and lens map, then `gc.collect()`;
8. only then build source map `b`, `fb = nmt.NmtField(b, None, spin=2)`, and second mask ALM;
9. reopen first ALM read-only through memory mapping; fail closed unless expected shape, canonical dtype, file size, SHA-256, and non-writeability all match the spill receipt;
10. call unchanged `hp.alm2cl(..., lmax=pcl_lmax)`;
11. clean local spill scratch in a `finally` path without touching scientific remote checkpoint namespaces.

No averaging, majority vote, preferred replica, tolerance, ULP rescue, rounding, smoothing, or acceptance-threshold modification is permitted.

## Full-scale infrastructure guards

- Expected full-scale first ALM storage: 1,208,057,856 bytes (about 1.12509 GiB) for canonical `<c16>`.
- Require at least 2.5 GiB free local spill space per active replica before PCL construction.
- Spill scratch must be local and isolated from scientific checkpoint authority.
- Future heavy workflow concurrency remains `max-parallel: 1` per constrained home host.
- `/usr/bin/time -v` may record infrastructure diagnostics only.
- Heartbeat interval must be <=60 s and report named stage, persisted completed/total when known, elapsed, ETA when estimable, threads, progress bar, and `intra_unit_progress=unknown` when an exact intra-unit fraction is unknowable. Heartbeat must not read/write scientific arrays or alter arithmetic.
- A 6 GiB WSL memory cap is NOT declared safe by this preregistration. Full-scale SHT workspace and mmap residency remain empirically unproven.

## Hosted-only exact selftest contract

A hosted-only QA may exercise small synthetic NSIDE values, but it is nonclassifying and cannot close a real-survey gate. For every frozen synthetic case it must compare a production-semantic sequential oracle with the spill/reload candidate and require all of:

- same runtime `ainfo_mask.lmax` receipt;
- exact first-ALM saved/reloaded SHA-256 identity;
- exact first-ALM shape and canonical `<c16>` dtype identity;
- read-only reload mapping;
- final `np.array_equal(oracle_pcl, spill_pcl) == True`;
- identical canonical `<f8>` SHA-256 of final PCL;
- no tolerance-based fallback.

Frozen classification branches for hosted QA:

- `CE_Q1_MEMORY_STABLE_EXACT_EQUIVALENCE_PASS`: all cases complete and all exact conditions pass; `+0/+0`.
- `CE_Q2_COMPLETE_EXACT_MISMATCH_FAIL`: execution completes but any frozen exact condition fails; `+0/+0`, no rescue.
- `CE_Q3_INFRASTRUCTURE_INCOMPLETE`: environment/setup/runtime prevents complete comparison; `+0/+0`, no scientific classification.

## Overnight lock

Until the user explicitly returns and says the home computer/WSL runner may be used again:

- do not start, rerun, trigger, or otherwise cause any `[self-hosted, Linux, X64]` / DSIR-HOME-PC job;
- do not revive Exp073CA replica B;
- do not create an alternative self-hosted workflow;
- do not change WSL/computer configuration.

This preregistration authorizes only hosted-only QA and repository-side preparation that cannot interfere with Exp073CA.