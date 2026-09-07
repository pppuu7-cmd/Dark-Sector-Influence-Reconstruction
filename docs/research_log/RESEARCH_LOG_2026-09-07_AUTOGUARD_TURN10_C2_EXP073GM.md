# Research log — 2026-09-07 — Auto-guard turn 10 / Exp073GM

## Orchestration audit

Fresh GitHub Actions audit found exactly one pre-existing in-progress heavy workflow before this turn:

- Exp073FU `WW_S1_S3` resume run `34103803637`;
- hosted launch-audit job `101684090730`: `SUCCESS`;
- self-hosted `home-science` job `101684145754`: `IN_PROGRESS` in the frozen `WW_S1_S3 A/B gate` compute step.

No queued duplicate heavy-run and no second active heavy-run were present. The running job therefore remains the sole heavy authority. No restart, rerun, cancellation, or duplicate heavy launch was performed.

The current `WW_S1_S3` result remains **NOT YET ADMITTED** until terminal evidence and downstream provenance admission exist.

## Next permitted DSIR4 step advanced in parallel

Because the heavy authority was healthy, the next non-heavy C2 prerequisite was advanced under the frozen `C2_IDE_LOCAL_TANGENT_CONE` order.

Created:

1. `scripts/dsir4/make_exp073gm_c2_observation_hook.py`
   - initial commit `1511bfb1f3883f161e7d88c6eae5288114558b40`;
   - fail-closed source anchor;
   - diagnostic block only;
   - explicit rejection of second cosmology calls and state writes.

2. `docs/dsir4/prereg/EXP073GM_C2_IDE_OBSERVATION_HOOK_BUILD_AUDIT_V0_1.md`
   - commit `e3598f3dd215e959f63bd887c222986e033b00b1`;
   - prospectively froze build/no-mutation criteria before any C2 numerical prediction.

3. `.github/workflows/exp073gm-c2-ide-observation-hook-build-audit-v0-1.yml`
   - initial commit `12275f15b8a6cc58b0d2c49b2735116f8d537b72`;
   - hosted-only static/build audit;
   - pinned `kaeonikc/class_iv@ac627d54e9ce196a08878d1ba33999819925d19c`;
   - no C2 numerical prediction generated.

## Exp073GM infrastructure failure and repair

Initial run:

- run `34109272397`;
- job `101701467632`;
- conclusion: `FAILURE` at the dry-run structural-equivalence step before compilation and before any numerical science.

Exact logged cause:

`FAIL: patched source is not source-equivalent after removing diagnostic block`

Root cause: the audit implementation removed a newline-delimited regex region rather than the exact inserted byte string, leaving a newline-normalisation mismatch. This was an audit/matcher defect only; it did not alter or test scientific equations, thresholds, frozen nodes, branch masks, or hypothesis ID.

Classification: **INFRASTRUCTURE/IMPLEMENTATION FAILURE +0/+0**, explicitly not a scientific FAIL.

Repair:

- generator repaired to prove equivalence by removing the exact `BLOCK` bytes: commit `0bc4a832e610dd821d51616aa9f7cdb6d38cba98`;
- workflow structural check repaired to import and remove that same exact `BLOCK`: commit `cb31dd38a21d968b75d1c392bf3abb820b0ab270`.

No scientific contract changed.

## Terminal repaired Exp073GM result

Authoritative repaired run:

- run `34109396865`;
- job `101701865122`;
- head SHA `cb31dd38a21d968b75d1c392bf3abb820b0ab270`;
- conclusion: `SUCCESS`.

All frozen audit steps passed:

- pinned clone identity;
- dry-run exact patch contract;
- exact structural source equivalence;
- static no-mutation audit;
- compile with diagnostics disabled;
- compile with `-DDSIR_EXP073GM_DIAGNOSTICS` enabled.

Recorded source identities from the terminal log:

- pinned `source/perturbations.c` SHA256 before patch: `61e73ed7d5b785ea5f49620e782c58ec552d2735640a1c1241d5ef354e7e0cbe`;
- patched source SHA256: `33d3425d7b8822b027f6b2a1f2155dec98d6f3c56d93351e057217c5cbbca91b`.

Terminal support statements:

- `EXP073GM_SOURCE_EQUIVALENCE_MODULO_DIAGNOSTIC_BLOCK=PASS`;
- `EXP073GM_STATIC_NO_MUTATION_AUDIT=PASS`;
- `EXP073GM_HOOK_BUILD_NO_MUTATION=PASS_SUPPORT_ONLY`;
- `EXP073GM_SCIENTIFIC_CONTRIBUTION=+0/+0`;
- `EXP073GM_G_DOMAIN_MAPPING=NOT_YET_TESTABLE`.

## Scientific status

- pre-existing heavy chain: healthy / in progress;
- C2 `mapping_ready = true`;
- C2 `source_site_ready = true`;
- C2 diagnostic hook build/no-mutation eligibility = `PASS_SUPPORT_ONLY`;
- C2 deterministic numerical prediction artifact = absent;
- `prediction_ready = false`;
- `G_DOMAIN_MAPPING = NOT_YET_TESTABLE`;
- new scientific FAIL: none.

`INVALID_FOR_SCIENCE`, `NOT_YET_TESTABLE`, `OUTSIDE_DOMAIN`, workflow/build failures, and missing terminal evidence remain explicitly non-scientific states unless a preregistered scientific gate is actually executed on valid admitted evidence.

Next permitted C2 step is a separate prospectively frozen deterministic extraction/generation contract using the admitted hook. It must not start a competing heavy-run while Exp073FU run `34103803637` remains active.
