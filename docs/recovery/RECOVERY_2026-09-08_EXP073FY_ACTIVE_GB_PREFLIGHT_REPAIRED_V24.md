# DSIR recovery — FY active / final GB preflight repaired V24

Date: 2026-09-08. Scope: DSIR only.

## Current heavy owner

Exp073FY namespace-repair V0.3 run `34160898921`, home job `101862390771`, remains the sole self-hosted heavy owner. The repaired frozen `WW_S2_S3` A/B gate remains in progress. No partial numerical payload was inspected and no competing self-hosted job was launched.

`WW_S2_S3` remains NOT ADMITTED until a real FZ provenance admission emits `PASS_EXP073FZ_WW_S2_S3_FILEBACKED_PROVENANCE_ADMISSION_V0_1` and `ww_s2_s3_authority_created=true`.

## Parallel hosted GA/GB preflight

While FY owned the home runner, a hosted-only audit was used prospectively to test the already-frozen final `WW_S3_S3` post-compute provenance path before any expensive GA execution.

### Exp073HA finding

Preregistration `experiments/073ha_ww_s3_s3_gb_provenance_static_audit_v0_1_prereg.md`, creation commit `dc776856b04f01a38bae1b2d425fa22e77ca71c9`.

Hosted run `34168565710`, job `101884366951`, failed support-only before any scientific payload because the original GB verifier blob `ee065b7d844090ae16386cc6944db23846d663ec` required lowercase transform token `exp073fw` in its exact pinned FX base blob `eb907944eac68b9fd13c405399cf238a8cb5bc96`; that token does not exist. This would have caused a future post-GA admission failure before reading the GA artifact. Classification: IMPLEMENTATION/PROVENANCE `+0/+0`, never scientific FAIL.

Prospective repair commit `2a6a3ea76d95202ff2bb6d87d9715ec4d9f28a00` removed only that nonexistent lowercase transform requirement. Intermediate GB blob was `075bb568f82407ec5ca2bdf8e598cfdac55dbe83`.

### Exp073HB finding

Preregistration `experiments/073hb_ww_s3_s3_gb_absent_lowercase_transform_repair_v0_1_prereg.md`, creation commit `0cb218e3fe6e49b656bdddf9b0aab7a4ba8ee9d3`.

Hosted run `34168722516`, job `101884804393`, then exposed a second deterministic transform-order defect: the earlier required `ww_s2_s2 -> ww_s3_s3` replacement already converts the authority key, so a later requirement to find `ww_s2_s2_authority_created` is impossible. This also is implementation/provenance `+0/+0`, not scientific evidence.

### Exp073HC repair and PASS

Preregistration `experiments/073hc_ww_s3_s3_gb_redundant_authority_transform_repair_v0_1_prereg.md`, creation commit `4f387e056f97acd523133b50f5f273c62551a731`.

Final prospective GB repair commit `7846c63765fcc8b1fc748fd7ecb25f88c1333a81` removed only the redundant long authority-key replacement while retaining the earlier exact substring transform and added explicit final/stale authority-key invariants. Current GB verifier blob is `cc815737e658a850452d9b0f9488e703f8de84ea`.

GA workflow rebinding commit `23b2253d02739c064bc539f28f8020de5069168c` binds `ADMIT_VERIFY_BLOB=cc815737e658a850452d9b0f9488e703f8de84ea`; current GA workflow blob is `7c408b877a5c0ddc96346cff74efffc1a1985687`. GA numerical driver, pruner, comparator, home wrapper, source ordering and science thresholds were unchanged.

Dedicated hosted audit workflow creation commit `f77ee669eb1f03e33daa1d86347c5977bd9e26bb` triggered Exp073HC run `34168906285`, hosted job `101885299058`, which completed SUCCESS. Raw log contains:
- `PASS_EXP073HC_REPAIRED_GB_TRANSFORM_INVARIANTS`
- `PASS_EXP073HC_REPAIRED_GA_GB_BINDING_INVARIANTS`
- `PASS_EXP073HC_WW_S3_S3_GB_REDUNDANT_AUTHORITY_TRANSFORM_REPAIR_STATIC_AUDIT_V0_1`
- `classification=SUPPORT_PLUS_0_PLUS_0`
- `ww_s3_s3_authority_created=false`

The successful static audit verifies that the transformed GB path still requires both pre-prune full-chain proofs, exact GA A/B PASS, live exclusivity, ordered `[3,3]` / `S3->S3`, same-field semantics, 19327352832-byte file-backed MCM, exact public adapter route, complete stage-manifest SHA binding, exact byte equality, finiteness, and no tolerance/rounding/smoothing/averaging rescue. It also verifies the repaired GB blob is exactly bound into GA's post-home provenance admission.

This is strictly prospective support `+0/+0`. It does not create `WW_S3_S3` authority. Only a future real Exp073GB execution over a successful GA artifact may do so.

## C2 parallel state

Exp073GZ runtime receipt contract static audit remains SUCCESS support-only. The next C2 transition remains real frozen 28-packet / 1792-byte runtime production/admission, still blocked by heavy-run exclusivity while FY owns the self-hosted runner.

## Next actions

1. Leave FY run `34160898921` undisturbed until terminal.
2. If FY succeeds, require real FZ provenance admission before any GA heavy start.
3. The dispatch-only GA workflow on `main` is now rebound to the HC-audited final GB verifier.
4. If FY fails, preserve complete valid checkpoints and diagnose first causal defect; do not blindly restart heavy work.
5. Do not start C2 real runtime while FY or GA owns the home runner.
