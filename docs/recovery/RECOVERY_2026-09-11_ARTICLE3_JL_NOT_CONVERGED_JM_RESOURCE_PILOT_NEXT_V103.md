# DSIR Article III recovery — recovered JL independently verified NOT_CONVERGED; JM branch active, 8193 resource pilot next V103

Updated: 2026-09-11. Scope: **DSIR only**. Never mix RTK or RQIR.

## Preserved scientific authority

Exp073IR remains `NUMERICALLY_UNRESOLVED_EXP073IR`; Exp073JI support remains feasible. Exp073JJ/JK remain support-only NOT_CONVERGED at `0.037280144773915974` / `0.016330535730270664`. Covariance restriction remains unauthorized and Wm_S3 remains unopened.

## Recovered Exp073JL terminal result — independently verified

Recovered JL retry workflow/run/job `exp073jl-article3-canonical-one-live-recovered-third-refinement-v0-2 / 34544293038 / 103093458667`, head `417ec30eb0acd2896068f7ed3d5eeb3d47cedbbf`, completed SUCCESS after the packaging-only request-plan repair. Terminal artifact `10178796851` was independently downloaded and verified: ZIP SHA256 `08e8b55c4c23374fc5e92e730e01c693a0aa2e8734d65bf3c38782a1bab16bab`; `result.json` SHA256 `b3798bbc83e6bbc070c02fba691813fe3de9d4fcc33de38a32c086b7e50c8478`; `capacity_patch.json` SHA256 `e1af249ccdfd393b9b0f1020ffa1b70d953fa457ca2212aa3ab29be01f74b66a`.

Frozen terminal classification is exactly:

`COMMON_GRID_THIRD_REFINEMENT_NOT_CONVERGED_PLUS_0_PLUS_0`.

Observed maximum atomic coarse-vs-fine relative component difference is `0.012273497268380687`, which is `12.273497268380687 ×` the strict `1e-3` threshold. This is a valid numerical-support NOT_CONVERGED outcome, not infrastructure failure.

All structural/provenance conditions are clean: finite/nonzero status unchanged; row labels unchanged; BOSS dense-z disagreement false; invalid rows 0 / invalid-row fraction 0.0; retained after Layer-B 107; unsupported target evaluations 0; max requested-node lookup mismatch `1.6559173278185046e-16`; exactly 8 solver constructions; `max_live_instances=1`; final live count zero; total transfer calls 4040; raw operand cross-process combination false; canonical 2049/4097 node/text identities exact; response-blind coarse/fine plan hashes exact; parent identity preserved.

Previous JK maximum was `0.016330535730270664`; empirical reduction factor JK/JL is `1.3305527652938685`. This diagnostic does not alter the deterministic next rung.

Durable recovered-JL terminal authority: `docs/dsir4/authority/EXP073JL_ARTICLE3_RECOVERED_CANONICAL_ONE_LIVE_THIRD_REFINEMENT_NOT_CONVERGED_V0_2.json`, creation commit `b16c28f02a6449e36e4a7bc74f6080e32c8c9df5`, Git blob `aca79d6596f49ced9fe9d965059a2352447f13b4`.

Exp073JL remains support-only `+0/+0`: it creates no scientific Layer-B authority, does not authorize covariance restriction and does not open Wm_S3.

## Branch selection is now fixed

The prospectively frozen conditional branch rule now selects **Exp073JM only** because JL is independently verified NOT_CONVERGED. Exp073JN is not activated and must not run for this JL outcome.

The deterministic refinement-ladder standard, frozen before the JL verdict, fixes JM to the immediately next rung: base 4096 -> 8192, guarded requested nodes 4097 -> 8193. No density may be chosen using the observed JL maximum.

## JM response-blind preparation already complete

JM recovered execution alignment was frozen before the JL verdict. It removes the historical extra activation predicates, consumes canonical byte streams instead of runtime-regenerated `geomspace`, and preserves the original JM scientific contract while using the recovered role-major one-live execution architecture.

Canonical coarse for JM is the existing authoritative JL 4097 lattice: decoded SHA256 `f30556be2547732ed0b87b56368e01e46504a975f94fcbbc5e7bc8cfc525e5eb`, text/u64hex SHA256 `290075f777c88964aa6b670694063e9b4ad0d5d4dcb16ee12adad5103ca1b6c7`.

