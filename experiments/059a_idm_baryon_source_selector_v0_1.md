# Experiment 059A — C9 IDM–baryon source-only selector v0.1

Date: 2026-08-26
Status: PREREGISTERED SOURCE-ONLY SELECTOR; no C9 perturbation or matter-power response may be generated in this experiment.

## Purpose

Exp058A preregistered a two-coordinate response-space law after the structural Exp056B/F29 failure on C8 IDM–photon. The next executable requirement is a genuinely fresh withheld family whose source-side control and solver provenance are frozen before any response is inspected.

C9 is fixed here as **interacting dark matter–baryon scattering** in official CLASS, controlled by the microscopic cross section `cross_idm_b`. A repository search before this preregistration found no prior DSIR experiment using `cross_idm_b`; DCDM is excluded because it already appeared as the C6 withheld family in Exp053A.

## Frozen source family

Pinned solver:

`lesgourg/class_public@e85808324f51fc694d12e3ed7439552a3c3f9540`

Frozen cosmology/source settings:

- `h = 0.67`
- `T_cmb = 2.7255`
- `omega_b = 0.0224`
- `omega_cdm = 0.0`
- `omega_idm = 0.1200`
- `m_idm = 1e9` eV
- `N_ur = 3.046`
- `Omega_k = 0`
- `YHe = 0.2404`
- `recombination = RECFAST`
- `reio_parametrization = reio_none`
- `n_index_idm_b = 0`

The microscopic/source coordinate is

` s = log10(cross_idm_b / cm^2) `.

The frozen ordered C9 grid is

`cross_idm_b = {1e-30, 1e-29, 1e-28, 1e-27, 1e-26} cm^2`.

This grid is geometric and source-defined. No response-derived amplitude tuning is permitted.

## Source-only validation contract

Exp059A may run CLASS only with a blank observable `output`, while requesting `write background = yes` and `write thermodynamics = yes`. It must:

1. verify that the pinned CLASS lineage exposes `cross_idm_b` and `n_index_idm_b`;
2. run all five frozen C9 source points successfully;
3. require background and thermodynamics records for every point;
4. reject the run if any matter-power, transfer, perturbation-source, or angular-spectrum output is created;
5. record the exact solver SHA, source settings, output manifest, and run logs.

No `P(k,z)`, transfer function, CMB spectrum, or perturbation source from C9 may be inspected before this selector is merged and the Exp058A response operator/tolerance implementation is frozen.

## Withheld-response boundary

C9 is reserved as the next withheld response family for Exp058A. After Exp059A is merged:

- the C9 source grid cannot be changed because of response behavior;
- the redshift grid, k-domain, reference cosmology, response mask, localization operator `ell`, shape coordinate `q`, segment-intersection tolerance, and leave-one-redshift rule must all be frozen before first C9 response generation;
- C8 cannot be reused as withheld evidence;
- any prospective failure must be retained as a negative scientific result.

## Gate state

This selector alone does not close any scientific gate. At preregistration:

- F27 remains HARD FAIL;
- F28 remains retrospective evidence only;
- F29 remains HARD PROSPECTIVE FAIL;
- G7 OPEN;
- G8 OPEN;
- G9 OPEN.

## Next step after a clean source-only run

Merge Exp059A, then implement and freeze Exp058A's exact `(ell,q)` response-coordinate construction and numerical intersection tolerance using training-only C3/C5/C7/C8 information. Only after that freeze may C9 response outputs be generated exactly once for the prospective test.