# Exp068B — literal upstream PCA semantics physical forward reproduction v0.1

**Date:** 2026-08-26  
**Status:** scientific contract frozen before the first Exp068B physical rerun.

## Why this experiment exists

Exp068A is permanently preserved as

`FAIL_ACT_UNWISE_PHYSICAL_FORWARD_REPRODUCTION_V0_1`.

Its failure was isolated to the preregistered tracer/PCA binding check. The same run simultaneously found:

- exact pinned provenance PASS;
- physical CAMB `P_WW`, `P_Wm`, `P_mm` sanity PASS;
- nontrivial physical signal control PASS;
- raw upstream-vs-DSIR component equivalence PASS, with zero numerical difference for every compared component.

The Exp068A tracer check had frozen the statement that the released Blue/Green correction files contain exactly 3/5 columns beyond redshift and that `dNdz.n_pcs` must therefore equal 3/5. Inspection of the pinned upstream source after that frozen FAIL showed a different literal convention:

1. the correction file contains **mean Delta dN/dz first**, followed by sampled PCA modes;
2. `dNdz.n_pcs` counts all correction columns, i.e. mean + sampled PCs;
3. the final coefficient vector used by the upstream evaluator is

   `pca_coeff_final = [1, 1, c_0, c_1, ...]`,

   where the first `1` is the fiducial cross-correlation `b dN/dz`, the second `1` fixes the mean correction, and only the remaining coefficients are sampled nuisance directions.

Exp068B is a separately numbered corrective experiment. It does **not** alter Exp068A, does not retrospectively redefine its PASS criterion, and does not claim that Exp068A passed.

## Purpose

On the same pinned physical R0 cosmology, the same official ACT x unWISE release, the same full raw multipole domain and the same no-CLEFT projector, test whether the physical forward adapter passes when the tracer basis is bound with the literal pinned-upstream PCA semantics.

This remains a forward-adapter validation only. It does not fit ACT data, does not construct the nuisance quotient, does not fit a G7 relation and does not select a G8 withheld family.

## Immutable provenance

Pinned upstream likelihood:

`ACTCollaboration/unWISExLens_lklh@6302c30d9e70f8e4ff2d4a84a9977b4471705179`.

Pinned CAMB:

`cmbant/CAMB@fa3f097343fbbe427cc04b4f5f0041c22c6ec764`.

Official data archive:

`data_unWISExLens.tar.gz`

SHA256:

`1b2d1563c5eb548ca6488ed8d60c5260d9e110b743a2e3a84620cfe46fbb6570`.

Any provenance mismatch is a hard Exp068B FAIL.

## Frozen cosmology and physical domain

Exactly inherit Exp068A:

- `H0=67 km/s/Mpc`, `h=0.67`;
- `ombh2=0.0224`;
- `omch2=0.1200`;
- `omk=0`;
- `mnu=0`, `nnu=3.046`;
- `TCMB=2.7255 K`;
- `YHe=0.24`;
- `As=2.10e-9` at `k_pivot=0.05 Mpc^-1`;
- `ns=0.965`;
- `w=-1`;
- linear spectra only;
- no HALOFIT, HMcode or CLEFT;
- raw `ell=0,...,6143`;
- `0 <= z <= 3`;
- projector `kmax=10 Mpc^-1`;
- CAMB interpolation grid may extend to `12 Mpc^-1`;
- Gauss-Legendre order `N_integration=96`;
- equivalence tolerance factor `5e-13`.

No physical setting, numerical tolerance or raw support from Exp068A may be changed to rescue Exp068B.

## Frozen released tracer files

Blue:

- `aux_data/dndz/unWISE_blue_xmatch_dndz.txt`;
- `aux_data/dndz/unWISE_blue_xcorr_bdndz.txt`;
- `aux_data/dndz/unWISE_blue_delta_bdndz_pcs.dat`.

Green:

- `aux_data/dndz/unWISE_green_xmatch_dndz.txt`;
- `aux_data/dndz/unWISE_green_xcorr_bdndz.txt`;
- `aux_data/dndz/unWISE_green_delta_bdndz_pcs.dat`.

## Frozen literal PCA semantics

Let `N_samp` be the number of sampled PCA nuisance coefficients in the likelihood.

Freeze:

- Blue: `N_samp = 3`;
- Green: `N_samp = 5`.

The pinned correction-file contract is:

`[z, mean_delta_bdndz, PC_0, ..., PC_(N_samp-1)]`.

Therefore the expected correction-basis width returned by the PCA interpolator is:

- Blue: `1 + N_samp = 4`;
- Green: `1 + N_samp = 6`.

The `dNdz.bdNdz(z, pcs=True)` expansion prepends the fiducial cross-correlation `b dN/dz`, so its expected width is:

- Blue: `2 + N_samp = 5`;
- Green: `2 + N_samp = 7`.

The upstream evaluator must admit exactly `N_samp` sampled coefficients and internally form

