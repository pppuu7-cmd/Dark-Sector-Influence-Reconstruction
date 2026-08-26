# Exp066C execution checkpoint — 2026-08-26

Integrated main commit: `b6b1e765d6c9179637bb81891332e68ab24a12f3`
Preregistration: `experiments/066c_act_unwise_exact_shot_noise_template_v0_1.md`
Workflow: `.github/workflows/act-unwise-exact-shot-noise-template-v0-1.yml`
Audit: `ci/act_unwise_exact_shot_noise_template_v0_1.py`
PR: #63

Implemented without changing frozen criteria:
- direct float64 solve of `C x = w2 * 1`;
- C1 threshold `5e-11` on relative infinity-norm solve residual;
- independent C2 reference using pinned upstream `D = W C^{-1}` algebra and threshold factor `5e-12`;
- C3 nonconstant-template control `max_abs(x-1) > 1e-6`;
- C4 frozen 26-element ordering `[Blue gg6, Blue kg7, Green gg6, Green kg7]`;
- no pseudoinverse, jitter, regularisation, fit, law search, withheld-family evaluation, or reclassification of Exp066B.

## Executed result

GitHub Actions run `32989328863`, job `98242896864`, completed with conclusion `success` on `main` commit `b6b1e765d6c9179637bb81891332e68ab24a12f3`.

Frozen scientific classification: `PASS_ACT_UNWISE_EXACT_SHOT_NOISE_TEMPLATE_V0_1`.

Checks:
- C1 PASS: relative residual `6.52315926577459e-15` for both Blue/Green, threshold `5e-11`.
- C2 PASS: max absolute selected-bin difference `4.218847493575595e-15`, thresholds approximately `5.07e-12`/`5.10e-12`.
- C3 PASS: `max_abs(x-1)=1.1140436272781788` against minimum `1e-6`.
- C4 PASS: final vector length 26 in the frozen ordering.

Preserved JSON: `data/derived/g7/exp066c_act_unwise_exact_shot_noise_template_v0_1.json`.
Artifact ID: `9614063228`; artifact ZIP SHA256 `2409cd974691f09d80893d8d64f7f61ac5bccff4e28d4eb4251a5a21baf80baf`.

Immutable lineage remains: Exp066B = `FAIL_ACT_UNWISE_SELECTED_BANDPOWER_CLOSURE_V0_1`; G7/G8/G9 = OPEN.

Next recovery action: execute separately preregistered Exp067A observational covariance-selection/whitening closure. Do not fit a G7 relation or inspect a fresh withheld family until that bridge passes.
