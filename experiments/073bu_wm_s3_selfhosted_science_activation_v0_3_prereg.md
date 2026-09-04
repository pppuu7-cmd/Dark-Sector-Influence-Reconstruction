# Exp073BU — Wm_S3 self-hosted science activation v0.3

**Frozen prospectively:** 2026-09-04 before any Exp073BU Wm_S3 A/B numerical science run is activated by this shell.

Scope: DSIR only. RTK/RQIR excluded.

## Purpose

This is an activation-mechanism-only successor to `experiments/073bu_wm_s3_selfhosted_science_activation_v0_2_prereg.md`. The connected GitHub tool available in the active research session does not expose a new-workflow `workflow_dispatch` write action. The user has explicitly authorized the assistant to launch the already-approved Exp073BU heavy science run. Therefore v0.3 replaces only the manual UI dispatch event with a unique path-scoped push activation that the connected GitHub write capability can execute.

This v0.3 shell **does not change** the scientific operator, masks, geometry, DES inputs, band edges, NaMaster/PyMaster version, production driver, fresh-PCL helper, exact adapter, downstream implementation, A/B ordering, checkpoint namespaces, comparator, thresholds, terminal classes, or claim boundary.

## Unchanged science authority

The original Exp073BU science preregistration remains authoritative:

- file `experiments/073bu_article3_wm_s3_fresh_independent_ab_exact_repeatability_v0_1_prereg.md`;
- commit `e1a0332c128c87049fb8699018a3a3e71c9c5321`;
- blob `816542c7eb7a8ba4e72d6e01228aa62d05c7c805`;
- required PASS token `PASS_EXP073BU_WM_S3_FRESH_AB_EXACT_REPEATABILITY_V0_1`.

The admitted numerical implementation remains exactly:

- production driver `ci/exp073bu_wm_s3_fresh_ab_production_v0_1.py` blob `5c8d5d3463e455389a1ca3df2639bf06a3b7b603`;
- fresh S3 helper `ci/exp073bu_fresh_wm_s3_pcl_v0_1.py` blob `73ef04c479547dc8e2e89c9f511f1a55fae3ed64`;
- exact adapter `ci/exp073cv_wm_s3_production_exact_adapter_v0_1.py` blob `dafe86086a470c852106f0d4ecccbda1d389e397`;
- component lineage `ci/exp073cv_component_blobs_v0_1.json` blob `0d6d6e882d1a4cf1ff79fbe8227a4f2b460c7e40`;
- exact mmap downstream `ci/exp073by_mmap_full_mcm_downstream_v0_1.c` blob `acafb095deafae7602101d8305e239341010ba79`;
- science launcher `ci/exp073bu_wm_s3_science_launcher_v0_1.py` blob `1a54ad89d32dd217443bc3062a6215bf10e8b17d`.

A/B namespaces remain `checkpoints/exp073bu-wm-s3-a-v0-1` and `checkpoints/exp073bu-wm-s3-b-v0-1`.

## Activation mechanism

The science workflow v0.3 is allowed to trigger only on a push to `main` that changes the unique file `control/activate_exp073bu_wm_s3_science_v0_3.txt`. There is no schedule and no broad push trigger. Creation or audit of the workflow does not activate science.

Before the activation control file is changed, a hosted-only v0.3 audit must PASS and an immutable recovery record containing the exact v0.3 science-workflow blob must be committed on `main`.

The activation commit itself is the explicit execution event authorized by the user's instruction to launch independently. The run-local hosted preflight must re-bind the exact source head, prereg blobs, implementation blobs, v0.3 workflow blob and audit recovery. Only then may the single `[self-hosted, Linux, X64]` science job run.

## Frozen execution and science classes

Execution remains fresh A then fresh B, sequentially, followed only after two complete provenance-valid receipts by exact comparison of the whole canonical `<f8 [39,12288]` arrays using both SHA256 equality and `numpy.array_equal`.

Allowed terminal classes remain exactly:

- `PASS` only with exact whole-array equality and full valid provenance;
- `SCIENTIFIC_REPEATABILITY_FAIL` only when two complete provenance-valid A/B arrays differ exactly;
- `INFRASTRUCTURE_INCOMPLETE` when comparable arrays do not exist because infrastructure/execution/dependency failed;
- `BLOCKED` when source/prereg/implementation/provenance/exclusivity/checkpoint identity is invalid or ambiguous before valid comparison.

No tolerance, ULP, rounding, smoothing, averaging, preferred-replica rerun, effective-scale or fiducial-P rescue is permitted.

## Historical boundary

The v0.1 GitHub-validation failure remains infrastructure history only and created no numerical authority. The successful v0.2 hosted audit remains support-only `+0/+0`. v0.3 does not reinterpret either result and does not increase Article-3 science readiness until a valid Exp073BU terminal science result exists.
