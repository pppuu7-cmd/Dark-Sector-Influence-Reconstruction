# DSIR V0.26 R1 — BOSS M300 cross-survey response replication falsifier v0.1

Status: **PREREGISTERED DESIGN ONLY — NO M300 RESPONSE CONSTRUCTION OR EXECUTION AUTHORIZED**

Date: 2026-09-18

## 1. Terminal scientific parent

This preregistration is admissible only because the first prospectively frozen DES scientific-response object is terminally closed:

- object: `DES M298 / call375`;
- terminal classification: `PASS_SCOPED_MINIMAL_SCIENTIFIC_RESPONSE_REPRODUCIBLE_NONZERO`;
- terminal authority blob: `7ea2cefde247845d4c6d70660b798dcaa79a4a72`;
- independent runtime Critic blob: `91fb97a73a820cf5172d7e0383752a1ee6a26143`;
- runtime Critic verdict: `PASS_TERMINAL_CLOSURE`;
- consumed run: `35368618232`.

The numerical source remains consumed run `35280281867`; it MUST NOT be rerun and no new CLASS solve is permitted.

## 2. Scientific question

**Does the complete prospectively frozen BOSS M300 beta-response family reproduce the finite-positive, technically reproducible, mixed/direct construction-stable response behavior that passed on DES M298, when evaluated over the existing immutable numerical witnesses under the same source-authoritative beta-response semantics?**

This is a cross-survey falsifier, not an attempt to confirm the DES result.

It is NOT a test of:

- cross-survey amplitude equality;
- statistical significance;
- covariance-aware likelihood;
- nuisance robustness;
- full107 validity;
- dark-sector detection;
- physical universality.

## 3. Freeze the entire M300 object

Use exactly:

- selection: `M300`;
- survey/data block: BOSS;
- calls: every integer `377..440` inclusive;
- call count: `64`;
- direct comparator batch: `D58`;
- replicate population: exactly `R01..R32`;
- native-dispatch population inherited from the frozen numerical run: 10 `NATIVE_AVX512_ACTIVE` + 22 `NATIVE_AVX512_INACTIVE`;
- order-arm population: 16 A + 16 B.

No call may be dropped after outcome inspection.

## 4. Target structure — unique coordinates versus source entries

The immutable frozen plan establishes:

- all 64 BOSS calls have the same raw target list;
- raw target entries per call: `297`;
- unique exact coordinates: `99`;
- every unique coordinate occurs exactly three times in each raw target list;
- canonical SHA256 of the sorted unique 99-coordinate identity:
  `a44a8921e3c10b17cdf222b97d18524454e927dadeea30b13e75c3a0d6fc42fc`;
- canonical SHA256 of the exact raw 297-entry per-call target list:
  `e5bcdcb7fbb802b24469d8e3f1965013dc35b3b9249868476cf22490456f344a`.

The numerical source contract uses the 99 unique coordinates to form the M300/D58 requested-node batches, but the persisted per-call `mixed_target` and `direct_target` source arrays preserve the exact 297-entry source target list.

Therefore this replication gate MUST retain all 297 persisted source entries per call. It MUST NOT deduplicate, subset, reweight, average or otherwise reduce them before atom-level response construction.

The 99-coordinate identity is a provenance identity; the 297-entry vectors are the scientific source arrays.

## 5. Structural source authority

The frozen numerical implementation binds:

- `M300 -> calls 377..440`;
- `M300 -> direct D58`;
- M300 mixed requested-node count: `996`;
- D58 direct requested-node count: `99`;
- source-array dtype: `<f8`;
- M300 per-call source-array shape: `[297]`;
- M300 per-call source-array byte length: `2376`.

The exact source code identities are:

- numerical executor blob `ca4307962c0e92dd4bf5d74e76dd4e6db27c10d1`;
- contract-audit blob `9109f2e2bcc6146fa62e423e145ad09a67b70b0c`.

Response-blind structural inspection of all 32 immutable lane receipts established exactly 256 M300 source arrays per lane and 8,192 selected manifest entries in total, all with the same raw-target identity SHA256 above. No NPZ scientific values were read for this design.

## 6. Exact source arrays

For every replicate `Rxx` and every call `CCC in 377..440`, use only:

- `mixed_target__M300__beta_plus__callCCC`
- `mixed_target__M300__beta_minus__callCCC`
- `direct_target__M300__beta_plus__callCCC`
- `direct_target__M300__beta_minus__callCCC`.

This freezes:

- 256 source arrays per lane;
- 8,192 source arrays over the 32-lane population.

No other numerical arrays may influence the classifier.

## 7. Provenance before arithmetic

Before any plus/minus arithmetic occurs, bind every selected source array through:

- source numerical run `35280281867`;
- exact lane artifact ID/name/outer digest;
- exact lane receipt and eligible lane identity;
- witness NPZ SHA256;
- manifest canonical SHA256;
- array name;
- selection `M300`;
- direct batch `D58` for direct arrays;
- beta role;
- call index;
- z identity;
- shape `[297]`;
- dtype `<f8`;
- byte length `2376`;
- per-array SHA256;
- raw-target identity SHA256 `e5bcdcb7fbb802b24469d8e3f1965013dc35b3b9249868476cf22490456f344a`.

