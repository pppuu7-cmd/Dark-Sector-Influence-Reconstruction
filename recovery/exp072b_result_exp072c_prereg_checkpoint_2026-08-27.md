# DSIR recovery checkpoint — Exp072B result + Exp072C preregistration — 2026-08-27

## Immutable newest result

Exp072B completed with

`DIAGNOSTIC_K_ONLY_TARGET_NOT_FOUND_EXP072B`.

Provenance:

- run `33030657898`;
- job `98382166843`;
- artifact `9630210086`;
- artifact digest `sha256:5bbca5717d29d24f8ba3b5ae24d8cc752bd5d90460859ae79f5212ca764615ad`;
- extracted result JSON SHA256 `d90b387b6acb5b48c6daae0f25da9adb7ea6ed851e3b22c8a79c6bc56b2d0f1d`;
- all B1–B6 hard controls PASS.

Exp072A remains permanent scientific FAIL.

## Causal result

Across 64 coordinate-block pairs:

- median `f_z_out = 0.4556923704004443`;
- median `f_k_out = 0.9705092579400587`;
- median `f_k_high = 0.9705092577608834`;
- median `f_k_low = 1.1786843354337586e-7`;
- k-out exceeds z-out in 60/64 pairs.

But all 26 complete coordinates have infinite upper-k-only route requirements because required Wm/WW and kg blocks retain >5% irreducible support outside the fixed redshift interval.

Redshift leakage is overwhelmingly low-z:

- overall median `f_z_low = 0.45567647226245966`;
- overall median `f_z_high = 8.58899591150497e-7`.

Therefore the supported causal diagnosis is:

`current route blocked by coupled lower-z + upper-k support`,

not lower-k and not upper-z.

## Exp069F lesson imported prospectively

`docs/PROVIDER_EXTENSION_NATIVE_SUPPORT_BOUNDARY_2026-08-27.md` freezes the old C5 lesson before any new provider extension:

- target/interpolated reachability is not provider certification;
- C3 extension must certify native source/transfer support and native matter closure;
- C5 extension must demonstrate solver-native raw support around any target and separately revalidate provider semantics;
- no Exp072B/Exp072C diagnostic rectangle becomes physical support automatically.

## Current preregistered next experiment

`experiments/072c_joint_lowz_highk_support_frontier_prereg_v0_1.md`

is frozen before any Exp072C output.

It keeps fixed:

- `z_max=2.33`;
- `k_min=0.000704833374744468 Mpc^-1`;
- threshold `0.05`;
- exact ACT×unWISE positive operator geometry;
- 26 coordinates / 64 coordinate-block pairs;
- route minimum `>=15` plus Blue/Green gg/kg coverage.

It varies only discrete lower-z and upper-k boundaries on existing projection samples, computes the route-support Pareto frontier, and reports minimal-redshift-extension and minimal-k-extension endpoints descriptively.

No provider is extended in Exp072C.

## Current gate state

- covariance restriction: NOT AUTHORIZED;
- nuisance SVD/rank: NOT AUTHORIZED;
- G7: OPEN;
- G8: OPEN;
- G9: OPEN.

## Continuation

1. merge Exp072B result and Exp072C preregistration;
2. only then implement Exp072C;
3. execute and preserve its diagnostic classification;
4. if a finite frontier exists, freeze one provider-extension target before running any new C3/C5 solver output;
5. independently certify both providers on that target using the native-support boundary;
6. only after both PASS may a new angular leakage gate be preregistered.
