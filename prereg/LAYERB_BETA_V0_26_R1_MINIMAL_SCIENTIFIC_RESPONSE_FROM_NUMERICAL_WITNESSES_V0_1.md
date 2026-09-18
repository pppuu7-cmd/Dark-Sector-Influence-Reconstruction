# DSIR V0.26 R1 — prospective minimal scientific response from frozen numerical witnesses v0.1

Status: **PREREGISTERED DESIGN ONLY — NOT AUTHORIZED FOR RESPONSE CONSTRUCTION OR EXECUTION**

Date: 2026-09-18

## 1. Terminal parent

This preregistration is admissible only because the minimal response-blind numerical reproducibility gate is terminally closed by:

- run `35280281867`, run #1 / attempt #1, head `6ba39aeade5b0603c02ea3d0fc7f8167c11c240a`;
- producer classification `PASS_SCOPED_MINIMAL_NUMERICAL_REPRODUCIBILITY_QUALIFIED`;
- independent runtime Critic git blob `9f19f8cc643bc978d0dbbcdd58f80fdf04395e24`, verdict `CONFIRMED_SCOPED`.

The numerical run is consumed and MUST NOT be rerun.

## 2. Gate question

**Does one response-blind, source-authoritative beta exact-target object already present in the immutable numerical witnesses yield a finite positive response that is reproducible across the frozen 32-lane population and agrees between mixed exact-target-union and fresh direct exact-target construction under the frozen scientific tolerance?**

This is a minimal scientific-response existence/stability gate only. It is not a statistical-significance, nuisance, covariance, model-selection or dark-sector inference gate.

## 3. Why this object is frozen prospectively

Freeze exactly `M298 / call375` from the already-preregistered numerical sentinel:

- mixed batch: `M298`;
- exact call index: `375`;
- exact target count: `244`;
- mixed requested-node count: `1141`;
- direct comparator: `D00`;
- direct target capacity: `1152`;
- replicate set: exactly `R01..R32`.

Selection is response-blind. Among the three already frozen sentinel selections, `M298` contains one call, whereas `M076` contains two calls and `M300` contains 64 BOSS calls. It therefore minimizes the number of scientific response objects while retaining a large exact-target vector and a pre-existing mixed/direct comparator. No response value has been read or constructed to make this selection.

## 4. Immutable source objects

For every replicate `Rxx`, consume only the immutable lane artifact from run `35280281867` and exactly these four raw witness arrays:

- `mixed_target__M298__beta_plus__call375`
- `mixed_target__M298__beta_minus__call375`
- `direct_target__M298__beta_plus__call375`
- `direct_target__M298__beta_minus__call375`

Each source array MUST be bound through its lane receipt, NPZ SHA256, manifest SHA256, shape, dtype `<f8`, byte length and per-array SHA256 before response construction.

No new CLASS solve is permitted in this gate.

## 5. Frozen response construction

Freeze:

- `h = 1e-4`;
- beta roles = `beta_plus=(0,+h)`, `beta_minus=(0,-h)`;
- response component = `abs_dDelta_m_dbeta_symmetric`;
- for each target scalar:
  `R = abs((d_m(beta_plus) - d_m(beta_minus)) / (2*h))`.

Construct separately:

- `R_mixed` from the two `mixed_target` arrays;
- `R_direct` from the two `direct_target` arrays.

No interpolation, smoothing, clipping, renormalization, covariance, whitening, nuisance fit, relation-null, `Wm_S3`, global65537 or row aggregation is allowed.

## 6. Frozen thresholds and comparisons

Technical reproducibility threshold:

- strict `< 1e-5`.

Scientific construction-agreement threshold:

- strict `< 1e-3`.

For each of `R_mixed` and `R_direct`, require:

- all 244 values finite;
- all 244 values strictly `> 0`;
- cross-host max pairwise relative spread over the exact 32 frozen replicates `<1e-5`;
- native-class mean relative separation `<1e-5`.

For each replicate require mixed-vs-direct response agreement:

`max(abs(R_mixed - R_direct) / max(abs(R_mixed), abs(R_direct), float64_tiny)) < 1e-3`.

The strict `1e-3` criterion is the inherited scientific relative tolerance. It is not an amplitude/significance threshold.

## 7. Nontrivial-response definition and claim ceiling

For this minimal gate only, "nonzero response" means exactly: every preregistered response atom is finite and strictly positive under the inherited source semantic parent.

This gate does **not** define a minimum physically meaningful amplitude and does not test statistical significance. A positive result therefore supports only the existence and numerical/scientific-construction stability of this minimal response object.

Nuisance-like response is explicitly **NOT_EVALUATED** because nuisance information remains closed and may not be read in this gate.

## 8. Frozen terminal taxonomy

Only these outcomes are allowed:

- `PASS_SCOPED_MINIMAL_SCIENTIFIC_RESPONSE_REPRODUCIBLE_NONZERO`
- `SCIENTIFIC_RESPONSE_ZERO_OR_NONFINITE`
- `SCIENTIFIC_RESPONSE_REPRODUCIBILITY_FAIL`
- `SCIENTIFIC_RESPONSE_CONSTRUCTION_MISMATCH`
- `PROVENANCE_FAIL`
- `INVALID_IMPLEMENTATION`

No post-outcome relabeling or new convenient category is permitted.

## 9. Response-blind chronology firewall

Before any of the four plus/minus arrays are combined into a response:

1. this preregistration must exist on `main`;
2. a machine-readable design authority must bind its git blob;
3. an independent static Critic must pass;
4. a separate implementation identity and execution authority must be frozen;
5. only then may one response-construction run be launched.

Until then:

- `scientific_response_read = false`;
- `scientific_classifier_invoked = false`;
- `covariance_read = false`;
- `nuisance_read = false`;
- `response_dependent_selection = false`.

## 10. Post-PASS ceiling

A PASS does not authorize full107.

After PASS, the dependency DAG must be recalculated. Same-realization exact-target expansion, bounded data expansion, covariance, whitening, nuisance marginalization, null models, systematics, full107, statistical/model validity and physical dark-sector inference all require separate prospective authorities.

Scientific effect remains `+0/+0` until this gate is actually executed.
