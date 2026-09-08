# DSIR immutable recovery — V33

Date: 2026-09-08. Scope: **DSIR only**. Never mix RTK or RQIR.

## Preserved scientific authority

Wm_S1 Track-A exact PASS and admitted Wm_S2/Wm_S3 remain preserved. WW admitted authority remains `S0_S0`, `S0_S1`, `S0_S2`, `S0_S3`, `S1_S1`, `S1_S2`, `S1_S3`, `S2_S2`, `S2_S3`, and **`S3_S3`**.

`WW_S3_S3` remains scientifically admitted by hosted recovery-admission run `34218457380`, job `102035691774 SUCCESS`, head `4e5514b6077e1d70537586b43c9b5ca0e51abcf2`, consuming GA artifact `10051382493`, digest `sha256:a192f50de34dc74f575b86e8ff1e6f7c92b9a9bb009d9d0ea6ff4ff6208f4109`. Historical GA recovery failure remains implementation/provenance `+0/+0`, not scientific FAIL.

## V32 HB build block and prospective resolution

V32 correctly classified HB v0.1 as `BLOCKED/IMPLEMENTATION_PLUS_0_PLUS_0`: pinned parent `kaeonikc/class_iv@ac627d54e9ce196a08878d1ba33999819925d19c` had a structural `source/background.c` build defect, and modifying that parent without prospective admission was forbidden.

The repository subsequently prospectively admitted a build-compatible derivative through Exp073HI, without representing it as the unmodified parent:

- Exp073HI prereg blob `030fac1023c1f811c1832cd0ec01060b27a613a7`;
- run `34224810650`, job `102056219075 SUCCESS`, head `8afb6ddc421a996455c861797291e2d4c36f439a`;
- exact token `PASS_EXP073HI_C2_PINNED_UPSTREAM_BUILD_COMPATIBILITY_ADMISSION_V0_1`;
- validated receipt blob `8313779961a6addce71843fe8b101c81fdae3ad1`;
- compatibility script blob `b7fe663154519b605699c1fd622d0079a5f76772`;
- derivative `source/background.c` SHA256 `bc4053922ae984652f5858b2869e7bbbe8682ea502b88e485709e6828e059ce0`;
- derivative `Makefile` SHA256 `2bb326590b3d0c3a23e984fc17cafce680674aa5234db15d35d72a06e1bfa87e`.

This is provenance-preserving build compatibility authority only; it does not change scientific equations or create model authority.

## Exp073HB v0.2 — raw-log validated PASS

Prospective HB v0.2 prereg:

- path `docs/dsir4/prereg/EXP073HB_C2_DIAGNOSTIC_EXACT_ENDPOINT_PRODUCER_BUILD_AUDIT_V0_2.md`;
- Git blob `514232fd1873600772e4eb1f6f59210b8ca6406b`;
- prereg commit `f94c935830f644ad926d2fbd24b608c29ef28eb1`;
- workflow/head commit `506f9ce1a6e066e0ed190e94351f5cc9d51b72a8`;
- run `34225024526`, job `102056923363 SUCCESS`;
- runner: GitHub-hosted `ubuntu-24.04`; no self-hosted/home ownership;
- artifacts: none, as required by this hosted build/static gate.

Raw job log was consumed, not merely workflow status. It verified:

- exact admitted Exp073HI derivative reconstruction and identities;
- producer patcher blob `f3d3d80cda2f937f544722e684a44c649e771487`;
- parent `source/perturbations.c` blob `92a48331658c5941ed4eb43b0e98ee78e39b8385`;
- parent `tools/evolver_ndf15.c` blob `790ced55f2eaa08e805d467734ad1435954bc5b7`;
- patched `source/perturbations.c` SHA256 `da7c427e383f1e9b83d7ff75ef82784c2fe89d91f9681e21e7805b7f354e7e79`;
- patched `tools/evolver_ndf15.c` SHA256 `b3967efaf7a45a3ec6c0144e892caab54f91c595bc726dc1704cfb812f9c0df6`;
- native exact-k mode, literal-z whitelist, `background_tau_of_z`, accepted NDF15 `ynew` terminal endpoint, pre-transform `ppw->delta_m`/`ppw->theta_m`, and exact hexadecimal IEEE-754 diagnostic emission;
- full solver compilation including the patched files and admitted derivative;
- no `./class` cosmological execution and no runtime record/payload creation.

