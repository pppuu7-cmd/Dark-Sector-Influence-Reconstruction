# Exp073IL — C2 ordered-join structural admission v0.1

Status: PROSPECTIVELY FROZEN before execution. Scope: DSIR only.

## Purpose
Evaluate only the newly frozen structural definition in `docs/dsir4/contracts/DSIR4_ORDERED_JOIN_DEFINITION_V0_1.md`. No radial multiplication, numerical projection, covariance operation, nuisance fit, or model-output scoring is allowed.

## Preconditions
- `G_DOMAIN_MAPPING=PASS` and `G_ANGULAR_AUTHORITY=PASS` in current repository authority.
- Exp073IK support PASS has frozen the exact source/observable order.
- C2 prediction artifact/payload identity and 28 exact z-major/k-minor coordinates are already frozen.

## Frozen exact slot order
`Wm_S0,Wm_S1,Wm_S2,Wm_S3,WW_S0_S0,WW_S0_S1,WW_S0_S2,WW_S0_S3,WW_S1_S1,WW_S1_S2,WW_S1_S3,WW_S2_S2,WW_S2_S3,WW_S3_S3`.

## Acceptance rule
PASS iff a hosted fail-closed audit verifies from frozen repository files that:
1. the ordered-join definition exists and explicitly defines `J_j` as a typed metadata/provenance tuple and `J` as the exact 14-slot ordered tuple;
2. it binds the same immutable C2 prediction identity to all slots and the exact prediction coordinates `z=[0.295,0.51,0.706,0.934,1.317,1.491,2.33]`, `k=[0.00067,0.00201,0.0067,0.0201]` Mpc^-1;
3. source labels/order and Wm `TE<-TE` / WW `EE<-EE` agree with Exp073IK inventory and admitted angular contract;
4. angular dimensions remain NSIDE=4096, ell=0..12287, 39 bands, canonical `<f8 [39,12288]`;
5. current authority has `G_DOMAIN_MAPPING=PASS`, `G_ANGULAR_AUTHORITY=PASS`, and no pre-existing `G_ORDERED_JOIN=PASS` is assumed as evidence;
6. the definition explicitly forbids numerical radial multiplication/projection and defers all coupling of `(z,k)` with `(band,ell)` to `G_RADIAL_SUPPORT`.

No tolerance or output-dependent decision exists.

## Terminal states
On exact PASS emit `PASS_EXP073IL_C2_ORDERED_JOIN_STRUCTURAL_ADMISSION_V0_1` and classify `SCIENTIFIC_GATE_PASS`, with `G_ORDERED_JOIN=PASS`, `G_RADIAL_SUPPORT=NOT_YET_TESTABLE`, `scientific_model_authority_created=false`, `overall_status=NOT_YET_TESTABLE`.

Any missing/mismatched frozen prerequisite produces `NOT_YET_TESTABLE`, not scientific FAIL. Any audit/parser/transport defect is infrastructure `+0/+0`.

## Runner/resource policy
GitHub-hosted only. No self-hosted runner, no checkpoint namespace, no cosmological or MCM computation, no scientific numerical output.