# DSIR RECOVERY LATEST — comparison-ready live overlay

**Date:** 2026-08-24  
**Read first:** `docs/RECOVERY_MANUAL.md`  
Then read this file, `docs/GATES.md`, `docs/STATUS.md`, `docs/RESEARCH_LOG.md`, `docs/RESEARCH_LOG_COMPARISON_2026-08-24.md`, `docs/PROVENANCE.md`, `docs/DISCRIMINANT_GRAPH.md`, and the response-basis specifications.

Hard boundary: **DSIR is separate from RTK. Do not modify, use, overwrite, or merge the RTK repository/project while continuing DSIR.**

---

## 1. Scientific status — major milestone

DSIR remains a reconstruction/meta-inference framework, **not yet a fundamental theory**, and no new law of nature is claimed.

However the project has now crossed the model-comparison readiness barrier:

\[
\boxed{\text{G3B = PASS in the v0.1 block-aware scope}}
\]

and Experiment 030 hard run `32772758188` returned

`PASS_READY_FOR_BLOCK_AWARE_MODEL_COMPARISON`, with `failures=[]`.

The first raw-theory cross-family comparison (Experiment 031) is complete. Two conditional-degeneracy separators have also passed fresh hard reruns after thresholds were frozen.

Current gates:

- **G1 PASS v0.1.1:** conservation/gauge contract and comoving total-matter response validated.
- **G2 PASS v0.1.1:** same-solver `r_Delta` basis and cross-solver bridge validated.
- **G3A PASS v0.1:** six control families embedded at background level.
- **G3B PASS v0.1 block-aware:** all six families have validated beyond-background response paths with explicit scale/channel masks.
- **G4 PASS:** synthetic low-rank recovery.
- **G5 PARTIAL:** whitening, missingness, family-prior protections exist; observationally whitened cross-family rank stress tests remain.
- **G6A/G6B PASS:** DESI DR2 AP and corrected DESI DR1 ShapeFit real-data response layers.
- **G7 OPEN:** raw-theory comparison is now unblocked, but no residual-law claim before observational whitening/rank stability.
- **G8 OPEN:** no discovery before a withheld physical prediction.

---

## 2. Frozen response basis v0.1.1

Redshift nodes:

`z={0.295,0.51,0.706,0.934,1.317,1.491,2.33}`.

Low-k nodes:

`k={0.001,0.003,0.01,0.03,0.1} h/Mpc`.

Background response:

\[
r_E(z;z_*)=\ln\left[\frac{H(z)/H(z_*)}{H_{ref}(z)/H_{ref}(z_*)}\right],\qquad z_*=0.51.
\]

For total matter,

\[
\delta_m=\frac{\sum_i\rho_i\delta_i}{\rho_m},\qquad
\theta_m=\frac{\sum_i(\rho_i+p_i)\theta_i}{\rho_m+p_m},\qquad
w_m=\frac{p_m}{\rho_m}.
\]

Production comoving contrast:

\[
\boxed{\Delta_m=\delta_m+3(1+w_m){\cal H}\frac{\theta_m}{k^2}}.
\]

Production perturbation response:

\[
\boxed{r_\Delta(k,z)=\ln\frac{P_{\Delta,model}^{S}(k,z)}{P_{\Delta,ref}^{S}(k,z)}}.
\]

`S` is the same solver lineage with matched numerical precision for model/reference. Absolute spectra from different solver vintages are not interpreted as dark-sector responses.

Cross-solver smooth-w hard bridge:

\[
\max|\Delta r_{bridge}|=2.3747404043\times10^{-10}<10^{-9}.
\]

---

## 3. Tangent, tangent-cone and manifold geometry

Do **not** identify SVD span with microscopic dimension.

For a smooth parameterized response manifold `r(theta)`, local geometry is set by the Jacobian

\[
J_{ai}=\frac{\partial r_a}{\partial\theta_i}.
\]

A curved one-parameter manifold can have global SVD rank greater than one. Therefore report separately:

- local tangent/Jacobian rank;
- global linear-span spectrum;
- curvature / tangent rotation.

If viability truncates parameter space, use a **tangent cone**, not an artificial symmetric derivative.

For IDE,

\[
Q=H(\alpha\rho_{idm}+\beta\rho_{iv}).
\]

Full-history positivity found all tested `alpha>0` points invalid because `rho_iv<0` at early times, while `alpha<0` and both beta signs remain valid. Thus use

\[
t_\alpha=\lim_{\alpha\to0^-}\frac{r(\alpha,0)}{\alpha}
\]

and a central beta tangent.

At the smallest calibrated step:

\[
\theta_H(\alpha,\beta)=10.8306^\circ,
\qquad
\theta_P(\alpha,\beta)=58.9338^\circ.
\]

