# Exp073R0 attempt 2 — transport/infrastructure incomplete record

Date: 2026-08-27

Run `33092211100`, job `98587741090`, head `5ee34c3fc80ab1091b7e925d321d880dbadade3c`.

The workflow-level 120-minute timeout was not reached. The sampled raw-row audit instead terminated inside `fetch_range` after all retry attempts for a metacal HTTP byte range failed with `TimeoutError: The read operation timed out`.

This is classified as `INCOMPLETE_EXP073R0`, not `FAIL_RAW_ROW_HEALPIX_EQUIVALENCE_EXP073R0` and not PASS. The implementation writes that incomplete status before re-raising transport errors; the upload step completed and preserved artifact `9656933701` with ZIP digest `sha256:a5037b4e644ddd9faba48088b3bc6a394874d30c81a9cf84f9627ae71efcff6d`.

No sampled decoder equality, HEALPix equivalence, science support fraction, covariance, nuisance SVD, relation/null, or G8 result is inferred from this interrupted attempt.

A job-level rerun was requested without changing the 16 frozen windows, field offsets/types, selection, `nside=4096`, HEALPix mapping, PASS/FAIL semantics or Exp073P acceptance criteria. This is a retry of a transient transport failure only.

Exp073R1 remains execution-forbidden until a genuine `PASS_RAW_ROW_HEALPIX_EQUIVALENCE_EXP073R0`, although its contract has already been prospectively frozen before this attempt-2 outcome.

G7 OPEN. G8 OPEN. G9 OPEN. Covariance/whitening CLOSED pending genuine Exp073P support PASS.
