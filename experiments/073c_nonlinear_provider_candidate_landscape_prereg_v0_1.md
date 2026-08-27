# Exp073C — nonlinear independent matter/Weyl provider candidate landscape — preregistration v0.1

**Date frozen:** 2026-08-27  
**Status:** PREREGISTERED BEFORE ANY Exp073C CANDIDATE RANKING OR SELECTION

## Motivation

Exp073B completed as

`GAP_EXISTING_STACK_NONLINEAR_MATTER_WEYL_ROUTE_EXP073B`.

The existing DSIR/ACT projection architecture can consume independent nonlinear `P_mm`, signed `P_Wm`, and `P_WW`, but the pinned C3/GDM and C5/designer-f(R) providers do not supply a complete physically justified nonlinear three-block layer over the Exp072C low-z/high-k planning region.

Exp073C is therefore a prospective literature/software landscape search for candidate nonlinear ingredients. It is not provider certification and cannot authorize covariance or G7 fitting.

## Search target

Identify public, citable theory codes, emulators, response frameworks, simulations/calibrations, or published prescriptions that could plausibly provide or calibrate nonlinear predictions for the DSIR blocks

- `P_mm(k,z)`;
- signed `P_Wm(k,z)`;
- `P_WW(k,z)`;

for at least one of:

- GDM/effective dark-matter pressure/shear-like models relevant to C3;
- designer/Hu-Sawicki-like `f(R)` or sufficiently close modified-gravity families relevant to C5.

The planning support target is the Exp072C frontier through approximately `z_min=0.0087346` and `k_max=4.8182611 Mpc^-1`.

## Frozen evidence hierarchy

Candidate claims must be supported in descending preference by:

1. primary code/repository source and exact API/output semantics;
2. peer-reviewed primary paper or official technical documentation;
3. published validation/comparison paper;
4. secondary summaries only as discovery aids, never as sole certification evidence.

Record publication/version/date and distinguish current maintenance from historical availability.

## Candidate capability classes

For every candidate classify each required block separately:

- `NATIVE`: directly predicted/calibrated nonlinear block;
- `DERIVABLE_WITH_MODEL_SPECIFIC_JUSTIFICATION`: derivation explicitly supported by the candidate's physical formalism for that model family;
- `MATTER_ONLY`: nonlinear `P_mm` only;
- `GR_CLOSURE_ONLY`: Weyl inferred through a GR closure not valid as an independent MG/dark-sector provider;
- `UNSUPPORTED`;
- `UNCLEAR`.

No `MATTER_ONLY`, `GR_CLOSURE_ONLY`, or `UNCLEAR` candidate can be promoted to a complete DSIR route.

## Hard evaluation dimensions

For each candidate record prospectively:

C1. model-family overlap with C3 and/or C5;

C2. nonlinear `P_mm` capability;

C3. nonlinear signed `P_Wm` capability;

C4. nonlinear `P_WW` capability;

C5. whether Weyl/slip is independent/model-specific rather than a GR matter closure;

C6. native/calibrated `(z,k)` support relative to the Exp072C frontier;

C7. physical units, gauge/field definitions and cross-power sign convention;

C8. public reproducibility: code/data/weights/API availability and versionability;

C9. GR/zero-limit or baseline validation relevant to eventual provider certification;

C10. known accuracy domain and stated failure/extrapolation boundaries.

## Forbidden selection shortcuts

Do not rank a candidate using ACT covariance, nuisance rank, G7 relation residual, held-out/G8 performance, or article-selection performance.

Do not prefer a candidate merely because it returns numbers to `k~5 Mpc^-1` if those numbers are outside its calibrated/validated model domain.

Do not treat generic GR HALOFIT/HMcode, CLEFT matter bias terms, or a nonlinear matter boost applied to linear Weyl as a complete nonlinear MG/dark-sector provider unless a primary source explicitly validates the required model-specific Weyl auto/cross construction.

## Frozen outcomes

If at least one publicly reproducible candidate or composable candidate set has explicit model-specific support for all three nonlinear blocks for **both** required training families, with plausible support toward the Exp072C frontier, classify

`CANDIDATE_ROUTE_FOUND_EXP073C`.

If candidates exist but no public/reproducible route covers all three blocks for both C3 and C5, classify

`NO_COMPLETE_PUBLIC_CANDIDATE_ROUTE_EXP073C`.

If the search/evidence provenance is incomplete enough that a landscape conclusion cannot be defended, classify

`INCOMPLETE_EVIDENCE_EXP073C`.

Exp073C is a landscape result only. `CANDIDATE_ROUTE_FOUND` does not certify a provider; the next step must freeze a specific provider-certification contract before numerical use.

## Downstream boundary

No covariance restriction, whitening, nuisance SVD/rank, G7 relation/null or fresh G8 family is authorized by Exp073C.

G7 OPEN. G8 OPEN. G9 OPEN.
