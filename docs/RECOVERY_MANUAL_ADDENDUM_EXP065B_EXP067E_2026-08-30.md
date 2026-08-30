# DSIR recovery addendum — Exp065B through Exp067E authority chain

**Date reconciled:** 2026-08-30  
**Purpose:** recover an underrepresented Article-2 observational/operator-validation chain from repository authority after the all-chat audit.  
**Scientific state:** unchanged. `G7=OPEN`, `G8=OPEN`, `G9=OPEN`. No readiness credit.

## 1. Why this addendum exists

During the all-chat reconciliation, an older chat summary was found to conflate parts of the Exp067 sequence with later nuisance-SVD work. The repository shows a different and much more precise lineage. This addendum records only the repository/hosted-authoritative sequence and explicitly rejects the conflated chat version.

The correct chain is:

`Exp065B selected covariance eligibility PASS`

`-> Exp066B selected-bandpower closure HARD FAIL`

`-> Exp066C exact shot-noise forward-template corrective PASS`

`-> Exp067A covariance-whitening PASS`

`-> Exp067B CAMB<->CLASS physical power-convention HARD FAIL`

`-> Exp067C localization of coherence defect to native CAMB powers`

`-> Exp067D causal float32-first transfer-product diagnosis`

`-> Exp067E preregistered out-of-sample corrected convention PASS on R0/R1/R2`.

No later PASS reclassifies or erases either Exp066B or Exp067B.

## 2. Exp065B — selected covariance eligibility PASS

Repository result commit:

`11f49105cbfba77a5a64aff5201d37a207806d96`.

Status:

`PASS_ACT_UNWISE_SELECTED_COVARIANCE_ELIGIBLE_V0_1`.

Hosted provenance:

- workflow run `32980117716`;
- job `98214421282`;
- pinned `ACTCollaboration/unWISExLens_lklh@6302c30d9e70f8e4ff2d4a84a9977b4471705179`;
- archive SHA256 `1b2d1563c5eb548ca6488ed8d60c5260d9e110b743a2e3a84620cfe46fbb6570`.

Frozen selected block:

- Blue_ACT: `Clgg=6`, `Clkg=7`, total 13;
- Green_ACT: `Clgg=6`, `Clkg=7`, total 13;
- combined selected covariance: `26 x 26`;
- minimum eigenvalue `1.2742353176342933e-17`;
- maximum eigenvalue `3.980349119528573e-15`;
- direct Cholesky succeeded;
- inverse residual infinity norm `3.8167569492587215e-15`.

No jitter, clipping, diagonal loading, shrinkage, nearest-PSD projection, or scale-cut retuning was used.

Interpretation: eligibility of a reproducible ACT DR6 x unWISE lensing+clustering observational covariance block only; not a DSIR law and not G7 closure.

## 3. Exp066B — permanent selected-bandpower closure FAIL

Preservation commit:

`d278d25142bba87bd157bf80f770546d8c628602`.

Immutable status:

`FAIL_ACT_UNWISE_SELECTED_BANDPOWER_CLOSURE_V0_1`.

The preregistered audit preserved the failure rather than modifying its criteria. Repository history states that nuisance/free-CLEFT algebra, signal bandwindow/transfer mapping and selected 26-bin ordering passed, while the frozen constant-mode white-noise shortcut failed.

The failed shortcut is permanently rejected. Exp066C is a separately numbered corrective experiment and does not rewrite Exp066B.

## 4. Exp066C — exact shot-noise template corrective PASS

Integrated PASS/next-gate commit:

`d46fcd97624380422358e16466adb7aafc091e5b`.

Status:

`PASS_ACT_UNWISE_EXACT_SHOT_NOISE_TEMPLATE_V0_1`.

Hosted provenance:

- run `32989328863`;
- job `98242896864`;
- artifact `9614063228`;
- artifact ZIP SHA256 `2409cd974691f09d80893d8d64f7f61ac5bccff4e28d4eb4251a5a21baf80baf`.

Frozen checks all passed:

- C1 exact linear solve: relative residual `6.52315926577459e-15 <= 5e-11` for both Blue/Green;
- C2 upstream selected-bandpower equivalence: max selected-bin difference `4.218847493575595e-15`, below frozen ~`5.07e-12`/`5.10e-12` limits;
- C3 nonconstant-template control: `max_abs(x-1)=1.1140436272781788 > 1e-6`;
- C4 selected-vector closure: exact final length 26 in frozen ordering.

