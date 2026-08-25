# DSIR status snapshot — 2026-08-25

DSIR remains a reconstruction/meta-inference framework, not a fundamental theory.

| Item | Status | Evidence |
|---|---|---|
| Project separation from RTK | PASS | dedicated DSIR repository; RTK excluded |
| Recovery/manual backup | **PASS and live** | current manual + preserved pre-Exp044 snapshot + `RECOVERY_LATEST` + findings register + BuyanovGPT atlas + logs |
| Conservation/gauge contract | **PASS G1 v0.1.1** | Bianchi/exchange bookkeeping + hard comoving-matter regression |
| Response basis | **PASS G2 v0.1.1** | same-solver `P_Delta/r_Delta`; hard cross-solver bridge |
| Six-family background atlas | **PASS G3A** | C0-C5 control embeddings |
| Six-family beyond-background atlas | **PASS G3B block-aware** | C1 smooth-w, C2 IDE, C3 GDM, C4 WDM high-k block, C5 f(R), C0 origin |
| Comparison readiness | **PASS** | Exp030 |
| GDM cs2/cv2 density degeneracy | **HARD** | `0.3226 deg` low-k; temporal `1.334 deg` |
| GDM cs2/cv2 slip separator | **HARD PASS** | slip `137.943 deg` oriented; equalized `56.963 deg` |
| GDM cs2/cv2 background/AP null | **HARD PASS / Exp037** | exact background/AP zero |
| Designer f(R) background/AP null | **HARD PASS / Exp038** | exact B0 background/AP zero; final run `32786915513` |
| GDM vs f(R) scale-only degeneracy | **HARD** | `0.0781/0.1017 deg` |
| GDM vs f(R) temporal/full separator | **HARD** | temporal `16.05/17.28 deg`; full `25.18/25.49 deg` |
| Finite-bin temporal operator | **HARD PASS / Exp040** | machine-precision controls |
| IDE alpha/beta channel migration | **HARD** | AP `9.04` -> temporal `29.40` -> structure `58.93 deg` |
| Smooth-w vs IDE-alpha reversal | **HARD** | AP `72.80`, temporal `10.31`, structure `52.19 deg` |
| WDM low-k blind / high-k visible | **HARD** | 3 keV `r_T(0.1)=-3.46e-6`, `r_T(10)=-0.10375` |
| ShapeFit finite-node proxy | **LIMIT** | ~36% residual for GDM/f(R) |
| Calibration-free AP | **HARD PASS / Exp035** | direct bridge ~`1e-14` |
| Low-z AP atlas | **SUBSTANTIALLY CLOSED** | C0 origin, C1/C2 nonzero, C3/C5 exact-null; C4 separate |
| ShapeFit RSD definition | **PROTOCOL FROZEN / Exp039** | `f_sigma_s8`, `s=r_d/r_d_ref`, density-velocity representability required |
| C5 scalar-growth representability | **HARD non-exact / Exp041** | `D_RSD` production `5.18e-6..8.81e-4` at kmax 0.24 |
| CAMB printed growth precision | **LIMIT** | four-decimal summaries rejected for small-B0 tangent |
| C3 GDM velocity/RSD bridge | **HARD VALIDATION FAIL / Exp042-043** | absolute sync/Newtonian Delta bridge `~2.5-3.0e-6` > `1e-6`; p10 worsens by factor `1.193`; exploratory velocity science rejected |
| BuyanovGPT influence atlas | **LIVE** | `docs/BUYANOVGPT_TABLE.md`; response taxonomy only, not theory |
| Candidate `Core=(G,T,tau)` | **HARD NEGATIVE / Exp045A** | compact additive core fails common C1/C2/C3/C5 low-k block |
| Scale-time interaction `I(k,z)` | **HARD RESPONSE FEATURE / Exp045A+046** | C5 `chi_I=0.299856`; C3 `~0.044`; IDE interaction near-null on current grid |
| Pairwise interaction localization | **HARD DESCRIPTIVE / Exp046** | GDM/f(R) `eta_I=0.612-0.614`; IDE-alpha/f(R) `0.572`; GDM cs2/cv2 `0.731` but total angle only `0.323 deg` |
| GDM interaction morphology | **HARD DESCRIPTIVE / Exp046** | cs2/cv2 interaction angle `0.743 deg`; interaction alone does not solve pressure/viscosity degeneracy |
| GDM vs f(R) interaction morphology | **HARD DESCRIPTIVE / Exp046** | interaction angles `10.99/11.71 deg`; joint k-x-z structure materially carries separation |
| Representation vs discrimination dimension | **METHOD RULE** | keep `N_repr` distinct from `N_disc` |
| Synthetic latent-rank recovery | PASS | injected rank 3 recovered |
| Whitening robustness | tested suite PASS; **G5 PARTIAL** | family-complete joint observational whitening still missing |
| DESI DR2 AP | PASS G6A | calibration-free AP/relative expansion |
| DESI corrected DR1 ShapeFit | PASS G6B | corrected covariance layer |
| Discriminant graph | **HARD current graph only** | `{slip, small-scale transfer, time/sign}`; not three-parameter theorem |
| Scientific findings register | **LIVE through F16** | status-preserving chronology |
| Universal model readiness | **NOT YET** | continue atlas; withheld validation and stable observation-space dimension required |
| New residual law | **OPEN G7** | no law claim |
| Withheld prediction | **OPEN G8** | mandatory before discovery |

