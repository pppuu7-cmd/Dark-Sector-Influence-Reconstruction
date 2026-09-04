# Exp073DE v0.2 — exact full-window resume repair

Date: 2026-09-04. Scope DSIR only. Support/infrastructure `+0/+0`.

## Historical predecessor
Exp073DE v0.1 run/job `33885148897 / 101062989940` is immutable `P2_PRODUCTION_DURABILITY_HOOK_IMPLEMENTATION_FAIL +0/+0`. Raw artifact `9941509491` (ZIP SHA256 `b110ea3c92e054e183d8c4ac574a6aff613f7f29bdcc9317fb08ef491eb2d0a1`) identified the first causal defect before remote-hook integration: production driver v0.1 loads `full_window_complete` but, when `selected_te_complete` is absent, replays `execute_exact_adapter` and therefore recomputes the verified full window.

## Frozen repair
Do not change the admitted full-window arithmetic. Add a resume-only helper that consumes an already verified canonical `<f8` full window of exact shape `[2,39,2,12288]`, takes exactly `full[0,:,0,:]`, applies the same contiguous `<f8` canonicalization used by the admitted adapter, and writes the exact selected-TE bytes. This is the same operation frozen in adapter blob `dafe86086a470c852106f0d4ecccbda1d389e397`: `te=canon(full[0,:,0,:]); te_path.write_bytes(memoryview(te).cast('B'))`.

The helper must fail closed on wrong byte size, dtype/shape contract or full-file SHA mismatch supplied by the caller. It must not compute or alter MCM/full-window values and must not use tolerance, rounding, smoothing or averaging.

Hosted synthetic regression must construct deterministic canonical full-window bytes, compute TE once by the literal admitted reference expression and once through the resume helper, and require exact SHA256 equality, `numpy.array_equal`, max absolute difference exactly `0.0`, exact bytes equality, and unchanged source full SHA before/after.

## Frozen classifications
- `Q1_FULL_WINDOW_RESUME_EXACT_PASS`: exact resume helper is byte-identical to the admitted TE selection and leaves full payload unchanged. Permits prospective durability wrapper integration.
- `Q2_FULL_WINDOW_RESUME_EXACTNESS_FAIL`: exact bytes/array equality fails; negative support result, no repair by tolerance.
- `Q3_FULL_WINDOW_RESUME_FAILCLOSED_FAIL`: malformed/corrupt full input is not rejected.
- `Q4_INFRASTRUCTURE_OR_SOURCE_BINDING_FAIL`: hosted/source failure prevents evaluation.

No DES-scale numerics, Exp073BU activation or Wm_S3 authority creation is permitted in this gate.
