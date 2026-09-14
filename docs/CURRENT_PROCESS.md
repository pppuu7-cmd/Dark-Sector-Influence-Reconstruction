# DSIR current-process ledger

Updated: 2026-09-14. Scope: **DSIR only**; RTK/RQIR/KMQGB/KMDSB excluded.

## Closed numerical-runtime chain through V0.21

V0.17 `CPU_CAPABILITY_RUNTIME_STATE_STRATIFICATION_SUPPORTED` established observational host/runtime stratification.

V0.18R and V0.19 both ended `CONTROLLED_CPU_CAPABILITY_DISPATCH_INTERVENTION_INVALID`, not because GitHub Actions or CLASS failed, but because the intervention validator targeted the wrong NumPy observable: it required every raw AVX-512 bit in `__cpu_features__` to become false. V0.19D (`f29190ead75225d8e8862e44ba06b51555c580b2`) diagnosed `NUMPY_RAW_CAPABILITY_BITS_NOT_RUNTIME_DISPATCH_VALIDATION_TARGET`. NumPy runtime dispatch is defined by membership in `__cpu_dispatch__` combined with the corresponding `__cpu_features__` state; residual non-dispatch raw capability bits are not evidence that dispatch remains active.

V0.20 authority `docs/dsir4/authority/LAYERB_BETA_NUMPY_RUNTIME_DISPATCH_SEMANTICS_V0_20.json`, commit `e1357e18bf95109e5b05b5e188d8f1e137f761e1`, validated the exact NumPy 1.26.4 runtime-dispatch mask response-free. Run `34869578874`, decision artifact `10358203034`, digest `sha256:397e2da8f05b92d300bf244f81ee411045508988ad04762ed3868615a66c4002`. Classification `NUMPY_AVX512_RUNTIME_DISPATCH_MASK_VALIDATED`.

V0.21 terminal authority: `docs/dsir4/authority/LAYERB_BETA_VALIDATED_CONTROLLED_CPU_CAPABILITY_DISPATCH_INTERVENTION_V0_21.json`, creation commit `7b6fc404e70ab75f1a7b7053123e7cf5dc46967e`.
Run `34870133635` is terminal success: invariant + 32 hosted lanes + decision all succeeded. Decision job `104071826031`; decision artifact `10359787747`, digest `sha256:5b85934b23cc01cd6a4c6f3c3662d9d196a491d52addf129127e5d63e8ca6e13`.
Classification: `NUMPY_AVX512_DISPATCH_INTERVENTION_SUPPORTED`, effect `+0/+0`.
Eligible/preflight-valid exact-target lanes: `R03,R15,R19,R22,R28` (`n=5`, frozen minimum 3). `numpy_switch_supported=true`, `glibc_switch_supported=false`, `combined_switch_supported=true`; intervention invalid=false; invariant=true. Maximum requested-node mismatch `1.6551974349255386e-16`; maximum anchor condition spread `1.0758876522574515e-6`.

Causal numerical interpretation: under the exact frozen AMD EPYC 9V74 object and identical binaries, disabling the validated NumPy AVX-512 runtime dispatch set switches both frozen V0.17 replay-failure responses from the native branch to the alternate branch in every eligible lane while the anchor remains stable. The glibc-only hwcaps mask does not switch the branch. Thus the host-dependent response branch is causally localized to NumPy AVX-512 runtime dispatch, not to glibc x86-64-v4 dispatch. This is numerical-runtime mechanism evidence only, not Layer-B or dark-sector evidence.

Authorized next stage exactly: `PROSPECTIVELY_FROZEN_FORCED_BASELINE_CROSS_HOST_REPRODUCIBILITY_AUDIT`.

## Exact next order

1. Do not repeat V0.18R/V0.19 or V0.21.
2. Prospectively freeze a forced NumPy non-AVX512 baseline cross-host reproducibility audit before execution.
3. Use response-free native fingerprints to prove representation of distinct native capability/dispatch classes, then compute only the forced-baseline numerical object.
4. Require the exact V0.20 validated NumPy mask and validate the forced active dispatch profile before any substantive response.
5. Test whether both frozen replay-failure cells and the anchor collapse to cross-host spread `<1e-5` and whether failure-cell responses agree with the frozen V0.17 alternate branch within `<1e-5`.
6. Keep all downstream science gates closed.

## Frozen boundaries

Production `h=1e-4`; scientific response threshold `<1e-3`; replay/intervention/reproducibility threshold `<1e-5`; exact binding `<=1e-12`; production sampling `0.00035`; `tol_perturb_integration=1e-12`. Full 107-row Layer-B, covariance, whitening, nuisance, relation-null, `Wm_S3`, global 65537 and downstream science remain closed. Frozen readiness remains `ARTICLE3_REPOSITORY_READINESS: 68%`; scientific frontier `67%`.
