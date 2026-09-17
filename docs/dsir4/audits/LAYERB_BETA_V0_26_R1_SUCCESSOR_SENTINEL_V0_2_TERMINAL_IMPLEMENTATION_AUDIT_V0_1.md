# DSIR Funnel Auditor — V0.26 R1 successor sentinel v0.2 terminal implementation audit

Date: 2026-09-17. Scope: **DSIR only**. GitHub repository/Actions are the durable scientific source of truth; chat is not authority.

Reviewed main baseline: `f07df98bb0a99b152b4a1becdb6203194ba72d5d`.

Reviewed terminal target: run `35181812498`, workflow `360201395`, exact head `1fd68a9814ac987300710c4e67d080c7455efa34`, event `push`, run #1 / attempt #1, terminal `failure`.

Reviewed terminal-history closure: run `35183519508`, workflow `360201396`, run #1 / attempt #1, terminal `success`.

## Gate chronology and frozen scientific object

The v0.2 attempt was prospectively authorized before execution by terminal launch authority blob `f5932ce87acc392220ca2fa71abbade8c5899723`. PR #201 froze the package without the launch marker; PR #202 merge `1fd68a9814ac987300710c4e67d080c7455efa34` added the one-shot marker and triggered the only target run for that exact head. Exact-head Actions enumeration returns exactly one run, run #1 / attempt #1. No rerun or same-nonce second attempt exists.

The V0.26 R1 scientific object remained unchanged: preregistration blob `545e5be589e0f8029d23db2edb4e2faad116c3a0`; contract blob `b510d8e97baf1c0b7b216c0605d83cdd029254e9`; 107 retained rows = DES 53 + BOSS 54; alpha tolerance `3e-10`; beta exact-target tolerance `1e-12`; scientific strict `<1e-3`; technical strict `<1e-5`; requested-node binding `<=1e-12`; full replay accounting 738 CLASS constructions. No post-outcome threshold, dataset, sampling or interpretation-ceiling change is present.

Exact frozen v0.2 identities remain: executor blob `1f727056491a6f4997298bb63dba26589fd3ddec`; decision blob `97f675e48e5b63a3d6dc7a10b0c2f2e6833cf2d9`; target-workflow blob `00bb68196c995079cad50da70be555d737d28ecb`; terminal-history workflow blob `9dc4962288471fbcd0803d22cabe1182bfac8ed3`; experiment `LAYERB_BETA_V0_26_R1_SUCCESSOR_SENTINEL_SCIENCE_V0_2`; nonce `DSIR-V026R1-SUCCESSOR-20260917-B1-4C92E7A1`.

## Independent artifact provenance closure

The exact decision artifact `10480279579` was independently downloaded. Its Actions ZIP SHA256 is `8718c9ece145907aaa4f4d1b812a7245fd226aa22c6415042a3fa293bda068b6`, matching repository/Actions metadata. The archive contains exactly `sentinel_decision.json` and `sentinel_decision.sha256`. Independent SHA256 of `sentinel_decision.json` is `4a6f064348f8cf042bc56483101af0674930a890949bea6bf171cdb772bc0fbc`; the embedded manifest binds that same digest to `safe/sentinel_decision.json`.

The exact terminal-history artifact `10480539101` was independently downloaded. Its Actions ZIP SHA256 is `0d61e9f90f03d875e8a67d99a7882530f44e5d6bd875d900c33391033c5fb329`, matching repository/Actions metadata. The archive contains exactly `terminal_receipt.json`, `terminal_receipt.sha256`, and `decision/sentinel_decision.json`. The copied decision JSON independently hashes to the same `4a6f064348f8cf042bc56483101af0674930a890949bea6bf171cdb772bc0fbc`. Independent SHA256 of `terminal_receipt.json` is `e8c9cee498e66ef53224041eee98860cab89ea031351ecdcf91bfd8b47e0ff49`, and the embedded manifest binds that digest exactly.

The terminal receipt binds target run `35181812498`, target head `1fd68a9814ac987300710c4e67d080c7455efa34`, run #1 / attempt #1, experiment and nonce, decision artifact `10480279579`, decision ZIP digest `8718c9...68b6`, decision-inner digest `4a6f064...0fbc`, target terminal timestamp `2026-09-17T04:51:48Z`, terminal-history closure `true`, and classifier `SENTINEL_INVALID`. It preserves `numerical_validity=NOT_EVALUATED`, `exact_target_validity=NOT_EVALUATED`, `scientific_criterion=NOT_EVALUATED`, `model_statistical_interpretation=NOT_EVALUATED`, and `full_107_row_execution_authorized=false`.

