# DSIR V0.26 candidate preregistration — forced-baseline exact-target-union full Layer-B numerical replay

Status: **PROSPECTIVE CANDIDATE FREEZE — NOT EXECUTABLE FROM THIS BRANCH**  
Date: 2026-09-15  
Scope: DSIR F1 numerical/reproducibility only; scientific effect `+0/+0`.

This file is intentionally created on a research branch. It does not authorize a 107-row run. Execution remains closed until this preregistration and a separate immutable V0.26 contract are reviewed/frozen on the authoritative path before executor/workflow/launch creation.

## 1. Parent authority and interpretation ceiling

Terminal parent authority is `docs/dsir4/authority/LAYERB_BETA_V0_25_PROVENANCE_CORRECTION_V0_1.json`, classification preserved as `FORCED_BASELINE_EXACT_TARGET_UNION_REMEDY_SUPPORTED`, corrected next stage exactly `PROSPECTIVELY_FROZEN_FORCED_BASELINE_EXACT_TARGET_UNION_FULL_LAYERB_NUMERICAL_REPLAY_AUDIT`.

V0.26 is a full Layer-B **numerical replay gate only**. A PASS cannot by itself open covariance, whitening, nuisance marginalization, relation-null, `Wm_S3`, global 65537, statistical/model inference, physical dark-sector inference, or later Core-v1 gates. Any successor requires an independent terminal artifact/provenance audit and a separate authority.

## 2. Frozen row denominator and geometry

The row denominator is exactly the Exp073IQ Layer-A retained object:

- 107 coordinates in inherited order;
- 53 DES + 54 BOSS;
- retained-ID SHA256 `44b57c6c910bc3612310ce415d773c8c180497528bfc5fc2927ce61da6ad40d7`;
- full-order SHA256 `bfaf582518cdbfd34b1e8392da83dac6b0885948bc31f2c29d4e48247c23af75`;
- parent run/job/artifact `34423479633 / 102703685034 / 10131794281`;
- parent artifact digest `sha256:ac959926639d3b46ecfe114e396ce03cb20a0763ef2781db454408d8ad0759df`.

No row may be selected, removed, reordered or replaced after any response is read.

The numerical request geometry is the response-blind Exp073JL plan, independently frozen before V0.26:

- authoritative summary: `docs/dsir4/authority/RECOVERED_EXP073JL_RESPONSE_BLIND_REQUEST_PLAN_V0_2.json`;
- exact materialized source artifact: run `34695347893`, artifact `10298655751`, ZIP SHA256 `9b8bdcf03cb05bc979e8c72135acac92232864a74dc1d510b579d8efb5cbb2a7`;
- inner `plan.json`: 3,953,984 bytes, SHA256 `c12bdb2a407de3f9e2c0c410719ae604d9b3516dabb76c9b1598340418ee8064`;
- coarse/production calls digest `9e829d5127457085f18d79901d4aa621a050ce8406ff30c4d7e157dd069b80b4`;
- fine calls digest `9f5f85e92570b68576bae91f52163cb0c005a1e003bfc09b8ccc80b332f79b36`;
- 441 production calls = 377 DES + 64 BOSS GL64, 83,666 scalar target entries;
- 569 fine calls = same 441-bitwise-identical prefix + 128 BOSS GL128 calls, 121,682 scalar target entries.

The 377 DES production calls contain 64,658 unique target-k values with zero cross-call overlap. Each DES call has 90–244 unique target-k values. All 64 BOSS GL64 calls and all 128 BOSS GL128 calls use the same 99-unique-k set; DES and BOSS target sets do not overlap. Therefore a single global exact-target union is impossible under the frozen CLASS k-output envelope and is not the V0.26 construction.

## 3. Frozen numerical state

- CLASS-IV commit `ac627d54e9ce196a08878d1ba33999819925d19c`.
- Baseline `configs/dsir4/c2/ide0_reference_v0_1.ini`.
- Precision `configs/dsir4/c2/dsir_ide_p8_v0_1.pre`.
- `h = 1e-4`.
- native `k_per_decade_for_pk = 20`.
- production perturb sampling `0.00035`.
- `tol_perturb_integration = 1e-12` for every substantive V0.26 model.
- scientific relative threshold: strict `<1e-3`.
- technical cross-host reproducibility threshold: strict `<1e-5`.
- exact requested-node binding threshold: `<=1e-12`.
- NumPy `1.26.4`, SciPy `1.17.1`; successor implementation must pin the numerical Python stack exactly before launch.

Forced runtime mask:
`NPY_DISABLE_CPU_FEATURES=AVX512CD,AVX512F,AVX512_CLX,AVX512_CNL,AVX512_ICL,AVX512_KNL,AVX512_KNM,AVX512_SKX`.

Required forced active AVX-512 dispatch: empty. Required forced active non-AVX512 dispatch exactly: `AVX,AVX2,F16C,FMA3,POPCNT,SSE41,SSE42,SSSE3`.

## 4. Preserve alpha; remedy beta only

