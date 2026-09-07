# DSIR research log — Exp073GK C2 generator and native source binding

Date: 2026-09-07

Exp073FS attempt 2 remained the sole active heavy DSIR computation, so no competing home task was launched and no partial WW numerical output was inspected.

Independent C2 work prospectively created Exp073GK: prereg commit `139fd5a949c7fbfca13b92a6550245440f84d490`, deterministic generator commit `b763b11a349422758414ffad3524305e0c84c965`, and hosted audit workflow creation commit `64e49b0a7b6aeaf7512bde9b65845376b8699aaf`.

First hosted run/job `34084884016 / 101626888946` failed support-only with first raw causal assertion `0.06664762008318016`: the harness demanded an inherited parent-domain literal locally. Minimal workflow-only repair commit `c80cb15cdb131dac785f8119d11155e2eb70d832` moved that check to the frozen parent Exp073GJ prereg without changing science. Repaired run/job `34084914369 / 101626977858` emitted exact token `PASS_EXP073GK_C2_IDE_DELTA_M_GENERATOR_STATIC_AUDIT_V0_1`, `classification=SUPPORT_PLUS_0_PLUS_0`, `self_hosted_science_started=false`, `scientific_model_authority_created=false`.

A direct audit of pinned `kaeonikc/class_iv@ac627d54e9ce196a08878d1ba33999819925d19c` then established a critical source-binding constraint: the solver constructs current-gauge total-matter density/momentum and subsequently applies `delta_m += 3*a*H*theta_m/k^2` before exporting the standard gauge-invariant `index_tp_delta_m` source. Therefore standard CLASS `d_m` cannot be fed into the frozen Exp073GJ current-gauge bridge and corrected again; that would double-transform. This is a provenance/interface `+0/+0` result, not a scientific C2 FAIL. The finding is recorded in commit `66bbf83bd87d6937cde3ada50adc0e5e7116fec8`.

C2 remains `mapping_ready=true`, `prediction_ready=false`, `G_DOMAIN_MAPPING=NOT_YET_TESTABLE`. Exact next independent C2 step is a prospectively frozen/static-audited pinned-lineage pre-transform extraction hook for current-gauge `delta_rho_m/rho_m`, `theta_m`, and `aH`, with exact source/blob provenance and no evolution/physics change.

Heavy priority remains terminal consumption of Exp073FS attempt 2, followed only on independently validated candidate PASS by Exp073FT admission.