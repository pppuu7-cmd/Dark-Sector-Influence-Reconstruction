# Exp073GA GitHub transport preflight audit v0.1

Status: PREPARED_NOT_DISPATCHED

This audit is deliberately prepared on an isolated branch while the expensive Exp073FY WW_S2_S3 run is active. It does not modify, cancel, restart, or share the self-hosted runner with FY.

## Frozen successor

- workflow: `.github/workflows/exp073ga-ww-s3-s3-home-science-v0-1.yml`
- target: `WW_S3_S3`
- ordered sources: `[3,3]`
- transform: `S3S3`
- scientific predecessor: the successful FY run containing the FZ provenance-admission tokens
- GA remains `workflow_dispatch` only and MUST NOT be dispatched before FZ admission succeeds.

## Transport finding

The earlier self-hosted `gh` failure mode is already removed from the expensive launcher path.

1. The GA `hosted-launch-audit` runs on `ubuntu-latest` and performs its `gh api` predecessor checks before the `home-science` job can start. Therefore failure of `gh` on the hosted runner is fail-closed before any expensive GA computation.
2. The GA home wrapper verifies the exact frozen base launcher blob `309c464bbfbe4896bd560165985ee7f643d9ee22` and transforms/executes that launcher.
3. The frozen base launcher uses authenticated `curl`/GitHub REST calls for live-run exclusivity and artifact restoration before `run_replica A` or `run_replica B`; the self-hosted path does not require `gh` for those operations.
4. No package installation or `gh` installation should be attempted on the self-hosted runner while FY is active.

## Fail-closed preflight contract for GA

Before GA consumes the home runner, require all of the following:

- hosted launch audit succeeds;
- predecessor run is completed/successful and contains `PASS_EXP073FZ_WW_S2_S3_FILEBACKED_PROVENANCE_ADMISSION_V0_1`;
- predecessor log contains `ww_s2_s3_authority_created=true`;
- GA frozen file/blob checks succeed;
- GA home wrapper still pins base launcher blob `309c464bbfbe4896bd560165985ee7f643d9ee22`;
- base launcher still performs authenticated GitHub REST access with `curl` before entering expensive replica computation;
- no competing self-hosted DSIR run is queued/in-progress.

If any item fails, GA must remain blocked and no heavy rerun is authorized.

## Operational decision

No scientific code patch is justified by this audit. The safest preparation is to preserve the already-frozen GA science path and treat the existing hosted-before-home `gh` check plus self-hosted `curl` REST path as the transport preflight. This avoids changing frozen numerical code while FY is running.
