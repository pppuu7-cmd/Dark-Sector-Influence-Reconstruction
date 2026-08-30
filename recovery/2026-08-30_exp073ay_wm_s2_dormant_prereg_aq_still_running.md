# DSIR checkpoint — Exp073AY dormant Wm_S2 preregistration while Exp073AQ remains active

**UTC date:** 2026-08-30  
**Scientific readiness:** 52% (unchanged)

## Chronology

1. Repository head was inspected; latest recovery reconciliation commits through `caea05031243fa885f9c4e65185b7eb40d512ec4` were present.
2. `docs/RECOVERY_LATEST.md` was read and confirmed the authoritative order: resolve Exp073AQ Wm_S1 first; do not launch Wm_S2 before exact AQ PASS.
3. Exp073AQ run `33327372191` was checked. Both replica jobs remained `in_progress` in `Compute exact controlled Wm_S1 replica`:
   - A job `99299799192`
   - B job `99299799338`
4. Exp073AQ artifact listing was checked and was empty at that point; therefore no comparator authority existed.
5. Repository code search found no prior `Wm_S2` controlled-twin preregistration.
6. A non-executing prospective successor freeze was created as Exp073AY:
   - `experiments/073ay_article3_controlled_twin_wm_s2_dormant_prereg_v0_1.md`
   - commit `9dd131d4610156d569b5b99659e13564b8a622cb`
7. Recovery guidance was added:
   - `docs/RECOVERY_MANUAL_ADDENDUM_EXP073AY_2026-08-30.md`
   - commit `55bfa6c951a1c150308191e55a063ebc67a01db1`

## Scientific classification

This checkpoint records methodological/preregistration progress only.

- no scientific PASS declared;
- no real-data gate scored;
- no readiness increment;
- no AQ result read or inferred;
- no Wm_S2 workflow launched;
- no G7/G8/G9 state changed;
- RTK/RQIR excluded.

## Next authorized action

Re-check Exp073AQ run `33327372191`.

Only if a hosted immutable comparator artifact exists with exact terminal class `PASS_EXP073AQ_WM_S1_CONTROLLED_TWIN_EXACT_V0_1` may Exp073AY proceed from dormant preregistration to final implementation/workflow freeze and hosted Wm_S2 execution.
