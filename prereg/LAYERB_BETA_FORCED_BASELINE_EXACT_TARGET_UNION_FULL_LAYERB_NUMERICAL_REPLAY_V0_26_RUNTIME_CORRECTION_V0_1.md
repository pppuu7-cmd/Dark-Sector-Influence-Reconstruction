# DSIR V0.26 candidate runtime correction V0.1

Status: **PROSPECTIVE CANDIDATE CORRECTION — NOT EXECUTABLE**  
Date: 2026-09-15  
Effect: `+0/+0`.

This correction is response-blind and was created before any V0.26 CLASS solve. It corrects one over-broad sentence in `prereg/LAYERB_BETA_FORCED_BASELINE_EXACT_TARGET_UNION_FULL_LAYERB_NUMERICAL_REPLAY_V0_26.md` and must be read jointly with that candidate preregistration and the hardening amendment.

## Correction

The original V0.26 candidate stated `tol_perturb_integration = 1e-12 for every substantive V0.26 model`. That is too broad and is superseded.

Freeze the route-specific perturbation tolerances instead:

- **alpha canonical-32769 route** (`reference`, `alpha_minus`): inherit the exact production precision file `configs/dsir4/c2/dsir_ide_p8_v0_1.pre`, therefore `tol_perturb_integration = 3e-10` and `perturb_sampling_stepsize = 0.00035`; no V0.25 beta override is applied to alpha;
- **beta exact-target route** (`beta_plus`, `beta_minus`, pure GRID896, mixed exact-target unions and target-only direct references): inherit the V0.25 beta intervention and explicitly override `tol_perturb_integration = 1e-12` while preserving `perturb_sampling_stepsize = 0.00035`.

Rationale: the operand-localization authority already places alpha below the frozen `1e-3` convergence threshold on the canonical 32769 route. Applying the later beta-specific `1e-12` override to alpha would alter the already validated alpha method while claiming to preserve it. The V0.25 beta contract explicitly freezes `tol300_override = 1e-12`; the historical production precision file itself contains `tol_perturb_integration = 3e-10` and `perturb_sampling_stepsize = 0.00035`.

## Consequences

- Solver counts remain unchanged: alpha 16, beta 722, total 738 CLASS constructions.
- All row-denominator, batching, canonical digest, capacity, sentinel, provenance and interpretation-ceiling rules remain unchanged.
- Alpha uses fresh V0.26 calculations under the inherited 32769 route; historical alpha response values remain non-gating.
- Beta uses fresh V0.26 calculations under the exact-target-union remedy.
- Any executor that applies `1e-12` to alpha, or fails to apply `1e-12` to beta, is INVALID for V0.26.
- No V0.26 science launch is authorized by this correction.
