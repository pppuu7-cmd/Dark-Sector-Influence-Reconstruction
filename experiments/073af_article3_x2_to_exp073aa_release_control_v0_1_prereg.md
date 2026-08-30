# Exp073AF — Article 3 X2 -> Exp073AA release-control gate v0.1

**Frozen:** 2026-08-30 while both Exp073X2 hosted chains P (`33300997298`) and Q (`33301058260`) are still in progress, before any X2 canonical output/hash exists and before any remaining Exp073AA production task is triggered.

## Purpose

Exp073AF is a **non-scientific release-control/firewall gate**. It prevents the original Exp073AA v0.1 prerequisite text (which names the now-incomplete Exp073X pilot) from being used directly after the prospectively frozen X2 succession amendments.

Exp073AF does not modify Exp073AA scientific/angular semantics. It freezes the exact state machine that converts future X2 P/Q outcomes into either:

- `RELEASE_13_EXP073AA_TASKS`, or
- `BLOCK_PRODUCTION`.

A hosted synthetic PASS only proves that this state machine fails closed. It adds **0 scientific-readiness points**; Article-3 strict readiness remains 52%, and G7/G8/G9 remain OPEN.

## Superseding governance documents

The release controller is subordinate to and must implement literally:

1. `docs/ARTICLE3_EXP073X2_PARALLEL_AUTHORITY_SELECTION_2026-08-30.md`;
2. `docs/ARTICLE3_DES_ANGULAR_14_TASK_MANIFEST_X2_SUCCESSION_AMENDMENT_2026-08-30.md`.

It must never reinterpret the old Exp073AA sentence requiring the cancelled Exp073X pilot PASS as current authority.

## Frozen X2 chains

### P — primary

- run `33300997298`;
- trigger/head `2403d9680e1d08a3853084034eb2878faa52b4e0`;
- role `primary`.

### Q — contingency/redundant

- run `33301058260`;
- trigger/head `730ae4951ab8cd8e1dd2c392e991c3120345678a`;
- role `contingency`.

## Frozen outcome vocabulary

Each chain may only be represented to this controller as one of:

- `PENDING`
- `PASS`
- `SCIENTIFIC_REPEATABILITY_FAIL`
- `INFRASTRUCTURE_INCOMPLETE`

For a `PASS`, an exact canonical selected-window SHA256 must also be supplied as 64 lowercase hexadecimal characters. For every non-PASS state, canonical SHA must be absent/null.

The controller never infers a chain result from logs or partial files; a real future caller must bind an immutable hosted classification receipt.

## Frozen release state machine

1. If P is `PENDING`: block.
2. If P is `SCIENTIFIC_REPEATABILITY_FAIL`: block permanently for this frozen route; Q cannot rescue.
3. If P is `PASS` and Q is `PENDING`: block until Q resolves, because a later nominal Q PASS with a different canonical hash would block production under the already-frozen cross-chain consistency rule.
4. If P is `PASS` and Q is `PASS`: release only if canonical hashes are identical; canonical source remains P.
5. If P is `PASS` and Q is `INFRASTRUCTURE_INCOMPLETE`: release with P canonical.
6. If P is `PASS` and Q is `SCIENTIFIC_REPEATABILITY_FAIL`: block; cross-chain scientific disagreement is not a production authority.
7. If P is `INFRASTRUCTURE_INCOMPLETE` and Q is `PASS`: release with Q only as the prospectively authorized fallback.
8. If P is `INFRASTRUCTURE_INCOMPLETE` and Q is `PENDING`: block.
9. If P is `INFRASTRUCTURE_INCOMPLETE` and Q is `INFRASTRUCTURE_INCOMPLETE`: block and require prospective infrastructure repair.
10. If P is `INFRASTRUCTURE_INCOMPLETE` and Q is `SCIENTIFIC_REPEATABILITY_FAIL`: block.
11. Any impossible/unknown field/state/hash combination: block by validation failure.

The conservative P-PASS/Q-PENDING block is prospective and ensures the existing rule “both PASS -> hashes must agree; disagreement blocks production” cannot be discovered only after 13 expensive tasks have already been launched.

## Frozen production task list

On release, the controller must emit exactly, in this order:

1. `Wm_S1`
2. `Wm_S2`
3. `Wm_S3`
4. `WW_S0_S0`
5. `WW_S0_S1`
6. `WW_S0_S2`
7. `WW_S0_S3`
8. `WW_S1_S1`
9. `WW_S1_S2`
10. `WW_S1_S3`
11. `WW_S2_S2`
12. `WW_S2_S3`
13. `WW_S3_S3`

`Wm_S0` must never appear because it comes only from the valid canonical X2 authority. No task may be duplicated, omitted or reordered.

## Anti-leakage / accounting firewall

The release decision may depend only on:

- frozen P/Q identities;
- immutable hosted outcome classes;
- canonical selected-window SHA256 for PASS outcomes;
- the frozen governance state machine above.

It must not read or depend on:

- radial kernels;
- support fractions / `f_invalid`;
- retained coordinates;
- fiducial P;
- covariance or whitening;
- nuisance geometry/SVD/rank;
- quotient/relation/null results;
- G8;
- scientific-readiness optimization.

Output must retain Article-3 readiness `52`, G7/G8/G9 `OPEN`, and `readiness_increment=0`.

## Hosted synthetic test matrix

At minimum test:

- P pending -> block;
- P scientific fail with Q pass -> block;
- P pass/Q pending -> block;
- P pass/Q pass same hash -> release P + exact 13;
- P pass/Q pass different hash -> block;
- P pass/Q infrastructure incomplete -> release P + exact 13;
- P pass/Q scientific fail -> block;
- P infrastructure incomplete/Q pass -> release Q + exact 13;
- both infrastructure incomplete -> block;
- malformed/missing/extra hash rules -> reject;
- unknown state/key -> reject;
- task list exactly 13 and excludes Wm_S0;
- readiness/gates/firewall remain unchanged.

## Required hosted QA token

`PASS_EXP073AF_X2_TO_EXP073AA_RELEASE_CONTROL_SYNTHETIC_V0_1`

This token is technical governance QA only, not a scientific PASS and not authorization based on the still-running real X2 chains.
