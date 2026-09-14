# DSIR current-process ledger

Updated: 2026-09-14. Scope: **DSIR only**; RTK/RQIR/KMQGB/KMDSB excluded.

## Closed numerical-runtime chain through V0.21

V0.18R and V0.19 terminal invalid outcomes were caused by a validation-model error, not by GitHub Actions or CLASS failure: the validator incorrectly required every raw NumPy `__cpu_features__` AVX-512 capability bit to become false. V0.19D (`f29190ead75225d8e8862e44ba06b51555c580b2`) diagnosed `NUMPY_RAW_CAPABILITY_BITS_NOT_RUNTIME_DISPATCH_VALIDATION_TARGET`. Runtime dispatch must be validated on `__cpu_dispatch__` members intersected with true `__cpu_features__`; residual non-dispatch hardware bits are irrelevant to mask success.

V0.20 authority `docs/dsir4/authority/LAYERB_BETA_NUMPY_RUNTIME_DISPATCH_SEMANTICS_V0_20.json`, commit `e1357e18bf95109e5b05b5e188d8f1e137f761e1`, response-free validated the exact NumPy 1.26.4 mask.

V0.21 terminal authority `docs/dsir4/authority/LAYERB_BETA_VALIDATED_CONTROLLED_CPU_CAPABILITY_DISPATCH_INTERVENTION_V0_21.json`, creation commit `7b6fc404e70ab75f1a7b7053123e7cf5dc46967e`. Run `34870133635` terminal success; decision job `104071826031`; artifact `10359787747`; digest `sha256:5b85934b23cc01cd6a4c6f3c3662d9d196a491d52addf129127e5d63e8ca6e13`. Classification `NUMPY_AVX512_DISPATCH_INTERVENTION_SUPPORTED`, effect `+0/+0`. Five exact-target preflight-valid lanes (`R03,R15,R19,R22,R28`) showed NumPy-only branch switch; glibc-only did not; combined did. Exact binding maximum `1.6551974349255386e-16`; anchor spread `1.0758876522574515e-6`.

Causal numerical result: the hosted response branch is localized to NumPy AVX-512 runtime dispatch under the frozen numerical object. This is not Layer-B or dark-sector evidence.

## Active authoritative frontier — V0.22 forced-baseline cross-host reproducibility

Preregistration: `prereg/LAYERB_BETA_FORCED_BASELINE_CROSS_HOST_REPRODUCIBILITY_V0_22.md`, commit `20403f5dbd2a3772752852c0c84ce306d7971c43`.
Executor: `ci/layerb_beta_forced_baseline_cross_host_reproducibility_v0_22.py`, commit `82684fa591911761720e744e5462e51902569fa2`, blob `7921f856f468d9b73889130df39148ccca3d048d`.
Contract: `docs/dsir4/contracts/LAYERB_BETA_FORCED_BASELINE_CROSS_HOST_REPRODUCIBILITY_V0_22.json`, commit `bc10698aa746747955d27ce2099867de236ef598`.
Workflow: `.github/workflows/layerb-beta-forced-baseline-cross-host-reproducibility-v0-22.yml`, commit `8c36fdeece4cfc6b6f6c8477282a40c9a2ccff25`.
Launch/head: `d2e4e2cfbc122683d2390369dc087b55e89fb2fc`.
Authoritative run: `34875798025`; exactly one run exists. Invariant audit is terminal `success`; 32 independent hosted lanes run with `max-parallel:32`.

V0.22 fixes the prior validator defect by construction: response-free preflight never treats raw non-dispatch AVX-512 capability bits as mask-success criteria. It validates the exact NumPy build baseline/dispatch sets and requires forced active AVX-512 dispatch to be empty while preserving the frozen active non-AVX512 dispatch set. No unmasked substantive response is computed. Only a validated forced-baseline child computes the two frozen replay-failure cells plus anchor.

Principal power requirement is frozen at total eligible `n>=6`, with at least `n>=3` from native `NATIVE_AVX512_ACTIVE` and at least `n>=3` from native `NATIVE_AVX512_INACTIVE`. Supported result requires cross-host spread `<1e-5` on both failure cells and anchor, native-class mean separation `<1e-5`, and every failure response within `<1e-5` of the frozen V0.17 alternate branch.

Do not inspect partial substantive V0.22 response values. Consume only the terminal frozen decision.

## Frozen boundaries

Production `h=1e-4`; scientific response threshold `<1e-3`; replay/intervention/reproducibility threshold `<1e-5`; exact binding `<=1e-12`; production sampling `0.00035`; `tol_perturb_integration=1e-12`. Full 107-row Layer-B, covariance, whitening, nuisance, relation-null, `Wm_S3`, global 65537 and downstream science remain closed. Frozen readiness remains `ARTICLE3_REPOSITORY_READINESS: 68%`; scientific frontier `67%`.
