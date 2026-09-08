# DSIR current-process ledger

Updated: 2026-09-08. Scope: **DSIR only**; RTK/RQIR excluded.

## Preserved authority

Wm_S1 Track-A exact PASS and admitted Wm_S2/Wm_S3 remain preserved. WW admitted authorities remain `S0_S0`, `S0_S1`, `S0_S2`, `S0_S3`, `S1_S1`, `S1_S2`, `S1_S3`, `S2_S2`, `S2_S3`, and **`S3_S3`**. `WW_S3_S3` remains scientifically admitted by hosted recovery-admission run `34218457380`, job `102035691774 SUCCESS`, consuming GA artifact `10051382493`, digest `sha256:a192f50de34dc74f575b86e8ff1e6f7c92b9a9bb009d9d0ea6ff4ff6208f4109`.

Newest immutable recovery authority: `docs/recovery/RECOVERY_2026-09-08_WW_S3_S3_ADMITTED_HB_V0_2_PASS_C2_RUNTIME_AUTHORIZED_V33.md`, creation commit `37acc422c8b3728abedfdd641f9cac9afe232c75`.

## Exp073HI — closed prerequisite

- prereg blob `030fac1023c1f811c1832cd0ec01060b27a613a7`;
- run `34224810650`, job `102056219075 SUCCESS`, head `8afb6ddc421a996455c861797291e2d4c36f439a`;
- exact token `PASS_EXP073HI_C2_PINNED_UPSTREAM_BUILD_COMPATIBILITY_ADMISSION_V0_1`;
- validated receipt blob `8313779961a6addce71843fe8b101c81fdae3ad1`;
- admitted derivative `source/background.c` SHA256 `bc4053922ae984652f5858b2869e7bbbe8682ea502b88e485709e6828e059ce0`;
- admitted derivative `Makefile` SHA256 `2bb326590b3d0c3a23e984fc17cafce680674aa5234db15d35d72a06e1bfa87e`;
- classification `SUPPORT_PLUS_0_PLUS_0`.

The immutable parent remains `kaeonikc/class_iv@ac627d54e9ce196a08878d1ba33999819925d19c`; the derivative is separately provenance-bound and must never be represented as unmodified parent source.

## Exp073HB v0.2 — terminal consumed PASS

- prereg `docs/dsir4/prereg/EXP073HB_C2_DIAGNOSTIC_EXACT_ENDPOINT_PRODUCER_BUILD_AUDIT_V0_2.md`, blob `514232fd1873600772e4eb1f6f59210b8ca6406b`;
- workflow/head commit `506f9ce1a6e066e0ed190e94351f5cc9d51b72a8`;
- run `34225024526`, job `102056923363 SUCCESS`;
- runner ownership: GitHub-hosted only; self-hosted heavy owner **none**;
- exact raw-log token `PASS_EXP073HB_C2_DIAGNOSTIC_EXACT_ENDPOINT_PRODUCER_BUILD_AUDIT_V0_2`;
- `classification=SUPPORT_PLUS_0_PLUS_0`;
- producer patch blob `f3d3d80cda2f937f544722e684a44c649e771487`;
- patched `source/perturbations.c` SHA256 `da7c427e383f1e9b83d7ff75ef82784c2fe89d91f9681e21e7805b7f354e7e79`;
- patched `tools/evolver_ndf15.c` SHA256 `b3967efaf7a45a3ec6c0144e892caab54f91c595bc726dc1704cfb812f9c0df6`;
- full solver compile verified;
- artifacts none, as required;
- `cosmological_run_started=false`, `record_payload_created=false`, `runtime_record_count=0`, `prediction_ready=false`, `scientific_model_authority_created=false`, `G_DOMAIN_MAPPING=NOT_YET_TESTABLE`.

HB v0.2 closes the V32 build blocker prospectively. It is support-only, not a C2 scientific PASS.

## Live process state

Latest Actions reconciliation: **0 queued, 0 in-progress** DSIR runs. No competing home-heavy process; runner ownership is **none**.

## Exact next permitted transition — real C2 runtime producer

The already-frozen runtime admission boundary is now eligible for implementation/dispatch:

- receipt contract `docs/dsir4/mappings/C2_IDE_RUNTIME_ADMISSION_RECEIPT_CONTRACT_V0_1.md`, blob `1c2e30e6563efe3976ee0b1825dfb250a902a529`;
- exact 7 z x 4 physical-k grid = 28 requests, ordering `z-major/k-minor`;
- z `[0.295,0.51,0.706,0.934,1.317,1.491,2.33]`;
- k `[0.00067,0.00201,0.0067,0.0201] Mpc^-1`;
- 64 bytes/record, eight binary64 fields, aggregate exactly 1792 bytes;
- raw records before decoding/mapping; `decoded=false`, `mapped=false`, `prediction_ready=false` at admission;
- exact producer run/job/head/artifact/digest/aggregate-SHA binding required;
- recovered tangent provenance is fixed: reference `(alpha,beta)=(0,0)`, alpha base direction `-1e-4`, beta `+/-1e-4`, baseline `h=0.67` cosmology and frozen p8 precision.

Current state: **READY_FOR_PROSPECTIVE_RUNTIME_PRODUCER_IMPLEMENTATION**. No producer run is active yet because the collision-free runtime workflow and exact per-model-point runtime command/artifact binding are not yet committed. This is implementation work, not scientific BLOCKED/FAIL.

SUCCESS: consume terminal raw artifact and admit only after exact coordinate/order/count/byte/SHA/provenance checks, without decoding. FAIL: diagnose first causal infrastructure/runtime/provenance error; preserve complete durable request/record checkpoints if self-hosted; never alter frozen science.

## Frozen boundaries

Unless prospectively superseded by repository authority: `0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; exact-threshold ambiguity `numerically_unresolved`; no tolerance, rounding, smoothing, averaging, effective ell/z/k or fiducial-P shortcut.
