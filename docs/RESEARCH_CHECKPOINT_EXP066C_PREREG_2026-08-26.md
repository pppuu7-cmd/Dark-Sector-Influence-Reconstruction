# DSIR recovery checkpoint — Exp066C preregistration

Date: 2026-08-26
Main lineage entering checkpoint: Exp066B hard FAIL.

## Frozen state

Exp066B is permanently negative: B1 free-CLEFT nuisance algebra PASS; B2 released signal bandwindow/transfer operator PASS; B3 constant-mode white-noise shortcut FAIL with relative residual 0.3615744168461421 versus 1e-10; B4 26-bin ordering PASS. G7/G8/G9 remain OPEN.

Do not reinterpret Exp066B as a pass and do not relax its threshold.

## Next experiment

Exp066C is preregistered in `experiments/066c_act_unwise_exact_shot_noise_template_v0_1.md`. It replaces only the rejected shortcut with the exact upstream map: solve `C x = w2*1`, then apply released `W` and transfer `T`. Frozen solve residual is 5e-11; upstream bandpower-equivalence tolerance is `5e-12*max(1,max_abs(reference))`; nonconstant control requires `max_abs(x-1)>1e-6`; final selected vector must remain finite and dimension 26 in the existing order.

No pseudoinverse, jitter, regularisation, scale-cut change, nuisance retuning, threshold relaxation, G7 law search, or fresh withheld-family inspection is permitted in Exp066C.

## Recovery action

Implement Exp066C as a new CI script/workflow against the same pinned likelihood commit and archive hash used by Exp066B. Preserve raw CI output as an artifact and commit a compact derived summary after execution. Update `RECOVERY_LATEST`, `RECOVERY_MANUAL`, `STATUS`, `GATES`, research log and findings register only with the observed result; never edit the frozen Exp066B outcome.

A PASS still leaves G7/G8/G9 OPEN; the next scientific step after forward-operator closure is a separately preregistered covariance-whitened training-only cross-channel relation/null statistic.