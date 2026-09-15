# DSIR independent funnel audit — V0.26 response-blind static candidate audit V0.1

Date: 2026-09-15. Scope: DSIR only. Effect: `+0/+0`.

## Reviewed object

This review concerns the prospective V0.26 candidate on branch `research/v026-full-layerb-prereg`, branch head `ed67dade1fb08873ec3807a9513a55a725527fe6`, and specifically the hosted response-blind static audit executed from head `20eb0f8db1bc4d426fd957dbed6a1211a0459f10`.

The candidate is not on `main` and is explicitly non-executable. The current terminal scientific/numerical authority on `main` remains the V0.25 provenance correction, which authorizes only prospective definition/freeze of `PROSPECTIVELY_FROZEN_FORCED_BASELINE_EXACT_TARGET_UNION_FULL_LAYERB_NUMERICAL_REPLAY_AUDIT` and does not authorize a 107-row science run.

## Authorization and chronology

The candidate preregistration was created first at commit `8fc1a9d8dc908309f956e2295e934639730d3796`; the machine-readable candidate contract followed at `2cf8c2fa3ee24c29c77026e8dd022b67a00cfa14`; the response-blind static auditor at `da18cff9982d7ef91f13caa7a46a388295cd5207`; the hardening amendment at `54c7a6c32d04cf498df6cd9a79e1bc04b8ad2c90`; and the response-blind runtime correction at `e6b5e622e27ff8fde0820cbf0f731fd0c3751cd3`. All precede the hosted static-audit workflow creation/launch commit `20eb0f8db1bc4d426fd957dbed6a1211a0459f10`.

No V0.26 CLASS solve or scientific response was used to make those corrections. The runtime correction prospectively separates alpha and beta perturbation tolerances: alpha inherits the canonical 32769 production route with `tol_perturb_integration=3e-10`; beta exact-target pure/mixed/direct paths use `1e-12`; both preserve sampling `0.00035`. The older global `1e-12` statement is therefore not a main-ready immutable specification and must not be silently interpreted as still active.

## Executed code and input identity

The hosted workflow is `.github/workflows/layerb-beta-v026-response-blind-static-audit-v0-1.yml`, git blob `2e98239ef9137f2d89bccc99150860fb0e30dd4c`. It checks out the exact candidate head, pins NumPy `1.26.4`, downloads request-plan artifact `10298655751`, verifies the artifact ZIP SHA256 `9b8bdcf03cb05bc979e8c72135acac92232864a74dc1d510b579d8efb5cbb2a7`, verifies `plan.json` byte length `3953984` and SHA256 `c12bdb2a407de3f9e2c0c410719ae604d9b3516dabb76c9b1598340418ee8064`, executes the frozen auditor, and uploads a receipt.

The executed auditor `ci/layerb_beta_v026_response_blind_static_audit_v0_1.py` has git blob `8a8195de8539f6408445933e898d62f004f26edc`, exactly the blob bound by the hardening amendment. Inspection confirms that it reads only the exact response-blind request plan and reconstructs target sets, guarded GRID896 geometry, deterministic mixed/direct packing, parser-capacity bounds, sentinel identities, and shard counts. It does not invoke CLASS and does not read scientific responses, covariance, whitening, nuisance objects, relation-null objects, `Wm_S3`, or global 65537 material.

The exact source-plan artifact was independently downloaded. Its ZIP SHA256 is `9b8bdcf03cb05bc979e8c72135acac92232864a74dc1d510b579d8efb5cbb2a7`; it contains exactly `plan.json`, `3953984` bytes, SHA256 `c12bdb2a407de3f9e2c0c410719ae604d9b3516dabb76c9b1598340418ee8064`. The source plan contains request geometry rather than scientific responses. Its originating Actions run `34695347893` is globally failed, but the `materialize-plan` job `103557768867` was terminal success and produced artifact `10298655751` before the later failed/cancelled science jobs. This source-plan use is therefore scoped to the successful response-blind materialization job, not to any claim that the parent run was terminal-success science.

## Hosted Actions and provenance

Actions run `34952288638` is the unique push run for head `20eb0f8db1bc4d426fd957dbed6a1211a0459f10`: run number 1, attempt 1, terminal `success`. Exactly one job, `static-audit` id `104325850674`, is terminal success and all of its steps completed successfully.

The run produced exactly one artifact: id `10389832162`, name `layerb-beta-v026-response-blind-static-audit-v0-1`, GitHub digest `sha256:8fce87986b0e96356fdc6935df0f16470b224d10caa371db3fe644929d4616b3`. Independent download reproduced that ZIP SHA256 exactly. The ZIP contains:

- `v026_static_audit.json`: 2924 bytes, SHA256 `718a1ba3be7ce14527e8995bff174c9f53e540a0e5f74008cff0bc1e687acbcd`;
- `v026_static_audit.sha256`: 100 bytes, SHA256 `122059ebda50101d55ecd594bbcf39a9ee24bea7c0e71db4dd48388a029dd1e6`, correctly binding the JSON hash.

The receipt records `PASS_LAYERB_BETA_V0_26_RESPONSE_BLIND_STATIC_AUDIT`, `class_solver_invoked=false`, `scientific_response_read=false`, and `covariance_read=false`.

## Independent reconstruction and counterexample

