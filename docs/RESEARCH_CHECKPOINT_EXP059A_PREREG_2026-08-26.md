# Research checkpoint — Exp059A C9 source-selector preregistration

Date: 2026-08-26

## Starting state

`main` at `e3b4c6e01d8b98eb4b187ee77de12fcd9c5f0069`.

Exp058A is preregistered. F29 remains a HARD PROSPECTIVE FAIL from C8 IDM-photon, with Exp057A establishing that the failure is structural rather than a scalar-coordinate artifact.

## Action taken

A genuinely fresh C9 family is frozen as official-CLASS IDM-baryon scattering using `cross_idm_b` with `n_index_idm_b=0`. The ordered microscopic grid is `{1e-30,1e-29,1e-28,1e-27,1e-26} cm^2`, with fixed cosmology and solver lineage.

The accompanying workflow is source-only: it builds pinned CLASS, runs the five C9 settings with no observable `output`, requires background and thermodynamics products, and hard-fails if any matter-power, transfer, perturbation-source, or angular-spectrum file is generated.

## Why C9 is fresh

The DSIR repository contained no prior use of `cross_idm_b` before this branch. DCDM is not reused because Exp053A already used it as the C6 withheld family. C3 GDM, C5 designer f(R), C7 IDM-DR, and C8 IDM-photon are already contaminated by construction/validation history and cannot serve as the new Exp058A withheld family.

## Anti-retuning boundary

- C9 source grid is fixed before response generation.
- No response-derived amplitude selection is allowed.
- C9 cannot generate `P(k,z)` until the exact Exp058A `(ell,q)` operators, mask, redshift grid, k-domain, intersection tolerance, and leave-one-redshift implementation are frozen.
- Any future prospective failure is retained as a scientific negative result.

## Gate state

- F27 HARD FAIL.
- F28 retrospective evidence only.
- F29 HARD PROSPECTIVE FAIL.
- G7 OPEN.
- G8 OPEN.
- G9 OPEN.

## Next executable step

Run and merge Exp059A if the contamination guard passes. Then implement/freeze the exact Exp058A response-coordinate construction from training-only information before any C9 response is generated.