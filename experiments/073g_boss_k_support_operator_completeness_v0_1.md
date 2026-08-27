# Exp073G — BOSS k-support operator completeness audit v0.1

**Date:** 2026-08-27  
**Scope:** pre-output audit under the already-frozen Exp073G contract. No support fraction or retained dimension is evaluated here.

## Frozen parent

This audit does not modify `experiments/073g_kids_boss_bnt_exact_physical_support_prereg_v0_1.md` or the pre-output binding `data/derived/g7/exp073g_kids_boss_bnt_operator_binding_v0_1.json`.

The frozen physical rectangle remains `0.295 <= z <= 2.33` and `0.000704833374744468 <= k <= 0.06664762008318016 Mpc^-1`, with maximum positive invalid-support fraction `0.05`. G7–G10 and the 15-coordinate planning floor remain unchanged.

## Question

Can the bound public BOSS high-z configuration-space wedge operator define the non-negative, solver-neutral, all-k support-envelope normalization required by Exp073G without adding a theory-dependent weight or a new k cutoff?

## Bound release facts

The exact KiDS public source is `KiDS-WL/Cat_to_Obs_K1000_P1@36676da44471979dacb779155d7e6e7212ae1f4f`.

The frozen high-z BOSS dataset contract identifies:

- `data_type = xi_wed`;
- three wedges;
- 32 released configuration-space points;
- fiducial retained point range 5–32;
- 160 radial/theory bands with 21–160 used by the released window construction;
- mean redshift `z=0.61`;
- a released finite radial/window matrix.

The exact dataset, radial-band and window-object SHA256 digests are already frozen in the Exp073G operator binding and are rechecked by the workflow.

## Operator completeness result

For a configuration-space correlation-function multipole, the linear response to a power-spectrum multipole has Fourier–Bessel form

`xi_l(s) = i^l/(2*pi^2) integral_0^infinity dk k^2 P_l(k) j_l(k s)`.

Therefore the P-independent linear kernel with respect to `P_l(k)` is proportional to

`K_l(k;s) = k^2 j_l(k s)`.

At fixed non-zero separation, the spherical Bessel function obeys `j_l(k s)=O(1/k)` with an oscillatory leading term, so the absolute kernel is generically `O(k)`. A finite discrete linear combination over released radial bands remains a finite sum of oscillatory terms of this type. Its absolute all-k integral is not a finite, release-defined normalizer in the generic case.

This matters because Exp073G deliberately forbids signed cancellation from hiding invalid-domain support: the support envelope must be non-negative. The usual oscillatory convergence of the signed Fourier–Bessel transform therefore cannot supply the required positive normalization.

A finite positive normalization can be manufactured only by adding an extra ingredient, for example:

- a fiducial `P(k)` weight;
- nonlinear damping;
- a finite high-k integration cutoff;
- another model-dependent response prescription.

None of these is frozen in the public BOSS operator binding. Choosing one now would make the geometric support gate theory/cutoff dependent and would violate the prospectively frozen no-post-hoc rule.

## Classification semantics

If the exact source/hash/contract checks pass, this is classified as

`FAIL_EXP073G_REPRODUCTION_OR_PROVENANCE`.

It is **not** `FAIL_KIDS_BOSS_BNT_PHYSICAL_SUPPORT_EXP073G`: no trustworthy `f_invalid` has been computed, and the candidate has not been scientifically rejected by the 5% support criterion.

The failure means that the current configuration-space BOSS `mm` coordinate does not provide a sufficiently complete public operator for the particular solver-neutral positive-support measure frozen in Exp073G.

If the source/hash checks themselves fail, the run is `INCOMPLETE_EXP073G`, not a scientific result.

## Downstream boundary

Covariance restriction/whitening, nuisance SVD/rank, relation/null fitting and G8 remain forbidden.

The next admissible step after a trustworthy operator-provenance failure is a **new prospectively frozen observational-operator branch**, preferably a public Fourier-space BOSS/eBOSS clustering statistic with finite released k bins/windows or another mm-sensitive public observable whose positive k-support measure is intrinsically normalizable. The 5% threshold and C3+C5 physical rectangle may not be weakened to rescue the present route.

G7 OPEN. G8 OPEN. G9 OPEN.