All 8,192 bindings must pass before any M300 scientific response arithmetic.

If provenance fails, classify `PROVENANCE_FAIL`. Do not construct a partial response first.

## 8. Frozen response construction

Preserve the source-authoritative response used for the terminal DES gate:

- `h = 1e-4`;
- `beta_plus=(0,+h)`;
- `beta_minus=(0,-h)`;
- component: `abs_dDelta_m_dbeta_symmetric`;
- atom-level formula:
  `R = abs((beta_plus - beta_minus) / (2*h))`.

Construct separately for every lane and call:

- `R_mixed[replicate, call, 297-source-entry]`;
- `R_direct[replicate, call, 297-source-entry]`.

Frozen shapes after construction are therefore:

- per lane/per construction: `[64,297]`;
- response atoms per lane/per construction: `19,008`;
- response atoms across 32 lanes/per construction: `608,256`;
- combined mixed + direct atoms checked: `1,216,512`.

No averaging, call aggregation or target reduction is allowed before atom-level construction and validation.

## 9. Finite-positive replication condition

To replicate the DES gate's scoped existence condition, every preregistered M300 response atom in both constructions must be:

- finite;
- strictly `> 0`.

This is an existence condition only. It is NOT a physical amplitude threshold or significance threshold.

One zero or nonfinite required atom is sufficient for terminal `SCIENTIFIC_RESPONSE_ZERO_OR_NONFINITE`.

## 10. Technical response reproducibility

Freeze the inherited strict technical tolerance:

`< 1e-5`.

For each of `R_mixed` and `R_direct`, compute across the complete `[64,297]` response tensor:

1. cross-host maximum pairwise relative spread over exactly `R01..R32`;
2. native-class mean relative separation between the frozen 10 active and 22 inactive lanes.

Each metric must be strictly `<1e-5`.

Take maxima over all calls and all 297 source entries. A failure at one call/entry is not hidden by averaging across calls.

Execution-order arm may be recorded descriptively if available, but it is not added as a new scientific pass criterion because it was not a pass criterion of the DES M298 scientific gate.

## 11. Mixed/direct scientific construction agreement

For every lane, compare the complete mixed and direct `[64,297]` response tensors atom by atom using:

`abs(a-b) / max(abs(a), abs(b), float64_tiny)`.

Freeze the inherited scientific construction-agreement threshold:

strict `< 1e-3`.

The gate metric is the maximum over all 32 lanes, all 64 calls and all 297 source entries.

This `1e-3` threshold is NOT a signal-detection, effect-size or significance threshold.

## 12. No DES-vs-BOSS amplitude matching

This replication gate asks whether the same scoped **response-existence / reproducibility / construction-stability properties** survive the switch from DES to BOSS.

It does NOT require M300 response amplitudes to equal M298 response amplitudes, and it freezes no DES/BOSS amplitude-ratio threshold.

Do not create one after observing M300.

## 13. Frozen terminal taxonomy

Only these outcomes are allowed:

- `PASS_SCOPED_BOSS_M300_CROSS_SURVEY_RESPONSE_REPLICATION`
- `SCIENTIFIC_RESPONSE_ZERO_OR_NONFINITE`
- `SCIENTIFIC_RESPONSE_REPRODUCIBILITY_FAIL`
- `SCIENTIFIC_RESPONSE_CONSTRUCTION_MISMATCH`
- `PROVENANCE_FAIL`
- `INVALID_IMPLEMENTATION`.

No rescue category may be added after outcome inspection.

## 14. Response-blind design firewall

During preregistration/design/static review:

- `M300_response_read = false`;
- `scientific_classifier_invoked = false`;
- `response_dependent_selection = false`;
- `covariance_read = false`;
- `nuisance_read = false`;
- `new_CLASS_solves = 0`.

It is forbidden to:

- combine M300 beta-plus/minus arrays;
- inspect M300 response amplitudes;
- choose a favorable call;
- choose a favorable target;
- remove repeated target entries based on outcome;
- calculate M300 scientific pass/fail metrics.

## 15. Claim ceiling

A future PASS could support only:

**the response-existence, technical-reproducibility and mixed/direct construction-stability behavior observed prospectively on DES M298 also replicates on the complete frozen BOSS M300 family in this tested scope.**

A PASS would NOT establish:

- all DES+BOSS rows valid;
- statistical significance;
- covariance validity;
- nuisance robustness;
- dark-sector detection;
- physical universality;
- full107 validity.

## 16. Chronology

The legal chronology is:

1. preregistration on `main`;
2. machine-readable design authority;
3. independent static design Critic;
4. STOP and re-read durable recovery/authorization;
5. implementation may be authored only under a later explicit durable authority;
6. scientific execution requires a later separate execution authority and one-shot identity.

This preregistration itself authorizes no M300 response construction.

## 17. Post-design stop rule

After design static Critic PASS, do not author or execute a response constructor merely because the design passed.

Implementation and execution remain CLOSED until separately authorized by durable repository state.

Scientific bookkeeping remains `+0/+0`.

