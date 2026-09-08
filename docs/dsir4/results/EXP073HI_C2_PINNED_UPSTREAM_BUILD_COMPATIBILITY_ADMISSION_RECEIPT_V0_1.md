# Exp073HI validated admission receipt v0.1

Scope: DSIR only. This receipt records a raw-log validated hosted support gate; it creates no scientific/model authority.

## Provenance

- prereg creation commit: `9e39633773bcdc8a133fdd3625a4569465044b2b`
- prereg blob: `030fac1023c1f811c1832cd0ec01060b27a613a7`
- workflow/head commit: `8afb6ddc421a996455c861797291e2d4c36f439a`
- GitHub Actions run: `34224810650`
- job: `102056219075 SUCCESS`
- upstream parent: `kaeonikc/class_iv@ac627d54e9ce196a08878d1ba33999819925d19c`
- parent `source/background.c` Git blob: `310e0f5764ab41da3a886ed239db3fff2aac32ec`
- parent `Makefile` Git blob: `45f912a2b8b2849998affb6857f49f5950fe9be5`
- compatibility script blob: `b7fe663154519b605699c1fd622d0079a5f76772`

## Raw-log validated identities and outputs

The terminal raw job log contains all of:

- `PASS_EXP073HI_PARENT_IDENTITIES_V0_1`
- `EXP073HB_PINNED_UPSTREAM_STRAY_BRACE_REMOVED_EXACTLY_ONCE`
- `EXP073HB_PINNED_UPSTREAM_MODERN_LINK_COMPAT_APPLIED_EXACTLY`
- `PASS_EXP073HI_EXACT_TRANSFORM_SEMANTIC_SURFACE_V0_1`
- `PASS_EXP073HI_WHOLE_TREE_DIFF_AND_HASH_V0_1`
- build-compatible derivative patch SHA256 `b96ff685d65f4857714fb6ed915e7af243fa0333d7e80b68100669cbfc122cd1`
- transformed `source/background.c` SHA256 `bc4053922ae984652f5858b2869e7bbbe8682ea502b88e485709e6828e059ce0`
- transformed `Makefile` SHA256 `2bb326590b3d0c3a23e984fc17cafce680674aa5234db15d35d72a06e1bfa87e`
- `PASS_EXP073HI_BUILD_COMPATIBLE_DERIVATIVE_COMPILES_V0_1`
- `classification=SUPPORT_PLUS_0_PLUS_0`
- `build_compatible_derivative_admitted=true`
- `cosmological_run_started=false`
- `record_payload_created=false`
- `runtime_record_count=0`
- `prediction_ready=false`
- `scientific_model_authority_created=false`
- `G_DOMAIN_MAPPING=NOT_YET_TESTABLE`
- final exact token `PASS_EXP073HI_C2_PINNED_UPSTREAM_BUILD_COMPATIBILITY_ADMISSION_V0_1`

## Classification

`EXP073HI = SUPPORT_PLUS_0_PLUS_0 / BUILD_COMPATIBLE_DERIVATIVE_ADMITTED`.

The derivative is admitted only as the exact parent-plus-compatibility fingerprint above. It must never be described as the unmodified upstream commit. No cosmological execution occurred, no C2 payload was created, and no DSIR scientific authority was changed.

## Consequence

A new prospectively frozen HB version may now apply the diagnostic exact-endpoint producer patch to this admitted derivative. The earlier HB run `34224529036` predates this admission and remains implementation evidence only; it cannot be retroactively promoted.