The existing exact operand-localization authority found the full Layer-B discrepancy in `abs_dDelta_m_dbeta_symmetric`: beta worst coarse→fine relative difference `0.007384797439715474`, while alpha worst difference is `0.0006776803529834111 < 1e-3`. V0.26 therefore must not silently move alpha onto the new low-node beta remedy.

Alpha remains on the already validated canonical 32769 route:

- roles: reference `(0,0)` and alpha-minus `(-h,0)` only;
- canonical 32769 node identity and eight-chunk method inherited from existing authorities;
- eight frozen slices per role, maximum live CLASS instances per job = 1;
- physical alpha solver constructions = `2 roles * 8 chunks = 16`;
- alpha response is the inherited centered-cubic value on the fully assembled canonical 32769 response table;
- all 569 inherited calls are evaluated, including BOSS GL128 dense-z controls.

No alpha remedy is claimed by V0.26. No 65537 successor is opened.

## 5. Beta exact-target construction

Beta preserves the V0.25 remedy semantics: beta-plus `(0,+h)` and beta-minus `(0,-h)` models only, exact target extraction from a common-grid-plus-target union, with fresh target-only direct reference.

### 5.1 Pure common control

The beta common control is guarded `GRID896`: base 896, lower guard 0, upper guard 1, total 897 common nodes. It is the densest V0.25-tested guarded common grid for which every complete production call can be unioned under the inherited V0.25 envelope. No inherited target is exactly identical to a GRID896 node.

Pure control constructs exactly two models: beta-plus and beta-minus. Cubic interpolation on pure GRID896 is a control only; it is never the V0.26 remedy value.

### 5.2 Response-blind mixed packing

Beta mixed build retains the V0.25 CLASS capacity/parser envelope: 1152 requested k nodes and 32768 parser bytes. GRID896 leaves 255 target-node slots. Since DES call target sets are pairwise disjoint and the minimum DES call has 90 targets, no three DES calls can fit (`3*90 > 255`).

Freeze the DES pairing algorithm:

1. for DES call indices `0..376`, build `(unique_target_count, call_index)`;
2. sort ascending by `(unique_target_count, call_index)`;
3. two-pointer pack: pair smallest remaining with largest remaining iff their target counts sum to `<=255`; otherwise emit the largest as a singleton;
4. sort call indices within a pair;
5. after packing, order DES batches by `(minimum_call_index, call_index_tuple)`;
6. batch node set = sorted exact union of GRID896 and all target k of all calls in the batch.

Expected result: 300 DES mixed batches = 77 pairs + 223 singletons. All BOSS GL64 and GL128 z calls share one 99-k target set and use one BOSS mixed batch. Total mixed batches = **301**, IDs `M000..M300`; target-union size 99–255; total requested node count 996–1152.

Canonical mixed-batch encoding is the UTF-8 bytes of Python-equivalent `json.dumps(records, sort_keys=True, separators=(',',':'))`, where each record contains exactly `batch_id`, `domain`, `call_indices`, `target_u64hex`; target hex strings are sorted unique IEEE-754 binary64 big-endian words, records are in batch-ID order. Frozen SHA256: `59abce49f6338c30b93d11fa462e1ff8642615d6100d23feca4b36505a5cef85`.

Observed response-blind parser bound under `.17g` serialization: maximum mixed payload 25,062 bytes (`M013`) < 32,768.

### 5.3 Fresh direct reference packing

Fresh direct beta reference uses target-only node sets and no interpolation. DES direct packing is first-fit decreasing:

1. sort DES calls by `(-unique_target_count, call_index)`;
2. place each whole call into the first existing bin whose exact target union remains `<=1152`; otherwise open a new bin;
3. call splitting is forbidden;
4. keep BOSS as a separate target-only domain batch.

Expected result: 58 DES direct batches + 1 BOSS direct batch = **59**, IDs `D00..D58`. Canonical encoding is identical in form to mixed encoding (`batch_id`, `domain`, `call_indices`, `target_u64hex`) and frozen SHA256 is `1c98927960e81d7fb55ebc687ef36059d964b233001551dba2aa9a01652c8864`.

Observed response-blind parser bound: maximum direct payload 24,262 bytes (`D20`) < 32,768.

Every exact beta target value is extracted by requested-node lookup with relative coordinate mismatch `<=1e-12`. Cubic interpolation is forbidden for the exact remedy and direct-reference values.

## 6. Solver accounting and sharding

Full physical solver accounting is frozen:

- alpha canonical 32769: 16 constructions;
- beta pure GRID896 control: 2;
- beta mixed: `301 * 2 = 602`;
- beta target-only direct: `59 * 2 = 118`;
- **total = 738 CLASS constructions**.

Any different scientific construction count is INVALID unless a new prospective preregistration supersedes V0.26 before execution.

Response-blind full-run sharding may be used only as follows:

- alpha: two role jobs, each sequentially executes the frozen eight 32769 chunks;
- beta mixed: 16 shards by `int(batch_id[1:]) mod 16`, expected batch counts `[19,19,19,19,19,19,19,19,19,19,19,19,19,18,18,18]` and model counts `[38,...,38,36,36,36]`;
- beta direct: 4 shards by `int(batch_id[1:]) mod 4`, expected batch counts `[15,15,15,14]` and model counts `[30,30,30,28]`;
- beta pure control: one job, two models;
- scientific shard artifacts are operands only and cannot classify the run;
- one finalizer reassembles exact inherited call/row order and alone applies the V0.26 classifier.

