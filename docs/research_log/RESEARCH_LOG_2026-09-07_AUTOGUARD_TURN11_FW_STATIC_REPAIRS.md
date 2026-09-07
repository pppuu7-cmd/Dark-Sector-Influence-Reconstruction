# DSIR research log — Exp073FW static repair chain

Date: 2026-09-07. DSIR only.

After Exp073FV admitted `WW_S1_S3`, chained Exp073FW attempt `34120059297` failed pre-science on an impossible outer-shell S2->S2 literal check. The frozen driver identities were valid; repair `2bc804f641568a2517f903c0417a351889213219` moved those checks to the driver.

Relaunch `34120560190` failed in hosted audit only because `$GITHUB_WORKSPACE` was expanded inside a grep pattern; home skipped. Quoting fixed in `4b61f3250964333072c27478d3c167efc238db17`.

Relaunch `34120852574` passed hosted audit but home `101738329773` stopped before numerical science on a tolerance-scanner self-match caused by forbidden spellings inside the driver wrapper's own fail-closed scanner. Repair `e10279e39398ecd7912a93eabe25ad9031dd6130`, wrapper blob `84bbfada3dadd405196c6986ccc012333108f6a9`, limits that outer scan to the generated shell while retaining direct frozen-driver identity checks.

Current run `34121012410`, head `656dc15eb1999f3935b5b2dc3e6db74dda3cfe38`: hosted audit `101738782234` SUCCESS; home job `101738820469` IN_PROGRESS on `DSIR-HOME-PC-2`. No competing heavy run launched. All prior FW failures are implementation/static `+0/+0`; `WW_S2_S2` scientific authority remains uncreated pending candidate consumption and Exp073FX admission.
