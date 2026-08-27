# Exp073D — nonlinear-completion identifiability audit result v0.1

**Date:** 2026-08-27  
**Scientific classification:** `C3_NONLINEAR_COMPLETION_NONIDENTIFIABLE_C5_DEFINED_EXP073D`

## Frozen question

Exp073D asked whether the already-frozen C3/GDM and C5/designer-f(R) training-family definitions uniquely determine their nonlinear continuation, independently of whether a numerical nonlinear provider currently exists.

This distinction matters because Exp073A showed that the released ACT×unWISE route requires nonlinear support, Exp073B showed that the pinned provider stack lacks the required nonlinear three-block layer, and Exp073C found no complete public replacement. A new provider is scientifically admissible only if it does not silently change the meaning of the training family.

## C3 / GDM result

The primary GDM literature is explicit that the phenomenological GDM construction used for cosmological inference is defined at the homogeneous-background and **linear perturbation** level and must be additionally extended to describe nonlinear structure.

Thomas, Kopp & Marković, *Using large-scale structure data and a halo model to constrain generalized dark matter*, MNRAS 490 (2019), arXiv:1905.02739, states that the GDM model used there is only defined perturbatively and introduces a halo-model extension precisely because a nonlinear prescription is otherwise absent.

Kopp, Skordis & Thomas, *An extensive investigation of the Generalised Dark Matter model*, Phys. Rev. D 94, 043512 (2016), arXiv:1605.00649, discusses several possible non-perturbative descriptions—effective-fluid, scalar-field, kinetic/thermodynamic and other microscopic realizations—rather than deriving one unique nonlinear stress tensor from the linear GDM parameters.

The current DSIR C3 implementation follows this same structure: its frozen parameter vector specifies background/linear fluid quantities such as `w`, effective sound speed and viscosity/shear functions, and the certified provider reconstructs linear `P_mm`, `P_Wm`, and `P_WW` from native linear matter and metric-transfer information. Nothing in that frozen vector specifies a unique nonlinear closure for the stress tensor, shell crossing, velocity dispersion, nonlinear anisotropic stress or nonlinear metric response.

The 2026 dedicated GDM simulation study by Sakr & López-Sánchez (arXiv:2601.16943) reinforces rather than removes this ambiguity: it chooses a particular nonlinear continuation by generating GDM-modified linear initial conditions and subsequently evolving collisionless N-body particles, while neglecting GDM thermal velocities and using standard lensing/Weyl assumptions for the studied setup. This is a legitimate phenomenological nonlinear construction, but it is an **additional modelling choice**, not a unique consequence of the frozen DSIR C3 parameter vector.

Therefore:

- D1 C3 closure order: **linear/perturbative**;
- D2 C3 nonlinear uniqueness: **not unique**;
- D3 unique nonlinear `P_mm/P_Wm/P_WW` inference from the frozen C3 vector: **not possible without additional completion assumptions**.

## C5 / designer-f(R) result

C5 is conceptually different. Hu–Sawicki/designer `f(R)` gravity is defined by a covariant action of the form

`S = ∫ d^4x sqrt(-g) [M^2/2 (R + f(R)) + L_m]`,

whose metric variation gives nonlinear field equations. The screening and nonlinear scalar/metric dynamics therefore belong to the theory itself; they are not an arbitrary phenomenological continuation added after specifying its linear perturbations.

Primary references include Hu & Sawicki, *Models of f(R) Cosmic Acceleration that Evade Solar-System Tests*, Phys. Rev. D 76, 064004 (2007), arXiv:0705.1158, together with later nonlinear f(R) simulation/emulator literature. The pinned EFTCAMB C5 provider used by DSIR is currently a **linear cosmological perturbation implementation**, but that numerical limitation does not make the underlying nonlinear theory ambiguous.

Thus:

- D4 C5 nonlinear theory definition: **defined in principle by the covariant theory**;
- D5 current certified nonlinear provider: **absent**, as established independently by Exp073B/C;
- this is a provider/calibration problem, not a model-identifiability problem.

## Training-family consequence

The asymmetry is scientifically important:

`C5 nonlinear extension = solve/calibrate the already-defined theory`

whereas

`C3 nonlinear extension = choose an additional nonlinear completion of a linear phenomenological family`.

Consequently there is no scientifically unique object that may be called **the nonlinear C3 provider** while retaining the exact frozen C3 model meaning. Selecting a halo prescription, collisionless N-body continuation, effective stress-tensor closure, EFT completion or microphysical realization creates an enlarged/refined model class.

That extra completion choice must be visible in DSIR's model space and cannot be hidden inside a numerical provider.

## Why this is not a failure of DSIR

The result identifies a genuine inverse-problem boundary. A model-agnostic dark-sector reconstruction based on linear effective response variables can remain well defined in the perturbative regime while becoming non-identifiable as a unique nonlinear theory. Real survey kernels can then demand scales on which the phenomenological parameterization itself no longer uniquely predicts the observables.

This means the current G7 obstruction is partly **ontological/model-definition**, not merely computational:

1. Exp072C shows the observational operator demands a very low-z/high-k support region;
2. Exp073A shows that region is not perturbatively linear;
3. Exp073B/C show there is no ready complete nonlinear provider;
4. Exp073D shows that for C3, even constructing one provider requires choosing extra physics not fixed by the current C3 definition.

## Frozen classification

The evidence therefore satisfies the preregistered classification

`C3_NONLINEAR_COMPLETION_NONIDENTIFIABLE_C5_DEFINED_EXP073D`.

No previous experimental classification is changed.

## Downstream rule

A single post-hoc nonlinear C3 closure is forbidden. The next admissible design step must prospectively define how DSIR treats this completion freedom. The scientifically distinct options are:

1. retain C3 strictly as a perturbative family and abandon the current ACT×unWISE realization for it;
2. enlarge C3 into an explicitly labelled nonlinear-completion ensemble, with completion identity treated as part of the model class;
3. replace/augment C3 with microphysical dark-matter families whose nonlinear stress-energy evolution is specified.

Exp073A already establishes that option 1 cannot recover the currently frozen ACT×unWISE route under the 5% support criterion, so further work should focus on whether options 2 or 3 can preserve DSIR's model-agnostic inference semantics without retrospective selection.

No covariance restriction, whitening, nuisance SVD/rank, G7 relation/null or G8 selection is authorized.

G7 OPEN. G8 OPEN. G9 OPEN.
