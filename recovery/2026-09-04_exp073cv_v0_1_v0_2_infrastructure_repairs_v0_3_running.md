# Recovery — Exp073CV v0.1/v0.2 infrastructure failures; v0.3 running

Date: 2026-09-04. Scope: DSIR only.

## Immutable historical outcomes
Exp073CV v0.1 run/job/head `33843210949 / 100929554219 / 340baf103192e2cd148daf1b0097a2444c9f3342` failed before numerical execution. First causal failure: `ci/exp073cv_wm_s3_production_exact_adapter_v0_1.py` read its complete own source and searched for the forbidden literal `.get_coupling_matrix(`; that literal existed inside the verifier itself, so it deterministically self-matched and raised `RuntimeError('forbidden materialization pattern')`. Expected audit receipt was never created. Classification: `I4_INFRASTRUCTURE_OR_SOURCE_BINDING_FAIL`, accounting `+0/+0`, no Wm_S3 authority, no Exp073BU activation.

The prospective v0.2 repair introduced AST-scoped verification of only the production functions `stream_fits_to_canonical_input`, `run_downstream`, and `execute`, with helper blob `640205ab9f21fd3b3ada6cb0b3a3e7c5e461f704`; numerical v0.1 production/reference arithmetic remained unchanged. V0.2 run/job/head `33847035743 / 100941100858 / 41fe6e521b69856ab6c4fd0569690b8b4dda4f09` also failed before numerics. First causal failure at the static freeze step: workflow expected prereg blob `22e2b1de27fb11b48352e2ddc68248dfc5fad68d`, while the actually committed v0.2 prereg blob was `a3635da105aed6b7e69f590577bd5e12523b142a`. Numerical/environment/compile/regression steps were skipped, and artifact upload found no receipt. Classification: `I4_INFRASTRUCTURE_OR_SOURCE_BINDING_FAIL`, `+0/+0`, no science authority.

## Prospective v0.3 repair and current process
V0.3 prereg commit `4d5729a1d7fc8e0e595e9225da44a85018f03c0b`, blob `8be0c16a3eddf823534b5e91450f97d6dd2138de`; workflow commit `af7340618d302ffb1d94d200f53ed5ef803c600a`; activation/head `77cc6ba35aac41d2f6af12c7b865787db2bb3e44`; authoritative hosted run/job `33847132443 / 100941396500`. Before activation live Actions showed zero queued and zero in-progress runs. V0.3 only corrects freeze binding and uses the same scoped-verifier helper; inherited production adapter blob remains `dafe86086a470c852106f0d4ecccbda1d389e397`.

Observed v0.3 status at this note: static freeze PASS; scoped-verifier runtime-copy PASS; exact NaMaster 2.7/GSL environment installation in progress. DSIR-HOME-PC remains FREE. There is no checkpoint namespace because this is hosted synthetic support QA.

Frozen PASS remains `I1_PRODUCTION_INTERFACE_EXACT_INTEGRATION_PASS`, requiring for every preregistered synthetic case whole full-window and TE<-TE SHA equality, `numpy.array_equal == True`, exact max absolute difference `0.0`, and inherited OS mmap/FITS `/proc/self/maps` evidence. Only I1 is support PASS `+0/+0`; it does not activate Exp073BU. I2/I3 are numerical or memory support failures; I4 infrastructure/source/verifier; I5 malformed/missing receipt. No tolerance rescue or science-boundary change is allowed.

Wm_S1 Track-A exact PASS, admitted Wm_S2 authority, historical Exp073CM resource/performance FAIL +0/+0 and all validated support authority remain preserved. Wm_S3 scientific authority remains absent.
