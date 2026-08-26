# Exp065A — Weyl/lensing observational-binding eligibility audit (2026-08-26)

## Motivation

Exp064A/F31 excluded the simplest covariance-aware homogeneous plane in the existing DESI DR1 ShapeFit AP/growth/shape block. G7 therefore remains open. The next admissible move is not to increase functional flexibility on the same five points, but to bind a genuinely independent Weyl/lensing-sensitive observable block to a public survey kernel and covariance.

## Public-product audit

### ACT DR6 lensing auto-spectrum — ELIGIBLE KERNEL/COVARIANCE BLOCK

NASA LAMBDA publishes the ACT DR6 lensing likelihood data products, explicitly including bandpowers, covariance matrices, binning matrices, fiducial spectra and likelihood-correction matrices. The ACT public likelihood consumes a binned convergence spectrum and covariance and applies a binning matrix to theory. This satisfies the repository's basic requirement that a Weyl-sensitive observable not be represented by a raw theory-space slip value.

Primary public product:
- https://lambda.gsfc.nasa.gov/product/act/actadv_dr6_lensing_lh_info.html
- https://github.com/ACTCollaboration/act_dr6_lenslike

### unWISE × ACT/Planck CMB lensing — PREFERRED CROSS-CHANNEL BINDING CANDIDATE

ACT publishes a public unWISE × CMB-lensing likelihood. Its documented data release contains bandpowers, covariances and auxiliary data and supports both cross-correlation-only and 3x2pt variants. This is stronger for G7 than lensing auto alone because it couples a Weyl-sensitive convergence field to a matter tracer with an explicit observational likelihood.

Primary public product:
- https://github.com/ACTCollaboration/unWISExLens_lklh

### Published E_G values — PHYSICALLY RELEVANT BUT NOT YET ELIGIBLE BY THEMSELVES

An E_G-style statistic is conceptually close to the desired DSIR cross-channel object because it combines lensing with clustering/RSD. However, a published scalar/table value is not sufficient for G7 unless the exact scale cuts/window operators and covariance required to reproduce the statistic are publicly bound in the repository. Therefore no E_G number is imported as a law candidate in this experiment.

## Decision

1. Keep raw theory Weyl/slip cells masked from observational G7 claims.
2. Admit ACT DR6 lensing auto as a reproducible Weyl-sensitive kernel/covariance block.
3. Prefer the public unWISE × CMB-lensing likelihood as the next cross-channel observational binding because it already contains a lensing–matter cross observable plus covariance/auxiliary products.
4. Do **not** test a G7 relation yet. First create a deterministic source/provenance selector and CI smoke test that proves the public likelihood/data interface can be reproduced without hidden local state.
5. Only after that binding is frozen may a mathematical residual relation and null statistic be preregistered. No withheld dark-sector family is selected before that freeze.

## Anti-retuning contract

F31 remains immutable. Exp065A is an eligibility/provenance decision, not a positive G7 result. G7/G8/G9 remain OPEN. Failure to make the public lensing likelihood reproducible in CI must be recorded as an infrastructure/eligibility failure, not repaired by substituting a paper-level scalar constraint.
