# DSIR recovery V93 — JR v0.1 coarse exact PASS, fine infra shutdown; JR v0.2 active

Date: 2026-09-11. Scope: DSIR only.

## Preserved science

Exp073IR remains `NUMERICALLY_UNRESOLVED_EXP073IR`; Exp073JI support remains feasible; Exp073JJ/JK remain valid support-only NOT_CONVERGED at `0.037280144773915974` / `0.016330535730270664`. The frozen Exp073JL science remains 2049->4097 guarded shared-grid comparison with `REL_TOL=1e-3`, `h=1e-4`, native kpd20, centered-cubic interpolation, unchanged 107-row parent/traversal/support/accounting and no rescue. Covariance restriction remains unauthorized; Wm_S3 remains unopened.

## Exp073JR v0.1 terminal classification

Run `34533562950`, head `7613953cff71fd26cb9b73e7148a4d6c7aa87895`.

Coarse job `103059792169` is a valid exact process PASS. Artifact `10174738651`, independently verified ZIP SHA256 `22f88a9559ace2bf2701c22c93595851ae1112362ffea0f80b18465e804f1b91`, result JSON SHA256 `f7e9e6eabbc7bb7668c313962fb0ecf0db048ebf51d94a09ca2662b57bdbd5f5`. Classification `SAME_RUN_SEQUENTIAL_RESPONSE_ENGINE_EXACT_EQUIVALENCE_PASS_PLUS_0_PLUS_0`. Both frozen A/B requests have exact array and byte-SHA equality, max abs/rel difference 0.0, unsupported 0, max requested-node mismatch `1.6531028205966003e-16`. Durable partial coarse receipt commit `208980760b7008798700d16037e81497ab3dc1c4`, blob `ee6526bd80daeac7990b2244b8ec2c8061a534c4`.

Fine job `103059792478` passed identity/stack/pinned-build checks, entered the frozen numerical step at `2026-09-10T21:42:32Z`, and at `21:48:05Z` the hosted runner reported `The runner has received a shutdown signal`; no numerical equality verdict/result artifact existed. Therefore fine v0.1 is `INVALID_INFRA_PLUS_0_PLUS_0`, not NOT_EXACT/scientific failure.

Aggregate artifact `10174743859`, ZIP SHA256 `a15a19f9a154467ecb60162f0cbf9c048a0550fa0853da5eb63ad20d34048481`, correctly classified combined v0.1 `INVALID_INFRA_PLUS_0_PLUS_0` because only one of two lattice receipts existed. Coarse PASS remains durable and must not be recomputed merely to repair fine.

## Fine repair theorem and v0.2 frozen contract

Response-blind model-operand decomposition note `docs/dsir4/methods/LAYERB_JR_MODEL_OPERAND_EQUIVALENCE_DECOMPOSITION_V0_1.md`, commit `0c9ce810198b073dbd2c35c2354043fc2b3e6635`, blob `ef6abdb3df51091b3ba99d4f3ab07334f14a21fa`, proves that exact equality of each of the four target-vector operands between original four-live context and candidate single-live context implies exact equality of the unchanged final response formula.

JR v0.2 fine-only prereg `docs/dsir4/prereg/EXP073JR_ARTICLE3_FINE4097_MODEL_OPERAND_EXACT_EQUIVALENCE_V0_2.md`, commit `53d6a1bff91ec1a1d69a920411a8a143adeec490`, blob `edaffcf8cd07817cba2bfd48791e752fcf02c5ab`, was frozen before v0.2 numerical output. Helper `ci/exp073jr_article3_fine4097_model_operand_exact_equivalence_v0_2.py`, commit `5fdd346b4439de9c3b82c84946591001fe142a2f`, blob `47e53f6ce429b94df25c2981dc81392c6834c957`.

Each of four model-role jobs constructs all four original reference instances live, queries only its selected role at frozen A/B, destroys them, constructs the same role single-live, and requires exact array/byte equality plus unchanged support/lookup guards. Four PASS receipts plus the durable coarse receipt imply combined JR exact PASS by the frozen operand theorem. No raw operands are combined across jobs.

## v0.2 infrastructure history and active corrected run

Initial workflow creation head `5bcbf1612f8a59ace4354cedc7e3a13e9caa24b6` triggered run `34534466782`. A workflow-only identity guard accidentally compared the decomposition blob to a literal command-substitution string. All four model jobs failed at `Enforce frozen JR v0.2 identities`; install/build/numerical steps were skipped. This run is `INVALID_INFRA_PLUS_0_PLUS_0` with no numerical content.

The guard was corrected before any v0.2 numerical result by binding the real decomposition blob `ef6abdb3df51091b3ba99d4f3ab07334f14a21fa`. Corrected workflow/head commit `a4b60431977fc2ee87dfd87e1c8e4f74cd04322d`, workflow content blob `7d17483e49394255b77927861a767626f5d107d8`. Corrected run `34534521584` is the sole authoritative active v0.2 run. At this recovery write all four jobs have passed identity, frozen stack and exact pinned CLASS-IV build and are inside `Execute fine-4097 model-operand exact control`:
- beta_minus job `103062907332`
- beta_plus job `103062907633`
- reference job `103062907728`
- alpha_minus job `103062907742`

Do not duplicate this run.

## Other response-blind process safeguards

Atomic recovery topology commit `1d98a555b412ef65ff88f6d98736a67690bb2283`; chunk-reduction associativity proof commit `b2108eee838e3da132310ee7db61583a7fe48a61`; inactive JM activation-alignment audit commit `259cedfa58032aab9db0a11bfe01739cfec23cdc`. These remain support/process `+0/+0`.

## Stable readiness

Article III repository readiness: **68%**.
Overall DSIR funnel readiness for methodology freeze: **67%**.

No process/diagnostic repair changes these scores.

## Exact next action

Terminal-consume corrected JR v0.2 run `34534521584`. Independently verify all available model artifacts and aggregate. Only a valid 4/4 fine exact PASS combined with durable coarse v0.1 PASS permits prospective registration of a full fixed-chunk same-run execution of unchanged Exp073JL. Any valid model inequality forbids sequential architecture. Missing/cancelled/invalid receipt permits only minimal infrastructure repair. No tolerance/grid/science rescue.