Structure therefore separates the IDE axes much more strongly than the background.

---

## 4. Validated family patches

### C0 — LambdaCDM/GR

Common response origin; several independent zero-limit regressions pass.

### C1 — smooth non-phantom dark energy

One-sided local ray

\[
\epsilon_w=1+w\to0^+.
\]

p8 scan uses `epsilon_w={1e-4,1e-3,1e-2}`. The `1e-4` tangent is resolved; change at `1e-3` is about `0.12%` in L2 and `0.014 deg`.

### C2 — interacting vacuum

Pinned `kaeonikc/class_iv@ac627d54...`, with provenance-tracked compile-only brace repair and legacy toolchain semantics. IDE-S1 hard zero limit passes. Local physical geometry is the alpha/beta tangent cone described above.

### C3 — GDM

Pinned `s-ilic/gdm_class_public@4c87916...`, validated p8 precision. Zero-limit hard PASS actual `1.471014806e-6` under frozen `5e-6` threshold.

Sound-speed local scan (`w=cv2=0`) shows near-one-dimensional tangent behavior for small `cs2`; strong deformation bends the manifold. Positive control:

\[
r_\Delta(k,z)\approx-c_s^2 A(z)k^2
\]

with max relative L2 residual about `2.01e-3`.

Viscosity scan with dynamic shear gives a second microphysical parameter, but the low-k matter-power tangent is nearly the same:

\[
\boxed{\theta_P(c_s^2,c_v^2)=0.322616^\circ}
\]

and the two-axis local singular ratio is

\[
\sigma_2/\sigma_1=2.572\times10^{-3}.
\]

### C4 — thermal WDM

Never impute it into the low-k block. For the 3 keV control,

\[
r_T(0.1)=-3.46\times10^{-6},\qquad r_T(10)=-0.10375.
\]

Thus low-k is an identifiability blind block and the validated separator is a separate small-scale transfer block.

### C5 — full designer f(R)

Pinned official H-EFTCAMB `EFTCAMB/EFTCAMB@16d9c4e9f85751e30efd0a53b177941713078904`, branch `eftcamb`.

Designer configuration: `EFTflag=3`, `DesignerEFTmodel=1`, `EFTwDE=0`, parameter `EFTB0=B0`.

MG-S0 exact-GR hard PASS. MG-S1 common-baseline multi-z hard PASS. Production points:

`B0={1e-6,1e-5,1e-4,1e-3}`.

Maximum response amplitudes:

- `1e-6 -> 8.90411e-4`
- `1e-5 -> 6.21099e-3`
- `1e-4 -> 4.29053e-2`
- `1e-3 -> 1.54344e-1`

`B0=1e-7` is a transition control near the solver GR threshold, not a production atlas point.

---

## 5. Comparison readiness and first model comparison

Experiment 030 hard run:

- run ID `32772758188`;
- artifact digest `sha256:f110de1071cb11ce7e927b403f92002c766b03e384715ddd435af2c1c67c4131`;
- status `PASS_READY_FOR_BLOCK_AWARE_MODEL_COMPARISON`;
- `failures=[]`.

Six nonzero low-k response objects:

1. C1 smooth-w ray;
2. C2 IDE negative-alpha ray;
3. C2 IDE beta line;
4. C3 GDM cs2 ray;
5. C3 GDM cv2 ray;
6. C5 designer-f(R) ray.

C0 is the origin; C4 WDM is a separate small-scale block.

Raw unit-direction singular ratios:

\[
(1,0.52046,0.26140,0.20087,0.08299,5.9178\times10^{-4}).
\]

**Do not call this `R_model=5`.** No intrinsic-rank threshold was frozen and observational whitening is not yet applied.

Experiment 031 first comparison separates full `(z,k)` direction, leading scale shape, and leading time shape using

\[
R(z,k)=U\Sigma V^T,
\]

with leading approximation

\[
R\simeq\sigma_1A_1(z)S_1(k).
\]

Key findings:

- GDM cs2/cv2 full low-k angle `0.3226 deg`;
- GDM cs2 vs f(R) scale angle `0.07813 deg`;
- GDM cv2 vs f(R) scale angle `0.10169 deg`;
- corresponding time-mode angles `25.18 deg`, `25.49 deg`;
- full oriented GDM/f(R) angles `154.82 deg`, `154.51 deg`;
- smooth wDE vs GDM scale shapes differ by about `59.42 deg`;
- IDE beta is the least separable response (`rank-1 variance fraction ~0.92235`).

The first-comparison conditional-discriminant thresholds were frozen before a fresh rerun. Run `32774501126` passed with `failures=[]`.

---

## 6. Hard channel-discriminant results