## Current comparison findings

1. **Exact channel-null structure repeats across different physics:** frozen GDM cs2/cv2 and designer-f(R) B0 are exactly background/AP-null while perturbation-active.
2. **Degeneracies migrate rather than monotonically disappear:** AP, temporal growth, density structure, slip and small-scale transfer can reorder the same model pairs.
3. **GDM pressure/viscosity remains a density/time microphysical degeneracy; slip is the established separator.** Exp046 shows even the interaction shapes are nearly collinear (`0.743 deg`).
4. **GDM/f(R) are not separated merely by “scale + time”.** Exp046 quantifies that `61.2-61.4%` of their normalized shape-separation power is in the irreducible scale-time interaction.
5. **Simple additive `(G,T,tau)` was explicitly tested and falsified.** C5 additive core captures only `70.01%` of low-k response power; irreducible interaction contributes `29.99%`.
6. **C3 has moderate nonseparability:** `chi_I~0.0436-0.0453` for cs2/cv2.
7. **IDE is strikingly different in this diagnostic:** both local IDE directions are essentially additive in `G+T+tau`, and IDE alpha/beta have `eta_I~1.5e-11`.
8. **A large `eta_I` is not detectability.** GDM cs2/cv2 have `eta_I=0.731` but total acute angle `0.323 deg`; interaction carries most of a tiny distinction.
9. **For materially separated pairs the localization can be physically useful:** GDM/f(R) combines `~25 deg` total separation with `eta_I~0.612`, while IDE-alpha/f(R) has `42.45 deg` and `eta_I~0.572`.
10. Smooth-w interaction morphology is almost orthogonal to GDM/f(R) interaction morphology (`~69.6-70 deg`), suggesting a potentially useful mechanism-level structural classifier to stress-test.
11. C4 WDM is not allowed into the low-k matrix as zero. Its high-k time-dependent atlas is needed before family-complete nonseparability claims.
12. **GDM velocity/RSD remains unvalidated:** tighter precision does not cure the synchronous/Newtonian absolute density mismatch, so exploratory velocity angles/defects are inadmissible.
13. Minimal latent dimension remains open. Do not equate the current three-channel discriminator set, or `I`, with a chosen number of universal parameters.

## Immediate continuation

1. Stress-test `chi_I`, `eta_I` and interaction-shape angles across available finite parameter steps / manifold amplitudes rather than only one local tangent normalization.
2. Test whether the ordering `IDE near-null -> smooth-w weak -> GDM moderate -> f(R) strong` survives those step changes; this is the most promising current cross-family regularity candidate.
3. Check grid/domain sensitivity by removing one k or z node at a time and measuring stability of `chi_I` and key `eta_I`; pre-freeze stability metrics before interpretation.
4. Extend C4 WDM to a physically relevant high-k `(k,z)` atlas and test its interaction morphology without domain mismatch.
5. Preserve slip/lensing and small-scale transfer as independent channels; interaction morphology does not replace them.
6. Continue survey/window-aware shape and RSD work; no survey distinguishability from theory angles alone.
7. Estimate `N_repr` and `N_disc` only after common observation-space operators exist; stress-test priors, sampling, solver precision, covariance and channel removal.
8. Continue primary model-to-model comparisons and search for exact nulls, channel reversals, sign changes, localization and robust cross-family relations.
9. Universal model only after readiness criteria and a credible withheld-family test.
10. G7 remains open; no discovery before G8.
