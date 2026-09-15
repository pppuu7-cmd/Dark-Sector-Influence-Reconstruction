# DSIR authoritative recovery — latest

Updated: 2026-09-15. Scope: **DSIR only**. GitHub repository/Actions state, frozen DSIR4 preregistrations/contracts, terminal authorities, independent audit qualifications, `docs/CURRENT_PROCESS.md`, and this file are the durable source of truth. Chat is not authority.

## Frozen scientific boundaries

Production `h=1e-4`; native `k_per_decade_for_pk=20`; sampling `0.00035`; scientific numerical threshold strict `<1e-3`; technical reproducibility strict `<1e-5`; requested/exact-node binding `<=1e-12`. V0.26 R1 freezes alpha canonical-32769 `tol_perturb_integration=3e-10` and beta exact-target-union `1e-12`. Covariance, whitening, nuisance, relation-null, `Wm_S3`, global 65537, statistical/model inference and physical dark-sector inference remain unopened. Static/provenance/governance progress alone does not raise readiness or scientific frontier.

## Terminal numerical baseline and R1

V0.25 remains terminal classification `FORCED_BASELINE_EXACT_TARGET_UNION_REMEDY_SUPPORTED`, effect `+0/+0`; the historical original-producer `INVALID_PROVENANCE` verdict remains historical and separately corrected without rewrite.

V0.26 R1 remains the prospectively frozen successor: preregistration blob `545e5be589e0f8029d23db2edb4e2faad116c3a0`, machine contract blob `b510d8e97baf1c0b7b216c0605d83cdd029254e9`, 107 rows (DES 53/BOSS 54), full-replay accounting 738 CLASS constructions. No full 107-row execution authority exists.

## Sentinel implementation and original package

PR171 implementation is promoted/qualified. Exact frozen code identities: W `19907175f0f3417ddee2aba6916d961c6be02e26`, executor `9affe7c7d4e02bbc728ba15e3cde893ec9876b38`, decision `97f675e48e5b63a3d6dc7a10b0c2f2e6833cf2d9`, implementation contract `e14804463d9eab288162b4c98e8dd5c1fd6a10eb`.

Original PR173 package identities were A `4ba40e59e6a9d48636d95d07efab575e56ae0966`, L `9c217e41764d979bea12644fae372354241bc976`, Q `ab3249a6fd71a8fe8dcbd8c1be0a8b18e3e789cd`.

PR178 staged exact W/A to active/final paths without L, merge `d605a941b412bb9625bf2fc6fedb0c7d9f8e8293`, after static/funnel qualification and a later post-promotion `CONFIRMED_SCOPED` audit.

PR179 then promoted exact old Q blob `ab3249a6fd71a8fe8dcbd8c1be0a8b18e3e789cd` to final Q path, merge `bcd1cfaaee2961fe4997d5789971547e3ea42955`, without L. PR179 head had zero push workflow runs.

Therefore the live pre-correction runtime state is:

- active W present: `19907175f0f3417ddee2aba6916d961c6be02e26`;
- final A present: old `4ba40e59e6a9d48636d95d07efab575e56ae0966`;
- final Q present: old `ab3249a6fd71a8fe8dcbd8c1be0a8b18e3e789cd`;
- final L absent;
- sentinel science never executed.

Any older recovery text saying final Q is absent is superseded.

## Runtime-schema blocker chain

PR179 final-Q post-promotion audit found old Q runtime-incompatible with frozen W: W reads six Q bindings at the top level, while old Q stores the exact values only in nested sections. Final L creation in that state would fail closed in W `authorize` before lane execution.

Hosted confirmation run `35023640741`, job `104565256669`, terminal success. Artifact `10419077399`; independently re-downloaded ZIP SHA256 `d35cbc348d7760a91a736a0571bf42e9b8f955ba8bd9f788d18f0f586121e83e`; inner receipt 2016 bytes, SHA256 `a83d4673b50784e1a0c714529d4dddf5bc048ac9eee34e77fed98ef6ca14ca0d`, verdict `BLOCKED`. Terminal hosted confirmation authority is `docs/dsir4/authority/LAYERB_BETA_V0_26_R1_SENTINEL_FINAL_Q_RUNTIME_SCHEMA_BLOCKER_HOSTED_CONFIRMATION_V0_1.json`.

A complete pre-solve source audit then identified a second fail-closed mismatch: executor `require_launch_authority()` requires A field `promotion_authority_git_blob_sha1`, while old A contains the same correct PR169 identity only under `r1_promotion_authority_git_blob_sha1`.

