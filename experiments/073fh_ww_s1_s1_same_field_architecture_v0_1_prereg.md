# Exp073FH — WW_S1_S1 same-field architecture support v0.1 preregistration

Prepared prospectively while Exp073FG `WW_S0_S3` heavy science is unresolved. Scope: DSIR only. This experiment is **support/static only** and must not launch a self-hosted production workspace, inspect any partial Exp073FG numerical payload, score a science gate, or create `WW_S1_S1` authority.

## Frozen next target

The frozen Article-3 14-task manifest defines `WW_S1_S1` as the next unique WW workspace after `WW_S0_S3`. Its authoritative source is DES Y1 R1 source bin 1:

- selected rows `7,851,711`;
- pixel-record bytes `31,406,844`;
- pixel-record SHA256 `752f585125e413c7bd40cc5174cf7ef98e95f970022a351c5d91206f371d2241`;
- unique occupied pixels `4,339,193`;
- binary occupancy SHA256 `fed1ffdf2ef7a7ae88e42615bd08e207e039239c44fa20b7994258f147a739f1`.

Frozen R1 authority remains run/job `33270843577 / 99148916507`, artifact `9720335366`, digest `sha256:ff87d8fc7d53b16b786a4eb3d6ffeb103676efb8a548223a187b9f59689f8abd`.

## Same-field semantic boundary

`WW_S1_S1` is an auto-pair, not a cross-pair. A future production replica must reconstruct the authoritative S1 count map once, construct one spin-2 `NmtField`, and hand **the same field object** to both sides of `compute_coupling_matrix(f1,f1,b)`. Creating two distinct field objects from equal S1 arrays is forbidden for this target. The frozen generic Article-3 task runner already encodes this boundary with `if bmap is a: fb=fa`.

This differs intentionally from Exp073FG `WW_S0_S3`, which requires two independently reconstructed source maps and two distinct field objects. Code reuse across the boundary may occur only after an explicit audited transformation of this semantic difference.

## Numerical/storage semantics reserved for future science

Any later `WW_S1_S1` science candidate must retain the admitted WW architecture unless separately preregistered otherwise: NSIDE=4096; ell `0..12287`; 39 bands; NaMaster/PyMaster 2.7 lineage; serialized workspace file-backed unbinned MCM route; public `get_bandpower_windows()`; full BPW `[4,39,4,12288]`; selected `EE<-EE = wins[0,:,0,:]`, canonical `<f8 [39,12288]`; exact A/B SHA equality and `numpy.array_equal`; all finite; no tolerance/allclose/rounding/smoothing/averaging/manual-reconstruction/effective-coordinate/fiducial rescue.

A future production implementation must also inherit the Exp073FG hardened checkpoint rule: six stages per replica, exact complete-chain verification before pruning large intermediates, and terminal comparison that does not restore completed replicas. No numerical authority is created by this preregistration.

## Current audit scope

Exp073FH v0.1 may only verify on GitHub-hosted runners that:

1. the frozen 14-task manifest contains `WW_S1_S1` exactly once and after `WW_S0_S3`;
2. the frozen task runner contains the exact S1 authority constants above;
3. the task runner parses WW pairs only for `i<=j`;
4. the auto-pair route reuses the same Python `NmtField` object (`fb=fa`) while cross-pairs construct a distinct second field;
5. the selected WW component remains `wins[0,:,0,:] = EE<-EE` with `[39,12288]` output;
6. no science, radial, covariance, nuisance, relation/null, G8, or physical-support gate is scored.

Candidate PASS token: `PASS_EXP073FH_WW_S1_S1_SAME_FIELD_ARCHITECTURE_AUDIT_V0_1`, classification `SUPPORT_PLUS_0_PLUS_0`, `ww_s1_s1_authority_created=false`.

Status: `PREREGISTERED_NOT_ACTIVATED`.
