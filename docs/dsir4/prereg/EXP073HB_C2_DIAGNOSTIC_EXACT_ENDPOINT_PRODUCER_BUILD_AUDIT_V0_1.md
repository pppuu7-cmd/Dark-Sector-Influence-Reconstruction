# Exp073HB — C2 diagnostic exact-endpoint producer build/static audit v0.1

Status: PROSPECTIVELY FROZEN after raw-validated Exp073HA support PASS. Scope: DSIR only. Scientific contribution ceiling: `SUPPORT_PLUS_0_PLUS_0`.

## Purpose

Exp073HA proved the admissible native exact-endpoint extraction architecture against pinned CLASS-IV sources. Exp073HB freezes the implementation/build-audit contract for a diagnostic-only producer patch before any C2 cosmological runtime or 28-packet payload exists.

This gate may clone, patch and compile the pinned solver on GitHub-hosted infrastructure. It MUST NOT execute a cosmological CLASS run, MUST NOT create the 28-packet/1792-byte record set, and MUST NOT decode, map, predict or create model/scientific authority.

## Frozen upstream and prior authority

- hypothesis: `C2_IDE_LOCAL_TANGENT_CONE`;
- upstream solver: `kaeonikc/class_iv@ac627d54e9ce196a08878d1ba33999819925d19c`;
- pinned `source/perturbations.c` Git blob: `92a48331658c5941ed4eb43b0e98ee78e39b8385`;
- pinned `tools/evolver_ndf15.c` Git blob: `790ced55f2eaa08e805d467734ad1435954bc5b7`;
- Exp073HA prereg blob: `f970da98a91f541e62aa957b16aaf4ea12bd98a7`;
- Exp073HA PASS token: `PASS_EXP073HA_C2_NATIVE_EXACT_ENDPOINT_EXTRACTION_STATIC_AUDIT_V0_1`;
- GR sampling contract SHA256: `6a14470157e0677ee10d65d24e759907b9a5df5fe1fd9d80e940787224dbfe9b`;
- recorder blob authority remains `c6144598b9f75908ee27a517d31eda509f7947f6`;
- exact z requests: `[0.295,0.51,0.706,0.934,1.317,1.491,2.33]`;
- exact physical-k requests in Mpc^-1: `[0.00067,0.00201,0.0067,0.0201]`;
- request order: z-major / k-minor, exactly 28 requests.

## Frozen implementation semantics

The diagnostic producer patch is observation-only and must satisfy all of the following.

1. It must be opt-in. With diagnostic mode absent, the patched solver must retain the ordinary upstream scientific path; the patch may not change equations, background/perturbation dynamics, approximation switches, precision/tolerance values, species sums, accepted physical branch, gauge transformation logic, or normal output semantics.
2. Requested k must enter only through native `k_output_values` insertion/indexing. No nearest-neighbour, tolerance match, rounded/effective k, bin centre, post-hoc k interpolation or fiducial-P substitution is allowed.
3. Requested z is literal authority. The patch may resolve only `background_tau_of_z(pba,z,&tau_target)` on that exact z. No independently reconstructed background, tolerance match, nearest time row, effective z or post-run perturbation interpolation is allowed.
4. The requested `tau_target` must be the integration terminal endpoint for the diagnostic extraction run. The admitted state is the accepted NDF15 `ynew` at `tnew=tfinal=tau_target`; `interp_from_dif`, `perturb_sources_at_tau`, source-table splines and any other perturbation-state interpolation are forbidden for recorder bytes.
5. Capture must happen only after terminal step acceptance. Newton trial states, rejected steps and intermediate accepted steps are invalid.
6. The producer must expose the previously frozen pre-transform total-matter values: `ppw->delta_m` and `ppw->theta_m` immediately after native total-matter construction and before the downstream standard gauge-invariant `delta_m` transformation. No second gauge correction and no reuse of standard downstream `index_tp_delta_m` as the raw record source.
7. If implementation uses process-global diagnostic flags/state, hosted build/static audit must prove that real extraction is frozen to a single process/thread (`OMP_NUM_THREADS=1`) and that the armed capture state exists only around the already accepted terminal endpoint callback. No racy capture path is admissible.
8. Recorder serialization contract remains external/frozen. The patch may hand exact endpoint values to the existing recorder interface but may not alter the recorder schema, packet count, packet width, request order, arithmetic meaning, provenance fields or admission logic.

## Required implementation artifacts

Before PASS, the repository must contain a deterministic patch/source artifact and a hosted audit workflow that fail closed on exact identities. The audit must:

- verify this preregistration blob exactly;
- verify the pinned upstream commit and both upstream Git blobs exactly before patching;
- apply the patch cleanly with no fuzz/rejects;
- statically prove an opt-in diagnostic switch and absence of unconditional scientific-path changes;
- statically prove exact-k native indexing, literal-z `background_tau_of_z`, terminal-endpoint orchestration, accepted `ynew` capture, pre-transform `delta_m/theta_m` capture, and explicit rejection/non-use of `perturb_sources_at_tau`/`interp_from_dif` for recorder bytes;
- compile the patched pinned solver successfully on GitHub-hosted infrastructure;
- run a no-cosmology smoke check limited to build/help/parser or equivalent non-scientific startup path if needed, never a cosmological model execution;
- report the exact patch blob/hash and resulting patched source hashes;
- fail if a payload file of 1792 bytes or a complete 28-record runtime set is produced during the audit.

## PASS token and classification

The only PASS token is:

`PASS_EXP073HB_C2_DIAGNOSTIC_EXACT_ENDPOINT_PRODUCER_BUILD_AUDIT_V0_1`

PASS classification is exactly `SUPPORT_PLUS_0_PLUS_0` and must also emit:

- `cosmological_run_started=false`;
- `record_payload_created=false`;
- `runtime_record_count=0`;
- `prediction_ready=false`;
- `scientific_model_authority_created=false`;
- `G_DOMAIN_MAPPING=NOT_YET_TESTABLE`.

Any patch/build/static-audit failure is `BLOCKED/IMPLEMENTATION_PLUS_0_PLUS_0`, never scientific FAIL.

## Authority after PASS

A raw-log validated PASS authorizes only the future real diagnostic extraction under the already frozen GZ receipt-admission contract and only when no competing home-heavy owner exists. It does not itself authorize the 28-packet runtime, decoding, mapping, prediction or model authority. While Exp073GA owns the home runner, real C2 runtime remains `BLOCKED_BY_HEAVY_RUN_EXCLUSIVITY`.
