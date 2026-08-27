# Exp073M source lead — DES Y3 harmonic-space Wm/WW operator pair

**Date:** 2026-08-27  
**Status:** NON-CLASSIFYING SOURCE-LEVEL FINDING UNDER FROZEN Exp073M

This note records a high-priority candidate discovered only after Exp073M was prospectively frozen. No physical-support fraction, covariance, nuisance rank, relation/null result or G8 information was used.

## Candidate structure

DES Y3 has two directly relevant harmonic-space analyses:

1. **galaxy clustering + galaxy-galaxy lensing in harmonic space** — a pseudo-`C_ell`/NaMaster measurement path supplying the Wm-type channel together with galaxy clustering;
2. **cosmic shear in harmonic space** — a pseudo-`C_ell` analysis supplying the WW-type channel.

The direct harmonic representation is attractive for Exp073M because its estimator band definition is finite in multipole space, avoiding the specific finite-theta absolute-response divergence established by Exp073L.

## Public Wm-side provenance

Paper/data-availability source:

- `Dark Energy Survey Year 3 results: cosmology from galaxy clustering and galaxy–galaxy lensing in harmonic space`, MNRAS 536 (2025) 1586;
- DOI/article: `https://academic.oup.com/mnras/article/536/2/1586/7914326`;
- data-availability section states that DES Y3 lens/source catalogues and redshift distributions are in the public DES Y3 release and that the measurement code interfacing the catalogues with NaMaster is public.

Public measurement repository:

- `hocamachoc/3x2hs_measurements`;
- pinned inspected commit: `21e589a3cfc3e30f1b06a4636ccc2da8aceda5ab` (master HEAD inspected 2026-08-27);
- repository: `https://github.com/hocamachoc/3x2hs_measurements`.

This is strong evidence for M1/M2 feasibility on the Wm side, but Exp073M does not yet mark those tests PASS until exact band/mixing products, redshift inputs and signed-cross operator semantics are bound file-by-file.

## WW-side provenance blocker

Paper:

- `Dark Energy Survey Year 3 results: cosmological constraints from the analysis of cosmic shear in harmonic space`, MNRAS 515 (2022) 1942;
- article: `https://academic.oup.com/mnras/article/515/2/1942/6625643`.

The paper explicitly uses the pseudo-`C_ell` method and public DES Y3 catalogues/redshift distributions, but its data-availability section states that the **measurement code can be obtained upon request** rather than providing an immutable public code repository.

Therefore a complete Wm+WW pair is **not yet authorized as `FINITE_POSITIVE_SUPPORT_OPERATOR_CANDIDATE_FOUND_EXP073M`**. The present blocker is provenance/operator reproducibility on the WW side, not the mathematical finiteness of pseudo-`C_ell` banding.

## Next exact task

Before any Exp073M classification:

1. inventory `hocamachoc/3x2hs_measurements@21e589a...` for exact NaMaster bins/workspaces, Wm bandpower semantics, released `n(z)` paths and whether the signed cross-spectrum can be represented before the positive envelope;
2. search for an immutable public release/repository of the DES Y3 harmonic cosmic-shear bandpowers/workspaces or an alternative public WW pseudo-`C_ell` release;
3. bind checksums/commit SHAs for the first complete Wm+WW pair;
4. evaluate M1–M8 only at source/operator level — still **no 5% support fraction**.

Exp073J threshold remains `5%`. Covariance restriction remains unauthorized. G7/G8/G9 remain OPEN.
