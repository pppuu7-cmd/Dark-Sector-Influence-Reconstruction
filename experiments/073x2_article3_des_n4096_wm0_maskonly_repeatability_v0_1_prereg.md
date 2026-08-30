# Exp073X2 — exact DES nside=4096 Wm0 mask-only angular repeatability repair v0.1

Status at preregistration: PROSPECTIVE / NON-CLASSIFYING / INFRASTRUCTURE-REPAIR.

## Motivation

Exp073X attempted two exact NaMaster workspaces sequentially inside one 180-minute job and persisted the authority only after both completed. The hosted run was cancelled without a reusable final artifact. This is recorded as INCOMPLETE / infrastructure-resource evidence, not scientific PASS or FAIL. No Exp073X numerical output is reusable as authority.

Exp073X2 changes only persistence/repeatability execution topology. It does not change the scientific/angular operator contract.

## Frozen operator contract

- DES Y1 real masks only; no synthetic angular mask may satisfy this gate.
- NaMaster/PyMaster 2.7 lineage.
- HEALPix `NSIDE=4096`, RING ordering, coordinate contract inherited from hosted Exp073R1.
- Source mask authority: Exp073R1 source bin 0, hosted artifact digest `sha256:ff87d8fc7d53b16b786a4eb3d6ffeb103676efb8a548223a187b9f59689f8abd`.
- Source selected rows: 7,705,486; unique occupied pixels: 4,305,774; occupancy SHA-256 `b6ed74f31540d4041267f94e2f7cdb70b7040d943ba22a4aa7eab62418f8cb32`.
- DES Y1 redMaGiC lens-mask file: 104,595,840 bytes; SHA-256 `a519b8522f899e4c33267bb0749f9734f8b7fa760d195636456d370f809a3d55`.
- Lens threshold remains exactly `m <= 0.5 -> 0`, as frozen in Exp073X.
- Bandpower edges remain exactly `[0,30,60,90,120,150,180,210,240,272,309,351,398,452,513,582,661,750,852,967,1098,1247,1416,1608,1826,2073,2354,2673,3035,3446,3914,4444,5047,5731,6508,7390,8392,9529,10821,12288]`, giving 39 bands.
- Spin coupling remains spin-0 × spin-2; selected response is output TE from input TE (`TE <- TE`).
- Exact ell axis remains 0..12287 (12,288 samples).

## Frozen execution topology

Two independent hosted jobs, replica A and replica B, must each:

1. independently download and verify the same immutable Exp073R1 authority;
2. independently download and hash-bind the same public DES Y1 lens mask;
3. independently reconstruct both dense masks;
4. compute exactly one NaMaster workspace under the frozen contract;
5. immediately persist JSON + NPZ containing the canonical `<f8`, C-order TE-window authority and its SHA-256;
6. preserve all non-classifying firewall flags.

The replicas must not exchange arrays, workspace files, hashes, or derived outputs before they have separately persisted their artifacts.

A third lightweight aggregator job may run only after both replica jobs complete successfully. It must download both hosted artifacts and require:

- identical frozen metadata and authority inputs;
- TE shape `[39,12288]` in each replica;
- identical canonical SHA-256;
- `numpy.array_equal` between the two stored TE arrays;
- all anti-leakage/non-classifying flags false;
- G7/G8/G9 still OPEN;
- Article 3 scientific readiness still exactly 52%.

Only the aggregator may issue `PASS_EXP073X2_DES_N4096_WM0_MASK_ONLY_REPEATABILITY_V0_1`. Any replica failure, cancellation, missing artifact, metadata mismatch, hash mismatch, or array mismatch leaves Exp073X2 INCOMPLETE/FAIL as appropriate and cannot be converted into scientific evidence.

## Anti-leakage firewall

During X2 no direct signal catalog, physical-support classification, retained-coordinate evaluation, fiducial-P weighting, covariance, nuisance geometry, relation-null information, or G8 information may be read or scored. X2 is angular-operator authority only.

## Readiness and gates

- Article 3 scientific readiness before X2: 52%.
- X2 infrastructure/repeatability PASS alone MUST NOT increase readiness.
- G7 = OPEN, G8 = OPEN, G9 = OPEN throughout X2.
- Real Layer A remains forbidden until the full finite operator authority is frozen.

## Authorized successor

After hosted X2 aggregator PASS, expand the same exact mask-only construction to Wm source bins 1..3 and all ten WW source-mask pairs, bind them to the already frozen exact radial/mapping authorities, and only then construct/freeze the complete finite candidate-operator manifest before any Layer-A support score.
