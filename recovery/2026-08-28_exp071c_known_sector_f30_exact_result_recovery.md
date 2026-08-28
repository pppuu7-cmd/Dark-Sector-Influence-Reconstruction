# Exp071C exact known-sector F30 result recovery

**Recovered:** 2026-08-28 from immutable GitHub Actions artifact.

## Immutable provenance

- Run: `33020201997`
- Artifact id: `9626235928`
- Artifact name: `exp071c-known-sector-f30-specificity-da74d592fbcc2bba9cd223e924b245a3e52437e1`
- Artifact digest: `sha256:ed486effa593a409640577f8cdde614d5fddfc95653eb4ca78c56ae69a234e5e`
- Frozen operator: Exp060A F30, trained only on dark-sector C3+C5+C7+C8 sources.
- Known-sector spectra: fresh official CLASS, not training inputs.

## Exact classification

`COMPLETE_KNOWN_SECTOR_F30_SPECIFICITY_CONTROL_V0_1`

Primary classification:

`F30_DARK_SPECIFICITY_WEAKENED_BY_KNOWN_SECTOR_CONTROL`

### K1 — primordial tilt

`pass_full_and_all_leave_one_z = false`.

Full-gate adjacent standardized step norms:

- `9.471713945036838e-12`
- `8.108486944218368e-12`
- `2.194877034314983e-12`
- `2.087705675612978e-12`

All four are zero/tiny under the frozen gate; nonadjacent intersections are also present. Thus K1 does not reproduce an admissible F30 path.

### K2 — baryon/CDM redistribution at fixed total matter

Frozen points:

- `omega_b=[0.0228,0.0232,0.0236,0.0240,0.0244]`
- `omega_cdm=[0.1196,0.1192,0.1188,0.1184,0.1180]`
- every point has `omega_b+omega_cdm=0.1424`.

`pass_full_and_all_leave_one_z = true`.

Full-gate adjacent standardized step norms:

- `0.0020539788273644314`
- `0.002184827949003851`
- `0.0021088528684104183`
- `0.0008492280765012907`

There are no zero/tiny steps and no nonadjacent intersections.

The centered family-local SVD is strongly one-dimensional:

- first singular value `0.0014571909317770537`;
- first variance fraction `0.999043969028475`;
- first three cumulative variance fraction `0.9999999558977343`.

## Scientific consequence for Article 2

The preregistered matter-only F30 morphology cannot be described as a dark-sector-specific fingerprint under the tested control set. A known-sector redistribution between baryons and CDM at fixed total matter follows an admissible F30 path.

This is a useful falsification result, not a failure of the broader response-geometry program. It changes the defensible question from “is F30 dark-specific?” to “which additional independently sourced channels break matter-space mimicry?”

The pre-existing GDM metric/slip hard regression provides one concrete example where slip adds such a direction. Exp071D is now the direct prospective K2 follow-up.

## Forbidden reinterpretations

- Do not retrain F30 to reject K2.
- Do not remove K2 from the control set after seeing its PASS.
- Do not claim that K2 necessarily mimics the signed Weyl/slip response; Exp071C tested F30 matter-space specificity only.
- Do not claim observational evidence or a dark-sector detection.

G7/G8/G9 remain OPEN.
