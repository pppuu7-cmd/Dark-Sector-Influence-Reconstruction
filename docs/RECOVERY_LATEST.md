# DSIR authoritative recovery — latest

Updated: 2026-09-10. Scope: **DSIR only**. Never mix RTK or RQIR.

Newest immutable authority note: `docs/recovery/RECOVERY_2026-09-10_ARTICLE3_JO_V05_CANONICAL_SHARDS_ACTIVE_V89.md`, creation commit `4f15c5b5e73d83d28437699b5daaa7bf0e059563`. Earlier recovery notes remain immutable history.

## Preserved scientific authority
Exp073IR remains `NUMERICALLY_UNRESOLVED_EXP073IR` with native-grid maximum `0.9998247463807295`, retained 107. Exp073JI remains support-only feasible; Exp073JJ/JK remain support-only NOT_CONVERGED at `0.037280144773915974` / `0.016330535730270664`. Covariance restriction remains unauthorized and Wm_S3 unopened. Frozen `REL_TOL=1e-3`, `h=1e-4`, science domain/masks/traversal and anti-rescue rules remain unchanged. Exp073JP separately retains validated support-only prediction-artifact admission.

## JO v0.4 terminal infra result
Repaired v0.4 run `34529375485` completed all eight per-model response shards, but aggregate job `103047043452` stopped before reconstructed response equality on `cross-shard identity mismatch node_sha256`. Independent receipt audit found two hosted `np.geomspace` 4097-node identities, `f30556be2547732ed0b87b56368e01e46504a975f94fcbbc5e7bc8cfc525e5eb` and `80d5a13c9fa32e77a248b5a835ecf210b9e6afdda27decaffba27b829c261a92`, with grid ratios differing by one ULP. Classification is infrastructure/provenance invalid `+0/+0`, not a valid history-control negative. No v0.4 response may be reused.

## JO v0.5 canonical recovery
Prospective prereg commit/blob `14093ed9e6cf4a89d21f338ea7814d66e80fe15f / 3f9514f9f18ffd5e28e2ef54d132759cbe9333a1` froze a response-independent rule: the first successful response-blind grid-freeze run defines the only canonical payload.

First and unique freeze run/job `34530311592 / 103049156874`, artifact `10173203482`, completed SUCCESS. Independently verified ZIP SHA256 `1f46f9df8a3a6cef3bb6f04bffe45c35d82bb29f95d739157419f8d2a2b20765`; canonical node SHA256 `f30556be2547732ed0b87b56368e01e46504a975f94fcbbc5e7bc8cfc525e5eb`; exact hex SHA256 `98cd360d0764a884471cb09b4504b79583e2ffaea4423389ec473e98b8656c2a`; 4097 nodes / 32776 bytes; response-blind, no CLASS/observational/prior-response reads.

Persistence run/job `34530521341 / 103049841655` SUCCESS; canonical bytes persisted in Git commit `b19a925bc1d282412da8759ccfe0a8fa31e98029`. Durable canonical authority commit/blob `247119aa7322ba41b50daf83a0d93b5e7cd6b500 / b70ede7f8ecdf0cc67a9f20d33cafc1708eee8e8`.

V0.5 helper commit/blob `a8f185cd134cc4bb234265dd62cd79662cfa1fef / 26da8da97c91ad4adac324ebf3e40dab48524975` loads exact canonical bytes and does not regenerate `np.geomspace`. Canonical eight-shard workflow head `5c11549604f3254c51dbc180464deb77740a12b3`; active run `34530745922`.

## Stable readiness telemetry
Current Article III repository readiness: **68%**. Overall funnel readiness for methodology freeze: **67%**. Process retries/recovery do not increase scores.

## Exact next action
Terminal-consume run `34530745922`; verify all eight canonical shard artifact hashes/provenance and common node SHA, then independently verify aggregate reconstructed `<f8 (4,2)` payloads and exact array/finite/positive-mask equality. Valid aggregate PASS -> durable JO v0.5 authority and exactly one unchanged checkpointed JL recovery. Valid exact inequality -> support-only negative, JL remains blocked. Infrastructure invalidity -> repair only first causal infra defect. No tolerance/grid/science rescue.
