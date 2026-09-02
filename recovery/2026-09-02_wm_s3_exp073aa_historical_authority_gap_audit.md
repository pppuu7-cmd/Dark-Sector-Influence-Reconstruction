# DSIR recovery — Wm_S3 / Exp073AA historical authority-gap audit

**Date:** 2026-09-02  
**Classification:** provenance/governance audit, `+0/+0`  
**Article-3 readiness:** Verified **52.0%** | Draft/data **54.6%** (unchanged)

## Question

Before any new Wm_S3 computation, determine whether a valid historical Wm_S3 angular authority already materialized through the frozen Exp073AA production route or a later prospective successor.

## Frozen Exp073AA route

Exp073AA was prospectively preregistered at commit `14b79794ab5dc1b8cc8a0fa769ab50cac99f45d9`. Its generic executor was implemented at commit `45ed8d8d1e90cdaf314e0384b6f3cdfef369925b` and explicitly recognizes all 14 angular identities, including `Wm_S3`. The production matrix was to compute the 13 identities excluding `Wm_S0` only after the upstream release condition was satisfied.

Exp073AF release control was prospectively preregistered at commit `91e9f3f25fa34cab3a33d927d47afa10e5f1cc29`. It froze the only authorized transition from Exp073X2 P/Q outcomes to `RELEASE_13_EXP073AA_TASKS` or `BLOCK_PRODUCTION`.

Frozen X2 inputs to that controller:

- P run `33300997298`, head `2403d9680e1d08a3853084034eb2878faa52b4e0`;
- Q run `33301058260`, head `730ae4951ab8cd8e1dd2c392e991c3120345678a`.

## Immutable run audit

### P — infrastructure incomplete

P replica jobs `99229007616` (A) and `99229007666` (B) completed successfully and uploaded immutable artifacts:

- A artifact `9730411514`, digest `sha256:34530157cddf594c93728d5e092ab937d16a653665623f00513f4fd58df17555`;
- B artifact `9730409129`, digest `sha256:36358663fb1980ad75cb71f7ca7149d06d357cf7de8b29feca4273f4f88c89e5`.

However aggregate job `99242068393` failed before scientific comparison because `ci/exp073x2_compare_replicas_v0_1.py` could not import NumPy (`ModuleNotFoundError: No module named 'numpy'`). Therefore P is **INFRASTRUCTURE_INCOMPLETE**, not a scientific FAIL and not a PASS.

### Q — scientific exact-repeatability failure

Q replica jobs `99229177604` (A) and `99229177540` (B) completed successfully and uploaded immutable artifacts:

- A artifact `9730452251`, digest `sha256:6fab306a14d76b6819820454eb2d56035c2ce74b126d2ac1a70eb94cbb5dac27`;
- B artifact `9730346824`, digest `sha256:a969aa3d04b2d2278d16e84e14ec2fbc046fc79c5bd1c63615e01c783592ce95`.

Aggregate job `99242395532` installed the lightweight NumPy dependency and performed the exact authority comparison. It terminated on:

`cross-replica authority mismatch {'canonical_hash': False, 'array_equal': False, 'contract': True, 'pymaster_version': True, 'r1_authority': True, 'source_mask': True, 'lens_mask': True, 'workspace_metadata': False, 'gate_state': True, 'readiness_52': True}`

Thus Q is **SCIENTIFIC_REPEATABILITY_FAIL** under the frozen exact criterion. No tolerance or rescue is permitted.

## Exp073AF decision

The realized pair is therefore:

- P = `INFRASTRUCTURE_INCOMPLETE`;
- Q = `SCIENTIFIC_REPEATABILITY_FAIL`.

Exp073AF frozen rule 10 maps this pair to **`BLOCK_PRODUCTION`**. Consequently the original 13-task Exp073AA production matrix, including `Wm_S3`, was never authorized by this route.

## Later-authority audit

Read-only searches of the current default branch and historical Actions naming/provenance found no valid later Wm_S3 run/job/artifact/digest or recovery record establishing a separate prospective Wm_S3 successor. Literal searches alone are not authority, but combined with the frozen Exp073AF block they remove the only identified historical materialization route.

Therefore, as of this audit, **no valid complete Wm_S3 angular authority is established**. This is an authority-gap finding, not a scientific result.

## Consequence

A NEW prospectively versioned Wm_S3 successor may now be prepared. It must not revive or modify Exp073AA/X2/AF historical workflows, and it must preserve the frozen angular arithmetic:

- DES `NSIDE=4096`, RING/C;
- ell `0..12287`;
- 39 frozen bands;
- Wm component `TE <- TE`;
- canonical little-endian `<f8 [39,12288]`;
- exact equality only;
- no effective-ell/z/k or fiducial-P shortcut.

Before any new self-hosted heavy Wm_S3 execution, first prospectively qualify wider concurrency with staged `4 -> 6 -> 8` exact-equivalence plus short RSS/swap safety measurements. Freeze the highest exact-equivalent memory-safe setting. At most one heavy DSIR job may own `DSIR-HOME-PC`.

No readiness change is authorized by this audit. G7/G8/G9 remain OPEN and no G8 jump is permitted.
