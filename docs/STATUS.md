# DSIR status snapshot — 2026-08-24

DSIR remains a reconstruction/meta-inference framework, not a fundamental theory.

| Item | Status | Evidence |
|---|---|---|
| Project separation from RTK | PASS | dedicated DSIR repository; RTK excluded from this research line |
| Recovery/manual backup | PASS and live | `RECOVERY_MANUAL.md` + `RECOVERY_LATEST.md` + gates/log/provenance |
| Conservation/gauge contract | **PASS G1 v0.1.1** | Bianchi/exchange bookkeeping + hard Newtonian/synchronous comoving-matter regression |
| Response basis v0.1.1 | **PASS G2** | same-solver `P_Delta/r_Delta`; hard cross-solver bridge `1e-9` PASS |
| Six-family background atlas | **PASS G3A v0.1** | control embeddings and exact background intersections documented |
| Six-family beyond-background atlas | **PASS G3B v0.1 block-aware** | C1 smooth-w, C2 IDE tangent cone, C3 GDM cs2/cv2, C4 WDM small-scale block, C5 full designer-f(R), C0 reference |
| Comparison readiness | **PASS** | Exp.030 run `32772758188`, `failures=[]`, status `PASS_READY_FOR_BLOCK_AWARE_MODEL_COMPARISON` |
| First cross-family comparison | **COMPLETE** | Exp.031; raw theory-space low-k comparison, no observational ranking |
| GDM cs2/cv2 low-k degeneracy | **HARD ESTABLISHED** | P angle `0.3226 deg`; Weyl amplitude also nearly collinear |
| GDM cs2/cv2 slip separator | **HARD PASS** | run `32774501069`: slip `137.943 deg`, equalized two-block angle `56.963 deg` |
| GDM vs f(R) scale-only degeneracy | **HARD ESTABLISHED** | scale-mode angles `0.0781/0.1017 deg` |
| GDM vs f(R) time/sign separator | **HARD PASS** | run `32774501126`: time-mode `25.18/25.49 deg`, full oriented `154.82/154.51 deg` |
| WDM low-k blindness / high-k separator | **HARD ESTABLISHED** | 3 keV: `r_T(0.1)=-3.46e-6`, `r_T(10)=-0.10375` |
| Synthetic latent-rank recovery | PASS | injected rank 3 recovered with corrected global noise edge |
| Whitening robustness | PASS tested suite; G5 PARTIAL | 30/30 coordinate/rescaling cases recover rank 3 after whitening |
| Theory-catalog prior sensitivity | CONTROLLED FAILURE MODE | report `R_model(pi)`; family-balanced sampling implemented |
| Missing-response handling | PASS method gate | validity masks/common subspaces; no zero/mean imputation |
| DESI DR2 AP response | PASS G6A | calibration-free AP and relative expansion |
| DESI DR1 corrected ShapeFit response | PASS G6B | geometry-growth-shape covariance from 2026 erratum |
| Conditional innovation | PASS preparation | aggregate null-consistent (`chi2~5.53/5`, `p~0.355`) |
| IDE solver/manifold | PASS + calibrated cone | hard zero limit; alpha positivity boundary; alpha/beta structure angle `58.93 deg` |
| GDM solver/manifold | PASS + calibrated two-axis patch | zero limit hard PASS; cs2/cv2 nearly collinear in P |
| H-EFTCAMB designer f(R) | **MG-S0 + MG-S1 PASS** | exact GR limit and common-baseline production `B0=1e-6..1e-3` |
| Discriminant graph v0.1 | HARD EVIDENCE FROZEN; CI pending/next | four proven edges; expected minimum separator set has three channels |
| New residual law | OPEN G7 | no law claimed; raw-theory comparison is now unblocked |
| Withheld prediction | OPEN G8 | mandatory before discovery |

## Current comparison findings

1. GDM sound speed and viscosity are nearly the same low-k matter-power direction, but metric slip separates them strongly.
2. GDM pressure/viscosity and designer f(R) have almost identical leading **scale shapes** on the current low-k grid, but differ in time evolution and physical response sign.
3. Smooth non-phantom wDE has a much flatter k-dependence than GDM/f(R).
4. IDE beta is much less separable into a single `A(z)S(k)` response than the other tested directions.
5. The descriptive six-direction raw-theory singular spectrum has a tiny sixth value, but **no intrinsic-rank claim is allowed** until observational whitening and a frozen rank threshold are applied.

## Immediate continuation

1. Merge/stabilize the comparison-readiness branch after all fresh hard runs are green.
2. Run the hard-evidence discriminant graph workflow from `main` and freeze its exact minimum hitting set.
3. Build the first **observationally whitened** cross-family comparison: map validated theory responses to measurable geometry/growth/lensing/shape channels and apply survey covariance/kernels.
4. Re-estimate local/global response rank under multiple family priors `pi` and report raw-theory vs data-whitened geometry separately.
5. Use the discriminant graph to choose the next independent real-data channel, with slip/lensing and small-scale transfer as high-value targets.
6. Resume G7 relation search only after observational-whitened rank/manifold stability; no discovery claim before G8.
