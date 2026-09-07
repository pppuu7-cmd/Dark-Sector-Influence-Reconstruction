# DSIR immutable recovery — FW static-chain repairs / home active

Date: 2026-09-07. Scope: DSIR only.

`WW_S1_S3` remains admitted only by Exp073FV run `34120000242`, job `101735763144`.

Exp073FW attempt `34120059297` failed before science with impossible outer-envelope literal requirement `source_pair:S2->S2`; classification implementation `+0/+0`. Repair commit `2bc804f641568a2517f903c0417a351889213219`, wrapper blob `3c7e64e9a359ced198c2cb56b9a7c93f6c54c3d1` moved exact S2->S2 identity checks to the frozen driver.

Relaunch `34120560190` then failed in hosted audit only because the grep pattern expanded `$GITHUB_WORKSPACE`; home science was skipped. Classification static-audit implementation `+0/+0`. Workflow quoting repair commit `4b61f3250964333072c27478d3c167efc238db17`.

Relaunch `34120852574` passed hosted audit but home job `101738329773` stopped before numerical science with `fail-closed tolerance/rescue path`. Cause: the home wrapper scanned `s+d`; the driver wrapper source intentionally contains forbidden spellings only inside its own fail-closed scanner, producing a self-match. No FW checkpoint/artifact science was created. Classification implementation/static `+0/+0`.

Prospective smallest repair commit `e10279e39398ecd7912a93eabe25ad9031dd6130`, wrapper blob `84bbfada3dadd405196c6986ccc012333108f6a9`: scan only the generated shell envelope `s`; retain direct frozen-driver identity checks. The frozen driver itself still fail-closed scans its transformed science source, and the hosted audit retains frozen prereg/source identities. Science/domain/tolerances/arithmetic unchanged.

Workflow binding commit `656dc15eb1999f3935b5b2dc3e6db74dda3cfe38` launched Exp073FW run `34121012410`. Hosted audit job `101738782234` completed SUCCESS. Home job `101738820469` is IN_PROGRESS and is the sole FW heavy process. Checkpoint namespace: `~/.cache/dsir/exp073fw-ww-s2-s2-filebacked-ab-v0-1`. Expected gate is frozen WW `S2->S2`, canonical `<f8 [39,12288] EE<-EE`, exact A/B, exact file-backed proof; only Exp073FX may create authority.

The FW workflow currently retains the one-shot path-scoped push trigger. Do not edit that workflow while home job `101738820469` is active if doing so can generate a duplicate. Restore dispatch-only semantics at the next safe terminal transition.
