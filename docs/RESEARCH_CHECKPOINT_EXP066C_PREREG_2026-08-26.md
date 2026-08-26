# DSIR recovery checkpoint — Exp066C preregistration (2026-08-26)

Exp066B is permanently recorded as `FAIL_ACT_UNWISE_SELECTED_BANDPOWER_CLOSURE_V0_1` because its preregistered constant-mode identity failed by a wide margin. B1 nuisance/free-CLEFT algebra, B2 signal bandwindow/transfer closure and B4 selected ordering remain immutable PASS subresults.

Exp066C is a separate corrective experiment. Its scientific contract was committed before execution in `experiments/066c_act_unwise_exact_shot_noise_template_v0_1.md`.

Frozen correction:

`C y = 1`, solved with `numpy.linalg.solve` in float64, followed by

`t = N*w2*(W@y)*T`.

Frozen hard controls:

- pinned ACT likelihood/data provenance unchanged;
- RNG seed 20260827 for the small-matrix literal inverse/solve regression;
- equivalence tolerance `5e-13*max(1,max|reference|)`;
- released 6144x6144 solve residual `max|Cy-1| <= 1e-10`;
- no jitter, pseudoinverse, diagonal loading, shrinkage, scale-cut change or threshold relaxation;
- unchanged Blue/Green shot-noise amplitudes and selected six `gg` bins.

A PASS closes only the ACT×unWISE selected-bandpower operator bridge when combined with the immutable Exp066B B1/B2/B4 passes. It does not close G7/G8/G9 and does not select a withheld theory family.
