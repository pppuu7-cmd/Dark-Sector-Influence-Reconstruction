# DSIR-2 figure captions — v0.1

**Date:** 2026-08-28  
**Source specification:** `docs/ARTICLE2_FINAL_FIGURE_TABLE_SPEC_V0_1.md` on `main`.  
**Boundary:** all Exp071 angular quantities are theory/provider-space quantities under the frozen Euclidean comparison metric; the 45-degree separator is an experiment convention, not a universal significance threshold.

## Figure 1 — From static ambiguity to nuisance-line falsification

**Figure 1. Response specificity across static, temporal and velocity representations for the K2 known-sector control.** Static matter and metric-response comparisons retain a sound-speed-like ambiguity: K2 lies at approximately 19 degrees from the GDM `cs2` direction after matter-only and equalized matter+Weyl+slip constructions. For the preregistered positive K2 displacement, the finite-bin temporal response rotates to `138.10/137.10 deg` from the GDM `cs2/cv2` directions, while the source-audited CLASS total-velocity-transfer response gives `165.95/164.71 deg`; per-redshift removal of the scale-independent velocity amplitude leaves `166.44/164.93 deg`, and all frozen leave-one-scale/redshift tests remain above `157.82 deg`. These large values describe a selected oriented ray. The line spanned by the projected positive K2 response is instead only `13.56/15.07 deg` from the two GDM directions. Exp071L prospectively generates the opposite-sign K2 displacement and confirms the line geometry: K2− is `179.91 deg` from K2+ and lies `13.55/15.07 deg` from GDM `cs2/cv2`. Thus robust oriented separation does not imply separation of the physically two-sided nuisance line. Angles are theory/provider-space quantities and do not represent survey significance.

## Figure 2 — Representation kernel and physical recovery

**Figure 2. A representation-null known-sector nuisance and its recovery in a physically complete response.** Exp071M varies the primordial tilt in both directions around `n_s=0.965` and finds an exactly zero response in transfer-only `Delta ln|t_tot|` on the frozen support. Because the response norm vanishes, normalized angular comparison is scientifically undefined and the experiment terminates `INVALID_FOR_SCIENCE_EXP071M`; the null is a property of the chosen representation, not evidence that primordial tilt has no physical effect. Exp071N restores the omitted primordial-spectrum contribution using the common linear velocity-power response `Delta ln P_R + 2 Delta ln|t_tot|`, followed by the same per-redshift constant-in-k quotient used for the K2 velocity-shape test. K1 then becomes resolvable, retaining `62.55%` of its raw projected norm, but its physical two-sided nuisance line remains only `36.06/37.85 deg` from the tested GDM `cs2/cv2` directions, below the frozen 45-degree separator. Fresh parent `P(k,z)` and `t_tot` references reproduce with maximum relative difference `0.0` against the `1e-10` integrity threshold. The panel therefore illustrates the ordering `representation -> resolvability -> geometry`.

## Figure 3 — Provider support versus observational admissibility

**Figure 3. Theory/provider completeness does not guarantee a usable observational mode.** The certified C3/C5 construction retains all `495/495` cells on the frozen signed `mm/Wm/WW` provider support, establishing a complete theory/provider comparison domain for the Article-2 response tests. Applying an initial ACT×unWISE support route under the frozen 5% leakage criterion nevertheless leaves observational dimension `0`; the failure is coupled in low redshift and high wavenumber, with a frozen joint frontier near `z_min=0.0087345858` and `k_max=4.8182610974 Mpc^-1`. Finite measurement operators alter the admissibility diagnosis: the bound BOSS true-k matrix contains a non-empty `54/240`-row component, whereas the examined KiDS finite-theta absolute-response route fails its frozen normalization/admissibility criterion. These cases separate provider support, physical support and finite-observation support. They do not constitute covariance-whitened likelihood tests.

## Figure 4 — DSIR fail-closed specificity hierarchy

**Figure 4. Fail-closed hierarchy for response-space specificity.** A physical response must first be represented by a declared map `A` and must pass a nonzero/resolvability test; a nuisance lying in `ker(A)` cannot be normalized or assigned an angle. The allowed nuisance freedom is then represented according to its physical geometry—as an oriented ray, a two-sided line, or a higher-dimensional nuisance subspace—under a declared metric `M`. Only after response geometry is defined are physical-support and finite-observation operators applied. Covariance restriction and whitening, construction of the complete resolved signed nuisance basis, nuisance projection, and the downstream G7 relation/null test belong to the observational quotient stage and are not performed in Article 2. The hierarchy is therefore `representation A -> resolvability/ker(A) -> channel block -> ray/line/subspace -> metric M -> physical support -> finite observation operator -> covariance whitening -> nuisance quotient -> G7 relation/null`, with DSIR-2 stopping before covariance whitening.

## Figure-caption wording rules

- `t_tot` and the velocity-power response are not tracer RSD or `f sigma_8`.
- “separated” must be qualified as oriented-ray, line/subspace, or observational as appropriate.
- Do not call the support frontier a validated linear science region.
- Do not describe the 45-degree separator as a statistical confidence threshold.
- Do not use dark-sector detection, unique fingerprint, survey distinguishability, or G7/G8/G9 closure language.
