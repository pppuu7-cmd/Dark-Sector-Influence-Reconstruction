# DSIR Article 3 — covariance / whitening fail-closed contract v0.1

**Date:** 2026-08-28  
**Status:** prospective architecture freeze before Article-3 covariance authorization.  
**No real covariance is inspected and no G7 statistic is evaluated here.**

## Purpose

Article 3 eventually compares finite-operator responses in an observational metric. That metric is scientifically meaningful only if the support-restricted covariance is bound to exactly the same ordered coordinates and passes a fail-closed numerical validity gate before any whitening, nuisance quotient or G7 relation/null statistic is evaluated.

This contract freezes the covariance-validation logic prospectively, before the current Exp073R1 prerequisite and physical-support gate have authorized covariance use.

## Mandatory order

`true reproduction -> physical support -> finite observation operator -> covariance coordinate binding -> covariance validation -> Cholesky whitening -> signed nuisance subspace -> nuisance quotient -> G7`

The following are forbidden:

- inspecting target/nuisance geometry before choosing covariance repairs;
- diagonal jitter added after seeing Cholesky failure;
- eigenvalue clipping or nearest-SPD replacement;
- silent symmetrization `(C+C^T)/2` as a repair;
- silent coordinate reordering;
- covariance-mode deletion selected to improve a later quotient or G7 statistic;
- use of `C^{-1}` by explicit matrix inversion when a triangular solve is available.

## 1. Immutable parent binding

A future covariance artifact must record at minimum:

- parent physical-support run/job/artifact/head SHA;
- parent retained-coordinate manifest path and SHA256;
- covariance source identity and immutable source digest;
- ordered covariance-coordinate manifest and SHA256;
- exact permutation map if the authoritative covariance order differs from the frozen support order.

The ordered support-coordinate hash and the coordinate sequence used to restrict covariance must agree exactly after applying only the prospectively declared permutation map.

A mismatch is not a scientific FAIL. It is:

`INVALID_FOR_SCIENCE_COVARIANCE_COORDINATE_BINDING`.

## 2. Shape and finiteness

For retained support dimension `d`, require

`C_S.shape == (d,d)`.

Every entry must be finite. The diagonal must be finite and strictly positive.

Terminal invalid states:

- `INVALID_FOR_SCIENCE_COVARIANCE_DIMENSION_MISMATCH`
- `INVALID_FOR_SCIENCE_COVARIANCE_NONFINITE`
- `INVALID_FOR_SCIENCE_COVARIANCE_NONPOSITIVE_DIAGONAL`

No rows or columns may be dropped to repair these states.

## 3. Symmetry gate

Define

`rho_sym = ||C_S - C_S^T||_F / max(||C_S||_F, tiny)`.

For float64 arithmetic freeze

`tau_sym(d) = 1000 * eps64 * max(1,d)`

with `eps64 = numpy.finfo(float).eps`.

Require

`rho_sym <= tau_sym(d)`.

The validator may use `(C_S+C_S^T)/2` only **after** the raw matrix has passed this symmetry gate, solely as a roundoff-neutral factorization copy. The raw residual and both hashes must be retained. A matrix that fails the gate may not be repaired by symmetrization.

Failure state:

`INVALID_FOR_SCIENCE_COVARIANCE_NONSYMMETRIC`.

## 4. Positive-definite gate

After symmetry PASS, attempt an ordinary lower-triangular Cholesky factorization

`C_sym = L L^T`.

Cholesky failure is terminal for the current Article-3 route:

`INVALID_FOR_SCIENCE_COVARIANCE_NOT_POSITIVE_DEFINITE`.

No pseudowhitening, eigenvalue clipping or jitter is authorized by this v0.1 contract. If a scientifically justified PSD route is ever needed, it must be separately preregistered before inspecting the target/nuisance quotient.

## 5. Factorization backward-error gate

Define

`rho_chol = ||C_sym - L L^T||_F / max(||C_sym||_F, tiny)`.

