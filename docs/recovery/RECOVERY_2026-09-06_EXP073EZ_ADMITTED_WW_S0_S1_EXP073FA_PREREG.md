# DSIR recovery — 2026-09-06 — Exp073EZ admits WW_S0_S1; Exp073FA preregistered

Scope: DSIR only; RTK/RQIR excluded.

## Exp073EY terminal candidate consumed

Authoritative checkpoint-resume run/job `34010599584 / 101425638857` completed SUCCESS at head `4c570bf6b7f3f53547f43e2882149defa125da89`. Candidate artifact `9983630139` (`exp073ey-ww-s0-s1-filebacked-ab-resume-v0-2`) has GitHub digest and independently downloaded ZIP SHA256 exactly `12291c1c9f6100ebfb03a6db1e613f422bd48bc6c02720f89ee613c8646cf9d6`.

Raw artifact validation confirmed both complete A/B six-stage checkpoint chains, ordered distinct `(S0,S1)`, source head `de83e20a68f79ccf25b89b0d33eb4206e294c757`, contract `b7845df5ce4bc2bd730461476b7ff0831512003ceb5b3558436005c9876bd251`, regular-file-backed MCM `19,327,352,832` bytes with `/proc/self/maps` proof, public serialized-workspace BPW route, full BPW SHA `eb6c2427c86e76225a39feab3a4788d3a0b7ba142809f79cecb2e362c0b44b98`, and exact canonical selected A/B SHA `49af7a3d165daaf7cc6781e2286e45cd5baa0042ed9770800588bced7d700e79`. `numpy.array_equal=true`, all finite, no tolerance rescue. Candidate token was `PASS_EXP073EY_WW_S0_S1_FILEBACKED_AB_EXACT_REPEATABILITY_V0_1`; candidate alone did not create authority.

## Exp073EZ admission

Terminal-binding erratum v0.3 was frozen after artifact consumption: `experiments/073ez_ww_s0_s1_filebacked_checkpoint_provenance_admission_v0_3_terminal_binding_erratum.md`, commit `9b63c291d6c966166a70111e31fd39ab0c31b1d6`, blob `d3c6c1ba9c6f6f4d41d1d123e765f8de5ead0fec`.

First hosted admission run `34017884048 / 101444857315` failed only because the hosted Python image lacked NumPy. All preceding frozen identity, terminal run/job, artifact metadata and independent ZIP digest checks had passed. Classification is `INFRASTRUCTURE_DEPENDENCY_FAIL +0/+0`; no scientific criterion was reached or changed.

Minimal dependency repair pinned only audit dependency `numpy==2.3.2`; science/provenance checks were unchanged. Repair commit `a429b4a3b439bcca92e3adccfaa0de621137f6bc`.

Repaired admission run/job `34017921734 / 101444964371` completed SUCCESS. Raw log emitted exactly:
- `PASS_EXP073EZ_WW_S0_S1_FILEBACKED_PROVENANCE_ADMISSION_V0_1`
- `classification=SCIENTIFIC_AUTHORITY_ADMITTED`
- `science_gate_scored=true`
- `ww_s0_s1_authority_created=true`

The admission re-downloaded artifact `9983630139`, independently reverified ZIP SHA256, checked frozen repository blobs and candidate run/jobs, all A/B manifests and receipts, exact selected payload SHA, canonical `<f8 [39,12288]` arrays, `numpy.array_equal`, finiteness, public file-backed BPW route, mmap/storage proof, live exclusivity evidence, and post-receipt pruning provenance. Therefore `WW_S0_S1` is now admitted scientific authority.

## New frontier

Frozen WW order advances exactly to `WW_S0_S2`. No queued or in-progress DSIR run existed at reconciliation immediately after admission.

Exp073FA science preregistration was frozen at commit `a1ce88850d037b408eb5f8cdd3275dbc7cf629b4`, file `experiments/073fa_ww_s0_s2_filebacked_full_resolution_ab_science_v0_1_prereg.md`, blob `edc044792be8ac7b796c8469943924942ae91932`.

It preserves the admitted full-resolution architecture but changes the scientific pair prospectively to ordered distinct `(S0,S2)` using authoritative source indices 0 and 2. Dedicated checkpoint namespaces are `checkpoints/exp073fa-ww-s0-s2-a-v0-1` and `...-b-v0-1`; six-stage checkpoint semantics, exact file-backed public-BPW route, 8-core/home exclusivity, exact A/B criterion, and all global frozen boundaries remain unchanged. Candidate token is frozen as `PASS_EXP073FA_WW_S0_S2_FILEBACKED_AB_EXACT_REPEATABILITY_V0_1`; candidate PASS alone will not create authority.

Exact next action: perform a hosted fail-closed implementation/static audit for Exp073FA before activating any self-hosted S0_S2 computation. On static PASS and live zero competing self-hosted ownership, launch the checkpointed home A/B gate. Any implementation failure is +0/+0 and must be repaired without changing the preregistered science.