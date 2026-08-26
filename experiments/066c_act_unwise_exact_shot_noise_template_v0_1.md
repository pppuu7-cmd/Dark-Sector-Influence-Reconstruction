# Exp066C — ACT DR6 × unWISE exact shot-noise template v0.1

Date: 2026-08-26
Status: **PASS_ACT_UNWISE_EXACT_SHOT_NOISE_TEMPLATE_V0_1**.

## Purpose

Correct exactly one failed assumption from Exp066B without changing that frozen negative result. Exp066B proved that the released ACT `gg` coupling matrix does **not** preserve the constant vector: the measured relative residual was 0.3615744168461421 against the frozen 1e-10 threshold. Therefore the cheap constant-full-sky white-noise reduction is permanently rejected.

Exp066C tests the exact upstream white-noise map instead. It is an infrastructure/forward-operator experiment only; it performs no G7 law search and inspects no fresh withheld dark-sector family.

## Immutable lineage

- Exp066B status remains `FAIL_ACT_UNWISE_SELECTED_BANDPOWER_CLOSURE_V0_1`.
- likelihood source remains `ACTCollaboration/unWISExLens_lklh@6302c30d9e70f8e4ff2d4a84a9977b4471705179`;
- public archive SHA256 remains `1b2d1563c5eb548ca6488ed8d60c5260d9e110b743a2e3a84620cfe46fbb6570`;
- samples remain `Blue_ACT`, `Green_ACT`;
- cuts remain `Clgg=[100,402]`, `Clkg=[51,402]`;
- selected order remains `[Blue gg(6), Blue kg(7), Green gg(6), Green kg(7)]`.

## Exact corrective operator

For the upstream auto-spectrum noise injection, let `C` be the released mode-coupling matrix, `W` the released bandpower-window matrix, `T` the released transfer vector, `1` the all-ones pseudo-spectrum vector, and `w2=sum(C[0,:])`. The exact full-sky vector is obtained from

`C x = w2 * 1`.

The exact selected noise template is then

`n_sel = select( T * (W x) )`.

No replacement `x = 1`, no pseudoinverse, no diagonal loading/jitter, no regularisation and no threshold relaxation are allowed.

## Frozen subtests

### C1 — exact linear-solve closure

For each released Blue/Green `gg` coupling matrix, solve `C x = w2*1` with a direct deterministic dense solve using float64. Require finite `x` and

`||C x - w2*1||_inf / max(||w2*1||_inf,1e-300) <= 5e-11`.

Record the condition number diagnostically. It cannot alter the threshold after execution.

### C2 — upstream bandpower equivalence

Construct the exact noise-only upstream expression independently from the pinned `NaMasterPowerSpectrumBinning` algebra and compare its selected `gg` bins to `select(T*(W x))`. Require identical shape, finite values, and

`max_abs_diff <= 5e-12 * max(1,max_abs(reference))`.

### C3 — nonconstant-template control

Require that the solved `x` is demonstrably not the rejected constant shortcut:

`max_abs(x-1) > 1e-6`.

This is a scientific control, not a tunable quality threshold: failure means the implementation did not actually exercise the corrective path.

### C4 — selected-vector closure

Combine the already validated Exp066B signal operator and nuisance algebra with the exact C2 shot-noise template at the same frozen Blue/Green nuisance point. Require the final vector to have dimension 26, order `[Blue gg6, Blue kg7, Green gg6, Green kg7]`, and all entries finite. This does not compare to observational data and does not fit parameters.

## Hard PASS / FAIL

PASS only if C1–C4 all pass under the frozen criteria:

`PASS_ACT_UNWISE_EXACT_SHOT_NOISE_TEMPLATE_V0_1`

Otherwise:

`FAIL_ACT_UNWISE_EXACT_SHOT_NOISE_TEMPLATE_V0_1`

Any FAIL is preserved and motivates a separately numbered experiment. Exp066B is never rewritten or reclassified.

## Executed outcome

GitHub Actions run `32989328863` on integrated `main` commit `b6b1e765d6c9179637bb81891332e68ab24a12f3` completed successfully.

- C1: PASS for both Blue/Green; relative solve residual `6.52315926577459e-15 <= 5e-11`; condition number `12.711071624037752`.
- C2: PASS for both Blue/Green; max selected-bin difference `4.218847493575595e-15`, below frozen thresholds `5.072522954317512e-12` and `5.1005923390015e-12`.
- C3: PASS; `max_abs(x-1)=1.1140436272781788 > 1e-6`, directly confirming that the exact template is nonconstant and therefore distinct from the Exp066B shortcut.
- C4: PASS; final selected vector length is exactly 26 with the frozen Blue/Green gg/kg ordering.

Preserved result: `data/derived/g7/exp066c_act_unwise_exact_shot_noise_template_v0_1.json`.

## Gate semantics

This PASS repairs only the forward-operator bridge. `G7`, `G8`, and `G9` remain OPEN. The next experiment must separately preregister observational covariance selection/whitening and a training-only cross-channel statistic before any fresh withheld-family evaluation.
