# DSIR provider-extension native-support boundary — 2026-08-27

**Status:** methodological hard boundary frozen before any Exp072B result is used to design a provider extension.

## Why this note exists

The C5 sequence already exposed a failure mode that must not be repeated in the observational-support program.

In Exp069F, increasing ordinary CAMB/EFTCAMB numerical accuracy made the frozen **target-grid** GR-limit criterion pass first at `q=2`, but the direct same-node raw discrepancy at that same setting remained slightly above the historical `5e-6` scale. The later provider route therefore used `q=3`, the smallest tested point at which both target-grid and same-node raw closure were below that scale, and it still required a separately preregistered Exp069H provider certification.

The scientific lesson is general:

> a diagnostic showing that a requested/interpolated target is reachable is not itself proof that the underlying physical provider has certified native support there.

This note applies that lesson prospectively to any provider-extension program that could follow Exp072B.

## Hard distinction: diagnostic target versus provider support

If Exp072B returns a finite `K_target_route`, that number is only an **operator-geometry target**. It does not mean C3 or C5 is physically valid to that k.

A future extension may be called certified only if each provider independently demonstrates physical support to the required boundary under a new preregistration.

No ACT×unWISE mask, covariance restriction, whitening, nuisance quotient or G7 relation may use the hypothetical Exp072B target as though it were already a provider domain.

## C3 / GDM rule

The currently certified C3 route is explicitly native-grid and forbids amplitude interpolation of `D_m`.

Therefore any C3 upper-k extension must demonstrate, at every newly admitted redshift/support slice used downstream:

- native source/transfer grid coverage to at least the required physical k;
- exact source/transfer node matching under the existing representation-level machine guard;
- native `pk_lin` closure of reconstructed `P_mm` under a prospectively frozen tolerance;
- finite `P_mm`, signed `P_Wm`, `P_WW` and the signed Weyl construction;
- coherence/PSD controls and no-state-mutation/repeatability;
- no nearest-neighbour or amplitude-interpolation rescue.

Merely asking CLASS for a larger interface/output k range is not certification.

## C5 / designer-f(R) rule

The currently certified C5 q=3 route may evaluate target nodes through the public CAMB interpolator only **inside** explicitly demonstrated solver support.

Any C5 upper-k extension must separately establish that:

- the solver-native physical raw support reaches beyond the requested target boundary;
- target interpolation is strictly interior to that demonstrated support and is not extrapolation;
- the q=3 zero/near-zero continuity and nontrivial-production provider semantics remain valid on the enlarged domain under newly frozen criteria;
- signed `P_Wm` and all auto/cross physicality checks remain valid;
- the enlarged route is repeatable and does not rely on floor subtraction, fitted renormalization, smoothing, source patching or threshold changes.

A successful interpolator call outside previously certified physical support is not evidence of physical validity.

## Common-domain rule

The post-extension common physical support is always the intersection of independently certified C3 and C5 domains:

`V_common_new = V_C3_certified_new ∩ V_C5_certified_new`.

The ACT×unWISE interface domain (`kmax=10 Mpc^-1`) remains only an algebraic projector domain and cannot substitute for either physical provider domain.

If redshift support also has to be extended, the same rule applies jointly in `(z,k,block)`. A larger k limit at one redshift does not certify it at another.

## Historical semantics

This boundary does not alter any existing classification:

- Exp069B remains permanent scientific FAIL;
- Exp069F remains a numerical-accuracy mechanism result;
- Exp069H remains the certified current C5 provider;
- Exp070A remains permanent scientific FAIL;
- Exp070C remains the certified current C3 provider;
- Exp071A remains the current provider-space common-support PASS;
- Exp072A remains permanent scientific FAIL.

## Relevance to Exp072B

Exp072B may diagnose whether an upper-k-only route target exists. Whatever it returns:

- `K_target_route` is planning information only;
- a provider extension must be a new numbered prospective certification;
- only after both providers independently pass may the angular support/leakage audit be rerun as a new experiment under its own frozen contract.

This prevents the exact conceptual error exposed by the Exp069F→Exp069H history: **target-level numerical reachability must never be silently promoted to provider-level physical certification**.

G7/G8/G9 remain OPEN.
