# Research log — 2026-09-07 — Auto-guard turn 10 / Exp073GM

## Orchestration audit

Fresh GitHub Actions audit found exactly one pre-existing in-progress workflow before this turn:

- Exp073FU `WW_S1_S3` resume run `34103803637`;
- hosted launch-audit job `101684090730`: `SUCCESS`;
- self-hosted `home-science` job `101684145754`: `IN_PROGRESS` in the frozen `WW_S1_S3 A/B gate` compute step.

No queued duplicate heavy-run and no second active heavy-run were present. The running job therefore remains the sole heavy authority. No restart, rerun, cancellation, or duplicate heavy launch was performed.

No new terminal infrastructure failure or scientific FAIL was found in the active chain during this audit. The current `WW_S1_S3` result remains **NOT YET ADMITTED** until terminal evidence and downstream provenance admission exist.

## Next permitted DSIR4 step advanced in parallel

Because the heavy authority was healthy, the next non-heavy C2 prerequisite was advanced under the frozen `C2_IDE_LOCAL_TANGENT_CONE` order.

Created:

1. `scripts/dsir4/make_exp073gm_c2_observation_hook.py`
   - commit `1511bfb1f3883f161e7d88c6eae5288114558b40`;
   - fail-closed source anchor;
   - diagnostic block only;
   - byte-for-byte source-equivalence proof after removing the inserted block;
   - explicit rejection of second cosmology calls and state writes.

2. `docs/dsir4/prereg/EXP073GM_C2_IDE_OBSERVATION_HOOK_BUILD_AUDIT_V0_1.md`
   - commit `e3598f3dd215e959f63bd887c222986e033b00b1`;
   - prospectively freezes the build/no-mutation criteria before any C2 numerical prediction is generated.

3. `.github/workflows/exp073gm-c2-ide-observation-hook-build-audit-v0-1.yml`
   - commit `12275f15b8a6cc58b0d2c49b2735116f8d537b72`;
   - hosted-only static/build audit;
   - clones pinned `kaeonikc/class_iv@ac627d54e9ce196a08878d1ba33999819925d19c`;
   - compiles the patched source both with diagnostics disabled and with `-DDSIR_EXP073GM_DIAGNOSTICS` enabled;
   - generates no C2 numerical prediction.

The push launched hosted Exp073GM run `34109272397`, job `101701467632`. At logging time the job is `IN_PROGRESS`; setup and checkout are complete and dependency installation is running. This hosted audit is not a heavy-run and does not duplicate the active self-hosted `WW_S1_S3` computation.

## Classification

- pre-existing heavy chain: healthy / in progress;
- Exp073GM: infrastructure/interface support test only;
- C2 `mapping_ready = true`;
- C2 `source_site_ready = true`;
- C2 hook build/no-mutation admission: pending terminal Exp073GM result;
- `prediction_ready = false`;
- `G_DOMAIN_MAPPING = NOT_YET_TESTABLE`;
- scientific contribution this turn: `+0/+0`;
- new scientific FAIL: none.

`INVALID_FOR_SCIENCE`, `NOT_YET_TESTABLE`, `OUTSIDE_DOMAIN`, workflow/build failures, and missing terminal evidence remain explicitly non-scientific states unless a preregistered scientific gate is actually executed on valid admitted evidence.
