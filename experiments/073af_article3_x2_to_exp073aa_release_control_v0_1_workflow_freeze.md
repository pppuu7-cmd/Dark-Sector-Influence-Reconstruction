# Exp073AF workflow freeze — X2 -> Exp073AA release control v0.1

**Frozen:** 2026-08-30 before the trigger commit, while real X2 chains P and Q are still in progress and before any real X2 receipt is read by Exp073AF.

- preregistration last-modifying commit: `91e9f3f25fa34cab3a33d927d47afa10e5f1cc29`
- implementation last-modifying commit: `2d772bff1971f81b8cdc94e5e2ca0d52290bfa8d`
- workflow_last_modifying_commit: `25397615a824c972330fc1a98043761991bfe744`
- trigger path: `ci/exp073af_article3_x2_to_exp073aa_release_control_v0_1.trigger`
- required hosted QA token: `PASS_EXP073AF_X2_TO_EXP073AA_RELEASE_CONTROL_SYNTHETIC_V0_1`

The hosted workflow may execute only the synthetic state-machine QA. It must not query/read real X2 receipts, must not launch Exp073AA production, must not download real angular artifacts, must not evaluate support/covariance/nuisance/G8 quantities, and must not change strict Article-3 scientific readiness from 52%.

A hosted PASS certifies only that the release controller implements the prospectively frozen P/Q governance and fails closed on ambiguous/inconsistent states.
