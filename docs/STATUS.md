# DSIR status snapshot — 2026-08-25

DSIR remains a reconstruction/meta-inference framework, not a fundamental theory.

| Item | Status | Evidence |
|---|---|---|
| Project separation from RTK | PASS | dedicated DSIR repository; RTK excluded from this research line |
| Recovery/manual backup | PASS and live | `RECOVERY_MANUAL.md` + per-iteration `RECOVERY_LATEST.md` + `SCIENTIFIC_FINDINGS_REGISTER.md` + gates/log/provenance |
| Conservation/gauge contract | **PASS G1 v0.1.1** | Bianchi/exchange bookkeeping + hard Newtonian/synchronous comoving-matter regression |
| Response basis v0.1.1 | **PASS G2** | same-solver `P_Delta/r_Delta`; hard cross-solver bridge `1e-9` PASS |
| Six-family background atlas | **PASS G3A v0.1** | control embeddings and exact background intersections documented |
| Six-family beyond-background atlas | **PASS G3B v0.1 block-aware** | C1 smooth-w, C2 IDE tangent cone, C3 GDM cs2/cv2, C4 WDM small-scale block, C5 designer f(R), C0 reference |
| Comparison readiness | **PASS** | Exp.030 run `32772758188`, `PASS_READY_FOR_BLOCK_AWARE_MODEL_COMPARISON` |
| First cross-family comparison | **COMPLETE** | Exp.031; raw theory-space low-k comparison, no observational ranking |
| GDM cs2/cv2 low-k degeneracy | **HARD ESTABLISHED** | P angle `0.3226 deg`; Weyl amplitude also nearly collinear |
| GDM cs2/cv2 slip separator | **HARD PASS** | run `32774501069`: slip `137.943 deg`, equalized two-block `56.963 deg` |
| GDM cs2/cv2 background/AP null | **HARD PASS / Exp.037** | run `32783243120`: exact background equality and exact AP zero for audited w=0 closure rays |
| Designer f(R) B0 background/AP null | **HARD PASS / Exp.038** | final run `32786915513`: source-proven `EFTwDE=0 -> w=-1`; exact saved background/AP zero for `B0=0..1e-3` |
| GDM vs f(R) scale-only degeneracy | **HARD ESTABLISHED** | leading scale-mode angles `0.0781/0.1017 deg` |
| Finite-bin structure-growth operator | **HARD PASS / Exp.040** | run `32785987735`: endpoint error `1.11e-16`, constant mode `0`, linearity `9.77e-15` |
| GDM vs f(R) temporal separator | **HARD THEORY-LEVEL** | Exp.040 finite-bin growth `16.05/17.28 deg` acute vs scale-only `0.078/0.102 deg`; full structure `25.18/25.49 deg` |
| IDE alpha/beta channel migration | **HARD ESTABLISHED** | AP `9.0379 deg` acute -> finite-bin growth `29.3978 deg` -> full structure `58.9338 deg` |
| Smooth-w vs IDE-alpha channel reversal | **HARD ESTABLISHED** | AP `72.8035 deg`, full structure `52.1943 deg`, finite-bin growth only `10.3106 deg` |
| WDM low-k blindness / high-k separator | **HARD ESTABLISHED** | 3 keV: `r_T(0.1)=-3.46e-6`, `r_T(10)=-0.10375` |
| Synthetic latent-rank recovery | PASS | injected rank 3 recovered with corrected global noise edge |
| Whitening robustness | PASS tested suite; **G5 PARTIAL** | 30/30 synthetic coordinate/rescaling cases + real-covariance shape/AP partial blocks; family-complete joint whitening remains |
| First cross-family real-covariance whitening | **PARTIAL PASS / Exp.034** | run `32777716140`: corrected DESI DR1 `m+n` marginal block |
| Shape-proxy adequacy | **LIMIT FOUND** | GDM/f(R) finite-node ShapeFit residual about 36%; no full DESI distinguishability claim |
| Calibration-free AP operator | **HARD PASS / Exp.035** | run `32778635058`: direct wCDM bridge `1.00e-14`; calibration mode cancels |
| C1/C2 production AP geometry | **HARD PASS / Exp.036** | run `32782545098`; exact full-background artifacts + corrected DESI `DH/DM` marginal weighting |
| Low-z AP geometry atlas coverage | **SUBSTANTIALLY CLOSED** | C0 origin, C1/C2 hard nonzero directions, C3/C5 hard exact-null cells; C4 WDM remains intentionally separate until a geometry contract is defined |
| ShapeFit growth/RSD definition | **PROTOCOL FROZEN / Exp.039** | use `f_sigma_s8`, `s=r_d/r_d_ref`; scalar compression requires density-velocity representability audit |
| C5 scalar-growth representability | **HARD FAIL OF EXACT SCALAR COMPRESSION / Exp.041 PASS** | run `32791510072`: GR/B0 floor `~1.4e-10`; production `D_RSD=5.18e-6..8.81e-4` at `kmax=0.24`; all production points remain nonzero at `kmax=0.10` |
| C5 weighted scale variation of growth ratio | **HARD ESTABLISHED / Exp.041** | `CV_w(g)` about `0.23%,1.39%,2.97%,2.96%` for `B0=1e-6..1e-3`, versus `~0.0012%` GR/B0 floor |
| CAMB printed growth-log precision | **LIMIT / REJECTED FOR TANGENTS** | four-decimal summaries quantize small-B0 response; Exp.041 therefore uses independent `E24.16` transfer output |
| C3 density-velocity/RSD bridge | **EXPLORATORY / Exp.042** | synchronous velocity output found gauge-ill-conditioned for RSD; N-body-gauge transfer extension is being audited before any C3 RSD claim |
| Theory-catalog prior sensitivity | CONTROLLED FAILURE MODE | report `R_model(pi)`; family-balanced sampling implemented |
| Missing-response handling | PASS method gate | validity masks/common subspaces; zero only after explicit theory/solver validation |
| DESI DR2 AP response | PASS G6A | calibration-free AP and relative expansion |
| DESI DR1 corrected ShapeFit response | PASS G6B | geometry-growth-shape covariance from 2026 erratum |
| Conditional innovation | PASS preparation | aggregate null-consistent (`chi2~5.53/5`, `p~0.355`) |
| IDE solver/manifold | PASS + calibrated cone | alpha positivity boundary; structure `58.93 deg`; AP `9.04 deg`; temporal growth `29.40 deg` alpha/beta |
| GDM solver/manifold | PASS + calibrated two-axis patch | P cs2/cv2 nearly collinear; AP exact-null; temporal growth still only `1.334 deg`; slip is needed; RSD velocity audit in progress |
| H-EFTCAMB designer f(R) | **MG-S0 + MG-S1 + Exp.038 + Exp.041 PASS** | exact GR limit, exact B0 AP-null, and hard nonzero scale-dependent density-velocity defect |
| Discriminant graph v0.1 | **HARD PASS** | Exp.033 run `32775055341`; unique current separator set `{slip, small-scale transfer, time/sign}` |
| Scientific findings register | **LIVE** | through F13; status-preserving updates every substantive iteration |
| New residual law | **OPEN G7** | family-complete observation-space growth/shape/window kernels and rank stability still incomplete |
| Withheld prediction | **OPEN G8** | mandatory before discovery |

