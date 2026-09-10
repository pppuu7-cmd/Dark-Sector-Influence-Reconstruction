# Layer-B sequential model-lifetime estimator invariance v0.1

Date: 2026-09-11. Scope: DSIR Article III support/process only. Effect `+0/+0`.

This note is response-blind with respect to Exp073JS and any future recovered Exp073JL output. It records an implementation invariant already explicit in the frozen JJ/JL response engine.

The frozen response engine obtains four interpolated target-value vectors in fixed model order:

1. reference `(0,0)`;
2. alpha-minus `(-h,0)`;
3. beta-plus `(0,+h)`;
4. beta-minus `(0,-h)`;

and then forms exactly

```python
ref, al, bp, bm = vals
np.column_stack((
    np.abs((al-ref)/(-H)),
    np.abs((bp-bm)/(2*H)),
))
```

with `H=1e-4`.

No expression in this estimator references Python object identity, simultaneous lifetime of the four solver instances, mutable state of a different model object, or evaluation wall time. Therefore changing object lifetime from four simultaneously retained independent solver instances to four sequential independent solver instances does not alter the estimator definition **provided that** the four resulting target-value vectors are the same binary64 arrays and are inserted into the same fixed order before applying the exact expression above.

This is an algebraic implementation invariant, not a proof that a particular solver produces identical vectors under different lifetime contexts. That separate solver-isolation obligation is why Exp073JR/JQ/JS exist. A future sequential implementation must preserve the target-vector bytes, fixed role order, `h`, interpolation, masks, target order, and NumPy response expression exactly; it may not recompute an alpha/beta response using a different finite-difference convention or combine raw model operands across runner/process boundaries.

Consequently, a valid process authorization for sequential one-live execution would change only resource lifetime/solver ownership, not the scientific estimator. This note creates no process authorization, no Layer-B science authority, no covariance authority and no readiness change.