# Exp072C — joint lower-z / upper-k support frontier result v0.1

**Date:** 2026-08-27  
**Scientific classification:** `DIAGNOSTIC_JOINT_LOWZ_HIGHK_FRONTIER_FOUND_EXP072C`

## Immutable provenance

- implementation merge: `b442cddd6ba032d1261a0994bc1c4f5cf899a9f7`;
- workflow run: `33031427090`;
- workflow job: `98384598473`;
- artifact: `9630407069`;
- artifact digest: `sha256:0e726d9f12b2b8951a4d2598b3723d54db1a14c09070d8e8770d5256773f2a71`;
- extracted JSON SHA256: `d0d8e6a19177f4a7b94d2f0b95d6fee3b5cd85078e8eadee06e7f0faaf5864c0`.

All frozen C1–C8 controls passed. Exp072A and Exp072B remain unchanged:

- Exp072A: permanent `FAIL_ACT_UNWISE_ANGULAR_SUPPORT_LEAKAGE_MASK_V0_1`;
- Exp072B: `DIAGNOSTIC_K_ONLY_TARGET_NOT_FOUND_EXP072B`.

## Frozen frontier result

The exact discrete scan used 28 lower-z candidates and 568937 sampled upper-k candidates above the current boundary. Five lower-z choices admit a finite route, but the Pareto frontier contains exactly **one** nondominated point:

`z_min = 0.0087345857837422`

`k_max = 4.818261097432861 Mpc^-1`.

At that point the frozen minimum route retains exactly 15 of the 26 released coordinates:

- Blue ACT: `gg=1`, `kg=4`;
- Green ACT: `gg=3`, `kg=7`.

Retained indices:

`[0,6,7,8,9,13,14,15,19,20,21,22,23,24,25]`.

Both preregistered descriptive extrema coincide with this same unique point: it is simultaneously the minimal-redshift-extension and minimal-k-extension endpoint of the finite frontier.

## Scale of the required extension

Relative to the current Exp071A common provider boundary,

`k_max,current = 0.06664762008318016 Mpc^-1`,

the frontier requires approximately

`4.8182610974 / 0.0666476201 = 72.29`

times larger physical k support.

Relative to the `0.30 Mpc^-1` internal C5 bridge range used in the current certification program, the frontier k is about `16.06` times larger.

The lower-z boundary moves from `0.295` to `0.0087346`, a factor of about `33.77` downward in z.

These ratios are descriptive planning facts, not provider-validity criteria.

## Scientific interpretation

Exp072C proves a narrower and more useful statement than “extend k a little farther”. Under the exact released ACT×unWISE positive operator geometry and the already frozen 5% support-leakage rule, the current linear/no-CLEFT route becomes geometrically viable only after a **very large coupled low-z/high-k extension**.

That frontier is not physical certification. In particular, the existence of a sampled Limber rectangle ending at `4.818 Mpc^-1` does not imply that either C3 or C5 has a valid linear physical prediction there.

This is precisely where the Exp069F→Exp069H lesson applies: target/interpolated reachability cannot be promoted to provider support. Any provider extension must be independently certified on native/raw support, and the current linear/no-CLEFT premise must itself be checked before spending scientific significance on such an extension.

## Downstream authorization

Exp072C does **not** authorize:

- C3 or C5 provider extension;
- covariance restriction;
- Cholesky/whitening;
- nuisance SVD/rank;
- G7 relation/null fitting;
- G8 selection.

The next causal step is a prospectively frozen perturbativity/physical-eligibility audit of the unique frontier under the current linear/no-CLEFT premise. Failure there blocks blind provider extension and points instead toward a genuinely nonlinear, solver-neutral matter/Weyl route.

G7/G8/G9 remain OPEN.
