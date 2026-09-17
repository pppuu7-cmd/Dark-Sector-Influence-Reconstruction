# DSIR Funnel Researcher — GRID896 V0.6 workflow-registry capture blocker audit

Date: 2026-09-17. Scope: **DSIR only**. GitHub repository/Actions remain the sole durable scientific source of truth; chat is not authority.

Reviewed main at gate start: `57c3883a02a9f7cea3334e6afa65fd95b5dd6739`.

## Authorized gate

The current terminal qualification blob `9cc8f6ad8ed01821841afc84181933efc75fa44e` authorizes only `CAPTURE_AND_INDEPENDENTLY_CONFIRM_READ_ONLY_GITHUB_ACTIONS_WORKFLOW_REGISTRY_ID_PATH_ACTIVE_STATE_FOR_EXACT_V0_6_CANONICAL_WORKFLOW_ONLY`.

The required positive tuple is:

- positive GitHub-assigned workflow ID;
- exact path `.github/workflows/layerb-beta-v026-r1-cross-host-grid896-producer-identity-diagnostic-v0-6.yml`;
- registry state exactly `active`.

Inference, guessing, alias substitution, and launching the diagnostic to discover the workflow ID are forbidden by the frozen gate.

## Repository and Actions recheck

The canonical active workflow remains present with exact Git blob `832f0491421619579c2a1d77ba9ca339cb4898ac`, byte-identical to the audited candidate. Frozen executor blob remains `eae9eee7ae6a1424bcac67279663a2c8ddd3ebf9`; implementation-manifest blob remains `e71d2c92a56555ffaea59a08c80d8f073c4b48da`; terminal static confirmation blob remains `6cc317eb359a820bc1ecb3c657fc33b46a7d152b`.

The future execution-authority path `docs/dsir4/authority/LAYERB_BETA_V0_26_R1_CROSS_HOST_GRID896_PRODUCER_IDENTITY_DIAGNOSTIC_IMPLEMENTATION_STATIC_AUDIT_AUTHORITY_V0_6.json` is absent. The V0.6 launch-marker path `docs/dsir4/launch/LAYERB_BETA_V0_26_R1_CROSS_HOST_GRID896_PRODUCER_IDENTITY_DIAGNOSTIC_V0_6.launch.json` is absent.

Current repository Actions state is quiet: queued run count `0`, in-progress run count `0`. The latest repository workflow run remains terminal-history run `35183519508`, created before V0.6 promotion; its only job `105080579651` is terminal success and artifact `10480539101` has digest `sha256:0d61e9f90f03d875e8a67d99a7882530f44e5d6bd875d900c33391033c5fb329`. No V0.6 diagnostic run or artifact exists.

Historical V0.13 control `34773514342` was also rechecked: run #1 / attempt #1 remains terminal success; all 12 replay-profile jobs, invariant-audit and decision job `103769308584` remain success; decision artifact `10322573705` remains `sha256:b04db83d530c36e03f2b80ad33fb4be80747817bd08cb2b001d5c8c6375fd202`.

## Registry capture attempt

A read-only capture was attempted through the connected GitHub interface without triggering any workflow. Repository, branch, contents, workflow-run, job and artifact reads remain available, but the GitHub Actions workflow-registry collection/item endpoint required to obtain a positive workflow ID/path/state tuple is not exposed by the connected interface in this environment. The generic GitHub read path rejects `actions/workflows` registry resources rather than returning the registry object.

No positive workflow ID, exact registry path, or registry state was observed. Therefore no value is inferred, guessed, reconstructed from chronology, or borrowed from another workflow.

This is an operational provenance blocker, not evidence that the V0.6 registry entry is absent or inactive.

## Classification

`BLOCKED_READ_ONLY_GITHUB_WORKFLOW_REGISTRY_INTERFACE_UNAVAILABLE`

This does **not** change the prior terminal qualification and does **not** authorize execution-authority creation, launch-marker creation, diagnostic execution, successor sentinel science or full107/downstream science.

Scientific effect remains `+0/+0`. Interpretation ceiling remains infrastructure/provenance/static implementation only.

## Required unblock

Expose or otherwise provide a read-only GitHub Actions workflow-registry read capable of returning the exact canonical V0.6 workflow record without launching it. Then persist raw or canonicalized registry evidence plus provenance/digest and independently verify:

1. positive GitHub-assigned workflow ID;
2. exact canonical path;
3. registry state `active`;
4. active Git blob `832f0491421619579c2a1d77ba9ca339cb4898ac`;
5. static confirmation blob `6cc317eb359a820bc1ecb3c657fc33b46a7d152b`;
6. zero V0.6 run history before execution-authority creation;
7. continued absence of execution authority and launch marker during capture.

Until that read succeeds, the authorized next stage remains unchanged and no launch may be used as a discovery mechanism.
