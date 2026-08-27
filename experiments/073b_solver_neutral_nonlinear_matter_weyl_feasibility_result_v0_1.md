# Exp073B — solver-neutral nonlinear matter/Weyl feasibility result v0.1

**Date:** 2026-08-27  
**Scientific/software-capability classification:** `GAP_EXISTING_STACK_NONLINEAR_MATTER_WEYL_ROUTE_EXP073B`

## Immutable provenance

Completed source-capability run:

- workflow run `33033279245`;
- workflow job `98390378310`;
- artifact `9631041961`;
- artifact digest `sha256:743ef140774eaeef164c506590a14ef999f2cb98e2bf5fd79e42bda9e69f96a5`;
- extracted JSON SHA256 `20e1378a2959679fe02116f6bdf7206a96fbac36b57c603ec2730357766f83ec`;
- execution head `ba64a1511dd36ad7f85f8ae325099f6d365fa2d2`.

The earlier run `33033220464` is infrastructure-only: it attempted to clone vanilla `lesgourg/class_public`, where the pinned GDM commit does not exist, so the Exp073B audit never executed. The workflow was corrected to the historically certified `s-ilic/gdm_class_public` source without changing any frozen scientific criterion.

Exact source pins were then reproduced:

- C3/GDM: `s-ilic/gdm_class_public@4c87916aab5ca124a68f1dd16f31846fc13d1829`;
- C5/designer-f(R): `EFTCAMB/EFTCAMB@16d9c4e9f85751e30efd0a53b177941713078904`;
- ACT×unWISE: `ACTCollaboration/unWISExLens_lklh@6302c30d9e70f8e4ff2d4a84a9977b4471705179`.

The audit is trustworthy.

## Frozen tests

- F1 projector separability: **PASS**;
- F2 upstream nonlinear/CLEFT scope: **PASS**;
- F3 C3/GDM complete nonlinear three-block provider: **FAIL / capability absent**;
- F4 C5/designer-f(R) complete nonlinear three-block provider: **FAIL / capability absent**;
- F5 support plausibility of a complete existing nonlinear candidate: **FAIL**;
- F6 independent/signed nonlinear semantics of a complete candidate: **FAIL because no complete candidate exists**;
- F7 provenance completeness: **PASS**;
- F8 no downstream leakage: **PASS**.

## What exists

The DSIR solver-neutral projector already accepts three independent physical block functions:

`P_mm`, signed `P_Wm`, and `P_WW`.

The pinned ACT×unWISE free-CLEFT module likewise accepts separate nonlinear `pk_weyl_weyl`, `pk_weyl_dnonu`, and `pk_dnonu_dnonu` inputs. Therefore the observational projection architecture itself is not the missing component.

However, the same upstream CLEFT implementation constructs its higher-order Weyl-matter correction using an explicit `matter2weyl_factor * cleft_interpolations_dtot_dnonu`. That is useful for the released GR-oriented likelihood model but is not evidence of an independent nonlinear Weyl provider for modified gravity/dark-sector models under the frozen DSIR rules.

## Missing provider physics

The currently certified C3/GDM provider is explicitly a **linear** construction based on native `pk_lin`, `D_m`, `phi`, and `psi`. Generic nonlinear matter modules in the source tree do not supply a separately justified nonlinear signed `P_Wm` and nonlinear `P_WW` for GDM.

The currently certified C5 q=3 provider is also explicitly **linear**: it uses `nonlinear=False` and `NonLinear_none` while requesting the independent linear variable pairs `(delta_nonu,delta_nonu)`, `(Weyl,delta_nonu)`, and `(Weyl,Weyl)`. Generic CAMB nonlinear corrections cannot be promoted to a designer-f(R) independent nonlinear Weyl provider without model-specific justification.

Thus the existing pinned stack has the correct three-block interface but lacks the physical nonlinear provider layer required after Exp073A.

## Consequence

The current G7 obstruction is now localized:

`observational projector architecture = sufficient`

but

`nonlinear dark-sector/MG physical provider layer = missing`.

A new or externally calibrated nonlinear ingredient is required. Forbidden shortcuts remain forbidden: no GR matter-to-Weyl closure, no assumed nonlinear rank-one coherence, no generic GR HALOFIT/HMcode relabeled as MG Weyl physics, and no fit-driven closure choice.

This result does not alter Exp072A/B/C or Exp073A. No covariance restriction, whitening, nuisance SVD/rank, G7 relation/null or G8 selection is authorized.

G7/G8/G9 remain OPEN.
