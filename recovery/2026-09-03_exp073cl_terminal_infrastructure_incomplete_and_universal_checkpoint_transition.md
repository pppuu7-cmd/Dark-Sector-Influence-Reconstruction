# Exp073CL terminal recovery — infrastructure incomplete + universal checkpoint transition

**Date:** 2026-09-03

Repository state and immutable GitHub Actions evidence are authoritative.

## Exp073CL terminal result

Workflow run `33683175039` is terminal. Hosted authorization job `100424294898` completed `success`. Hosted DES mask staging job `100424333794` completed `success` and produced immutable artifact `9867046699`, name `exp073cl-exact-des-mask-9a7b1c19aa130c5b11f68c2d9ea73ff9a2f6c105`, digest `sha256:e795118e73f6f98f1253a5e87b2f62cc5c5182ebfcfcc572b1cfb1c3ae87c915`.

Self-hosted job `100424401979` is terminal `cancelled`. Steps through local DES-mask verification and spill-capacity preflight completed successfully. The atomic step `Build fresh real Wm_S3 PCL` was cancelled before a durable PCL output/checkpoint was produced. The compile and eight-band 1-thread-vs-8-thread benchmark steps were skipped. The final artifact upload failed because no qualifying self-hosted result payload existed.

Therefore Exp073CL is classified **INFRASTRUCTURE_INCOMPLETE_EXP073CL_V0_1**, readiness `+0/+0`. It is not a scientific or numerical repeatability FAIL. No exact 1-vs-8 comparator was reached, so no resource-plan scientific classification is permitted.

Historical Exp073CK remains infrastructure incomplete `+0/+0` and is not retried or rewritten.

## Universal self-hosted checkpoint transition

User policy effective 2026-09-03 requires durable checkpoint/resume for **every future self-hosted DSIR task**, independent of size or classification. This is now durably encoded in `docs/SELF_HOSTED_CHECKPOINT_POLICY.md` at commit `f45ae0ce4d199ae381e8612d41cfd7e4c7dfc427`.

Exp073CL is the final grandfathered exception because it was already running when the policy was introduced. It remains immutable historical evidence.

The next resource successor is prospectively preregistered as Exp073CM at commit `914a57e45ee98b6ebbb8830a524ec59bfef0c78b`. It must use dedicated remote namespace `checkpoints/exp073cm-wm-s3-resource-v0-1`, exact restore verification, and durable stage checkpoints for complete PCL, reference, target, and final classification before advancing between stages.

No future self-hosted DSIR workflow may launch without an explicit frozen checkpoint contract satisfying `docs/SELF_HOSTED_CHECKPOINT_POLICY.md`.

## Coordination and readiness

At the recovery write point, GitHub Actions reports `0` queued and `0` in-progress runs. The home runner is therefore **FREE**, but no new home-runner job is authorized until Exp073CM implementation/binding/activation are fully frozen and checkpoint semantics are audited.

Article-3 readiness remains **Verified 52.0% | Draft/data 54.6%** (exact Draft/data `54.57142857142857%`). Infrastructure/resource/checkpoint QA is `+0/+0` unless a frozen ledger explicitly authorizes otherwise.

## Exact next permitted gate

Finish prospective Exp073CM implementation under the universal checkpoint policy, perform a hosted/static fail-closed audit of its checkpoint/restore semantics, freeze workflow/binding/activation, and only then dispatch Exp073CM if coordination is still clean. A full Wm_S3 A/B scientific successor remains forbidden until Exp073CM returns `PASS_EXP073CM_WM_S3_EIGHTBAND_DIRECT8_RESOURCE_V0_1`.