Scope is exact shot-noise forward-operator correction only. The immutable lineage explicitly retains Exp066B as FAIL. No G7 law fit or withheld-family evaluation occurred.

## 5. Exp067A — covariance-whitening PASS

Result commit:

`0e04eda9d996a48b6f4b497c0b5d360952f81499`.

Status:

`PASS_ACT_UNWISE_OBSERVATIONAL_COVARIANCE_WHITENING_V0_1`.

Hosted provenance:

- run `32994782105`;
- job `98261038810`;
- execution commit `2b02556bcac07c475d160736241c8e8b8ed0d1fc`;
- selected dimension `26`.

Key frozen checks:

- raw selected covariance symmetry ratio `0.0 <= 1e-12`;
- direct unmodified Cholesky reconstruction relative infinity residual `7.799310879558051e-17 <= 5e-12`;
- whitening identity residual `1.0425503003180775e-15 <= 5e-10`;
- deterministic round-trip relative infinity error `3.1871930361769926e-16 <= 5e-12`.

Operator hashes:

- selected covariance `<f8` bytes SHA256 `df7e285c40009e0ba20cc5d920342e1066ceff69d277fdf3233ac63463ffddb9`;
- Cholesky L SHA256 `6a30b1792d8b3f29ae66102dadb285f394f6aa4c30cba29dc3c3234a1897f109`;
- whitener W SHA256 `b32e59a98b6910427ac5026bc3f882ea8b0934b65de9abe44c599e1c7ec66822`.

No symmetrization, Hartlap rescaling, jitter, shrinkage, clipping, diagonal loading, pseudoinverse, or nearest-PSD rescue was used. This made later covariance-whitened work eligible; it did not close G7.

## 6. Exp067B — permanent CAMB<->CLASS convention HARD FAIL

Preservation/merge commit:

`abdc8c7746589c5f9a3a7e1d965108a0e14afeb3`.

Status:

`FAIL_CAMB_CLASS_PHYSICAL_POWER_CONVENTION_BRIDGE_V0_1`.

Hosted run/job recorded in the frozen result:

- run `32995950843`;
- job `98265107213`.

Pinned solvers:

- CAMB `fa3f097343fbbe427cc04b4f5f0041c22c6ec764`;
- CLASS `e85808324f51fc694d12e3ed7439552a3c3f9540`.

The source contracts and the three frozen cross-solver log statistics passed, but the CAMB adiabatic rank-one/coherence control exceeded its preregistered `5e-8` threshold. This is an immutable HARD FAIL under that frozen criterion.

No later diagnosis may reinterpret it as a PASS.

## 7. Exp067C — defect localized to native CAMB powers

Result commit:

`13334b6f66da1e2a35ad5257e34bd8f84853691f`.

Classification:

`NATIVE_CAMB_COHERENCE_DEFECT_V0_1`.

Hosted provenance:

- run `32997216952`;
- job `98269515280`;
- artifact `9617073194`;
- artifact SHA256 `836c6f0306a34a52af3b4948d525b08e3cb892f5a2dc06b923fb1dc30c5d1bfa`.

Under the inherited `5e-8` threshold:

- official native CAMB `E_max = 1.616012643701481e-7` -> FAIL;
- interpolator evaluated on native knots `E_max = 1.6160126170561284e-7` -> FAIL;
- interpolator on Exp067B targets `E_max = 9.253183930191256e-8` -> FAIL;
- interpolation reconstruction errors were only ~`1e-14`.

Thus the defect was already present in native CAMB powers and was not created by `PkInterpolator`. Exp067B remained `HARD_FAIL_UNCHANGED`.

## 8. Exp067D — float32-first transfer multiplication causally confirmed

Result commit:

`b37a1697fa8dd55b048e5b872cac670b71e93778`.

Classification:

`FLOAT32_TRANSFER_PRODUCT_CAUSALLY_CONFIRMED_V0_1`.

Hosted provenance:

- run `32998129409`;
- job `98272608213`;
- artifact `9617429413`;
- artifact SHA256 `b0377ab357f751d4703526cfb4c9aa0e925dc58c3f9f4b19662fc662f932a6d9`.

Key causal numbers:

