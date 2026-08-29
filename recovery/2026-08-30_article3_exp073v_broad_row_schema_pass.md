# DSIR recovery checkpoint — Article 3 Exp073V broad-row schema PASS

**Checkpoint:** 2026-08-30 UTC

## State transition

The Article-3 broad-observation representation ambiguity is now prospectively closed without scoring any real support result.

Before Exp073V, the architecture had a mismatch:

- Exp073U correctly froze 1410 finite observation-row identities without scalar `(z,k)` proxies;
- Layer A correctly required broad operator-support leakage;
- the older Layer-B synthetic schema still expected one scalar row-level `z` and `k_Mpc^-1`.

That mismatch could have forced an invalid effective-`(z,k)` reduction for broad Wm/WW pseudo-`C_ell` bandpowers or BOSS finite-matrix rows.

Exp073V freezes and tests the corrected broad-row representation before any real Layer-A/Layer-B outcome is inspected.

## Frozen representation amendment

Document:

`docs/ARTICLE3_BROAD_ROW_LAYERB_SCHEMA_AMENDMENT_2026-08-30.md`

Introduction commit:

`1bfc556ec16ea9c55cd47e60742890e435270a31`

Core distinction:

- **observation row** = immutable measured coordinate/covariance row with Exp073U `coordinate_id` and `ordinal`;
- **physical support atom** = deterministic finite operator/quadrature cell carrying canonical `(z,k)`, non-negative absolute support weight, and ordered common-response values.

For current Wm/WW/BOSS rows, row-level scalar `z`, scalar `k`, effective `ell`, effective `z`, effective `k`, weighted-mean/centroid/midpoint `k` are forbidden.

Layer A evaluates the unchanged physical domain on broad support atoms:

`0.295 <= z <= 2.33`, `0 < k <= 0.06664762008318016 Mpc^-1`, `operator_f_invalid <= 0.05` inclusive.

Layer B receives only Layer-A-retained rows and verifies finite strictly positive common response on every active in-domain support atom. Its row-count invalid fraction remains bounded by `<=0.05`, with minimum final observation dimension `15`.

Covariance remains blocked until **both** real Layer A and real Layer B pass on the same inherited authority.

## Exp073V preregistration and implementation

Preregistration:

`experiments/073v_article3_broad_row_support_schema_synthetic_v0_1_prereg.md`

Preregistration commit:

`f8ff9dba44685d00ab3b3803e60dfa6d66b7b135`

Implementation:

`ci/exp073v_article3_broad_row_support_schema_synthetic_v0_1.py`

Implementation commit:

`3f574bfd52b29ad2e5ed1813a1487af2bfc18c5c`

Workflow:

`.github/workflows/exp073v-article3-broad-row-support-schema-synthetic-v0-1.yml`

Workflow introduction commit:

`e4314c491bf9c7a55ac639542c6551861ff20588`

Workflow freeze:

`experiments/073v_article3_broad_row_support_schema_synthetic_v0_1_workflow_freeze.md`

Trigger/head:

`187c8cd14cbb882282287d7eca81223ba15302a8`

## Hosted authority

- workflow run: `33275479258`
- job: `99161308291`
- conclusion: `success`
- artifact: `9721353934`
- artifact name: `exp073v-broad-row-schema-synthetic-187c8cd14cbb882282287d7eca81223ba15302a8`
- artifact ZIP digest: `sha256:287aa65b3f6f30200466049c7af20112009afd8507718b9e308462a169769505`
- internal JSON SHA256: `504db54cacc23cd301c13e856839244f2a095c033278f39fc0bf11093260fc25`
- positive token: `PASS_EXP073V_ARTICLE3_BROAD_ROW_SUPPORT_SCHEMA_SYNTHETIC_V0_1`

All workflow steps passed, including prospective freeze enforcement, 19 synthetic architecture controls, the non-classifying firewall and artifact upload.

## What the 19 controls established

The synthetic gate verifies, before real survey support scoring:

1. broad-row baseline Layer-A/Layer-B semantics are internally consistent;
2. inherited ordinal order makes input permutation irrelevant;
3. row-level scalar `k` is rejected;
4. row-level effective `z` is rejected;
5. weighted-mean `k` can lie inside the domain while broad support leakage exceeds 5%, and the broad row is correctly rejected;
6. Layer-A exact 5% boundary passes;
7. Layer-A value above 5% rejects;
8. exact physical domain boundaries are inclusive;
9. Layer-A row PASS does not imply common-response validity;
10. Layer-B exact 5% row-invalid fraction passes;
11. Layer-B value above 5% fails;
12. exactly 15 final observation rows passes;
13. 14 rows blocks Layer B;
14. positive response-amplitude rescaling does not alter retention;
15. zero operator normalization is INVALID_FOR_SCIENCE;
16. duplicate ID is invalid;
17. duplicate ordinal is invalid;
18. downstream covariance leakage is invalid;
19. wrong Exp073U order authority is invalid.

## Scientific accounting

Article 3 strict scientific repository readiness remains **52%**.

Exp073V earns **no scientific-readiness credit** because it is synthetic architecture QA. It does not evaluate real Wm/WW/BOSS support, does not compute a real `S_op`, and does not authorize covariance.

Gate state remains:

- Layer A: OPEN;
- Layer B: OPEN;
- covariance/whitening: BLOCKED;
- G7: OPEN;
- G8: OPEN;
- G9: OPEN.

## Newly sharpened real-data dependency

The real broad pre-support producer must now bind content-hashed physical arrays rather than scalar row coordinates.

### DES Wm/WW

Required real object:

`pinned NaMaster bandpower window x exact released redshift-kernel quadrature`

with classifying `nside=4096`, frozen bandpower edges, Wm=`TE`, WW=`EE`, positive absolute support envelope, signed measured Wm, and no fiducial `P(k)` weighting.

### BOSS

The previous finite-matrix audit binds the true-`k` geometry `C=W@M`, but its historical 54/240 result was only a k-support component audit. The real broad `(z,k)` producer must additionally bind the actual survey-redshift support/provenance for the selected BOSS z-bin. An effective-redshift point is not sufficient.

This is an implementation/provenance dependency, not a scientific failure.

## Current authorized order

`exact hosted R1 + Exp073P receipt`

`-> Exp073U immutable 1410-row order`

`-> Exp073V broad-row schema PASS`

`-> bind exact DES Wm/WW physical support atoms + exact BOSS true-k x redshift support atoms`

`-> content-hash/freeze the full pre-support broad operator`

`-> real Layer A`

`-> freeze S_op`

`-> real Layer B`

`-> retained finite operator`

`-> covariance restriction / whitening`

`-> nuisance quotient`

`-> relation/null`

`-> fresh G8`.

## Next research action

Audit and freeze the missing **BOSS redshift-support provenance** and, in parallel, define the exact DES kernel quadrature/array serialization needed by the real broad operator producer. No real support score should be run until both block representations are complete and content-hashed.
