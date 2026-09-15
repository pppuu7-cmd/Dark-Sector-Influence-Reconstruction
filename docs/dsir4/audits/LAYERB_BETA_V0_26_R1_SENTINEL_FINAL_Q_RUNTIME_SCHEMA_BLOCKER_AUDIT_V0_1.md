# DSIR V0.26 R1 final-Q runtime-schema blocker audit

Status: **FAIL-CLOSED BLOCKER — HOSTED CONFIRMATION PENDING**  
Date: 2026-09-15  
Effect: `+0/+0`.

## Result reviewed

Reviewed exact PR179 promotion merge `bcd1cfaaee2961fe4997d5789971547e3ea42955`, first parent `370e8bb6fd77bcc3cbf3d5826a6e3a908beacda4`, second parent / exact Q staging head `24082fa57d420de2f6e837c578fbbf0d21e25fb7`.

PR179 added exactly one file relative to its first parent and deleted nothing:
`docs/dsir4/authority/LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_PACKAGE_QUALIFICATION_V0_1.json`.
Its git blob is exactly the previously qualified Q candidate blob `ab3249a6fd71a8fe8dcbd8c1be0a8b18e3e789cd`.

Final launch descriptor `docs/dsir4/launch/LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_V0_1.json` is absent. Exact PR179 promotion head has zero push Actions runs. No sentinel workflow, CLASS solve, scientific response or covariance read occurred.

## Newly discovered runtime-contract defect

Active sentinel workflow W remains exact blob `19907175f0f3417ddee2aba6916d961c6be02e26`. Its `authorize` job requires Q to expose these six keys at the **top level**:

- `active_workflow_git_blob_sha1`
- `launch_authority_git_blob_sha1`
- `launch_descriptor_git_blob_sha1`
- `executor_git_blob_sha1`
- `decision_git_blob_sha1`
- `implementation_contract_git_blob_sha1`

Exact final Q blob `ab3249a6fd71a8fe8dcbd8c1be0a8b18e3e789cd` does not contain any of those six keys at the top level. It instead contains the correct corresponding values under `acyclic_package` and `implementation_bindings`.

Thus the substantive identities are present, but the runtime schema consumed by W is incompatible with the promoted Q layout. If exact final L were created now, W would enter `authorize` and raise a Python `KeyError` before any sentinel solver construction. This is fail-closed, but it means the one-run sentinel is **not executable as intended** in the current state.

## Scope of historical Q qualification

Historical Q funnel authority `docs/dsir4/authority/LAYERB_BETA_V0_26_R1_SENTINEL_Q_FUNNEL_QUALIFICATION_V0_1.json`, blob `43696ebc566c23871c0bcd94feca40bb9c03d82c`, was scoped to the inactive Q promotion boundary. Its historical `QUALIFIED` verdict is not rewritten. The newly discovered defect is a later runtime-consumer compatibility layer that was not established by that scoped promotion qualification.

PR178 post-promotion confirmation `docs/dsir4/authority/LAYERB_BETA_V0_26_R1_SENTINEL_WA_PR178_POST_PROMOTION_CONFIRMATION_V0_1.json`, blob `500fbea5dbad463debf712bd466a3aaf8d9a7653`, correctly authorized exact-Q promotion plus a separate post-promotion audit; it did not authorize skipping this newly observed runtime-compatibility check.

## Reproducibility

The blocker is reproducible directly from immutable git objects without substantive science:

1. `git show bcd1cfaaee2961fe4997d5789971547e3ea42955:.github/workflows/layerb-beta-v026-r1-sentinel-science-v0-1.yml` shows six top-level `Q[...]` accesses in `authorize`.
2. `git show bcd1cfaaee2961fe4997d5789971547e3ea42955:docs/dsir4/authority/LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_PACKAGE_QUALIFICATION_V0_1.json` lacks those top-level keys while preserving exact equivalent nested values.
3. `git rev-parse` reproduces W blob `19907175f0f3417ddee2aba6916d961c6be02e26` and final-Q blob `ab3249a6fd71a8fe8dcbd8c1be0a8b18e3e789cd`.
4. GitHub Actions API for `head_sha=bcd1cfaaee2961fe4997d5789971547e3ea42955&event=push` returns zero runs.
5. Final L is absent at the reviewed commit.

Hosted response-blind confirmation workflow is staged on branch `audit/v026-r1-sentinel-final-q-post-promotion`, exact workflow head `00c8c1221e499b695a4a8eea94ba1961bf853a77`. Run `35023640741`, job `104565256669`, is pending runner execution at the time this fail-closed audit record is created. Its intended terminal blocker token is `BLOCKED_LAYERB_BETA_V0_26_R1_SENTINEL_FINAL_Q_RUNTIME_SCHEMA_PLUS_0_PLUS_0`.

## Correction boundary

The smallest prospective repair is Q-only. W, A, L, executor, decision code and scientific R1 contract need not be changed. A corrected Q candidate should add the six exact top-level bindings required by W while preserving the already-bound values:

- W `19907175f0f3417ddee2aba6916d961c6be02e26`
- A `4ba40e59e6a9d48636d95d07efab575e56ae0966`
- L `9c217e41764d979bea12644fae372354241bc976`
- executor `9affe7c7d4e02bbc728ba15e3cde893ec9876b38`
- decision `97f675e48e5b63a3d6dc7a10b0c2f2e6833cf2d9`
- implementation contract `e14804463d9eab288162b4c98e8dd5c1fd6a10eb`

That corrected Q must undergo a new response-blind static/runtime compatibility audit and independent funnel qualification before any replacement at the final-Q path.

## Verdict

`BLOCKED`

Classification: `SENTINEL_FINAL_Q_RUNTIME_SCHEMA_INCOMPATIBILITY_BLOCKED_BEFORE_L`.

Final L creation is not authorized. Sentinel science has not executed and is not authorized from the current final-Q state. Full 107-row execution remains closed. Readiness remains `68%`; scientific frontier remains `67%`.
