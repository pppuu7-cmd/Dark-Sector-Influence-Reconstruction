# DSIR V0.26 R1 — DES M076 remaining-sentinel response replication falsifier v0.1

Status: **PREREGISTERED DESIGN ONLY — NO M076 RESPONSE CONSTRUCTION OR EXECUTION AUTHORIZED**

Date: 2026-09-19

## 1. Terminal parents

This gate is admissible only after both prior prospectively frozen scientific response gates are terminally closed:

- DES M298/call375 terminal authority blob `7ea2cefde247845d4c6d70660b798dcaa79a4a72`;
- DES M298 runtime Critic blob `91fb97a73a820cf5172d7e0383752a1ee6a26143`, verdict `PASS_TERMINAL_CLOSURE`;
- BOSS M300 terminal authority blob `e7e94650dd75b2a148717e241a907761fdbdbcda`;
- BOSS M300 runtime Critic blob `5c54869af9c5bf157d2ec857ca1623b763a0d7d3`, verdict `PASS_TERMINAL_CLOSURE`.

The numerical source remains consumed run `35280281867`. It MUST NOT be rerun. No new CLASS solve is permitted.

## 2. Scientific question

**Does the remaining frozen DES sentinel family M076 reproduce the finite-positive, technically reproducible, mixed/direct construction-stable beta-response behavior already established prospectively on DES M298 and BOSS M300?**

This is a counterexample-first replication gate over a different DES packing/comparator geometry. It is not an attempt to optimize for PASS.

## 3. Frozen M076 object

Use exactly:

- survey/data block: DES;
- mixed selection: `M076`;
- direct comparator batch: `D50`;
- calls: exactly `[76,78]`, in that order;
- call count: 2;
- frozen lane population: exactly `R01..R32`;
- native population inherited from the numerical run: 10 `NATIVE_AVX512_ACTIVE` + 22 `NATIVE_AVX512_INACTIVE`;
- order arms: 16 A + 16 B;
- new CLASS solves: 0.

No call may be dropped after outcome inspection.

## 4. Exact target identities

Frozen plan and all 32 immutable receipts establish:

Call 76:
- z u64hex: `3fdf851eb851eb85`;
- persisted target entries: `127`;
- exact target-list SHA256:
  `661250b46dfc123a84fb8bfe908893780d419ebf5ba8ee51b83e24e826e26198`.

Call 78:
- z u64hex: `3fdfafb7e90ff972`;
- persisted target entries: `128`;
- exact target-list SHA256:
  `1969c1c6e83087e5408b19fb948d52ce9f91caf163969a66d7bd6647323aa57c`.

The two target lists are disjoint.

Frozen ordered union:
- exact atom count: `255`;
- canonical sorted-union SHA256:
  `bc86d3e98ff1e7d79bb8b3057e2a810b9dbaffd82f8c552cf781ffa52fd07df3`.

The persisted scientific source arrays remain call-specific and MUST retain shapes `[127]` and `[128]`. No target subsetting, deduplication, reweighting or cross-call averaging is allowed.

## 5. Structural source contract

The frozen numerical design binds:

- mixed requested-node count for M076: `1152`;
- direct comparator: `D50`;
- D50 requested-node/target-only count: `1146`;
- exact per-call arrays:
  - `mixed_target__M076__beta_plus__call076`;
  - `mixed_target__M076__beta_minus__call076`;
  - `direct_target__M076__beta_plus__call076`;
  - `direct_target__M076__beta_minus__call076`;
  - same four roles for call078.

Thus:
- 8 selected arrays per lane;
- 256 selected arrays over R01..R32.

Response-blind structural audit of all 32 receipts verified those identities without opening NPZ scientific values.

## 6. Provenance-before-arithmetic

Before any beta plus/minus arithmetic, every selected array must bind through:

