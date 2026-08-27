# Exp072B — Exp072A support-boundary decomposition result v0.1

**Date:** 2026-08-27  
**Scientific classification:** `DIAGNOSTIC_K_ONLY_TARGET_NOT_FOUND_EXP072B`

## Immutable provenance

- preregistration commit: `c51693ab17e9df042269da68789ed8441d7e50d7`;
- preregistration merge: `2d531646e0a3b2cd120d532adb5b59350a6b1155`;
- implementation PR: #108;
- implementation merge: `3dce5449e9d23dbc71091905ad51bd8c7b45bba2`;
- workflow run: `33030657898`;
- workflow job: `98382166843`;
- immutable artifact: `9630210086`;
- artifact digest: `sha256:5bbca5717d29d24f8ba3b5ae24d8cc752bd5d90460859ae79f5212ca764615ad`;
- extracted result JSON SHA256: `d90b387b6acb5b48c6daae0f25da9adb7ea6ed851e3b22c8a79c6bc56b2d0f1d`.

All B1–B6 hard controls passed. The result is therefore a completed causal diagnostic, not an infrastructure outcome.

Exp072A remains permanently

`FAIL_ACT_UNWISE_ANGULAR_SUPPORT_LEAKAGE_MASK_V0_1`.

Exp072B does not retest or soften that result.

## Frozen question

Keeping the Exp072A redshift interval, lower-k boundary, released ACT×unWISE operator geometry, 5% invalid-support threshold and 26-coordinate route requirements fixed, can **upper-k extension alone** recover the minimum route?

Answer: **no**.

No finite upper-k-only requirement exists for any of the 26 observation coordinates once all applicable physical blocks are required simultaneously:

- finite `K_req_coord`: `0/26`;
- infinite `K_req_coord`: `26/26`;
- `K_target_route = none`.

Therefore no amount of upper-k extension by itself can satisfy the frozen observation-space route.

## Causal decomposition

Across the 64 coordinate-block pairs:

- median redshift-outside fraction: `0.4556923704004443`;
- maximum redshift-outside fraction: `0.8839350857532944`;
- median k-outside fraction: `0.9705092579400587`;
- maximum k-outside fraction: `0.9999982983363256`;
- median high-k fraction: `0.9705092577608834`;
- median low-k fraction: `1.1786843354337586e-7`;
- `f_k_out > f_z_out` for `60/64` pairs;
- `f_z_out > f_k_out` for `4/64` pairs;
- exact ties: `0`.

Thus the existing support is strongly too narrow in k, but that is **not sufficient** to explain the blockage because the redshift-outside contribution is independently above the frozen 5% ceiling for required blocks.

## Which redshift side is responsible?

The redshift leakage is overwhelmingly at **low redshift**, not high redshift:

- overall median `f_z_low = 0.45567647226245966`;
- overall maximum `f_z_low = 0.8839350857452918`;
- overall median `f_z_high = 8.58899591150497e-7`;
- overall maximum `f_z_high = 0.016498436964947242`.

The lower-k contribution is also negligible relative to the high-k contribution. Therefore the data do not motivate extending the lower-k or upper-z boundaries at this stage.

The causally indicated support problem is the coupled pair:

`lower-z extension + upper-k extension`.

This coupling is physically expected from the Limber map

`k=(ell+1/2)/f_K(chi)`:

admitting lower redshift at fixed angular multipole simultaneously demands larger physical k. The two missing support directions therefore cannot be treated as independent engineering knobs.

## Blockwise structure

Median `(z-out, k-out)` fractions:

- `gg/mm`: `(0.0908048, 0.7963393)`;
- `gg/Wm`: `(0.4556924, 0.9824384)`;
- `gg/WW`: `(0.8121921, 0.9996269)`;
- `kg/Wm`: `(0.1621263, 0.6482495)`;
- `kg/WW`: `(0.6634361, 0.9871138)`.

This is important for the DSIR mechanism picture. The strongest support problem is not uniform across physical blocks: independent Weyl-sensitive pieces are much more exposed to low-z/high-k support than the matter-only `gg/mm` block.

Only six individual coordinate-block pairs have finite upper-k-only targets, all Green `gg/mm`, with required k approximately `0.711–0.732 Mpc^-1`. But every corresponding angular coordinate also contains Wm/WW blocks whose fixed redshift-outside contribution already exceeds 5%, so no complete coordinate is rescued.

## Scientific interpretation

Exp072B identifies a **support-geometry obstruction**, not a dark-sector signal and not a failure of GDM or designer-f(R).

The observation operator mixes the current finite C3/C5 domain into a broad low-z/high-k region. The route therefore fails before covariance whitening or nuisance quotienting because the currently certified joint physical domain does not cover the survey operator deeply enough.

This result strengthens the channel-conditional DSIR picture: a theory-space common domain can be perfectly valid while its image under a real observational operator has essentially no usable coordinates.

## Exp069F lesson carried forward

The earlier C5 sequence is directly relevant. Exp069F showed that a target-grid numerical PASS could occur before same-node/raw provider closure was adequate, and Exp069H therefore required a separate provider certification.

Accordingly, any future support rectangle inferred from Exp072B/Exp072C is a **planning target only**. It cannot be promoted to physical support until C3 and C5 independently certify native/raw coverage under a new prospective contract. This boundary is frozen in

`docs/PROVIDER_EXTENSION_NATIVE_SUPPORT_BOUNDARY_2026-08-27.md`.

## Downstream state

No covariance restriction, Cholesky/whitening, nuisance SVD/rank, G7 relation/null, or G8 response is authorized.

The next admissible causal diagnostic is a prospectively frozen **joint lower-z / upper-k support-frontier** calculation under the unchanged 5% threshold and released operator geometry.

- G7: `OPEN`;
- G8: `OPEN`;
- G9: `OPEN`.
