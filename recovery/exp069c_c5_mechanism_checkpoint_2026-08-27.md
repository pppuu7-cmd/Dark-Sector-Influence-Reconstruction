# DSIR recovery checkpoint — after Exp069C C5 mechanism audit

Date: 2026-08-27

Current scientific state before merging this branch:

- main includes Exp070B mechanism localization and Exp070C C3 provider PASS through merge `0384347429dab2e6da422d51c59d7c14b12f89b7`.
- Exp070A remains permanent scientific FAIL.
- Exp069B remains permanent scientific FAIL.

## C3 status

C3/GDM physical-provider prerequisite is CLOSED by Exp070C:

`PASS_C3_GDM_NATIVE_GRID_PHYSICAL_POWER_PROVIDER_V0_1`.

Native P_mm closure max `2.8144898798669162e-14`; 33 common native nodes at every frozen z/case; same-mode coherence max `4.440892098500626e-16`; no state mutation.

## C5 mechanism result

Exp069C is descriptive only.

Provenance:
- prereg commit `44a9f5540eef7e4702c8ca9545048f239a36eb05`
- execution head `8ed8028b3fafc656ddc7ee6b217a812aa9be2521`
- run `33016782748`
- artifact `9625109424`
- digest `sha256:efbf9f80d71bce59f3441e51295d97c66073dd28d2583268c478636968c85cb8`

Frozen labels:
- `RAW_POWER_ZERO_LIMIT_RESIDUAL`
- `KGRID_NONCONVERGENCE`

GR/designer-zero raw k grids are bitwise identical. Target residual maxima remain about `5.26e-6 .. 5.41e-6` as `k_per_logint` increases from 40 to 320. Same-node raw residual maxima are larger, about `7.32e-6 .. 7.60e-6`. Therefore the Exp069B exact-zero defect is already present in solver-returned raw powers and is not caused by DSIR interpolation or sparse k sampling.

At k_per_logint=320, target residual correlations are:
- mm/Wm `0.9998508557`
- mm/WW `0.9995629927`
- Wm/WW `0.9998044549`

## Consequence

Do NOT create a corrective C5 bridge by merely increasing k_per_logint or changing the target interpolator. That mechanism is ruled out by Exp069C.

Next admissible C5 step: preregister a solver-mechanism audit comparing explicit designer B0=0 with ordinary GR under branch/accuracy/source/background diagnostics. The audit must identify whether the same-node residual is due to solver integration accuracy, explicit EFT branch initialization, background evolution, source evolution, or unresolved mixed behavior. Exp069B remains FAIL throughout.

Only after a separately certified C5 physical provider exists may DSIR preregister the common C3+C5 physical support-validity mask.

Mandatory order:
1. C5 solver-mechanism audit;
2. justified corrective C5 provider preregistration, if mechanism supports one;
3. C5 certification;
4. common support-validity mask;
5. covariance restriction/whitening;
6. nuisance tangent SVD/rank;
7. G7 quotient/relation/null control;
8. fresh G8 withheld family;
9. G9 afterwards.

G7/G8/G9 remain OPEN.
