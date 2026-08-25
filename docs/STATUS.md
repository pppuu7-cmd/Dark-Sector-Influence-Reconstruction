# DSIR status snapshot — 2026-08-26

DSIR remains a reconstruction/meta-inference framework, not a fundamental theory.

| Item | Status | Evidence |
|---|---|---|
| Project separation from RTK | PASS | dedicated DSIR repository; RTK excluded |
| Recovery/manual backup | **PASS and live** | stable manual + live overlay + Exp047A appendix + findings + atlas + logs |
| Conservation/gauge contract | **PASS G1 v0.1.1** | hard bookkeeping/bridge regressions |
| Response basis | **PASS G2 v0.1.1** | same-solver `P_Delta/r_Delta` + cross-solver bridge |
| Six-family background atlas | **PASS G3A** | C0-C5 |
| Six-family beyond-background atlas | **PASS G3B block-aware** | C1-C5 with C4 separate high-k block |
| Comparison readiness | **PASS** | Exp030 |
| GDM cs2/cv2 density degeneracy | **HARD** | `0.3226 deg`; temporal `1.334 deg` |
| GDM cs2/cv2 slip separator | **HARD** | slip `137.943 deg` oriented / `56.963 deg` equalized |
| GDM and C5 background/AP nulls | **HARD** | Exp037/038 |
| GDM vs f(R) scale-only degeneracy | **HARD** | `0.0781/0.1017 deg` |
| GDM vs f(R) temporal/full separator | **HARD** | `16-17 deg` temporal; `25.18-25.49 deg` full |
| WDM low-k blind / high-k visible | **HARD** | 3 keV `r_T(0.1)=-3.46e-6`, `r_T(10)=-0.10375` |
| ShapeFit finite-node proxy | **LIMIT** | ~36% residual for GDM/f(R) |
| C5 scalar-growth representability | **HARD non-exact** | Exp041 `D_RSD` nonzero |
| C3 GDM velocity/RSD bridge | **HARD VALIDATION FAIL** | Exp042/043; exploratory velocity science rejected |
| Candidate `Core=(G,T,tau)` | **HARD NEGATIVE** | Exp045A |
| Scale-time interaction `I(k,z)` | **HARD RESPONSE FEATURE** | Exp045A/046 |
| Pairwise interaction localization `eta_I` | **HARD DESCRIPTIVE** | GDM/f(R) `0.612-0.614` |
| Interaction grid robustness | **HARD DESCRIPTIVE** | Exp047B: class order 12/12; GDM/f(R) `eta_I=0.550-0.655` |
| Smooth-w exact `chi_I` | **LIMIT** | low-k node sensitivity ~27.6x |
| Finite-amplitude nonseparability order | **HARD DESCRIPTIVE** | Exp047A: sampled `IDE < smooth-w < GDM < f(R)` envelopes do not overlap |
| Finite response-trajectory curvature | **HARD DESCRIPTIVE** | cv2 `7.18/12.19 deg`; f(R) `12.14/13.00 deg` full/interaction turning |
| Dimension bookkeeping | **METHOD RULE** | keep `N_micro`, `N_manifold`, `N_repr`, `N_disc` distinct |
| Interaction localization `q_k,q_z` | **HARD DESCRIPTIVE / Exp048A** | normalized squared-energy marginals with algebraic controls |
| GDM/f(R) scale-localization degeneracy | **HARD DESCRIPTIVE / Exp048A** | `q_k` angles `0.040/0.051 deg`; `q_z` angles `20.15/21.52 deg` |
| smooth-w/f(R) complementary localization | **HARD DESCRIPTIVE / Exp048A** | `q_k=79.37 deg`, `q_z=1.93 deg` |
| GDM cs2/cv2 localization degeneracy | **HARD DESCRIPTIVE / Exp048A** | `q_k=0.0113 deg`, `q_z=1.382 deg`; slip still required |
| Finite localization flow | **HARD DESCRIPTIVE / Exp048B** | cv2 and f(R) both shift `k_I^geo ~0.051 -> ~0.040 h/Mpc` at large amplitude |
| Time-localization flow | **MECHANISM-SPECIFIC / Exp048B** | cv2 `z_I 1.234->1.390`; f(R) nonmonotonic `0.984->0.836->0.914->1.119` |
| Transition-window interpretation | **SUPPORTED/PRELIMINARY** | common scale migration + nonmonotonic compression defects; solver-level `k_*` bridge still required |
| BuyanovGPT influence atlas | **LIVE** | response taxonomy/geometry, not theory |
| Synthetic latent-rank recovery | PASS | injected rank 3 recovered |
| Whitening robustness | **G5 PARTIAL** | family-complete joint observational whitening missing |
| DESI layers | **G6A/G6B PASS** | AP + corrected ShapeFit |
| Discriminant graph | **HARD current graph only** | `{slip, small-scale transfer, time/sign}` |
| Scientific findings | **LIVE through standalone F20** | main register F1-F17 + standalone F18-F20 |
| Universal model readiness | **NOT YET** | withheld validation/observation-space dimension still missing |
| New residual law | **OPEN G7** | no law claim |
| Withheld prediction | **OPEN G8** | mandatory before discovery |

