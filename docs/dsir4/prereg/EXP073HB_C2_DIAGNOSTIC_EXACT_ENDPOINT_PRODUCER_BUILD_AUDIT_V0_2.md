# Exp073HB — C2 diagnostic exact-endpoint producer build audit v0.2

Status: **PROSPECTIVELY FROZEN BEFORE V0.2 EXECUTION**. Scope: DSIR only.

## Authority chain

This gate supersedes HB v0.1 for future execution only. It does not rewrite historical HB runs.

Required prerequisite authority is the raw-log validated Exp073HI build-compatible derivative admission:

- Exp073HI prereg blob `030fac1023c1f811c1832cd0ec01060b27a613a7`;
- Exp073HI run `34224810650`, job `102056219075 SUCCESS`, head `8afb6ddc421a996455c861797291e2d4c36f439a`;
- exact PASS `PASS_EXP073HI_C2_PINNED_UPSTREAM_BUILD_COMPATIBILITY_ADMISSION_V0_1`;
- validated receipt `docs/dsir4/results/EXP073HI_C2_PINNED_UPSTREAM_BUILD_COMPATIBILITY_ADMISSION_RECEIPT_V0_1.md`, Git blob `8313779961a6addce71843fe8b101c81fdae3ad1`;
- compatibility script Git blob `b7fe663154519b605699c1fd622d0079a5f76772`;
- admitted derivative `source/background.c` SHA256 `bc4053922ae984652f5858b2869e7bbbe8682ea502b88e485709e6828e059ce0`;
- admitted derivative `Makefile` SHA256 `2bb326590b3d0c3a23e984fc17cafce680674aa5234db15d35d72a06e1bfa87e`.

The immutable parent remains `kaeonikc/class_iv@ac627d54e9ce196a08878d1ba33999819925d19c`; the derivative must never be represented as the unmodified parent.

## Frozen producer implementation

- producer patcher: `scripts/dsir4/exp073hb_c2_exact_endpoint_producer_patch_v0_1.py`;
- producer patcher Git blob: `f3d3d80cda2f937f544722e684a44c649e771487`;
- parent `source/perturbations.c` Git blob: `92a48331658c5941ed4eb43b0e98ee78e39b8385`;
- parent `tools/evolver_ndf15.c` Git blob: `790ced55f2eaa08e805d467734ad1435954bc5b7`;
- patched `source/perturbations.c` SHA256: `da7c427e383f1e9b83d7ff75ef82784c2fe89d91f9681e21e7805b7f354e7e79`;
- patched `tools/evolver_ndf15.c` SHA256: `b3967efaf7a45a3ec6c0144e892caab54f91c595bc726dc1704cfb812f9c0df6`.

These producer hashes were frozen from the deterministic implementation before this v0.2 execution; no cosmological numerical result is involved.

## Frozen diagnostic semantics

The diagnostic path must be opt-in only. With `DSIR_C2_EXACT_Z` absent, ordinary solver behavior is unchanged.

When armed, the code must:

1. require single-thread diagnostic execution (`OMP_NUM_THREADS=1`);
2. require exactly one native `k_output_values` request and act only on its native `index_k_output_values` mode;
3. accept only literal z in `{0.295,0.51,0.706,0.934,1.317,1.491,2.33}`;
4. resolve z to endpoint conformal time only through native `background_tau_of_z`;
5. terminate that native perturbation mode at the exact literal-z endpoint;
6. commit only from an accepted NDF15 terminal state `ynew` at `tnew=tfinal`;
7. capture native current-gauge `ppw->delta_m` and `ppw->theta_m` immediately after their native construction and before downstream gauge-invariant/source transforms;
8. not use `perturb_sources_at_tau`, `interp_from_dif`, effective z/k, tolerance, rounding, smoothing, averaging, or interpolation as the raw C2 state authority;
9. emit exact hexadecimal IEEE-754 text for the diagnostic observation; serialization into the frozen C2 binary record remains the responsibility of a later runtime gate.

## V0.2 hosted checks

The workflow must reconstruct the derivative from the exact parent plus the admitted Exp073HI compatibility transform, verify all derivative identities, apply the frozen producer patch, verify patched hashes and exact semantics, install the hosted GSL build dependency, and compile the full solver.

It must **not execute `./class`**. It must create no cosmological result, no runtime C2 record, and no 28-record/1792-byte payload.

## Frozen PASS and ceiling

Only exact raw-log token:

`PASS_EXP073HB_C2_DIAGNOSTIC_EXACT_ENDPOINT_PRODUCER_BUILD_AUDIT_V0_2`

with all of:

- `classification=SUPPORT_PLUS_0_PLUS_0`
- `exp073hi_build_compatible_derivative_verified=true`
- `diagnostic_producer_compile_verified=true`
- `cosmological_run_started=false`
- `record_payload_created=false`
- `runtime_record_count=0`
- `prediction_ready=false`
- `scientific_model_authority_created=false`
- `G_DOMAIN_MAPPING=NOT_YET_TESTABLE`

is HB v0.2 PASS.

Workflow success or compile success alone is insufficient. Any identity/hash/static/build mismatch is implementation/infrastructure `+0/+0`.

## Consequence

Only after raw-log validated HB v0.2 PASS may the repository consider dispatching the already frozen real C2 runtime/receipt contract. That runtime must independently satisfy live heavy-run exclusivity, exact provenance, durable checkpoint/resume if self-hosted, and its own frozen record/payload admission rules.
