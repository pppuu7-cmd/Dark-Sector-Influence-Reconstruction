# Exp073BU self-hosted connectivity result — 2026-09-04

Status: **PASS (infrastructure only; no scientific authority advance).**

## Binding

- workflow: `.github/workflows/exp073bu-selfhosted-connectivity-probe-v0-1.yml`
- trigger head: `20741f82249363294e835d0cf01ebbdfddc6f6e3`
- Actions run: `33813773616`
- job: `100841253278` (`probe`)
- conclusion: `success`
- raw token: `PASS_EXP073BU_SELFHOSTED_CONNECTIVITY_PROBE_V0_1`

## Proven home listener

- runner name: `DSIR-HOME-PC`
- runner group: `Default`
- machine: `win-ws338`
- runner version: `2.337.0`
- runner OS/arch: `Linux` / `X64`
- kernel: WSL2 Linux on `win-ws338`
- online CPUs observed by probe: `8`
- RAM observed: 5.8 GiB total, about 5.1 GiB available during probe
- swap observed: 16 GiB total, 0 used during probe
- root filesystem: about 1007 GiB total, about 948 GiB available during probe

## Label correction

The first probe run `33813694199` targeted `[self-hosted, dsir-exp073cr]` and remained queued because the proven home registration uses the standard labels inherited from successful Exp073CR: `[self-hosted, Linux, X64]`.

The corrected probe used `[self-hosted, Linux, X64]` and completed successfully.

## Scientific boundary

This probe computed no Wm_S3 numerical data and creates no scientific authority. Exp073BU still requires its frozen hosted static implementation audit, fingerprint/activation, queue exclusivity check, and fresh-independent A/B computation under the preregistered contract.

The stale first queued probe must be cancelled or otherwise terminal before Exp073BU scientific activation because the preregistration requires no competing queued/in-progress DSIR home workload.
