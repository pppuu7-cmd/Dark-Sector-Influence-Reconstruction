# 2026-09-01 — Exp073CB helper RSS-semantics audit

## Authority state

- Exp073BJ remains terminal Track-A exact Wm_S1 authority PASS.
- Exp073AQ remains permanent historical exact-repeatability scientific FAIL.
- Exp073BD remains provisional/incomplete and forbidden downstream.
- Exp073BV source-lineage PASS, Exp073BW exact streaming-equivalence PASS, and Exp073BZ checkpoint/failover PASS remain preserved.
- Article-3 readiness remains Verified 52.0% | Draft/data 53.7%.

## Actions coordination state

At this audit, Exp073CA attempt3 run `33448843621` remained the only queued Actions run; replica B job `99673921530` remained queued self-hosted. No DSIR run was in progress. Overnight home-runner hard lock therefore remains in force and no self-hosted workload was triggered or revived.

## New negative result: frozen Exp073CB helper is unsuitable for the intended RSS claim

The frozen helper `ci/exp073cb_pcl_lifetime_exact_equivalence_rss_v0_1.py` was audited directly.

Its `masks(nside)` function allocates and returns both synthetic masks `(a,b)` on every call. The frozen `sequential(nside)` implementation then executes:

```python
a,_=masks(nside)
...
_,b=masks(nside)
```

In Python, `_` is an ordinary live variable, not a discard operator. Consequently:

1. after `a,_=masks(nside)`, the unwanted `b` mask is still referenced by `_` while the first field/transform proceeds;
2. after `_,b=masks(nside)`, the unwanted newly generated `a` mask is still referenced by `_` while the second field/transform proceeds.

Therefore the frozen CB `sequential` mode does **not** realize the intended one-target-mask-at-a-time lifetime. Any peak-RSS comparison produced by simply repairing NaMaster provisioning while reusing this exact helper would not validly test the proposed production memory repair.

This does not retroactively alter Exp073CB attempt1 classification: run `33464547851`, job `99721585397` remains `CB_Q3_INFRASTRUCTURE_INCOMPLETE`, because setup failed before any numerical/RSS case ran.

The helper's exact-output comparator logic (`np.array_equal` plus canonical `<f8` SHA-256) remains conceptually suitable for an exact-equivalence gate, but the RSS/lifetime implementation itself must be replaced prospectively in a new experiment rather than post-hoc modified under Exp073CB.

## Correct prospective hosted-only QA design

The next admissible memory QA must be a new prospectively frozen experiment with a helper that generates only the requested target mask at each stage, e.g. separate `lens_mask(nside)` and `source_mask(nside)` constructors (or an equivalent single-target generator). The scientific transforms, one-thread policy, `hp.alm2cl` call, output dtype/order, exact `np.array_equal` comparator, canonical `<f8` SHA comparator, and independent-process RSS measurement must remain frozen prospectively.

Required branches should distinguish:

- complete exact-equivalence PASS;
- complete exact mismatch FAIL for the implementation-equivalence prerequisite;
- infrastructure incomplete before valid comparator inputs.

This remains synthetic/nonclassifying infrastructure QA and is always `+0/+0`; it cannot close a real-survey gate.

## Exact next gate

Do **not** launch a conda-only successor that reuses the frozen CB helper unchanged. Prospectively preregister a new hosted-only corrected-lifetime QA with single-target mask generation and conda-forge NaMaster 2.7 provisioning. Before any trigger, re-check all queued/in-progress runs and preserve the overnight home-runner lock. No G7/G8 advance.
