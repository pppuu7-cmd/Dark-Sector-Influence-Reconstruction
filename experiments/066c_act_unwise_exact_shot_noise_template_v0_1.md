# Exp066C — exact ACT × unWISE shot-noise template v0.1

Date: 2026-08-26
Status: preregistered before execution.

## Immutable starting point

Exp066B is a permanent hard FAIL for the proposed constant-mode shortcut. The released ACT `gg` coupling matrix gave

`max|C 1 - w2 1|/|w2| = 0.3615744168461421`,

against the frozen `1e-10` criterion. That failure is not altered here.

The following Exp066B subresults remain immutable:

- B1 free-CLEFT nuisance algebra: PASS;
- B2 signal bandwindow/transfer operator: PASS;
- B4 selected 26-bandpower ordering: PASS.

## Corrective question

Can the exact upstream white-noise term be represented solver-neutrally without a dense matrix inverse and without any approximation?

Pinned upstream `NaMasterPowerSpectrumBinning` defines

`D = W C^{-1}`

and for a constant pseudo-spectrum white-noise contribution `N w2 1` returns

`N w2 W C^{-1} 1`,

followed by the released transfer function.

Exp066C freezes the equivalent construction

1. solve `C y = 1` in IEEE float64 using `numpy.linalg.solve`;
2. require the explicit solve residual

   `rho = max|C y - 1| <= 1e-10`;

3. construct the unit-noise 59-bin template

   `t_unit = w2 (W y) odot T_gg`;

4. at the frozen Blue/Green nuisance points multiply by `N=10^log10SN` and apply the unchanged Exp066B `gg` selection.

No jitter, diagonal loading, pseudoinverse, iterative tolerance, shrinkage, row rescaling, threshold relaxation or coupling modification is permitted.

## Frozen provenance

- `ACTCollaboration/unWISExLens_lklh@6302c30d9e70f8e4ff2d4a84a9977b4471705179`;
- public data archive SHA256 `1b2d1563c5eb548ca6488ed8d60c5260d9e110b743a2e3a84620cfe46fbb6570`;
- released ACT bandwindow/coupling file from the pinned `binning_setup.yaml`;
- Blue transfer and Green transfer files from the same pinned config;
- Blue `log10SN=-7.05`, Green `log10SN=-6.79`;
- selected `gg` midpoints `[126.5,176.5,226.5,276.5,326.5,376.5]`.

## Frozen controls

### C1 — small-matrix literal-upstream equivalence

Using RNG seed `20260827`, construct a deterministic well-conditioned non-symmetric 32×32 matrix `C`, a 7×32 `W`, a 7-vector transfer `T`, and scalar noise `N`.

Compare

`(W @ inv(C)) @ (N*w2*1) * T`

against

`N*w2*(W @ solve(C,1))*T`.

Hard tolerance:

`max_abs_difference <= 5e-13 * max(1,max|reference|)`.

### C2 — released ACT solve

On the actual released 6144×6144 `gg` coupling matrix:

- `numpy.linalg.solve(C,ones)` must return finite values;
- `rho=max|Cy-1| <= 1e-10`;
- the 59-bin unit-noise template must be finite and nonzero;
- the template must not be forced to a constant shape;
- the six selected Blue and six selected Green noise contributions must be finite and nonzero.

### C3 — non-shortcut diagnostic

Compute the relative difference between the exact unit-noise template and the permanently rejected Exp066B shortcut `W 1 odot T` after normalising both by the same `w2`. This is descriptive only; no threshold is used. A nonzero difference is expected and reinforces why Exp066B failed, but it cannot determine PASS/FAIL.

## Hard PASS

PASS iff C1 and C2 both pass under the frozen tolerances and exact provenance.

Status:

`PASS_ACT_UNWISE_EXACT_SHOT_NOISE_TEMPLATE_V0_1`

Otherwise:

`FAIL_ACT_UNWISE_EXACT_SHOT_NOISE_TEMPLATE_V0_1`.

A PASS, combined with immutable Exp066B B1/B2/B4 PASS subresults, is sufficient to close the ACT×unWISE selected-bandpower **operator bridge**. It does not close G7, G8 or G9.

## Anti-retuning

No post-execution change to solver, dtype, residual threshold, seed, scale cuts, noise amplitudes, selected ell bins, matrix file, or algebra is allowed. A failure is permanent for v0.1 and any further correction requires a new experiment.

## Next step after PASS

Before a G7 law search, freeze a physical convention bridge for the independent solver-neutral inputs `P_WW`, `P_Wm`, `P_mm`, including the exact CAMB `Weyl=(Phi+Psi)/2` convention, density-species convention, physical `k`/power units and a reference ΛCDM regression. No fresh withheld dark-sector family may be chosen before the later G7 relation itself is frozen.