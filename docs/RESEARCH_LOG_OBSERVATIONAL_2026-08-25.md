# DSIR observational-whitening research log — 2026-08-25

This log continues `docs/RESEARCH_LOG_OBSERVATIONAL_2026-08-24.md`. Scientific claim status is controlled by `docs/GATES.md`; evolving interpretation status is mirrored in `docs/SCIENTIFIC_FINDINGS_REGISTER.md`.

## Experiments 036–040 — earlier same-day chronology

The full detailed protocols/results remain in their numbered experiment files and in the preserved pre-Exp044 recovery manual. Key chronology:

### Experiment 036 — pinned-artifact AP family geometry

Run `32782545098`, artifact `9540273287`, SHA256 `553faa2ef7ddbc44e25ddd6faca237d0be7fc265b9c23cfafb2a32570534d126`.

Corrected DESI `D_H/D_M` marginal-whitened acute angles:

- smooth-w / IDE negative-alpha `72.803493 deg`;
- smooth-w / IDE beta `64.151094 deg`;
- IDE negative-alpha / beta `9.0379006 deg`.

### Experiment 037 — GDM AP-zero audit

Run `32783243120`, artifact `9540510596`, SHA256 `ba1fa93e348f9685d84a675311c79f9c746574463086710b4a46911d125f4edf`.

For frozen `w_gdm=0` cs2/cv2 closure rays, all saved background columns and AP responses equal reference exactly. C3 geometry zero is validated, not imputed.

### Experiment 038 — designer-f(R) AP-zero audit

First hard run `32785800977`; final transfer-preserving regression `32786915513`, artifact `9541895055`, SHA256 `74d975790d00a04762d45bf183481f69d6fc54b84d186c63e89b88bbb9d20b16`.

Frozen `B0=0..1e-3` on the source-proven `EFTwDE=0` designer branch has exact saved background/AP equality to reference while perturbation response is nonzero.

### Experiment 039 — ShapeFit growth/RSD contract

Correct coordinate is `f_sigma_s8`, with

\[
s=r_d/r_d^{ref},\qquad R=s\,8h^{-1}{\rm Mpc},
\]

and scalar-representability diagnostic

\[
{\cal D}_{RSD}=1-\frac{S_{\delta\Theta}^2}{S_{\delta\delta}S_{\Theta\Theta}}.
\]

Printed H-EFTCAMB summary logs are rejected for small-B0 tangents because ~4-decimal precision quantizes the response.

### Experiment 040 — finite-bin temporal structure response

Run `32785987735`, artifact `9541462864`, SHA256 `0457823510fead4ff56e8e29843e39de47805f8fbfda86f4d9d33585be556ac9`.

Hard comparison ladder/reversals:

- IDE alpha/beta: AP `9.04 deg` -> temporal `29.40 deg` -> full structure `58.93 deg`;
- smooth-w/IDE-alpha: AP `72.80 deg`, temporal `10.31 deg`, structure `52.19 deg`;
- GDM cs2/cv2: structure `0.3226 deg`, temporal `1.3340 deg`;
- GDM/f(R): scale-only `0.078-0.102 deg`, temporal `16-17 deg`, full `25 deg`.

Hard interpretation: **degeneracies migrate between response operators**.

---

## Experiment 041 — high-precision designer-f(R) density/velocity representability

### Goal

Test whether the frozen C5 density and Newtonian-matter velocity transfer fields can be compressed into one scale-independent ShapeFit-like growth amplitude.

### Diagnostic

With `g(k)=Theta/delta`, the moment defect satisfies

\[
\boxed{{\cal D}_{RSD}=\frac{\mathrm{Var}_w[g]}{\langle g^2\rangle_w}},
\]

hence

\[
CV_w(g)=\sqrt{\frac{{\cal D}_{RSD}}{1-{\cal D}_{RSD}}}.
\]

### Hard result

Run `32791510072`, artifact `9543375564`, SHA256 `1e4d86f7f13185d69a07b71afa9bfd6fefa6003119064652d6388491738212bc`.

At `kmax=0.24 h/Mpc`:

- GR/B0=0 floor `~1.42e-10`;
- `B0=1e-6`: `D_RSD=5.18e-6`;
- `1e-5`: `1.92e-4`;
- `1e-4`: `8.81e-4`;
- `1e-3`: `8.78e-4`.