Independent reconstruction from the exact plan confirms the core response-blind geometry:

- 377 DES production calls, 64,658 unique DES target-k values, zero cross-call target overlap, 90–244 unique targets per DES call;
- 64 BOSS GL64 calls and 128 fine-only BOSS GL128 calls sharing one 99-k target set, with no DES/BOSS target overlap;
- guarded GRID896 geometry requiring 0 lower and 1 upper guard, hence 897 common nodes, with zero exact target/common-node overlap;
- deterministic mixed packing: 301 total batches, 77 DES pairs + 223 DES singletons + one BOSS batch, canonical SHA256 `59abce49f6338c30b93d11fa462e1ff8642615d6100d23feca4b36505a5cef85`;
- deterministic target-only direct packing: 59 batches, canonical SHA256 `1c98927960e81d7fb55ebc687ef36059d964b233001551dba2aa9a01652c8864`;
- frozen sentinel identities M076 `[76,78]` -> D50, M298 `[375]` -> D00, M300 BOSS `[377..440]` -> D58; each mixed target set is contained in its frozen direct comparator target set;
- mixed/direct shard counts match the candidate contract.

However, the hosted pinned-NumPy receipt exposes a concrete discrepancy that the PASS implementation does not gate. The preregistration and base candidate contract state maximum mixed `.17g` payload `25062` bytes at M013. The hosted static audit under the prospectively frozen NumPy `1.26.4` records **`25063`** bytes at M013. The direct maximum remains `24262` bytes at D20.

This is not a parser-capacity failure: `25063 < 32768` by a wide margin. It is nevertheless a frozen-specification mismatch. The static auditor only checks that payload size is below the parser capacity; it does not assert equality to the candidate's frozen maximum. Therefore the hosted PASS token cannot be interpreted as proof that every frozen static scalar reproduced exactly.

A causal numerical control strengthens this qualification. Re-executing the same response-blind reconstruction with NumPy `2.3.5` produces M013 maximum `25062` and a complete output SHA256 `d55cb61f2cd5338dba0b36df656409fdc248afe3cfa1972fe060b3a09b09c515` — exactly the non-authoritative local-precommit hash recorded in the hardening amendment. The hosted run, which correctly pins NumPy `1.26.4`, produces the different authoritative JSON hash `718a1ba3...` and M013 size `25063`. Direct packing is unchanged because it contains no NumPy-generated GRID896 common lattice. This is an explicit environment-sensitive witness in the generated common-grid representation/serialization, not a scientific response effect.

Consequently, a consolidated R1 specification must not carry forward the unqualified `25062` value. It should freeze the intended NumPy-1.26.4 GRID896 representation more strongly, preferably with an exact canonical binary64/u64hex node-payload hash or equivalent immutable node identity, and must define and assert the payload-byte counting convention. The static auditor must assert the R1 expected maximum rather than only the loose `<32768` capacity condition.

## Stale branch observation

The latest branch note, commit `ed67dade1fb08873ec3807a9513a55a725527fe6`, records `NO_RUN_CREATED_FROM_RESEARCH_BRANCH_WORKFLOW_CREATION_PUSH` and `observed_workflow_run_count=0`. Actions is authoritative over that race-prone observation: run `34952288638` was created at 2026-09-15T09:23:21Z and completed at 09:23:39Z, while the note commit was timestamped 09:23:37Z. A fresh query for push runs at the exact head returns total count 1. The branch note is therefore stale and must be superseded for workflow-registration/provenance bookkeeping. This does not alter a scientific result because no scientific response was read.

## Interpretation ceiling and gate consequence

The hosted receipt confirms a substantial but narrow result: the exact source-plan bytes are recoverable; the principal response-blind target/batch identities and canonical target-set hashes reproduce under the hosted workflow; the selected sentinel identities and capacity safety are coherent; and no forbidden scientific object was read. It does not validate any V0.26 scientific response, solver tolerance behavior, cross-host response reproducibility, exact-target/direct agreement, node-set side effects, 107-row Layer-B labels, covariance, nuisance handling, statistical/model inference, or physical dark-sector inference.

The candidate remains non-executable. In particular, the hosted static PASS does not authorize authoring/launching a sentinel science workflow or a full 107-row workflow from the split base specification. The next admissible action remains consolidation into one prospective V0.26 R1 preregistration plus one immutable machine-readable contract that directly incorporates the alpha hardening, route-specific tolerance correction, the hosted static-audit evidence, the corrected/explicit mixed-payload identity, and a stronger exact GRID896 node identity. That R1 pair must then receive an independent contract audit before any sentinel executor/workflow is authorized.

Readiness remains 68%; scientific frontier remains 67%; effect remains `+0/+0`.

## Verdict

**QUALIFIED**

The hosted response-blind static audit is accepted as scoped infrastructure/contract-preparation evidence for the identities it actually verifies. It is not accepted as a complete frozen-contract PASS because (1) the candidate's frozen mixed-payload maximum differs from the hosted pinned-runtime result, (2) the current static auditor does not assert that frozen scalar, (3) the exact generated GRID896 node representation is not independently hash-bound in the candidate, (4) the split preregistration/contract/amendments still require consolidation, and (5) the latest branch trigger note is stale relative to Actions. No scientific gate advances.