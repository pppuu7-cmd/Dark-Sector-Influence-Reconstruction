# DSIR current-process ledger

Updated: 2026-09-16. Scope: **DSIR only**. Repository/Actions state, frozen DSIR4 contracts and terminal authorities are authoritative. Chat is not authority.

## Scientific baseline and immutable boundary

V0.25 remains terminal numerical classification `FORCED_BASELINE_EXACT_TARGET_UNION_REMEDY_SUPPORTED`, effect `+0/+0`. V0.26 R1 remains prospectively frozen under preregistration blob `545e5be589e0f8029d23db2edb4e2faad116c3a0` and contract blob `b510d8e97baf1c0b7b216c0605d83cdd029254e9`.

Frozen science boundary is unchanged: 107 retained rows = DES 53 + BOSS 54; alpha route tolerance `3e-10`; beta exact-target tolerance `1e-12`; scientific strict `<1e-3`; technical strict `<1e-5`; requested-node binding `<=1e-12`; full replay accounting 738 CLASS constructions. There is no full-107 execution authority. Covariance, whitening, nuisance marginalization, relation-null, `Wm_S3`, global 65537, statistical/model inference and physical dark-sector inference remain closed.

Science run `35033268924`, workflow `359060727`, run #1 / attempt #1, is permanently consumed. It failed before science at the frozen W event guard and must never be rerun or recreated as a same-nonce second attempt. Historical authorities/results remain immutable.

## Final v0.4 source and static qualification

Frozen source origin head: `10e7f9bd8aaa5623e9f34adf17c2f53f50db5873`.

Exact runtime identities:
- hosted failure-funnel workflow blob `6bf2027a121348823914e9076338055a4820162e`;
- post-run terminal-history workflow blob `6c2617e756877fb3cbb8b27dcf16b2bfc164cab5`;
- v0.4 candidate contract blob `23e2404d835b4615308fbbb345f8a00e45c449a1`.

Terminal static qualification is persisted on `main` as `docs/dsir4/authority/LAYERB_BETA_V0_26_R1_SENTINEL_FIRST_ATTEMPT_FAILURE_FUNNEL_V0_4_FINAL_STATIC_QUALIFICATION_V0_1.json`, blob `eba53204d3a46b11c54c37adefe729722b00783f`. Authoritative static run `35139440106` is terminal success. Artifact `10464695970` ZIP SHA256 is `bff94d6a0c0eb956efd19357a8099075ea035fcc78fe8a638b6e2c7b75333b60`; receipt SHA256 is `7072fa7f39f8c903f0b75fddc14f108981c9ec6beafc052f5593ba949b4e88ae`. Static qualification itself authorizes no execution or science.

## Terminal v0.4 execution-authority gate

Prospectively frozen authority chain:
- execution authority blob `d68aa9ffa3fb5a7768e6802146aed74a3b57cf1b`;
- independent review blob `01e5e9e0145e8c2ad1f0da639f3de073d9b26da2`;
- runtime static authority blob `6bbacdc70dbfbee1dc4753e4a05266f9dbe45399`;
- nonce `DSIR-V026R1-FFHOSTED-V0-4-10E7F9BD-7072FA7F-20260916-A1`;
- authorized ref `refs/heads/main`;
- authorized target event `workflow_dispatch`;
- target run number 1 / attempt 1 only;
- required prior target dispatch count 0;
- required parallel/in-progress target sibling count 0;
- rerun, second dispatch and same-nonce second attempt forbidden.

The first execution-gate audit run `35144971693` failed only because the Critic harness searched for a stale local marker name (`trig` rather than the frozen source's `e`). It produced no authority artifact and changed no v0.4 source or authority object. It is immutable historical FAIL and is not rerun.

Corrected Critic v0.2 uses auditor blob `ea2a41f7ea9692d3c9f95ea82ff7785c486eb092`, hosted audit workflow blob `9b062b091e118927ab602a464bd8adef3805d719`, and contract blob `d859aa3becf60dca328d41d4aa268c54904c23ef`.

Authoritative corrected execution-gate run `35145130524`, workflow `359972281`, run #2 / attempt #1, exact head `8b1957e0e0aa1c85281b7975c2cda91941f31541`, job `104959104646`, is terminal `success`.

Artifact `10467180869` was independently downloaded and verified. ZIP SHA256 is `3935d4a48cd9e596dca040ddc22f23ed2b71e299bd51a33f4e90a629197eb5b3`; receipt SHA256 is `5bb92f3548d64a8b2757c75c149dff9ebc2738ee535277a959415c7edb16de66`. Fresh target history at the terminal gate contains zero target `workflow_dispatch` runs and zero competing/in-progress target siblings.

Receipt classification is `V0_4_EXACT_ONE_FIRST_LIVE_FAILURE_FUNNEL_DISPATCH_AUTHORITY_QUALIFIED`; token is `QUALIFIED_LAYERB_BETA_V0_26_R1_SENTINEL_FIRST_ATTEMPT_FAILURE_FUNNEL_V0_4_EXECUTION_GATE_V0_2_PLUS_0_PLUS_0`.

Durable terminal gate authority: `docs/dsir4/authority/LAYERB_BETA_V0_26_R1_SENTINEL_FIRST_ATTEMPT_FAILURE_FUNNEL_V0_4_TERMINAL_EXECUTION_AUTHORITY_GATE_V0_1.json`.

This terminal gate authorizes exact promotion of the frozen source/authority set and, only after that promotion plus a fresh atomic zero-history preflight, exactly one target v0.4 dispatch. It does **not** authorize any successor sentinel science, full 107-row execution or downstream science.

## Current funnel position

`V0.25 TERMINAL -> V0.26 R1 FROZEN -> CONSUMED SENTINEL PRE-SCIENCE FAILURE -> FORENSIC AUTHORITY TERMINAL -> V0.2/V0.3 DEFECTS TERMINAL -> V0.4 STATIC QUALIFIED -> V0.4 EXECUTION AUTHORITY QUALIFIED -> EXACT PROMOTION + ATOMIC PRE-DISPATCH GATE NEXT -> ONE FAILURE-FUNNEL DISPATCH MAX -> TERMINAL POST-RUN HISTORY REQUIRED -> SCIENCE STILL CLOSED`.

Interpretation ceiling remains governance/provenance/execution-authority only. Effect remains `+0/+0`.

## Exact next admissible action

1. Promote the exact v0.4 runtime source and authority chain to `main` without changing their Git blobs.
2. Immediately before target dispatch, atomically recheck: exact main blobs, nonce/ref/authority identity, target dispatch history count 0, no competing/in-progress target dispatch, target workflow run-number history compatible with first run.
3. If and only if that preflight remains clean, create exactly one `workflow_dispatch` of the target v0.4 workflow with the exact authority blob inputs and nonce.
4. No rerun, retry, second dispatch or manual outcome repair is permitted after target dispatch begins.
5. Require the target main run to be run #1 / attempt #1, pass its end-of-run live history recheck, then require the separate post-run `workflow_run: completed` audit to confirm exactly one terminal successful target run.
6. Only after independent consumption of both runtime artifacts may a separate runtime authority be authored and the minimal next scientific object be considered. Full 107 rows and all downstream science remain closed.