## 7. Pre-full hosted reproducibility sentinel

Before any full 107-row replay, run a 32-lane `ubuntu-24.04` beta sentinel after the static invariant gate. Each lane first verifies the forced NumPy profile, then evaluates only three response-blind mixed batches and their corresponding production direct batches:

- `M076`: DES calls `[76,78]`, 255 target nodes, 1152 mixed nodes; direct comparator `D50`, 1146 target-only nodes;
- `M298`: DES call `[375]`, 244 target nodes, 1141 mixed nodes; direct comparator `D00`, 1152 target-only nodes;
- `M300`: BOSS calls `[377..440]`, 99 target nodes, 996 mixed nodes; direct comparator `D58`, 99 target-only nodes.

`M076` is the first frozen full-capacity mixed pair whose two calls share one frozen direct bin; selection is response-blind. Per lane: 2 pure beta models + 6 mixed beta models + 6 direct beta models = **14 CLASS constructions**.

Power gate: minimum 6 eligible lanes, minimum 3 `NATIVE_AVX512_ACTIVE`, minimum 3 `NATIVE_AVX512_INACTIVE`; both classes required. No science retry may be launched solely to obtain a more favorable class mix.

Before full replay, every sentinel primitive beta response must satisfy cross-host maximum pairwise relative spread `<1e-5` and native-class mean separation `<1e-5`. Every sentinel exact-vs-direct comparison and mixed-common-vs-pure-common node-set-side-effect comparison must satisfy strict `<1e-3`. INVALID, underpowered or blocked sentinel => **no full 107-row response job is launched**.

## 8. Full replay finalizer and predicates

The exact frozen Exp073IR traversal/geometry is reused to build the 107 row summaries and active masks. The response adapter changes only the beta source:

- alpha column = fresh forced-baseline canonical-32769 reference/alpha-minus response;
- beta column = fresh forced-baseline exact-target-union beta response;
- every row retains its exact inherited coordinate ID, ordinal, block and atom membership.

For every inherited beta target scalar, including BOSS GL128 controls:

- exact mixed and direct values finite;
- exact/direct finite/nonzero status identical;
- requested-node binding each `<=1e-12`;
- exact-target-union vs direct response relative difference strict `<1e-3`;
- beta response from cubic interpolation of the mixed model's GRID896 common-node subset vs pure GRID896 beta control strict `<1e-3`.

Full row result requirements:

- denominator exactly 107 and inherited order/hash identities unchanged;
- zero invalid rows and retained-after-Layer-B = 107;
- no row label change relative to the inherited all-valid Layer-B state;
- BOSS GL64-vs-GL128 dense-z label disagreement = false;
- all alpha and beta atom responses finite and >0;
- no covariance/whitening/nuisance/relation-null/`Wm_S3` read.

Historical floating-point response values are non-gating; only frozen identities plus fresh V0.26 responses gate.

## 9. Decision hierarchy

Priority order:
`INVALID -> INCONCLUSIVE -> SENTINEL_UNDERPOWERED -> SENTINEL_REPRODUCIBILITY_BLOCKED -> SENTINEL_NODE_SET_SIDE_EFFECT_BLOCKED -> SENTINEL_DIRECT_REFERENCE_BLOCKED -> FULL_NODE_SET_SIDE_EFFECT_BLOCKED -> FULL_DIRECT_REFERENCE_BLOCKED -> FULL_ROW_REPLAY_BLOCKED -> PASS`.

PASS classification exactly:
`FORCED_BASELINE_EXACT_TARGET_UNION_FULL_LAYERB_NUMERICAL_REPLAY_SUPPORTED`.

PASS remains numerical/reproducibility evidence only, effect `+0/+0`; it creates no automatic next science authority.

## 10. Artifact/provenance requirements

The authoritative workflow must preserve and bind:

- static invariant receipt and response-blind reconstructed source-plan/batch-plan digests;
- all sentinel lane artifacts plus complete primitive reproducibility metrics;
- both alpha role operands, beta pure-control operand, all 16 mixed-shard operands, all 4 direct-shard operands;
- complete reassembled row/atom summary and complete decision JSON;
- launch head, run/job IDs, artifact IDs, ZIP SHA256 values, exact inner filenames, byte lengths and SHA256 values;
- prereg/contract/executor/workflow/source/baseline/precision git blob identities;
- exact CLASS/classy binary hashes and complete software-control identity for every substantive job.

The repository terminal decision materialization must be byte-identical to the authoritative decision artifact or be explicitly labelled a derived summary. Omitting primitive metrics is forbidden.

## 11. Frozen firewalls

Forbidden during V0.26: response-informed row or k selection, target-local post-result construction changes, batch repacking after responses, grid/h/tolerance/sampling/NumPy-mask changes, silent scientific retry, covariance/whitening/nuisance/relation-null access, `Wm_S3`, global 65537, downstream physical interpretation or science-gate opening.
