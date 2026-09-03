# Exp073CN Wm_S3 checkpointed 8-core resource qualification v0.2 — prospective preregistration

Date: 2026-09-03
Classification scope: resource/performance/checkpoint QA only; `+0/+0` unless a frozen ledger explicitly says otherwise.

## Motivation and predecessor boundary

Exp073CN v0.1 is frozen as `BLOCKED_PRE_EXECUTION_CHECKPOINT_CONTROL` before any authorized home execution because its early hosted audit predated the eventual driver and the driver did not integrate durable per-unit remote checkpointing. v0.2 is a new prospective resource contract; it does not repair, reinterpret, or rescue any historical result.

## Frozen science

No scientific arithmetic changes are permitted. Task `Wm_S3` means Wm source bin S3 (`source_bin=3`, not spin-3), signature `(0,2,0,2)`, DES `NSIDE=4096` RING/C, `ell=0..12287`, 39 frozen bands, `Wm TE<-TE`, canonical little-endian `<f8`. Exact equality only. No tolerance/ULP/rounding/averaging/smoothing/effective-ell/effective-z/effective-k/fiducial-P rescue.

## Resource architecture

1. Exactly 8 visible CPUs are required.
2. Exactly 8 outer compute workers are used for target scheduling.
3. Nested BLAS/OpenMP/MKL/OpenBLAS/BLIS/NUMEXPR thread pools are pinned to 1 per worker.
4. Work units are independent complete frozen bands. Scheduling is dynamic and preserves per-band arithmetic/order; canonical final reassembly is by ascending frozen band id, never completion order.
5. Target scope is all 39 bands unless a later activation binding fail-closed narrows the resource-only scope before execution; no result-dependent narrowing is permitted.

## Universal durable checkpoint contract

A dedicated new namespace `checkpoints/exp073cn-wm-s3-8core-resource-v0-2` is mandatory.

Before any compute the workflow MUST query and restore that namespace using the robust checkpoint transport semantics equivalent to `ci/dsir_checkpoint_git_sync_v0_2.sh`. Remote PRESENT is restored exactly; a prospectively new verified ABSENT namespace may start fresh only under explicit `ALLOW_ABSENT`; unknown transport fails closed.

The local checkpoint contract MUST bind at least: experiment/version, source/activation head, preregistration commit, helper/execution commits, task/source_bin/signature, L/ell/band edges, target band ids, dtype/shape, worker count, nested-thread policy, frozen input PCL identity/provenance, reference identity/method, checkpoint namespace and resource thresholds. The canonical JSON contract receives a SHA256 fingerprint. Any mismatch/corruption/unknown provenance fails closed.

Every completed target band is an expensive complete unit. Immediately after a worker returns a finite canonical `<f8` row, the coordinator MUST:

- validate band id, shape, dtype and finite values;
- write canonical payload + metadata + row SHA256 bound to the contract fingerprint;
- durably synchronize the checkpoint state to the dedicated remote namespace with exact post-push verification;
- only then admit that band as durable completed progress.

A transport/push failure stops further admission fail-closed. A worker result that was computed but not durably admitted is not progress and may be recomputed after restart. No fabricated intra-band progress exists.

On restart, every restored band MUST pass exact contract/dtype/shape/SHA verification before it is skipped. Only missing bands are scheduled. Canonical reassembly MUST be made from verified durable rows and must itself receive a SHA256/provenance receipt.

If a prerequisite atomic PCL/reference stage is reused from an already validated immutable authority, its exact payload SHA/provenance must be bound and copied/checkpointed into the new namespace before target compute; no expensive verified PCL may be recomputed merely for resource QA. If a new atomic stage is required, its completed output must be checkpointed immediately; interruption inside that atomic stage repeats only that stage.

## Frozen resource gates

PASS requires all of the following under the final activation binding:

- all frozen target bands are present exactly once via verified restore or new durable completion;
- canonical target reassembly finite and exact-valid;
- exact `np.array_equal` and identical canonical SHA256 against the prospectively frozen single-worker/reference construction for the same bands;
- no positive swap increase during the target resource measurement;
- process/children effective CPU fraction across 8 visible CPUs is `>= 0.90` under the prospectively frozen telemetry definition;
- complete checkpoint/provenance/contract validation passes;
- final machine token is `PASS_EXP073CN_WM_S3_8CORE_CHECKPOINTED_RESOURCE_V0_2`.

Exact mismatch => `FAIL_EXP073CN_WM_S3_8CORE_CHECKPOINTED_EXACT_V0_2`, resource/numerical-plan FAIL `+0/+0`, no tolerance rescue.

Exact pass with swap increase >0 => `FAIL_EXP073CN_WM_S3_8CORE_CHECKPOINTED_SWAP_V0_2`, resource FAIL `+0/+0`.

Exact pass with CPU fraction <0.90 => `FAIL_EXP073CN_WM_S3_8CORE_CHECKPOINTED_CPU_V0_2`, resource/performance FAIL `+0/+0`.

Transport/runner/dependency/malformed checkpoint/contract/source-head failures before a valid frozen comparison => `INFRASTRUCTURE_INCOMPLETE`, `+0/+0`, not scientific FAIL.

## Mandatory pre-execution audit

No self-hosted v0.2 execution is authorized until a NEW hosted static/regression audit at or after the final execution/workflow/binding commits verifies the *actual* chain, including:

- restore-before-compute;
- dedicated `checkpoints/*` namespace;
- per-complete-band save + remote durable sync + exact post-push verification;
- exact restore validation and missing-band-only scheduling;
- exactly 8 outer workers and inner-thread pinning;
- deterministic ascending-band canonical reassembly;
- reference/target exact comparator and frozen CPU/swap gates;
- fail-closed behavior for contract/source/provenance mismatch and unknown transport.

An audit that predates the execution driver/workflow/binding does not authorize home execution.

## Downstream boundary

This resource qualification is `+0/+0` and does not itself create Wm_S3 angular authority. Full Wm_S3 A/B scientific production remains forbidden until this or a later prospectively versioned resource gate earns its exact PASS token. Historical Exp073CM and Exp073CN v0.1 remain unchanged.
