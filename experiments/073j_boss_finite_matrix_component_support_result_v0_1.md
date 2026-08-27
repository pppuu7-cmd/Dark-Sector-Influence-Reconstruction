# Exp073J — BOSS finite-matrix component support result v0.1

**Date:** 2026-08-27  
**Status:** NON-CLASSIFYING COMPONENT RESULT

The frozen BOSS finite-matrix component audit completed successfully in workflow run `33042052616`, job `98417620281`, artifact `9634226231`, digest `sha256:239b198c1adfc21333779ef1efb597885710bddd593b380a67ac6dd1399daa65`, from implementation merge `1bd022ffca543361d265a72b782ef96fe069d2ce`.

All implementation/control checks passed. The exact composed operator was `C=W@M`, with `W=200x2000`, `M=2000x1200`, `C=200x1200`. Physical true-k support used the prospectively frozen `h_fid=0.676` conversion, the unchanged common rectangle `0.000704833374744468 <= k <= 0.06664762008318016 Mpc^-1`, and the unchanged positive-invalid threshold `<=0.05`. The envelope was `abs(C[row,:])`; no signed cancellation, fiducial P(k) weighting, covariance weighting, nuisance weighting, post-hoc k cut or downstream information was used.

## Component result

Across both BOSS z3 caps and observed even multipoles, `54/240` component rows satisfy the 5% support criterion:

- NGC: `27/120`, exactly `9/40` for each of P0, P2 and P4;
- SGC: `27/120`, exactly `9/40` for each of P0, P2 and P4.

For the retained low-k rows the minimum invalid fractions are of order `1e-3--3e-3`. Higher observed-k rows rapidly become dominated by support above the common provider ceiling; the median invalid fraction within each 40-row multipole block is approximately `0.99997--0.99999`.

This is useful localization: the finite-matrix BOSS branch is not an absolute obstruction to the common route, because it leaves a non-empty and substantial low-k subset. It also shows that the full released BOSS range cannot be retained under the already-frozen common provider support.

## Interpretation boundary

This result is deliberately **not** a PASS or FAIL classification for Exp073J. Exp073J still requires exact KiDS-BNT `Wm` and `WW` positive-support evaluation, followed by the preregistered full-coordinate intersection. Only the full audit can test the minimum retained dimension of 15 and authorize covariance restriction/whitening.

No covariance, nuisance SVD/rank, quotient/relation/null, held-out family or G8 information was read. G7, G8 and G9 remain OPEN.
