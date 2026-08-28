# DSIR checkpoint — Exp073R1 v0.6 long-run execution recovery

Date: 2026-08-29 (Europe/Moscow)

## Scientific state

Exp073R1 remains **reproduction/infrastructure INCOMPLETE**, not scientific FAIL. The canonical v0.5 hosted execution run `33175886694` was terminated at the 360-minute GitHub-hosted job boundary after reaching 54,525,952 / 136,930,995 metacal rows. No frozen acceptance criterion is changed here.

## Execution-only recovery

Added `.github/workflows/exp073r1-desy1-selfhosted-longrun-v0-6.yml` in commit `16f11bdeaca61da713a54ea99043dd2a6cec00f5` and dispatched the canonical long-run recovery path.

The v0.6 workflow deliberately reuses `ci/exp073r1_sequential_wholestream_v0_5.py` unchanged and preserves the exact v0.5 scientific/identity assertions:

- source whole-object SHA256 `491f623d9370d3e5657db67d410e7cfd0e89475827046e6cd82ef6b3dd88c7a5`;
- metacal whole-object SHA256 `39a7fe03e54d96b85cee2fb523ea108c2a548ba1584368203f0464ed6241ebc8`;
- 136,930,995 source rows and 136,930,995 metacal rows;
- no HTTP Range requests and identity encoding;
- immutable Exp073R0 run `33103083736` parent binding;
- unchanged selection `zbin_mcal == t AND dec >= -90 AND dec <= -35 AND flags_select == 0`;
- unchanged HEALPix mapper `nside=4096`, RING, celestial lon/lat;
- final status must be exactly `PASS_DESY1_FULL_ONEPASS_WEAK_LENSING_MASK_EXP073R1`;
- no science-gate scoring, no `f_invalid`, no covariance read and no G8 read before R1 PASS.

Only the execution resource changes: the metacal mapper is moved to `[self-hosted, Linux, X64]` with a 1440-minute job allowance. This is an infrastructure recovery, not a modified experiment.

## Runs

- Authority candidate: run `33212040452` from commit `16f11bdeaca61da713a54ea99043dd2a6cec00f5`. At checkpoint time its hosted Stage-A source-index is in progress.
- A second trigger commit accidentally produced duplicate run `33212050260`. It is **non-authoritative**. A dedicated actions-write cancellation workflow was added in commit `a4e4181a4fe8a3f09df0d27e197584309f6c5ca4` to cancel that duplicate before any self-hosted heavy mapping is admitted.

Do not merge artifacts from the two runs. Only a single terminal authority run may satisfy R1.

## Gate order remains frozen

`validated physical forward/power-input bridges -> genuine Exp073R1 PASS -> preregistered Exp073P physical support-validity mask -> covariance restriction/whitening -> nuisance tangent rank/SVD -> quotient/relation/null control -> fresh G8 withheld family`.

Until genuine R1 PASS, downstream G7 steps remain CLOSED.
