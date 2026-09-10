# DSIR recovery V69 — Exp073JE repair static-audit ordering fixed; third attempt active

Date: 2026-09-10. Scope: DSIR only.

Preserve all scientific authority and frozen boundaries from V68 unchanged. Exp073IR remains `NUMERICALLY_UNRESOLVED_EXP073IR`; covariance restriction and Wm_S3 remain unauthorized.

Exp073JE attempt 1, run/job `34474514433 / 102861967751`, remains infrastructure/software failure `+0/+0`: `malloc(): corrupted top size` before scientific artifact creation. Its first diagnosed capacity mismatch is addressed prospectively by repair prereg commit `16f984a9a81ac5e3d559d67e191f7bb9f6ffd85b` using parser `_ARGUMENT_LENGTH_MAX_ 1024 -> 32768` plus the already frozen k-output capacity `30 -> 512`, with no science change.

Exp073JE attempt 2, run/job `34474839354 / 102863020808`, head `6090af1b41b86bd878c4e348874a496c04a09053`, is also infrastructure-only `+0/+0`: the newly added serialized-length regression imported numpy before the dependency-install step, producing `ModuleNotFoundError: No module named 'numpy'`. No CLASS build or scientific computation ran in attempt 2.

Smallest repair: move the exact same static serialized-length regression after frozen numpy installation. No numerical settings or science criteria changed. Workflow repair commit/head `3f74511a78724ac11e64d98284321df12cc7d1a8`.

Current authoritative process: workflow `exp073je-article3-layerb-shared-fixed-k-grid-scaling-v0-1`, run/job `34474978911 / 102863474356`, head `3f74511a78724ac11e64d98284321df12cc7d1a8`, GitHub-hosted `ubuntu-24.04`, checkpoint N/A, home/self-hosted ownership none. Last observed state IN_PROGRESS. Contract/repair/JD lineage checks succeeded; frozen dependency installation plus parser-capacity regression is in progress.

Exact next action: terminal-consume `34474978911`; if successful, inspect and independently hash the raw result and capacity patch artifact and classify strictly under the original frozen JE scaling contract. If it fails, diagnose the first causal failure before any further rerun. A support diagnostic cannot retroactively PASS Exp073IR or authorize covariance restriction.
