# DSIR recovery checkpoint — Exp056B/F29 — 2026-08-26

## Immutable chronology

1. Exp055A/F28 retrospectively qualified `C50 = Delta ln(k50_geo)/Delta ln(k_source) > 0` on already-seen C3 GDM, C5 designer-f(R), and C7 IDM-DR. It explicitly required a fresh prospective mechanism before any G7/G8 upgrade.
2. Exp056A introduced C8 IDM-photon scattering and selected five couplings using only the pinned CLASS source equations. Run `32922159744` passed the no-response contamination guard and was merged to main as `0e27dffc079b512c91b41898e3eda19fc84d50a6`.
3. Exp056B complete scientific contract was committed at `84d05ad72af1aea4fe3beadf071ee20cadf93c19`, before any C8 `P(k,z)` existed.
4. An initial run `32925960293` stopped before response generation because two workflow float-string assertions did not match Python `.17g` serialization. This was purely infrastructure; no response step ran. Only those assertions were corrected; the scientific contract, grid, operator and acceptance rule were unchanged.
5. Clean first-response run `32926084015` then completed CLASS response generation and the frozen evaluator. It returned `FAIL_IDM_PHOTON_ENDPOINT_HALF_TRANSITION_PROSPECTIVE_V0_1`.

## Frozen C8 source grid

`k_source [h/Mpc] = [0.08484582985947185, 0.07347864406347489, 0.05999506164903260, 0.04647197492427811, 0.03927598733289058]`

`u_idm_g = [1.9784961959913951e-13, 2.7180740724473660e-13, 4.2866377403625277e-13, 7.7340788471244140e-13, 1.1546648138593298e-12]`

Pinned solver: `lesgourg/class_public@e85808324f51fc694d12e3ed7439552a3c3f9540`.

## Frozen operator and gate

At each of seven redshifts and each of five C8 couplings, on `k={0.001,0.003,0.01,0.03,0.1} h/Mpc`:

`R=ln(P_C8/P_ref)`,

`u=(R-R(k_min))/(R(k_max)-R(k_min))`,

with exactly one `u=0.5` crossing interpolated piecewise-linearly in `ln k`.

`k50_geo=exp(mean_z ln k50(z))`,

`C50=Delta ln(k50_geo)/Delta ln(k_source)`.

PASS required all 35 unique crossings, all four full-sample `C50>0`, and all 28 leave-one-redshift `C50>0`. No magnitude band was allowed.

## Hard result

All 35/35 crossings were valid and unique.

`k50_geo [h/Mpc] = [0.016129751071873887, 0.04959012032253081, 0.01818439764920937, 0.039720915301257036, 0.01583583466167637]`

`C50 = [-7.808106760860718, 4.948527764236845, -3.0590240270100333, 5.466141893053988]`

Pairs `1->2` and `3->4` fail strict positivity. Every one of the seven leave-one-redshift recomputations preserves this failed-pair pattern. This is therefore a robust prospective falsification of F28 v0.1 on C8, not a missing-crossing or single-redshift pathology.

Run provenance: `32926084015`; artifact `9591561317`; artifact SHA256 `eb44e29725ace326e707d396158e7c4ed6fd4dccdd86d9ad18e67f42526750b1`.

## Gate state after F29

- Exp056B/F29: HARD PROSPECTIVE FAIL.
- F28: remains a positive retrospective pattern but is falsified as the proposed prospective cross-mechanism law v0.1.
- G7: OPEN.
- G8: OPEN.
- G9: OPEN.
- Exp054C/F27: remains HARD FAIL independently.
- Earlier mechanism-specific characteristic-scale/epoch findings remain valid within their frozen domains.

## Mandatory recovery rules

Do not retune Exp056B. Do not delete C8 nodes/redshifts, change the endpoint normalization, reverse signs, refit couplings, or construct a magnitude band and call it the same test. Any new common relation must have a new experiment identifier, a scientifically distinct derivation, and a complete preregistration before the response of a genuinely fresh validation mechanism is inspected.

The next research direction should seek a stronger invariant/quotient description that explains why C8 alternates its half-transition ordering, or advance the separate masked discriminant/observability program. Keep negative results in the permanent chronology.
