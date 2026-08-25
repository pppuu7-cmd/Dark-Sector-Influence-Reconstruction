# DSIR status snapshot — 2026-08-26

DSIR remains a reconstruction/meta-inference framework, not a fundamental theory.

| Item | Status | Evidence |
|---|---|---|
| Project separation from RTK | PASS | dedicated DSIR repository; RTK excluded |
| Recovery/manual backup | **PASS and live** | stable manual + `RECOVERY_LATEST` + findings register/standalone findings + BuyanovGPT atlas + logs |
| Conservation/gauge contract | **PASS G1 v0.1.1** | Bianchi/exchange bookkeeping + hard comoving-matter regression |
| Response basis | **PASS G2 v0.1.1** | same-solver `P_Delta/r_Delta`; hard cross-solver bridge |
| Six-family background atlas | **PASS G3A** | C0-C5 control embeddings |
| Six-family beyond-background atlas | **PASS G3B block-aware** | C1 smooth-w, C2 IDE, C3 GDM, C4 WDM high-k block, C5 f(R), C0 origin |
| Comparison readiness | **PASS** | Exp030 |
| GDM cs2/cv2 density degeneracy | **HARD** | `0.3226 deg` low-k; temporal `1.334 deg` |
| GDM cs2/cv2 slip separator | **HARD PASS** | slip `137.943 deg` oriented; equalized `56.963 deg` |
| GDM cs2/cv2 background/AP null | **HARD PASS / Exp037** | exact background/AP zero |
| Designer f(R) background/AP null | **HARD PASS / Exp038** | exact B0 background/AP zero |
| GDM vs f(R) scale-only degeneracy | **HARD** | `0.0781/0.1017 deg` |
| GDM vs f(R) temporal/full separator | **HARD** | temporal `16.05/17.28 deg`; full `25.18/25.49 deg` |
| WDM low-k blind / high-k visible | **HARD** | 3 keV `r_T(0.1)=-3.46e-6`, `r_T(10)=-0.10375` |
| ShapeFit finite-node proxy | **LIMIT** | ~36% residual for GDM/f(R) |
| Calibration-free AP | **HARD PASS / Exp035** | direct bridge ~`1e-14` |
| C5 scalar-growth representability | **HARD non-exact / Exp041** | `D_RSD` production `5.18e-6..8.81e-4` at kmax 0.24 |
| C3 GDM velocity/RSD bridge | **HARD VALIDATION FAIL / Exp042-043** | absolute sync/Newtonian bridge `~2.5-3.0e-6` > `1e-6`; p10 worsens; exploratory velocity science rejected |
| BuyanovGPT influence atlas | **LIVE through Exp047A** | response taxonomy + trajectory geometry; not theory |
| Candidate `Core=(G,T,tau)` | **HARD NEGATIVE / Exp045A** | compact additive core fails common C1/C2/C3/C5 low-k block |
| Scale-time interaction `I(k,z)` | **HARD RESPONSE FEATURE / Exp045A+046** | C5 strong, C3 moderate, IDE near-null on current low-k grid |
| Pairwise interaction localization | **HARD DESCRIPTIVE / Exp046** | GDM/f(R) `eta_I=0.612-0.614`; GDM cs2/cv2 `0.731` but total angle tiny |
| Interaction grid robustness | **HARD DESCRIPTIVE / Exp047B** | tier `IDE < smooth-w < GDM < f(R)` preserved 12/12; GDM/f(R) `eta_I=0.550-0.655` under every single-node deletion |
| Smooth-w interaction magnitude | **LIMIT / Exp047B** | dropping `k=0.001` reduces `chi_I` ~27.6x; tier stable but precise scalar not grid invariant |
| Finite-amplitude interaction hierarchy | **HARD DESCRIPTIVE / Exp047A** | sampled envelopes remain non-overlapping: IDE `1.4e-11..5.5e-11`, smooth `~1.08e-3`, GDM `0.013..0.0454`, f(R) `0.173..0.313` |
| Finite response trajectory curvature | **HARD DESCRIPTIVE / Exp047A** | GDM cv2 turns `7.18 deg` full / `12.19 deg` interaction; C5 turns `12.14/13.00 deg`; one-parameter families need not be straight in response space |
| GDM cs2 finite trajectory | **HARD DESCRIPTIVE / Exp047A** | nearly straight: `0.0279 deg` full turn; `chi_I~0.04525-0.04541` |
| IDE finite trajectories | **HARD DESCRIPTIVE / Exp047A** | interaction near-null across sampled alpha/beta amplitudes; beta central shape turns only `0.0041 deg` |
| Representation/discrimination/micro dimension | **METHOD RULE** | keep `N_micro`, `N_manifold`, `N_repr`, `N_disc` distinct |
| Synthetic latent-rank recovery | PASS | injected rank 3 recovered |
| Whitening robustness | tested suite PASS; **G5 PARTIAL** | family-complete joint observational whitening still missing |
| DESI DR2 AP | PASS G6A | calibration-free AP/relative expansion |
| DESI corrected DR1 ShapeFit | PASS G6B | corrected covariance layer |
| Discriminant graph | **HARD current graph only** | `{slip, small-scale transfer, time/sign}`; not three-parameter theorem |
| Scientific findings | **LIVE through standalone F18** | main register through F17 + `SCIENTIFIC_FINDING_F18_FINITE_AMPLITUDE_TRAJECTORY_GEOMETRY.md` |
| Universal model readiness | **NOT YET** | continue atlas; withheld validation and stable observation-space dimension required |
| New residual law | **OPEN G7** | no law claim |
| Withheld prediction | **OPEN G8** | mandatory before discovery |

