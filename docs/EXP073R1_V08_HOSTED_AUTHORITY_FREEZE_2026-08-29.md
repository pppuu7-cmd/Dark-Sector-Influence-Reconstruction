# Exp073R1 v0.8 GitHub-hosted implementation authority freeze

**Frozen:** 2026-08-29, before the v0.8 trigger commit and before any v0.8 execution output exists.

## Exact protected implementation

The only implementation eligible for a future authoritative v0.8 receipt is the repository state containing these exact Git blobs:

- preregistration `experiments/073r1_v0_8_github_hosted_rate_qualified_wholestream_prereg.md` — blob `eecb24cdf4012fdb95f660b0cfe21b61be774b8a`;
- transport wrapper `ci/exp073r1_hosted_wholestream_retry_v0_8.py` — blob `976ede2c62c781d08c7f77c013c25c5bf818cb03`;
- workflow `.github/workflows/exp073r1-desy1-github-hosted-wholestream-retry-v0-8.yml` — blob `27007861423964e30ca05aa60765fdb6a44a9fff`;
- unchanged frozen mapper `ci/exp073r1_sequential_wholestream_v0_5.py` — blob `46fe1271d97ddd9e2164d24e7d79cf27bfda805d`.

The frozen runtime parameters are exactly: qualification prefix `67108864` bytes, minimum active read rate `8.0 MiB/s`, socket timeout `45 s`, maximum route attempts `8` per map attempt, and maximum map attempts `3`.

## Sole automatic launch form

The next authoritative run must be produced by a direct child commit of **this authority-freeze commit** whose only changed path is:

`ci/exp073r1_v0_8_hosted_wholestream_retry.trigger`

That trigger file must contain exactly the parent authority commit in the form

`authority_commit=<parent commit SHA>`.

The workflow is required to verify at runtime that:

- `git rev-parse HEAD^` equals the `authority_commit` value in the trigger file;
- the diff `HEAD^..HEAD` contains only the trigger path above;
- this authority document exists in the parent commit.

A `workflow_dispatch` execution, a run from any later implementation revision, a trigger commit with any additional changed path, or a run that cannot prove the parent authority freeze is **not eligible** for downstream scientific authority even if its mapper output happens to say PASS.

## Frozen parent identities

Preserve without substitution:

- Stage-A source-index run `33175886694`, head `2926f1866fed4f0767ce3d1ec797f6e6ed4f4f2c`, artifact `exp073r1-v05-source-index-2926f1866fed4f0767ce3d1ec797f6e6ed4f4f2c`;
- source whole SHA256 `491f623d9370d3e5657db67d410e7cfd0e89475827046e6cd82ef6b3dd88c7a5`;
- source-index SHA256 `dbb362b10c68825e775e7398b18eb77d37fe725ce80cfd5c07faec5cb5755628`;
- Exp073R0 run `33103083736`, head `94b05d307295d5e9263646983ece9514f9fa2e88`;
- metacal bytes `84075649920` and SHA256 `39a7fe03e54d96b85cee2fb523ea108c2a548ba1584368203f0464ed6241ebc8`.

## Result taxonomy

Only a push-triggered run satisfying the authority checks and ending with both

- frozen mapper status `PASS_DESY1_FULL_ONEPASS_WEAK_LENSING_MASK_EXP073R1`, and
- wrapper status `PASS_EXP073R1_V08_HOSTED_RATE_QUALIFIED_WHOLESTREAM`

may be considered a genuine v0.8 reproduction PASS candidate.

Transport exhaustion, slow-route rejection, timeout, GitHub-hosted cancellation, or artifact-delivery failure is infrastructure `INCOMPLETE/INVALID`, never a science FAIL. Any mapper/hash/parent assertion failure is fail-closed and may not be converted into a transport retry.

## Prospective downstream migration

If and only if this exact v0.8 authority route later produces a genuine PASS, the obsolete operational dependence on the user's self-hosted v0.7 attempt-3 may be replaced by a separately recorded hosted prerequisite receipt. That future receipt must bind the actual run ID, job ID, run head, artifact ID and GitHub artifact digest after they exist; it may not alter the Article-3 physical-support thresholds or score G7/G8/G9.

Until such a genuine v0.8 PASS and receipt exist:

- Article-3 scientific readiness remains 44%;
- real physical-support scoring remains unauthorized;
- covariance/whitening remains blocked;
- G7/G8/G9 remain OPEN.