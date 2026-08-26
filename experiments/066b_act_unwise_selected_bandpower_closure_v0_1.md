# Exp066B — ACT DR6 × unWISE selected-bandpower closure v0.1

Date: 2026-08-26
Status: preregistered before execution.

## Purpose

Close the remaining operator gap after Exp065B and Exp066A without performing a G7 law search and without choosing or inspecting a fresh withheld theory family.

Exp065B established that the exact public XCorrACT Blue/Green selected 26×26 covariance is positive definite without regularisation. Exp066A established algebraic equivalence of the solver-neutral raw no-CLEFT projection basis with the pinned upstream projection and proved that `P_WW`, `P_Wm`, and `P_mm` remain independent inputs.

Exp066B tests the closure from raw basis components to the selected observable bandpowers.

## Immutable upstream inputs

- likelihood source: `ACTCollaboration/unWISExLens_lklh@6302c30d9e70f8e4ff2d4a84a9977b4471705179`;
- public data archive SHA256: `1b2d1563c5eb548ca6488ed8d60c5260d9e110b743a2e3a84620cfe46fbb6570`;
- selected samples: `Blue_ACT`, `Green_ACT`;
- scale cuts: `Clgg=[100,402]`, `Clkg=[51,402]`;
- selected counts per sample: 6 `Clgg` + 7 `Clkg` = 13, combined 26.

The upstream fixed test point is also frozen as the nuisance reference:

### Cosmology source point

From pinned `test_unWISExLens_lklh.yaml`:

- `H0=67`;
- `As=2.15086031154146e-9`;
- `nnu=3.046`;
- `mnu=0.06 eV`;
- `ns=0.9665`;
- `omegabh2=0.02242`;
- `omegach2=0.11935351837638222`;
- CAMB `NonLinear_both`, `halofit_version=mead`, `lmax=4000`, `lens_margin=1250`, `lens_potential_accuracy=4`, `AccuracyBoost=lSampleBoost=lAccuracyBoost=1`.

The README endpoint control `total log-posterior=-62.1652` is diagnostic in this experiment, not part of the hard DSIR equivalence criterion because upstream does not pin the exact Cobaya/CAMB dependency versions required to make that scalar bitwise reproducible.

### Frozen Blue nuisance point

- `b=1.6`;
- `log10SN=-7.05`;
- `s=0.455`;
- PCA = `[-0.5843837663087972,-0.3985951242854526,-0.14460224245714698]`;
- free-CLEFT shifts: `cb2=(1,0.5551969885793376)`, `cbs=(1,0.16830370991953963)`, `cb3=(1,0)`.

### Frozen Green nuisance point

- `b=2.3`;
- `log10SN=-6.79`;
- `s=0.653`;
- PCA = `[-0.30320235632661185,-0.3042716635545827,-0.30615305724122277,-0.0945228819723003,-0.23779156954362762]`;
- free-CLEFT shifts: `cb2=(1,0.41552846311201563)`, `cbs=(1,0.21990237272388719)`, `cb3=(1,0)`.

## Frozen subtests

### B1 — free-CLEFT nuisance algebra

Create deterministic nonzero synthetic raw tensors with the exact Blue/Green PCA dimensionalities and nonzero free-CLEFT terms. Compare the DSIR implementation of the pinned free-CLEFT `__kg` and `__gg` equations against the exact pinned upstream private static methods.

- RNG seed: `20260826`;
- synthetic ell count: `64`;
- free-CLEFT coefficient matrices: generated from the frozen nuisance point using the public `CleftInterpolationHelperFreeCleft.assemble_cleft_coeff` formula with second-order, shear and third-order sectors enabled;
- tolerance per output: `5e-13 * max(1,max(abs(reference)))`;
- all outputs must be finite and shapes identical.

A second control sets all CLEFT raw tensors to zero while keeping Halofit/magnification pieces nonzero; only the CLEFT-dependent contribution may disappear.

### B2 — released bandwindow/transfer signal operator

For the actual public Blue/Green ACT matrices, use the exact algebra of upstream `NaMasterPowerSpectrumBinning`.

For signal-only cells the upstream expression

`(W C^{-1})(C x) = W x`

is an exact identity, so the DSIR signal operator is the released bandpower-window matrix applied to the padded spectrum, followed by the released transfer function. Exp066B must verify the required shapes/finite values and compare this reduced operator against an independently reconstructed upstream expression on deterministic test spectra at the selected bins.

The coupling matrix is not numerically inverted in DSIR; this is an exact algebraic cancellation, not regularisation or approximation.

### B3 — shot-noise eigen-template condition

The upstream auto-spectrum path injects a constant pseudo-spectrum `N*w2`, with `w2=sum(C[0,:])`. The exact cheap reduction to a constant full-sky template is valid only if

`C 1 = w2 1`.

Exp066B must test this identity on the released Blue/Green `gg` coupling matrices before using the reduced shot-noise template. Frozen threshold:

`max|C1-w2*1| / max(|w2|,1e-300) <= 1e-10`.

If this fails, Exp066B is a scientific/infrastructure FAIL for the full selected-bandpower closure; no jitter, approximate inverse, scale-cut change or post-hoc threshold change is allowed.

### B4 — selected ordering contract

The final order is frozen as

`[Blue gg(6), Blue kg(7), Green gg(6), Green kg(7)]`.

The selected ell midpoints must remain:

- `gg = [126.5,176.5,226.5,276.5,326.5,376.5]`;
- `kg = [76.5,126.5,176.5,226.5,276.5,326.5,376.5]`.

## Hard PASS

Exp066B passes only if B1–B4 all pass exactly under the frozen tolerances. The official fixed-cosmology endpoint value may be recorded as a diagnostic but cannot rescue or veto the algebraic gate unless a dependency stack is separately pinned.

PASS status:

`PASS_ACT_UNWISE_SELECTED_BANDPOWER_CLOSURE_V0_1`

FAIL status:

`FAIL_ACT_UNWISE_SELECTED_BANDPOWER_CLOSURE_V0_1`

## Anti-retuning

No post-output change to nuisance values, RNG seed, tensor shapes, scale cuts, selected ordering, CLEFT sector, row-sum threshold, algebraic reduction, or equivalence tolerance is allowed. A FAIL is permanent for v0.1 and motivates a separately numbered corrective experiment.

## Gate semantics

Even a PASS is a forward-operator bridge PASS only. `G7`, `G8`, and `G9` remain OPEN. No fresh withheld family may be selected until a covariance-whitened training-only cross-channel relation and its null statistic are frozen in a later experiment.