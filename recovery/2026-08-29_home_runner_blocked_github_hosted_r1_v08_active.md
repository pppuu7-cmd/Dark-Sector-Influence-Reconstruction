# DSIR recovery checkpoint — home runner blocked, GitHub-hosted Exp073R1 v0.8 active

Date: 2026-08-29

## Operational change

The user's home/self-hosted runner must no longer be treated as an available route for internet-dependent DSIR computation while the user's network issue is under technical-support investigation.

This is an infrastructure constraint only. It is **not** a negative scientific result and does not alter any frozen DSIR/Article-3 criterion.

The self-hosted Exp073R1 v0.7 attempt-3 lineage remains preserved for provenance but is now classified operationally as `BLOCKED_HOME_INTERNET_DEPENDENCY`; do not request that the user start `./run.sh`, and do not make Article-3 progress depend on that runner.

## Evidence that GitHub-hosted whole-stream transport is feasible

Historical GitHub-hosted run `33081571259`, job `98549908881`, streamed the complete metacal object:

- bytes `84075649920`;
- SHA256 `39a7fe03e54d96b85cee2fb523ea108c2a548ba1584368203f0464ed6241ebc8`;
- full stream approximately 14:19:18 -> 14:28:27 UTC on 2026-08-27;
- result `PASS_FULL_OBJECT_STREAMING_SHA256_BINDING`.

By contrast, old GitHub-hosted range transport was unreliable: run `33170454493` failed even a `40239104`-byte strict range with repeated 0-byte timeouts. Therefore the current route deliberately returns to whole-object GETs and rejects slow connections before expensive mapping.

## New prospective route frozen before execution

Preregistration:

`experiments/073r1_v0_8_github_hosted_rate_qualified_wholestream_prereg.md`

Protected implementation:

- frozen v0.5 mapper blob `46fe1271d97ddd9e2164d24e7d79cf27bfda805d`;
- v0.8 wrapper blob `976ede2c62c781d08c7f77c013c25c5bf818cb03`;
- v0.8 workflow blob `27007861423964e30ca05aa60765fdb6a44a9fff`;
- v0.8 prereg blob `eecb24cdf4012fdb95f660b0cfe21b61be774b8a`.

Authority freeze:

`docs/EXP073R1_V08_HOSTED_AUTHORITY_FREEZE_2026-08-29.md`

Authority-freeze commit: `9c950247799ff09a9df62e39aa508588125da031`.

Trigger-only child commit: `ef783ca941fb9b9b5f5eae537986c56ff06e6536`.

## Active run

- workflow run: `33270843577`;
- workflow: `Exp073R1 DESY1 GitHub-hosted rate-qualified whole-stream retry v0.8`;
- event: `push`;
- head: `ef783ca941fb9b9b5f5eae537986c56ff06e6536`;
- job: `99148916507` (`hosted-wholestream-retry`);
- runner class: GitHub-hosted `ubuntu-24.04`;
- latest observed state at this checkpoint: `in_progress`.

Already observed PASS steps:

1. checkout;
2. frozen evaluator / preregistration firewall;
3. trigger-parent authority binding;
4. pinned runtime installation;
5. immutable Stage-A / Exp073R0 metadata binding.

At checkpoint creation the workflow was downloading the frozen parent artifacts and had not yet entered the 84-GB mapper stream.

## Frozen transport mechanics

- whole-object GET only;
- zero Range requests;
- every connection begins at byte 0;
- qualification prefix `64 MiB`;
- minimum active network throughput `8 MiB/s`;
- socket timeout `45 s`;
- up to 8 route candidates per map attempt;
- up to 3 clean map attempts;
- rejected/failed attempts discard all partial record/mask products;
- only transport exceptions retry;
- mapper/hash/parent assertion failures remain fail-closed.

The qualifying prefix is replayed byte-for-byte into the unchanged v0.5 mapper, so the mapper still sees the exact object from byte zero.

## Article-3 state

Strict scientific readiness remains **44%**.

A v0.8 PASS may increase readiness only after its terminal artifact is independently bound into a new hosted prerequisite receipt. v0.8 by itself does not score physical support, does not authorize covariance, and does not close G7.

Current gate state:

- G7 OPEN;
- G8 OPEN;
- G9 OPEN;
- real Article-3 physical support BLOCKED pending genuine reproduction authority;
- covariance/whitening BLOCKED.