# Article 3 — prospective Exp073X Wm_S0 pilot-reuse amendment

**Frozen:** 2026-08-30 while Exp073X run `33277263287` is still in progress, before its angular-window output is available and before any DES Layer-A support fraction is evaluated.

This amendment reduces duplicate computation without changing the operator.

## Rule

If and only if Exp073X run `33277263287` finishes with all of its already-frozen controls and token

`PASS_EXP073X_DES_N4096_WM0_MASK_ONLY_ANGULAR_WINDOW_V0_1`,

then `workspace_1` / `wm0_te_window` from its immutable artifact is adopted as production task `Wm_S0` in the ordered 14-task manifest.

The second Exp073X workspace remains a repeatability QA copy and is not a second physical task.

Under that PASS condition, the later production matrix computes exactly the remaining 13 unique tasks:

- `Wm_S1`, `Wm_S2`, `Wm_S3`;
- `WW_S0_S0`, `WW_S0_S1`, `WW_S0_S2`, `WW_S0_S3`;
- `WW_S1_S1`, `WW_S1_S2`, `WW_S1_S3`;
- `WW_S2_S2`, `WW_S2_S3`;
- `WW_S3_S3`.

If Exp073X is incomplete, fails reproduction/resource controls, lacks an immutable artifact, or does not satisfy exact repeatability, **no pilot reuse is authorized** and no production join may count it as `Wm_S0`.

## Identity requirement

Before join, the production collector must verify that adopted Exp073X `Wm_S0` has exactly:

- `nside=4096`;
- NaMaster 2.7 lineage;
- the frozen 39-band edges;
- true-ell axis `0..12287`;
- R1 run `33270843577`, artifact `9720335366`, digest `sha256:ff87d8fc7d53b16b786a4eb3d6ffeb103676efb8a548223a187b9f59689f8abd`;
- source bin S0 pixel record SHA256 `5b507215ca961c09b82786e61e681a0178c29e9b593c17b588e366722a021f15`;
- source occupancy SHA256 `b6ed74f31540d4041267f94e2f7cdb70b7040d943ba22a4aa7eab62418f8cb32`;
- lens-mask SHA256 `a519b8522f899e4c33267bb0749f9734f8b7fa760d195636456d370f809a3d55`;
- spin0 x spin2 selected physical component TE<-TE;
- canonical selected-window shape `[39,12288]`;
- exact equality between its two independently computed selected windows.

No scientific threshold or support output is involved in the reuse decision.

Strict Article-3 readiness remains **52%**.
