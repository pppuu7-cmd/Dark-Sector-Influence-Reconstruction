# Exp073CF continuation successor workflow/binding prepared

Date: 2026-09-02
Classification: `STATIC_INFRASTRUCTURE_PREPARATION_NONCLASSIFYING`, readiness `+0/+0`.

## Coordination check

Immediately before preparation, repository-wide GitHub Actions state was `queued=0`, `in_progress=0`. Exp073CF attempt2 run `33548649445` is already terminal infrastructure-incomplete and is not an active frontier despite older chat wording.

No self-hosted job was triggered, rerun, duplicated, replaced, or superseded in this preparation.

## Prepared real workflow

Workflow path: `.github/workflows/exp073cf-continuation-successor-v0-1.yml`

Workflow commit: `93ac80426c877c4769ded24fb16196fcfa2501f5`.

The workflow preserves:

- `[self-hosted, Linux, X64]` A/B heavy replicas with `max-parallel=1`;
- `OMP_NUM_THREADS=8`, chunk size 4 through the frozen continuation wrapper, and 60 s heartbeat;
- exact R1 artifact source and network-hardened DES transport with exact size `104595840` and SHA-256 `a519b8522f899e4c33267bb0749f9734f8b7fa760d195636456d370f809a3d55`;
- memory-stable fresh Wm_S2 PCL construction;
- frozen BW/range compilation flags and frozen checkpoint-boundary preflight;
- exact-pinned checkpoint restore through `ci/dsir_checkpoint_git_sync_v0_2.sh` only;
- A restore head `5c7ccddb54afe1ad286d08abc6f7372aa5a11103` (32/39 authoritative bands);
- B restore head `ce9189a1ccaabc62708f753897b9cab5f51cb9f4` (28/39 authoritative bands);
- resumed heavy calculation only through `ci/exp073cf_continuation_wm_s2_v0_1.py`;
- frozen compact and final exact comparators using `np.array_equal` plus SHA-256, with no tolerance/ULP/rounding/averaging/smoothing/majority/preferred-replica rescue;
- readiness increment requiring a separate frozen ledger update.

## Prospective binding

Binding path: `experiments/073cf_continuation_successor_v0_1_binding.json`

Binding commit: `1a9f34f87d4e485b00b073e1a75eafd90b0cbe5c`.

Binding state is deliberately `PREPARED_NOT_AUTHORIZED`; `scientific_contract_changed=false`.

Historical payload provenance remains exact:

- source/head contract: `f9cb1eec582276776ddac3b1207686b1e01d3b6a`;
- historical checkpoint-sync fingerprint: `96886916b41dce7f0a40807622928c841ef5fc58`.

Continuation provenance remains separate:

- preregistration `36853b723b172a6038c6d3023805f08f37ffac72`;
- wrapper `ce818db7ae53376ba6e5f7934c24f4c5acb3c75c`;
- checkpoint transport v0.2 `bc468ca73a3c4e281bd2b1ee46d6f7704bb54bb1`.

## Activation guard

The workflow requires `ci/exp073cf_continuation_successor_v0_1.activation.json` and checks that its workflow and binding commits exactly match repository history. That activation file is intentionally absent at this stage. Therefore this preparation does **not** authorize DSIR-HOME-PC execution.

A later activation must be separately prospective, must follow a fresh repository-wide `queued=0` / `in_progress=0` collision check, and must bind the exact workflow and binding commits before any intended run.

## Authority/readiness

Exp073CF attempt2 remains:

`INFRASTRUCTURE_EXECUTION_INCOMPLETE_NO_SCIENTIFIC_CLASSIFICATION_EXP073CF_ATTEMPT2`, `+0/+0`.

Durable authority remains A 32/39 and B 28/39. No complete A/B comparator inputs exist and Wm_S2 repeatability remains unclassified.

Article-3 readiness remains **Verified 52.0% | Draft/data 53.7%**.

## Next permitted gate

Perform a final read-only/static audit of the *actual* workflow and binding against the previously passed disabled specification, including activation fail-closed semantics, exact restore roots, frozen helper lineage, DES binding, heartbeat, comparator/finalizer bodies, and absence of any unauthorized active run. Only if that audit passes may a separate prospective activation/trigger authorization be prepared. Do not launch self-hosted science merely because the workflow and binding now exist.
