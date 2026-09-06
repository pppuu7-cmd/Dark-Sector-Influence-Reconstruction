# DSIR20 — G_DOMAIN_MAPPING re-audit correction

Date: 2026-09-07
Status: **CORRECTED / SUPERSEDES THE EARLIER SAME-DAY RE-ADMISSION CLAIM**

## Why this correction is necessary

The earlier version of this note incorrectly promoted legacy Exp030/031 response-space evidence for IDE, GDM, and designer-f(R) to DSIR-4 `G_DOMAIN_MAPPING=PASS`.

That promotion violated the frozen migration rule in `docs/dsir4/DSIR4_EXISTING_MODEL_PILOT_V0_1.md` and the artifact requirements in `docs/dsir4/DSIR4_MODEL_MAPPING_ARTIFACT_CONTRACT_V0_1.md`.

The frozen DSIR-4 contract requires, before Gate-1 scientific admission, a dedicated hypothesis mapping/prediction lineage that explicitly binds the common residual tensor

`X_{mu nu} = M0^2 G_{mu nu} - T_known_{mu nu}`,

including all six required residual components, the `T_known` partition, conventions, certified `(z,k)` domain, stability/branch assumptions, and immutable prediction provenance. Legacy theory-response separability is not a substitute for this artifact.

## Repository audit

At the time of this correction, `docs/dsir4/mappings/` contains only:

`C0_C1_ANALYTIC_RESIDUAL_MAPPINGS_V0_1.md`.

There are no dedicated DSIR-4 mapping artifacts in that directory for:

- C2 IDE;
- C3 GDM;
- C5 designer-f(R).

Therefore the earlier same-day claim that those three hypotheses had been re-admitted at Gate 1 is retracted.

## Correct DSIR-4 status

| Hypothesis/family | Legacy theory evidence | Dedicated DSIR-4 mapping artifact | Current `G_DOMAIN_MAPPING` |
|---|---|---|---|
| C0 LambdaCDM reference | strong | present/admitted | PASS |
| C1 smooth-w local control | strong | present/admitted | PASS |
| C2 IDE local tangent cone | strong; Exp030/031 comparison-ready | **missing** | **NOT_YET_TESTABLE** |
| C3 GDM cs2/cv2 local pair | strong; Exp030/031 and slip separator | **missing** | **NOT_YET_TESTABLE** |
| C5 designer-f(R) | strong; controlled GR limit and Exp030/031 response | **missing** | **NOT_YET_TESTABLE** |

No scientific FAIL is created by the missing mapping artifacts. This is a missing-authority state, not evidence against any model.

## Legacy evidence retained

The correction does **not** invalidate the old hard computations:

- IDE has a pinned interaction implementation, physical tangent-cone constraints, and non-collinear alpha/beta response geometry;
- GDM has controlled CDM zero closure, cs2/cv2 manifolds, and a theory-level slip separator;
- designer-f(R) has a controlled H-EFTCAMB GR limit and nonzero production response manifold;
- Exp030 remains a valid block-aware theory-comparison readiness PASS;
- Exp031 remains a valid raw-theory cross-family comparison.

Those facts remain support for constructing the missing DSIR-4 mapping artifacts. They are not themselves DSIR-4 Gate-1 authority.

## Methodological lesson

DSIR must apply the same anti-circular/fail-closed discipline to its own bookkeeping as to external cosmological models. A strong prior result cannot be promoted across a newly frozen gate unless the new gate's exact artifact contract is satisfied.

## Next prospective order

Preserve the previously frozen no-cherry-picking order for mapping conversion:

`C2 IDE -> C3 GDM -> C5 designer-f(R)`.

For each family:

1. freeze the six-component residual mapping and `T_known` partition;
2. certify the exact domain and branch/stability conditions;
3. bind the immutable prediction artifact/source lineage;
4. run the Gate-1 admission audit without using downstream outcomes;
5. only then expose the hypothesis to later DSIR-4 gates.

This correction creates no model PASS/FAIL beyond the already admitted C0/C1 Gate-1 results.