# Exp073BU v0.1 frozen-input staging closure — PASS

Date: 2026-09-04
Scope: DSIR only. RTK/RQIR excluded.
Accounting: `+0/+0`; this is an input/provenance closure gate only and creates no Wm_S3 scientific authority.

## Why this gate was needed

Exp073BU preregistration requires each replica to acquire and exact-hash-verify the immutable Exp073R1 S3 pixel-record authority and the public DES Y1 redMaGiC lens mask before any fresh NaMaster/PCL construction. A prior connectivity/source scan did not establish an on-head staging locator, so numerical Exp073BU remained fail-closed.

Repository history and validated Actions provenance supply a non-search staging route without importing any historical Wm_S3 numerical window:

- S3 source bytes: bound Exp073R1 run `33270843577`, artifact `9720335366`, digest `sha256:ff87d8fc7d53b16b786a4eb3d6ffeb103676efb8a548223a187b9f59689f8abd`;
- historical first-party lens route: Exp073S0 run `33086762750`, job `98568401949`, head `82c5804b1fcbbdc100f09a9878643ddc51975d8e`, which fetched `https://desdr-server.ncsa.illinois.edu/despublic/y1a1_files/redmagic/DES_Y1A1_3x2pt_redMaGiC_MASK_HPIX4096RING.fits` and recorded exact bytes/hash matching the Exp073BU preregistration.

## Prospectively executed closure

Workflow: `.github/workflows/exp073bu-input-staging-closure-v0-1.yml`
Implementation/trigger commit: `00b8a2c25ec4e50ae1027a1a2141a0023a033ab9`
Run/job: `33815944381` / `100848002128`
Conclusion: workflow SUCCESS, followed by raw-receipt inspection.

The hosted job downloaded the exact bound R1 artifact via `actions/download-artifact@v4` using run ID `33270843577`. GitHub independently reported downloaded artifact SHA256 `ff87d8fc7d53b16b786a4eb3d6ffeb103676efb8a548223a187b9f59689f8abd`.

It then verified:

- S3 selected rows: `4,196,641`;
- S3 pixel-record bytes: `16,786,564`;
- S3 pixel-record SHA256: `3996f2bacf29d46278773530058d4f5666c0d590bf6cebc06459659166bc60ec`;
- S3 occupancy bytes: `25,165,824`;
- S3 occupancy SHA256: `21e3776111de305c108463b02b0e3fd5e138cc97817d37e7b05330132d058094`.

The same hosted job then downloaded the exact first-party DES redMaGiC file from the repository-frozen Exp073S0 URL and verified:

- lens bytes: `104,595,840`;
- lens SHA256: `a519b8522f899e4c33267bb0749f9734f8b7fa760d195636456d370f809a3d55`.

Raw terminal token:

`PASS_EXP073BU_FROZEN_INPUT_STAGING_CLOSURE_V0_1`

Closure artifact: `9916526843`
Closure artifact digest: `sha256:74307daaf5e7cece0ce2be2fa68edef8bc63c2e7f2439f20375ccac3dde97b69`

## Classification

**PASS — frozen input staging closure, `+0/+0`, no scientific authority delta.**

This removes the external-input locator block for Exp073BU without browser/search-engine discovery and without importing any Exp073CR/CQ/CM numerical Wm_S3 output. It does not authorize a self-hosted numerical run by itself.

## Exact next permitted gate

Implement the fresh replica-local mask/PCL path so A and B each independently:

1. download the same bound R1 artifact and verify artifact/content hashes;
2. reconstruct the dense S3 count map from the exact little-endian uint32 pixel records;
3. download/hash-verify the same first-party lens mask and apply frozen `mask>0.5` weighted semantics;
4. construct fresh NaMaster/PyMaster 2.7 fields/workspace/PCL without reading historical Wm_S3 numerical arrays;
5. create a complete-stage durable PCL checkpoint inside the replica's isolated namespace;
6. continue through the validated exact 8-core shard/checkpoint architecture.

Before home execution the implementation still requires hosted machine-checkable static audit, frozen implementation fingerprint/source head, explicit activation, zero competing home-run reconciliation, and `docs/CURRENT_PROCESS.md` ownership binding.
