# DSIR publication architecture — frozen 2026-09-06

Status: **PROJECT-LEVEL ARCHITECTURE DECISION**.  
Scope: **DSIR only**. Do not mix RTK or RQIR.

## Purpose

Freeze the publication sequence so that the observational reconstruction, comparison of existing models, and construction of any future DSIR-derived model remain scientifically separable and non-circular.

The central rule is:

> The existing-model funnel must be evaluated before a new DSIR-derived model is claimed to be needed, and the future model must not be designed and validated on exactly the same information.

## Frozen article sequence

### DSIR-1 — Framework

**Question:** What is a model-agnostic reconstruction of dark-sector influence?

**Core deliverable:** the DSIR formalism and the common residual/source representation, including the model-independent interface through which dark matter, dark energy, interacting-dark-sector and modified-gravity hypotheses can later be compared.

**Role in sequence:** defines the language. It does not claim that any particular cosmological model passes or fails the complete DSIR funnel.

---

### DSIR-2 — Inverse reconstruction / mathematical machinery

**Question:** Can observable influence be reconstructed without selecting a specific dark-sector model in advance?

**Core deliverable:** inverse reconstruction machinery, operators, validity/domain gates, representation rules and the mathematical infrastructure needed for a model-agnostic reconstruction.

**Role in sequence:** defines the reconstruction machinery and its admissible domain. It does not yet constitute the complete observational model-comparison funnel.

---

### DSIR-3 — Observational implementation and complete funnel

**Question:** Can the DSIR reconstruction be implemented on the real observational data chain with auditable provenance and controlled nuisance/covariance structure?

**Core deliverable:** the complete observational funnel, including the currently developing DES angular layer and, once prerequisites are satisfied, the ordered angular join, radial multiplication, physical-support scoring, covariance/whitening, nuisance quotient, relation/null structure and final observational gates.

**Current boundary:** the 14-task angular production inventory is still being completed. The ordered 14-window join, radial multiplication, physical-support scoring, covariance/whitening, nuisance quotient/relation/null and G8 remain forbidden until their prerequisites are satisfied.

**Role in sequence:** establishes the observational instrument that later papers may use. It must not be retrofitted to favor a specific model.

---

### DSIR-4 — Existing-Model Funnel Matrix

**Question:** Which existing model classes survive the same prospectively frozen DSIR funnel?

**Core deliverable:** a systematic model-by-model matrix using statuses such as:

- `PASS`
- `FAIL`
- `OUTSIDE_DOMAIN`
- `NOT_YET_TESTABLE`
- `NUMERICALLY_UNRESOLVED` where a prospectively frozen ambiguity rule requires it

The initial representative model inventory should include, at minimum, appropriate realizations of:

- LambdaCDM / GR baseline;
- wCDM;
- w0wa dark energy;
- quintessence-like models;
- interacting dark-energy / interacting dark-sector models;
- f(R)-type modified gravity;
- DGP-like models where a clean DSIR mapping is possible;
- Horndeski / EFT-like representative classes;
- additional representative dark-matter/dark-sector models when their observable mapping is sufficiently well defined.

This list is an inventory target, not a claim that these models have already been fully tested.

**Critical scientific rule:** DSIR-4 must be completed as an existing-model comparison problem. It must not use the future DSIR-derived model as a target while thresholds, scoring rules or funnel semantics are being chosen.

**Interpretation of possible outcomes:**

1. If LambdaCDM alone survives, DSIR has independently collapsed the reconstruction onto a LambdaCDM-compatible equivalence class and a new model is not justified merely for novelty.
2. If multiple existing models survive, the surviving equivalence class becomes the target for additional discriminating observables/gates.
3. If no existing representative model survives all required gates, DSIR identifies an empirically constrained gap in model space. Only then is construction of a genuinely new model strongly motivated.

---

### DSIR-5 — DSIR-derived new dark-sector model

**Question:** If the existing-model funnel leaves an unexplained residual structure, what is the minimal viable dynamics that reproduces the required influence while avoiding already-excluded signatures?

**Core deliverable:** a new model derived from constraints produced by DSIR rather than chosen first and fitted afterward.

The construction direction is frozen conceptually as:

`data -> DSIR residual/influence structure -> required properties -> exclusion of existing classes -> minimal viable dynamics -> equations/action -> predictions`.

This paper is conditional: it should be written as a new-model paper only if DSIR-4 provides a scientific reason that an existing model/equivalence class is insufficient.