- official native `E_max = 1.616012643701481e-7`;
- reconstructed float32-first `E_max = 1.616012642591258e-7`;
- residual-field max difference vs official `6.661338147750939e-16`;
- common-factor max spread `4.440892098500626e-16`;
- promoting the same stored transfer values before multiplication gives `E_max = 0.0`.

The source contract shows the CAMB transfer array is default-real/float32, while the power destination is double precision; two float32 transfer values are multiplied before the result is promoted by the common double-precision power factor.

This explains the numerical coherence floor. It does **not** change Exp067B from HARD FAIL.

## 9. Exp067E — preregistered out-of-sample corrected convention PASS

Merge/preservation commit:

`502af6dc9789665d373868536ff5282af8d446bf`.

Status:

`PASS_CAMB_CLASS_OUT_OF_SAMPLE_POWER_CONVENTION_V0_1`.

Hosted provenance:

- run `32998659859`;
- job `98274406590`;
- artifact `9617676816`;
- artifact SHA256 `6e6419040b7295dfe4b1b4c126a5cfeaa6e1e24a76a7e29c05ccd7c706f65ee2`.

The prospectively frozen references were exactly:

- R0 regression anchor: `h=0.67, omega_b=0.0224, omega_cdm=0.1200, A_s=2.10e-9, n_s=0.965`;
- R1 fresh low-matter/high-h: `h=0.72, omega_b=0.0220, omega_cdm=0.1050, A_s=2.00e-9, n_s=0.970`;
- R2 fresh high-matter/low-h: `h=0.62, omega_b=0.0230, omega_cdm=0.1350, A_s=2.20e-9, n_s=0.960`.

All inherited controls passed across R0/R1/R2: cross-solver spectral/log statistics, CLASS-internal Weyl control, missing-k^2 negative control, and the independently diagnosed CAMB precision signature.

The CAMB native coherence floors reproduced near `1.6-1.7e-7`; the float32-first field reconstruction matched at ~`6.66e-16`; promote-before-product residual was zero. The deliberately wrong missing-k^2 convention remained strongly rejected (~`11.98` median absolute log discrepancy vs frozen minimum `5`).

Exp067E is an out-of-sample **physical power-convention certification**. It is not a retrospective relaxation of Exp067B's failed `5e-8` criterion. Exp067B remains `HARD_FAIL_UNCHANGED`; Exp067D remains the causal numerical explanation. No G7 relation was fitted and no G8 family was exposed.

## 10. Corrected interpretation of the whole chain

The correct scientific/methodological lesson is not “a failed nuisance SVD was later fixed.” The repository-authoritative lesson is:

1. selected observational covariance and its direct whitening were reproducibly bound (Exp065B/067A);
2. a simplistic selected-bandpower shot-noise closure failed prospectively (Exp066B);
3. an exact nonconstant shot-noise template separately repaired that forward-operator issue (Exp066C) without rewriting the FAIL;
4. a separately frozen CAMB<->CLASS convention bridge then failed because its raw-CAMB coherence tolerance was stricter than the pinned solver's numerical floor (Exp067B);
5. Exp067C localized that floor to native CAMB powers;
6. Exp067D causally traced it to float32-first transfer multiplication;
7. Exp067E prospectively certified the corrected physical convention on two fresh LambdaCDM reference cosmologies while preserving the original FAIL and its numerical mechanism.

This sequence is valuable precisely because it preserves falsification, causal numerical diagnosis and out-of-sample correction as separate authority classes.

## 11. Relation to current Article-3 route

This historical chain does **not** authorize reuse of its 26-dimensional ACT x unWISE covariance in current Article-3 support selection. The current Article-3 route has its own frozen 1410-row candidate manifest, support-selection firewalls and covariance admission sequence Exp073AR->AS->AT->AU->AV.

The historical lesson carried forward is procedural:

- bind released operators/covariance exactly;
- prefer direct unrescued Cholesky;
- preserve failed frozen criteria;
- diagnose numerical floors causally;
- correct only by separately preregistered successor experiments;
- validate corrected conventions out-of-sample;
- never let a later PASS erase an earlier FAIL.

Current state remains:

`Article-3 readiness = 52%`, `Layer A=OPEN`, `Layer B=OPEN`, `covariance/whitening=BLOCKED`, `G7=OPEN`, `G8=OPEN`, `G9=OPEN`.
