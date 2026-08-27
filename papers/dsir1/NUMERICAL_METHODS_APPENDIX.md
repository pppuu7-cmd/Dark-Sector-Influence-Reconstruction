# DSIR-I numerical methods appendix — v0.1

This appendix freezes the numerical conventions required to reproduce the manuscript-level DSIR-I claims. Provider identity is bound by immutable source/run/artifact provenance rather than by a floating package-name label. The central mappings are recorded in `PROVENANCE_MATRIX.md` and `SUPPORT_OPERATOR_PROVENANCE.md`.

## A. Analysis layers and comparison object

DSIR separates:

1. **theory/provider layer** — a concrete model realization and solver/provider contract;
2. **physical response layer** — response functions on explicitly stated domains;
3. **observational operator layer** — survey/window projection and support restriction;
4. **statistical quotient layer** — covariance whitening and nuisance projection.

No manuscript result may skip a failed earlier layer.

For theory parameter state `theta`, write the physical response vector as

\[
r(\theta)\in\mathbb R^n.
\]

For a retained channel block `B`, the eventual observational signature is

\[
s_B(\theta)=A_Br(\theta),\qquad A_B=Q_BW_BK_B,
\]

where `K_B` is the physical/window operator, `W_B` the covariance whitener and `Q_B` the retained nuisance quotient. DSIR-I theory-space morphology results precede the final covariance/nuisance quotient unless explicitly labelled otherwise.

## B. Reference and response coordinates

The common response origin is LambdaCDM/GR under matched provider settings.

### B.1 Background response

The anchored relative expansion coordinate is

\[
r_E(z;z_*)=\ln\left[
\frac{H(z)/H(z_*)}{H_{\rm ref}(z)/H_{\rm ref}(z_*)}
\right],
\]

with frozen anchor

\[
z_*=0.51.
\]

### B.2 Low-k structure response

The production low-k matter coordinate is the same-provider comoving total-matter power response

\[
r_\Delta(k,z)=
\ln\left[
\frac{P^{S}_{\Delta,{\rm model}}(k,z)}
     {P^{S}_{\Delta,{\rm ref}}(k,z)}
\right],
\]

where model and reference share solver/provider lineage `S` and matched numerical settings wherever the comparison contract requires this.

Gauge-specific density variables are not substituted for a universal matter coordinate. Provider certification and gauge/conservation regression are treated separately from morphology analysis.

### B.3 Metric blocks

Where defined and certified, independent Weyl-amplitude and metric-slip response blocks are retained rather than inferred from matter power by a hidden GR closure. Signed Weyl--matter cross semantics are preserved by provider contracts.

## C. Frozen grids and block awareness

### C.1 Common low-k grid

The main C1/C2/C3/C5 low-k response grid is

\[
z=\{0.295,0.51,0.706,0.934,1.317,1.491,2.33\},
\]

\[
k=\{0.001,0.003,0.01,0.03,0.1\}\;h\,{\rm Mpc}^{-1}.
\]

This is a `7 x 5` grid.

### C.2 WDM high-k block

The thermal-WDM time atlas is deliberately separate:

\[
k=\{0.1,0.3,1,3,10,20\}\;h\,{\rm Mpc}^{-1},
\]

on the same seven redshift nodes. It is not zero-padded into the low-k block.

### C.3 Missing/undefined cells

A missing model/channel combination is a mask, not the number zero. Cross-family statistics are evaluated only on explicit common support. This prevents absent high-k or metric information from manufacturing artificial null directions or rank.

## D. Additive scale-time projection

For a response matrix `R(z,k)`, DSIR uses the two-way additive projection

\[
R(z,k)=\mu+T(k)+\tau(z)+I(z,k),
\]

where `I` is the residual after the best additive projection under the frozen Euclidean grid norm.

The interaction-power fraction is

\[
\chi_I=\frac{\|I\|_2^2}{\|R\|_2^2}.
\]

This decomposition is a representation diagnostic. `I` is not interpreted as a fundamental fourth dark-sector degree of freedom.

For pairwise normalized response-shape difference `d`, the localized interaction fraction is