The corresponding weighted fractional scale variation is about `0.23%, 1.39%, 2.97%, 2.96%`.

**Hard conclusion:** scalar growth compression is not exact for the frozen designer-f(R) direction even though its background/AP response is exactly zero.

---

## Experiment 042 — exploratory GDM density/velocity bridge

### Motivation

After C5, test whether the GDM velocity sector adds a separator between the strongly density-degenerate `cs2/cv2` directions.

### Chronology

1. The exact frozen synchronous configurations were extended to output transfer density/velocity fields.
2. Synchronous dark-matter velocity is gauge-fixed/ill-conditioned for RSD and was rejected as a physical RSD estimator.
3. The pinned branch exposes an N-body transfer option, but upstream stops because `H_T_Nb_prime` derivative is not propagated.
4. Matched synchronous and Newtonian runs were generated instead.
5. The first analysis attempt failed before science because synchronous output had 16 columns including an auxiliary CDM column while Newtonian output had 15. The parser was corrected by actual layout; no scientific threshold changed.

### Frozen gauge bridge

Before Newtonian target interpretation:

- max absolute comoving-density log mismatch `<=1e-6`;
- max model/reference response difference `<=1e-6`.

The initial raw transfer-grid `1e-12` comparison was later recognized as methodologically inappropriate because adaptive output k grids can differ between gauges; Experiment 043 corrected this by interpolation to frozen DSIR nodes.

### Actual result

Run `32793688546`:

- max absolute `ln|Delta_S/Delta_N| = 2.58664e-6` -> FAIL;
- max model/reference response difference `6.78698e-7` -> within threshold.

Status:

`FAIL_GDM_SYNC_NEWTONIAN_DELTA_BRIDGE_V0_2`.

Exploratory cs2/cv2 velocity angles and `D_RSD` were numerically produced, but because the bridge failed they are **not scientific claims** and must not be used downstream.

---

## Experiment 043 — GDM gauge precision convergence

### Question

Could the Exp042 absolute synchronous/Newtonian mismatch be ordinary perturbation-integration precision error?

### Method

Interpolate each gauge independently to the frozen DSIR nodes. Compare the original p8 setup with a p10 run changing only numerical precision:

- `tol_perturb_integration: 3e-10 -> 3e-12`;
- `perturb_sampling_stepsize: 0.00035 -> 0.00015`.

Pre-frozen requirement: p10 must both pass the existing `1e-6` bridge ceiling and reduce the absolute residual by at least a factor two.

### Hard result

Run `32794067542`, artifact `9544255453`, SHA256 `c62613798a6a6f8e9e573bb158315ca03a5c9f998805ebfc6bdda25de4d4100a`.

p8:

- absolute bridge `2.5195769e-6`;
- response bridge `6.7869784e-7`.

p10:

- absolute bridge `3.0062530e-6`;
- response bridge `8.02173997e-7`;
- absolute residual ratio p10/p8 `1.1931579`.

Status:

`FAIL_GDM_GAUGE_PRECISION_CONVERGENCE_V0_1`.

**Negative conclusion:** tighter perturbation precision does not explain or reduce the absolute mismatch. Do not relax the frozen bridge. The current pinned GDM Newtonian velocity/RSD route remains unvalidated.

---

## Experiment 044 — chat audit / BuyanovGPT hypothesis formalization

### Purpose

Audit the current chat against repository state and preserve all substantive ideas without upgrading conversation-level hypotheses into hard science.

### Preserved strategy

The primary DSIR program remains model comparison and pattern discovery:

- compare physically different families;
- find exact nulls, approximate degeneracies, sign/orientation changes, channel reversals, localization and nonseparability;
- seek new physics only when hard controls survive;
- estimate minimal dimension in parallel;
- postpone universal-model construction until the atlas and withheld validation are mature.

The nickname **BuyanovGPT table** is now formalized in `docs/BUYANOVGPT_TABLE.md` as an influence atlas, not a theory.

### Preserved hypotheses / corrected overstatements

The chat proposed candidate response labels `G,T,tau,S,M,N,B` and a black-hole/no-hair analogy. These remain only organizers.

Two quantities are now explicitly distinguished:

- `N_repr`: response representation dimension;
- `N_disc`: mechanism discrimination dimension.

