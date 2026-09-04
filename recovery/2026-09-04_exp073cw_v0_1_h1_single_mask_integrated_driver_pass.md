# Recovery — Exp073CW v0.1 H1 single-mask integrated-driver PASS

Date: 2026-09-04. Scope: DSIR only.

## Authoritative process
- Workflow run/job: `33860891989 / 100984835847`.
- Activated source head: `b7e42a5a9d215990f97943e3ee270ad09127d612`.
- Preregistered contract commit/blob: `11240638a39811c90fdf74a4b214e7876010eab2 / cd656f5bdca99673088aac427fae7bd182f982f6`.
- Integrated-driver helper commit/blob: `bada97b874fef18188481ea9e563d012733b6df0 / f61b4e42ace7e2ab7220c0df0b38d8663136896c`.
- Workflow commit: `e766b7c0fa1ffb809534876d7c8705dd3d1bd99d`.
- Frozen Exp073BU prereg commit/blob: `e1a0332c128c87049fb8699018a3a3e71c9c5321 / 816542c7eb7a8ba4e72d6e01228aa62d05c7c805`.
- Artifact ID: `9932088071`.

## Consumed raw result
GitHub Actions completed successfully and the raw job log emitted `H1_SINGLE_MASK_INTEGRATED_DRIVER_PASS` and `PASS_EXP073CW_V0_1_EXECUTABLE_DRIVER_AUDIT` after the frozen static checks and exact PyMaster 2.7 execution.

The frozen executable analogue verifies the required single-reconstruction/single-field handoff semantics: lens and source reconstruction counters are each exactly one, the same NaMaster field objects are handed to the PCL and workspace paths, the frozen DES 40 edges / 39 bands and `TE <- TE` selection are preserved, and the six durable checkpoint stages remain ordered as `fresh_masks_complete -> fresh_workspace_mcm_complete -> mcm_fits_verified -> full_window_complete -> selected_te_complete -> replica_receipt_complete`.

The result remains support-only: accounting `+0/+0`, `historical_wm_s3_numerical_import=false`, `no_tolerance_rescue=true`, `science_gate_scored=false`, `wm_s3_authority_created=false`, and `exp073bu_activated=false`.

## Classification
Authoritative **support/integration PASS `H1`, accounting `+0/+0`**. This closes the single-mask integrated-driver handoff gate only. It does not create Wm_S3 scientific authority and does not activate Exp073BU.

## Consequence
The next permitted branch is the prospectively frozen Exp073BU activation-readiness audit required by the seven pre-execution gates in the frozen Exp073BU preregistration. Only after that hosted readiness audit is consumed as PASS, implementation/contract lineage is frozen, checkpoint isolation/fail-closed restore and anti-import firewall are verified, and live DSIR-HOME-PC exclusivity is re-checked may the single explicitly activated self-hosted Exp073BU A/B scientific workflow be considered for launch.