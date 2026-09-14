# DSIR current-process ledger

Updated: 2026-09-14. Scope: **DSIR only**; RTK/RQIR/KMQGB/KMDSB excluded.

## Closed numerical-runtime chain through V0.22

V0.18R and V0.19 terminal invalid outcomes were caused by a validation-model error, not by GitHub Actions or CLASS failure: the validator incorrectly required every raw NumPy `__cpu_features__` AVX-512 capability bit to become false. V0.19D (`f29190ead75225d8e8862e44ba06b51555c580b2`) diagnosed `NUMPY_RAW_CAPABILITY_BITS_NOT_RUNTIME_DISPATCH_VALIDATION_TARGET`. Runtime dispatch must be validated on `__cpu_dispatch__` members intersected with true `__cpu_features__`; residual non-dispatch hardware bits are irrelevant to mask success.

V0.20 authority `docs/dsir4/authority/LAYERB_BETA_NUMPY_RUNTIME_DISPATCH_SEMANTICS_V0_20.json`, commit `e1357e18bf95109e5b05b5e188d8f1e137f761e1`, response-free validated the exact NumPy 1.26.4 mask.

V0.21 terminal authority `docs/dsir4/authority/LAYERB_BETA_VALIDATED_CONTROLLED_CPU_CAPABILITY_DISPATCH_INTERVENTION_V0_21.json`, creation commit `7b6fc404e70ab75f1a7b7053123e7cf5dc46967e`. Run `34870133635` terminal success; decision job `104071826031`; artifact `10359787747`; digest `sha256:5b85934b23cc01cd6a4c6f3c3662d9d196a491d52addf129127e5d63e8ca6e13`. Classification `NUMPY_AVX512_DISPATCH_INTERVENTION_SUPPORTED`, effect `+0/+0`.

V0.22 terminal authority `docs/dsir4/authority/LAYERB_BETA_FORCED_BASELINE_CROSS_HOST_REPRODUCIBILITY_V0_22.json`, creation commit `2b3cb46863fb85e6456a5a11e30183acf3b6de10`.
Run `34875798025` terminal success: invariant + all 32 hosted lanes + decision. Decision job `104089235776`; decision artifact `10360469338`; digest `sha256:12769549f5d44da9dc01ee82d426dd07e171cefe27282e92e40df15b43ea2ba0`.
Classification `FORCED_NUMPY_BASELINE_CROSS_HOST_REPRODUCIBILITY_SUPPORTED`, effect `+0/+0`.
All 32 lanes were candidates and eligible. Native dispatch classes: `NATIVE_AVX512_ACTIVE=10`, `NATIVE_AVX512_INACTIVE=22`, exceeding frozen power requirements. `invalid=false`, `invariant_ok=true`, `powered=true`, one binary key and one software-control key. Exact requested-node mismatch maximum `1.6551974349255386e-16`.

Under the exact V0.20 NumPy mask, both frozen replay-failure cells and the anchor had cross-host maximum pairwise relative spread `0.0`. Native-class mean separation on both failure cells was `0.0`, and every forced failure response matched the frozen V0.17 alternate branch with relative mismatch `0.0`. Thus the forced NumPy non-AVX512 baseline completely removes the previously observed hosted numerical branch on the frozen witness object across heterogeneous native dispatch classes.

This is a numerical reproducibility repair only. It does not validate full Layer-B or constitute dark-sector evidence.

Authorized next stage exactly: `PROSPECTIVELY_FROZEN_FORCED_BASELINE_PRODUCTION_H_REPLAY_REVALIDATION_AUDIT`.

## Exact next order

1. Prospectively freeze a production-h replay revalidation under the validated forced NumPy baseline before execution.
2. Revalidate the original production-h numerical replay object under the forced baseline; do not expand to full 107-row Layer-B yet.
3. Preserve production `h=1e-4`, exact inputs/grid/sampling/tolerance and all previously frozen scientific boundaries.
4. Validate the forced runtime-dispatch profile response-free before any substantive solve.
5. Only a terminal supported replay-revalidation authority may authorize any later numerical-to-scientific bridge.

## Frozen boundaries

Production `h=1e-4`; scientific response threshold `<1e-3`; replay/intervention/reproducibility threshold `<1e-5`; exact binding `<=1e-12`; production sampling `0.00035`; `tol_perturb_integration=1e-12`. Full 107-row Layer-B, covariance, whitening, nuisance, relation-null, `Wm_S3`, global 65537 and downstream science remain closed. Frozen readiness remains `ARTICLE3_REPOSITORY_READINESS: 68%`; scientific frontier `67%`.
