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
| A2-C12 | ✅ falsification | Adding the matter-power tangent to the same frozen Weyl+slip geometry **does not remove the residual sound-speed-like ambiguity**. Matter-only K2-bar1 lies at **19.2231°** from GDM `cs2` and **19.0371°** from GDM `cv2`; after GDM-only equalization of the three-channel `(r_P,r_W,Delta_slip)` vector, the angles are **19.0749°** to `cs2` and **50.1667°** to `cv2`. The primary 45° two-axis separator therefore fails only on the `cs2`-like direction. Finite-step stability is strong: maximum three-channel K2 drift from bar1 is **0.11694°**. | Exp071F prereg commit `85daeca416ce8ed1e691008fd4178fd6bbf94d15`; run `33178154667`; job `98872091411`; artifact `9688506671`, SHA256 `e03e72251ab8ed9e0fa820bdae31342dc718349d78713db5fcac06bf00cc6779`; classification `K2_3CHANNEL_DIRECTION_OVERLAPS_AT_LEAST_ONE_GDM_AXIS_EXP071F`. | “More correlated matter/metric channels automatically guarantee specificity” or “K2 is indistinguishable from viscosity-like GDM.” |
| A2-C13 | ✅ | A qualitatively independent **finite-bin temporal derivative of the same matter response** resolves the static K2↔GDM ambiguity under the frozen directional test. K2-bar1 is **138.1006°** from the GDM `cs2(1e-7)` temporal direction and **137.0973°** from `cv2(1e-7)`, despite the corresponding static matter angles being only **19.2231° / 19.0371°**. The result is insensitive to the GDM tangent convention: replacing the `1e-7` parents by the Exp040 averaged parents shifts the K2 angles by only **+0.0101° / −0.0262°**. | Exp071H prereg commit `93bd51867d90fa346ce644deebe228e6d0d45697`; run `33179056348`; job `98875221176`; artifact `9688888346`, ZIP SHA256 `60d582b9f0249329c323066f248cbdc33f3c149966eb30317ecb2f3f22cda0a5`; classification `K2_FINITE_BIN_GROWTH_SEPARATED_FROM_BOTH_GDM_1E7_AXES_EXP071H`. Exp071G v0.1 is retained as invalid-for-science because its integrity check mixed the two parent-tangent constructions. | “This is tracer RSD”, “this is observational distinguishability”, “temporal separation uniquely identifies microscopic physics”, or “static degeneracy implies full physical equivalence.” |
| A2-C14 | ✅ | A **same-definition CLASS total-velocity-transfer** channel independently confirms that the K2 known-sector direction is not equivalent to either tested GDM direction. After a pre-execution source/parser audit and fresh `vTk` I/O-only reruns that reproduce all immutable K2 and GDM parent matter-power spectra with maximum relative difference **0.0** (threshold `1e-10`), K2-bar1 lies **165.9455°** from GDM `cs2(1e-7)` and **164.7113°** from `cv2(1e-7)` in `r_ttot=ln|t_tot/t_tot_ref|` space. The GDM velocity directions themselves remain close (**2.3683°**), and the maximum K2 finite-step drift is only **0.1284°**. An independent common `t_b` sensitivity also separates K2 from both GDM axes (**80.99° / 76.23°**). | Exp071I original prereg `30797f97f9ee4d295dcaf1905d3647230b6fa1cc`; pre-execution `vTk` amendment `55ea3d6435767ecf570702b55d411a12eddd59b4`; source contract `docs/ARTICLE2_TOTAL_VELOCITY_PROVIDER_CONTRACT_2026-08-28.md`; run `33181895623`; job `98884913088`; artifact `9690064470`, ZIP SHA256 `ba41e25e6bcdfd2c23c4c9c8bc48bf9ddd85d7776a2e5bb7976e2e061d531e14`; terminal summary `data/derived/exp071i_k2_gdm_total_velocity_direction_summary_v0_1.json`; classification `K2_TOTAL_VELOCITY_SEPARATED_FROM_BOTH_GDM_AXES_EXP071I`. | “This is tracer RSD or `f sigma_8`”, “this proves survey distinguishability”, “velocity uniquely identifies dark-sector microphysics”, or “G7 is closed.” |

## Core narrative implied by the matrix

The strongest Article-2 narrative is a **hierarchy of specificity** rather than a hierarchy of model names:

1. matter response geometry compresses mechanism families usefully;
2. matter-only morphological specificity fails a direct known-sector falsification control;
3. metric/slip information adds a genuinely new direction that separates sound-speed-like from viscosity-like GDM perturbations, but neither a scalar slip statistic nor the full two-channel direction is universally mechanism-specific;
4. Exp071E localizes the known-sector ambiguity to the GDM sound-speed-like direction;
5. Exp071F shows that simply concatenating the matter-power direction with Weyl+slip does **not** cure that ambiguity: the K2↔`cs2` angle remains near 19°, while the K2↔`cv2` angle stays safely above the 45° separator;
6. Exp071H shows that a **temporal transform of the same matter response is not redundant with the static matter block**: the K2↔GDM angles jump from ~19° in static matter space to ~137–138° in finite-bin temporal-response space, robustly under two GDM parent-tangent conventions;
7. Exp071I then supplies an independent true velocity-transfer test with a source-level cross-solver contract: `t_tot` places K2 ~165° from both GDM directions after exact parent-spectrum reproduction, while the two GDM velocity directions remain only ~2.37° apart;
8. the combined H/I result therefore localizes the static ambiguity: K2 can mimic GDM in selected **static** response coordinates while evolving and flowing in a qualitatively different direction;
9. this still does not turn `t_tot` into tracer RSD: observational interpretation requires finite tracer/window operators, physical support and the Article-3 covariance/nuisance chain.

In compact form:

`matter morphology -> known-sector falsification -> Weyl/slip separation -> residual K2~cs2 static degeneracy -> matter+Weyl+slip non-cure -> finite-bin temporal separation -> same-definition total-velocity confirmation -> provider/physical-support boundary -> finite operator admissibility`.

The publishable result is not a “unique fingerprint”. It is a controlled demonstration that response specificity is **coordinate- and channel-conditioned**: apparently degenerate static response directions can be sharply separated by independent evolution and velocity information.

## Suggested paper figures/tables

1. **Figure 1 — Specificity hierarchy:** matter-only response through known-sector falsification, Weyl/slip augmentation, three-channel falsification, temporal separation, total-velocity confirmation and physical support.
2. **Figure 2 — Known-sector F30 falsification:** dark-sector families, K1 tilt controls and K2 baryon/CDM controls.
3. **Figure 3 — Metric/slip hierarchy:** GDM `cs2` vs `cv2` channel angles, Exp071D scalar control, and Exp071E joint-direction angles `18.93° / 58.91°`.
4. **Figure 4 — Static three-channel non-cure:** Exp071F matter-only `19.22° / 19.04°` versus three-channel `19.07° / 50.17°`.
5. **Figure 5 — Static → temporal → velocity reversal:** K2 vs the two GDM axes in static matter (~19°), finite-bin temporal (~137–138°) and `t_tot` velocity (~165°) response spaces.
6. **Figure 6 — Velocity controls:** GDM `cs2/cv2` mutual `t_tot` angle `2.37°`, K2 finite-step velocity drift `<0.129°`, and `t_b` sensitivity angles `80.99° / 76.23°`.
7. **Figure 7 — K2 finite-step robustness:** Exp071E/F static joint drifts below `0.125°`, Exp071H temporal drift below `0.420°`, Exp071I `t_tot` drift below `0.129°`.
8. **Figure 8 — Physical/observational support boundary:** Exp071A 495/495 provider cells vs Exp072A zero admissible observational dimension, then Exp072B/C boundary localization.
9. **Figure 9 — Finite-operator route inventory:** BOSS finite-matrix success/non-classifying component contrasted with KiDS finite-theta absolute-response failure.
10. **Table 1 — Claim matrix:** shortened version of this document with run IDs and classifications.
11. **Table 2 — Negative-result / integrity ledger:** scientific falsifications separated from infrastructure failures and invalid-for-science provenance mismatches such as Exp071G v0.1.
12. **Table 3 — Channel hierarchy:** static matter, static metric/slip, temporal derivative and total-velocity response angles for K2 vs GDM.

## Result language for the abstract/discussion

Safe language:

> Matter-response morphology is informative but not generically mechanism-specific: a fixed-total-matter baryon/CDM control reproduces the preregistered F30 criterion. Metric-slip responses add independent information, yet frozen scalar, two-channel and three-channel static tests retain a sound-speed-like known-sector degeneracy near 19°. A preregistered finite-bin temporal derivative breaks that static degeneracy, placing the K2 direction about 137–138° from both tested GDM axes. A separate source-audited CLASS total-velocity-transfer control independently confirms the separation at about 165° from both GDM axes, after I/O-extended runs reproduce the immutable parent matter-power spectra exactly. Response equivalence is therefore channel-conditioned: similarity in static matter/metric coordinates need not survive temporal evolution or a same-definition velocity channel. Observational use remains restricted by physical-support, finite-window, tracer/RSD and downstream covariance/nuisance requirements.

Do not use language equivalent to “dark-sector detection”, “unique fingerprint”, “proof of modified gravity”, “RSD detection”, or “observational preference” in Article 2 unless a future independent observational gate explicitly authorizes it.

## Separation from Article 3

Article 2 may use provider-space, finite-operator **applicability**, the theory-space temporal operator and the source-audited same-definition CLASS `t_tot` velocity-transfer control. It must not import unfinished Article-3 covariance whitening, nuisance quotient, G7 relation/null, G8 or G9 results. Those remain downstream and independently gated.
