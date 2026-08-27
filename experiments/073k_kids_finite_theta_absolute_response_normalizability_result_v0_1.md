# Exp073K — KiDS finite-theta absolute-response normalizability result v0.1

**Date:** 2026-08-27  
**Classification:** `INDETERMINATE_ABSOLUTE_RESPONSE_ASYMPTOTICS_EXP073K`

## Immutable provenance

- workflow run: `33046916180`
- job: `98432968464`
- artifact: `9636045444`
- artifact digest: `sha256:358dcd196c32d929e3ebb64a905cc0e785321138d04d3474f0736b2c9f2be04e`
- execution HEAD: `86cb97b8a2933fbd70e3f80eef1420b170634524`
- KiDS source: `KiDS-WL/Cat_to_Obs_K1000_P1@36676da44471979dacb779155d7e6e7212ae1f4f`
- `xi2bandpow.c` SHA256: `3a2311c06432b131696caa9c8cd46799fd85f8316335cad6dc76a4d8eee92e7a`

All frozen numerical/provenance controls P1–P4 passed.

## Frozen-classification outcome

The preregistered asymptotic ladder was `ell_max=[7500,15000,30000,60000,120000]` with primary `Delta ell=1` above ell=20 and the required `Delta ell=0.5` shell checks. All six half-step checks passed at relative discrepancies below `9e-6`, far inside the frozen `5e-3` tolerance.

At the final `60000 -> 120000` dyadic shell, all 8/8 shear/WW bands lie inside the frozen non-normalizable box. For GGL/Wm, 6/8 bands lie inside; bands 6 and 7 have final local exponents `1.6583818721` and `1.6543345345`, narrowly above the frozen upper bound `1.65`, while their shell fractions are `0.6832057340` and `0.6823157514` and all positive normalizations remain strictly increasing.

Therefore the frozen requirement of at least 7/8 qualifying bands in each response type is not met. The result is scientifically `INDETERMINATE`, not `NONNORMALIZABLE` and not numerical failure.

The observed asymptotic behavior remains strongly consistent with the preregistered `N(L) ~ L^(3/2)` mechanism: the target shell fraction is `q_sqrt=0.6464466094`, and most final shell fractions cluster near 0.65–0.68. This observation is descriptive only and does not override the frozen classification box.

## Consequence boundary

Exp073K does not change the Exp073J 5% physical-support threshold, does not authorize a post-hoc ell cutoff or fiducial-power weighting, and does not open covariance restriction. Because the result is indeterminate rather than finite-saturation, the KiDS branch cannot return to Exp073J under the existing consequence rule.

A separately preregistered extended asymptotic ladder is admissible to determine whether the two unresolved Wm high bands settle into the already-frozen Exp073K non-normalizable box at larger cutoffs. Exp073K itself remains permanently `INDETERMINATE` regardless of that later result.

G7 OPEN.  
G8 OPEN.  
G9 OPEN.