\[
\eta_I=\frac{\|d_I\|_2^2}{\|d\|_2^2}.
\]

`eta_I` is always interpreted together with an absolute distance or angle: a large fraction of a tiny separation is still a tiny separation.

## E. Response angles and trajectory geometry

For non-zero response vectors `a,b`, the Euclidean normalized angle is computed from

\[
\cos\theta=\frac{a\cdot b}{\|a\|_2\|b\|_2}.
\]

The manuscript distinguishes oriented full-response angles from acute/subspace comparisons; orientation is never silently discarded when response sign is physically informative.

For a one-parameter response family,

\[
u(\theta)=\frac{r(\theta)}{\|r(\theta)\|_2},
\]

and

\[
\frac{du}{d\theta}=\frac{(I-uu^T)}{\|r\|_2}\frac{dr}{d\theta}.
\]

Finite-amplitude turning angles are sampled direction changes, not claimed as continuous Frenet curvature. Their purpose is to separate microscopic parameter count from linear representation rank.

## F. Finite-amplitude and grid-robustness protocol

Local tangent morphology is not promoted automatically to a finite-family statement. Exp047A recomputes the same response geometry on immutable finite-amplitude products and reports sampled `chi_I` envelopes and direction turns.

Grid robustness is evaluated deterministically by deleting each frozen node separately:

- five leave-one-`k` grids;
- seven leave-one-`z` grids.

No post-hoc scientific stability threshold is invented from the resulting plot. The paper reports the observed 12/12 tier-order preservation and separately notes node-sensitive absolute values such as smooth-w at the lowest-k node.

## G. Withheld and prospective tests

Three distinct statuses are maintained:

1. **withheld interpolation within an already represented family** — e.g. WDM cutoff masses;
2. **withheld mechanism/family** — e.g. DCDM temporal localization;
3. **prospective falsification** — a frozen relation evaluated on withheld IDM-DR and failed.

A family examined after a failed withheld test cannot be relabelled “fresh withheld” for a new law chosen from that failure.

## H. Provider certification and failure preservation

Provider correction is never performed by changing a failed threshold after viewing the result.

### H.1 C3 GDM provider chain

The original target-grid physical-power bridge Exp070A remains failed with a reconstruction defect of approximately `0.0475359`. Mechanism audit localized the defect to the interpolation construction. A separately frozen native-grid provider Exp070C subsequently passed matter-power closure at approximately `2.81e-14` and same-mode coherence at machine precision.

These are different contracts. Exp070C does not retroactively convert Exp070A into a PASS.

### H.2 C5 designer-f(R) provider chain

The original q=1 C5 bridge remains failed at an exact-GR-limit matter-power miss of approximately `5.3064e-6` against the unchanged `5e-6` criterion. A prospectively frozen accuracy ladder showed monotone convergence, after which a separately frozen q=3 provider passed the same physical boundary without floor subtraction, renormalization or threshold relaxation.

### H.3 Reproducibility identity

For paper-level numerical claims, provider identity is bound by the corresponding:

- source/implementation commit where available;
- GitHub Actions workflow run;
- immutable artifact ID;
- artifact SHA256 digest;
- frozen scientific criterion.

These bindings are enumerated in the manuscript provenance ledgers.

## I. Observation-route support eligibility

The support selector `M_supp` is applied before covariance whitening. For an eligible row set,

\[
K_{B,{\rm supp}}=M_{\rm supp}K_B,
\]

\[
C_{B,{\rm supp}}=M_{\rm supp}C_BM_{\rm supp}^{T},
\]

then

\[
W_{B,{\rm supp}}=C_{B,{\rm supp}}^{-1/2},
\qquad
A_{B,{\rm supp}}=Q_{B,{\rm supp}}W_{B,{\rm supp}}K_{B,{\rm supp}}.
\]

No covariance or nuisance quantity is used to rescue a support-ineligible coordinate.

### I.1 Frozen support threshold

For the relevant observation-route audits, the future physical-support criterion is retained at

\[
f_{\rm invalid}\le0.05,
\]

