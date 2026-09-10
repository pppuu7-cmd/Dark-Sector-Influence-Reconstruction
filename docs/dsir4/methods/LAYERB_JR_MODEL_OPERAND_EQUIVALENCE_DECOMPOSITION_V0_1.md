# Layer-B JR model-operand equivalence decomposition v0.1

Date: 2026-09-11. Scope: DSIR Article III process/support only. Effect `+0/+0`.

This note is frozen after the Exp073JR v0.1 fine job suffered an external runner shutdown before producing any numerical result and while the v0.1 coarse job was still running. It does not inspect or use a JR numerical response value.

## Problem

JR v0.1 directly compares the original four-live-instance response engine with a one-live-instance-at-a-time candidate. For one lattice job this requires eight CLASS constructions/solves: four simultaneously retained reference instances plus four sequential candidate instances. The 4097-node job was externally terminated during that numerical step before any equality verdict or result artifact existed.

The exact-equivalence question can be decomposed without weakening the exact criterion.

## Frozen response algebra

For target vectors `r`, `a`, `bp`, `bm` corresponding respectively to reference `(0,0)`, alpha-minus `(-h,0)`, beta-plus `(0,+h)` and beta-minus `(0,-h)`, the existing JL/JJ response is exactly

```python
np.column_stack((
    np.abs((a-r)/(-h)),
    np.abs((bp-bm)/(2*h)),
))
```

with `h=1e-4` and the existing NumPy/binary64 environment.

Let superscripts `F` and `S` denote target vectors obtained from the original four-live reference context and the candidate single-live context in the same hosted job. If

`r^F == r^S`, `a^F == a^S`, `bp^F == bp^S`, and `bm^F == bm^S`

all hold byte-for-byte as contiguous `<f8` arrays, then substituting identical binary64 operands into the same frozen response expression produces identical binary64 response arrays. No tolerance argument is involved.

## Per-model same-job control

A resource-safe preflight may therefore use one job per frozen model role. In each job:

1. construct all four reference CLASS instances in the original fixed order, retaining all four live exactly as in the original response engine;
2. after all four exist, query only the matrix-selected reference instance at the frozen JR requests and serialize the interpolated target vector(s) as contiguous `<f8`;
3. destroy all four reference instances;
4. construct only the same selected model as a single candidate instance, query the exact same request(s), and serialize identically;
5. require `np.array_equal`, byte SHA256 equality, equal finite/positive masks, zero unsupported targets and lookup mismatch <= `1e-12`.

Thus each job uses five CLASS constructions rather than eight while still comparing the selected model under the true original four-live coexistence context against the single-live candidate context. Four model jobs jointly establish exact equality of all operands required by the frozen response expression.

## Scope ceiling

This decomposition is a process theorem only. It does not itself repair or supersede JR v0.1, does not authorize recovered JL, and does not change Article III/funnel readiness. Any replacement JR contract must be prospectively frozen before its numerical outputs and must bind all four model-role receipts, both JL lattices and both frozen JR requests. A missing, cancelled or mismatched receipt fails closed as infrastructure-invalid; no majority vote or approximate equality is allowed.