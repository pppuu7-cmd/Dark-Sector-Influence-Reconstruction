# DSIR research checkpoint — Exp068A active / G7 bridge audits — 2026-08-26

## Immutable scientific lineage

Start from `main@502af6dc9789665d373868536ff5282af8d446bf`, after merged Exp067E.

Preserved top-level state:

- F27: HARD FAIL;
- F29: HARD PROSPECTIVE FAIL;
- F30: HARD PROSPECTIVE PASS;
- F31: `NO_NONTRIVIAL_COMMON_PLANE_RELATION_V0_1`;
- Exp067B: permanent FAIL under its frozen raw-CAMB coherence threshold;
- Exp067E: prospective PASS for corrected CAMB↔CLASS physical power convention on R0/R1/R2;
- G7/G8/G9: OPEN.

Active PR: #71, branch `research/post-exp067e-recovery-and-exp068a-prereg`.

## 1. Exp068A remains preregistered and unretuned

Exp068A asks whether the DSIR solver-neutral linear/no-CLEFT ACT×unWISE raw projector reproduces the exact pinned upstream algebra on a real LambdaCDM CAMB cosmology and real released Blue/Green redshift kernels.

Frozen before the first physical comparison:

- upstream likelihood `ACTCollaboration/unWISExLens_lklh@6302c30d9e70f8e4ff2d4a84a9977b4471705179`;
- CAMB `fa3f097343fbbe427cc04b4f5f0041c22c6ec764`;
- official data archive SHA256 `1b2d1563c5eb548ca6488ed8d60c5260d9e110b743a2e3a84620cfe46fbb6570`;
- `ell=0..6143`;
- `z=[0,3]`;
- interface `kmax=10 Mpc^-1`;
- Gauss-Legendre order 96;
- componentwise tolerance factor `5e-13`;
- nontriviality checks on physical raw basis pieces;
- no CLEFT, no G7 fit, no fresh G8 family.

The first NERSC attempt (`33001472791`) failed before science because the runner could not connect to `portal.nersc.gov`; no physical comparison executed and therefore this is **infrastructure-only**, not `FAIL_ACT_UNWISE_PHYSICAL_FORWARD_REPRODUCTION_V0_1`.

A second infrastructure path was added using the official NASA LAMBDA mirror first, NERSC fallback second, while requiring the exact same frozen archive SHA256 before extraction. This changes no scientific criterion or byte-level accepted dataset.

Current mirror run:

- workflow run `33003973559`;
- job `98292701587`;
- at this checkpoint all build/source steps have passed;
- the job remains inside `Fetch and verify official ACT x unWISE data archive`;
- the physical comparison has not yet started.

The public ACT/NERSC landing page and NASA LAMBDA product page both identify the likelihood dataset as a released tarball containing bandpowers, covariances, binning matrices, likelihood-correction material, redshift distributions and transfer functions. No official small-file substitute was used.

## 2. Nuisance inventory correction

Pinned `XCorrACT` has exactly 18 named nuisance parameters: 8 Blue and 10 Green.

However, four are CLEFT-shift directions. In the Exp068A no-CLEFT map those columns are algebraically zero, so

\[
\operatorname{rank}J_{\eta,\mathrm{no-CLEFT}}\le14.
\]

The actual rank is unknown and must be determined only under a separately preregistered SVD threshold/normalization/derivative rule. Parameter count is not rank.

See `docs/ACT_UNWISE_NUISANCE_TANGENT_INVENTORY_2026-08-26.md`.

## 3. Public CLEFT is not solver-neutral for arbitrary DSIR models

The pinned public CLEFT branch forms a higher-order Weyl–matter contribution from a matter CLEFT contribution using `matter2weyl_factor`, a GR Poisson-type conversion. DSIR may not silently apply this to arbitrary MG/dark-sector models whose metric response is independent.

Therefore a first rigorous G7 attempt may use an explicitly labelled **linear/no-CLEFT observational subspace**, while a future general nonlinear bridge must accept independent higher-order Weyl/matter information rather than impose a GR identity.

See `docs/ACT_UNWISE_CLEFT_SOLVER_NEUTRALITY_BOUNDARY_2026-08-26.md`.

## 4. Training-family physical power-input feasibility

### Designer f(R) / C5

Pinned `EFTCAMB/EFTCAMB@16d9c4e9f85751e30efd0a53b177941713078904` preserves the standard CAMB power-variable contract. It exposes `delta_nonu` and `Weyl=k^2(phi+psi)/2`, and CAMB can form the signed cross power directly. Thus linear C5 is source-level feasible for direct