The exact final raw-log boundary is:

`PASS_EXP073HB_C2_DIAGNOSTIC_EXACT_ENDPOINT_PRODUCER_BUILD_AUDIT_V0_2`

with

- `classification=SUPPORT_PLUS_0_PLUS_0`;
- `exp073hi_build_compatible_derivative_verified=true`;
- `diagnostic_producer_compile_verified=true`;
- `cosmological_run_started=false`;
- `record_payload_created=false`;
- `runtime_record_count=0`;
- `prediction_ready=false`;
- `scientific_model_authority_created=false`;
- `G_DOMAIN_MAPPING=NOT_YET_TESTABLE`.

Therefore **Exp073HB v0.2 = PASS / SUPPORT_PLUS_0_PLUS_0**. It is not a C2 scientific PASS and does not create `prediction_ready`.

## Current C2 transition

The V32 build blocker is closed. The already-frozen real-runtime admission boundary is now eligible for implementation/dispatch, subject to exact provenance and live run exclusivity:

- runtime receipt contract: `docs/dsir4/mappings/C2_IDE_RUNTIME_ADMISSION_RECEIPT_CONTRACT_V0_1.md`, blob `1c2e30e6563efe3976ee0b1825dfb250a902a529`;
- its static audit: Exp073GZ, exact token `PASS_EXP073GZ_C2_RUNTIME_ADMISSION_RECEIPT_CONTRACT_STATIC_AUDIT_V0_1`;
- sampling contract: exactly seven z values `[0.295,0.51,0.706,0.934,1.317,1.491,2.33]` times four physical-k values `[0.00067,0.00201,0.0067,0.0201] Mpc^-1`, z-major/k-minor, 28 packets;
- record ABI: eight binary64 fields, 64 bytes/record, exact aggregate 1792 bytes;
- no interpolation, smoothing, averaging, effective-coordinate substitution, tolerance rescue, coordinate repair, reorder, decoding or scientific mapping before raw-record admission.

Recovered immutable tangent provenance remains authoritative: reference `(alpha,beta)=(0,0)`, left-sided alpha base step `-1e-4`, beta central steps `+/-1e-4`, baseline `h=0.67` cosmology and committed p8 precision preset. Any runtime producer must bind the exact chosen frozen model-point identity; it may not invent a new tangent point.

At this V33 snapshot there is no queued/in-progress DSIR Actions run and no self-hosted heavy owner. Real C2 runtime is therefore no longer blocked by heavy-run exclusivity, but scientific interpretation remains forbidden until a complete runtime artifact is terminal-consumed and admitted through the frozen receipt boundary.

## Exact next action

Implement and prospectively freeze a collision-free real C2 producer gate that consumes only the admitted Exp073HI derivative + HB producer identities + frozen GR/GY/GZ contracts, emits raw 64-byte records first, binds run/job/head/artifact/digest and aggregate SHA256, and leaves `decoded=false`, `mapped=false`, `prediction_ready=false`. If self-hosted, it must use durable complete-record/request checkpoints and fail-closed resume; no competing home job is permitted.

Any infrastructure/build/runtime/provenance failure remains `+0/+0` and must be repaired from the first causal failure. Physical branch violations are `OUTSIDE_DOMAIN`. No scientific C2 PASS/FAIL exists at this boundary.

## Global frozen boundaries

Unless prospectively superseded by explicit repository authority: `0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; exact-threshold ambiguity `numerically_unresolved`; no tolerance, rounding, smoothing, averaging, effective ell/z/k or fiducial-P shortcut.
