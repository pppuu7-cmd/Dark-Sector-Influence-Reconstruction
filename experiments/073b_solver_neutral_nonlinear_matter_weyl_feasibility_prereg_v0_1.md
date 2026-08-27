# Exp073B — solver-neutral nonlinear matter/Weyl feasibility audit — preregistration v0.1

**Date frozen:** 2026-08-27  
**Status:** PREREGISTERED BEFORE ANY Exp073B FEASIBILITY OUTPUT IS EVALUATED

## 1. Motivation

Exp073A completed as

`INELIGIBLE_GR_REFERENCE_LINEAR_ROUTE_EXP073A`.

All P1–P8 controls passed, while the primary `Delta2_m<=1` mask and even the relaxed `Delta2_m<=2` diagnostic retain `0/26` complete ACT×unWISE observation coordinates inside the unique Exp072C frontier.

Therefore the current linear/no-CLEFT observational route is scientifically blocked. Blindly extending the current linear C3/C5 providers to the Exp072C low-z/high-k frontier is not authorized.

The next question is architectural rather than inferential:

> Does the currently pinned DSIR software/provider stack contain a physically defensible, solver-neutral path to independent nonlinear `P_mm`, `P_Wm`, and `P_WW` over the observationally required low-z/high-k region, without imposing a GR matter-to-Weyl closure on modified-gravity/dark-sector models?

Exp073B is a source/provenance/physics-capability feasibility audit only. It does not create a nonlinear provider, does not run covariance or G7 relation fitting, and cannot by itself reopen the ACT×unWISE route.

## 2. Immutable parent binding

Bind exactly:

- Exp073A classification `INELIGIBLE_GR_REFERENCE_LINEAR_ROUTE_EXP073A`;
- run `33032781761`;
- job `98388840817`;
- artifact `9630897385`;
- artifact digest `sha256:0f2212d691c38c3e953d2a0d823b498a5557b9485fc759079719000cdc48cb25`;
- extracted result JSON SHA256 `a8bbafa971283cadf9ff27a27af4d0c4e3042bc0aec590d690142d39c919abb2`;
- all P1–P8 controls PASS;
- primary, conservative and relaxed retained dimensions all equal `0`.

Preserve Exp072A/B/C and Exp073A classifications under every Exp073B outcome.

## 3. Frozen software/provenance targets

Audit only pinned, already-used sources unless a source is explicitly introduced as a candidate and recorded without promoting it to certification:

- ACT×unWISE likelihood/theory source `ACTCollaboration/unWISExLens_lklh@6302c30d9e70f8e4ff2d4a84a9977b4471705179`;
- C3/GDM provider source `lesgourg/class_public@4c87916aab5ca124a68f1dd16f31846fc13d1829`;
- C5/designer-f(R) provider source `EFTCAMB/EFTCAMB@16d9c4e9f85751e30efd0a53b177941713078904`;
- CAMB baseline/projection dependency `cmbant/CAMB@fa3f097343fbbe427cc04b4f5f0041c22c6ec764`.

No source version may be changed after the first Exp073B audit output to manufacture capability.

## 4. Required nonlinear information channels

The target nonlinear interface remains solver-neutral and block-explicit:

- `P_mm(k,z)` matter auto power;
- signed `P_Wm(k,z)` Weyl-matter cross power;
- `P_WW(k,z)` Weyl auto power.

The audit must distinguish three logically different capabilities:

1. projector/interface capability to consume externally supplied independent nonlinear blocks;
2. C3/GDM capability to produce physically justified nonlinear versions of all required blocks;
3. C5/designer-f(R) capability to produce physically justified nonlinear versions of all required blocks.

A route is not feasible merely because the projector can accept arbitrary functions.

## 5. Forbidden shortcuts

The following do not count as a feasible nonlinear DSIR provider:

- replacing `P_Wm` or `P_WW` by a GR Poisson/slip closure derived only from nonlinear `P_mm`;
- assuming rank-one coherence `P_Wm^2=P_WW P_mm` as a nonlinear physical law without provider-specific justification;
- applying standard GR HALOFIT/HMcode/nonlinear matter corrections to MG/GDM Weyl channels without model-specific support;
- multiplying linear Weyl ratios by an unrelated nonlinear matter boost and treating the result as certified physics;
- using an upstream CLEFT/matter-only bias model as evidence that independent nonlinear Weyl auto/cross power exists;
- extrapolating a provider beyond its documented/native nonlinear support;
- using covariance, fitted relations, held-out performance or G8 information to choose a nonlinear closure.

