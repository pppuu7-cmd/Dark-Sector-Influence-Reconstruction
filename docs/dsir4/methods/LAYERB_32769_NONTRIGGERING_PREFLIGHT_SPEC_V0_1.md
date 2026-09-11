# Layer-B 32769 non-triggering preflight specification v0.1

Date: 2026-09-11. Scope: DSIR Article III Layer-B support refinement only.

## Status
`PREFLIGHT_SPEC_FROZEN_EXECUTION_UNAUTHORIZED`

This document is a **non-triggering specification**. It creates no workflow dispatch, no solver execution, no scientific classification, and no authority to run the 16385->32769 rung. Its purpose is to make the missing prerequisites explicit and independently auditable before any production execution can even be considered.

## Immutable scientific parent
A future 32769 preflight MUST bind exactly to:

- terminal parent authority: `docs/dsir4/authority/LAYERB_CANONICAL_8193_TO_16385_NOT_CONVERGED_V0_1.json`;
- terminal parent Git blob: `7958e1f44c0224e1828f89b1472aa33226c61886`;
- parent scientific classification: `COMMON_GRID_NEXT_REFINEMENT_NOT_CONVERGED_PLUS_0_PLUS_0`;
- parent maximum relative component difference: `0.012484060640679777`;
- frozen strict relative tolerance: `0.001`;
- frozen finite-difference `h`: `0.0001`;
- frozen native `k_per_decade_for_pk`: `20`.

The parent explicitly records `denser_successor_32769_authorized=false`. This specification does not override that bit.

## Immutable canonical 16385 anchor
A future preflight MUST independently verify all of the following before generating any successor support:

- response-blind authority: `docs/dsir4/authority/LAYERB_RESPONSE_BLIND_CANONICAL_FINE_16385_V0_1.json`;
- authority Git blob: `50aa473299c82c857921a083f7d4de652ba476a4`;
- canonical node file: `docs/dsir4/canonical/LAYERB_CANONICAL_FINE_16385_NODES_U64HEX_V0_1.txt`;
- canonical node-file Git blob: `fc4eb1e7f51a0ad3773b8be13c477652b1f71368`;
- canonical 16385 node-payload SHA256: `3e10cea6e46a6d0c07eac825a4e508829727914c8690d42b187ef894eaa2c975`;
- canonical 16385 u64hex/text SHA256: `7e8f13abe29617bc0d331f07143e6680f50512e2f3811e017bbc74ea847dff69`;
- requested canonical node count: `16385`;
- response-blind generation property: `scientific_response_read=false`.

Any mismatch is a terminal preflight failure. No successor bytes may be accepted after an anchor mismatch.

## Deterministic successor-support requirement
The logical successor size is `32769 = 2^15 + 1`, following the already frozen one-rung sequential common-grid ladder. The future canonicalization stage MUST:

1. generate exactly 32769 requested support nodes by the same deterministic ladder semantics used for the canonical family;
2. be response-blind: it MUST NOT read the 16385 scientific discrepancy/result when constructing node values;
3. emit a canonical 32769 node payload plus an exact bitwise/u64hex representation;
4. record both content SHA256 hashes and Git blob identities after repository freeze;
5. run at least one independent static consumer that recomputes the node count, ordering/monotonicity, endpoint/anchor invariants and hashes from the frozen artifact;
6. fail closed on any host-dependent canonicalization disagreement rather than choosing a scientifically favorable replica.

This specification deliberately does not invent a 32769 payload hash or a generator commit before those bytes exist.

## Scientific-equivalence invariants
A future 16385->32769 scientific comparison is admissible only if the evaluator preserves the already frozen scientific semantics without rescue modifications:

- `REL_TOL = 1e-3` with the same strict comparison semantics;
- `h = 1e-4`;
- native CLASS `k_per_decade_for_pk = 20`;
- centered-cubic interpolation;
- identical physical domain, masks and 107-row accounting rules;
- invalid-row fraction `<=0.05`;
- retained dimension `>=15`;
- unsupported target evaluations `=0`;
- requested-node coordinate mismatch guard `<=1e-12`;
- same component-wise common-grid comparison definition and atom identity rules.

Changing any of these to obtain convergence invalidates the successor as a continuation of the frozen ladder.

## CLASS build-capacity gate
The validated 16385 build envelope expanded CLASS point capacity only to `18432`, while a 32769 rung requires at least 32769 points. Therefore the current build is insufficient.

Before execution authority can be considered, a new **capacity-only build patch** MUST be frozen and independently audited with:

- point capacity `>=32769`;
- exact base CLASS source commit recorded;
- exact patch diff/hash recorded;
- parser argument capacity proven compatible with the new support size;
- clean rebuild identity and executable/library hashes where available;
- a static assertion that no scientific equation, transfer-function logic, interpolation method, precision setting, `h`, tolerance, mask or estimator changed with the capacity patch.

The prior parser capacity `524288` is numerically above 32769, but parser/build parity MUST still be revalidated after the new patch; prior sufficiency is not inherited automatically.

## Resource and lifecycle gate
The existing canonical 16385 GitHub-hosted evidence established memory exhaustion in all four tested roles at approximately 15.4--15.7 GB peak Python RSS. This specification makes **no numerical extrapolation** of 32769 memory use.

A future preflight MUST therefore identify and validate a higher-memory execution topology before production. Required evidence:

1. exact runner/topology identity and available physical memory;
2. a non-scientific resource/lifecycle pilot or equivalent measured proof that the intended topology can construct the required solver lifecycle without OOM;
3. maximum live solver instances constrained to the already frozen lifecycle semantics (`max_live_instances=1` unless an independently proven scientifically equivalent lifecycle is separately frozen);
4. cleanup proof showing final live instances return to zero;
5. peak RSS/available-memory/swap telemetry captured without using the scientific outcome to adapt settings;
6. no silent fallback to ordinary GitHub-hosted `ubuntu-24.04` as the production topology while the 16385 hosted-memory exhaustion authority remains applicable.

Resource failure must classify as infrastructure/resource invalidity, never as scientific convergence or non-convergence.

## Anti-duplication / one-live gate
Immediately before any future production dispatch, an independent guard MUST prove that there is no other live or authoritative 32769 canonical scientific run for the same parent and contract. The intended production authority, if ever created, must authorize exactly one canonical run plus at most one unchanged retry for independently classified infrastructure failure.

A retry MUST reuse identical canonical bytes, build identity, scientific parameters and resource topology. Any parameter change requires a new prospective contract and cannot be called a retry.

## Required terminal evidence chain
A future production contract MUST predeclare:

- canonical input hashes and parent authority identities;
- workflow/head SHA and build identities;
- deterministic artifact names and JSON schema;
- full scientific guard fields and resource/lifecycle telemetry;
- artifact SHA256 values;
- a separate independent terminal consumer that verifies hashes and all decisive assertions without reading mutable workflow state;
- explicit classifications separating scientific CONVERGED/NOT_CONVERGED from infrastructure invalidity;
- frozen downstream authority bits for covariance restriction and Wm_S3.

No scientific result may be promoted from a workflow green/red status alone.

## Preconditions required before a one-run authorization document may exist
All of the following must be TRUE simultaneously:

- `PARENT_TERMINAL_AUTHORITY_MATCH = TRUE`
- `CANONICAL_16385_ANCHOR_MATCH = TRUE`
- `CANONICAL_32769_BYTES_FROZEN = TRUE`
- `CANONICAL_32769_STATIC_CONSUMER_PASS = TRUE`
- `CLASS_32769_CAPACITY_BUILD_AUDIT_PASS = TRUE`
- `PARSER_BUILD_PARITY_AUDIT_PASS = TRUE`
- `SCIENTIFIC_EQUIVALENCE_STATIC_AUDIT_PASS = TRUE`
- `HIGH_MEMORY_RESOURCE_LIFECYCLE_PREFLIGHT_PASS = TRUE`
- `ONE_LIVE_ANTI_DUPLICATION_GUARD_PASS = TRUE`
- `TERMINAL_SCHEMA_AND_INDEPENDENT_CONSUMER_FROZEN = TRUE`

Until then:

`32769_EXECUTION_AUTHORIZED = FALSE`

`COVARIANCE_RESTRICTION_AUTHORIZED = FALSE`

`Wm_S3_OPENED = FALSE`

## Current state under this specification
At creation time:

- immutable parent bound: TRUE;
- immutable canonical 16385 anchor bound: TRUE;
- logical successor size fixed at 32769: TRUE;
- canonical 32769 bytes frozen: FALSE;
- current CLASS capacity sufficient: FALSE (`18432 < 32769`);
- higher-memory production topology validated: FALSE;
- triggerable production contract frozen: FALSE;
- 32769 execution authorized: FALSE.

No heavy computation is launched by creating this file.

## Next research action
Implement only the **static/non-scientific side** of this specification next: identify or write the deterministic response-blind 32769 canonical-node generator contract and a non-triggering static consumer, then audit the minimal CLASS capacity-only patch and candidate higher-memory topology. Do not dispatch the 32769 scientific solver until every prerequisite above is independently closed and a separate one-run authorization is created.