### Constraint-skeleton rule

Before fixing a concrete Lagrangian/action, maintain a model constraint skeleton `C1...Cn`. Each constraint must record its provenance: which DSIR gate or external consistency requirement created it.

Examples of possible constraint categories include:

- allowed z and k domain;
- required scale dependence;
- required redshift dependence;
- permitted or forbidden gravitational slip structure;
- growth/lensing relation constraints;
- stability requirements;
- causal/locality requirements where applicable;
- existence of a GR/LambdaCDM-compatible limit in regions where the reconstructed residual is compatible with zero;
- absence of signatures already excluded by null channels.

These examples are architectural categories only, not current empirical findings.

### Anti-circularity / blind-gate rule

The future model must not be both designed and validated on exactly the same complete DSIR information.

Split the eventual evidence into two logical sets:

- `G_design`: gates/constraints permitted to inform model construction;
- `G_blind`: prospectively reserved gates or external observables not used to tune the final frozen model.

Once the model equations, parameterization and allowed fitting procedure are frozen, evaluate `G_blind` without altering the model to rescue a failure. A blind-gate failure remains a failure unless a new, explicitly versioned model is defined and treated as a new hypothesis.

This is intended to distinguish prediction from reconstruction-by-construction.

---

### DSIR-6 — Independent predictions / external falsification tests (conditional)

**Question:** Does the frozen DSIR-derived model predict phenomena or datasets that were not used in its construction?

**Core deliverable:** genuinely external or withheld tests, new predictions and falsification opportunities.

This is a conditional follow-on paper rather than a required prerequisite for DSIR-5. It becomes especially valuable if DSIR-5 produces a nontrivial new model.

## Publication dependency graph

```text
DSIR-1  Framework
   |
   v
DSIR-2  Inverse reconstruction machinery
   |
   v
DSIR-3  Observational implementation + complete funnel
   |
   v
DSIR-4  Existing-Model Funnel Matrix
   |
   +--> existing model/equivalence class sufficient -> no forced new-model claim
   |
   +--> unresolved/excluded existing inventory
            |
            v
        DSIR-5  DSIR-derived minimal new model
            |
            v
        DSIR-6  Independent predictions / external falsification tests
```

## Separation rules

1. **DSIR-3 is not the model paper.** It builds and validates the observational funnel.
2. **DSIR-4 is not merged into DSIR-5 by default.** Existing models are tested before the new model is constructed.
3. **DSIR-5 is conditional.** A new model is not scientifically required if an existing model or equivalence class already survives the completed funnel.
4. **No model-driven threshold tuning.** Funnel thresholds/semantics used in DSIR-4 must be prospectively fixed independently of the desired fate of any specific model.
5. **No post-hoc rescue inside a frozen hypothesis.** If a frozen model fails a blind gate, changing its equations/parameterization defines a new model version.
6. **Model Funnel Matrix work may begin before DSIR-3 is numerically complete**, but unavailable gates must be marked `NOT_YET_TESTABLE`; they may not be guessed or replaced by proxies that change the frozen semantics.
7. **Early matrix results are provisional by layer.** No model receives a full `DSIR PASS` until every mandatory gate in the final frozen funnel has admissible authority.

## Immediate project consequence

Parallel to completion of Article 3, the project may now prepare the DSIR-4 Model Funnel Matrix infrastructure:

- freeze the representative model inventory;
- define the exact mapping of each model to the common DSIR interface;
- define model-domain admissibility rules;
- define machine-readable per-gate status semantics;
- run only gates whose observational authority is already available;
- retain unavailable later gates as `NOT_YET_TESTABLE` rather than extrapolating outcomes.

At the same time, DSIR-5 work is limited to a **constraint skeleton** and anti-circularity design. No final new-model claim should be frozen before DSIR-4 establishes whether such a model is scientifically needed.

## Frozen architecture summary

The project publication architecture is therefore:

1. **DSIR-1 — Framework**
2. **DSIR-2 — Inverse reconstruction / mathematical machinery**
3. **DSIR-3 — Observational implementation + complete funnel**
4. **DSIR-4 — Existing-Model Funnel Matrix**
5. **DSIR-5 — DSIR-derived new dark-sector model, conditional on DSIR-4**
6. **DSIR-6 — Independent predictions / external falsification tests, conditional follow-on**

Any future reordering or merger must be explicit, versioned, and justified; it must not silently erase the separation between existing-model testing and construction of the new model.