## Current comparison findings

1. **Exact null patterns are part of model identity:** GDM and designer-f(R) can be background/AP-null yet perturbation-active.
2. **Degeneracies migrate between operators rather than disappearing monotonically.**
3. **Simple additive `G+T+tau` is insufficient:** joint `k x z` interaction is material, especially for C5.
4. **About 61% of GDM/f(R) normalized low-k structure separation is localized in irreducible scale-time interaction, and this survives every single-node deletion.**
5. **The sampled nonseparability order `IDE < smooth-w < GDM < f(R)` survives both grid deletion and finite amplitude**, but exact `chi_I` is not a family invariant.
6. **One-parameter families can be strongly curved in response space.** Several global SVD modes can therefore be curvature/compression modes rather than extra microscopic degrees of freedom.
7. **Localization geometry exposes complementary degeneracies:** GDM/f(R) are almost identical in scale localization but separated in time localization; smooth-w/f(R) are almost identical in time localization but strongly separated in scale localization.
8. **GDM pressure/viscosity remain localization lookalikes as well as density lookalikes.** Metric slip remains the demonstrated mechanism separator.
9. **GDM viscosity and f(R) both move interaction localization toward lower k at large amplitude**, while their redshift flows differ. This supports a transition-window hypothesis but does not establish a physical transition law.
10. C4 WDM remains outside the low-k interaction geometry and is never zero-imputed.
11. Minimal latent dimension remains open; `N_micro`, `N_manifold`, `N_repr`, and `N_disc` must not be conflated.

## Immediate continuation

1. Build a **solver-level characteristic-scale bridge** `k_*(z;theta)` for GDM and designer f(R); test whether measured `k_I^geo/q_k` flow tracks it.
2. Stress `q_k/q_z` localization under leave-one-node deletion, especially smooth-w low-k sensitivity.
3. Extend C4 WDM to a high-k time-dependent `(k,z)` atlas and compute `I,q_k,q_z` without domain mismatch.
4. Preserve slip/lensing, RSD and small-scale transfer as independent channels.
5. Continue survey/window/covariance projection; theory geometry is not detectability.
6. Continue exact-null, channel-reversal, orientation/sign, localization-flow and failed-compression searches.
7. Universal model only after readiness and withheld-family validation.
8. G7 remains open; no discovery before G8.

<!-- DSIR_EXP049B_DOC_SYNC_2026_08_26 -->
## 2026-08-26 update — Exp049B

✅ **PR #27 Exp047A merged** into `main` as merge `a29e44ceca75da5dd9efc997ddfa3dfc9b3d707c`.

✅ **PR #28 Exp048A/B merged** into `main` as merge `282d0d8000ee551ae8f365c55f063e910edab91a`.

✅ **Exp049B withheld GDM window-crossing test PASS**: run `32904158849`, artifact `9584180621`, SHA256 `892db89ea5e530af6b8c1aae5404ef75c0fc84448e671e780ce02d91b4711a8a`. New intermediate `cv2` points obey the pre-frozen non-increasing `k_I_geo` prediction.

🟡 **Exp049A designer-f(R) exact physical-scale bridge remains active** on PR #29. A CAMB output-root double-underscore naming issue was identified before scientific reading and corrected; only the corrected head/run may be interpreted.

❌ **G7 remains OPEN**: no universal residual law has been established.

❌ **G8 remains OPEN**: no withheld-family/model prediction sufficient for discovery/universal-model construction has been completed. Exp049B is withheld within one validated control family, not a withheld dark-sector family.

<!-- EXP049A_F22_SYNC_2026-08-26 -->
## Exp049A / F22 status — 2026-08-26

🟢 Source-native physical-scale extraction PASS: run `32904376001`, artifact `9584346604`.

🟢 Exact designer-f(R) diagnostic controls pass; max terminal `B0` relative error `8.75255e-9 < 1e-6`.

🟢 GDM Exp049B/F21 supplies independent withheld confirmation that `k_I^geo` migrates downward after the dynamic-shear proxy enters the low-k window.

🟡 Designer-f(R) shows the same window-entry/localization ordering retrospectively; Exp049C is the required withheld test.

🔴 No G7 residual law, no G8 discovery, no universal-model construction, no intrinsic-rank/no-hair claim.

<!-- F23_FR_WINDOW_CROSSING_SYNC_2026-08-26 -->
## F23 status — second withheld mechanism

🟢 Exp049C designer-f(R) withheld prediction PASS: run `32907619613`, artifact `9585579947`.

🟢 Exact source-scale contract PASS; max terminal B0 error `7.51e-11`, every withheld exact k_C enters `k<=0.1` on the frozen z grid, and min k_C decreases with B0.

🟢 `k_I^geo` decreases at every withheld step: `0.0480162 -> 0.0420339 h/Mpc`.

🟢 Together with GDM F21, the finite-window directional prediction is independently supported in **two physically distinct frozen mechanisms**.

🟡 Cross-family universality remains unestablished; C4 high-k time atlas, broader family/domain tests and observation-space kernels remain missing.

🔴 G7 OPEN. G8 OPEN. Universal-model construction remains deferred.

