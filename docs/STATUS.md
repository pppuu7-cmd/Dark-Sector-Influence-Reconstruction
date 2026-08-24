# DSIR status snapshot — 2026-08-25

DSIR remains a reconstruction/meta-inference framework, not a fundamental theory.

| Item | Status | Evidence |
|---|---|---|
| Project separation from RTK | PASS | dedicated DSIR repository; RTK excluded from this research line |
| Recovery/manual backup | PASS and live | `RECOVERY_MANUAL.md` + per-iteration `RECOVERY_LATEST.md` + `SCIENTIFIC_FINDINGS_REGISTER.md` + gates/log/provenance |
| Conservation/gauge contract | **PASS G1 v0.1.1** | Bianchi/exchange bookkeeping + hard Newtonian/synchronous comoving-matter regression |
| Response basis v0.1.1 | **PASS G2** | same-solver `P_Delta/r_Delta`; hard cross-solver bridge `1e-9` PASS |
| Six-family background atlas | **PASS G3A v0.1** | control embeddings and exact background intersections documented |
| Six-family beyond-background atlas | **PASS G3B v0.1 block-aware** | C1 smooth-w, C2 IDE tangent cone, C3 GDM cs2/cv2, C4 WDM small-scale block, C5 full designer-f(R), C0 reference |
| Comparison readiness | **PASS** | Exp.030 run `32772758188`, `failures=[]`, status `PASS_READY_FOR_BLOCK_AWARE_MODEL_COMPARISON` |
| First cross-family comparison | **COMPLETE** | Exp.031; raw theory-space low-k comparison, no observational ranking |
| GDM cs2/cv2 low-k degeneracy | **HARD ESTABLISHED** | P angle `0.3226 deg`; Weyl amplitude also nearly collinear |
| GDM cs2/cv2 slip separator | **HARD PASS** | run `32774501069`: slip `137.943 deg`, equalized two-block angle `56.963 deg` |
| GDM cs2/cv2 background/AP null | **HARD PASS / Exp.037** | run `32783243120`: all audited background tables exactly equal to C3 reference; `max_relative_H=0`, `max_abs Delta ln(DH/DM)=0` |
| GDM vs f(R) scale-only degeneracy | **HARD ESTABLISHED** | scale-mode angles `0.0781/0.1017 deg` |
| GDM vs f(R) time/sign separator | **HARD PASS** | run `32774501126`: time-mode `25.18/25.49 deg`, full oriented `154.82/154.51 deg` |
| WDM low-k blindness / high-k separator | **HARD ESTABLISHED** | 3 keV: `r_T(0.1)=-3.46e-6`, `r_T(10)=-0.10375` |
| Synthetic latent-rank recovery | PASS | injected rank 3 recovered with corrected global noise edge |
| Whitening robustness | PASS tested suite; **G5 PARTIAL** | 30/30 synthetic coordinate/rescaling cases + real-covariance shape/AP partial blocks; family-complete joint whitening remains |
| First cross-family real-covariance whitening | **PARTIAL PASS / Exp.034** | run `32777716140`: `PASS_PROXY_OBSERVATIONAL_WHITENING_SHAPE_BLOCK`; corrected DESI DR1 `m+n` marginal errors |
| Shape-proxy adequacy | MIXED / LIMIT FOUND | smooth-w residual <=1.33%; IDE <=5.87%; GDM/f(R) finite-node ShapeFit residual about 36%, so no full DESI distinguishability claim |
| Calibration-free AP operator | **HARD PASS / Exp.035** | run `32778635058`: direct wCDM bridge `1.00e-14`, calibration-mode residual `7.83e-15`, DH/DM sign identity exact at reported precision |
| C1/C2 production AP geometry | **HARD PASS / Exp.036** | run `32782545098`: `PASS_AP_FAMILY_GEOMETRY_V0_1`; exact frozen full-background artifacts and corrected DESI `DH/DM` marginal weighting |
| IDE alpha/beta AP degeneracy | **HARD ESTABLISHED / Exp.036** | whitened oriented angle `170.9621 deg`, acute angle `9.03790 deg`; structure-block angle remains `58.9338 deg` |
| AP production-history coverage | **PARTIAL, IMPROVED** | C1/C2 full histories validated; C3 AP cell now hard-zero; C5 designer-f(R) numerical background/AP audit remains before family-complete geometry |
| Theory-catalog prior sensitivity | CONTROLLED FAILURE MODE | report `R_model(pi)`; family-balanced sampling implemented |
| Missing-response handling | PASS method gate | validity masks/common subspaces; zero allowed only after explicit theory/solver validation such as Exp.037 |
| DESI DR2 AP response | PASS G6A | calibration-free AP and relative expansion |
| DESI DR1 corrected ShapeFit response | PASS G6B | geometry-growth-shape covariance from 2026 erratum |
| Conditional innovation | PASS preparation | aggregate null-consistent (`chi2~5.53/5`, `p~0.355`) |
| IDE solver/manifold | PASS + calibrated cone | hard zero limit; alpha positivity boundary; alpha/beta structure angle `58.93 deg`; AP angle `9.04 deg` acute |
| GDM solver/manifold | PASS + calibrated two-axis patch | zero limit hard PASS; cs2/cv2 nearly collinear in P; background/AP exactly null for audited w=0 closure rays |
| H-EFTCAMB designer f(R) | **MG-S0 + MG-S1 PASS** | exact GR limit and common-baseline production `B0=1e-6..1e-3`; AP-zero audit still open |
| Discriminant graph v0.1 | **HARD PASS** | Exp.033 run `32775055341`; unique minimum current separator set has three channels |
| Scientific findings register | **LIVE** | `docs/SCIENTIFIC_FINDINGS_REGISTER.md`; status-preserving updates every substantive iteration |
| New residual law | **OPEN G7** | observational whitening has started but full family-complete kernels/rank stability are not yet established |
| Withheld prediction | **OPEN G8** | mandatory before discovery |

