# DSIR-4 ordered-join definition v0.1

Status: PROSPECTIVELY FROZEN. Scope: DSIR only. This definition is frozen before any ordered-join output is computed or scored.

## Scientific premise
The mandatory funnel order already freezes `G_ORDERED_JOIN` before `G_RADIAL_SUPPORT`. Therefore `G_ORDERED_JOIN` is the typed, ordered, provenance-bound association between a frozen hypothesis prediction identity/domain and the admitted angular-observable authority slots. It is **not** radial multiplication, line-of-sight projection, source-window integration, covariance weighting, nuisance fitting, or a model viability test. Those operations belong to later separately frozen gates.

This distinction avoids inventing source-bin redshift edges or radial weights at the join stage.

## Preconditions
For hypothesis `C2_IDE_LOCAL_TANGENT_CONE`:
- `G_DOMAIN_MAPPING=PASS`;
- `G_ANGULAR_AUTHORITY=PASS`;
- prediction artifact `docs/dsir4/predictions/C2_IDE_LOCAL_TANGENT_CONE_PREDICTION_V0_1.md`, payload `C2_IDE_LOCAL_TANGENT_CONE_PREDICTION_BASIS_V0_1.jsonl`;
- prediction coordinates are exactly z = `[0.295,0.51,0.706,0.934,1.317,1.491,2.33]` and k [Mpc^-1] = `[0.00067,0.00201,0.0067,0.0201]`, z-major/k-minor, with no interpolation or extrapolation;
- source basis labels are exactly `[S0,S1,S2,S3]` with `zbin_mcal=[0,1,2,3]`;
- angular authority dimensions remain DES NSIDE=4096, ell `0..12287`, 39 bands, canonical `<f8 [39,12288]`.

## Exact ordered membership
The ordered join has exactly 14 typed slots, in this order:
1. `Wm_S0`
2. `Wm_S1`
3. `Wm_S2`
4. `Wm_S3`
5. `WW_S0_S0`
6. `WW_S0_S1`
7. `WW_S0_S2`
8. `WW_S0_S3`
9. `WW_S1_S1`
10. `WW_S1_S2`
11. `WW_S1_S3`
12. `WW_S2_S2`
13. `WW_S2_S3`
14. `WW_S3_S3`

Wm semantics are exactly `TE<-TE`; WW semantics are exactly `EE<-EE`. No slot may be substituted, dropped, duplicated, averaged, symmetrized beyond the already-frozen WW pair convention, or reordered.

## Join operator
Let `P` denote the immutable C2 prediction-basis identity plus its exact 28-point `(z,k)` coordinate set. Let `A_j` denote the admitted angular authority identity for slot `j`, including run/job/artifact/provenance and canonical array identity. Define

`J_j := (slot_id_j, source_labels_j, observable_semantics_j, P_identity, P_domain_coordinates, A_j_identity, A_j_angular_coordinates)`

and

`J := ordered_tuple(J_1,...,J_14)`.

This is a typed metadata/provenance join only. It performs **no numerical multiplication between P and A_j**. Consequently the differing `(z,k)` and `(band,ell)` coordinate systems remain explicitly separate at this gate. Their scientifically defined coupling is deferred to `G_RADIAL_SUPPORT`.

## Fail-closed rules
`G_ORDERED_JOIN` is PASS only if all 14 required slots exist exactly once in the frozen order; every slot binds the exact admitted angular authority required by `G_ANGULAR_AUTHORITY`; every slot binds the same exact C2 prediction identity and exact 28 prediction coordinates; Wm/WW semantics and canonical angular dimensions match their frozen authorities; and no radial weight, redshift-bin edge, interpolation, projection, covariance, nuisance, smoothing, tolerance, effective coordinate, or fiducial-P substitution is introduced.

Any missing/mismatched authority or identity yields `NOT_YET_TESTABLE` unless an already-frozen mandatory prerequisite has a scientific FAIL. Infrastructure/parser/transport defects remain `+0/+0` and do not become scientific FAIL.

## Status boundary
A PASS of this gate means only that the model prediction identity and the complete angular authority set are joined in a deterministic, prospectively frozen order with unambiguous provenance. It does not assert that the prediction has radial support for any source bin and does not create complete model authority.

On PASS:
- `G_ORDERED_JOIN=PASS`;
- `G_RADIAL_SUPPORT=NOT_YET_TESTABLE` remains unchanged until a separate prospective radial-support contract exists;
- all later gates remain unchanged;
- `scientific_model_authority_created=false`;
- overall model status remains `NOT_YET_TESTABLE`.

## Anti-circularity
This definition may be audited only from frozen repository identities and authority metadata. No numerical join/projection output may be read or used to alter membership, ordering, coordinates, or rules. Any future numerical coupling between the C2 `(z,k)` prediction and angular slots requires a new prospectively frozen `G_RADIAL_SUPPORT` contract.