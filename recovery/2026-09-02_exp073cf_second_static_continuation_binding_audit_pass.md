# Exp073CF second static continuation binding/integration audit — PASS

Date: 2026-09-02
Classification: STATIC_INFRASTRUCTURE_INTEGRATION_AUDIT
Readiness delta: +0/+0
Scientific authority delta: none

## Coordination

Repository-wide GitHub Actions state was checked immediately before each write in this audit and remained queued=0, in_progress=0. No self-hosted job was triggered, rerun, or created.

Exp073CF attempt2 run `33548649445` remains terminal infrastructure incomplete, not scientific FAIL. Durable checkpoint authority remains exactly A 32/39 at `5c7ccddb54afe1ad286d08abc6f7372aa5a11103` and B 28/39 at `ce9189a1ccaabc62708f753897b9cab5f51cb9f4`.

## Concrete audited integration object

A non-executable successor specification was added outside `.github/workflows`:

- `ci/exp073cf_continuation_successor_v0_1.disabled.yml`
- initial commit `c8659fdf49999f8db623b0088b25b56d53efa994`
- strengthened binding assertions commit `05cbcecc57975187cb1dffcf5295876aee6bec61`

The file has no Actions trigger and explicitly states `self_hosted_authorized: false`. It is an audit object only.

## Audit findings

### R1 — exact-pinned historical restore: PASS

The successor spec binds:

- replica A branch `checkpoints/exp073cf-wm-s2-a-v0-1`, exact expected head `5c7ccddb54afe1ad286d08abc6f7372aa5a11103`, historical durable prefix bands 0..31;
- replica B branch `checkpoints/exp073cf-wm-s2-b-v0-1`, exact expected head `ce9189a1ccaabc62708f753897b9cab5f51cb9f4`, historical durable prefix bands 0..27.

Restore is specified only through `ci/dsir_checkpoint_git_sync_v0_2.sh restore ... EXPECTED_HEAD`. v0.2 rejects verified absence, wrong head, malformed/unknown remote state, and head changes during fetch. The frozen historical BandCheckpointStore then validates the historical payload contract and row SHAs; locally computed attempt2 bands beyond the two authoritative heads are not admitted.

### R2 — continuation execution path: PASS

The only resumed heavy driver in the spec is `ci/exp073cf_continuation_wm_s2_v0_1.py`. Direct workflow invocation of `ci/exp073ca_checkpoint_streaming_wm_s2_v0_1.py` is explicitly forbidden.

The wrapper executes the frozen historical driver internally, forces historical payload `GITHUB_SHA=f9cb1eec582276776ddac3b1207686b1e01d3b6a`, preserves historical `checkpoint_sync_commit=96886916b41dce7f0a40807622928c841ef5fc58` in the checkpoint fingerprint, and monkey-patches only remote checkpoint push transport to v0.2.

### R3 — arithmetic/thread/chunk/output invariants: PASS

The spec binds the frozen values:

- OMP threads = 8;
- chunk = 4 bands;
- true ell length = 12288 / lmax 12287;
- 39 bands with the exact frozen edge vector;
- signature `(0,2,0,2)`;
- canonical compact dtype `<f8`, shape `[39,12288]`, key `A`;
- complete comparator-input status `COMPLETE_VALID_COMPARATOR_INPUT_EXP073CA_WM_S2_COMPACT_V0_1`.

The wrapper itself fail-closes on historical driver constants for lmax, nbands, threads, chunk, signature and frozen helper lineage. The disabled successor spec additionally requires exact git-history assertions for the wrapper, preregistration, v0.2 transport helper, historical driver, CA range helper, BW helper, checkpoint utility, production finalizer helper and heartbeat helper before restore.

### R4 — provenance separation: PASS

Historical payload authority remains bound to attempt2 source commit `f9cb1eec...` and historical checkpoint sync field `96886916...`. Continuation provenance is separate:

- preregistration commit `36853b723b172a6038c6d3023805f08f37ffac72`;
- wrapper commit `ce818db7ae53376ba6e5f7934c24f4c5acb3c75c`;
- checkpoint transport v0.2 commit `bc468ca73a3c4e281bd2b1ee46d6f7704bb54bb1`.

No historical checkpoint fingerprint rewrite is authorized.

### R5 — heartbeat: PASS

The successor spec requires the frozen heartbeat wrapper with interval 60 s, total 39, threads 8 and checkpoint directory as the persisted-state source. The helper reports named stage, persisted completed/total, elapsed, ETA when estimable, threads, progress bar, and `intra_unit_progress=unknown`, while never reading scientific arrays.

### R6 — comparator/finalizer/no-rescue semantics: PASS

The successor spec binds comparison/finalization semantics to attempt2 workflow commit `de881f52d2639fc16400796a33514bf69ecad1f8` and requires the comparator/finalizer bodies to be copied without scientific arithmetic or acceptance changes. Compact and final authority require exact `np.array_equal` and exact SHA-256 equality. Tolerance, ULP rescue, rounding, averaging, smoothing, majority voting, or preferred-replica selection remain forbidden. Any readiness increment still requires a separate frozen-ledger update after terminal immutable evidence.

## Verdict

`PASS_EXP073CF_SECOND_STATIC_CONTINUATION_BINDING_INTEGRATION_AUDIT_V0_1`

This PASS is infrastructure/static evidence only, `+0/+0`. It does not authorize a self-hosted run and does not classify Wm_S2 repeatability.

## Exact next permitted gate

Prepare a separate prospective Exp073CF continuation successor binding around a real workflow definition. That preparation must:

1. keep the new workflow untriggered while the workflow commit and binding commit are frozen;
2. require `max-parallel=1` for A/B;
3. exact-pin A/B restore heads above;
4. invoke only the versioned continuation wrapper for resumed heavy computation;
5. bind all historical and continuation commits listed in this audit;
6. preserve the network-hardened exact DES download, PCL memory-stable path, compile/preflight, heartbeat, comparator and finalizer semantics;
7. re-check repository-wide queued/in_progress runs immediately before any eventual trigger;
8. require an explicit prospective trigger/head authorization before DSIR-HOME-PC work begins.

No self-hosted successor is authorized by this audit alone.

Article-3 readiness remains Verified 52.0% | Draft/data 53.7%.
