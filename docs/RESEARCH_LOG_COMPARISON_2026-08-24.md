# DSIR comparison-stage research log — 2026-08-24

This addendum continues `docs/RESEARCH_LOG.md`. Scientific claim status is controlled by `docs/GATES.md`.

## Response basis and solver readiness

- Response basis v0.1.1 was frozen on the gauge-safe comoving total-matter response `r_Delta` rather than raw gauge-specific density variables.
- Cross-solver smooth-w response bridge passed a pre-frozen `1e-9` hard tolerance; matched-p8 mismatch was `2.3747404043e-10`.
- GDM zero-limit hard regression passed (`1.471014806e-6 < 5e-6`).
- IDE zero-coupling hard regression passed (`P(k)` core < `2e-8`, semantic background < `2e-12`).
- H-EFTCAMB MG-S0 exact-GR hard gate passed; MG-S1 common-baseline multi-z production manifold passed for `B0={1e-6,1e-5,1e-4,1e-3}`.

## Negative / corrective results retained

1. Raw Newtonian/synchronous `mPk` comparison at default precision produced a false mismatch around `9.84e-5`; high precision and explicit comoving construction resolved the issue. This prevented a gauge/numerical direction from entering the atlas.
2. Pushing only `start_small_k_at_tau_c_over_tau_h` earlier than `1e-6` worsened GDM zero-limit behavior; it is not a monotonic accuracy control.
3. `class_iv` pinned source required a compile-only brace repair and legacy toolchain semantics. These are tracked as implementation caveats, not physics modifications.
4. First H-EFTCAMB parallel build failed because of an upstream Makefile dependency race. Serial upstream-style build succeeds.
5. First MG-S1 multi-z run failed because CAMB requires decreasing redshift order; shell `tee` also initially masked the solver exit code without `pipefail`. Both infrastructure issues were corrected without changing the physical grid.
6. CAMB text matter-power output introduced ppm-level quantization; high-precision output audit isolated this and prevented an overstrong numerical precision claim.
7. IDE `alpha>0` points were solver-computable but violated full-history `rho_iv>=0`; they were marked physically invalid rather than imputed. The local object is therefore a tangent cone, not a symmetric tangent plane.

## Experiment 025 — GDM sound-speed manifold geometry

For `w=cv2=0` and small constant `cs2`, the local response is almost one-dimensional:

`local sigma2/sigma1 = 4.40e-5`.

Including `cs2=1e-4` bends the one-parameter response manifold, yielding global `sigma2/sigma1 ~2.50e-2` and about `11.3 deg` tangent rotation. Therefore global SVD span is not intrinsic parameter dimension.

Positive control:

`r_Delta ~ -cs2 * A(z) * k^2`

with max relative L2 residual about `2.01e-3` in the local regime.

## Experiment 027 — IDE tangent cone

Pinned interacting-vacuum convention:

`Q = H(alpha rho_idm + beta rho_iv)`.

Full-history positivity masks all sampled `alpha>0` points. Physical local directions are a left-sided alpha ray and a central beta line.

At the smallest step:

- background-H angle alpha/beta = `10.8306 deg`;
- low-k structure angle alpha/beta = `58.9338 deg`.

Thus growth/structure provides much stronger local discrimination than background expansion for these two interaction directions.

## Experiment 028 — GDM viscosity and local two-axis Jacobian

With dynamic shear and `w=cs2=0`, the viscosity axis is itself nearly one-dimensional (`sigma2/sigma1=1.034e-4`).

Sound speed and viscosity are almost collinear in low-k matter power:

`angle(cs2,cv2)=0.322616 deg`,

and the two-axis Jacobian has `sigma2/sigma1=2.572e-3`.

This is an explicit example of different microphysical parameters collapsing onto almost one observable direction.

## Experiment 030 — comparison-readiness hard gate

Pre-frozen readiness conditions required:

- six finite nonzero low-k response objects;
- GDM cs2/cv2 angle <=1 deg;
- IDE alpha/beta structure angle >=30 deg;
- WDM low-k invisibility plus high-k response;
- resolved C1 local tangent;
- C5 production `B0>=1e-6`.

GitHub Actions run `32772758188` PASS, `failures=[]`, status `PASS_READY_FOR_BLOCK_AWARE_MODEL_COMPARISON`.

This is the point at which DSIR became ready for systematic block-aware model comparison.

## Experiment 031 — first cross-family comparison

Six validated low-k directions were compared as full 35-cell responses and via leading scale/time modes.

Important full-response angles:

- GDM cs2 vs cv2: `0.3226 deg`;
- IDE negative-alpha vs GDM cs2: `24.9345 deg`;
- smooth wDE vs GDM cs2: `59.8042 deg`;
- smooth wDE vs IDE beta: `80.5209 deg`;
- GDM cs2 vs designer f(R): oriented `154.8182 deg`;
- GDM cv2 vs designer f(R): oriented `154.5119 deg`.

Leading scale-mode angles:

- `cs2` vs `cv2`: `0.02436 deg`;
- `cs2` vs f(R): `0.07813 deg`;
- `cv2` vs f(R): `0.10169 deg`.

The GDM/f(R) scale shapes are nearly identical over the current five low-k nodes, but their time modes differ by about `25 deg` and the full physical response has opposite orientation/sign.

A hard rerun after frozen thresholds, run `32774501126`, PASS with `failures=[]`.

The normalized raw-theory six-direction singular ratios are

`(1,0.52046,0.26140,0.20087,0.08299,5.9178e-4)`.

No intrinsic-rank threshold was frozen. It is forbidden to report this as `R_model=5`.

## Experiment 032 — GDM Weyl/slip separator

Calibration found that GDM sound speed and viscosity remain nearly collinear in Weyl amplitude but rotate strongly in metric slip.

Thresholds were frozen before a fresh rerun:

- Weyl angle <=1 deg;
- slip angle >=120 deg;
- combined equalized angle >=45 deg;
- tangent convergence <=1 deg;
- relative L2 change <=2%.

Hard run `32774501069` PASS with `failures=[]`:

- Weyl angle `0.300737 deg`;
- slip angle `137.943212 deg` at `1e-7`;
- combined equalized angle `56.963212 deg`.

Thus metric slip is a proven theory-level separator for the frozen GDM cs2/cv2 degeneracy. This is not yet proof that a real survey can measure the separation.

## Experiment 033 — hard-evidence discriminant graph v0.1

Only edges with hard evidence are admitted.

Current edges:

1. LambdaCDM vs 3 keV WDM in low-k -> `small_scale_transfer`;
2. GDM cs2 vs cv2 in low-k P/Weyl amplitude -> `metric_slip`;
3. GDM cs2 vs designer f(R) in leading scale shape -> `time_evolution_or_response_sign`;
4. GDM cv2 vs designer f(R) in leading scale shape -> same separator.

Graph CI run `32775055341` PASS with status `PASS_HARD_EVIDENCE_DISCRIMINANT_GRAPH_V0_1`.

Exact unique minimum hitting set:

`{metric_slip, small_scale_transfer, time_evolution_or_response_sign}`

with cardinality 3.

This result is only for the current hard-established edge catalogue, not a universal observing strategy.

## Next research front

Move from raw theory-response geometry to **observationally whitened geometry**:

1. define observation operators / kernels for DESI geometry-growth-shape, lensing/slip-like channels and WDM small-scale blocks;
2. map each validated theory response into measurable coordinates;
3. whiten with the corresponding covariance `C^{-1/2}`;
4. compare raw-theory and data-whitened pairwise geometry separately;
5. estimate local/global rank and `R_model(pi)` only after whitening and explicit rank-threshold calibration;
6. use the hard discriminant graph to prioritize new independent data channels;
7. only then reopen G7 law discovery; no discovery before G8 withheld prediction.