Freeze

`tau_chol(d) = 1000 * eps64 * max(1,d)`.

Require

`rho_chol <= tau_chol(d)`.

Failure state:

`INVALID_FOR_SCIENCE_COVARIANCE_CHOLESKY_RESIDUAL`.

## 6. Whitening definition

For any support-restricted response vector `x`, define whitening by triangular solve

`w = solve(L, x)`.

Do not form `inv(L)` or `inv(C_S)` in the scientific implementation.

The metric identity is

`||w||_2^2 = x^T C_S^{-1} x`.

The implementation must retain a deterministic solve-consistency unit test using synthetic vectors.

## 7. Whitening consistency diagnostic

For validator-only matrix QA define

`I_hat = solve(L, solve(L, C_sym).T).T`

which evaluates `L^{-1} C_sym L^{-T}` without explicit inverses.

Define

`rho_white = ||I_hat-I||_F / max(1,d)`.

Freeze a conservative float64 acceptance threshold

`tau_white = sqrt(eps64)`.

Require

`rho_white <= tau_white`.

This threshold is frozen before real covariance inspection. It is intentionally much looser than ordinary backward error but still rejects catastrophic whitening instability.

Failure state:

`INVALID_FOR_SCIENCE_COVARIANCE_WHITENING_RESIDUAL`.

## 8. Conditioning diagnostics

Always record:

- smallest and largest eigenvalues of the already symmetry-passed matrix for diagnostics only;
- `kappa_2(C_sym)`;
- `rho_sym`;
- `rho_chol`;
- `rho_white`.

No condition-number cutoff is used to delete modes in v0.1. Numerical instability is judged by the frozen factorization/whitening residual gates above. An ill-conditioned covariance that nevertheless passes all frozen gates remains admissible; one that fails may not be repaired post hoc.

## 9. Coordinate-permutation invariance unit test

Synthetic QA must verify that a simultaneous permutation of

- response coordinates;
- covariance rows/columns;
- nuisance rows

leaves whitened metric norms and final subspace diagnostics invariant within frozen numerical tolerance.

Permuting only one object must be detected as a coordinate-binding error by manifest/hash logic in the future scientific implementation.

## 10. Required synthetic negative controls

Before real covariance use, software QA must contain deterministic cases for:

1. valid SPD covariance -> PASS;
2. wrong matrix shape -> dimension invalid;
3. NaN/Inf -> nonfinite invalid;
4. nonpositive diagonal -> invalid;
5. material asymmetry -> nonsymmetric invalid;
6. symmetric indefinite matrix -> Cholesky invalid;
7. singular positive-semidefinite matrix -> Cholesky invalid;
8. valid but strongly correlated SPD matrix -> PASS if frozen residual gates pass;
9. simultaneous coordinate permutation -> invariant;
10. response/covariance order mismatch -> future binding layer must fail closed.

Synthetic tests are architecture QA only and must never consume real survey files.

## 11. Terminal classification

A covariance object is authorized for downstream whitening only if every upstream and covariance gate is terminal PASS. The positive terminal label is

`PASS_ARTICLE3_COVARIANCE_WHITENING_V0_1`.

Any invalid covariance state blocks nuisance quotient and G7. It is not evidence for or against dark-sector physics.

## 12. G7 firewall

This contract does not authorize covariance execution now. Real covariance inspection starts only after:

1. Exp073R1 true reproduction PASS;
2. physical-support classification PASS;
3. retained-coordinate manifest is frozen and immutable.

Only covariance PASS can authorize the already-frozen signed nuisance-subspace contract.

Current state remains:

- `G7 = OPEN`
- `G8 = OPEN`
- `G9 = OPEN`
- covariance/whitening execution = NOT AUTHORIZED
- nuisance quotient execution = NOT AUTHORIZED

## Contract verdict

`ARTICLE3_COVARIANCE_WHITENING_FAILCLOSED_ARCHITECTURE_FROZEN_V0_1`
