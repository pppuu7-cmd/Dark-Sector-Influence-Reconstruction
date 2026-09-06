# DSIR research log — 2026-09-06 — Exp073EY patch-binding repair/resume

Scope: DSIR only.

- Consumed Exp073EY terminal run/job `34006214398 / 101413789646` rather than treating workflow failure as science. Artifact `9982181156`; GitHub and independent ZIP SHA256 `9b600273307c915cba691a998ea33a9443f188a8d4f81f03bc60fb471c0a61c5`.
- Raw evidence preserves replica A `fresh_sources_complete`, `fresh_workspace_mcm_complete`, `mcm_fits_verified`; no later A stage, no B science and no A/B token. Classification `INFRASTRUCTURE_SOFTWARE_PATCH_BINDING_FAIL +0/+0`.
- First causal error: fail-closed serialized-read adapter found zero file-backed FITS-read candidates after A MCM/FITS completion.
- Root cause: EY bound construction-only patch blob `f1eb886ca8af2584a9f621f333cd8be3c6cdb967`; unlike the already qualified Exp073ER read patch blob `d534b698f9131688d263eedcef27260386c58641`, it has no `src/nmt_io.c` allocator hook.
- Prospectively froze repair erratum blob `a6fc7a1a3af86f8f02eba8c02294283192642784` and wrapper blob `a9cabeadc9b091424246adf00e9959dc62145e9b`. Frozen science drivers/source/contract and checkpoints are unchanged.
- Hosted repair audit `34010599584 / 101425618749` PASS. Home checkpoint-resume job `101425638857` is active on head `4c570bf6b7f3f53547f43e2882149defa125da89`; DSIR-HOME-PC exclusively reserved.
- Resume must restore A through `mcm_fits_verified` exactly rather than recompute it; local Exp073EM exact storage qualification remains mandatory before science.

Next: terminal-consume resume artifact. Candidate exact PASS still requires separately preregistered Exp073EZ admission before WW_S0_S1 authority.