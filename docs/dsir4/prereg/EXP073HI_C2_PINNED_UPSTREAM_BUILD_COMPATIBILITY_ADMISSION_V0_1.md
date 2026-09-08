# Exp073HI — C2 pinned-upstream build-compatibility admission v0.1

Status: **PROSPECTIVELY FROZEN BEFORE EXP073HI EXECUTION**. Scope: DSIR only.

## Purpose

Exp073HB is blocked before any cosmological execution because the exact upstream source tree `kaeonikc/class_iv@ac627d54e9ce196a08878d1ba33999819925d19c` does not build on the current hosted GCC/GSL toolchain. This gate admits, at most, one exact **build-compatible derivative** of that source tree for subsequent diagnostic C2 support work. It creates no scientific/model authority and changes no frozen DSIR science.

The immutable upstream provenance remains the parent commit. The derivative must always be identified by both the parent commit/blob identities and the exact compatibility-patch fingerprint; it must never be represented as the unmodified upstream commit.

## Frozen parent identities

- upstream commit: `ac627d54e9ce196a08878d1ba33999819925d19c`
- `source/background.c` Git blob: `310e0f5764ab41da3a886ed239db3fff2aac32ec`
- `Makefile` Git blob: `45f912a2b8b2849998affb6857f49f5950fe9be5`
- compatibility implementation: `scripts/dsir4/exp073hb_pinned_class_iv_build_compat_v0_1.py`
- compatibility implementation Git blob: `b7fe663154519b605699c1fd622d0079a5f76772`

## Frozen allowed transformation — exactly three build surfaces

No other source/build file may change in Exp073HI.

1. `source/background.c`: remove exactly the single switch-closing brace between the existing EDE `break;` and existing `case IDM_IV:`. No expression, numeric literal, assignment, function call, case body, or equation token may change.
2. `Makefile`: append only `-fcommon` to `OPTFLAG = -O2` to restore the legacy tentative-common-symbol semantics required by this historical source tree on modern GCC.
3. `Makefile`: move only `-lgsl -lgslcblas` from the generic `LDFLAG` position to after the object list in the final `class` link command. No compiler optimization, OpenMP, HYREC, include, object, or mathematical library selection may otherwise change.

The exact transformed-file SHA256 values are prospectively frozen from the deterministic transform implementation, not from any scientific result:

- transformed `source/background.c` SHA256: `bc4053922ae984652f5858b2869e7bbbe8682ea502b88e485709e6828e059ce0`
- transformed `Makefile` SHA256: `2bb326590b3d0c3a23e984fc17cafce680674aa5234db15d35d72a06e1bfa87e`

## Required hosted admission checks

Exp073HI PASS requires all of the following in one raw hosted log:

- exact parent commit/blob/compat-script identities;
- exact one-brace source transformation and exact two Makefile transformations;
- whole-tree diff proves only `source/background.c` and `Makefile` changed;
- transformed-file SHA256 values equal the frozen values above;
- token/line audit proves the `background_w_fld` numerical expressions and the full `IDM_IV` case body are byte-identical apart from the one removed brace;
- full `make -j2 class` succeeds after installing only the hosted GSL development dependency;
- executable `./class` exists but is **not executed**;
- no cosmological run, C2 record, payload, prediction, mapping, or scientific authority is created.

## Frozen classification and PASS token

Only this exact PASS token admits the derivative for later support-only HB execution:

`PASS_EXP073HI_C2_PINNED_UPSTREAM_BUILD_COMPATIBILITY_ADMISSION_V0_1`

A PASS must also emit exactly:

- `classification=SUPPORT_PLUS_0_PLUS_0`
- `build_compatible_derivative_admitted=true`
- `cosmological_run_started=false`
- `record_payload_created=false`
- `runtime_record_count=0`
- `prediction_ready=false`
- `scientific_model_authority_created=false`
- `G_DOMAIN_MAPPING=NOT_YET_TESTABLE`

Any identity/diff/hash/build mismatch is implementation/infrastructure `+0/+0` and creates no admission. A successful compile alone is not PASS unless every frozen check and token above is present in the raw log.

## Consequence

Only after a raw-log validated Exp073HI PASS may a prospectively rebound HB workflow use this exact derivative, with provenance explicitly naming both the upstream parent and Exp073HI compatibility fingerprint. The earlier HB run on an unadmitted derivative remains historical implementation evidence and cannot be retroactively promoted.