### GDM cs2 vs cv2

Low-k matter power and Weyl amplitude are nearly degenerate, but metric slip is not.

After calibration, thresholds were frozen:

- Weyl angle `<=1 deg`;
- slip angle `>=120 deg`;
- combined equalized angle `>=45 deg`;
- tangent convergence `<=1 deg`;
- relative L2 change `<=2%`.

Fresh hard run `32774501069` PASS, `failures=[]`:

\[
\theta_W=0.300737^\circ,
\qquad
\theta_{slip}=137.943212^\circ,
\]

\[
\theta_{combined}=56.963212^\circ.
\]

Artifact digest:
`sha256:4197b9286e53481164f5a842796199ea94ded202d4e62f6cb232186247291d0e`.

Thus `metric_slip` is an established theory-level separator for this frozen C3 edge.

### GDM vs designer f(R)

The leading low-k **scale shape** is nearly identical, but time evolution / physical response sign separates the mechanisms.

Hard rerun `32774501126` PASS after thresholds were frozen:

\[
\theta_S(cs2,fR)=0.07813^\circ,
\qquad
\theta_t(cs2,fR)=25.18^\circ,
\]

\[
\theta_{full}^{oriented}(cs2,fR)=154.82^\circ,
\]

with analogous cv2 values `0.10169 deg`, `25.49 deg`, `154.51 deg`.

Thus `time_evolution_or_response_sign` is an established separator for the frozen scale-only degeneracy.

---

## 7. Hard-evidence discriminant graph v0.1

Experiment 033 graph CI run `32775055341` PASS.

Artifact digest:
`sha256:8a6e926dbea9c369ffb4d22bc9e73c7f33c59bcdf6507f30bd5bd6624376de06`.

Status:

`PASS_HARD_EVIDENCE_DISCRIMINANT_GRAPH_V0_1`.

Four established edges:

1. C0 vs 3 keV WDM in low-k -> `small_scale_transfer`;
2. GDM cs2 vs cv2 in low-k P/Weyl amplitude -> `metric_slip`;
3. GDM cs2 vs designer f(R) in leading scale shape -> `time_evolution_or_response_sign`;
4. GDM cv2 vs designer f(R) in leading scale shape -> same separator.

Exact minimum hitting set for this **current hard-established edge catalogue** is unique:

\[
\boxed{
\{\text{metric slip},\text{small-scale transfer},\text{time/sign evolution}\}
}
\]

with cardinality 3.

This is not a universal globally optimal survey design; it is the exact minimum for the current frozen evidence graph.

---

## 8. Real-data layer already available

DESI DR2 AP gives a calibration-free geometry response via

\[
F_{AP}=D_M/D_H.
\]

Flat-FLRW relative expansion identity:

\[
\frac{E(z_2)}{E(z_1)}=
\frac{F_{AP}(z_2)}{F_{AP}(z_1)}
\exp\left[-\int_{z_1}^{z_2}\frac{dz}{F_{AP}(z)}\right].
\]

Corrected DESI DR1 ShapeFit provides joint geometry/growth/shape covariance. The original Appendix-A growth/covariance numbers were superseded by a 2026 erratum and must not be used.

Measurement-induced AP/growth correlations are removed conditionally using

\[
r_g^\perp=r_g-C_{gN}C_{NN}^{-1}r_N.
\]

Current aggregate remains null-consistent:

\[
\chi^2\simeq5.53/5,\qquad p\simeq0.355.
\]

---

## 9. Exact continuation sequence — NEW MAIN FRONT

The next major stage is **observational whitening of the cross-family comparison**.

1. Stabilize/merge comparison PR #14 after final diff review and all hard workflows are green.
2. Preserve Experiment 033 graph result and provenance in `main`.
3. Build observation operators that map validated theory responses into actually measured channels. Keep separate:
   - DESI geometry / AP;
   - DESI growth/ShapeFit and shape;
   - lensing/Weyl/slip-like response channels;
   - WDM small-scale transfer / Ly-alpha-like block.
4. For each data block construct

\[
Z=C^{-1/2}\Delta O
\]

using the actual covariance/kernel for that block. Never use raw theory angles as observational significance.
5. Report raw-theory geometry and data-whitened geometry side by side.
6. Recompute pairwise separability, local Jacobian spectra and `R_model(pi)` under multiple defensible family priors.
7. Stress-test against removal of families, redshift/scale sub-blocks, solver precision and within-family sampling.
8. Use the hard discriminant graph to choose the most valuable next real-data channel.
9. Only after data-whitened manifold/rank stability may G7 residual-law search resume.
10. Any candidate relation must predict a withheld physical channel before G8 can PASS.

**Never claim discovery before G8.**
