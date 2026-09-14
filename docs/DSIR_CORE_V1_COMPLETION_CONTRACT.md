# DSIR Core v1 Completion Contract

Status: PROSPECTIVE FREEZE-SCOPE CONTRACT
Date: 2026-09-15
Scope: DSIR Core only. Polygon model realization work is explicitly out of scope except where used as regression evidence for the frozen core.

## Purpose

Freeze DSIR as a reusable, model-independent adjudication core for the DSIR Polygon. The Core defines numerical, statistical, comparison, provenance, decision, and governance semantics. Model-specific implementations, solvers, priors, and scientific claims remain in the Polygon/adapters and must not silently modify Core rules.

## Freeze criterion

DSIR Core v1 is eligible to be declared `FROZEN` only when every blocker below is terminally closed with immutable provenance and reproducible validation. G7, G8, and G9 scientific discovery gates are not freeze blockers; their procedures must be frozen, but their scientific outcomes may remain OPEN.

### F1 — Layer-B numerical closure

1. Prospectively freeze the full 107-row denominator and exact input identities.
2. Freeze the validated forced NumPy baseline and exact-target-union construction for the full object.
3. Freeze solver accounting, support/domain checks, thresholds, and fail-closed rules.
4. Execute the full 107-row numerical replay only after the preregistration and immutable contract are committed.
5. Complete an independent numerical/provenance audit and persist a terminal authority object.

No target-local, ad hoc, or post-result node union is authorized.

### F2 — Production reference closure

Promote the reference/control layer from partial readiness to a production-grade baseline contract:

- canonical LambdaCDM/reference origin;
- solver-equivalence policy;
- zero-limit and bridge tolerances;
- deterministic classification of PASS / FAIL / BLOCKED / INVALID / N_A;
- provenance requirements for all reference comparisons.

### F3 — Whitening, rank, covariance, nuisance, and quotient closure

Freeze the model-independent statistical layer used by all Polygon comparisons:

- covariance transformation and whitening;
- data-whitened cross-family rank stress tests;
- `R_obs` and `R_model(pi)` semantics;
- theory-prior/family weighting sensitivity;
- nuisance projection or marginalization rules;
- exact-identity / gauge / calibration quotienting;
- common-domain and missing-channel semantics;
- uncertainty propagation and null calibration;
- explicit rule that unknown/undefined cells are masked and never zero-imputed.

### F4 — Core-to-Polygon adapter contract

Freeze a machine-readable adapter interface. Each model realization submitted by the Polygon must provide, at minimum:

- model and realization identifiers;
- parameter-space identity and tested point/ray/manifold identity;
- solver/code version and immutable source identifier;
- numerical settings and input hashes;
- validity/support domain;
- mapping from native solver outputs to DSIR response coordinates;
- response blocks and masks;
- theory and numerical uncertainty descriptors;
- complete provenance sufficient for replay.

Model-specific fixes belong in adapters/Polygon unless they expose a genuine Core implementation defect.

### F5 — Decision semantics, including NEW_MODEL_REQUIRED

Freeze terminal Core states and escalation semantics before evaluating future candidate models.

Minimum terminal states:

- `PASS`
- `FAIL`
- `BLOCKED`
- `INVALID`
- `N_A`

`BLOCKED`, unavailable adapters, unsupported domains, masked cells, or incomplete provenance must never be reinterpreted as evidence that a new physical model is required.

A `NEW_MODEL_REQUIRED` conclusion is eligible only after a prospectively frozen coverage denominator of known models/realizations has been tested under a common admissible domain, with covariance/whitening/nuisance/quotient handling complete, uncertainty and model-prior sensitivity accounted for, robustness checks passed, and a residual discrepancy surviving the frozen comparison procedure. A future discovery claim still remains subject to the G7/G8/G9 hierarchy.

### F6 — Executable methodology and release validation

Create and validate a single machine-readable Core test registry and a fail-closed orchestration path that can answer whether a repository commit satisfies DSIR Core v1.

The release validator must check at least:

- required contracts and authorities exist;
- immutable hashes/commits resolve;
- required regression workflows are terminal;
- expected artifacts and provenance digests match;
- all freeze blockers F1-F5 are closed;
- no open blocker is hidden behind a summary percentage;
- the release bundle is deterministic and reproducible.

### F7 — Governance and change control

Before final freeze, add and validate:

- `DSIR_CORE_V1_FREEZE_MANIFEST`;
- `DSIR_CORE_CHANGE_CONTROL`;
- machine-readable version identity;
- maintenance versus methodology-change rules;
- mandatory regression scope for any post-freeze Core change.

After freeze:

- model-specific failures or extensions are handled in Polygon adapters;
- implementation defects may be repaired only under maintenance rules with regression evidence;
- changes to response definitions, covariance/whitening semantics, thresholds, masks, decision states, or `NEW_MODEL_REQUIRED` logic require a new Core version and full prescribed regression.

## Scientific frontier explicitly outside the freeze blocker set

The following may remain scientifically OPEN when DSIR Core v1 is frozen:

- G7: universal residual relation;
- G8: withheld predictive survival of such a relation;
- G9: reconstruction or exclusion of candidate underlying dynamics/action.

The Core must freeze how these gates are evaluated; it does not need to force their scientific success before release.

## Readiness accounting

The legacy single readiness percentage must not be used as the sole freeze criterion. Track at least three independent dimensions:

1. `CORE_METHODOLOGY_READINESS`
2. `CORE_EXECUTABLE_REPRODUCIBILITY_READINESS`
3. `POLYGON_SCIENTIFIC_COVERAGE`

Only the first two are required to reach 100% for `DSIR Core v1 FROZEN`. Polygon scientific coverage may continue to grow afterward without changing the Core.

## Authorized critical path

The freeze workstream is restricted to:

1. full 107-row Layer-B prospective freeze and replay;
2. independent numerical/provenance audit;
3. production reference closure;
4. G5/statistical-layer closure;
5. covariance/whitening/nuisance/quotient Core closure;
6. Core-to-Polygon adapter contract;
7. terminal decision and `NEW_MODEL_REQUIRED` semantics;
8. executable registry/orchestrator/release validator;
9. freeze manifest, versioning, and change control;
10. post-freeze-style regression on existing Polygon model families without modifying Core rules;
11. declaration of `DSIR Core v1 FROZEN` only if all preceding blockers pass.

Any work outside this path requires an explicit reason why it is a freeze blocker. Otherwise it belongs to the scientific Polygon backlog.

## Anti-drift rule

No new model family, scientific mechanism, or attractive post-result relation may expand the DSIR Core v1 freeze scope unless it demonstrates a missing model-independent Core capability. The completion contract itself may be amended before freeze only prospectively, with an explicit rationale and immutable history; it must not be retrofitted to make completed results pass.
