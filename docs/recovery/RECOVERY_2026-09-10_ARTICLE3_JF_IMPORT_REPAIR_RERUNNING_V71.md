# DSIR recovery V71 — Exp073JF first attempt infrastructure-invalid; import repair active

Date: 2026-09-10. Scope: DSIR only. Never mix RTK or RQIR.

All scientific authority and frozen boundaries from V70 remain unchanged. Repaired Exp073IR remains `NUMERICALLY_UNRESOLVED_EXP073IR`; covariance restriction and Wm_S3 remain unauthorized.

## Exp073JF attempt 1
Run/job `34480017627 / 102880180988`, head `a99465377e0d070bce43982906d29ba21b1eb06b`, completed FAILURE. Contract/JE-authority, frozen dependency/capacity regression, and exact pinned patched CLASS-IV build all succeeded. The first causal failure occurred before any JF numerical computation or artifact creation: direct script execution raised `ModuleNotFoundError: No module named 'ci'` while importing the sibling JE implementation as `ci.exp073je_article3_layerb_shared_fixed_k_grid_scaling_v0_1`.

Classification: infrastructure/software failure `+0/+0`, not scientific FAIL and not evidence about the N={384,512} gate.

## Smallest repair
Only the local Python import path was repaired: commit `1cd0692454e238162be0235f56e49453b4f40999` inserts the executing `ci/` directory in `sys.path` and imports the sibling JE module directly. No numerical constants, grid nodes, estimator, physics, exact references, h=1e-4, kpd ladder, or REL_TOL=1e-3 changed.

A reproducible import regression was then added after frozen numpy installation, and the workflow was touched to dispatch the repaired run: workflow/head commit `2e5e43de2abaec3be93f5fe1a2fbe909b6e86048`. The regression imports the JF module through `PYTHONPATH=ci` and requires `NS==(384,512)` before build/science.

## Current authoritative process
Workflow `exp073jf-article3-layerb-shared-fixed-k-grid-extended-density-v0-1`; run/job `34480349238 / 102881291672`; branch/head `main / 2e5e43de2abaec3be93f5fe1a2fbe909b6e86048`; checkpoint N/A; GitHub-hosted `ubuntu-24.04`; home/self-hosted ownership none. Last observed state IN_PROGRESS.

Exact next action: terminal-consume `34480349238`. If valid, independently verify raw result/artifact hashes and classify strictly under the frozen Exp073JF contract. If another infrastructure failure occurs, diagnose the first causal defect before any further rerun. If valid observations show a scaling candidate, only nominate the smallest qualifying N for a separate prospective full-support feasibility audit; otherwise continue mechanism isolation with no tolerance rescue.
