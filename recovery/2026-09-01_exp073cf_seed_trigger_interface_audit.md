# 2026-09-01 — Exp073CF seed-trigger and interface audit

Classification: `PRE_ACTIVATION_SEED_AND_INTERFACE_AUDIT_PASS_NO_EXECUTION_AUTHORIZED`; repository-side infrastructure/methodology audit only; `+0/+0`.

## Coordination state

At audit time GitHub reported zero queued DSIR workflow runs and zero in-progress DSIR workflow runs. Exp073CA attempt3 run `33448843621` is terminal and remains `INFRASTRUCTURE_EXECUTION_INCOMPLETE_NO_SCIENTIFIC_CLASSIFICATION_EXP073CA`, not scientific FAIL and not authority.

The home runner remains locked. No self-hosted workflow was created, triggered, rerun or revived by this audit.

## New seed-trigger provenance

Commit `fc4db4477c64c5e3119b99deed629b43fc3acbab` added `ci/exp073cf_fullscale_memory_stable_wm_s2_successor_v0_1.trigger` with state `SEED_NO_EXECUTION`, `activation_binding_commit=null`, and `activated_workflow_commit=null`. No active Exp073CF workflow existed when the seed was created, so this commit created no execution authority.

The older preparation binding `experiments/073cf_fullscale_memory_stable_wm_s2_successor_v0_1_binding.json` remains an immutable historical record and still states `trigger_file_exists=false`. That field is now operationally stale by design; it must not be edited retroactively. The new audit binding records the later seed explicitly.

## Frozen interface audit

The frozen Exp073CA streaming driver at commit `583c34420d5f02a1ac8e77efb9625bbc3ab73de8` emits compact files with:

- NPZ key `A`;
- shape `[39,12288]`;
- metadata field `pcl_sha256`;
- frozen complete-input status token `COMPLETE_VALID_COMPARATOR_INPUT_EXP073CA_WM_S2_COMPACT_V0_1`;
- `threads=8`, `chunk_bands=4`;
- checkpoint contract source commit equal to runtime `GITHUB_SHA`.

The corrected Exp073CF authority-tail specification at commit `80c273d89f20cd91065b18236b50060328d33ae8` consumes those exact frozen interfaces. In particular it deliberately requires the inherited Exp073CA complete-input status token rather than silently renaming it, compares replica A/B compact arrays exactly, and after the prospective correction downloads/finalizes replica-specific A and B artifacts independently.

The disabled Exp073CF workflow specification preserves `max-parallel: 1`, OMP threads `8`, the existing checkpoint streaming driver, the fresh replica-isolated checkpoint branches `checkpoints/exp073cf-wm-s2-{a,b}-v0-1`, and the <=60 s heartbeat wrapper. No acceptance threshold, scientific arithmetic, reduction order or comparator tolerance changes were introduced.

## Memory/copy audit continuation

No new full-size copy used solely for SHA verification was found beyond the already-corrected PCL helper. The streaming driver's `canon(...).tobytes()` hashes act only on the 12288-element PCL or 39x12288 compact matrix, not on the ~1.125 GiB ALM spill, so they are not a recurrence of the full-scale ALM verification-copy defect. Full-scale `NmtField`/SHT workspace and final mmap residency remain empirically uncertified under the 6 GiB WSL cap.

## Binding

Audit binding commit: `c379f7cc8ce2be2aef82f7ce9f6532c11c65a911`.

## Next gate

Exp073CF remains non-executable. The next scientifically permitted gate is still a home memory/infrastructure preflight followed, only after explicit user re-enable, by a separate prospective activation binding that pins the actual active `.github/workflows` commit, corrected authority-tail commit `80c273d89f20cd91065b18236b50060328d33ae8`, and isolated trigger activation commit. The seeded trigger must not itself be interpreted as authorization.

Article-3 readiness remains **Verified 52.0% | Draft/data 53.7%**.
