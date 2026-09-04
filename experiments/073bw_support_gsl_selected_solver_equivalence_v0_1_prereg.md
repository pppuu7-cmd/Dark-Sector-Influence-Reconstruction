# Exp073BW v0.1 — GSL selected-solver exact-equivalence support QA preregistration

Date frozen: 2026-09-04
Scope: DSIR only; hosted deterministic synthetic support QA.
Accounting: `+0/+0` for every outcome. No Wm_S3 authority and no Exp073BU science activation can be created.

## Prospective question

Exp073BV R1 established exact equality between the public Python wrapper and direct stock SWIG raw-buffer route, so the historical Exp073BU selected-compact Q2 discrepancy is not caused by Python reshape/transpose semantics. This gate isolates the next causal hypothesis: whether replacing stock GSL LU with NumPy/OpenBLAS solve is sufficient to explain the exact mismatch, while holding the previously frozen selected/general-coupling construction fixed.

This gate is diagnostic. It is not allowed to promote the selected compact route into Exp073BU science, because the scientific preregistration requires full stock component semantics before TE selection.

## Frozen lineage
- PyMaster/NaMaster runtime: exactly 2.7 / 2.7.x from conda-forge.
- stock source authority: `LSSTDESC/NaMaster` tag `v2.7`, commit `24365fa59a38c15732f4f37e8b29265b75c442d5`.
- source audit: S1 run/job `33816987697` / `100851195938`, artifact `9916910028`.
- Exp073BV exact wrapper/raw-layout R1: run/job `33820184200` / `100860976434`, artifact `9917999087`, immutable recovery `recovery/2026-09-04_exp073bv_wrapper_raw_layout_r1_exact.md`.
- Python helper `ci/exp073bw_gsl_selected_solver_equivalence_v0_1.py`, introduction commit `d58e57925f1dd1a9abab9b50ce4a50a798e720d0`, frozen Git blob `22c0cb391931e578f92c7ce75c4dba3429e09265`.
- C/GSL helper `ci/exp073bw_gsl_selected_solver_equivalence_v0_1.c`, introduction commit `b87405206145228f0e0fbde6ae0447407fe8a308`, frozen Git blob `c247d449ecaec12ab05975181f0a05e4c3ac52fe`.

Any lineage/blob mismatch is fail-closed before numerical interpretation.

## Frozen domain and operations
Exactly the same three deterministic NSIDE=16, RING, lmax=47 weighted synthetic mask pairs and band edges `[0,4,8,12,16,24,32,40,48]` used by Exp073BV.

For every case:
1. build fresh stock spin-0 x spin-2 workspace and complete stock window tensor `[2,8,2,48]`;
2. select stock `wins[0,:,0,:]` only for this diagnostic comparison;
3. independently reproduce the already-frozen selected/general-coupling construction: mask ALMs -> `hp.alm2cl` -> `nmt.get_general_coupling_matrix(pcl,0,2,0,2)` -> exact source-order band compression A -> K;
4. solve `K X = A` twice: (a) diagnostic NumPy baseline; (b) compiled GSL 2.7 helper using `gsl_linalg_LU_decomp` once and `gsl_linalg_LU_solve` for each RHS ell column in increasing source order;
5. compare stock selected tensor against the GSL-selected result by whole canonical C-order `<f8` SHA256 and `numpy.array_equal`.

No closeness tolerance is an acceptance criterion. Max-absolute differences against GSL and NumPy are recorded only as non-authorizing diagnostics.

No DES, R1 physical, historical Wm, Exp073CR/CQ/CM numerical arrays, or Exp073BU physical data may be read.

## Frozen classifications
- `G1_EXACT_SELECTED_GSL_EQUIVALENCE`: all three cases have exact canonical SHA equality and `numpy.array_equal=true` between stock selected windows and the GSL-selected construction. This identifies NumPy/OpenBLAS solve order as sufficient for the earlier Q2 exact mismatch under these frozen synthetic cases. It still does not authorize selected-only science; next step is a prospectively frozen full-component stock-C/GSL implementation/equivalence QA.
- `G2_SELECTED_CONSTRUCTION_NOT_EXACT`: valid provenance, but any stock-vs-GSL exact mismatch. This falsifies the hypothesis that merely substituting stock GSL LU into the selected compact construction is sufficient. The next permitted path is full-component stock C/GSL operation-order implementation; no tolerance rescue.
- `G3_SOURCE_LINEAGE_MISMATCH`: PyMaster/GSL/helper/source freeze mismatch. BLOCKED `+0/+0`; no numerical interpretation.
- `G4_INFRASTRUCTURE_INCOMPLETE`: compile/dependency/runner/software failure before a valid complete receipt. Infrastructure `+0/+0`; diagnose first causal failure and repair prospectively without changing this gate.

## Workflow discipline
Hosted Ubuntu only. Before numerical execution the workflow must verify prereg/helper blob identities, install exact `namaster=2.7` (thereby GSL 2.7 in the same conda environment), verify runtime `workspaces.py` SHA `442e23eb542087566689271ad1c897d5da45f5b76e39def05b37d93b0098178f`, compile the frozen C helper against that conda GSL, then run the frozen Python helper. Upload the complete JSON receipt even on terminal classification. Workflow success alone is not G1/G2; raw receipt/artifact must be consumed.

No home/self-hosted runner, durable checkpoint, readiness increment, or scientific authority is allowed.
