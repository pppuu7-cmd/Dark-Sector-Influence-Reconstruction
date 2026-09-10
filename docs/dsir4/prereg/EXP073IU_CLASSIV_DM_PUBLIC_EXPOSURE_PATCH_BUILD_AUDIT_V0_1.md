# Exp073IU — CLASS-IV d_m public-exposure patch build/static audit v0.1

Date frozen: 2026-09-10. Scope: DSIR Article 3 / C2 only.

Status: PROSPECTIVELY FROZEN AFTER Exp073IT PASS, BEFORE ANY PATCHED Exp073IR NUMERICAL RESPONSE.

## Immutable parent
Exp073IT run/job `34431545882 / 102727918512`, head `cd8fb5e069bd8b404d15b04bea4c823e54ca90c8`, raw token `PASS_EXP073IT_CLASSIV_DM_INTERNAL_SOURCE_PATCH_TARGET_AUDIT_V0_1`, classification `SUPPORT_PLUS_0_PLUS_0`.

## Exact repair scope
At exact upstream `kaeonikc/class_iv@ac627d54e9ce196a08878d1ba33999819925d19c`, `source/perturbations.c` blob `92a48331658c5941ed4eb43b0e98ee78e39b8385`, apply only these three interface changes:

1. Inside the existing `if (ppt->has_density_transfers == _TRUE_)` source-flag block, set `ppt->has_source_delta_m = _TRUE_;` in addition to the existing `has_source_delta_tot`. This causes the already-existing source assignment `_set_source_(ppt->index_tp_delta_m) = ppw->delta_m;` to be populated for ordinary `mTk` transfer requests.
2. Inside CLASS-format density-transfer titles, add one distinct `d_m` title immediately before existing `d_tot`.
3. Inside CLASS-format density-transfer data, add one distinct `tk[ppt->index_tp_delta_m]` column immediately before existing `tk[ppt->index_tp_delta_tot]`.

The patch MUST preserve `d_tot/index_tp_delta_tot` as a separate existing column. It MUST NOT alter `ppw->delta_m`, the gauge-invariant source definition, coupling equations, baseline cosmology, finite-difference directions or `h=1e-4`, interpolation rule, frozen domain, Layer-A retained set, Layer-B validity thresholds, covariance firewall, or any later gate.

## Build/static acceptance
Hosted audit must fail closed unless:
- upstream commit and perturbations blob match exactly before patch;
- each insertion anchor occurs exactly once in its intended context;
- resulting source contains exactly the intended `d_m` public title/data route and retains `d_tot`;
- existing gauge-invariant source assignment remains byte-identical as a line;
- CLASS core and Python wrapper build successfully after applying the already-proven modern build-compatibility adaptations used by DSIR;
- no Exp073IR numerical Layer-B computation is run.

No output values may be inspected or classified in Exp073IU.

PASS token: `PASS_EXP073IU_CLASSIV_DM_PUBLIC_EXPOSURE_PATCH_BUILD_AUDIT_V0_1`.
PASS classification: `SUPPORT_PLUS_0_PLUS_0` only.

Only PASS authorizes a prospective implementation-only Exp073IR retry binding that applies this exact patch before the frozen Layer-B calculation.