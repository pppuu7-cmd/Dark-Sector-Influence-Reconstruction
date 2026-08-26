# Recovery checkpoint — Exp065A (2026-08-26)

Current immutable base before this branch: main at `341b7de16534ca1130c63d61701cb553434bc616` (Exp064A/F31).

## Scientific state

- F31: NO_NONTRIVIAL_COMMON_PLANE_RELATION_V0_1 for DESI ShapeFit AP/growth/shape. Frozen p-values: p(lambda_min lower)=0.2653367332; p(LOO RMS lower)=0.3612319384. No rescue/retuning.
- G7 OPEN; G8 OPEN; G9 OPEN.
- F30 remains a positive prospective out-of-family result for the two-coordinate matter-response representation, but is not G7.

## Exp065A decision

The next G7 route is an independently observed Weyl/lensing block with explicit public kernels and covariance. ACT DR6 lensing likelihood products meet this requirement at the auto-spectrum level. The public ACT `unWISExLens_lklh` is preferred for the next binding experiment because it provides lensing×galaxy cross bandpowers, covariances and auxiliary data.

Raw theory slip/Weyl from earlier experiments remains masked from observational distinguishability claims until this binding exists.

## Exact next action

Create Exp066A as a source/provenance-only reproducibility gate for the public unWISE×CMB-lensing likelihood/data interface. The gate should verify pinned upstream source identity, deterministic acquisition or documented immutable checksum, presence/dimensions/positive-definiteness of the relevant covariance, and availability of the window/auxiliary operators needed to map theory to the released bandpowers. It must not fit a DSIR law and must not inspect/select a withheld dark-sector family.

If Exp066A cannot be reproduced in GitHub Actions, record the failure and evaluate ACT DR6 lensing auto as the fallback kernel block; do not substitute a scalar literature constraint.
