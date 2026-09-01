# 2026-09-01 — Exp073CF pre-activation static audit

Classification: repository-side infrastructure/methodology audit only; `+0/+0`; no Article-3 readiness credit.

## Stale Exp073CA closure

The user reconnected `DSIR-HOME-PC` at 2026-09-01 18:45:47Z and the runner immediately picked up stale Exp073CA attempt3 replica B job `99673921530`. The user stopped the runner with Ctrl+C at 18:47:24Z. GitHub records replica B terminal before PCL: DES-mask download step failed/cancelled and all PCL/compile/preflight/heavy steps were skipped. Replica A job `99673921219` remains the prior infrastructure failure. Exp073CA attempt3 run `33448843621` has no valid A/B scientific comparator inputs and remains `INFRASTRUCTURE_EXECUTION_INCOMPLETE_NO_SCIENTIFIC_CLASSIFICATION_EXP073CA`, `+0/+0`.

## Exp073CF static audit finding

The disabled Exp073CF authority-tail specification inherited an implementation defect from the Exp073CA finalizer wiring: the finalizer matrix contained replicas A and B, but both rows downloaded `exp073cf-compact-A-${{ github.sha }}` into `external/a` and both searched for `*compact_a_v0_1.npz`. Thus the nominal B finalizer would have finalized replica A again. A final A/B equality result from that wiring would therefore not constitute an independent finalizer comparison.

This defect was found before Exp073CF activation and before any Exp073CF run.

Prospective infrastructure-only correction commit:

- `80c273d89f20cd91065b18236b50060328d33ae8`

Corrected wiring:

- each finalizer matrix row downloads `exp073cf-compact-${{ matrix.replica }}-${{ github.sha }}`;
- each row uses its own `external/current` artifact tree;
- each row searches `*compact_${lower}_v0_1.npz`, with `lower` derived from its matrix replica;
- final A/B artifacts remain independently named and are later compared exactly.

No acceptance criterion, numerical tolerance, scientific input, reduction order, finalizer arithmetic, thread policy or authority rule was changed.

## Memory/copy audit

The bound memory-stable PCL helper `ci/exp073cf_memory_stable_wm_s2_pcl_v0_1.py` at commit `5423976c09d5ee338d1a7894ce143faf1bb88225` was inspected. The previously discovered verification copy (`mmap -> ascontiguousarray -> tobytes`) is absent. SHA verification of spill files uses streaming 8 MiB reads; in-memory canonical arrays are hashed through `memoryview(...).cast('B')`; the spill is reopened read-only with `np.memmap`; temp files are cleaned in `finally`; the replica spill directory is removed in the outer `finally`; and temp-to-final publication uses flush/fsync plus same-filesystem atomic `os.replace`.

No additional full-size array copy used solely for SHA verification was found in this static audit. This does not certify full-scale peak memory: `NmtField`/SHT workspace and final mmap + source-side residency remain empirical unknowns at NSIDE=4096.

## Audit binding

Pre-activation static-audit binding commit:

- `82e70d38fba65ddf667e4866f92abfa18b0c0122`

Classification: `PRE_ACTIVATION_STATIC_AUDIT_PASS_WITH_PROSPECTIVE_REPLICA_ISOLATION_FIX`.

## Readiness and next gate

Article-3 readiness remains **Verified 52.0% | Draft/data 53.7%**. This audit is `+0/+0`.

Exp073CF remains disabled and untriggered. Before activation, the home infrastructure must be deliberately re-enabled with an explicit memory-stability preflight; then a new activation binding must pin the actual `.github/workflows` commit and trigger commit. Only a fresh Exp073CF A/B pair may become comparator input. Stale Exp073CA replica B is forbidden as authority.