Canonical fine 8193 was materialized response-blind before the JL verdict. Six of eight independent replicas first reproduced the authoritative 4097 anchor and all six emitted byte-identical 8193 candidates. Committed 8193 decoded SHA256 `6d35a9d79aa8826554e8e39315ab12a8be1675d32d25a86ec04c978c7723a515`; text/u64hex SHA256 `90b9aee9e01784a4af89ab0aa1bd5cbf1e95061f2d412d7a0e1b8ee5332ba7d6`. Canonical materialization commit `944619861bd2630431d8693615919820067cd1f0`.

Host-side regeneration is explicitly forbidden: the response-blind audit observed a non-authoritative host variant differing from the canonical 8193 candidate at 2275/8193 nodes, exactly one binary64 ULP each, even under nominally matching NumPy 1.26.4 environments.

Recovered JM helper `ci/exp073jm_article3_recovered_canonical_one_live_fourth_refinement_v0_2.py`, implementation commit `0acfa1f00516a055795335c372845f51961ad797`, Git blob `4ba4868d751b95b97b2ac7f18701f5349e70c950`. It preserves the original JM estimator, `h=1e-4`, strict `REL_TOL=1e-3`, native kpd20, exact response-blind 441 coarse + 569 fine calls/role, same Exp073IR 107-row accounting, GL64 direct comparison and fine-only GL128 stability control, while scheduling exactly 8 role-major CLASS constructions with max one live.

No-science JM recovered static audit run/job `34545274582 / 103096420233` is independently verified 41/41 PASS; artifact `10178767490`, ZIP SHA256 `01c26c1a5586b964f395d3f1ab589bcfd100c518a653f136d9782428b39791d8`, result SHA256 `d265f98ff74b30917ced73e7ca2523fef19e28306c0e21bfed6f32e2faaf0eef`. Durable authority creation commit `1a1ccbd179fd6c8bd4a2cb3c589e57d21aad49a4`.

## Mandatory next gate — canonical 8193 resource-only pilot

Full JM science MUST NOT launch yet. The recovered JM alignment prospectively requires a dedicated resource-only pilot because Exp073JW established the one-live lifecycle only through canonical 4097, not canonical 8193.

The new pilot must mirror the already-validated JW resource protocol and change only what the pre-frozen JM rung requires:

- exact canonical 8193 u64hex byte stream and its independently verified authority;
- pinned CLASS-IV commit `ac627d54e9ce196a08878d1ba33999819925d19c`;
- JM infrastructure-only capacities `_MAX_NUMBER_OF_K_FILES_=9216`, `_ARGUMENT_LENGTH_MAX_=262144`;
- native `k_per_decade_for_pk=20`;
- fixed JW pilot request set, frozen before JM/JL science: request A at binary64 z `float.fromhex('0x1.3851eb851eb85p-1')` with k `[0.0013,0.0047,0.013,0.041]`, request B at binary64 z `float.fromhex('0x1.1c28f5c28f5c3p+0')` with k `[0.0019,0.0073,0.021,0.057]`;
- exactly four sequential 8193-lattice model-role CLASS constructions in order `reference, alpha_minus, beta_plus, beta_minus`;
- max one live solver;
- finite transfer/pilot response arrays;
- zero unsupported requested targets;
- requested-node lookup mismatch `<=1e-12`;
- no full 107-row JM traversal and no JM convergence classification.

Resource-pilot PASS is process authority `+0/+0` only. It cannot alter the canonical grid, tolerance, estimator or branch.

## Stable readiness telemetry

**ARTICLE3_REPOSITORY_READINESS: 68%.** Funnel-freeze readiness: **67%**. A valid JL NOT_CONVERGED result advances the process branch but does not close Layer-B scientific support, so these percentages remain unchanged pending a valid converged support rung and subsequent fresh science-authorizing closure.

## Exact next action

Prospectively freeze and statically audit the JM canonical-8193 resource-only pilot against the existing JW pilot request set. Perform a fresh anti-duplication check. If clean, launch exactly one 8193 resource pilot. Only an independently verified pilot PASS may authorize the full recovered JM 4097->8193 production convergence run. No JN execution, no tolerance/grid/science rescue.
