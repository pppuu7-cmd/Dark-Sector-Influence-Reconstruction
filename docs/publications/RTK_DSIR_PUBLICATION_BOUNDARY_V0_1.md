# RTK ↔ DSIR publication boundary v0.1

**Date:** 2026-08-27  
**Status:** architecture / provenance contract

## Core rule

RTK and DSIR remain **independent research programs with independent repositories, evidence chains, gates and failure histories**.

The DSIR repository must not absorb RTK source code, RTK experimental outputs or RTK gate status merely to make a combined narrative look stronger. Likewise, DSIR results do not validate RTK.

This boundary implements the prior RTK-vs-DSIR planning principle: compare the programs where scientifically useful, but do not mix their evidentiary chains before each is independently mature.

## No hidden common dark-sector statistic

The RTK↔DSIR comparison architecture has an additional hard rule: there is **no hidden shared dark-sector statistic** that may be passed between the projects and treated as common evidence.

In particular, `mu` is **not** a common RTK/DSIR table, latent coordinate or externally supplied universal observable.

For DSIR:

- any `mu`-like quantity used by a DSIR analysis must be computed **inside DSIR** from admissible DSIR observables/background quantities through the explicitly frozen DSIR basis and window/operator chain;
- an external physical provider may pass only the physical inputs explicitly allowed by the DSIR provider contract;
- an external provider must not pass a ready-made `mu` whose value already depends on an RTK-specific statistic, calibration, fit or latent coordinate and have it treated as native DSIR evidence;
- if a candidate external provider is already RTK-dependent, it must either be rejected from the native DSIR evidence chain or used only as an explicitly labelled external stress-test with `external_to_dsir=true`;
- a numerical coincidence between an RTK statistic and a DSIR-derived `mu` does not establish that they are the same physical object.

This rule prevents a future comparative manuscript from silently creating cross-project confirmation by defining the same intermediate statistic on both sides after the fact.

## What DSIR may store about RTK

For future article planning DSIR may store only a thin external cross-reference record containing, when needed:

- external project name: `RTK`;
- external repository URL;
- immutable RTK commit/tag/DOI;
- external claim/result identifier;
- one-sentence comparison purpose;
- explicit marker `external_to_dsir=true`;
- whether the external result is independent, analogous, complementary or conflicting.

No copied RTK numerical table becomes DSIR evidence merely by being present in a manuscript note.

## Allowed comparative questions

A future RTK↔DSIR synthesis paper may compare:

1. problem architecture and inverse-problem structure;
2. use of low-dimensional effective descriptions versus microscopic degrees of freedom;
3. degeneracy, identifiability and withheld-test methodology;
4. the difference between theory-space constraints and observation-space constraints;
5. shared methodological lessons about preregistration, negative results, numerical solver floors and causal validation;
6. whether any independently derived mathematical structures are genuinely analogous after units, variables and physical meaning are made explicit.

The comparison itself must not manufacture a physical equivalence.

## Prohibited shortcuts

The following are prohibited:

- using a PASS in RTK as evidence for a DSIR gate;
- using a DSIR PASS as evidence for an RTK gate;
- copying a fitted coefficient from one project into the other without a new independent test;
- supplying an RTK-derived `mu` or equivalent hidden latent statistic to a native DSIR provider;
- describing visually similar formulas as the same physics without a derivation;
- combining significance values from the two projects as though they were one experiment;
- hiding project-specific negative results in a joint manuscript;
- moving unresolved DSIR dark-sector claims into an RTK paper to avoid G7/G8/G9;
- moving unresolved RTK claims into DSIR for the same reason.

## Publication-series interface

The manuscript architecture therefore has two layers:

### Independent layer

- RTK papers are supported by RTK evidence and stored/managed in RTK.
- DSIR papers are supported by DSIR evidence and stored/managed in DSIR.

### Comparative layer

Only after at least one independently supportable paper exists from each program should a dedicated RTK↔DSIR comparison/synthesis manuscript become eligible. That paper should import **citations and immutable references**, not silently merge repositories or gate states.

Any cross-project variable comparison must first include a definition-level mapping that states units, operators, physical meaning and derivation on each side. Similar notation alone is not a mapping.

## DSIR repository implementation

Future external comparison metadata should live under

`docs/publications/external_crosswalk/`

with one small manifest per external result or manuscript. If a full numerical reproduction of an RTK result is scientifically required inside DSIR, it must become a newly numbered DSIR experiment with its own provenance and must be described as an independent reproduction, not copied evidence.

A future `external_crosswalk` manifest involving `mu` must additionally record whether each side's quantity is independently derived and must never contain a field that replaces the DSIR-native provider output with an RTK-generated value.

## Current boundary status

As of 2026-08-27:

- DSIR remains scientifically independent of RTK;
- DSIR has no authorized hidden/common RTK↔DSIR dark-sector statistic;
- DSIR-native `mu`, if used, must be derived only inside the DSIR operator chain;
- the first DSIR manuscript may proceed on DSIR-only evidence;
- a combined RTK↔DSIR physics paper is **not** authorized merely by this architecture document;
- the later comparative paper remains dependent on independently mature RTK and DSIR publication records.
