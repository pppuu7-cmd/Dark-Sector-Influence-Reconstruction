# Article-3 provisional evidence / exact-recompute ledger — 2026-08-31

This ledger implements `Exp073BB` dual-track policy. Entries here are **not scientific authority** and add `+0` readiness.

## Status vocabulary

- `P1 PROVISIONAL_BRANCH_ROBUST_MANUSCRIPT_ELIGIBLE` — all complete propagated branches support the same qualitative conclusion under frozen downstream rules; may orient the working manuscript with explicit provisional labeling.
- `P2 PROVISIONAL_NUMERICALLY_SENSITIVE_RECOMPUTE_PRIORITY` — branch spread changes a scientific conclusion/boundary; do not use as a positive manuscript claim.
- `P3 PROVISIONAL_INCOMPLETE_NO_DOWNSTREAM_USE` — incomplete/malformed/missing branch; do not propagate.

Every central provisional item has `recompute_before_final_submission=true` until later Track-A authority supersedes it.

---

## P-001 — Wm_S1 Exp073AQ complete A/B branch pair

**Authority status:** Exp073AQ remains permanent hosted exact repeatability FAIL. This ledger entry does not alter that classification.

Source:

- run `33327372191`;
- A job `99299799192`, artifact `9739721339`, artifact digest `sha256:ec6ab1e6a602bd37f7a781a5e8030b09171905e5800b0cfeeba6fabe06e195a1`;
- B job `99299799338`, artifact `9739045909`, artifact digest `sha256:4069f4deb3c608f6fb2c1fa686181746901befbe945cc07374c7d32346778e2f`;
- comparator authority artifact `9739725913`, digest `sha256:5184bb3034bd2c1bd497ad30db3dbd4e1550d09a0c25af328cdee553385fef03`.

Exact-authority result:

`SCIENTIFIC_REPEATABILITY_FAIL_EXP073AQ_WM_S1_CONTROLLED_TWIN_EXACT_V0_1`.

Branch diagnostics on selected `<f8 [39,12288]` arrays:

- differing entries `472997 / 479232`;
- maximum absolute difference `2.0816681711721685e-17`;
- mean absolute difference `2.5248672723363528e-20`;
- `max(abs(A)) = max(abs(B)) = 0.04906169081530385`;
- `max|delta| / max|W| = 4.2429605188470844e-16`;
- RMS(delta)/RMS(A) = `2.193471255136272e-16`;
- sign-bit mismatch count = `0`;
- zero/nonzero mismatch count = `0`;
- max relative difference of per-band `sum(abs(W))` = `4.130423023448714e-16`.

### Current provisional class

`P1-INPUT PROVISIONAL_WM_S1_BRANCH_PAIR_ELIGIBLE_FOR_DOWNSTREAM_SENSITIVITY_PROPAGATION`

This is deliberately narrower than a downstream P1 scientific claim. It says only that both complete branches are suitable for parallel propagation. No Layer-A/Layer-B/support claim is pre-awarded.

### Allowed working use

- use both A and B, never select one;
- construct provisional downstream quantities separately for A and B;
- report branch envelope/range;
- provisional manuscript statements become P1 only if both downstream branches preserve the same frozen classification/qualitative conclusion.

### Exact-recompute priority

`HIGH` because Wm_S1 belongs to the 14-window authority needed before real Exp073AR/AS and because the exact route failed.

`recompute_before_final_submission = true`.

Track-A recovery is currently Exp073AZ -> Exp073BA low-memory deterministic succession.

---

## Pending entries

Future Wm_S2/Wm_S3/WW provisional results are added only after complete branch outputs exist. Partial jobs are P3 and are not used downstream.

For each new item record:

1. exact source provenance;
2. all complete branches;
3. branch spread metrics;
4. frozen downstream decision on every branch;
5. P1/P2/P3 class;
6. manuscript dependency;
7. exact-recompute priority;
8. later authoritative supersession without deleting the historical provisional entry.
