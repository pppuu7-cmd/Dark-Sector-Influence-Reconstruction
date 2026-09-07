# Exp073GM — C2 IDE observation-only hook build/no-mutation audit v0.1

Date: 2026-09-07

Hypothesis / scope authority: `C2_IDE_LOCAL_TANGENT_CONE` only.

Status before execution: **PREREGISTERED / NOT_YET_TESTABLE / +0/+0**.

## Purpose

Test only whether the already-audited pre-transform C2 observation site can be instrumented with a diagnostic-only hook in pinned `class_iv` without changing frozen scientific logic or solver state.

This experiment is not a C2 numerical prediction and cannot produce a scientific PASS/FAIL for the model.

## Frozen solver authority

- repository: `kaeonikc/class_iv`;
- commit: `ac627d54e9ce196a08878d1ba33999819925d19c`;
- source site: `source/perturbations.c`, inside `perturb_einstein()` immediately after the existing `perturb_total_stress_energy(...)` call and before any metric inference or gauge-independent transformation of `ppw->delta_m` / `ppw->theta_m`;
- predecessor eligibility: Exp073GL run `34093619964`, job `101652242887`, success;
- source-site audit: `docs/dsir4/mappings/C2_IDE_OBSERVATION_HOOK_SOURCE_SITE_AUDIT_V0_1.md`.

## Frozen patch contract

The patch may only add an `#ifdef DSIR_EXP073GM_DIAGNOSTICS` observation block at the source site above. The block may read and emit:

- `tau`;
- `k`;
- native `a`;
- native `H`;
- pre-transform `ppw->delta_m`;
- pre-transform `ppw->theta_m`;
- `rho_idm_iv`;
- `rho_iv`;
- gauge identifier.

It must not:

- write `ppw`, `y`, `pvecback`, `pvecmetric`, derivatives, approximation flags, precision settings, species sums, branch state, or integration state;
- call `background_at_tau`, `thermodynamics_at_z`, or any second cosmology/background calculation;
- alter equations, tolerances, frozen nodes, branch masks, thresholds, or hypothesis ID;
- emit a scientific gate decision.

The runtime output path is diagnostic I/O only and is disabled unless the compile-time macro is present and `DSIR_EXP073GM_DIAGNOSTICS=1` is set.

## Hard audit criteria

PASS only if all conditions hold:

1. pinned commit identity matches exactly;
2. the generator finds exactly one frozen source anchor;
3. removing the inserted diagnostic block restores `perturbations.c` byte-for-byte;
4. static forbidden-token checks find no state write or second cosmology call in the inserted block;
5. the patched `perturbations.c` compiles once with diagnostics disabled;
6. the patched `perturbations.c` compiles once with `-DDSIR_EXP073GM_DIAGNOSTICS` enabled;
7. no numerical C2 prediction is generated or interpreted by this workflow.

Any failure of cloning, dependency installation, patch anchoring, compilation, or audit implementation is **INFRASTRUCTURE/IMPLEMENTATION FAILURE +0/+0**, not a scientific FAIL.

A successful audit yields only:

`EXP073GM_HOOK_BUILD_NO_MUTATION = PASS_SUPPORT_ONLY`

and leaves:

- `prediction_ready = false`;
- `G_DOMAIN_MAPPING = NOT_YET_TESTABLE`;
- scientific contribution = `+0/+0`.

Numerical C2 extraction remains forbidden until this audit has a terminal successful run and its exact patch/source identities are recorded.
