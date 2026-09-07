# Exp073GN — C2 IDE hook ABI/build equivalence v0.1

Status: PROSPECTIVELY FROZEN BEFORE ANY C2 NUMERICAL PREDICTION.
Scope: DSIR only. Classification ceiling: `SUPPORT_PLUS_0_PLUS_0`.

## Frozen predecessor

This gate is permitted only after repaired Exp073GM run `34098464411`, job `101667247380`, emitted exact token `PASS_EXP073GM_C2_IDE_OBSERVATION_ONLY_HOOK_STATIC_AUDIT_V0_1` for pinned `kaeonikc/class_iv@ac627d54e9ce196a08878d1ba33999819925d19c`.

GM froze the exact observation-only insertion transform. GN must not alter that transform, hook site, argument order, matter convention, source arithmetic, cosmology, numerical settings, or scientific acceptance criteria.

## GN question

Does the exact GM-instrumented pinned solver remain buildable/linkable when the observation ABI is supplied as a no-op read-only diagnostic function, while the uninstrumented pinned solver also builds from the same source lineage and toolchain?

## Frozen no-op ABI

The only GN observer implementation is `scripts/dsir4/fixtures/dsir_c2_pretransform_hook.h`. It is a `static inline void dsir_c2_pretransform_observe(...)` accepting exactly the eight scalar arguments frozen by GM: `tau,k,a,H,delta_m,theta_m,rho_idm_iv,rho_iv`. Its body may only cast those inputs to `(void)` and return implicitly. It may not allocate, perform I/O, mutate solver state, call CLASS functions, branch on values, calculate a scientific observable, or emit a scientific decision.

## Hosted audit procedure

1. Clone two independent checkouts of the exact pinned class_iv commit.
2. Build the uninstrumented checkout with the hosted compiler/toolchain.
3. Apply the exact committed GM transformer to the second checkout.
4. Copy only the frozen no-op ABI header into its `include/` directory.
5. Build/link the instrumented checkout with `DSIR_C2_PRETRANSFORM_HOOK` defined.
6. Re-run the GM static auditor on the instrumented source identity.
7. Require both `class` executables to exist and be executable.

This is compile/link validation only. No cosmological run, C2 prediction, tangent response, downstream gate, or partial scientific output may be generated or inspected by GN.

## Classification

Exact PASS token: `PASS_EXP073GN_C2_IDE_HOOK_ABI_BUILD_EQUIVALENCE_V0_1`.

PASS => `SUPPORT_PLUS_0_PLUS_0`, `prediction_ready=false`, `scientific_model_authority_created=false`, `G_DOMAIN_MAPPING=NOT_YET_TESTABLE`. It may authorize only a separately prospectively frozen diagnostic-recorder implementation/audit stage. It does not authorize numerical C2 prediction generation by itself.

Any build, ABI, source identity, dependency, or static-audit failure is `IMPLEMENTATION_OR_INFRASTRUCTURE_PLUS_0_PLUS_0` / `INVALID_FOR_SCIENCE`, never scientific model FAIL.
