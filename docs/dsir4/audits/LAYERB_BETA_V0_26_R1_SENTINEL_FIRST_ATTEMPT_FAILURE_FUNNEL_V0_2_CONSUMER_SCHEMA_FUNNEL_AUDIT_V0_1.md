# DSIR Funnel Auditor review — V0.26 R1 failure-funnel v0.2 consumer schema

Date: 2026-09-16

Scope: independent response-blind source/code/provenance audit only. GitHub repository and Actions are authoritative. No scientific-response values were read or generated.

## Reconstructed authority state

The reviewed default-branch baseline was `8493f247b3095a139626cf11cfaa80e85daad293`, which merged PR #193 and persisted `docs/dsir4/authority/LAYERB_BETA_V0_26_R1_SENTINEL_FIRST_ATTEMPT_FAILURE_FUNNEL_HOSTED_WORKFLOW_STATIC_AUDIT_AUTHORITY_V0_1.json`. That terminal static authority has verdict `QUALIFIED`, effect `+0/+0`, and authorizes only prospective authoring and independent review of a separate one-run hosted failure-funnel execution authority. It explicitly does not authorize a failure-funnel dispatch, sentinel rerun, same-nonce second attempt, successor sentinel science, full 107-row execution, or downstream science.

The consumed sentinel attempt remains run `35033268924`, workflow `359060727`, head `9a333294f3acb80201c5f6ed5b74918c1c767232`, run #1 / attempt #1, terminal failure before science. Historical forensic evidence and hardened PR190 identities remain unchanged.

A later execution-authority compatibility audit, run `35041244978`, was terminal `completed/success` but its artifact/classification recorded `HOSTED_FAILURE_FUNNEL_EXECUTION_AUTHORITY_RUNTIME_BINDING_INCOMPLETE`; the v0.2 candidate was therefore authored prospectively to correct those runtime bindings.

## Nonterminal workflow boundary

At review time, the exact v0.2 runtime-binding audit run `35044374801`, workflow `359223774`, branch `audit/v026-r1-failure-funnel-runtime-binding-v02`, head `4c8a59b68791c0320840652dff65f1a106e89634`, run #1 / attempt #1, remained `queued` with job `104630920289` queued and no terminal conclusion. This audit does not use or predict any partial output from that run and does not issue a competing verdict on its eventual result.

## Exact candidate identities inspected

- Hosted failure-funnel workflow: `.github/workflows/dsir-v026-r1-first-attempt-failure-funnel-hosted-v0-2.yml`, git blob `670a771e1d2e2854c33d71cc1c37ea6beea85566`.
- Execution authority candidate: `docs/dsir4/authority/LAYERB_BETA_V0_26_R1_SENTINEL_FIRST_ATTEMPT_FAILURE_FUNNEL_HOSTED_EXECUTION_AUTHORITY_V0_2.json`, git blob `47788695c3ab7050099ed44cacbb6f507cbbf03d`.
- Independent review-confirmation candidate: `docs/dsir4/authority/LAYERB_BETA_V0_26_R1_SENTINEL_FIRST_ATTEMPT_FAILURE_FUNNEL_HOSTED_EXECUTION_AUTHORITY_REVIEW_CONFIRMATION_V0_2.json`, git blob `f8824d107a7fbfb260e5c5946a9d05f71131c94b`.
- Runtime-binding static auditor: `ci/dsir_v026_r1_sentinel_first_attempt_failure_funnel_runtime_binding_audit_v0_2.py`, git blob `66f4c9352c8efa0732d625689c4ba582535dfb73`.
- Frozen hardened PR190 failure-funnel auditor at head `5731b605afdc35bd85d3a2014a9e135719a07697`: `ci/dsir_v026_r1_sentinel_first_attempt_failure_funnel_audit_v0_1.py`, git blob `f7eff337e511baa25d51e5b0c333a97534e1bbc3`.

The v0.2 authority/review pair prospectively bind `refs/heads/main`, one `workflow_dispatch`, exact nonce `DSIR-V026R1-FFHOSTED-V0-2-8493F247-670A771E-20260916-A1`, one dispatch and run attempt 1, while keeping the consumed science rerun, same-nonce second attempt, successor sentinel science and full-107 execution false.

## Explicit deterministic counterexample

The exact hosted v0.2 workflow runs the frozen hardened PR190 auditor and then validates the emitted JSON receipt. Its post-audit consumer code requires:

`assert d['successor_science_authorized'] is False`

The frozen producer auditor does not emit that field. Its output schema instead contains:

`'successor_science_authorized_by_this_receipt': False`

The adjacent consumed keys are compatible: `verdict`, `classification`, `terminal_first_attempt_authority_admissible`, `rerun_authorized`, `same_nonce_second_attempt_authorized`, and `full_107_row_execution_authorized` are present. Therefore the successor-science field is a specific producer/consumer schema mismatch, not a general suspicion.

If the hosted workflow reaches this validation step after the frozen auditor produces its intended receipt, Python dictionary lookup of `d['successor_science_authorized']` deterministically raises `KeyError`. The workflow therefore cannot reach its intended successful hosted evidence persistence under the exact frozen producer schema.

This is an infrastructure/implementation defect only. It neither changes nor refutes the historical pre-science sentinel failure, the forensic reconstruction, or the hardened PR190 failure-funnel logic.

## Static-auditor coverage gap

The v0.2 runtime-binding auditor checks exact workflow/authority/review blob identities, authorized ref, nonce, review binding, first-attempt guards and zero dispatch history. It does not verify the interface between the hosted workflow's receipt-consumer keys and the exact frozen PR190 auditor's emitted receipt schema. Consequently a green result from that static audit, if later terminal, would not close this independently demonstrated schema mismatch.

## Alternative explanations tested

This mismatch is not threshold tuning, interpolation behavior, grid resolution, sampling, solver tolerance, execution-order state dependence, numerical nondeterminism, nuisance handling, covariance structure, look-elsewhere selection, or external systematic origin. None of those layers are reached by this candidate. It is a deterministic response-blind software-interface mismatch between a frozen producer schema and a prospective consumer.

The earlier runtime-binding corrections in v0.2 are separately meaningful: the candidate now enforces main ref, exact execution-authority blob, exact review-confirmation blob, exact workflow blob, nonce, first dispatch and run attempt. This audit does not invalidate those corrections; it shows they are insufficient for execution readiness.

## Interpretation ceiling and funnel consequence

Green CI or a future terminal result of run `35044374801` cannot by itself be scientific PASS. No CLASS solve, scientific response, interpolation/grid/tolerance stability, covariance, nuisance, statistical/model inference, or physical dark-sector inference is established here.

The exact v0.2 candidate set is not admissible for promotion-to-dispatch as currently written. Do not dispatch it. Do not rerun science run `35033268924`; do not create a same-nonce second attempt; do not modify/remove/recreate final L; do not run successor sentinel science or full 107 rows.

A prospective corrected successor must at minimum either consume the exact producer key `successor_science_authorized_by_this_receipt` or freeze an explicit equivalent schema transformation, and its independent static audit must verify all hosted receipt-consumer fields against the exact frozen producer output schema before any dispatch authority can be activated.

Scientific effect remains `+0/+0`; readiness remains `68%`; scientific frontier remains `67%`.

## VERDICT

`QUALIFIED`

Qualification scope: exact v0.2 hosted failure-funnel execution candidate implementation only. The nonterminal run `35044374801` receives no outcome verdict here. The current candidate is not execution-ready because of the deterministic frozen-producer/hosted-consumer schema mismatch described above.