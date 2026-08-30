# Exp073X2 — Article 3 exact DES nside=4096 Wm source-bin-0 replica authority repair v0.1

Date: 2026-08-30
Status: PROSPECTIVE PREREGISTRATION — no Exp073X2 workspace output has been evaluated.
Article-3 scientific readiness before and after this infrastructure-repair experiment: **52%**.

## Purpose

Exp073X v0.1 attempted to construct the exact DES Y1 `nside=4096` Wm source-bin-0 NaMaster bandpower-window authority twice sequentially inside one Python process. Hosted run `33277263287`, job `99166064222`, was CANCELLED before an auditable result artifact was produced. That outcome is infrastructure-INCOMPLETE, not a scientific PASS or FAIL.

Exp073X2 repairs only the execution architecture. It preserves the complete frozen scientific/operator contract of Exp073X while moving repeatability across two independent hosted jobs. Each replica computes exactly one workspace and uploads its complete compact operator immediately. A third lightweight aggregator requires exact cross-replica equality.

## Frozen scientific/operator contract — unchanged from Exp073X

- DES Y1 classifying angular route: `NSIDE=4096`, RING ordering.
- Source mask authority: Exp073R1 exact source-bin-0 pixel-record authority from the byte-bound 84,075,649,920-byte metacal object.
- Source mask supplied to NaMaster: dense count map reconstructed exactly from the R1 little-endian `uint32` pixel record; no measured shear values are read.
- Lens mask authority: public `DES_Y1A1_3x2pt_redMaGiC_MASK_HPIX4096RING.fits`, byte count `104595840`, SHA256 `a519b8522f899e4c33267bb0749f9734f8b7fa760d195636456d370f809a3d55`; `UNSEEN -> 0`, then values `<=0.5 -> 0` exactly as in Exp073X.
- `NmtField(lens_mask, None, spin=0)` and `NmtField(source_count_mask, None, spin=2)`.
- NaMaster / pymaster 2.7 lineage.
- Band edges exactly:
  `0,30,60,90,120,150,180,210,240,272,309,351,398,452,513,582,661,750,852,967,1098,1247,1416,1608,1826,2073,2354,2673,3035,3446,3914,4444,5047,5731,6508,7390,8392,9529,10821,12288`.
- Exactly 39 bandpowers and ell axis `0..12287`.
- spin-0 x spin-2 component order `[TE, TB]`; selected authority is output `TE` <- input `TE`.
- Exact selected array shape must be `[39,12288]`, canonical little-endian float64.
- No effective ell, effective z, effective k, centroid, midpoint, fiducial-P weighting, or signal-amplitude shortcut is introduced.

## Frozen input provenance

Exp073R1 authority remains:
- run `33270843577`
- job `99148916507`
- head `ef783ca941fb9b9b5f5eae537986c56ff06e6536`
- artifact id `9720335366`
- artifact digest `sha256:ff87d8fc7d53b16b786a4eb3d6ffeb103676efb8a548223a187b9f59689f8abd`
- metacal SHA256 `39a7fe03e54d96b85cee2fb523ea108c2a548ba1584368203f0464ed6241ebc8`
- source-bin-0 selected rows `7705486`
- source-bin-0 unique pixels `4305774`
- source-bin-0 pixel-record SHA256 `5b507215ca961c09b82786e61e681a0178c29e9b593c17b588e366722a021f15`
- source-bin-0 binary occupancy SHA256 `b6ed74f31540d4041267f94e2f7cdb70b7040d943ba22a4aa7eab62418f8cb32`.

## Prospectively frozen execution repair

Two independent hosted jobs, replica `a` and replica `b`, shall each:
1. enforce this preregistration and implementation freeze;
2. install the same NaMaster 2.7 lineage;
3. download the same frozen Exp073R1 artifact;
4. download and hash-bind the same public DES lens mask;
5. reconstruct the same source-bin-0 count mask;
6. construct **one and only one** exact `NmtWorkspace` for the frozen spin-0 x spin-2 fields and binning;
7. extract `wins[0,:,0,:]` as contiguous `<f8` `[39,12288]`;
8. save the array and metadata immediately as that replica's artifact.

The replica jobs may have a larger wall-clock timeout than Exp073X. Runtime, timeout, scheduling, and parallelization are infrastructure parameters and do not enter the scientific classification.

A third aggregator job shall not construct a NaMaster workspace. It shall download both replica artifacts and require all of the following:
- both replica metadata files identify the frozen input/operator contract;
- both arrays have dtype `<f8` and shape `[39,12288]` after canonicalization;
- both canonical SHA256 values are identical;
- `numpy.array_equal(replica_a, replica_b)` is true;
- provenance-critical metadata (R1 authority, lens authority, band edges, nside, ell axis, selected component, source/lens dense-mask hashes) is identical;
- all non-classifying science-firewall fields remain false and `G7/G8/G9` remain OPEN.

Only after those checks may the aggregator emit:

`PASS_EXP073X2_DES_N4096_WM0_REPLICA_AUTHORITY_V0_1`

Any mismatch is Exp073X2 FAIL. A timeout, runner cancellation, package/network failure, unavailable artifact, or resource exhaustion before classification is infrastructure-INCOMPLETE and must not be relabelled as scientific FAIL.

## Science firewall

Exp073X2 is an angular-operator authority experiment only. It must not evaluate:
- any DES `(z,k)` physical support fraction;
- any Layer-A retain/drop decision;
- any Layer-B common-response validity;
- any covariance or inverse covariance;
- whitening/Cholesky;
- nuisance tangent geometry/SVD/rank;
- signed quotient/relation/null statistics;
- chi-square, p-values, G7/G8/G9 outputs.

Frozen gate state in all outputs: `G7=OPEN`, `G8=OPEN`, `G9=OPEN`.

## Interpretation and next authorized step

A PASS establishes only a reproducible exact Wm source-bin-0 angular-window authority. It does **not** raise Article-3 readiness above 52% and does not classify any observation row.

After PASS, expand the same exact `nside=4096` mask-only construction to the remaining three Wm source masks and all ten unordered WW source-mask pairs. The full set of 14 exact DES angular authorities must then be bound together with the frozen DES radial authority, deterministic 1170-row DES mapping, Exp073W BOSS authority, factorized evaluator, domain/threshold/firewall metadata, and synthetic factorization-equivalence QA into one immutable pre-support candidate manifest **before** any real combined Layer-A scoring. Only that complete manifest freeze can justify the next ~55–57% readiness checkpoint.