Accordingly the previously pending artifact-inner provenance closure is complete. The historical terminal classifier is preserved and is not rewritten.

## Independent implementation counterexample

The terminal decision found only 10 lane artifacts, so the frozen finalizer classified the attempt `SENTINEL_INVALID` before numerical/scientific evaluation. Independent job-log review identifies a concrete implementation cause for at least the missing-lane class.

Failed lane `R01` job `105075573436` used the exact authorized head, Ubuntu 24.04 image, Python 3.12.3, NumPy 1.26.4, SciPy 1.17.1 and the exact frozen executor. It passed both response-free fingerprint stages. Before any CLASS solve, v0.2 then invoked `materialize-grid` under `base.clean_env()`. That subprocess failed inside the inherited v0.1 `reconstruct()` guard with `RuntimeError: GRID896 binary identity mismatch`; no `lane_R01.json` was produced.

The source-level reason is exact and deterministic for a host whose native NumPy dispatch materializes different bytes. `lane_v2()` recomputes GRID896 independently inside every lane by running `materialize-grid` under each lane host's native NumPy dispatch. `materialize_grid()` calls the inherited `base.reconstruct()`, and inherited v0.1 `reconstruct()` immediately requires the locally generated 897-node `<f8` byte payload to hash to frozen SHA256 `8499eb0f240b85581e0dcb804b841ba911c4b3a58e8fe15702aea134e40bd65d`. Therefore a host-native dispatch class that generates any different exact bytes fails before the v0.2 frozen-byte handoff can occur.

Completed lane jobs provide the wrong-sign counterexample to the assumption that `ubuntu-24.04 + NumPy 1.26.4 + native dispatch` uniquely defines those bytes: e.g. `R09` and `R15` passed the same native materialization guard and proceeded, whereas `R01` failed it. No substantive response values from those completed lanes are used here. The only inference is infrastructure/code-scoped: per-lane native materialization is not invariant across the authorized hosted-runner population.

This is consistent with, but narrower and more operational than, the earlier response-blind diagnostic. That diagnostic established that GRID896 binary materialization depends on NumPy CPU dispatch on one diagnostic host and authorized only a prospective primitive: materialize frozen native bytes, then consume those exact bytes inside unchanged forced science runtime. It did **not** establish that independently re-materializing under native dispatch on every hosted runner produces one universal byte identity.

The v0.2 authority encoded producer dispatch as `NATIVE_NUMPY_1_26_4_ON_AUTHORIZED_UBUNTU_24_04_LANE`. The terminal run falsifies the sufficiency of that producer identity for the 32-lane hosted execution contract. The implementation therefore overgeneralized a single-host diagnostic into a cross-host per-lane producer assumption.

## Scope of invalidity

This is not a numerical/scientific FAIL. Failed lanes stop at GRID896 identity before CLASS. The terminal receipt correctly leaves numerical validity, exact-target validity and scientific criterion `NOT_EVALUATED`. Successful partial lane response values are not admissible as a replacement for the missing 32-lane terminal object and are not interpreted here.

This is also not evidence for interpolation physics, tolerance dependence, covariance/nuisance structure, a dark-sector signal, or physical identifiability. It is an implementation/provenance defect in the response-blind prerequisite materialization strategy.

The historical `SENTINEL_INVALID` result is retained exactly. No full-107, covariance, whitening, nuisance, relation-null, `Wm_S3`, global 65537, model/statistical or physical gate is opened.

## Required correction boundary

Do not repair or rerun consumed v0.2. Any successor must use a new prospectively frozen experiment identity and preserve the R1 science object unchanged unless a separately preregistered scientific successor explicitly changes it.

Before any successor science authorization, the next admissible object is response-blind diagnosis/design only. It must determine and bind a producer identity that is independent of arbitrary per-lane host-native NumPy dispatch. A plausible candidate is a single immutable, independently hashed GRID896 byte artifact produced under an explicitly frozen producer environment and distributed byte-for-byte to every lane, but that is **not authorized here**; it must be prospectively specified and independently audited. An alternative is an exact producer implementation whose byte identity is proven across the intended host classes. In either case, no CLASS response or partial scientific metric is needed for the diagnostic.

## Review result

Verdict: **INVALID_IMPLEMENTATION**.

Classification: `SUCCESSOR_SENTINEL_V0_2_PER_LANE_NATIVE_GRID896_MATERIALIZATION_NOT_HOST_INVARIANT`.

Authorized next stage: prospective authoring only of a response-blind cross-host GRID896 producer-identity diagnostic/design contract. Execution of such a diagnostic requires its own independent pre-execution review/authority. No successor sentinel science, rerun, same-nonce attempt, full-107 traversal or downstream science is authorized by this review.
