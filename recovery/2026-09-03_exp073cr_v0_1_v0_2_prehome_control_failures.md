# Exp073CR v0.1/v0.2 — pre-home control failures (+0/+0)

Date: 2026-09-03
Scope: Wm_S3 resource/control preparation only. No self-hosted Exp073CR numerical task executed under v0.1 or v0.2.

## Exp073CR v0.1

The prospectively created 64-shard geometry was scientifically/arithmetic-preserving by construction, but the v0.1 preregistration/driver bound the candidate file to an incorrect byte SHA256 (`15d8f15a...`). Direct hashing of the already-created candidate established the actual immutable file SHA256 as `d48e46197b48a6fcdf7d3eb3b0817973a2eadb25bbb617e7b8060c8c17209462` before any home execution.

Hosted run `33768087823`, job `100690981125`, therefore remained a pre-home static/provenance control failure. v0.1 cannot authorize home execution and is preserved rather than edited.

Classification: **PRE-EXECUTION CONTROL/PROVENANCE FAIL +0/+0**. Not a numerical/scientific result.

## Exp073CR v0.2

v0.2 prospectively corrected the candidate byte SHA and moved to a fresh checkpoint namespace. Hosted run `33768408220`, job `100692073818`, demonstrated:

- corrected geometry validation: PASS;
- authoritative ll3 bitwise regression: PASS;
- durable v0.2 seed creation: PASS;
- final restore/static-audit step: FAIL.

The final static audit failed because the workflow searched for a brittle prose literal `durability-before-refill`; the frozen driver expresses the contract field as `durability_before_refill` while implementing the actual compute-loop order as `store_shard -> durable checkpoint sync -> refill submit`.

No v0.2 home activation was created. The failure is therefore isolated to hosted static-control code and does not change the ll3 numerical/exactness evidence.

Classification: **PRE-EXECUTION STATIC-AUDIT CONTROL FAIL +0/+0**. Not a numerical/scientific result.

## Successor rule

Exp073CR v0.3 is the only permitted successor. It changes only the static-audit mechanism and version/checkpoint namespace. It verifies the concrete source-order invariant programmatically and keeps unchanged:

- corrected candidate SHA `d48e46197b48a6fcdf7d3eb3b0817973a2eadb25bbb617e7b8060c8c17209462`;
- heavy-first queue SHA `3ba315d9bc24883ef746d92e785e0a040f9b13e751f59dda9a93e825a6390db4`;
- 64 shard geometry;
- exact helper arithmetic;
- exactly 8 persistent outer workers and nested numerical threads=1;
- durability-before-refill;
- exact complete-band reconstruction against immutable Exp073CQ terminal references;
- CPU fraction threshold >=0.90;
- zero positive swap increase;
- no tolerance/ULP/rounding/smoothing/averaging rescue;
- scientific credit +0/+0.
