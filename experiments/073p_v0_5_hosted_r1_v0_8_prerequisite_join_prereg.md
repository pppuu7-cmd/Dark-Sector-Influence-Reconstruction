# Exp073P v0.5 — hosted Exp073R1 v0.8 prerequisite join — preregistration

**Frozen:** 2026-08-29 while the bound R1 v0.8 run is still `in_progress`, before its terminal result and before any v0.5 receipt exists.

## Purpose

Replace the operational dependence on the unavailable home/self-hosted R1 route with a fail-closed GitHub-hosted prerequisite receipt. This join is authority/provenance only. It must not compute physical support, covariance, nuisance quantities, relation/null statistics, G7, G8 or G9.

## Sole bound R1 candidate

Freeze exactly:

- workflow run ID: `33270843577`;
- job ID: `99148916507`;
- run event: `push`;
- run head: `ef783ca941fb9b9b5f5eae537986c56ff06e6536`;
- workflow path: `.github/workflows/exp073r1-desy1-github-hosted-wholestream-retry-v0-8.yml`;
- workflow ID: `345506303`;
- expected artifact name: `exp073r1-v08-hosted-wholestream-ef783ca941fb9b9b5f5eae537986c56ff06e6536`;
- authority-freeze parent commit: `9c950247799ff09a9df62e39aa508588125da031`;
- trigger commit changes only `ci/exp073r1_v0_8_hosted_wholestream_retry.trigger` and contains that exact authority parent.

Protected blobs already frozen before launch:

- v0.8 prereg `eecb24cdf4012fdb95f660b0cfe21b61be774b8a`;
- v0.8 transport wrapper `976ede2c62c781d08c7f77c013c25c5bf818cb03`;
- v0.8 workflow `27007861423964e30ca05aa60765fdb6a44a9fff`;
- frozen v0.5 mapper `46fe1271d97ddd9e2164d24e7d79cf27bfda805d`.

No other v0.8 run may substitute for this candidate under this preregistration.

## PASS prerequisites

A receipt may be `PASS_EXP073P_PREREQUISITE_BINDING_V0_5_HOSTED` only if all are true:

1. run `33270843577` is terminal `completed/success`;
2. job `99148916507` is terminal `completed/success`;
3. the authority-binding step, parent-metadata step, downloaded-parent internal-contract step, hosted mapper/retry step, and final genuine reproduction assertion all concluded `success`;
4. exactly one non-expired artifact with the frozen expected name exists;
5. the GitHub-reported artifact SHA256 digest is recorded verbatim in the receipt;
6. downloaded transport provenance has status `PASS_EXP073R1_V08_HOSTED_RATE_QUALIFIED_WHOLESTREAM`, zero Range requests, all routes starting at byte 0, at least one complete 84,075,649,920-byte route, and the frozen execution-only gate state;
7. downloaded mapper summary has status `PASS_DESY1_FULL_ONEPASS_WEAK_LENSING_MASK_EXP073R1`, exact metacal SHA256 `39a7fe03e54d96b85cee2fb523ea108c2a548ba1584368203f0464ed6241ebc8`, exact source whole/index identities, exact 136,930,995 row counts, frozen selection and mapper, zero out-of-range pixels, nonzero selected rows in all four bins, parent-R0 checks all true and repeatability all true;
8. both downloaded records assert `science_gate_scored=false`, `f_invalid_computed=false`, `covariance_read=false`, `G8_read=false`, `G7/G8/G9=OPEN`.

Only that PASS receipt may set `support_executor_authorized=true`.

## Non-PASS taxonomy

- bound R1 run/job terminal non-success, hosted timeout, transport exhaustion, runner interruption, or missing output because execution never reached a trustworthy terminal reproduction result -> `INCOMPLETE_EXP073P_PREREQUISITE_BINDING_V0_5_HOSTED`;
- run/head/workflow/job/artifact identity mismatch, duplicate artifact, malformed or contradictory provenance, wrong SHA/row/mapper/selection values, downstream payload leakage, or a success claim lacking all frozen assertions -> `INVALID_FOR_SCIENCE_EXP073P_PREREQUISITE_BINDING_V0_5_HOSTED`.

Neither class is evidence against any physical model. Both require `support_executor_authorized=false`.

## Receipt schema minimum

Record:

- `synthetic=false`;
- exact run ID, job ID, head, workflow path/ID;
- exact artifact ID/name/GitHub digest when present;
- protected blob identities;
- all bound step conclusions;
- exact mapper and transport PASS tokens if present;
- `scientific_classification=null`;
- `science_gate_scored=false`;
- `f_invalid_computed=false`;
- `covariance_read=false`;
- `G8_read=false`;
- `gate_state={G7:OPEN,G8:OPEN,G9:OPEN}`;
- `support_executor_authorized=true` only for the exact PASS class.

## Downstream boundary

This receipt is not Article-3 physical support. Even a PASS authorizes only the separately frozen real Article-3 coordinate-level support executor. Covariance/whitening remains blocked until `PASS_PHYSICAL_SUPPORT_ARTICLE3` exists under its unchanged criteria.