# Exp073BU — Wm_S3 self-hosted science activation v0.2

**Frozen prospectively:** 2026-09-04 after the v0.1 manual science workflow was found to be rejected by GitHub Actions validation before any self-hosted Exp073BU numerical job was created.

Scope: DSIR only. RTK/RQIR excluded.

## Purpose

This is an infrastructure-only successor to `experiments/073bu_wm_s3_selfhosted_science_activation_v0_1_prereg.md`. It does not change the scientific contract, masks, geometry, binning, numerical implementation, A/B ordering, exact-equality rule, classification vocabulary, thresholds, or claim boundary frozen in `experiments/073bu_article3_wm_s3_fresh_independent_ab_exact_repeatability_v0_1_prereg.md`.

The original Exp073BU science preregistration remains authoritative:

- commit `e1a0332c128c87049fb8699018a3a3e71c9c5321`;
- blob `816542c7eb7a8ba4e72d6e01228aa62d05c7c805`;
- PASS token `PASS_EXP073BU_WM_S3_FRESH_AB_EXACT_REPEATABILITY_V0_1`.

## Historical v0.1 infrastructure result

The v0.1 science workflow blob `62774cbbe8073aeeb3f66e04a50c891173f91a23` is preserved as historical infrastructure. GitHub Actions produced a validation-level failure with no jobs for run `33883760874`; this is not a numerical/scientific result and creates no Wm_S3 authority. The causal defect is use of the `runner` context in `jobs.science-ab.env` (`CHECKPOINT_ROOT: ${{ runner.temp }}/...`), a context that is not valid at that workflow evaluation scope.

No Exp073BU A or B numerical output was produced or inspected in diagnosing this defect.

## Frozen v0.2 repair

The v0.2 workflow must be identical in science intent and admitted implementation to v0.1 except for the following execution-shell repair:

1. remove the job-level `CHECKPOINT_ROOT: ${{ runner.temp }}/...` expression;
2. create and export the persistent checkpoint root inside the already-existing self-hosted runtime step after a runner has been assigned;
3. update self-referential workflow path/version labels and the hosted-audit recovery path to v0.2;
4. preserve manual-only `workflow_dispatch`; no push or schedule activation for science.

All admitted implementation blobs remain frozen unchanged:

- production driver `ci/exp073bu_wm_s3_fresh_ab_production_v0_1.py`: `5c8d5d3463e455389a1ca3df2639bf06a3b7b603`;
- fresh helper `ci/exp073bu_fresh_wm_s3_pcl_v0_1.py`: `73ef04c479547dc8e2e89c9f511f1a55fae3ed64`;
- exact adapter `ci/exp073cv_wm_s3_production_exact_adapter_v0_1.py`: `dafe86086a470c852106f0d4ecccbda1d389e397`;
- component lineage `ci/exp073cv_component_blobs_v0_1.json`: `0d6d6e882d1a4cf1ff79fbe8227a4f2b460c7e40`;
- full-stock mmap downstream `ci/exp073by_mmap_full_mcm_downstream_v0_1.c`: `acafb095deafae7602101d8305e239341010ba79`;
- science launcher `ci/exp073bu_wm_s3_science_launcher_v0_1.py`: `1a54ad89d32dd217443bc3062a6215bf10e8b17d`;
- CX v0.4 A1 recovery blob `43b658028f74b7a0b52fca8261beeb58026d8ffc`.

## Required activation chain

Before v0.2 can run DES-scale numerics:

1. a hosted-only audit must bind the exact v0.2 workflow blob and this prereg blob and PASS;
2. the resulting immutable recovery record must exist on `main`;
3. the user must explicitly dispatch the v0.2 workflow on `main` with `ACTIVATE_EXP073BU_WM_S3_V0_1`;
4. the run-local hosted preflight must PASS exact binding and repository noncompetition;
5. exactly one self-hosted `[self-hosted, Linux, X64]` job may own `DSIR-HOME-PC`;
6. live local/process exclusivity must PASS immediately before A starts;
7. replica A then B execute sequentially under the original isolated namespaces;
8. only after both complete receipts exist may the exact whole-array SHA256 plus `numpy.array_equal` comparator score science.

## Terminal vocabulary and authority

The only allowed terminal science classes remain `PASS`, `SCIENTIFIC_REPEATABILITY_FAIL`, `INFRASTRUCTURE_INCOMPLETE`, and `BLOCKED`. No tolerance, ULP, rounding, smoothing, averaging, effective-scale, fiducial-P, preferred-replica, or rerun-to-prefer rescue is allowed.

This v0.2 activation-shell repair is support-only `+0/+0`. Wm_S3 scientific authority remains absent until a valid terminal Exp073BU comparator result exists.
