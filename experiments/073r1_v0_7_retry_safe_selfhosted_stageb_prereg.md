# Exp073R1 v0.7 retry-safe self-hosted Stage-B preregistration

**Frozen:** 2026-08-29 06:18 UTC, while run `33222848695`, attempt `2`,
job `99062223326` was inside the unchanged whole-object mapper and before any
attempt-2 terminal summary or artifact existed.

## Scope

This preregistration permits a future retry-safe execution wrapper only if the
currently active attempt becomes terminal without an admissible Exp073R1
result.  It does not launch a second mapper while attempt 2 is active and does
not modify the frozen scientific or reproduction evaluator.

The future wrapper version is `v0.7`.  Its sole purpose is to prevent a failed
attempt's diagnostic files from occupying the canonical result-artifact name
on a later retry of the same GitHub Actions run.

## Observed infrastructure boundary before this freeze

Run `33222848695`, attempt 1, job `99020389131` passed setup, immutable-parent
binding and runtime creation, then the ordinary no-Range metacal response ended
prematurely after 37,748,736 reported rows.  The exact exception was:

`EOFError: whole stream ended after 18479432 of requested 40239104 bytes`

Its upload step nevertheless created artifact `9709998972` under name
`exp073r1-v06-selfhosted-longrun-98c4b8783a95932949947d9e214706c4ec7eaf8c`,
with digest
`sha256:d770bbfdda55788661b2676d4768e1da38d2e7310cbf96d2bfe52f41a3616351`.
That artifact contains only four partial pixel-record files.  It has no
terminal summary and no mask files and is permanently inadmissible.

Attempt 2 reuses the same run id and workflow snapshot.  GitHub documents that
`GITHUB_RUN_ID` does not change on re-run while `GITHUB_RUN_ATTEMPT` increments.
The checked-in `actions/upload-artifact@v4` step uses the same head-only name
and leaves `overwrite` at its default `false`.  The action's primary
documentation states that an existing matching artifact then causes the
upload to fail.  Therefore a future execution wrapper must make result and
diagnostic identities attempt-specific; it may not delete, overwrite or
reinterpret attempt-1 evidence.

Primary operational references, accessed 2026-08-29:

- <https://docs.github.com/en/actions/reference/workflows-and-actions/variables>
- <https://github.com/actions/upload-artifact#inputs>

This naming defect is infrastructure only.  It is not a scientific result and
does not change the interpretation of the active attempt.

## Frozen evaluator and input contract

Any v0.7 implementation must retain exactly:

- evaluator `ci/exp073r1_sequential_wholestream_v0_5.py`;
- evaluator Git blob SHA-1
  `46fe1271d97ddd9e2164d24e7d79cf27bfda805d`;
- source whole-object SHA256
  `491f623d9370d3e5657db67d410e7cfd0e89475827046e6cd82ef6b3dd88c7a5`;
- source-index SHA256
  `dbb362b10c68825e775e7398b18eb77d37fe725ce80cfd5c07faec5cb5755628`;
- metacal expected bytes `84075649920` and SHA256
  `39a7fe03e54d96b85cee2fb523ea108c2a548ba1584368203f0464ed6241ebc8`;
- required rows `136930995`;
- one HTTP 200 whole-object GET, `Accept-Encoding: identity`, zero Range or
  resume requests;
- selection
  `zbin_mcal == t AND dec >= -90 AND dec <= -35 AND flags_select == 0`;
- `NSIDE=4096`, RING, coordinates `C`, `lonlat=True`;
- all source/R0 parent bindings, four nonempty bins, finite-coordinate,
  in-range-pixel, record-hash, mask-hash and independent repeatability checks;
- exact internal status
  `PASS_DESY1_FULL_ONEPASS_WEAK_LENSING_MASK_EXP073R1`;
- `science_gate_scored=false`, `f_invalid_computed=false`,
  `covariance_read=false`, `G8_read=false`, and
  `gate_state={G7: OPEN, G8: OPEN, G9: OPEN}`.

No threshold, data boundary, coordinate, mapper or acceptance rule may be
changed to repair transport reliability.

## Frozen runtime contract

The v0.7 exact-reproduction route must use the runtime observed in attempt 1,
not a later unconstrained resolution:

- CPython ABI `cp314` / Linux x86-64;
- NumPy `2.5.2`;
- healpy `1.20.0`.

It must print Python, pip, NumPy, healpy, platform and machine metadata before
the mapper.  A mismatch is an infrastructure/reproducibility failure and may
not be relabelled as a scientific FAIL.

## Retry-safe artifact separation

The implementation must use names containing at least exact
`github.run_id`, `github.run_attempt`, and `github.sha`.

1. A **result** artifact may be uploaded only after the mapper and terminal
   assertion both succeed.  It must contain the terminal summary, four pixel
   records and four masks.  Missing files are an error.
2. A **diagnostic** artifact may be uploaded only when the result assertion
   did not succeed.  It must use a different `diagnostic` name and contain a
   machine-readable infrastructure receipt.  Partial pixel records, if
   retained, remain explicitly inadmissible and must never share a result
   artifact name.
3. The final job must fail unless the genuine terminal assertion and result
   upload both succeed.  Uploading diagnostics is not a PASS.
4. `overwrite:true`, deletion of historical artifacts and reuse of a prior
   attempt's artifact id or digest are forbidden.

## Execution and authority firewall

- The v0.7 workflow is not authorized to start while any v0.6/v0.7 heavy
  mapper is queued or active.
- Implementation and synthetic/static validation must be committed before a
  trigger value is changed.
- After a future v0.7 run is dispatched, its exact run, job, head, workflow
  blob, result name and execution attempt must be frozen in a new aggregate
  authority document before terminal output is inspected.
- Aggregate join v0.1 and v0.2 remain immutable.  Neither may be repointed to
  attempt 2 or to a future v0.7 run.
- Attempt-1 artifact `9709998972` and its digest above must be explicit
  fail-closed mutation cases in any successor metadata collector.

## Scientific firewall

No support fraction, `f_invalid`, retained dimension, covariance, whitening,
nuisance rank/SVD, quotient/relation/null, held-out or G8 quantity may be read
or computed by this retry wrapper.  Until genuine Exp073R1 PASS and a separate
aggregate prerequisite PASS exist, `support_executor_authorized=false` and
G7/G8/G9 remain OPEN.
