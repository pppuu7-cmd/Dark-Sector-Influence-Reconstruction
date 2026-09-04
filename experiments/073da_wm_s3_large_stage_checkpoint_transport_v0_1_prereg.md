# Exp073DA v0.1 — Wm_S3 large-stage durable-checkpoint transport gate

Date: 2026-09-04. Scope: DSIR only. Support/infrastructure gate; accounting always `+0/+0`; no Wm_S3 scientific authority may be created here.

## Authority and motivation

Exp073CX v0.4 raw-validated `A1_EXP073BU_ACTIVATION_READINESS_PASS` closes the production-driver/readiness layer but does not activate Exp073BU. The mandatory universal self-hosted checkpoint policy remains authoritative. Its preferred `ci/dsir_checkpoint_git_sync_v0_2.sh` transport constructs one Git tree/commit containing the whole checkpoint directory.

Exp073BU production checkpoints contain DES-scale payloads that are too large for that transport without a prospective large-object adaptation. In particular the frozen full stock MCM has 603,979,776 float64 values = 4,831,838,208 bytes before FITS container overhead, while GitHub enforces a 100 MB single Git-object/file limit and a 2 GB push-size limit. The dense NSIDE=4096 canonical `<f8` masks are also large: 12*4096^2 = 201,326,592 values, i.e. 1,610,612,736 payload bytes per dense map before `.npy` framing.

Historical checkpoint branches and results remain immutable. Exp073BU remains NOT ACTIVATED until this gate and its permitted successor(s) close transport readiness.

## Frozen purpose

Determine whether the existing canonical Git checkpoint transport can safely carry every one of the six Exp073BU boundaries without violating GitHub object/push limits. If it cannot, freeze and executable-audit a minimal prospective sharded transport adaptation that preserves the existing `checkpoints/*` authority model and fail-closed semantics rather than creating a competing control plane.

## Frozen requirements for an admissible large-stage adaptation

1. Dedicated `checkpoints/*` namespace only; A and B remain isolated.
2. Science payload bytes are never numerically transformed. Transport compression is allowed only if decompression is byte-exact and verified against the canonical payload SHA256.
3. Every remote Git blob/chunk must be <= 64 MiB, leaving margin below GitHub's enforced 100 MB object limit.
4. Every push batch must carry <= 1 GiB of new checkpoint chunk payload, leaving margin below the enforced 2 GB push-size limit.
5. Chunk ordering, byte offsets, byte counts, per-chunk SHA256, whole-file SHA256, source head, contract fingerprint, stage, replica and checkpoint namespace are frozen in a canonical manifest.
6. Restore requires exact remote-head binding, exact manifest identity, exact per-chunk SHA256, exact reassembly byte count and whole-file SHA256. Missing/extra/reordered/corrupt chunks, unknown transport state or head races fail closed.
7. A stage becomes `complete` only after every required payload is remotely durable and a final manifest commit has been independently observed at the expected remote head. Partial chunk upload is resumable transport progress but never scientific/stage completion.
8. No scientific arithmetic, DES masks, NaMaster 2.7 operations, band edges, `TE<-TE`, tolerances, data domain or provenance rules may change.
9. No historical Wm_S3 numerical payload may be imported.
10. Hosted audit uses deterministic synthetic byte payloads only; no DES-scale science numerics.

## Frozen classifications

- `K1_LARGE_STAGE_SHARDED_CHECKPOINT_TRANSPORT_PASS`: existing whole-tree transport is correctly rejected for Exp073BU large stages; the prospective sharded adapter passes deterministic split/manifest/reassemble/corruption/race/static-limit tests and preserves canonical checkpoint identity. Permits a separate activation-orchestration binding audit; does NOT activate Exp073BU.
- `K2_LARGE_STAGE_TRANSPORT_IMPLEMENTATION_FAIL`: requirements are sound but implementation/static tests fail. Repair smallest causal infrastructure defect prospectively; no science run.
- `K3_EXISTING_TRANSPORT_SAFELY_SUFFICIENT`: only admissible if frozen size/object/push inequalities prove the unmodified existing transport is within limits. Otherwise this classification is forbidden.
- `K4_INFRASTRUCTURE_OR_SOURCE_BINDING_FAIL`: source/blob/runner/dependency/transport audit infrastructure fails before the frozen classification can be evaluated.

## Fixed checks

Hosted audit must verify: A1 immutable recovery ancestor/token; universal checkpoint policy and `dsir_checkpoint_git_sync_v0_2.sh` blob binding; Exp073BU production-driver blob binding; six-stage order; 4,831,838,208-byte MCM lower bound; NSIDE=4096 dense-map payload lower bound; existing-transport incompatibility with 100 MB object / 2 GB push limits; 64 MiB chunk cap; 1 GiB batch cap; exact synthetic whole-file SHA round trip; corruption rejection; missing/reordered chunk rejection; A/B namespace isolation; no historical import; no tolerance rescue; `science_gate_scored=false`; `exp073bu_activated=false`.
