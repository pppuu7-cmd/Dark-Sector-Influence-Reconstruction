# Exp073M — finite-positive-support observational operator landscape result v0.1

**Date:** 2026-08-27  
**Scientific classification:** `FINITE_POSITIVE_SUPPORT_OPERATOR_CANDIDATE_FOUND_EXP073M`

## Parent preservation

Exp073J KiDS component remains `FAIL_EXP073J_KIDS_COMPONENT_REPRODUCTION_OR_NUMERICAL_COMPLETENESS`; Exp073K remains `INDETERMINATE_ABSOLUTE_RESPONSE_ASYMPTOTICS_EXP073K`; Exp073L remains `EXTENDED_LADDER_SUPPORTS_NONNORMALIZABLE_ABSOLUTE_RESPONSE_EXP073L`. The Exp073J physical-support threshold remains exactly 5%, and the BOSS finite-matrix mm component remains 54/240 retained and non-classifying.

No 5% physical-support fraction, covariance, nuisance rank/SVD, relation/null or G8 quantity was evaluated in Exp073M.

## Frozen search outcome

A complete public Wm+WW operator pair satisfying the frozen M1–M8 landscape requirements exists by combining two direct harmonic/pseudo-C_ell DES analyses:

1. **Wm candidate — DES Y3 galaxy clustering + galaxy-galaxy lensing in harmonic space.** The publication states that the measurement uses pseudo-C_ell and that its DES-catalogue/NaMaster measurement code is publicly available at `hocamachoc/3x2hs_measurements`. The operator source is immutably bound here to commit `21e589a3cfc3e30f1b06a4636ccc2da8aceda5ab`.
2. **WW candidate — DES Y1 cosmic shear in harmonic space.** The publication states that the pseudo-C_ell measurement pipeline is publicly available at the same repository. At the same immutable commit, `cshtest.py` explicitly constructs finite NaMaster bins, computes shear-shear mode-coupling workspaces, stores `get_bandpower_windows()`, computes coupled signed spectra and decouples them. The frozen Y1 metacal configuration points to four source tomographic bins and `etc/binNicola2020.txt`; that bin file contains explicit finite ell edges.

The pair is allowed by Exp073M section 3 because Wm and WW may come from different public releases if independently bindable and a later joint support audit preserves the same common physical rectangle. BOSS remains the frozen mm component.

## Exact source bindings

Operator repository:

- repository: `hocamachoc/3x2hs_measurements`;
- commit: `21e589a3cfc3e30f1b06a4636ccc2da8aceda5ab`;
- tree verified from the GitHub object at that commit;
- WW field/operator source: `csh.py`, blob `4b81b23e0074d7e4bb8c1e1cb9c8b916c5549787`;
- WW estimator source: `cshtest.py`, blob `33c4d3ae40098dec70a7a90f7115b16a7083aed4`;
- Y1 WW configuration: `etc/y1mcal_csh.yml`, blob `6cfb2291ab6f64116ed7a7df203fa0488bd45e81`;
- finite ell edges: `etc/binNicola2020.txt`, blob `4230a1a3b10cc631e98a03d0ed6e288b35ed6cd4`;
- Wm estimator evidence: `ggltest.py`, blob `3b52360549230e5805252bfb2c5fdbaae885a01c`.

The DES Y1 harmonic cosmic-shear paper's data-availability statement points to the public DES Y1 catalogue release and this public pipeline. The DES Y3 harmonic clustering+GGL paper's data-availability statement says the Y3 release includes the lens/source catalogues and redshift distributions used in that analysis and points to the public measurement repository.

The separate DES Y3 cosmic-shear harmonic analysis is **not** used as the WW candidate because its publication says its measurement code is available only upon request; it therefore does not independently pass frozen M1.

## Frozen M1–M8 evaluation

- **M1 PASS — public immutable provenance.** Both chosen operator implementations are source-bindable at one exact public Git commit. Public DES Y1/Y3 releases are identified for the required catalog/redshift inputs; exact data-file checksums must be frozen prospectively before the next support computation.
- **M2 PASS — finite positive normalization by construction.** NaMaster uses explicitly finite ell bins and produces finite bandpower window/mode-coupling objects. `cshtest.py` and `ggltest.py` save `get_bandpower_windows()` and MCM workspaces. A later support envelope may take the absolute value only after this finite signed operator is defined; no asymptotic ell cutoff is selected from support results.
- **M3 PASS — no model/downstream weighting.** Estimator finiteness follows from the finite pixelized map/pseudo-C_ell bandpower operator and finite bin definitions. No fiducial P(k), C_ell, covariance, nuisance, relation/null or held-out weighting is needed to normalize the operator.
- **M4 PASS — Wm signed semantics.** The GGL estimator computes the galaxy–shear cross-spectrum through `compute_coupled_cell` and linear decoupling; no absolute-value replacement defines the physical cross observable.
- **M5 PASS — WW independent semantics.** The WW observable is directly measured from two shear fields and their shear-shear coupling workspace. It is not manufactured from nonlinear matter via a GR closure.
- **M6 PASS — redshift/operator information.** DES releases identify lens/source tomography and redshift distributions, while the pinned source supplies finite ell bins, map construction, mode coupling and bandpower-window semantics. This is sufficient in principle for a later (k,z) support mapping without covariance or fitted cosmology.
- **M7 PASS — unchanged 5% audit remains possible.** The finite bandpower response can be projected through source/lens kernels and tested against the already frozen common C3+C5 rectangle using exactly `f_invalid <= 0.05`. Exp073M does not evaluate that fraction.
- **M8 PASS — no downstream leakage.** No covariance, whitening, nuisance SVD/rank, G7 relation/null, G8 response or held-out result was used to select this pair.

## Important boundary

`FINITE_POSITIVE_SUPPORT_OPERATOR_CANDIDATE_FOUND_EXP073M` is an **operator/source landscape result only**. It does not say that DES Y3 Wm or DES Y1 WW will pass the common physical-support rectangle. In particular, low-redshift tails may later make some or all coordinates fail the unchanged 5% rule. That question is delegated to a separately preregistered exact support experiment.

The next experiment must first bind exact public DES Y1/Y3 redshift/mask/operator inputs by checksum and reproduce the finite NaMaster bandpower response. Only then may it calculate positive physical-support leakage for Wm/WW and combine it with the frozen BOSS mm component.

G7 OPEN.  
G8 OPEN.  
G9 OPEN.
