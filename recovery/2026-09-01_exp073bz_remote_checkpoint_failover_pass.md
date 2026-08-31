# DSIR recovery — Exp073BZ remote checkpoint failover PASS

**Date:** 2026-09-01  
**Scope:** DSIR only; RTK/RQIR excluded.  
**Article-3 readiness:** **Verified 52.0% | Draft/data 53.7%**.

Repository state and immutable hosted artifacts outrank chat wording. Synthetic/infrastructure/provenance/numerical/performance QA remains `+0/+0` unless a frozen ledger explicitly authorizes otherwise.

## Scientific authority preserved

- **Exp073BJ** remains terminal Track-A exact Wm_S1 authority PASS; final authority artifact `9758841785`, digest `sha256:a7d5b30e0a8ba4ce6d8437db82982f69f41c01ac6a58c6cb121d4cbbb2c4f008`.
- **Exp073AQ** remains the permanent historical hosted exact-repeatability scientific FAIL.
- **Exp073BD** remains `P3 PROVISIONAL_INCOMPLETE_NO_DOWNSTREAM_USE` and is forbidden downstream.
- No BZ result changes scientific or draft/data readiness.

## Exp073BZ — terminal remote checkpoint/failover QA PASS

Preregistration:

- `experiments/073bz_remote_checkpoint_pythonpath_successor_v0_1_prereg.md`
- commit `4b8f371be552cb248c1959ad7ed5d65bcb9e9ffe`

Frozen implementation lineage:

- checkpoint helper `ci/dsir_remote_band_checkpoint_v0_1.py` commit `0b0324afb69acb16cbea97bb924b9be48f303dde`;
- git-sync helper `ci/dsir_checkpoint_git_sync_v0_1.sh` commit `96886916b41dce7f0a40807622928c841ef5fc58`;
- failover driver `ci/exp073bx_remote_checkpoint_failover_qa_v0_1.py` commit `15809928dbeea082c0bb6921d581085a89ea6e45`.

Workflow:

- `.github/workflows/exp073bz-remote-checkpoint-pythonpath-successor-v0-1.yml`
- commit `616e797fc08122c3c79bb7d3853f652f9ac0c72d`

Trigger/head:

- `experiments/073bz_hosted_trigger_v0_1.md`
- run head `d263ae64ba4423af6380e91d52d8901c1df435b3`

Hosted run `33441962503` completed successfully.

Jobs:

- home checkpoint writer `99652059232`: success;
- hosted failover reader `99652226100`: success.

The frozen BZ-only correction was exactly the preregistered Python-path repair: the unchanged driver was executed with `PYTHONPATH="$GITHUB_WORKSPACE"`. No checkpoint algorithm, deterministic row, branch, SHA criterion, environment lineage, progress format, or interpretation changed.

### Immutable artifacts

Home receipt artifact:

- id `9776581747`;
- digest `sha256:809b24b9e1c76158ba50af9883048eff537a15a2d075cd7f7792ae59901f43e2`;
- branch `checkpoints/exp073bx-v0-1`;
- completed bands `[0,1,2]`;
- matrix SHA256 `1d42b89e8719cd75850103041edba0e8d2f038e384a711a31b6512ceaff0cb1e`;
- status `HOME_REMOTE_CHECKPOINTS_DURABLE`.

Hosted failover artifact:

- id `9776592370`;
- digest `sha256:2b5cbb49bbf0ca16679f63bd6aee8150e06cf617054b1afe8936dac10b778dd8`;
- restored the same branch and all 3/3 completed bands;
- `array_equal=true`;
- `sha_equal=true`;
- expected and restored matrix SHA256 both `1d42b89e8719cd75850103041edba0e8d2f038e384a711a31b6512ceaff0cb1e`;
- frozen inherited status `BX_Q1_REMOTE_CHECKPOINT_FAILOVER_PASS`.

The hosted logs additionally show remote restore from `checkpoints/exp073bx-v0-1`, `RESUME restored 3/3 completed bands`, followed by exact array/SHA equality and immutable artifact upload.

## Interpretation firewall

Exp073BZ is **NONCLASSIFYING infrastructure/durability QA only**. It demonstrates that bandwise state can be committed remotely from the home runner and restored on a clean hosted runner with exact bytes/SHA for the frozen deterministic QA payload. It does **not** establish Wm/WW scientific authority, physical support validity, covariance validity, nuisance-rank validity, quotient/null validity, G7 authorization, or any readiness increment.

Therefore:

- BZ = `+0 Verified / +0 Draft-data`;
- no tolerance, ULP, rounding, averaging, majority vote, or preferred-replica rescue is introduced;
- Exp073AQ remains historical FAIL unchanged;
- Exp073BJ remains authority PASS unchanged.

## Architectural consequence

The previously open durability prerequisite for a long full-scale streaming successor is now positively demonstrated at QA scale: a future full-DES run may prospectively use the frozen checkpoint/sync mechanism to persist completed bands and recover after runner loss without treating recovery as a scientific comparator or changing exact acceptance criteria.

This only removes an **execution architecture risk**. Before any scientific classification, the full-scale successor still requires its own prospective preregistration binding:

1. immutable BV source-lineage authority;
2. immutable BW exact full-vs-stream equivalence artifact and exact helper/code lineage;
3. frozen DES geometry `NSIDE=4096`, true ell `0..12287`, 39 bands;
4. frozen Wm operator semantics and selected-window canonical `<f8 [39,12288]` representation;
5. independent replicas;
6. frozen exact comparator and exact finalizer authority path;
7. explicit infrastructure-incomplete branch for timeout/cancellation/missing comparator inputs;
8. no downstream use of Exp073BD provisional Wm_S2.

## Frozen Article-3 order

Required order remains:

`validated physical forward/power-input bridges -> preregistered physical support-validity mask -> Layer A/Layer B prerequisites -> covariance restriction/whitening -> nuisance tangent rank/SVD -> quotient/relation/null control -> actual G7 authorization -> fresh G8 withheld family`.

No G8 jump.

## Exact next gate

Prospectively preregister the **full-scale checkpoint-capable streaming Track-A execution/authority successor** bound to immutable BV Q1, BW Q1 and BZ checkpoint/failover QA lineage. Its scientific comparator must remain exact-only and independent of checkpoint boundaries: checkpointing may change where execution resumes, never the arithmetic order or acceptance criteria. A complete exact mismatch must classify under the prospectively frozen repeatability branch; cancellation/timeout/incomplete before two valid comparator inputs must remain infrastructure incomplete with no scientific classification.

- ✅ Exp073BJ Track-A exact Wm_S1 authority PASS preserved.
- ✅ Exp073BZ remote checkpoint/failover exact-byte QA PASS.
- ❌ Exp073AQ permanent historical scientific FAIL preserved.
- ❌ Exp073BD remains provisional and forbidden downstream.
- ❌ Layer A/B, covariance/whitening, nuisance SVD, quotient/relation/null, G7/G8/G9 unauthorized.

**Verified: 52.0% | Draft/data: 53.7%**
