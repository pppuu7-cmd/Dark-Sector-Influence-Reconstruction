# DSIR immutable recovery — V34

Date: 2026-09-08. Scope: **DSIR only**. RTK/RQIR excluded.

## Preserved authority

All V33 scientific authority is preserved unchanged. In particular `WW_S3_S3` remains `SCIENTIFIC_AUTHORITY_ADMITTED` through recovery-admission run `34218457380 / 102035691774`, consuming GA artifact `10051382493`, digest `sha256:a192f50de34dc74f575b86e8ff1e6f7c92b9a9bb009d9d0ea6ff4ff6208f4109`.

C2 remains `prediction_ready=false`, `scientific_model_authority_created=false`, `G_DOMAIN_MAPPING=NOT_YET_TESTABLE`.

## Exp073HK — consumed implementation-fingerprint PASS

Hosted run `34227090985`, job `102063746865 SUCCESS`, head `1a8110e84bda1152a94c56469db7ad3bc90d6ba2` was raw-log consumed. It exactly reconstructed HI+HB source, applied committed HJ extension blob `9096eddfb592703ef6a2adc82bf27db05bee9ee0`, and emitted deterministic final `source/perturbations.c` SHA256:

`f1a5619ea2dfb60e4e236349485dcffb58c1c2ef96358bd59b8a1207d77248d2`.

Exact token: `PASS_EXP073HK_C2_HJ_OUTPUT_FINGERPRINT_DERIVATION_V0_1`; classification `SUPPORT_PLUS_0_PLUS_0`; no compile, no cosmological run, no payload, no science authority.

## Exp073HJ — raw-log validated PASS

Prospective prereg creation commit `d79784e1c980c879fe52d074e308e09347db0fee`, prereg blob `16009f3a0016dc0fb04c0271af954bd6fc76f9e8`; implementation commit `50fc7378dfcae35df7a731c643098c205f00d30e`, extension blob `9096eddfb592703ef6a2adc82bf27db05bee9ee0`; workflow/head commit `f20bf0a0a3db41702ad30d1b44bf5b8ff0c4e900`.

Run `34227197810`, job `102064106469 SUCCESS` was consumed from raw log. It verified the prospectively fingerprinted final source SHA above, static no-second-background/interpolation invariance, exact eight-field observation order

`tau,k,a,H,delta_m,theta_m,rho_idm_iv,rho_iv`,

and compiled the full admitted derivative successfully without executing CLASS cosmology.

Exact final raw-log boundary:

`PASS_EXP073HJ_C2_COMPLETE_NATIVE_RECORD_PRODUCER_BUILD_AUDIT_V0_1`

with `classification=SUPPORT_PLUS_0_PLUS_0`, `complete_eight_field_observation_verified=true`, `native_endpoint_background_workspace_verified=true`, `diagnostic_producer_compile_verified=true`, `cosmological_run_started=false`, `record_payload_created=false`, `runtime_record_count=0`, `prediction_ready=false`, `scientific_model_authority_created=false`, `G_DOMAIN_MAPPING=NOT_YET_TESTABLE`.

Therefore HJ is support PASS only. No binary runtime record or scientific value was created or inspected.

## Newly discovered pre-runtime implementation guard issue

Before launching any C2 runtime, source audit found an important producer guard mismatch:

1. the immutable legacy zero-interaction baseline is exactly `output = mPk`;
2. pinned CLASS sets `ppt->has_source_delta_m = _TRUE_` whenever `has_pk_matter` is true;
3. in `perturb_total_stress_energy`, native total-matter momentum accumulation and assignment of `ppw->theta_m` are executed whenever `(ppt->has_source_delta_m == _TRUE_) || (ppt->has_source_theta_m == _TRUE_)`;
4. therefore the legacy `mPk` baseline already computes native `ppw->theta_m` as part of the total-matter source path;
5. the HB observation-only `dsir_c2_diag_prepare` nevertheless requires **both** `has_source_delta_m` and `has_source_theta_m`, where the latter is independently enabled by number-count RSD logic and is not required for the already-executed native total-matter calculation.

Thus a real baseline runtime under unchanged `output=mPk` would fail the diagnostic guard before producing a record despite the required native `theta_m` already being computed. Adding RSD/nCl merely to satisfy this observer guard would introduce an unnecessary output/config change.

This is classified **prospective implementation/observation guard incompleteness +0/+0**, not scientific FAIL and not a relaxation of any scientific acceptance criterion. No runtime was attempted and no result exists to rescue.

## Exact next permitted gate

Prospectively freeze and hosted-audit the smallest post-HJ observation-only guard correction: require native `has_source_delta_m=true` for this mPk-backed C2 diagnostic, while statically proving the pinned source still computes both `ppw->delta_m` and `ppw->theta_m` under the delta-m source path. Preserve all HJ endpoint, source hash chain, exact z/k, accepted-ynew, pre-transform and eight-field observation semantics. No cosmology may be executed by this repair audit.

Only after raw-log PASS may the real runtime producer be frozen against the unchanged legacy baseline `output=mPk` and frozen p8 configuration.

## Runtime boundaries preserved

Frozen C2 runtime receipt remains blob `1c2e30e6563efe3976ee0b1825dfb250a902a529`: exact z `[0.295,0.51,0.706,0.934,1.317,1.491,2.33]`, k `[0.00067,0.00201,0.0067,0.0201] Mpc^-1`, z-major/k-minor, 28 records, exact eight-binary64/64-byte ABI, 1792 bytes total, raw admission before decode/map, exact run/job/head/artifact/digest/SHA provenance. Endpoint rho fields do not substitute for the separately required full-history physical-branch proof.

No self-hosted heavy process owns the runner at this snapshot.

Global frozen DSIR boundaries from V33 remain unchanged.
