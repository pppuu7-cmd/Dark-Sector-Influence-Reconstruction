# Exp073L methodology note — dyadic exponent / shell-fraction relation

**Date:** 2026-08-27

This note is non-classifying and does **not** modify any frozen Exp073K/Exp073L acceptance criterion.

For an asymptotic positive normalization behaving locally as

`N(L) = A L^p`,

on a dyadic ladder `L -> 2L`, the shell fraction used in Exp073K/L is

`f_shell = [N(2L)-N(L)] / N(2L) = 1 - 2^{-p}`.

Therefore, under an exact local power law, the frozen Exp073L exponent box

`p in [1.35,1.65]`

implies

`f_shell in [1-2^{-1.35}, 1-2^{-1.65}] = [0.6076..., 0.6814...]`,

which lies strictly inside the separately frozen shell-fraction box `[0.55,0.75]`.

## Interpretation

The two diagnostics remain useful in the executed experiment because finite-cutoff responses need not be exact power laws, so disagreement between the measured finite-difference exponent and measured shell fraction can expose non-power-law curvature or numerical problems. However, for an asymptotic pure power law they are algebraically linked rather than statistically independent.

Consequences for future experiments only:

- do not count simultaneous satisfaction of these two boxes as two independent pieces of evidence;
- report their consistency residual, e.g. `r = f_shell - (1-2^{-p})`, when diagnosing asymptotic curvature;
- preregister any future independent asymptotic discriminator before evaluating new outputs;
- never alter Exp073L thresholds or classification because of this retrospective analytic observation.

Exp073J physical-support threshold remains 5%. Covariance, nuisance SVD, relation/null and G8 remain unauthorized until the physical-support gate is actually passed.

G7 OPEN. G8 OPEN. G9 OPEN.
