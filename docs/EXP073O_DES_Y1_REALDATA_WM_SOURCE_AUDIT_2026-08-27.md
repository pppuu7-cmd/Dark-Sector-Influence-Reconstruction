# Exp073O — DES Y1 real-data Wm candidate source/provenance audit

**Date:** 2026-08-27  
**Parent preregistration:** `experiments/073o_public_realdata_finite_harmonic_wm_replacement_prereg_v0_1.md`  
**Candidate disposition:** `REJECT_DES_Y1_CANDIDATE_ON_O3_EXACT_PUBLIC_INPUT_BINDING`  
**Exp073O global classification:** **NOT YET ASSIGNED**

## Scope

This is a candidate-level source/operator audit under the already-frozen Exp073O O1–O8 criteria. It does not compute physical-support fractions, does not modify the common physical rectangle or the future 5% threshold, and does not use covariance, nuisance directions, relation/null residuals or G8 information.

## Immutable operator source

Candidate lineage:

`hocamachoc/3x2hs_measurements@21e589a3cfc3e30f1b06a4636ccc2da8aceda5ab`

Relevant source blobs:

- `ggltest-old.py` — `58a0c4fa975115be778fb00a6a06000f0e2dd121`;
- `mcm_ggltest.py` — `8d27e005beb787f7aa33d84c73b05ac9cd9e500f`;
- `mcalcat.py` — `d8544fb86312a02ffd402577acb6b6fe0647f357`;
- `ggmap.py` — `016aa1b98fee340948eea221f927babe43c76045`;
- `gcltest.py` — `c438c14e6a2d31c58f0e5effbca01e855851939d`.

## Frozen-criterion audit

### O1 — public immutable real-data provenance: PARTIAL/PASS at operator-code level

The pinned source contains an explicit `type == "y1metacal"` real-data execution branch. This is materially different from the Exp073N Y3 path, whose public configuration was simulation-only. The Y1 code consumes Metacal source data and real redMaGiC lens maps rather than FLASK realizations.

This establishes a public immutable real-data *operator implementation path*, but it does not by itself establish exact public input reproducibility.

### O2 — finite operator: PASS structurally

The Y1 path constructs finite `NmtBin` ell bins, builds NaMaster fields and a finite mode-coupling workspace, and exposes `w.get_bandpower_windows()`. The positive support envelope can therefore be defined later from the absolute finite bandpower response without introducing fiducial cosmological weighting.

### O3 — exact public inputs bindable: FAIL for this candidate

The decisive blocker is the lens-side input realization. The real-data Y1 branch reads

- `redmagic/wcountsmap_zbin{i}.fits` for five lens bins, and
- `redmagic/maskmap.fits`,

from a site-local `redmagic` directory supplied by the YAML configuration.

The pinned repository does not contain these FITS products and, in the audited source tree, no generator was found that constructs them from a publicly pinned redMaGiC catalogue with frozen cuts, weights, mask semantics and exact pixelization. A source search for `wcountsmap_zbin` finds readers, not a reproducible producer. `ggmap.py` constructs source shear maps and does not generate the redMaGiC lens count/mask products. `gcltest.py` implements the clustering measurement only for `type == "flask"`, not a real-data redMaGiC reconstruction path.

The source-side Metacal path also requires an external redshift-binning FITS file with `zbin_mcal` and sheared-bin assignments. Public availability of the underlying DES Y1 catalogues is not sufficient under frozen O3: the exact catalogue-derived objects used by this operator must be publicly identifiable and prospectively checksum-bindable.

Therefore this DES Y1 candidate cannot be promoted to `PUBLIC_REALDATA_FINITE_HARMONIC_WM_REPLACEMENT_FOUND_EXP073O`.

### O4 — signed Wm: PASS structurally

The cross observable is measured directly as `compute_coupled_cell(field_i, field_j)` and decoupled by the NaMaster workspace. No absolute value is inserted into the measured galaxy–shear cross spectrum. Absolute values remain reserved for a future support envelope.

### O5 — no GR closure: PASS

The estimator is a direct galaxy-density × shear cross observable. It is not synthesized from matter power through a GR Poisson/slip relation.

### O6 — no model/downstream weighting: PASS for operator construction

The finite operator construction requires masks, fields and angular bins, not fiducial `P(k)`, `C_ell`, covariance, nuisance, relation/null or G8 weighting.

### O7 — exact support audit remains possible: BLOCKED BY O3

If exact public lens maps/mask plus source redshift inputs (or a public deterministic generator with all selections frozen) are later found and checksum-bound, the finite NaMaster bandpower windows would be suitable for a separately preregistered support mapping. Until then O7 cannot be promoted for this candidate.

### O8 — provenance completeness: FAIL for candidate promotion

Source-code provenance is exact, but required catalogue-derived lens products are not bound. Publication statements that the underlying DES Y1 catalogues are public cannot override this missing source/input realization.

## Candidate conclusion

The DES Y1 lineage is stronger than the failed Y3 realization in one important way: a real-data finite signed pseudo-`C_ell` Wm implementation genuinely exists in the pinned source. However, the exact real-data lens map/mask realization required by that implementation is not reproducibly bound from the audited public source.

Hence:

`DES_Y1_CANDIDATE_REJECTED_ON_O3_EXACT_PUBLIC_INPUT_BINDING`

This is **not** the global Exp073O classification. The frozen search must continue to the next public candidate before assigning `NO_PUBLIC_REALDATA...` or `FAIL_EXP073O...`.

No support fraction has been computed. Exp073N remains unchanged. G7/G8/G9 remain OPEN; covariance and all later G7 stages remain closed.