## Current comparison findings

1. **Exact null patterns are physical information:** frozen GDM and designer-f(R) are exactly background/AP-null while perturbation-active.
2. **Degeneracies migrate across operators:** AP, structure, time, slip and small-scale transfer can reorder the same model pairs.
3. **GDM pressure/viscosity remains a microphysical density/time degeneracy; slip is the established separator.**
4. **GDM/f(R) separation is substantially joint `k x z` structure:** about 61% of normalized low-k shape separation is localized in irreducible scale-time interaction.
5. **That localization is grid-robust:** every single-node deletion keeps GDM/f(R) `eta_I` between roughly 0.55 and 0.655.
6. **The coarse nonseparability ordering now survives both grid deletion and finite amplitude:** `IDE near-null < smooth-w < GDM < f(R)` across the current sampled manifolds.
7. **But `chi_I` is not a universal family constant.** GDM viscosity and f(R) change materially along their finite physical rays.
8. **A one-parameter physical family may generate a curved high-dimensional response trajectory.** Therefore several significant global SVD modes can be curvature/compression modes rather than additional microscopic degrees of freedom.
9. **GDM pressure and viscosity differ strongly in finite-amplitude trajectory geometry:** cs2 stays almost straight while cv2 bends by several degrees at large amplitude, despite near-collinearity in the local density tangent.
10. **IDE is strikingly separable on the current low-k block:** physical alpha and beta remain at `chi_I~1e-11` across two decades in amplitude.
11. **Preliminary new pattern:** small-amplitude GDM and f(R) appear almost identical in the `k`-localization of interaction power but strongly different in its redshift localization. This is not yet a registered hard finding.
12. C4 WDM is missing from all low-k interaction comparisons, never zero-imputed.
13. Minimal latent dimension remains open; no parameter count is inferred from response modes alone.

## Immediate continuation

1. **Exp048 interaction localization geometry:** define normalized interaction-power marginals over `k` and `z`; test the preliminary GDM/f(R) pattern with exact controls and amplitude/grid stress tests.
2. Determine whether trajectory bending correlates with movement of characteristic transition scales through the finite `(k,z)` window; compare GDM cv2 and f(R).
3. Extend C4 WDM to a physically relevant high-k time-dependent `(k,z)` atlas and compute its interaction morphology without domain mismatch.
4. Preserve slip/lensing and small-scale transfer as independent channels; interaction geometry does not replace them.
5. Continue survey/window-aware shape and RSD work; theory angles are not detectability.
6. Estimate `N_repr`/`N_disc` only after common observation-space operators exist; never equate them with `N_micro`.
7. Continue searches for exact nulls, channel reversals, sign changes, localization flow and cross-family relations.
8. Universal model only after readiness criteria and a credible withheld-family test.
9. G7 remains open; no discovery before G8.
