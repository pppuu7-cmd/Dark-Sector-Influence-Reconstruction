# Exp073R1 v0.5 — Stage A source whole-stream PASS

**Date:** 2026-08-28

## Terminal result

Exp073R1 v0.5 run `33175886694`, job `98864259826` completed Stage A successfully.

Terminal status:

`PASS_EXP073R1_V05_SOURCE_WHOLE_STREAM_INDEX_BINDING`

This is a **transport/reconstruction prerequisite PASS only**. It does not score G7 or any science statistic.

## Exact identity binding

Authoritative source object:

`y1_source_redshift_binning_v1.fits`

Observed and expected bytes:

`2738626560`

Authoritative whole-object SHA256:

`491f623d9370d3e5657db67d410e7cfd0e89475827046e6cd82ef6b3dd88c7a5`

Exact rows:

`136930995`

Derived row-aligned z-bin index:

- bytes: `273861990`
- SHA256: `dbb362b10c68825e775e7398b18eb77d37fe725ce80cfd5c07faec5cb5755628`

Stage-A artifact:

- artifact ID `9688707039`
- artifact ZIP SHA256 `366aad6468046e6964edc9cd2bfd299960d5dadf1856a30ec608e9ae191c1582`

## Transport mode that passed

- HTTP Range requests: `0`
- whole-object GET: `true`
- `Accept-Encoding: identity`
- exact byte-count check
- exact whole-object SHA check
- exact row-count check

The full source stream progressed monotonically from 4,194,304 rows to 136,930,995 rows and completed on the first v0.5 attempt.

This establishes that the prior DES/NCSA failures are specifically compatible with unreliable random Range transport rather than a blanket inability to read the authoritative object from GitHub Actions.

## Explicit non-science boundary

The Stage-A assertions require:

- `selection_applied = false`
- `science_gate_scored = false`
- `f_invalid_computed = false`
- `covariance_read = false`
- `G8_read = false`

Therefore this PASS cannot be cited as physical support, covariance closure, G7, G8, or G9 evidence.

## Downstream state

The same run has started job `98873808534`, `metacal-map`, which is sequentially streaming the authoritative metacal object and executing the previously frozen mapper.

The metacal whole-object identity remains:

- expected bytes: `84075649920`
- authoritative SHA256: `39a7fe03e54d96b85cee2fb523ea108c2a548ba1584368203f0464ed6241ebc8`

No downstream reconstruction PASS is claimed until that job terminates and its exact parent/reproduction assertions pass.

## Gate state

- G7 OPEN
- G8 OPEN
- G9 OPEN
