# Research checkpoint — Exp057A C8 failure-mechanism audit

Date: 2026-08-26

## Boundary
Diagnostic-only follow-up to the prospectively frozen Exp056B/F29 HARD FAIL. This record does not rescue F29, alter its threshold/operator/domain, retune C8, or change G7/G8/G9.

## Reproduction
Pinned CLASS commit: `e85808324f51fc694d12e3ed7439552a3c3f9540`.
Exact Exp056B C8 IDM-photon coupling grid was reproduced against the same uncoupled reference at the seven frozen redshifts and low-k response domain.
Workflow run: `32929473919` (success).

## Diagnostic result
- Adjacent full-response cosines: `[-0.21276087, 0.81699483, 0.87074497, 0.91879000]`.
- The first adjacent coupling step reverses orientation (negative cosine).
- Normalized-response singular values: `[1.98867426, 0.98229531, 0.28325389, 0.00614371, 0.00029210]`.
- Leading-mode variance fraction: `0.7909650664`; therefore a single normalized shape mode is not an adequate description of the five C8 responses.
- Sign-reversal cells: `35/35 = 1.0` across the adjacent-coupling diagnostic.
- Geometric k50 values remain non-monotone: `[0.01612975, 0.04959012, 0.01818440, 0.03972092, 0.01583583] h/Mpc`.
- Only models 2 and 5 have monotone normalized profiles at all seven redshifts; models 1, 3 and 4 are non-monotone at all seven redshifts.

## Interpretation
Exp056B/F29 failed for a structural reason rather than merely a poor scalar threshold coordinate: the C8 response family changes orientation/shape as coupling increases. The source scale is monotone while the full response is not representable by a single monotone localization coordinate over this frozen grid. This is evidence against the attempted one-coordinate universal source-to-response law v0.1, not evidence against DSIR itself.

No post-hoc replacement law is promoted from this diagnostic. A future law attempt must be separately preregistered and should allow at least a multi-coordinate/shape description before testing on a genuinely withheld family.

## Gate state
- G7 OPEN.
- G8 OPEN.
- G9 OPEN.
- Exp054C/F27 remains HARD FAIL.
- Exp055A/F28 remains retrospective evidence only.
- Exp056B/F29 remains HARD PROSPECTIVE FAIL.
