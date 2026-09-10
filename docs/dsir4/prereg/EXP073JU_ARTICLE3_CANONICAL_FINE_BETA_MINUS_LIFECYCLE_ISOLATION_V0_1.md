# Exp073JU — Article III canonical-fine beta-minus lifecycle isolation v0.1

Date frozen: 2026-09-11. Scope: DSIR Article III process/support only. Effect `+0/+0`.

Status: PROSPECTIVELY FROZEN after independent Exp073JS artifact audit, after Exp073JT canonical shared-lattice materialization and durable promotion, and before any Exp073JU numerical output.

## Purpose

Exp073JS proved exact one-live cross-model lifecycle isolation for all four finite-difference roles on each role's locally generated 4097-node grid. Independent audit then found that `reference`, `alpha_minus`, and `beta_plus` ran on the pre-existing JQ canonical fine node stream SHA256 `f30556be2547732ed0b87b56368e01e46504a975f94fcbbc5e7bc8cfc525e5eb`, while the `beta_minus` JS job ran on a host-dependent last-bit variant. Exp073JT subsequently materialized and committed the exact pre-existing canonical fine stream.

Exp073JU closes exactly this one coverage gap. It does not rerun the three already canonical-covered roles and does not alter any scientific threshold, interpolation rule, finite-difference rule, observational traversal, or Exp073JL decision criterion.

## Frozen authorities and canonical input

Required before execution:

- independently verified Exp073JT authority `docs/dsir4/authority/EXP073JT_ARTICLE3_CANONICAL_SHARED_LATTICES_V0_1.json`, classification `CANONICAL_SHARED_LATTICES_MATERIALIZED_PASS_PLUS_0_PLUS_0`;
- conservative JS coverage audit `docs/dsir4/authority/EXP073JS_ARTICLE3_LIFECYCLE_GEOMETRY_COVERAGE_AUDIT_V0_1.json`, classification `LOCAL_LIFECYCLE_PASS_CANONICAL_FINE_COVERAGE_3_OF_4_PLUS_0_PLUS_0`, with only `beta_minus` missing;
- canonical fine file `docs/dsir4/canonical/EXP073JL_CANONICAL_FINE_4097_NODES_U64HEX_V0_1.txt`;
- exact canonical fine text SHA256 `290075f777c88964aa6b670694063e9b4ad0d5d4dcb16ee12adad5103ca1b6c7`;
- exact decoded contiguous little-endian `<f8` node SHA256 `f30556be2547732ed0b87b56368e01e46504a975f94fcbbc5e7bc8cfc525e5eb`;
- requested-node count 4097, base N=4096, guard `(0,1)`.

The JU execution MUST decode the committed uint64 stream. It MUST NOT call `np.geomspace` or `guarded_lattice()` to regenerate the fine grid.

## Frozen solver/model protocol

- pinned CLASS-IV commit `ac627d54e9ce196a08878d1ba33999819925d19c`;
- baseline `configs/dsir4/c2/ide0_reference_v0_1.ini`;
- precision `configs/dsir4/c2/dsir_ide_p8_v0_1.pre`;
- infrastructure-only capacities `_MAX_NUMBER_OF_K_FILES_=4608`, `_ARGUMENT_LENGTH_MAX_=131072`;
- native `k_per_decade_for_pk=20`;
- finite-difference `h=1e-4`;
- centered-cubic interpolation in `ln(k)` from frozen JJ response machinery;
- requested-node lookup ceiling `1e-12`;
- threads OMP/OpenBLAS/MKL/NUMEXPR all 1.

Model parameters remain exactly:
`reference=(0,0)`, `alpha_minus=(-1e-4,0)`, `beta_plus=(0,+1e-4)`, `beta_minus=(0,-1e-4)`.

Run one hosted job with at most one CLASS instance live at a time, in this exact lifecycle order:

1. fresh `beta_minus`, evaluate request A then B, serialize selected outputs;
2. fresh `reference`, evaluate A then B, cleanup;
3. fresh `alpha_minus`, evaluate A then B, cleanup;
4. fresh `beta_plus`, evaluate A then B, cleanup;
5. fresh `beta_minus`, evaluate A then B, serialize selected outputs and cleanup.

Requests are exactly the JS/JR controls:
- A: `z=float.fromhex('0x1.3851eb851eb85p-1')`, targets `[0.0013,0.0047,0.013,0.041]`;
- B: `z=float.fromhex('0x1.1c28f5c28f5c3p+0')`, targets `[0.0019,0.0073,0.021,0.057]`.

Intervening model outputs are process witnesses only and MUST NOT be used in any convergence/scientific calculation.

## PASS / FAIL

`CANONICAL_FINE_BETA_MINUS_LIFECYCLE_ISOLATION_PASS_PLUS_0_PLUS_0` requires:

- exact canonical text and decoded node SHAs above;
- 4097 nodes, finite, positive, strictly increasing;
- zero unsupported target evaluations across all five fresh instances;
- max requested-node coordinate mismatch `<=1e-12` across all five instances;
- for selected beta-minus request A and B separately: exact `np.array_equal(before,after)`, exact contiguous `<f8` SHA equality, identical finite masks and identical positive masks;
- max absolute and relative diagnostic differences exactly `0.0`.

A valid bitwise inequality is `CANONICAL_FINE_BETA_MINUS_LIFECYCLE_ISOLATION_FAIL_PLUS_0_PLUS_0`. Missing/malformed authority, canonical stream mismatch, build failure, solver/runtime failure, unsupported target, or provenance mismatch is `INVALID_INFRA_PLUS_0_PLUS_0`. No ULP allowance, tolerance relaxation, rounding, smoothing or majority vote is permitted.

## Interpretation ceiling

JU PASS closes canonical fine lifecycle coverage to 4/4 only when combined with the independently audited canonical-grid JS PASS receipts for `reference`, `alpha_minus`, and `beta_plus`. It permits a separate sequential-execution authorization audit over JR/JQ/JS/JT/JU/source evidence. It does not itself authorize a recovered Exp073JL execution, does not evaluate `REL_TOL`, creates no Layer-B scientific authority, does not authorize covariance restriction and does not open Wm_S3.

Repository readiness for preparing Article III remains 68% and funnel-freeze readiness remains 67% regardless of this process-control outcome.