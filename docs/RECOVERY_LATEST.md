# DSIR authoritative recovery — latest

Updated: 2026-09-11. Scope: **DSIR only**. Never mix RTK, RQIR, KMQGB or KMDSB.

Newest immutable current-front recovery note: `docs/recovery/RECOVERY_2026-09-11_ARTICLE3_32769_STATIC_CANONICALIZATION_CLOSED_V126.md`, creation commit `4a472a65ffbaa86d9a3c5c7aff5997ddd6b91bc6`. V125 and all earlier recovery notes remain immutable history; V126 supersedes them for current-front recovery.

## Scientific frontier — unchanged
Canonical 8193->16385 remains independently verified `COMMON_GRID_NEXT_REFINEMENT_NOT_CONVERGED_PLUS_0_PLUS_0`, max relative component difference `0.012484060640679777` versus frozen strict `<1e-3`. Frozen `REL_TOL=1e-3`, `h=1e-4`, native kpd20, centered-cubic interpolation, physical domain/masks/107-row accounting, invalid fraction `<=0.05`, retained `>=15`, unsupported=0 and lookup `<=1e-12` remain unchanged.

No 16385->32769 scientific execution is authorized. Covariance restriction remains unauthorized. Wm_S3 remains unopened.

## Cancellation / numerical-conditioning diagnosis — support-complete
The top-64 branch is closed for the current Article III cycle. The single permitted unchanged retry `34614119149`, attempt 2/job `103331912096`, reproduced all 64 ordered atoms at the primary guard and found `21/64 >=1e-3`. Corrected confounder run `34628562363` and independent consumer `34628673923` established `64 -> 58` unique physical atoms, collapsed Spearman `-0.5163800793626381`, DES-only Spearman `-0.5078643578643579`, and cancellation-scale quartile exceedances `13/16`, `6/16`, `1/16`, `1/16`.

These results support a distributed finite-difference cancellation/ill-conditioning diagnosis but remain support-only `+0/+0` and do not rescue the scientific convergence gate.

## 32769 next-rung preflight — static canonicalization closed
V126 closed the response-blind canonical-bytes prerequisite without invoking CLASS or reading a 32769 scientific response.

Source run `34630453409` used the inherited frozen `guarded_lattice(n)` semantics under exact NumPy 1.26.4. Five of eight replicas `[1,4,5,7,8]` reproduced the canonical 16385 anchor and emitted byte-identical 32769 candidates; replicas `[2,3,6]` were retained as host variants. Independent consumer run `34630559826` revalidated the canonical payload.

Canonical 32769 identities:
- requested nodes: `32769`;
- guard counts: `[0,1]`;
- node-payload SHA256: `82c48c17dba812bd08a3437f7e48376208a8c506f4a63087191608793fba4599`;
- u64hex/text SHA256: `7422d00aab2b32a060878224e81834277a67d42016595a0e9088db05b14166e2`;
- durable file: `docs/dsir4/canonical/LAYERB_CANONICAL_FINE_32769_NODES_U64HEX_V0_1.txt`;
- materialization commit: `68a37d43a3496e9f0d760c66bcb494ea520aa13e`;
- Git blob: `7b67706156d7d2016ecba0628210fb08f6f05616`;
- durable authority: `docs/dsir4/authority/LAYERB_RESPONSE_BLIND_CANONICAL_FINE_32769_V0_1.json`, creation commit `b49b0d0065be2878644c9b81a23b4741e80e4387`.

This is support-only `+0/+0`: `CANONICAL_32769_BYTES_FROZEN=TRUE`, while `32769_EXECUTION_AUTHORIZED=FALSE` and `scientific_authority_created=false`.

## Remaining production blockers
The validated 16385 CLASS build point capacity is `18432`, insufficient for 32769. A new capacity-only CLASS patch with point capacity `>=32769`, exact source/patch identities, parser/build parity and independent scientific-equivalence audit is still required.

Ordinary GitHub-hosted `ubuntu-24.04` is not an admissible inferred 32769 production topology: the canonical 16385 hosted-memory audit exhausted memory in all four roles at roughly 15.4--15.7 GB Python RSS. No 32769 memory requirement is extrapolated from that result. A higher-memory candidate topology must be validated response-blind for resource/lifecycle feasibility before any separate one-run scientific authorization may be considered.

## Ownership / Actions
No duplicate heavy science lane is authorized. Stale superseded self-hosted run `34550495778 / 103112190909` must not receive home-runner ownership.

## Readiness
**ARTICLE3_REPOSITORY_READINESS: 68%.** Funnel-freeze readiness: **67%**.

The percentages remain unchanged because V126 closes static reproducibility/preflight infrastructure rather than the frozen scientific convergence gate.

## Exact next action
Freeze and independently audit the `>=32769` CLASS capacity-only build prerequisite. In parallel, identify and validate a higher-memory resource/lifecycle topology without reading the 32769 scientific response. Preserve exact base CLASS commit and patch hashes, parser/build parity, scientific-equivalence invariants and fail-closed anti-duplication. Only after both prerequisites close may a separate explicit one-run 16385->32769 scientific authorization be considered.
