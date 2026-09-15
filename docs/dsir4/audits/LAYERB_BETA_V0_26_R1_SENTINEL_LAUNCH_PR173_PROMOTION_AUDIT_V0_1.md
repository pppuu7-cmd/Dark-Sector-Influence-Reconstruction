# DSIR V0.26 R1 PR173 inactive launch-package promotion audit V0.1

Date: 2026-09-15. Scope: DSIR only. This review is strictly a post-promotion provenance/gate audit of merge commit `7224e044b0c972456127dd969dcf212918e6f47f`; it is not a sentinel science result and does not inspect any substantive CLASS response.

## Reconstructed authority chain

The numerical/reproducibility chain remains terminal through V0.25. Consolidated V0.26 R1 remains the prospective full-107 numerical specification; PR171 supplied only a separately qualified inert sentinel implementation. Terminal launch-package audit authority `docs/dsir4/authority/LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_PR173_FUNNEL_QUALIFICATION_V0_1.json`, current git blob `ed3cec954d2077e6b5a6daab5da53e8fe72cc2e0`, verdict `QUALIFIED`, authorized exact inactive promotion of PR173 head `1403581d4d608d98597eaff2c77c80a98d6c3c6e` only after that authority was on main. It explicitly forbids active W/A/L/Q creation, sentinel science, full 107-row replay, and downstream science.

Chronology is correct. PR174 merged the qualification authority to main at `cb5fe39993c66d7ab9f952ee9527ce310073f292` at 2026-09-15T10:52:31Z. PR173 was then merged at `7224e044b0c972456127dd969dcf212918e6f47f` at 2026-09-15T10:52:57Z. The promotion merge has parents exactly `cb5fe39993c66d7ab9f952ee9527ce310073f292` and audited PR173 head `1403581d4d608d98597eaff2c77c80a98d6c3c6e`.

## Exact promotion identity

The promotion merge added exactly the seven audited inactive files, with 827 additions and zero deletions. Current main preserves every audited blob exactly:

- static package-audit workflow: `09e3a4b14bacd33e451b5f35aa4dc78004ac7945`;
- static package auditor: `8efdccffcf0e740a799fd462c3988cdc20a29b1a`;
- static package evidence record: `4bbed7fc77e57aab82a72bf886c697cf6f07c1a6`;
- launch-authority candidate A: `4ba40e59e6a9d48636d95d07efab575e56ae0966`;
- launch-package contract: `26806597e651fb22956de59f102c0ad24d11c576`;
- launch-descriptor candidate L: `9c217e41764d979bea12644fae372354241bc976`;
- active-workflow candidate W: `19907175f0f3417ddee2aba6916d961c6be02e26`.

No audited candidate blob was mutated during promotion.

## Activation-leak negative controls

Current main still lacks all four active/final paths:

- `.github/workflows/layerb-beta-v026-r1-sentinel-science-v0-1.yml`;
- `docs/dsir4/authority/LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_AUTHORITY_V0_1.json`;
- `docs/dsir4/launch/LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_V0_1.json`;
- `docs/dsir4/authority/LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_PACKAGE_QUALIFICATION_V0_1.json`.

Therefore the merge did not stage or trigger sentinel science. GitHub Actions reports zero workflow runs for exact current promotion head `7224e044b0c972456127dd969dcf212918e6f47f`. This is consistent with an inactive promotion, not evidence of a missed science result.

## Hosted evidence revalidation

The frozen response-blind package static audit is run `34959657394`, run #1 / attempt #1 / push, head `5d42cd84ce54c9781d7bbefd41b01d3cf775fbd7`, terminal success. Its sole job `104349972403` is terminal success. Artifact `10393170033` reports GitHub digest `sha256:e95c4675db77a2ecd864d21e39dfdccffe289ed61a84ece95182f22c46e16184`.

The artifact was independently downloaded during this review. ZIP SHA256 independently equals `e95c4675db77a2ecd864d21e39dfdccffe289ed61a84ece95182f22c46e16184`. It contains exactly five members. `launch_package_static_audit.json` is 1,348 bytes and SHA256 `133df1d2753c9228198a15be792fdcbbf99da243efeccdb785d610aad7dc5ee5`. The exact-copy members independently hash as W git blob `19907175f0f3417ddee2aba6916d961c6be02e26`, A git blob `4ba40e59e6a9d48636d95d07efab575e56ae0966`, and L git blob `9c217e41764d979bea12644fae372354241bc976`. The receipt records no CLASS solve, no scientific-response read, no active W/A/L/Q, and no full-107 authorization.

The external funnel audit is run `34960031527`, run #1 / attempt #1 / push, head `9d39949b0531aa91f229dea18372d79d6c6b6e00`, terminal success. Its sole job `104351158807` is terminal success. Artifact `10392992058` reports GitHub digest `sha256:73ea7849b60dd65b20e2f93144c7afbb0f7dc7bd09ae8e0e9cfe0e3d63801c59`.

That artifact was independently downloaded during this review. ZIP SHA256 independently equals `73ea7849b60dd65b20e2f93144c7afbb0f7dc7bd09ae8e0e9cfe0e3d63801c59`. `funnel_audit.json` is 1,728 bytes and SHA256 `f525feaf938e99a9282ea97619842ded9883ac54219e60c9bbdd3f34f934a1aa`; its verdict is `QUALIFIED`, classification `SENTINEL_ACYCLIC_LAUNCH_PACKAGE_QUALIFIED_FOR_INACTIVE_PROMOTION_AND_Q_CONSTRUCTION`, and it records no candidate workflow execution, CLASS solve, or scientific-response read.

## Counterexample search and qualification checks

I explicitly tested the plausible failure modes relevant to this scope: promotion before authority, promotion from a different PR head, mutation of any audited W/A/L/package/static blob, accidental creation of active workflow/authority/descriptor/Q paths, accidental sentinel Actions execution at the promotion head, and hidden substantive-value contamination. None is present.

Interpolation, sampling, solver tolerance, resolution, execution-order dependence, nuisance structure, covariance, look-elsewhere effects, and physical/systematic alternatives cannot be adjudicated by this promotion because no sentinel scientific response exists. Treating the green static/audit runs as evidence for any such scientific claim would exceed the interpretation ceiling.

One governance inconsistency was found outside the promoted object: `docs/RECOVERY_LATEST.md` and `docs/CURRENT_PROCESS.md` still described PR171 as open and the launch package as not yet frozen/audited. This is stale recovery state, not a defect in the exact promotion. It must be reconciled before further funnel work so a clean session does not repeat or skip the launch-package gate.

## Verdict

`CONFIRMED_SCOPED`.

Confirmed scope only: exact inactive promotion of the already independently qualified PR173 W/A/L package and static evidence. This verdict does not upgrade the candidate A/L internal `sentinel_science_execution_authorized=true` fields into current repository authorization because those objects remain under candidate paths and the governing terminal authority explicitly requires a separately constructed and audited Q plus later staged active paths.

Scientific effect remains `+0/+0`; repository readiness remains `68%`; scientific frontier remains `67%`.

## Authorized next stage

The next admissible action is only to construct a package qualification Q that binds exact W/A/L plus the frozen static-package and external-funnel evidence, keep full-107 authorization false, and submit Q to a separate response-blind static audit before Q promotion. Do not stage active W/A yet; do not create final L; do not run sentinel science; do not run full 107 rows. Covariance, whitening, nuisance, relation-null, `Wm_S3`, global 65537, statistical/model inference, and physical dark-sector inference remain closed.
