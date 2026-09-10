# Exp073JM activation prereg-alignment audit v0.1

Date: 2026-09-11. Scope: DSIR Article III support/process only. Effect `+0/+0`.

This audit was completed while Exp073JR was still running and before any recovered Exp073JL numerical result exists. It is response-blind with respect to the future JL verdict.

## Frozen prereg activation

`docs/dsir4/prereg/EXP073JM_ARTICLE3_LAYERB_COMMON_GRID_FOURTH_REFINEMENT_CONVERGENCE_V0_1.md` authorizes JM only if Exp073JL is a valid independently verified `COMMON_GRID_THIRD_REFINEMENT_NOT_CONVERGED_PLUS_0_PLUS_0`. Infrastructure/malformed/non-valid JL outcomes do not activate JM. The prereg does not require `retained_after_layer_b==107` or `unsupported_target_evaluations==0` as additional activation predicates.

Those support quantities are explicitly part of JM's own frozen decision: zero unsupported targets, invalid-row fraction <=0.05, retained dimension >=15, plus the other support/convergence conditions.

## Current implementation mismatch

The current `ci/exp073jm_article3_layerb_common_grid_fourth_refinement_convergence_v0_1.py` correctly checks JL classification and independent artifact verification, but then additionally requires:

```python
jo = jl.get("observations", {})
if jo.get("retained_after_layer_b") != 107 or jo.get("unsupported_target_evaluations") != 0:
    raise SystemExit("JL support authority mismatch")
```

This is stricter than the prospectively frozen activation condition. It could incorrectly classify an otherwise valid independently verified JL NOT_CONVERGED authority as non-activating before JM gets the chance to apply its own frozen support checks.

## Mandatory repair before any JM execution

If and only if a future valid independently verified JL NOT_CONVERGED authority activates JM, the executable implementation must first be aligned by removing the two extra activation predicates above. The later JM calculations of `unsupported`, lookup mismatch, row validity, invalid-row fraction, retained dimension and all frozen convergence criteria must remain unchanged.

The repair is implementation/prereg alignment only. It must not change grid sizes 4097/8193, interpolation, `h=1e-4`, `REL_TOL=1e-3`, physical domain, masks, diagnostic maximum, or any scientific threshold.

A static regression test must prove both cases before JM production:

1. a syntactically valid independently verified JL NOT_CONVERGED authority without the extra `107/0` observation pair reaches the JM internal-gate path rather than failing activation;
2. wrong JL classification or `artifact_verified_independently != true` still fails closed.

Until that repair and regression PASS exist, current JM implementation is **NOT EXECUTION-READY**, even if the future JL branch activates JM. This audit creates no JL/JM scientific result and changes no readiness percentage.