# DSIR recovery — Exp073FY namespace-repair resume V22

Date: 2026-09-07. Scope: DSIR only. Repository state is authoritative.

## Consumed failures

Exp073FY original heavy run `34147009217` remains infrastructure/implementation FAIL `+0/+0`, not scientific FAIL. Replica A completed through `replica_receipt_complete` with correct ordered `S2->S3`, `[2,3]` science payload but invalid checkpoint namespace `checkpoints/exp073fy-ww-s3-s3-a-v0-1`. FZ admission was never reached.

Checkpoint-first recovery run `34157571794` failed at the FY pruner with `fail-closed stage identity fresh_sources_complete`, correctly exposing the namespace cascade rather than weakening identity checks.

First namespace-repair workflow run `34160466102`, head `4b23fd691dd0e4c644c0f59762f8e41abeacfe52`, also ended infrastructure FAIL `+0/+0` before heavy computation. Hosted launch audit succeeded, but home job `101861088550` stopped in its first service step because the self-hosted runner does not provide GitHub CLI: `/...sh: line 2: gh: command not found`. No scientific calculation occurred in that attempt.

## Prospective repairs

Driver repair commit `f899b93f966e617ad1ff46b5abba6f928d4ad389`, blob `65161f78f7c993df571be3ea871de03c54f6847a`, protects already-correct `checkpoints/exp073fy-ww-s2-s3-{a,b}-v0-1` namespace strings before the generic source-symbol `s2 -> s3` transform. Static fail-closed regression requires the exact S2-S3 namespaces and forbids `exp073fy-ww-s3-s3-`. Frozen science is unchanged.

Recovery workflow V0.3 commit `b5c8a059a014bee5d318d6067f7a2fac37c5b173` removes the self-hosted `gh` dependency from the legacy-artifact metadata check and uses the already-proven authenticated `curl` GitHub API route. Hosted-only steps may continue using `gh`.

The V0.3 retirement step does not rewrite or relabel invalid manifests. It independently checks the known bad namespace, source head, contract fingerprint, replica/source order, receipt hash and selected-EE hash when present, writes retirement evidence, and moves the invalid checkpoint directory to `retired_invalid_namespace_v0_3/`. The repaired authority chain is then regenerated under the exact prospectively required S2-S3 namespace. This preserves the historical numerical evidence without importing the invalid checkpoint into scientific authority.

## Current authoritative process

Run `34160898921`, workflow path `.github/workflows/exp073fy-ww-s2-s3-namespace-repair-resume-v0-3.yml`, head `b5c8a059a014bee5d318d6067f7a2fac37c5b173`:
- hosted launch audit job `101862362835`: SUCCESS;
- home-science job `101862390771`: IN_PROGRESS at latest reconciliation;
- invalid S3-S3-labelled FY checkpoint retirement step: SUCCESS;
- repaired frozen `WW_S2_S3` A/B gate step: IN_PROGRESS;
- single self-hosted DSIR runner owns the heavy job;
- no competing DSIR home-heavy run exists.

Frozen FY science remains: ordered `S2->S3`, `[2,3]`, distinct field objects, DES NSIDE=4096, ell `0..12287`, 39 bands, canonical `<f8 [39,12288] EE<-EE`, public NaMaster 2.7 file-backed serialized-workspace route, exact 19,327,352,832-byte MCM proof, finiteness, exact SHA and `numpy.array_equal`, no tolerance/allclose/isclose/rounding/smoothing/averaging/manual-reconstruction rescue. `WW_S2_S3` remains NOT ADMITTED until Exp073FZ emits `PASS_EXP073FZ_WW_S2_S3_FILEBACKED_PROVENANCE_ADMISSION_V0_1`.

## Next actions

1. Do not duplicate run `34160898921` while home job `101862390771` is active.
2. On terminal state, inspect exact logs/artifact and classify by the frozen FY/FZ contract.
3. On successful FY candidate and FZ provenance admission, dispatch the already-frozen Exp073GA `WW_S3_S3` successor.
4. On infrastructure/software failure, preserve any newly complete valid checkpoints and repair only the first causal defect; do not weaken science or blindly restart completed expensive stages.
