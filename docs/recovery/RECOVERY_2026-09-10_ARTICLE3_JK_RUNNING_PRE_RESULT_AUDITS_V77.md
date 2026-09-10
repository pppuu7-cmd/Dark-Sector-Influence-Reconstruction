# DSIR recovery V77 — Exp073JK running, pre-result audits complete

Date: 2026-09-10. Scope: DSIR only.

## Preserved authority

All validated authority from V76 remains unchanged. In particular, repaired Exp073IR remains `NUMERICALLY_UNRESOLVED_EXP073IR`; Exp073JI remains validated full-support feasibility +0/+0; Exp073JJ remains validated `COMMON_GRID_RESOLUTION_REFINEMENT_NOT_CONVERGED_PLUS_0_PLUS_0` with maximum atomic relative component difference 0.037280144773915974; covariance restriction remains unauthorized and Wm_S3 remains unopened.

## Current process

Authoritative Exp073JK workflow/run/job remains:

- workflow: `exp073jk-article3-layerb-common-grid-second-refinement-convergence-v0-1`
- run: `34495159732`
- job: `102931623100`
- launch head: `6490000bd63b68f651c328382a36db03c42c8ccc`
- runner: GitHub-hosted `ubuntu-24.04`
- current state at this recovery update: IN_PROGRESS in the frozen numerical step after contract, numerical stack, CAMB, pinned CLASS-IV build/capacity patch, DES payloads, inherited authorities and BOSS operators all passed.

No self-hosted ownership; no checkpoint namespace is involved.

## Pre-result implementation audit

A response-blind implementation/capacity audit was completed while JK was still running and before any JK response output was available.

Audit file: `docs/dsir4/audits/EXP073JK_PRE_RESULT_IMPLEMENTATION_AUDIT_V0_1.md`, creation commit `c3b4614d1b5fa47bd482f4ff0f8b77cf5917cf14`.

Findings:

- inherited slot 10 maps only to guarded N=1024 / 1025 requested nodes;
- inherited slot 20 maps only to guarded N=2048 / 2049 requested nodes;
- CLASS native `k_per_decade_for_pk=20.0` remains fixed for both, so native-kpd dependence is not reintroduced;
- centered-cubic ln(k), h=1e-4, REL_TOL=1e-3, judged support and physical masks remain unchanged;
- serialized `k_output_values` lengths are 22489 characters for 1025 nodes and 44961 for 2049 nodes, so frozen parser capacity 65536 is adequate;
- `_MAX_NUMBER_OF_K_FILES_=2304` is also adequate for current 2049 nodes.

Conditional infrastructure warning only: a hypothetical later guarded N=4096 architecture would require 4097 requested nodes and about 89918 serialized characters, so current JK capacity limits must not be reused blindly for such a future gate.

## Pre-result convergence-order expectation

A separate method-level expectation was recorded before any JK response output:

`docs/dsir4/audits/EXP073JK_PRE_RESULT_CONVERGENCE_ORDER_EXPECTATION_V0_1.md`, creation commit `fab6a579270857bf7b1f193c2f0ac3cf71ba91f4`.

The exact geometric ln(k) spacings are approximately 0.0127240791 (N=512), 0.00635582056 (N=1024), 0.00317635781 (N=2048), 0.00158779107 (N=4096). A smooth four-node cubic interpolation has nominal fourth-order local remainder. Applying only this method-level scaling to the validated JJ maximum gives an indicative JK scale around 0.00232091, still above 1e-3. Passing at JK from the JJ magnitude in one refinement would correspond to empirical order >~5.213 under the same simple scaling model. One further ideal fourth-order sequential refinement would have indicative scale ~1.45e-4.

These are not JK results, do not change the frozen gate, and do not authorize a later experiment. They only prevent a future valid JK NOT_CONVERGED result from being misclassified as unexpected infrastructure failure and provide prospective rationale for a further sequential resolution gate if JK itself later authorizes it.

## Exact next action

Terminal-consume run 34495159732. Inspect raw logs and artifact, independently verify ZIP/result/capacity hashes and frozen lineage. Classify only against the prospectively frozen JK contract.

- If `COMMON_GRID_SECOND_REFINEMENT_CONVERGED_PLUS_0_PLUS_0`: preserve it as support-only +0/+0 and prospectively freeze the separate scientific Layer-B rerun architecture before evaluating scientific responses.
- If `COMMON_GRID_SECOND_REFINEMENT_NOT_CONVERGED_PLUS_0_PLUS_0`: preserve the negative support result, use the measured empirical refinement reduction factor as interpretation only, then prospectively freeze the next sequential resolution gate. Before any N=4096-class run, enlarge infrastructure capacities prospectively with exact provenance; do not change REL_TOL, interpolation, h, masks or domain.
- If infrastructure failure: diagnose first causal failure and repair only infrastructure, preserving the frozen JK scientific contract.

Global frozen DSIR boundaries remain unchanged: `0.295<=z<=2.33`; judged `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; REL_TOL=1e-3; h=1e-4; no tolerance/rounding/smoothing/averaging/effective-coordinate/fiducial-P rescue.
