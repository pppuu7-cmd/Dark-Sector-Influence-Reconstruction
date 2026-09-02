# DSIR recovery — Exp073CL abandoned and universal self-hosted checkpoint transition

**Date:** 2026-09-03

## Exp073CL terminal classification

Run `33683175039` completed with overall conclusion `cancelled`. Hosted `authorize` and hosted DES-mask staging succeeded. Self-hosted job `100424401979` was abandoned/cancelled after the runner reported a TLS/SSL connection failure to GitHub. The active stage was `Build fresh real Wm_S3 PCL`; the range-helper compile and eight-band 1-thread/8-thread benchmark were skipped. The final self-hosted artifact upload failed, and the only durable run artifact is the already-completed hosted DES mask artifact.

Therefore Exp073CL is classified **INFRASTRUCTURE_INCOMPLETE_EXP073CL_V0_1**, `+0/+0`, not a scientific/numerical model FAIL. No Wm_S3 angular authority is created by Exp073CL.

## Universal self-hosted checkpoint rule

At the user's explicit instruction, every future task executed on the home/self-hosted runner must have durable checkpoint/resume semantics regardless of perceived task weight or category. This is frozen in `docs/SELF_HOSTED_CHECKPOINT_POLICY.md`, commit `f45ae0ce4d199ae381e8612d41cfd7e4c7dfc427`.

A task without a safe prospective checkpoint contract must not be launched on the home runner. Atomic stages may repeat only themselves if interrupted; all previously completed safe stages must survive via exact remote checkpoint state.

## Exp073CM successor

Exp073CM prospectively repeats the unfinished Exp073CL resource question without changing the science/numerics, but checkpointing stages `pcl -> reference -> target -> final` under dedicated branch `checkpoints/exp073cm-wm-s3-resource-v0-1`.

Frozen chain before launch:

- policy commit `f45ae0ce4d199ae381e8612d41cfd7e4c7dfc427`;
- prereg commit `914a57e45ee98b6ebbb8830a524ec59bfef0c78b`;
- PCL helper commit `8a5f9f5e0341d24ee843f3097199075c50ab2d02`;
- checkpoint/resource driver commit `e48737a0f616ed4fa05e4c45cf05d06b05ad6c6f`;
- workflow commit `8572cc233659815fadf8ea96f33af1417dd9d239`;
- binding commit `96eb1fdd7fcb7226248860dee2a0a475ff211710`;
- activation commit `b4cdb3b4eb1306c5f273eb33b29564467f3844ed`;
- checkpoint transport commit `bc468ca73a3c4e281bd2b1ee46d6f7704bb54bb1`;
- range helper commit `fa971eb4ef8c47e81eb0bb4e13eeb76f7cf42e22`.

Exp073CM still scores `+0/+0`; only later frozen ledger admission can alter Article-3 readiness.
