# Auxiliary common-grid resonance diagnostics during V0.12

Status: **NON-AUTHORITATIVE / DOES NOT MODIFY V0.12 FROZEN DECISION RULES**.

This note uses only terminal V0.9/V0.10/V0.11 artifacts and deterministic guarded-grid geometry. It was written after the V0.12 contract was frozen and launched, while V0.12 science lanes were still behind their decision barrier. It must not be used to retune V0.12 targets, thresholds or classification rules.

## Absolute response scale at the three frozen V0.11 violation cells

The V0.11 relative discrepancies are not caused by division by nearly-zero beta responses.

| Parent violation | common-grid signed response | direct TOL300R signed response | absolute shift | relative shift |
|---|---:|---:|---:|---:|
| GRID640, h=2e-4, z=0.6325, k=0.015680905231730345 | -0.0967210098679061 | -0.09708111633699446 | 0.0003601064690883504 | 0.003709335890188209 |
| GRID768, h=1e-4, z=0.4175, k=0.01223449922166366 | -0.3076372240684577 | -0.30639508963759 | 0.0012421344308677362 | 0.004037659729341879 |
| GRID896, h=1e-4, z=0.62, k=0.015516351488496949 | 0.13535147559196048 | 0.1355052995677397 | 0.00015382397577923257 | 0.0011351878950117023 |

GRID768 therefore contains an absolute signed-response displacement of about 1.24e-3, not merely an inflated relative error from a small denominator.

## Resolution localization

Each large discrepancy is sharply localized to one grid resolution/h combination. For the GRID640 parent target at h=2e-4 the relative common-vs-direct discrepancies on GRID512/640/768/896/1024 are approximately:

`5.42e-5, 3.709e-3, 2.72e-6, 2.89e-6, 4.05e-6`.

For the GRID768 parent target at h=1e-4:

`9.44e-6, 6.22e-6, 4.038e-3, 1.84e-6, 7.01e-7`.

For the GRID896 parent target at h=1e-4:

`2.58e-5, 3.03e-5, 9.88e-6, 1.135e-3, 1.64e-5`.

This is a resonance-like non-monotonic resolution pattern rather than a smooth error that decreases with grid refinement.

## h localization

The same cells show isolated h spikes. At the GRID640 target, only h=2e-4 reaches 3.709e-3; the other four frozen h values are O(1e-5). At the GRID768 target, only h=1e-4 reaches 4.038e-3; the other four are O(1e-5) or smaller. At the GRID896 target, h=1e-4 reaches 1.135e-3; the other frozen h values are at most about 6.34e-5.

This favors a rare numerical resonance/cancellation interpretation over a broad smooth interpolation bias, but it is not a causal classification. V0.12 remains the authority for separating cubic interpolation error from k-output node-set solver dependence.

## Cubic-stencil phase

The target fractional positions in the relevant log-grid cell are approximately:

- GRID640 offending target: 0.7950
- GRID768 offending target: 0.03284
- GRID896 offending target: 0.3719

Corresponding centered cubic weights are approximately:

- GRID640: `[-0.0327, 0.2217, 0.8598, -0.0488]`
- GRID768: `[-0.0104, 0.9825, 0.0334, -0.00547]`
- GRID896: `[-0.0634, 0.7015, 0.4153, -0.0534]`

There is no common bad within-cell phase or obviously shared cubic-weight pathology across the three violations. This again is only an auxiliary clue; no V0.12 criterion is changed.