## Current comparison findings

1. GDM sound speed and viscosity are nearly the same low-k matter-power direction; their five-bin DESI `m+n` proxy histories also remain nearly collinear after marginal covariance whitening (`0.189582 deg`). Metric slip remains the established theory-level separator.
2. **Experiment 037 sharpens the GDM picture:** with frozen `w_gdm=0`, all sampled nonzero `cs2/cv2` closure directions have exactly the same saved background as the reference and exactly zero AP response, despite their strong nonzero perturbation responses. This is a hard example of channel-null/block-sparse influence.
3. GDM pressure/viscosity and designer f(R) have almost identical leading raw scale shapes, but differ in time/sign. In the first whitened `m+n` proxy their acute history angle is about `23 deg`; however the ShapeFit-basis residual is about `36%`, so this is not promoted to a DESI distinguishability claim.
4. Smooth non-phantom wDE has a much flatter k-dependence than GDM/f(R), and its finite-node ShapeFit representation is much better behaved (maximum residual about `1.33%`).
5. Experiment 036 hard-confirms a complementary IDE degeneracy: negative-alpha and beta are almost antiparallel in the DESI AP geometry block (`170.9621 deg` oriented; `9.03790 deg` acute), despite their much larger structure-block separation (`58.9338 deg`).
6. The exact AP identity proves that response-basis anchoring `r_E(z;z*=0.51)` does not discard AP information: any additive constant in log E cancels from `F_AP=E chi`.
7. The repeated GDM, GDM/f(R), WDM, and IDE examples support—but do not prove universally—the DSIR meta-hypothesis that model identity is carried by a multi-channel influence trajectory. Experiment 037 further suggests that this trajectory can be block-sparse, including exact channel nulls.
8. The five-bin unit-direction shape spectrum `(1,0.20559,0.01065,0.00195,1.37e-6)` is descriptive only. **No intrinsic-rank claim is allowed** without family-complete observation operators, full covariance whitening, frozen null/rank thresholds, and prior stress tests.

## Immediate continuation

1. Audit C5 designer f(R) background equivalence (`EFTwDE=0`) numerically. The existing frozen artifact preserves the configs and indicates background writing was enabled, but does not expose a clearly usable preserved background history; create a dedicated pinned H-EFTCAMB background/AP audit if necessary.
2. Only after C5 audit form the family-complete AP geometry cell; keep C4 WDM in its separate small-scale block unless a validated geometry response is explicitly defined.
3. Build a family-complete gauge-safe `f_sigma_s8` growth operator using the corrected ShapeFit convention and validated total-matter response lineage.
4. Replace/calibrate the finite-node `m+n` proxy with a survey/window-aware shape response and propagate compression-model error.
5. Then form the full corrected ShapeFit block `Z=C^{-1/2} Delta O` and compare raw-theory versus data-whitened geometry side by side.
6. Stress-test local/global response spectra under family priors `pi`, channel removal, solver precision, and within-family sampling before assigning any `R_model(pi)` statement.
7. In parallel, prioritize observational lensing/slip and small-scale-transfer blocks because the hard discriminant graph identifies them as high-value independent separators.
8. Resume G7 residual-law search only after observationally whitened manifold/rank stability; no discovery claim before G8.