The broader current blocker is `docs/dsir4/authority/LAYERB_BETA_V0_26_R1_SENTINEL_RUNTIME_CHAIN_SCHEMA_BLOCKER_V0_2.json`, blob `09190c92c1311b66e953d19ef3811d63a0bf871a`, verdict `BLOCKED`. It supersedes only the earlier Q-only repair guidance; historical qualifications and blocking verdicts remain intact.

No additional launch-package schema mismatch was found in executor `load_contract()` / PR169 precondition or the frozen decision finalizer. This review invoked no CLASS solver and read no scientific response.

## Corrected governance-only A-L-Q package v0.2

Branch `research/v026-r1-sentinel-runtime-chain-correction-v02`, exact frozen/audited head `d3b32cd341ce16b5494024dfa9785a2480173dc1`.

Corrected package:

- A `1c9945dd00b137f3e202efa14bf4112fffebf8af`: old A plus exactly one executor-compatible alias `promotion_authority_git_blob_sha1`;
- L `fa7014435f0a5688def2124898ddd01d0c0183aa`: old L with only exact A binding changed;
- Q `f7b97f47d9e771e3d3ea78875da5a45962160cd0`: six W-required top-level runtime bindings plus exact corrected A/L bindings.

Source diff against correction base main `78f96f2c60db385f88a391b7fd046dd312176019`: A `+1/-0`; L `+1/-1`; Q `+8/-2`. W, executor, decision, R1 contract, thresholds and target geometry are unchanged.

Correction contract `docs/dsir4/contracts/LAYERB_BETA_V0_26_R1_SENTINEL_RUNTIME_CHAIN_CORRECTION_CONTRACT_V0_2.json`, blob `01af3648bd3dc640acf35c7b0b7c116334b61cfe`.

Hosted static full-runtime-chain audit run `35025081430`, job `104570053404`, terminal success. Artifact `10419525675`; ZIP SHA256 `82929104a6129f5f8f8bd465ef574b4ce55c172411415c19458de9bb8fe5fa0f`; inner `runtime_chain_correction_static_audit.json` 1590 bytes, SHA256 `b326cfc032a2e758d9565b4672d34f5f18ec61d8475ee5d23601e037bf3dab39`.

That receipt proves, within response-blind static scope:

- A delta is exactly one alias;
- L delta is exactly corrected-A binding;
- Q delta is exactly six top-level bindings plus corrected A/L bindings;
- W authorize contract passes statically;
- executor launch-authority contract passes statically;
- PR169 executor precondition is present;
- decision full-replay firewall remains intact;
- final A/Q were not replaced by the audit;
- final L is absent;
- no CLASS solver or scientific-response/covariance read occurred.

Independent external funnel audit run `35025283328` is required before promotion qualification. Until that run is terminal `QUALIFIED` and a separate authority reaches main, corrected A/L/Q remain candidates only.

## Current funnel position

`V0.25 TERMINAL -> V0.26 R1 QUALIFIED -> PR171 IMPLEMENTATION -> PR173 ORIGINAL PACKAGE -> PR178 OLD W/A STAGED -> PR179 OLD FINAL Q PRESENT -> RUNTIME CHAIN BLOCKED -> V0.2 GOVERNANCE-ONLY A-L-Q CORRECTION STATIC PASS -> INDEPENDENT FUNNEL QUALIFICATION REQUIRED -> FINAL L ABSENT -> SENTINEL SCIENCE NOT EXECUTED -> FULL 107 ROW CLOSED`.

## Exact recovery action

First inspect current `main`; then inspect run `35025283328` and exact correction head `d3b32cd341ce16b5494024dfa9785a2480173dc1`.

If independent funnel is not terminal `QUALIFIED`, do not promote corrected runtime objects. If it is terminal `QUALIFIED`, independently re-download/hash its artifact, persist a separate qualification authority, and place that authority on main before any final A/Q replacement.

Only after authority-first qualification may exact corrected A and Q replace the old final A/Q **without L**. Then perform a separate post-replacement fail-closed audit. Only a later explicit confirmation may make creation of exact corrected L (`fa7014435f0a5688def2124898ddd01d0c0183aa`) admissible as the unique new-file one-run sentinel trigger.

Do not create L early. Do not rerun the sentinel. Do not launch the full 107-row replay. Even a future sentinel PASS still requires independent sentinel-result funnel audit and a distinct full-replay launch authority.

Effect remains `+0/+0`; repository readiness `68%`; scientific frontier `67%`.
