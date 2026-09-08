# Exp073HK — C2 HJ deterministic output fingerprint derivation v0.1

Status: **PROSPECTIVELY FROZEN BEFORE EXECUTION**. Scope: DSIR only. Scientific ceiling: `SUPPORT_PLUS_0_PLUS_0`.

## Purpose

Derive, before Exp073HJ build-audit execution, the deterministic SHA256 of `source/perturbations.c` after applying exactly: admitted Exp073HI build compatibility, frozen Exp073HB producer patch, then committed Exp073HJ observation-only extension. HK is only an implementation fingerprint derivation gate. It does not compile or execute cosmology and cannot create runtime/scientific authority.

## Frozen inputs

- parent `kaeonikc/class_iv@ac627d54e9ce196a08878d1ba33999819925d19c`;
- Exp073HI compatibility script blob `b7fe663154519b605699c1fd622d0079a5f76772`;
- Exp073HB producer script blob `f3d3d80cda2f937f544722e684a44c649e771487`;
- Exp073HB patched perturbations SHA256 `da7c427e383f1e9b83d7ff75ef82784c2fe89d91f9681e21e7805b7f354e7e79`;
- Exp073HJ extension script blob `9096eddfb592703ef6a2adc82bf27db05bee9ee0`;
- HJ prereg creation commit `d79784e1c980c879fe52d074e308e09347db0fee`.

## Frozen procedure

Hosted-only workflow must clone exact parent, verify parent source identities, apply exact HI transform, verify admitted derivative identities, apply exact HB transform and verify the frozen HB source hash, apply exact HJ transform once, and print only its deterministic final `source/perturbations.c` SHA256 plus support markers. It must run `git diff --check`.

It MUST NOT compile or execute `./class`, create a cosmological result, create a binary runtime record/payload, decode/map any scientific field, or claim HJ PASS.

Exact token:

`PASS_EXP073HK_C2_HJ_OUTPUT_FINGERPRINT_DERIVATION_V0_1`

required with `classification=SUPPORT_PLUS_0_PLUS_0`, `cosmological_run_started=false`, `record_payload_created=false`, `prediction_ready=false`, `scientific_model_authority_created=false`.

The emitted final SHA may be used only to prospectively bind a later HJ workflow commit. Any failure is implementation/infrastructure `+0/+0`, never scientific FAIL.
