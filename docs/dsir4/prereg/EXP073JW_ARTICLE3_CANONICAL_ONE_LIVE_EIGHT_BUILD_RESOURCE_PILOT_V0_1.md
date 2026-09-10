# Exp073JW — Article III canonical one-live eight-build resource pilot v0.1

Date frozen: 2026-09-11. Scope: DSIR Article III process/resource feasibility only. Effect `+0/+0`.

Status: PROSPECTIVELY FROZEN while Exp073JU is still running and before any Exp073JU/Exp073JV result. Exp073JW may be activated only by a valid independently verified Exp073JV classification `SEQUENTIAL_CANONICAL_JL_EXECUTION_AUTHORIZED_PLUS_0_PLUS_0`.

## Purpose

A full recovered Exp073JL using one-live solver lifetime requires four frozen finite-difference models on each of the two canonical lattices, hence eight sequential CLASS constructions in one runner/process domain. Fine-grained cross-run model splitting is forbidden because raw scientific operands may not cross runner/process boundaries. This pilot tests whether that exact eight-build lifecycle is operationally feasible before launching the full 107-row traversal.

Exp073JW is not a convergence gate and cannot determine Layer-B PASS/FAIL.

## Frozen inputs

- exact committed JT canonical coarse stream: 2049 nodes, decoded `<f8` SHA256 `6305c95025e52296b6cb623903f82dc45bb66ac692708b242fc354862ac54c46`;
- exact committed JT canonical fine stream: 4097 nodes, decoded `<f8` SHA256 `f30556be2547732ed0b87b56368e01e46504a975f94fcbbc5e7bc8cfc525e5eb`;
- grids MUST be decoded from committed u64hex files, never regenerated with `np.geomspace`/`guarded_lattice`;
- pinned CLASS-IV `ac627d54e9ce196a08878d1ba33999819925d19c`;
- frozen baseline/precision, native kpd20, `h=1e-4`, centered-cubic ln(k) interpolation and lookup ceiling `1e-12`;
- infrastructure capacities 4608 / parser 131072;
- threads OMP/OpenBLAS/MKL/NUMEXPR = 1;
- model order for each lattice exactly `reference`, `alpha_minus`, `beta_plus`, `beta_minus` with `(0,0),(-1e-4,0),(0,+1e-4),(0,-1e-4)`;
- control requests exactly A then B from JR/JS/JU.

## Frozen one-process protocol

One hosted Python process performs exactly eight solver constructions, with at most one CLASS instance live at any instant:

1. coarse reference -> A,B -> cleanup;
2. coarse alpha_minus -> A,B -> cleanup;
3. coarse beta_plus -> A,B -> cleanup;
4. coarse beta_minus -> A,B -> cleanup;
5. fine reference -> A,B -> cleanup;
6. fine alpha_minus -> A,B -> cleanup;
7. fine beta_plus -> A,B -> cleanup;
8. fine beta_minus -> A,B -> cleanup.

Raw A/B target vectors remain local to this process only. After all four model operands for a lattice are available locally, the unchanged frozen finite-difference response estimator is formed. After both lattice responses are available locally, the unchanged coarse/fine relative-component diagnostic may be computed and recorded, but its magnitude is **decision-neutral** for Exp073JW.

No raw operand may be uploaded for later cross-process scientific combination.

## Resource PASS

`CANONICAL_ONE_LIVE_EIGHT_BUILD_RESOURCE_PILOT_PASS_PLUS_0_PLUS_0` requires:

- valid independently verified JV authorization;
- exact canonical coarse/fine text and decoded node SHAs;
- exactly eight completed CLASS constructions in the frozen order and `max_live_instances=1`;
- all A/B target evaluations valid with zero unsupported targets;
- max requested-node coordinate mismatch <= `1e-12`;
- finite transfer/response tables and unchanged response shapes;
- both coarse and fine A/B responses formed from same-process raw operands using the frozen estimator;
- clean completion and artifact emission within one hosted job.

Any valid numerical value of the A/B coarse/fine relative diagnostic, including a value above `REL_TOL`, does not fail this resource pilot. It is retained only as a decision-neutral consistency diagnostic. Build/runtime/runner-loss/timeout/provenance failure classifies `RESOURCE_OR_INFRA_NOT_FEASIBLE_PLUS_0_PLUS_0`; it is not scientific non-convergence.

## After PASS

Only a valid independently verified JW PASS may permit preregistration/launch of a full recovered Exp073JL one-live canonical traversal. The full run must still use the original JL science classifier and may not inherit a scientific result from this pilot.

JW cannot increase `ARTICLE3_REPOSITORY_READINESS`, authorize covariance restriction, or open Wm_S3. Repository readiness for preparing Article III remains 68%; funnel-freeze readiness remains 67%.