## Current comparison findings

1. **Exact channel-null structure repeats across different physics.** GDM `cs2/cv2` and designer-f(R) `B0` are exactly background/AP-null in their frozen constructions while remaining perturbation-active.
2. **C5 now gives a stronger cross-channel example:** the very same `B0` direction that is exactly AP-null is not representable by one exact scale-independent density-velocity amplitude. Experiment 041 places production `D_RSD` four to six orders above the GR/B0=0 numerical floor.
3. **The RSD defect has a direct physical meaning:** `D_RSD=Var_w[g]/<g^2>_w` for `g=Theta/delta`; hence `sqrt(D/(1-D))` is the weighted fractional scale variation of the growth ratio.
4. **Degeneracies migrate between operators rather than disappearing monotonically.** Smooth-w vs IDE alpha is strongly separated in AP (`72.80 deg`) but nearly degenerate in finite-bin temporal growth (`10.31 deg`), while IDE alpha vs GDM changes in the opposite direction (~`25 deg` full structure to ~`61 deg` temporal growth).
5. **IDE alpha/beta forms a three-channel ladder:** AP `9.04 deg` -> temporal growth `29.40 deg` -> full structure `58.93 deg`.
6. **GDM cs2/cv2 remains a hard microphysical degeneracy in density/growth:** `0.323 deg` raw low-k structure and `1.334 deg` finite-bin growth. Metric slip remains the established separator. The new velocity audit must use a gauge-safe transfer convention; synchronous `theta_m` is not admissible as an RSD observable.
7. **GDM/f(R) scale lookalikes are separated by time:** scale-only `0.078-0.102 deg`, finite-bin growth `16.05-17.28 deg`, full structure `25.18-25.49 deg`.
8. The finite-node ShapeFit `m+n` proxy is not universal: about `36%` representation residual for GDM/f(R), so proxy angles are not DESI distinguishability claims.
9. Descriptive singular spectra remain non-rank claims. **No intrinsic `R_model` claim is allowed** before family-complete observation operators, full covariance whitening, frozen null/rank thresholds, and prior stress tests.

## Immediate continuation

1. Finish the C3 GDM density-velocity exploration using the pinned solver's built-in N-body-gauge transfer transformation; explicitly reject synchronous-gauge velocity ratios as an RSD estimator.
2. If C3 shows a meaningful velocity separator or nonzero `D_RSD`, freeze a new independent confirmatory threshold before rerunning the target output.
3. Extend the Experiment-039 density/velocity representability audit to C1 smooth-w and C2 IDE with matched pinned-solver conventions; do not mix solver velocity definitions silently.
4. For every family compute the correct `s=r_d/r_d_ref` and `R=s*8 h^-1 Mpc` before admitting a scalar `f_sigma_s8` coordinate.
5. Replace/calibrate the finite-node `m+n` proxy with a survey/window-aware shape response or propagate compression-model error.
6. Then form the corrected joint ShapeFit block `Z=C^{-1/2} Delta O` on valid common observable subspaces.
7. Stress-test response spectra under family priors `pi`, channel removal, solver precision, covariance perturbations, and within-family sampling before any `R_model(pi)` statement.
8. Continue observational lensing/slip and small-scale-transfer blocks because the hard discriminant graph identifies them as independent high-value separators.
9. Resume G7 residual-law search only after observationally whitened manifold/rank stability; no discovery claim before G8.
