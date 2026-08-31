# Article-3 general-coupling elision audit — 2026-08-31

**Status:** nonclassifying prerequisite / execution-engineering audit only.  
**Readiness effect:** `+0 Verified / +0 Draft-data`.  
**Active authority:** Exp073BJ run `33379013167` is unchanged by this document.

## Live BJ snapshot at audit time

Both full-scale compact jobs remain after all frozen binding gates:

- replica A job `99446854065`: prospective freeze PASS; exact NaMaster 2.7 lineage PASS; immutable BI/AZ downloads PASS; exact BI_Q1 + Exp073AZ canonical-PCL binding PASS; currently inside `Compute two-thread compact Wm_S1 replica`;
- replica B job `99446854363`: same frozen gates PASS; currently inside the same compact computation.

No BJ artifact and no exact compact-comparator classification existed at this audit snapshot. Therefore there is no BJ scientific PASS/FAIL to reinterpret.

## Dense-output lower bound

For the frozen true-ell range `0..12287`, `nl = 12288`. A single scalar dense `nl x nl` float64 matrix contains

`12288^2 = 150,994,944` doubles,

or `1,207,959,552` bytes = exactly `1.125 GiB`, before native work arrays, allocator overhead, copies, spin-component bookkeeping, Python/Numpy objects, or later compressed arrays.

The useful frozen compact projected object has shape `[39,12288]` = `479,232` doubles, about `3.66 MiB`. Thus the retained scalar payload is roughly 315 times smaller than one dense scalar `12288 x 12288` matrix. This ratio is a storage observation only; it is not a proof of an achievable runtime reduction.

## Public-API audit: negative results

Inspection of the documented NaMaster 2.7 workspace API gives two important negative results.

1. **Slice/chunk after `get_general_coupling_matrix` does not elide dense construction.** The public call materializes and returns the full general-coupling matrix. Python-side slicing or block consumption after that return occurs too late to remove the original dense allocation/construction cost.
2. **`NmtWorkspace.couple_cell` is not a construction-streaming replacement.** It applies coupling through an already constructed workspace/coupling operator; it does not expose a documented row/block iterator that constructs only the projected bands required by the frozen low-memory path.

No documented public block/row streaming interface for `get_general_coupling_matrix` was identified in this audit. Therefore a successor that merely wraps the current public call in Python chunking would not address the observed dense-construction bottleneck and is rejected as a meaningful elision strategy.

## Candidate future route — plausible, unqualified

A future execution successor may investigate a **direct band-projected general-coupling accumulator** that computes only the frozen projected quantity needed downstream rather than first materializing the full dense operator. This is an engineering hypothesis, not an authorized scientific route.

Before any classifying use it must be prospectively frozen and independently qualified against the current reference implementation on deterministic tractable cases. The qualification must preserve the exact frozen mathematical object and must explicitly test independent-process repeatability. A change in accumulation/summation order can change floating-point bits, so numerical closeness cannot substitute for the frozen exact comparator. No tolerance, ULP, rounding, averaging, majority vote or preferred-replica rescue is permitted for scientific classification.

A native/source-level implementation may be necessary if the documented public API cannot expose the required partial construction. That path requires source-level provenance and a separate code-equivalence gate before a full-scale Track-A successor.

## Runtime caveat

Eliminating retained dense storage does **not** by itself prove a CPU speedup. If every native coupling element is still evaluated, runtime may remain comparable even if peak memory falls. A genuine speedup would require avoiding or reorganizing native work, which creates an additional numerical-equivalence/repeatability risk and therefore must be qualified prospectively.

This is consistent with the existing local numerical-structure audit: provisional real-DES Wm_S2 has `cond_2(K)=2.1928888836909883`, and its 39x39 finalizer solve is well conditioned. The observed multi-hour cost is therefore not explained by the small `solve(K,A)` stage.

## Frozen boundaries preserved

This audit changes no Exp073BJ code, workflow, preregistration, binding receipt, timeout, thread policy, scientific criterion or artifact route. Exp073AQ remains the permanent historical exact-repeatability scientific FAIL. The Article-3 anti-leakage firewall, dual-readiness accounting and G7 ordering remain unchanged; G8 is not authorized.

## Exact next gate

The authority gate remains the terminal Exp073BJ compact A/B outcome. Two complete valid compact artifacts must reach the frozen exact comparator. Exact compact mismatch is the prospectively frozen scientific repeatability FAIL; cancellation/timeout/incomplete before two valid comparator inputs is infrastructure execution incomplete with no scientific classification. Only exact compact PASS may admit both finalizers and final exact authority.
