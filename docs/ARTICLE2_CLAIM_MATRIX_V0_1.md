# DSIR Article 2 — claim matrix v0.1

**Consolidated:** 2026-08-28

Purpose: convert the completed provider, specificity-control, physical-support and finite-operator audit chain into a paper-ready claim set. This matrix is deliberately conservative: a result is promoted only to the strongest statement directly supported by a prospectively frozen or immutable computation.

## Proposed Article-2 scope

**Working scientific question:** Which response-geometry features survive progressively stronger physical and known-sector controls, and which additional channels are required to distinguish mechanisms that are degenerate in matter-only response space?

The article should not be framed as a dark-sector detection paper. Its publishable contribution is a falsification-resistant hierarchy of response information and a set of explicit applicability boundaries.

## Claim matrix

| ID | Status | Paper-ready claim | Evidence | Explicitly forbidden stronger claim |
|---|---|---|---|---|
| A2-C1 | ✅ | A common response-geometry language can compare physically distinct dark-sector mechanisms without using model names as the primary coordinates. | Exp060-series cross-family response atlas, block-aware comparison, interaction/localization and transition-scale audits. | “The geometry uniquely identifies every microscopic model.” |
| A2-C2 | ✅ | Certified C3 and C5 physical providers can be placed on a shared signed `mm/Wm/WW` domain; Exp071A retains **495/495** provider cells. | Exp069H/069I C5 certification, Exp070C C3 native-grid provider, Exp071A common physical provider support. | “All nonlinear or observationally required scales are physically certified.” |
| A2-C3 | ✅ falsification | Matter-only F30 morphology is **not dark-sector-specific** under the tested known-sector controls: the K2 baryon/CDM redistribution family at fixed total `omega_m` passes the full F30 gate and all leave-one-redshift gates, while K1 primordial-tilt controls do not. | Exp071C run `33020201997`, immutable artifact `9626235928`; F30 operator inherited unchanged from dark-sector training. | “F30 by itself is a dark-sector fingerprint.” |
| A2-C4 | ✅ | Adding a metric/slip response can break a degeneracy that remains almost invisible in the Weyl-amplitude response: for GDM local `cs2` vs `cv2`, frozen `r_W` angles are ~0.30–0.38°, while slip angles are ~137.9–138.1° and the equalized combined metric angle is 56.96°. | Frozen GDM Weyl/slip hard regression, run `32774198185`, immutable artifact `9537340616`. | “This constitutes observational evidence for GDM” or “slip is uniquely dark-sector-specific.” |
| A2-C5 | ✅ falsification | A single scalar relative-slip amplitude ratio does **not** restore generic dark-sector specificity. K2 gives `q_slip/W=(1.31–1.42)e-8`, overlapping the frozen GDM `cs2` scale (`9.62e-9`) under the prospectively frozen ordering rule, although it remains many orders below the GDM `cv2` ratio (`7.64e-5`). | Exp071D run `33176559280`, artifact `9687861012`. | “K2 reproduces the full GDM cs2 direction” or “K2 overlaps the cv2 axis.” |
| A2-C6 | ✅ | The first ACT×unWISE observational-support route is physically inadmissible under the frozen 5% leakage criterion, despite a complete provider-space domain. | Exp072A: retained observational dimension 0. | “Provider-space completeness guarantees observational admissibility.” |
| A2-C7 | ✅ | The ACT×unWISE failure is localized to a coupled **low-redshift + high-k** boundary rather than being removable by a simple lower-k or higher-z cut independently. | Exp072B causal boundary decomposition. | “A single scalar k-cut solves the observational-support problem.” |
| A2-C8 | ✅ | The unique frozen joint support frontier lies at approximately `z_min=0.0087345858`, `k_max=4.8182610974 Mpc^-1`, but the simple linear GR-reference route remains ineligible through `Delta^2 <= 2`. | Exp072C + Exp073A. | “The Pareto frontier is a usable linear science region.” |
| A2-C9 | ✅ negative boundary | The current public/provider stack does not supply the independent nonlinear C3/C5 signed `mm/Wm/WW` completion required to rescue that route; phenomenological C3 continuation is not identifiable under the frozen completion tests. | Exp073B-E. | “A chosen phenomenological extrapolation is equivalent to a physical nonlinear provider.” |
| A2-C10 | ✅ | Finite observational operators change the admissibility diagnosis: a finite BOSS true-k matrix can be bound and yields a non-empty component (54/240 rows), while the examined KiDS finite-theta absolute-response route is non-normalizable under its frozen absolute criterion. | Exp073I/J/K/L. | “Any nominal survey window automatically supplies a valid finite physical-support operator.” |
| A2-C11 | ✅ falsification | Full equalized joint `(r_W, Delta_slip)` direction **still does not generically separate** the K2 known-sector mimic from both tested GDM axes. The preregistered K2-bar1 tangent is only **18.9257°** from GDM `cs2` but **58.9127°** from GDM `cv2`, against the frozen 45° threshold. This is stable across the five K2 steps: the largest joint drift from bar1 is only **0.1240°**. | Exp071E prereg commit `220e73f6cd5b52746498731073bf7392f6917dd9`; run `33177588360`; artifact `9688299959`; classification `K2_DIRECTION_OVERLAPS_AT_LEAST_ONE_GDM_AXIS_EXP071E`. | “Adding Weyl+slip guarantees unique dark-sector identification” or “K2 is degenerate with both GDM axes.” |

