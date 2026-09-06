# Recovery — Exp073GF LambdaCDM/GR mapping support PASS while Exp073FM runs

Date: 2026-09-06. Scope: DSIR only; never mix RTK/RQIR.

## Authoritative heavy process unchanged
Exp073FM / `WW_S1_S1` remains the sole active self-hosted science process: run `34050657030`, home job `101533574294`, head `f0caca0c3e812710e5958ee13348a150d045a7d8`, checkpoint namespaces `checkpoints/exp073fm-ww-s1-s1-a-v0-1` and `checkpoints/exp073fm-ww-s1-s1-b-v0-1`. Live reconciliation during this iteration found the frozen A/B step still in progress. `DSIR-HOME-PC` remains exclusively owned by that job. No partial numerical output or checkpoint stage was inspected.

Canonical post-candidate Exp073FR admission remains frozen and forbidden until FM terminal evidence is independently consumed. The autonomous successor queue through GB remains unchanged.

## Reconciled newer independent DSIR-4 infrastructure
Exp073GD model-funnel v0.1 run/job `34058614540 / 101554983550` remains infrastructure/static `+0/+0`; its Python validator passed and the first causal failure was shell quoting/count handling. Repaired v0.2 `34058689801 / 101555187453` is raw-verified support PASS. Exp073GE run/job `34058778331 / 101555427506` was independently re-read from raw logs and emitted `PASS_EXP073GE_DSIR4_MODEL_MAPPING_ARTIFACT_STATIC_AUDIT_V0_1`, `classification=SUPPORT_PLUS_0_PLUS_0`, `self_hosted_science_started=false`, `scientific_model_authority_created=false`.

## Newly closed Exp073GF — first concrete DSIR-4 model mapping
A symbolic LambdaCDM/GR baseline mapping was frozen without using any partial Exp073FM result:
- mapping path `data/dsir4/model_mapping_lcdm_gr_baseline_v0_1.json`, blob `9d438b385db5bc2cd07cfaa3c9088f5baa79dd6b`, creation commit `605b043e119e3fc951d174953269b8f2e85cee28`;
- validator `ci/validate_dsir4_lcdm_gr_mapping_v0_1.py`, blob `bcd081c1d8cde8dd89ff545ca20504dfc8a9aef5`, creation commit `62e15557c9062117d9879fce99ef733b0e61ac8f`;
- prereg `experiments/073gf_dsir4_lcdm_gr_mapping_static_audit_v0_1_prereg.md`, creation commit `42b39ef68049f2dd5ef3f4153655d58de2cb63ed`;
- workflow creation commit `e5dbd71c29a9a8dd80800d39cfff2d41bda67bfe` and activation head `5fc723c9a5cdefaac2eb61739d209548360aaa07`.

Frozen convention: `X_munu=M0^2 G_munu-T_known_munu`, with `T_known` = baryons + photons + standard neutrinos; pressureless CDM and exact Lambda remain in the residual. The mapping explicitly records all six required background/scalar components. In particular `delta p_X=0` and scalar anisotropic stress are structural zeros for this baseline, Lambda perturbations are structural zero, while density/momentum residuals inherit the CDM perturbations. Certified domain is exactly `0.295<=z<=2.33`, `0<k<=0.06664762008318016 Mpc^-1`; linear scalar perturbations, no quasi-static assumption, no sub-horizon assumption.

Exp073GF run/job `34059473109 / 101557289555` was consumed from raw logs. Exact token: `PASS_EXP073GF_DSIR4_LCDM_GR_MAPPING_STATIC_AUDIT_V0_1`. Classification is strictly `SUPPORT_PLUS_0_PLUS_0`; `self_hosted_science_started=false`; `scientific_model_authority_created=false`. The mapping is `mapping_ready=true` but remains `prediction_ready=false`, `numerically_evaluated=false`, `scientific_gate_status=NOT_YET_TESTABLE`. No LambdaCDM scientific PASS/FAIL is claimed.

## Next permitted work
1. Highest priority remains terminal consumption of Exp073FM as soon as run/job `34050657030 / 101533574294` becomes terminal.
2. If FM is still running, independent DSIR-4 work may continue by freezing the next existing-model mapping/prediction interface prospectively, without using partial FM output and without creating model scientific authority.
3. Do not launch any competing home/self-hosted job while FM owns `DSIR-HOME-PC`.
