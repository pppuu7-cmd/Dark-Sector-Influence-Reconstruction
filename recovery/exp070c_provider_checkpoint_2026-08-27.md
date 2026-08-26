# DSIR recovery checkpoint — Exp070C C3 provider PASS

Date: 2026-08-27

## Preserved history

- Exp070A remains permanent scientific FAIL (~4.75% target-grid D_m->mPk reconstruction defect; no threshold retuning).
- Exp070B mechanism result is `INTERPOLATION_DOMINATED`; native D_m reconstruction closed native mPk to `2.7665e-14`, while the rejected amplitude interpolation reproduced `0.0475359` error.

## New hard result

Exp070C: `PASS_C3_GDM_NATIVE_GRID_PHYSICAL_POWER_PROVIDER_V0_1`.

Provenance:
- prereg commit `c66c7bd327a0f13ba8ef732c94482ca6d9ce0b9b`
- execution head `a1f0ce9e02f934acdf79c546abbcbfe76b7fcfbd`
- run `33017214292`
- artifact `9625032179`
- digest `sha256:34cf89f2207c72b4e3d669f7e4e6419753b6b046ed7de9e3a9fa7fb144b4c081`

Hard numerics:
- C1 native P_mm closure max: `2.8144898798669162e-14` against frozen `1e-10`.
- C2: 33 common native nodes at every frozen z/case; max representation k mismatch `1.545552650407278e-16`.
- C3 signed Weyl/power finiteness and sign contract PASS.
- C4 same-mode coherence max `4.440892098500626e-16` against `2e-10`.
- C5 missing-variable-k^2 software negative control PASS; engineering control only, not a dimensionless physical observable.
- C6 accessor bitwise repeatability PASS; native mPk state mutation exactly `0.0` against `1e-12`.
- C7 complete native-grid provider schema PASS; no observational projection.

Provider construction:
`P_mm=(2*pi^2/k^3) P_R D_m^2`
`W=0.5 k^2 (phi+psi)`
`q_W=W/D_m`
`P_Wm=q_W P_mm` (signed)
`P_WW=q_W^2 P_mm`

No D_m amplitude interpolation is used.

## Gate state and mandatory next order

C3 physical-provider prerequisite is now closed.

C5 is still open because Exp069B is permanent FAIL and Exp069C mechanism audit is running/awaiting classification. Do not preregister the common physical support-validity mask until C5 has a separately certified corrective provider if required.

Order:
1. finish/record Exp069C C5 mechanism audit;
2. preregister a corrective C5 provider only if Exp069C identifies a justified mechanism;
3. certify C5;
4. preregister common physical support-validity mask;
5. covariance restriction/whitening;
6. nuisance tangent SVD/rank;
7. G7 quotient/relation/null control;
8. fresh G8 withheld family;
9. G9 afterwards.

G7/G8/G9 remain OPEN.
