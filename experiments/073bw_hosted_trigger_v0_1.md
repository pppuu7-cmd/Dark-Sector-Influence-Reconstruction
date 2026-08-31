# Exp073BW hosted trigger v0.1

Triggered prospectively on 2026-08-31 after:

- preregistration commit `ba4b28ec9aeca2a465202374e390ba9b43bb3952`;
- streaming C helper commit `9fb0ecb79986cf5f542760377533a685745b31e2`;
- exact-equivalence Python harness commit `0c3f1290a30e9f437577fbe557559b722c20b4e3`;
- corrected binding commit `ba31ac3f7e610fe9ed56bdb5c02e0367d47ab5b5`;
- workflow creation commit `0019b6cf16f481ca83cb56d3fce0c6502682dc4a`.

Immutable upstream source-lineage prerequisite: Exp073BV run `33420824723`, artifact `9768866582`, digest `sha256:33f013a8c7c06ce2f5f68e62a324b80f2b1911ff2a3cd3ff89a6af4add179cc5`, status `BV_Q1_EXACT_SOURCE_LINEAGE_CONFIRMED`.

This run is NONCLASSIFYING exact implementation-equivalence QA and is `+0/+0` for every outcome. Only the preregistered token `BW_Q1_FULL_AND_STREAM_COMPRESSED_EXACT_EQUIVALENCE_PASS` permits a separately preregistered full-scale streaming successor. No tolerance/ULP/rounding/averaging/majority/preferred-replica rescue. Exp073AQ remains permanent FAIL, Exp073BJ remains PASS, Exp073BD remains provisional/no-downstream-use, and no G8 jump is permitted.

## Infrastructure-only rerun note — 2026-08-31

Initial hosted run `33426592794` terminated before BV binding or any exact scientific/implementation comparator because the workflow requested the immutable BV artifact under the wrong artifact name. Artifact identity itself was already frozen correctly by run ID `33420824723`, artifact ID `9768866582`, and digest above. Workflow commit `249db1b6b5e7b2f3e5267a86a0899d7180eac5ef` changes only the retrieval name to the actual immutable artifact name `exp073bv-namaster27-exact-source-lineage-v0-1`; no helper, harness, comparator, inputs, thread policy, thresholds, or frozen classifications changed. This trigger reruns the same preregistered BW QA after that infrastructure-only correction.
