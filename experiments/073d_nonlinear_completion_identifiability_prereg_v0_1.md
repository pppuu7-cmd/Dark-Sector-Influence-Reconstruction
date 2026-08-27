# Exp073D — nonlinear-completion identifiability audit — preregistration v0.1

**Date frozen:** 2026-08-27  
**Status:** PREREGISTERED BEFORE ANY Exp073D CLASSIFICATION

## Motivation

Exp073B established that the current pinned stack lacks a complete nonlinear three-block provider. Exp073C then found useful nonlinear matter ingredients but no complete public nonlinear `P_mm/P_Wm/P_WW` route for both C3 and C5.

Before designing a new provider, DSIR must answer a more fundamental theory question:

> Do the already-frozen C3/GDM and C5/designer-f(R) training-family definitions uniquely determine their nonlinear continuation, or would a nonlinear provider necessarily introduce additional physical assumptions not present in the current model definition?

If a training family is only a linear phenomenological closure, choosing one nonlinear continuation would silently change the scientific model class. Exp073D prevents that from happening implicitly.

## Frozen targets

### C3

Current C3 is the GDM imperfect-fluid family represented in the pinned GDM-CLASS implementation and certified DSIR linear provider. Audit whether its frozen background + linear perturbation closure (`w`, sound-speed and viscosity/shear functions as used by the current branch) uniquely specifies the nonlinear stress-energy evolution required to predict nonlinear density and metric/Weyl fields.

### C5

Current C5 is designer f(R) defined by the pinned EFTCAMB designer branch. Audit whether the underlying covariant gravitational action/field equations specify a nonlinear theory in principle, independently of whether the current numerical provider solves that nonlinear regime.

## Evidence hierarchy

Use primary model papers and exact pinned source semantics first, followed by peer-reviewed nonlinear-model papers. Distinguish:

- mathematical definition of a nonlinear theory;
- numerical implementation availability;
- calibrated prediction accuracy.

These are not interchangeable.

## Frozen tests

D1. C3 closure order: determine whether the GDM closure equations used by the frozen family are explicitly linear/perturbative or define the full nonlinear stress tensor.

D2. C3 uniqueness: search primary GDM literature for whether multiple inequivalent microphysical/EFT/fluid nonlinear completions can share the same linear GDM parameters.

D3. C3 provider consequence: determine whether nonlinear `P_mm/P_Wm/P_WW` can be inferred uniquely from the current C3 parameter vector without adding a new completion choice/parameterization.

D4. C5 theory completeness: determine whether designer f(R) corresponds to a covariant nonlinear action/field equation, even though EFTCAMB currently supplies a linear cosmological perturbation provider.

D5. C5 provider consequence: distinguish “nonlinear theory exists uniquely in principle” from “current certified nonlinear provider exists”.

D6. observation-block consequence: determine whether a proposed nonlinear DSIR provider would preserve the meaning of the existing training-family label or create a new enlarged family.

D7. exact provenance/source references recorded.

D8. no covariance, nuisance, G7 relation/null or G8 result used.

## Frozen classifications

If C3 is not uniquely defined beyond linear order while C5 is defined nonlinearly in principle, classify

`C3_NONLINEAR_COMPLETION_NONIDENTIFIABLE_C5_DEFINED_EXP073D`.

If both current training-family definitions uniquely specify nonlinear dynamics in principle, classify

`BOTH_NONLINEAR_COMPLETIONS_IDENTIFIABLE_EXP073D`.

If neither can be defensibly determined from primary evidence, classify

`INCOMPLETE_THEORY_EVIDENCE_EXP073D`.

## Downstream consequence

Under `C3_NONLINEAR_COMPLETION_NONIDENTIFIABLE_C5_DEFINED_EXP073D`, DSIR must not create a single “the C3 nonlinear provider” as though it followed uniquely from the frozen C3 vector. The next design step must instead choose prospectively between:

1. restricting the observational route to a perturbatively valid domain;
2. enlarging C3 into an explicitly defined nonlinear-completion ensemble, treating completion choice as part of the model class;
3. replacing C3 by one or more microphysical nonlinear dark-matter families whose nonlinear stress tensor is defined.

None of these choices may use G7/G8 performance for retrospective selection.

G7 OPEN. G8 OPEN. G9 OPEN.
