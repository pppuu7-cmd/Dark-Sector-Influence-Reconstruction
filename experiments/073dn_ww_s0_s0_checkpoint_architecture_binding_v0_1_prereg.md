# Exp073DN — WW_S0_S0 checkpoint-architecture binding v0.1

**Frozen:** 2026-09-05 after independently validated Exp073DM support PASS and before any `WW_S0_S0` numerical production output exists.

**Scope:** implementation/resource governance only, `+0/+0` for every outcome. No WW scientific authority may be created here.

## Purpose

Determine prospectively whether the proven Exp073BU 8-core durable A/B architecture can be reused unchanged for `WW_S0_S0`, or whether a WW-specific exact adapter/driver is required before home computation. This is a source-only audit; it must not execute NaMaster or inspect any WW numerical output.

## Frozen authorities

Bind:

- Exp073DM raw support token `PASS_EXP073DM_WW_S0_S0_EXACT_AUTHORITY_PREFLIGHT_V0_1` from run/job `33937980591 / 101229540163`, head `71e8ad4ea601eb756e0e0b2218620b5347416cbe`, artifact `9960805717`, digest `sha256:fa19dbf8c6735e25ec1a500a3f8540f2f868f30e92aa589d3194d7f9deb5c8e3`;
- frozen WW target semantics from `ci/exp073aa_article3_des_angular_task_runner_v0_1.py`: `WW_S0_S0`, spin-2×spin-2 auto, full `[4,39,4,12288]`, selected `EE<-EE`, canonical `<f8 [39,12288]`, no lens mask;
- proven Wm durable base `ci/exp073bu_wm_s3_fresh_ab_production_v0_1.py` and hardware-matched wrapper `ci/exp073bu_wm_s3_fresh_ab_production_8core_v0_3.py`.

## Audit decision rule

Classify `PASS_EXP073DN_REQUIRE_WW_SPECIFIC_CHECKPOINT_ADAPTER_V0_1` if the existing Wm production base is correctly recognized as **not directly reusable unchanged**, while its checkpoint invariants are reusable. The audit must verify all of the following Wm-specific bindings that require a prospective WW implementation rather than runtime flag substitution:

1. Wm imports `reconstruct_lens_mask` and `reconstruct_s3_count_map`;
2. Wm checkpoints `lens_mask.npy` plus `s3_mask.npy`;
3. Wm constructs spin-0 lens field `f0` and spin-2 source field `f2`;
4. Wm requires CLI `--lens-mask`;
5. Wm exact adapter uses `ncls=2` and full window `[2,39,2,12288]`;
6. Wm selected checkpoint is named/semantically bound to `selected_te_complete`, `selected_te.bin`, `TE<-TE`;
7. its namespaces are explicitly `exp073bu-wm-s3-*` and therefore may not be reused for WW.

At the same time, audit and preserve as reusable architecture invariants:

- independent A/B checkpoint roots and namespaces;
- source-head + contract-fingerprint fail-closed binding;
- canonical payload SHA verification on restore;
- complete-stage manifests and atomic persistence;
- no other-replica output read;
- exact A/B SHA plus `numpy.array_equal` comparator with no tolerance rescue;
- exactly 8 outer compute workers when the hardware-matched wrapper is used, nested BLAS/MKL/OpenBLAS/NumExpr threads pinned to 1.

A PASS authorizes only implementation of a **new WW-specific** checkpointed adapter/driver, followed by a separate exact-equivalence/static audit before any home run. It does not authorize direct execution of the Wm driver under modified flags.

Any mismatch in the source evidence is `BLOCKED_EXP073DN_CHECKPOINT_ARCHITECTURE_BINDING` or infrastructure failure, still `+0/+0`.

## Prospective WW requirements after PASS

A future WW-specific implementation must preserve unchanged scientific arithmetic from the frozen Exp073AA WW route:

- reconstruct only S0 count-map authority; no redMaGiC lens input;
- construct one spin-2 field and reuse the exact same field object for S0×S0;
- NaMaster full stock WW component space `[4,39,4,12288]` before selecting `wins[0,:,0,:]`;
- selected semantics `EE<-EE`, canonical `<f8 [39,12288]`;
- dedicated namespaces under `checkpoints/` distinct from all Wm namespaces;
- complete-unit durable checkpointing and fail-closed resume;
- if parallelized, arithmetic/order equivalence to the frozen stock WW route must be prospectively proven exactly before scientific execution.

Only after that implementation/readiness chain passes may a separately preregistered A/B exact-repeatability home gate create `WW_S0_S0` authority.