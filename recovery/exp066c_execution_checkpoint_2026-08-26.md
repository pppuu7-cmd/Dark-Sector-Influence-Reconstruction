# Exp066C execution checkpoint — 2026-08-26

Current branch: `exp066c-exact-shot-noise`
Base main checkpoint: `ad803790508aafc7a420f8a401c6eea49834606e`
Preregistration: `experiments/066c_act_unwise_exact_shot_noise_template_v0_1.md`

Implemented without changing frozen criteria:
- direct float64 solve of `C x = w2 * 1`;
- C1 threshold `5e-11` on relative infinity-norm solve residual;
- independent C2 reference using pinned upstream `D = W C^{-1}` algebra and threshold factor `5e-12`;
- C3 nonconstant-template control `max_abs(x-1) > 1e-6`;
- C4 frozen 26-element ordering `[Blue gg6, Blue kg7, Green gg6, Green kg7]`;
- no pseudoinverse, jitter, regularisation, fit, law search, withheld-family evaluation, or reclassification of Exp066B.

Workflow: `.github/workflows/act-unwise-exact-shot-noise-template-v0-1.yml`
Audit: `ci/act_unwise_exact_shot_noise_template_v0_1.py`
PR: #63

At this checkpoint the PR-triggered workflow had not yet appeared in the Actions run list. Scientific outcome is therefore not yet classified; G7/G8/G9 remain OPEN. The next recovery action is to inspect the PR head workflow run, preserve the JSON outcome, then merge only the frozen implementation/result trail without modifying Exp066B.