## Core narrative implied by the matrix

The strongest Article-2 narrative is a **hierarchy of specificity** rather than a hierarchy of model names:

1. matter response geometry compresses mechanism families usefully;
2. matter-only morphological specificity fails a direct known-sector falsification control;
3. independent metric/slip information adds genuinely new separating directions, but neither a scalar slip-to-Weyl norm ratio nor the present two-channel joint direction is universally mechanism-specific;
4. Exp071E localizes the remaining ambiguity: the K2 known-sector tangent remains close to the GDM sound-speed-like direction while being separated from the viscosity-like direction, so additional independent channels/observables are required for generic specificity;
5. any richer directional construction must still survive certified physical support and finite observational operators before observational inference is allowed.

In compact form:

`matter morphology -> known-sector falsification -> joint directional matter/Weyl/slip geometry -> residual mechanism degeneracy -> additional independent channels -> physical-support intersection -> finite operator admissibility`.

This is stronger and safer than claiming that one matter-only feature, one scalar slip statistic, or the present two-channel direction is itself a unique dark-sector signature.

## Suggested paper figures/tables

1. **Figure 1 — Specificity hierarchy:** schematic from matter-only response through known-sector falsification to joint metric/slip geometry and observational support.
2. **Figure 2 — Known-sector falsification:** F30 gate outcome for dark-sector families, K1 tilt controls and K2 baryon/CDM controls.
3. **Figure 3 — Metric/slip hierarchy:** GDM `cs2` vs `cv2` channel angles, Exp071D scalar control, and Exp071E joint-direction angles `18.93° / 58.91°`.
4. **Figure 4 — K2 finite-step robustness:** joint direction drift stays below `0.125°` across bar1–bar5 while the primary cs2 overlap remains far below the 45° separator.
5. **Figure 5 — Physical/observational support boundary:** Exp071A 495/495 provider cells vs Exp072A zero admissible observational dimension, then Exp072B/C boundary localization.
6. **Figure 6 — Finite-operator route inventory:** BOSS finite-matrix success/non-classifying component contrasted with KiDS finite-theta absolute-response failure.
7. **Table 1 — Claim matrix:** shortened version of this document with run IDs and classifications.
8. **Table 2 — Negative-result ledger:** every scientific FAIL/falsification kept as a boundary result, separated from infrastructure failures.

## Result language for the abstract/discussion

Safe language:

> Matter-response morphology is informative but not generically mechanism-specific: a fixed-total-matter baryon/CDM control reproduces the preregistered F30 criterion. Metric-slip responses add independent information, yet prospectively frozen scalar and full-direction tests both retain a sound-speed-like known-sector degeneracy while separating the viscosity-like direction. This identifies the need for additional independent response channels rather than a single universal fingerprint, with observational use further restricted by physical-support and finite-window admissibility.

Do not use language equivalent to “dark-sector detection”, “unique fingerprint”, “proof of modified gravity”, or “observational preference” in Article 2 unless a future independent observational gate explicitly authorizes it.

## Separation from Article 3

Article 2 may use provider-space and finite-operator **applicability** results. It must not import unfinished Article-3 covariance whitening, nuisance quotient, G7 relation/null, G8 or G9 results. Those remain downstream and independently gated.
