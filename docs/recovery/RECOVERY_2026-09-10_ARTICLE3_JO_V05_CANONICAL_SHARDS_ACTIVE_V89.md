# DSIR recovery V89 — JO v0.5 canonical shards active

Date: 2026-09-10. Scope: DSIR only.

## Preserved science authority
Exp073IR remains `NUMERICALLY_UNRESOLVED_EXP073IR`; JI support remains feasible; JJ/JK remain support-only NOT_CONVERGED at `0.037280144773915974` / `0.016330535730270664`. Covariance restriction remains unauthorized; Wm_S3 remains unopened. Frozen `REL_TOL=1e-3`, `h=1e-4`, physical domain, support, masks, traversal and anti-rescue rules are unchanged.

Readiness telemetry remains Article III **68%**, overall funnel-to-freeze **67%**. Process recovery alone creates no score increase.

## JO v0.4 terminal classification
Repaired v0.4 run `34529375485` completed static equivalence and all eight per-model response shards. Aggregate job `103047043452` failed closed before response reconstruction/equality on `cross-shard identity mismatch node_sha256`.

Independent receipt audit found two 4097-node identities from independent hosted executions of the same frozen `np.geomspace` construction:
- `f30556be2547732ed0b87b56368e01e46504a975f94fcbbc5e7bc8cfc525e5eb`, ratio binary64 `1.0015890522775792`;
- `80d5a13c9fa32e77a248b5a835ecf210b9e6afdda27decaffba27b829c261a92`, ratio binary64 `1.001589052277579`.

The ratio difference is one ULP. The aggregate never reached `np.array_equal` on reconstructed responses; therefore v0.4 is `INVALID_INFRA_PLUS_0_PLUS_0`, not a valid history-control negative. No v0.4 response value is authority for node selection and no v0.4 response shard may be reused.

## JO v0.5 canonical-node recovery
Prospective preregistration `docs/dsir4/prereg/EXP073JO_ARTICLE3_JL_SLOT20_CANONICAL_NODE_SHARD_RECOVERY_V0_5.md`, creation commit `14093ed9e6cf4a89d21f338ea7814d66e80fe15f`, blob `3f9514f9f18ffd5e28e2ef54d132759cbe9333a1`, was frozen before any v0.5 grid-freeze output.

The preregistered selection rule is first successful response-blind grid-freeze execution only, independent of prior response values. First and therefore unique authoritative freeze run/job `34530311592 / 103049156874` completed SUCCESS at workflow head `012ca1dfb37b1f3edf597c3372b16af3b688fe3d`.

Freeze artifact `10173203482`:
- GitHub and independently verified ZIP SHA256 `1f46f9df8a3a6cef3bb6f04bffe45c35d82bb29f95d739157419f8d2a2b20765`;
- exact canonical `<f8` node payload SHA256 `f30556be2547732ed0b87b56368e01e46504a975f94fcbbc5e7bc8cfc525e5eb`;
- exact `float.hex()` payload SHA256 `98cd360d0764a884471cb09b4504b79583e2ffaea4423389ec473e98b8656c2a`;
- 4097 nodes / 32776 raw bytes, guards `(0,1)`, ratio binary64 `1.0015890522775792`;
- response-blind true, CLASS not imported/run, observational/prior-response artifacts not read.

Persistence run/job `34530521341 / 103049841655` completed SUCCESS after a minimal pinned-NumPy audit dependency repair and committed the exact payload to Git at `b19a925bc1d282412da8759ccfe0a8fa31e98029`.

Durable canonical authority: `docs/dsir4/authority/EXP073JO_CANONICAL_4097_NODE_PAYLOAD_AUTHORITY_V0_5.json`, creation commit `247119aa7322ba41b50daf83a0d93b5e7cd6b500`, blob `b70ede7f8ecdf0cc67a9f20d33cafc1708eee8e8`.

V0.5 shard helper `ci/exp073jo_slot20_per_model_shard_v0_5.py`, creation commit `a8f185cd134cc4bb234265dd62cd79662cfa1fef`, blob `26da8da97c91ad4adac324ebf3e40dab48524975`, loads the committed canonical bytes and does not regenerate `np.geomspace`.

Canonical eight-shard workflow head `5c11549604f3254c51dbc180464deb77740a12b3`; active run `34530745922`. It recomputes all four frozen models for both phases. V0.4 responses are forbidden from reuse.

## Exact next action
Terminal-consume run `34530745922`. Verify static-equivalence, all eight shard receipts and artifact SHA/provenance. Require the common node SHA exactly `f30556be2547732ed0b87b56368e01e46504a975f94fcbbc5e7bc8cfc525e5eb`. Then consume aggregate artifact and independently verify reconstructed after-history/fresh-tail `<f8 (4,2)` payload hashes and exact `np.array_equal`, finite-mask and positive-mask identity.

Valid aggregate PASS -> record durable JO v0.5 authority and unlock exactly one unchanged checkpointed JL recovery. Valid exact inequality with complete provenance -> record support-only negative and keep JL blocked. Infrastructure failure -> repair only first causal infrastructure defect; no science/tolerance/grid rescue.
