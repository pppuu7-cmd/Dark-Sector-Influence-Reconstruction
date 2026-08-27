# Exp073E — C3 nonlinear-completion model-class boundary result v0.1

**Date:** 2026-08-27  
**Scientific/model-class classification:** `C3_COMPLETION_ENSEMBLE_NOT_FEASIBLE_EXP073E`

## Frozen question

Exp073E asked whether the frozen C3 linear GDM family could be carried into the nonlinear regime by attaching at least two physically distinct, explicitly labelled nonlinear completions while preserving the exact previously certified C3 linear semantics and keeping completion uncertainty separate from dark-sector influence uncertainty.

The answer under the preregistered E1–E8 requirements is **no** for the currently defensible completion landscape.

## Evidence by completion class

### A. Collisionless-initial-condition continuation

The 2026 dedicated GDM simulation route of Sakr & López-Sánchez (arXiv:2601.16943) is a useful nonlinear matter construction but is not a completion of the full frozen C3 family. It initializes simulations with GDM-modified linear matter spectra and then evolves collisionless N-body particles; the study explicitly neglects GDM thermal velocities and does not implement the viscosity degree of freedom because its nonlinear implementation is unavailable.

This fails the strict Exp073E linear-family preservation boundary for the full frozen C3 parameterization: the nonlinear evolution no longer carries the same general pressure/shear closure represented by the certified C3 vector. It also does not provide an independent nonlinear signed `P_Wm/P_WW` provider.

Result: E1 **not established for full C3**, E3/E6 **not satisfied**.

### B. Halo/spherical-collapse GDM continuation

Thomas, Kopp & Marković, MNRAS 490 (2019), explicitly develops a halo-model extension because GDM had only been defined perturbatively. The nonlinear halo prescription is therefore an additional phenomenological construction rather than a unique continuation of the frozen closure.

Pace, Sakr & Tutusaus, Phys. Rev. D 102, 043512 (2020), develops spherical collapse for a reduced GDM setup with background pressure and sound speed, while the viscosity sector of the general GDM model is not part of that nonlinear treatment. The paper also uses phenomenologically motivated nonlinear matter-power modelling rather than a full independent metric/Weyl three-block provider.

Result: physically distinct from class A, but E1 **not established for the full frozen C3 family**, and E3/E6 **not satisfied**.

### C. Effective nonlinear stress-tensor / EFT completion

Kopp, Skordis & Thomas, Phys. Rev. D 94, 043512 (2016), discusses EFT-of-fluids, EFT-of-large-scale-structure, nonequilibrium-thermodynamic and other nonperturbative descriptions as possible ways to extend or relate to GDM. This establishes that such completions are conceptually possible, but it does not define a unique finite nonlinear extension of the frozen arbitrary GDM `w/c_s^2/c_vis^2` closure with an exact one-to-one mapping that recovers the whole DSIR C3 family.

An EFT completion introduces additional nonlinear operators/coefficient functions whose values are not fixed by the frozen linear vector. Therefore it can become a new enlarged family, but it does not currently satisfy E1/E2 as an explicit finite completion of the same model class, nor E6 as a provider-ready independent `P_mm/P_Wm/P_WW` route.

### D. Microphysical embedding

Primary GDM literature shows that several microphysical/nonperturbative systems can reproduce subsets of GDM-like linear behavior—scalar fields, tightly coupled fluids and related constructions. But this many-to-one relation is precisely the nonlinear non-identifiability found in Exp073D. No finite public set was found with an exact mapping covering the entire frozen C3 time-binned pressure/shear family while preserving the same linear outputs and then uniquely supplying nonlinear metric/Weyl dynamics.

Selecting such embeddings would **replace/refine** the phenomenological C3 training class rather than simply add a provider underneath it.

## Frozen E1–E8 decision

- E1 linear-limit preservation for the **full frozen C3 family**: **FAIL / not established** for the available explicit nonlinear constructions;
- E2 explicit completion identity: achievable in principle, but insufficient without E1;
- E3 no hidden GR Weyl closure: **FAIL / incomplete** for the available executable matter-focused constructions;
- E4 at least two physically distinct nonlinear assumptions: **yes descriptively**, but they are not two admissible completions satisfying all other tests;
- E5 prospective weighting: can be imposed, but does not repair missing compatibility;
- E6 provider-certifiability for independent nonlinear `P_mm`, signed `P_Wm`, `P_WW`: **FAIL** for the current candidates;
- E7 separation of completion uncertainty from influence uncertainty: conceptually possible only after a valid explicit completion set exists;
- E8 no downstream leakage: **PASS**.

Therefore the preregistered FEASIBLE condition is not met. The existing choices either omit parts of the frozen C3 physics or introduce additional nonlinear theory content that changes/refines the model class.

## Scientific interpretation

The sequence Exp073A–E establishes a hard boundary for the current ACT×unWISE realization:

1. the released observation operator requires a low-z/high-k domain;
2. that domain is not perturbatively linear;
3. no ready independent nonlinear three-block provider exists;
4. the C3 phenomenological family does not uniquely determine nonlinear dynamics;
5. and the presently available nonlinear GDM constructions cannot be assembled into a finite completion ensemble that preserves the full frozen C3 family under the preregistered rules.

Therefore forcing the current C3 family through the ACT×unWISE nonlinear regime would change the scientific model being tested.

The correct next strategy is not to pick one nonlinear closure retrospectively. It is to seek an observational realization whose support remains within the already-certified perturbative C3/C5 domain, or to explicitly start a new research branch with microphysical nonlinear training families.

## Downstream state

The present ACT×unWISE G7 route remains blocked before covariance restriction. No whitening, nuisance SVD/rank, G7 relation/null or G8 selection is authorized.

G7 OPEN. G8 OPEN. G9 OPEN.

## Primary evidence

- Kopp, Skordis & Thomas, Phys. Rev. D 94, 043512 (2016), DOI `10.1103/PhysRevD.94.043512`, arXiv:1605.00649.
- Thomas, Kopp & Marković, MNRAS 490, 813–831 (2019), DOI `10.1093/mnras/stz2559`, arXiv:1905.02739.
- Pace, Sakr & Tutusaus, Phys. Rev. D 102, 043512 (2020), DOI `10.1103/PhysRevD.102.043512`.
- Sakr & López-Sánchez, *Forecast on the generalised dark matter properties from a Euclid-like survey*, arXiv:2601.16943 (2026).
