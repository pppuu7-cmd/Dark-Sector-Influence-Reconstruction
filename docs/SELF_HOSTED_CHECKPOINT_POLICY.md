# DSIR universal self-hosted checkpoint policy

**Effective:** 2026-09-03

This policy is mandatory for every task executed on the user's self-hosted/home runner, without classifying the task as heavy, medium, light, preflight, benchmark, production, QA, staging, or utility.

## Mandatory rule

No new self-hosted task may be launched unless its prospective workflow contains a durable checkpoint/resume contract.

The contract must:

1. preserve all safely completed expensive stages;
2. for banded/chunked/iterative work, checkpoint only at complete deterministic unit boundaries (complete band/chunk/replica/stage), never fabricate intra-unit progress;
3. store canonical payloads with SHA256 plus exact provenance and a contract fingerprint;
4. persist checkpoints remotely under a dedicated `checkpoints/*` namespace or an immutable GitHub Actions artifact when the stage is immutable and independently addressable;
5. restore only after exact verification of provenance, contract, dimensions/dtype and SHA; mismatch, corruption, unknown transport state, or ambiguous remote state must fail closed;
6. checkpoint an atomic expensive stage immediately after it completes. If an atomic stage cannot be safely checkpointed internally, interruption may repeat that stage only, not earlier completed stages;
7. stop further computation if a completed stage cannot be durably checkpointed;
8. keep independent scientific replicas in independent checkpoint namespaces;
9. never alter frozen historical experiment results or reinterpret a failed/incomplete historical run through a later checkpoint repair.

Preferred implementation is the proven Wm_S2 architecture based on `ci/dsir_remote_band_checkpoint_v0_1.py` and the transport-safe semantics of `ci/dsir_checkpoint_git_sync_v0_2.sh`, adapted prospectively for each experiment.

## Current transition

Exp073CL run `33683175039` is historical infrastructure-incomplete evidence: the self-hosted job was abandoned/cancelled after a TLS disconnect while building the fresh real Wm_S3 PCL, before the coupling benchmark. It had no durable compute checkpoint and remains immutable.

The next Wm_S3 successor and every subsequent home-runner task must satisfy this policy before launch.

This policy is infrastructure/governance only and changes Article-3 readiness by `+0/+0` unless a frozen ledger explicitly authorizes otherwise.
