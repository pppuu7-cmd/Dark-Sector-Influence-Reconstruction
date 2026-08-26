# Exp063A — G7 observable-eligibility audit (2026-08-26)

## Purpose

Select the smallest scientifically admissible channel set for the next G7 law search without promoting raw theory-space separators to observational claims.

## Immutable starting state

- F27: HARD FAIL.
- F29: HARD PROSPECTIVE FAIL.
- F30: HARD PROSPECTIVE PASS.
- Exp062A: G7/G8 closure audit; G7/G8 remain OPEN.
- G7 requires a nontrivial residual cross-channel relation after quotienting known identities and measurement degeneracies.
- A raw theory-space metric/Weyl/slip separator is not observational distinguishability without a stated survey kernel and covariance convention.

## Audit choice

The existing corrected DESI DR1 ShapeFit block is the first eligible training-side observational block because it already contains three independently meaningful channels with a measured covariance:

1. AP geometry: `DH_over_DM`;
2. growth: `f_sigma_s8`;
3. shape: `m_plus_n`.

Experiment 009 already validates the covariance structure and Experiment 010 already implements the Gaussian conditional-innovation quotient for AP/growth/shape. Exp063A re-runs those controls and asserts positive-definite three-channel covariance in the informative bins `LRG1, LRG2, LRG3, ELG2, QSO`.

The existing GDM Weyl/slip result remains scientifically useful but **ineligible for a G7 observational-law claim at this stage** because the repository does not yet contain a survey response-kernel plus covariance binding for that metric block. Undefined or unbound channels remain masked, never zero-imputed.

## Frozen next step

The next experiment may construct exactly one training-only mathematical cross-channel relation inside the eligible ShapeFit AP/growth/shape block. Before any fresh withheld family/mechanism is selected, it must freeze:

- the residual vector and exact covariance quotient;
- the mathematical relation being tested;
- the scalar acceptance statistic and numerical tolerance;
- a null/permutation or covariance-coordinate control;
- the channel mask and informative-bin set.

No fresh withheld family is to be chosen until that training-side relation is frozen. The withheld family must not influence channel selection, statistic, tolerance, sign convention, bin subset, or whitening convention.

## Gate consequence

Exp063A is an infrastructure/eligibility gate only. A PASS does not close G7. It narrows the admissible search space to an observationally grounded block and prevents accidental reuse of an unwhitened raw-theory separator as a discovery law.

Top-level state remains: **G7 OPEN, G8 OPEN, G9 OPEN.**