with minimum retained dimension 15 where specified by the corresponding preregistration.

### I.2 Finite positive normalizer

A positive support fraction

\[
f_{\rm out}=\frac{\int_{\Omega\setminus D}|\mathcal K|d\mu}
{\int_{\Omega}|\mathcal K|d\mu}
\]

is defined only if the denominator is finite and non-zero. Exp073L demonstrates a frozen route for which this condition fails. No retrospective ultraviolet cutoff or fiducial-power weighting is introduced to force normalizability.

### I.3 Exact realized-operator provenance

A finite operator *class* is not sufficient. The exact public real-data realization used for a support calculation must be reconstructible from frozen public inputs. This distinction is preserved by the Exp073M -> Exp073N -> Exp073O chain:

- Exp073M: finite-positive operator-class candidate;
- Exp073N: mandatory exact-realization provenance FAIL before support scoring;
- Exp073O: prospectively selected public DES Y1 replacement under unchanged future support criteria.

### I.4 Public-input and pixelization reproduction

The replacement route then closes public-input prerequisites in frozen order:

- Exp073P2: exact release-object SHA256 binding;
- Exp073S0: redMaGiC mask and lens/source `n(z)` reproduction;
- Exp073R0: raw-row/HEALPix equivalence on 131,072 prospectively sampled rows, `Nside=4096`, `coords=C`, exact in all four source bins.

Exp073R0 explicitly has `science_gate_scored=false`; it is not the physical-support result.

## J. Statistical rank and whitening boundary

Noise-edge rank claims are defined only after covariance whitening. `R_obs` denotes the dimension distinguishable by the observational response operator after whitening; `R_model` refers to the dimension occupied by viable theory manifolds after projection into identifiable space. These are not inferred from a raw unwhitened singular spectrum.

A finite theory catalogue also induces a sampling prior. Any future global model-rank statement must therefore report sensitivity to defensible family weighting/stratification rather than treating catalogue multiplicity as a neutral prior.

## K. Nuisance quotient and discovery hierarchy

Candidate physical relations are searched only after conditioning/removing exact definitions, conservation/Bianchi identities, shared calibration directions, gauge/frame artifacts and retained nuisance tangent directions.

For Gaussian residual conditioning, the project-level working form is

\[
r_{t\perp}=r_t-C_{tN}C_{NN}^{-1}r_N,
\]

with conditional variance

\[
C_{tt}-C_{tN}C_{NN}^{-1}C_{Nt}.
\]

This is a statistical innovation coordinate, not automatically a causal physical law.

The claim hierarchy remains:

`control identity -> identifiability pattern -> empirical residual relation -> predictive law candidate -> physical model candidate`.

DSIR-I stops before any universal-law/discovery claim.

## L. Machine precision, repeatability and plotting

Where repeatability/state controls apply, manuscript-level provider certifications use their prospectively frozen tolerances, commonly at or near `1e-12` for deterministic state/repeatability checks. Physical closure tolerances are contract-specific and are never replaced by a single universal numerical epsilon.

Publication plots are generated from frozen repository products by scripts under `papers/dsir1/figures/`. Scientific values are recomputed or hard-checked before rendering, and output PDF/PNG/SVG files receive SHA256 hashes in the CI build artifact. Display-only choices may change; scientific masks, response orientation, domains, frozen thresholds and provider identity may not change silently.

## M. Reproduction entry points

A submission/reproduction audit should start from:

- `papers/dsir1/CLAIMS_LEDGER.md`;
- `papers/dsir1/PROVENANCE_MATRIX.md`;
- `papers/dsir1/SUPPORT_OPERATOR_PROVENANCE.md`;
- `papers/dsir1/OBSERVATION_ROUTE_LEDGER.md`;
- `papers/dsir1/FIGURE_MANIFEST.md`;
- `papers/dsir1/evidence/`;
- the latest successful `DSIR-I paper build v0.2` GitHub Actions artifact.

The base `manuscript.md` remains an immutable v0.1 source; later evidence is injected deterministically by `build_manuscript_v0_2.py` so the article history is recoverable without chat context.