## 6. Frozen capability tests

### F1 — ACT×unWISE projector separability

At source level, determine whether the validated DSIR linear/no-CLEFT projection architecture can accept three independent callable/tabulated blocks `P_mm`, signed `P_Wm`, `P_WW` without an internal compulsory GR closure.

PASS if independent block injection is structurally supported or can be isolated through the already validated solver-neutral DSIR projector without changing observational operator semantics.

### F2 — upstream nonlinear/CLEFT scope

Audit the pinned ACT×unWISE theory modules and document exactly which nonlinear/CLEFT ingredients are generated and whether Weyl auto/cross power remains independently supplied or is derived from matter/GR closure.

This is descriptive; presence of CLEFT does not by itself pass F3/F4.

### F3 — C3/GDM nonlinear provider capability

Search the pinned C3 source and current certified C3 bridge for a native or source-supported nonlinear prediction path that simultaneously provides physically justified `P_mm`, signed `P_Wm`, and `P_WW` for GDM on the required low-z/high-k region.

PASS only if all three blocks have an identifiable nonlinear physical source with explicit model semantics and no forbidden shortcut.

### F4 — C5/designer-f(R) nonlinear provider capability

Search the pinned C5 source and current certified C5 bridge for a native or source-supported nonlinear prediction path that simultaneously provides physically justified `P_mm`, signed `P_Wm`, and `P_WW` for designer-f(R) on the required low-z/high-k region.

PASS only if all three blocks have an identifiable nonlinear physical source with explicit model semantics and no forbidden shortcut.

### F5 — support plausibility

For any claimed nonlinear provider capability, verify that its documented/native support plausibly reaches the Exp072C planning rectangle at least to

- `z_min=0.0087345857837422`;
- `k_max=4.818261097432861 Mpc^-1`.

A source that provides nonlinear blocks only on a much smaller domain is recorded as partial capability, not a complete feasible route.

### F6 — independence/sign semantics

Any candidate route must preserve signed `P_Wm` and permit `P_WW`, `P_Wm`, `P_mm` to vary independently subject to physical PSD/coherence constraints; absolute-value replacement of the cross spectrum is forbidden.

### F7 — provenance completeness

Every capability claim must cite exact pinned source path/function/API or existing immutable DSIR provider record. Documentation-only claims must be labeled as such and cannot override source behavior.

### F8 — no downstream leakage

No covariance, whitening, nuisance SVD/rank, G7 relation/null, G8 response, article selection or held-out result may be read or used.

## 7. Frozen classifications

If F1–F8 all pass, including complete C3 and C5 nonlinear provider capability and support plausibility, classify

`FEASIBLE_EXISTING_STACK_NONLINEAR_MATTER_WEYL_ROUTE_EXP073B`.

If F1, F2, F5–F8 are evaluable but either C3 or C5 lacks a complete physically justified independent nonlinear matter/Weyl provider, classify

`GAP_EXISTING_STACK_NONLINEAR_MATTER_WEYL_ROUTE_EXP073B`.

This GAP is a scientific/software-capability result: it means a new nonlinear provider or external calibrated theory ingredient is required before G7 can proceed.

If provenance/source reproduction fails such that the capability audit itself is not trustworthy, classify

`FAIL_EXP073B_REPRODUCTION_OR_PROVENANCE`.

Infrastructure interruption before complete evaluation is `INCOMPLETE_EXP073B` and is not a scientific result.

## 8. Downstream rule

A `GAP` result authorizes only a prospectively frozen design/search phase for missing nonlinear provider ingredients. It does not authorize inventing a closure, weakening Exp073A, or moving to covariance/nuisance/G7 fitting.

A `FEASIBLE` result still does not certify a nonlinear provider numerically. The next step would be a separate provider-certification experiment with native support, GR/zero limits where applicable, signed cross-power controls, PSD/coherence, repeatability and no-extrapolation tests.

G7 OPEN.  
G8 OPEN.  
G9 OPEN.