\[
P_{mm},\quad P_{Wm},\quad P_{WW}
\]

without Poisson reconstruction. A prospective bridge is still required before observational use.

### GDM / C3

Pinned `s-ilic/gdm_class_public@4c87916aab5ca124a68f1dd16f31846fc13d1829` constructs its total `mPk` from internal `index_tp_delta_m`, the gauge-invariant/comoving matter source. For the frozen C3 manifold (`omega_cdm=0`, `omega_gdm=0.1200`, `w_gdm=0`, adiabatic single IC), the source is based on baryon+GDM matter and the standard comoving velocity correction.

Crucially, ordinary CLASS-format `mTk` does **not** export this internal `delta_m`; it exports species densities and `d_tot`. Therefore `d_tot` substitution is forbidden.

The clean future route is a read-only accessor for the already computed `index_tp_delta_m`, with a hard reconstruction check against the solver's own `mPk`. Then, for the single adiabatic mode,

\[
q_W=k^2\frac{\phi+\psi}{2D_m},\qquad
P_{Wm}=q_WP_m,\qquad
P_{WW}=q_W^2P_m.
\]

This is a transfer-product identity, not a Poisson reconstruction.

See `docs/G7_LINEAR_TRAINING_POWER_INPUT_FEASIBILITY_2026-08-26.md`.

## 5. Redshift-PCA noise-bias boundary

The released noise-bias correction is caused by nonlinear averaging over uncertain redshift-distribution PCA coefficients, not by CLEFT itself. The pinned wrapper retains nonzero corrections for `gg_bsq`, `gmu_b`, and `kg_b` even when CLEFT is absent.

However, the released correction was computed at a fixed fiducial cosmology. DSIR must therefore distinguish:

1. an **upstream-fidelity** linear/no-CLEFT contract using released fixed correction templates exactly as published;
2. a stronger **model-neutral** contract that recomputes the PCA expectation for each model.

The choice must be frozen before nuisance-rank singular values or G7 performance are inspected.

See `docs/ACT_UNWISE_NOISE_BIAS_MODEL_NEUTRALITY_BOUNDARY_2026-08-26.md`.

## 6. Physical validity mask must precede whitening/SVD

A major sequencing correction was identified.

Exp068A's `kmax=10 Mpc^-1` is an **interface reproduction domain**, not a certification that linear C3/C5 physics is valid to that scale. The released angular bandpowers combine a redshift projection with mask coupling/bandwindows, so each selected observable has extended `(k,z)` support.

DSIR's rule remains: invalid theory support is missing, never zero.

Therefore, before a nuisance tangent rank is measured, a separately preregistered support/leakage audit must freeze a common observable validity mask for the candidate training families. If the retained coordinate set is `M`, then the covariance must be subselected first,

\[
\Sigma_M=S_M\Sigma S_M^T,
\]

and only then whitened by its own direct Cholesky factor. Full-26D whitening followed by coordinate deletion is not generally equivalent.

This corrects the earlier informal order. The rigorous sequence is now:

1. finish Exp068A;
2. validate C3/C5 physical power bridges;
3. freeze family physical `(k,z)` validity domains;
4. freeze survey-kernel/bandwindow support-leakage statistic and common observable mask;
5. bind/whiten the covariance submatrix of that mask;
6. validate retained-coordinate nuisance/bandpower closure including the chosen PCA noise-bias contract;
7. only then preregister and measure nuisance tangent rank;
8. quotient nuisances, fit one training-only relation, and run its frozen null/permutation control;
9. freeze the relation before selecting any fresh G8 withheld family.

See `docs/G7_LINEAR_OBSERVATIONAL_VALIDITY_MASK_BOUNDARY_2026-08-26.md`.

## 7. Current scientific boundary

No new universal law or discovery claim has been made during this iteration. The iteration improved the admissible experiment design and removed several routes to false positive G7 evidence:

- parameter count cannot masquerade as nuisance rank;
- public GR CLEFT conversion cannot masquerade as solver neutrality;
- `d_tot` cannot masquerade as GDM's gauge-invariant matter source;
- a LambdaCDM-fiducial PCA noise-bias template cannot silently masquerade as exact model-neutral correction;
- broad numerical `kmax` cannot masquerade as physical linear validity;
- invalid survey support cannot be zero-imputed before whitening.

G7/G8/G9 remain OPEN.