- source run `35280281867`;
- exact lane artifact ID/name/outer SHA256;
- exact lane receipt;
- witness NPZ SHA256;
- witness manifest canonical SHA256;
- kind;
- selection `M076`;
- direct batch `D50` for direct arrays;
- role;
- call index;
- exact z u64hex;
- exact call-specific target SHA256;
- exact shape;
- dtype `<f8`;
- exact byte length;
- per-array SHA256.

All 256 bindings must pass before response construction.

## 7. Frozen response construction

Preserve the source-authoritative construction used by M298 and M300:

`R = abs((beta_plus-beta_minus)/(2*h))`

with:

`h = 1e-4`.

Construct mixed and direct independently for each lane and each call.

Keep call-specific tensors:
- call076 shape `[127]`;
- call078 shape `[128]`.

For atomwise max metrics only, concatenate in frozen call order `[76,78]` into one `[255]` vector per lane/construction. This concatenation performs no averaging or target reduction and preserves a deterministic inverse map back to exact call + source-entry index.

Per construction:
- 255 atoms per lane;
- 8,160 atoms across 32 lanes.

Combined mixed+direct:
- 16,320 required response atoms.

## 8. Finite-positive replication condition

Every required mixed and direct atom must be:
- finite;
- strictly `>0`.

One zero or nonfinite required atom is sufficient for:
`SCIENTIFIC_RESPONSE_ZERO_OR_NONFINITE`.

This is an existence condition, not an effect-size/significance threshold.

## 9. Technical reproducibility

Freeze the inherited strict technical threshold:

`<1e-5`.

For both mixed and direct complete 255-atom vectors:
- cross-host maximum pairwise relative spread over R01..R32 must be strict `<1e-5`;
- native-class mean relative separation between the frozen 10 active and 22 inactive lanes must be strict `<1e-5`.

Execution-order arm separation may be reported descriptively but is not a new scientific pass criterion.

## 10. Mixed/direct construction agreement

For every lane and every atom:

`abs(a-b)/max(abs(a),abs(b),float64_tiny)`

must have global maximum strict `<1e-3`.

The `1e-3` number is a construction-agreement criterion, not a physical significance threshold.

## 11. No amplitude matching

Do not require M076 amplitudes to match M298 or M300 amplitudes.

This gate tests replication of:
- finite-positive response existence;
- host/native technical reproducibility;
- mixed/direct construction stability.

It does not test cross-object amplitude equality.

## 12. Frozen terminal taxonomy

Only:

- `PASS_SCOPED_DES_M076_REMAINING_SENTINEL_RESPONSE_REPLICATION`
- `SCIENTIFIC_RESPONSE_ZERO_OR_NONFINITE`
- `SCIENTIFIC_RESPONSE_REPRODUCIBILITY_FAIL`
- `SCIENTIFIC_RESPONSE_CONSTRUCTION_MISMATCH`
- `PROVENANCE_FAIL`
- `INVALID_IMPLEMENTATION`.

No rescue category may be added after response inspection.

## 13. Failure witness rule

If the future execution fails scientifically, persist the lexicographically smallest exact witness under:
- lane order R01..R32;
- call order 76 then 78;
- source-entry index ascending;
- mixed before direct where applicable.

Persist:
- failure class;
- lane/context;
- call;
- source-entry index;
- mixed/direct values as applicable;
- observed relative difference as applicable.

Do not cherry-pick another subset.

## 14. Response-blind design firewall

During prereg/design/static review:
- `M076_response_read=false`;
- `scientific_classifier_invoked=false`;
- `response_dependent_selection=false`;
- `covariance_read=false`;
- `nuisance_read=false`;
- `new_CLASS_solves=0`.

Do not open NPZ M076 values or combine beta plus/minus before a later execution authority.

## 15. Claim ceiling

A future PASS would establish only that the tested scoped response-existence/reproducibility/construction-stability behavior also holds on the remaining frozen DES M076 sentinel family.

It would NOT establish:
- statistical significance;
- covariance validity;
- nuisance robustness;
- full107 validity;
- dark-sector detection;
- physical dark-sector inference;
- new physics.

Scientific bookkeeping remains `+0/+0`.

