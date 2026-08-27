# Exp073M — finite-positive-support observational operator landscape audit — preregistration v0.1

**Date frozen:** 2026-08-27  
**Status:** PREREGISTERED BEFORE ANY Exp073M CANDIDATE CLASSIFICATION

## 1. Parent binding

Bind permanently:

- Exp073J KiDS component = `FAIL_EXP073J_KIDS_COMPONENT_REPRODUCTION_OR_NUMERICAL_COMPLETENESS` and full Exp073J scientific classification remains unauthorized;
- Exp073K = `INDETERMINATE_ABSOLUTE_RESPONSE_ASYMPTOTICS_EXP073K`;
- Exp073L = `EXTENDED_LADDER_SUPPORTS_NONNORMALIZABLE_ABSOLUTE_RESPONSE_EXP073L` from run `33049366874`, artifact `9637070322`, digest `sha256:03a8f63155c40180c81b6472828210408b472463aec244fff8c442ad7cd7c684`;
- Exp073J physical-support threshold remains exactly `5%`;
- BOSS finite-matrix component remains `54/240` retained and non-classifying.

No parent classification may be weakened or relabeled by Exp073M.

## 2. Frozen question

Does a public, reproducibly bindable observational operator/support definition exist for the missing Wm and WW channels that has a **finite P-independent positive support normalization by construction**, preserves signed Wm physics, exposes enough redshift/angular or true-k operator information for a later exact common C3+C5 support audit, and does not require covariance/model weighting or a post-hoc cutoff?

Exp073M is a source/operator landscape audit only. It does not compute the 5% physical-support fractions and cannot authorize covariance.

## 3. Candidate classes

Search public source/release material in the following fixed order, recording exact URL/repository/tag/commit/file provenance for every candidate:

1. direct harmonic/pseudo-C_ell tomographic galaxy-lensing and shear bandpowers with explicitly finite multipole band/window matrices;
2. finite Fourier or finite basis transforms whose published estimator response has compact or absolutely integrable positive support without fiducial power weighting;
3. other public joint Wm+WW observables only if their finite-positive-support property is explicit at operator level.

A candidate may combine different public releases for Wm and WW only if both are independently bindable and a later joint support audit can preserve the same common physical rectangle. BOSS remains the frozen mm component unless a future separately preregistered experiment replaces it.

## 4. Frozen tests

### M1 — public immutable provenance
PASS only if the candidate release/operator can be bound to immutable or checksum-verifiable public files/source.

### M2 — finite positive normalization by construction
PASS only if the operator's P-independent positive support measure is finite without selecting a cutoff after viewing support results. A published finite ell/k window matrix, compact basis coefficient matrix, or mathematically absolutely integrable kernel can qualify.

### M3 — no model/downstream weighting
PASS only if finiteness does not require fiducial `P(k)`, `C_ell`, covariance, nuisance, relation/null, held-out/G8, or model-specific amplitude weighting.

### M4 — Wm signed semantics
For a Wm candidate, PASS only if the physical cross-spectrum remains signed; absolute value may be used only in the support envelope after the signed observable operator is defined.

### M5 — WW independent semantics
For a WW candidate, PASS only if the lensing/Weyl auto channel is independently defined and is not manufactured from nonlinear matter through a GR closure.

### M6 — redshift/operator information
PASS only if source/lens kernels, tomography, mixing matrices, or equivalent released information are sufficient in principle to map support into `(k,z)` without using covariance or fitted cosmology.

### M7 — later 5% audit possible without changing threshold
PASS only if the candidate can in principle be subjected to the unchanged Exp073J common rectangle and `f_invalid <= 0.05` rule prospectively. Exp073M itself must not evaluate that fraction.

### M8 — no downstream leakage
No covariance, whitening, nuisance SVD/rank, G7 relation/null fit, G8 response, or held-out result may be used to select or rank candidates.

## 5. Frozen classification

Classify `FINITE_POSITIVE_SUPPORT_OPERATOR_CANDIDATE_FOUND_EXP073M` iff at least one complete pair of Wm+WW operator candidates passes M1–M8 and is sufficiently specified for a separately preregistered exact physical-support audit.

Classify `NO_FINITE_POSITIVE_SUPPORT_OPERATOR_CANDIDATE_FOUND_EXP073M` iff the frozen search classes are reproducibly audited but no complete Wm+WW candidate pair satisfies M1–M8.

Classify `FAIL_EXP073M_REPRODUCTION_OR_PROVENANCE` if source/release reproduction is insufficient to trust the landscape audit. Infrastructure interruption before complete evaluation is `INCOMPLETE_EXP073M` and is not a scientific result.

## 6. Downstream rule

A `FOUND` result authorizes only a separate preregistration that binds the chosen candidate files/operators and evaluates exact positive physical support against the unchanged C3+C5 rectangle and 5% threshold. It does not authorize covariance.

A `NO ... FOUND` result authorizes a new prospective observational-strategy/design branch; it does not authorize a post-hoc KiDS ell cutoff, fiducial-power weighting, or changing Exp073J.

G7 OPEN.  
G8 OPEN.  
G9 OPEN.
