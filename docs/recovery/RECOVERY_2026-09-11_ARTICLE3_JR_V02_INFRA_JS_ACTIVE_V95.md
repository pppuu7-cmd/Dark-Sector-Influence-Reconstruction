# DSIR recovery V95 — JR v0.2 terminal infrastructure-invalid; source isolation audited; JS active

Date: 2026-09-11. Scope: DSIR only.

## Preserved science

Exp073IR remains `NUMERICALLY_UNRESOLVED_EXP073IR`; Exp073JI support remains feasible; Exp073JJ/JK remain valid support-only NOT_CONVERGED with maxima `0.037280144773915974` and `0.016330535730270664`. Frozen Exp073JL remains the unchanged 2049->4097 guarded shared-grid convergence test with `REL_TOL=1e-3`, `h=1e-4`, native kpd20, centered-cubic interpolation, exact domain/masks/107-row traversal/accounting and anti-rescue rules. Covariance restriction remains unauthorized; Wm_S3 remains unopened.

Exp073JQ remains independently verified same-run history-independent for all four finite-difference roles, durable authority commit `3bdba4626ab12994c9d27a16a4446fd2bf79512b`. JR v0.1 coarse-2049 remains independently verified direct four-live-vs-sequential exact PASS, durable partial receipt commit `208980760b7008798700d16037e81497ab3dc1c4`.

## JR v0.2 terminal

Corrected run `34534521584`, head `a4b60431977fc2ee87dfd87e1c8e4f74cd04322d`, is terminal. All four fine-4097 model jobs passed frozen identity, stack and exact pinned CLASS-IV build, then terminated during the numerical four-live-context control before writing any model receipt:

- beta_minus `103062907332`: external runner shutdown, no result;
- beta_plus `103062907633`: external runner shutdown, no result;
- reference `103062907728`: external runner shutdown / exit 143, no result;
- alpha_minus `103062907742`: external runner shutdown at `2026-09-10T22:01:50Z`, no result.

Aggregate job `103065497724` correctly found zero fine receipts and emitted `INVALID_INFRA_PLUS_0_PLUS_0`; artifact `10175154654`, independently verified ZIP SHA256 `c4905bf5429ea17d677f3e1303d08d25596579d5495a964690c30f447707aacf`, result JSON SHA256 `981dfb43778b741df2de8043c387c03e3ee8b7140f4e7324774a12d011623ab9`. `recovered_JL_preregistration_permitted=false`. No numerical NOT_EXACT result exists. Do not blindly rerun the same four-live fine architecture on the same hosted runner class.

Hosted peak-resource audit: `docs/dsir4/audits/EXP073JR_FINE4097_HOSTED_PEAK_RESOURCE_AUDIT_V0_1.md`, commit `0113262e3e093eb7805edb31de1e9948bd8ab40a`. It deliberately does not claim OOM without direct telemetry; it records repeated execution-feasibility failure associated with the four-live 4097 context.

## Pinned source instance-locality audit

`docs/dsir4/audits/CLASSIV_C2_INSTANCE_LOCALITY_SOURCE_AUDIT_V0_1.md`, commit `02bfefb9e04b837e8f04350d533be46331197a78`, blob `f4c9b7b241f22985b2c38bc3dcae8f9fda07267a`.

Pinned `python/classy.pyx` owns the principal solver structs per `Class` instance and passes pointers to those instance fields into the C modules. A real file-scope mutable `work_rom` was identified in the fork, but its allocation/use/free is conditional on `fluid_equation_of_state==IDM_IV`. Frozen C2 does not provide that parameter; pinned defaults set `CLP`, and `f_idm_iv=1`/`f_iv=1` alter interacting densities without switching the enum. Therefore this specific global workspace branch is inactive for frozen C2. This is a narrow source conclusion, not an explanation for runner shutdown.

## Exp073JS active

Prospective JS prereg `docs/dsir4/prereg/EXP073JS_ARTICLE3_FINE4097_CROSS_MODEL_LIFECYCLE_ISOLATION_V0_1.md`, commit `c10afa7a392354722f7467cc90de777e30517cce`, blob `73bac6764a62f3de6cbf2c7fec3fa987fb648ecc`. Helper `ci/exp073js_article3_fine4097_cross_model_lifecycle_isolation_v0_1.py`, commit `25cd585f4b09c09a762a50ad39841ad5733f66f0`, blob `70a38a45d6d743878e1b5d8a8c2d14630bf3ee80`.

JS uses one live CLASS instance at a time. Per selected role it evaluates selected-before, then each of the other three roles sequentially, then selected-after, and requires exact array/SHA equality of selected-before/after for both frozen A/B requests, zero unsupported targets and lookup <=1e-12. It tests residual cross-model lifecycle contamination at fine 4097 and does not create science authority.

Initial JS run `34535627564`, head `b2ebbe5719500d550a50e2c9d6835da17eaa340f`, is pure infrastructure-invalid: an incorrect JQ authority blob in the workflow caused all four jobs to fail the identity guard; numerical steps were skipped. The JQ blob was corrected before any JS numerical output to actual `a1c29c4ead5daee53a6fe82bc2b77a363a38b7a7` in workflow/head commit `7676f64e811520e96a09b76c35c2bf3d49b0cf01`.

Corrected run `34535674581` is the sole authoritative JS run. At this recovery write all four jobs have passed identity guards and are in stack/build preparation. Do not duplicate it.

## Stable readiness

Article III repository readiness: **68%**.
Overall DSIR funnel readiness for methodology freeze: **67%**.

Process/source/diagnostic work alone does not increase scores.

## Exact next action

Terminal-consume corrected JS run `34535674581`; independently verify every available model receipt and aggregate. If and only if all four roles validly PASS exact lifecycle isolation, perform the separately required prospective sequential-execution authorization audit over the fixed evidence bundle (JR coarse direct exact PASS + JQ fine repeat/history exact PASS + pinned source audit + JS fine lifecycle PASS). Only a valid authorization may then preregister a one-live fixed-chunk execution of unchanged Exp073JL. JS numerical FAIL forbids that route; JS infrastructure invalidity permits only minimal infrastructure repair. No tolerance/grid/science rescue.