The statement “G,T,tau are always present in C1-C5” was too strong. In particular, C4 WDM's informative response lives in a separate high-k block and cannot be inserted into the low-k common matrix as zero.

---

## Experiment 045A — additive `G,T,tau` core projection

### Question

Can the common C1/C2/C3/C5 low-k structure response be represented by three additive response types: global amplitude, scale-only dependence and time-only dependence?

### Frozen decomposition

For each response matrix `R(z,k)`:

\[
\mu=\langle R\rangle_{z,k},
\]

\[
T(k)=\langle R\rangle_z-\mu,
\]

\[
\tau(z)=\langle R\rangle_k-\mu,
\]

\[
\boxed{R(z,k)=\mu+T(k)+\tau(z)+I(z,k)}.
\]

`I(k,z)` is the irreducible scale-time interaction.

Pre-frozen compact adequacy:

- every direction core power capture `>=0.95`;
- every pairwise acute-angle distortion `<=5 deg`.

### Infrastructure chronology

First run failed before science on `numpy.bool_` JSON serialization. Second run exposed double-precision accumulation orthogonality residual `3.70e-11` against the frozen `1e-12` operator control. No threshold changed. Arithmetic accumulation only was upgraded to `numpy.longdouble`.

Final operator controls:

- reconstruction error `0`;
- scaled zero-mean residual `4.22e-21`;
- normalized core/I inner product `2.57e-15` -> PASS.

### Hard result

Run `32883280742`, artifact `9576600500`, SHA256 `59839a2717646e50501a949cf5b310cb6c0e55f85dd6839fce2832c704ec28dd`.

Status:

`FAIL_COMPACT_G_T_TAU_CORE_LOW_K_V0_1`.

| Direction | `||I||/||R||` | interaction power | core capture |
|---|---:|---:|---:|
| C1 smooth-w | 0.03287 | 0.108% | 99.892% |
| C2 IDE alpha | 3.97e-6 | ~1.57e-9% | ~100% |
| C2 IDE beta | 7.41e-6 | ~5.49e-9% | ~100% |
| C3 GDM cs2 | **0.21285** | **4.53%** | 95.47% |
| C3 GDM cv2 | **0.20889** | **4.36%** | 95.64% |
| C5 designer f(R) | **0.54759** | **29.99%** | **70.01%** |

Pairwise distortions after dropping `I`:

- IDE-alpha/f(R): **14.31 deg**;
- GDM-cs2/f(R): **10.41 deg**;
- GDM-cv2/f(R): **10.56 deg**;
- smooth-w/f(R): `5.92 deg`;
- IDE-beta/f(R): `6.87 deg`.

### New hard interpretation

**The simple additive `Core=(G,T,tau)` hypothesis is falsified on the common C1/C2/C3/C5 low-k theory block.**

Designer f(R) carries nearly 30% of its structure-response power in irreducible scale-time interaction; GDM carries ~4.4-4.5%. By contrast the current IDE directions are almost perfectly additive in this diagnostic.

This sharpens the earlier GDM/f(R) comparison: part of their distinguishability is specifically in **how scale dependence evolves with time**, not simply the availability of separate scale and time summaries.

`I(k,z)` is therefore a new **candidate response signature** for comparison. It is not yet a universal hair, a fourth fundamental parameter, a residual law, or a discovery.

C4 WDM remains outside this test until a high-k time-dependent response atlas exists.

---

## Gate consequences and continuation after Exp045A

G5 remains PARTIAL. G7/G8 remain OPEN.

Immediate research sequence:

1. freeze a morphology/stability test for `I(k,z)` across C1/C2/C3/C5;
2. determine whether `I` has mechanism-specific sign/orientation patterns and whether it independently separates GDM/f(R);
3. extend C4 WDM to a high-k `(k,z)` atlas, then test its interaction without domain mismatch;
4. continue slip/lensing, because GDM cs2/cv2 proves density/time can erase mechanism information;
5. continue survey/window-aware shape and RSD operators;
6. keep `N_repr` distinct from `N_disc` and do not force latent dimension to a preselected value;
7. continue the main model-comparison program and search for robust new cross-family relations;
8. build a universal model only after the explicit readiness criteria and a credible withheld-family prediction test;
9. no residual-law claim before G7 and no discovery before G8.
