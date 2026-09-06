# Exp073EL — WW_S0_S1 full-resolution resource-path admission v0.3

**Prospective governance supersession:** 2026-09-06, after real Exp073EO v0.2 admission PASS and before any Exp073EL self-hosted execution.

**Accounting:** resource/support `+0/+0`; cannot create `WW_S0_S1` science authority.

This v0.3 changes exactly one governance dependency from the never-executed Exp073EL v0.2 preregistration. Exp073EL v0.2 required literal token `PASS_EXP073EO_WW_S0_S0_FILEBACKED_PROVENANCE_ADMISSION_V0_1`. The first real EO v0.1 auditor was subsequently shown to contain a JSON representation bug for the otherwise exact Exp073EM artifact ID. The prospectively frozen representation-only Exp073EO v0.2 repair has now produced real admission token `PASS_EXP073EO_WW_S0_S0_FILEBACKED_PROVENANCE_ADMISSION_V0_2`, run/job `34005373819 / 101411448176`, artifact `9980754356`, digest `sha256:0e1a4cff3b761fecc65d8e07df9e56f8109fd221fb4454746caa8c7d0f2fb4be`, with `classification=SCIENTIFIC_AUTHORITY_ADMITTED` and `ww_s0_s0_authority_created=true`.

Therefore the sole v0.3 governance change is:
- replace the unsatisfied literal EO-v0.1 prerequisite token with the exact admitted EO-v0.2 token above;
- bind that exact EO run/job/artifact/digest/head and no other EO authority.

Every numerical route, support prerequisite, host threshold and resource criterion from `experiments/073el_ww_s0_s1_full_resolution_resource_path_v0_2_prereg.md` remains unchanged. In particular: NSIDE=4096; ell=0..12287; 39 bands; ordered spin-2 `S0 -> S1`; selected `EE<-EE`; canonical `<f8 [39,12288]`; sequential source reconstruction/spill; unified v0.2 file-backed MCM construction/read; exact regular-file geometry; public `get_bandpower_windows()` only in fresh serialized state; no tolerance/allclose/rounding/smoothing/averaging/effective-ell/reduced-resolution rescue.

The already statically audited host checker remains byte-frozen and unchanged: `ci/exp073el_host_resource_admission_v0_2.sh`, blob `f0a3a2e42326183944b838d42c5072c59e259b68`. Its only valid PASS token remains `PASS_EXP073EL_WW_S0_S1_FULLRES_RESOURCE_PATH_V0_2`; v0.3 is a governance-binding supersession, not a change to the resource arithmetic or checker implementation.

Mandatory support PASS chain remains Exp073EM, EK, EP, ER, EU, EV, EW; Exp073ET remains immutable historical support FAIL `+0/+0`. Exp073EX remains the static fail-closed qualification of the unchanged checker.

A resource BLOCK or failure remains `+0/+0` and must never be promoted to `WW_S0_S1` scientific FAIL. A resource PASS only authorizes prospectively freezing and dispatching a separate full-resolution `WW_S0_S1` A/B scientific gate.