`[1, 1, c_0, ..., c_(N_samp-1)]`.

At zero sampled PCA displacement this is

- Blue: `[1, 1, 0, 0, 0]`;
- Green: `[1, 1, 0, 0, 0, 0, 0]`.

No alternative interpretation is allowed after the first Exp068B output.

## Physical spectra

Use independent pinned-CAMB linear interpolators in physical units:

- `('Weyl','Weyl') -> P_WW`;
- `('Weyl','delta_nonu') -> P_Wm`;
- `('delta_nonu','delta_nonu') -> P_mm`.

Use the Exp067E-certified Weyl convention `W = k^2(phi+psi)/2`. No Poisson reconstruction and no forced rank-one replacement are allowed.

## Exact reference and DSIR implementation

Reference:

`unWISExLens_theory_model.compute_raw_spectra`

from the pinned upstream commit, no-CLEFT branch, using exact pinned `evaluate_pk_kmax`.

DSIR side:

`src/dsir/act_unwise_projection.py::compute_raw_no_cleft`.

Both receive the same cosmology object, tracer objects and physical power interpolators.

## Hard tests

### B1 — provenance

Require exact upstream commit, CAMB commit and archive SHA256.

### B2 — literal tracer/PCA basis binding

For each sample require:

1. all three released tracer files exist and are finite;
2. correction file width is exactly `2 + N_samp` columns including redshift;
3. pinned `dNdz.n_pcs == 1 + N_samp`;
4. `bdNdz(z, pcs=True)` has width `2 + N_samp` on all frozen projection nodes;
5. xmatch and expanded cross-correlation arrays are finite and nonzero on the projection support;
6. the pinned evaluator source contains the literal dimensional rule `len(pca_coeff[i]) == n_pcs - 1` and constructs a leading fixed pair `[1.0, 1.0]` when PCA marginalisation is active.

### B3 — physical provider sanity

At `z={0.5,1.0,2.0}` and `k={0.02,0.10,0.20} Mpc^-1` require finite `P_WW`, `P_Wm`, `P_mm`, strictly positive auto powers and nonzero cross power.

### B4 — full raw-component equivalence

For every returned Blue/Green raw component and `bdndz_norm`, require identical keys, shapes and finite patterns and

`max_abs(DSIR-reference) <= 5e-13 * max(1, max_abs(reference))`.

If the reference component is identically zero, DSIR must be identically zero in the same component.

### B5 — nontrivial physical signal control

For each sample require nonzero:

- `kg/kg_b`;
- `kg/kmu`;
- `gg/gg_bsq`;
- `gg/gmu_b`;
- `gg/mumu`;
- `bdndz_norm`.

Require exactly zero no-CLEFT slots:

- `kg/kg_nob`;
- `gg/gg_b`;
- `gg/gg_nob`;
- `gg/gmu_nob`.

### B6 — zero-displacement coefficient-vector sanity

Construct the literal zero-nuisance coefficient vectors of lengths 5/7,

`[1,1,0,...]`,

and require exact dimensional compatibility with the raw `kg_b` final axis and `bdndz_norm` vector for Blue/Green. Require the normalization dot product to be finite and nonzero.

This is a dimensional/semantic control, not a likelihood fit.

## Hard outcome

PASS iff B1-B6 all pass:

`PASS_ACT_UNWISE_LITERAL_PCA_PHYSICAL_FORWARD_V0_1`.

Otherwise:

`FAIL_ACT_UNWISE_LITERAL_PCA_PHYSICAL_FORWARD_V0_1`.

The workflow must preserve either scientific outcome as an artifact. Scientific FAIL must not be converted into an infrastructure exception.

## Anti-retuning

After the first Exp068B physical output, do not change:

- commits or archive;
- physical cosmology;
- tracer files;
- `N_samp=3/5`;
- literal mean-plus-PC interpretation;
- multipole/redshift/k support;
- integration order;
- power variables;
- no-CLEFT scope;
- tolerance;
- PASS/FAIL logic.

Infrastructure failures occurring before the scientific comparison may be repaired only when these frozen conditions remain unchanged.

## Gate semantics

A PASS would validate the missing physical linear/no-CLEFT raw forward bridge under the literal released upstream tracer convention. It would **not** close G7/G8/G9.

Even after PASS, the next step is not an immediate full 26D SVD. The already-audited ordering is:

1. preregister a physical survey-kernel validity/leakage mask;
2. restrict the released covariance to the retained selected bins;
3. whiten only that valid subspace;
4. construct the no-CLEFT nuisance tangent Jacobian, whose structural rank is bounded by 14 because the four `shift_cleft_*` directions are identically absent;
5. freeze the numerical SVD rank rule before any G7 relation is fitted.

A FAIL remains a scientific finding and blocks that quotient until separately diagnosed.

Top-level state entering Exp068B: **G7 OPEN, G8 OPEN, G9 OPEN**.
