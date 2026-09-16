---
title: "Dark-Sector Influence Reconstruction I: Observable-response geometry, channel-conditional equivalence, and failure-resistant model comparison"
author:
  - "[authors to be finalized]"
date: "2026-08-27"
bibliography: references.bib
---

# Abstract

Cosmological dark-sector models that differ sharply at the level of microscopic interpretation can become nearly degenerate after projection onto a restricted set of observables. Conversely, models that are nearly indistinguishable in one response channel can separate strongly in another. We introduce **Dark-Sector Influence Reconstruction (DSIR)**, a model-agnostic framework that compares dark energy, interacting dark-sector, generalized-dark-matter, warm-dark-matter, decaying-dark-matter, and modified-gravity models in a common response geometry before assigning ontological meaning to the inferred influences. For a low-wavenumber structure response we decompose

\[
R(z,k)=\mu+T(k)+\tau(z)+I(z,k),
\]

and quantify the irreducible scale-time component by \(\chi_I=\|I\|^2/\|R\|^2\). Across prospectively frozen grids and finite-amplitude rays we find a non-overlapping descriptive hierarchy, \(\mathrm{IDE}<\mathrm{smooth\ DE}<\mathrm{GDM}<f(R)\), with sampled \(\chi_I\) envelopes of approximately \(10^{-11}\), \(10^{-3}\), \(10^{-2}\), and \(10^{-1}\), respectively. The tier ordering survives all 12 deterministic single-node deletion tests. Pairwise analysis shows that about 61% of the normalized GDM--\(f(R)\) response-shape separation on the frozen low-\(k\) grid is localized in the irreducible \(k\times z\) component. At the same time, degeneracy is explicitly channel conditional: GDM pressure and viscosity directions have a matter-response angle of only \(0.3226^\circ\), while metric slip separates them by \(137.94^\circ\); GDM and designer-\(f(R)\) are nearly aligned in a leading scale mode but separate through time evolution and response sign. We formalize this with the quotient signature operator \(A_B=Q_BW_BK_B\), under which exact equivalence is defined by \(A_B(r_1-r_2)=0\). Thermal warm dark matter and a withheld decaying-dark-matter family provide additional mechanism-level tests showing that response localization can be scale dominated, time dominated, or genuinely nonseparable. DSIR-I is therefore a response-classification and identifiability result, not a claim of a universal dark-sector invariant or a discovery of new fundamental physics.

# 1. Introduction

The cosmological dark sector is inferred indirectly through its gravitational and statistical influence on the expansion history, structure formation, metric potentials, lensing, and related observables. This indirectness creates a fundamental identification problem: different microscopic descriptions can generate the same or nearly the same observable response in a restricted data space. The classic ``dark degeneracy'' emphasizes that gravity couples to the total stress-energy content rather than to a unique decomposition into named dark components [@Kunz2007]. Related work has shown that generalized dark energy can reproduce signatures usually associated with modified gravity in linear cosmological perturbations [@BertschingerZukin2008], while parameterized post-Friedmann and effective-field-theory approaches provide powerful common descriptions of broad classes of modified-gravity and dark-energy models [@HuSawicki2007; @Gubitosi2012; @BelliniSawicki2014]. Generalized dark matter similarly demonstrates that clustering, pressure, and anisotropic stress can alter perturbations independently of the homogeneous equation of state [@Hu1998].

These frameworks motivate a question that is narrower than constructing another universal theory but broader than fitting one microscopic model at a time: **what observable influence structure is actually required to distinguish physically different dark-sector mechanisms, and how does that structure change when the measurement operator changes?**

DSIR addresses this question by separating three layers. The **data layer** contains observables, likelihoods, covariances, windows, and nuisance parameters. The **response layer** contains model-independent or minimally model-dependent physical responses such as relative expansion, matter growth, scale-dependent transfer, Weyl/lensing response, metric slip, and time dependence. The **theory layer** embeds concrete model families into that response space. The logical direction is therefore not ``choose a dark-sector ontology and fit it'', but rather ``compare influence trajectories under controlled operators, identify null and discriminating directions, and only then ask which theory interpretations remain viable.''

This paper develops and tests the first part of that program. Its contributions are fivefold. First, we define a block-aware response geometry in which undefined model/channel combinations are masked rather than silently replaced by zeros. Second, we show quantitatively that a simple additive description of scale and time dependence fails for some mechanisms because an irreducible scale-time interaction carries substantial response power. Third, we demonstrate with frozen examples that degeneracy is channel conditional: matter-response lookalikes can be split by metric information, while scale-only lookalikes can be split by temporal evolution. Fourth, we separate microscopic parameter count from response-manifold curvature and linear representation rank. Fifth, we formalize exact channel-conditional equivalence through physical projection, covariance whitening, and nuisance quotienting, while keeping the current empirical atlas distinct from a completed survey-level detectability analysis.

The scope boundary is important. DSIR-I does **not** claim a universal dark-sector law, a no-hair theorem, or a discovery of new fundamental physics. The later DSIR gates for a nontrivial residual law, fresh withheld prediction of that law, and reconstruction of underlying dynamics remain open. The present result is methodological and phenomenological: physically different mechanisms occupy structured, operator-dependent trajectories in response space, and that geometry can be tested without pretending that every useful response coordinate is a fundamental degree of freedom.

# 2. DSIR response construction

## 2.1 Three-layer architecture

Let a theory state be represented by parameters \(\theta\) and let its response vector be

\[
r(\theta)\in\mathbb{R}^n.
\]

The coordinates of \(r\) are not assumed to be microscopic parameters. They are explicitly defined physical-response samples or summaries. Depending on the block, these may include relative expansion, comoving matter response, Weyl-potential response, metric slip, small-scale transfer, or other certified quantities.

The theory layer may contain conventional dark energy, interacting dark energy, generalized dark matter, warm dark matter, modified gravity, decaying dark matter, or other models. DSIR does not require these families to share a common Lagrangian parameterization. Instead, they are compared only where a common physical response can be defined.

The data layer acts through a measurement or projection operator. A later fully observational comparison will include survey windows, covariance, and nuisance tangent directions. In this paper, we distinguish carefully between raw/certified theory-response geometry and that final observational quotient.

## 2.2 Frozen background and matter-response coordinates

For background evolution, one DSIR production coordinate is the anchored relative expansion response

\[
r_E(z;z_\star)=
\ln\left[
\frac{H(z)/H(z_\star)}{H_{\rm ref}(z)/H_{\rm ref}(z_\star)}
\right],
\]

with the frozen anchor \(z_\star=0.51\).

For the low-wavenumber perturbation block, the production matter coordinate is the same-solver comoving total-matter response

\[
r_\Delta(k,z)=
\ln\left[
\frac{P_{\Delta,\rm model}^{S}(k,z)}
{P_{\Delta,\rm ref}^{S}(k,z)}
\right],
\]

where model and reference use the same solver lineage \(S\) and matched numerical settings wherever possible. The frozen low-\(k\) grid is

\[
z=\{0.295,0.51,0.706,0.934,1.317,1.491,2.33\},
\]

\[
k=\{0.001,0.003,0.01,0.03,0.1\}\;h\,\mathrm{Mpc}^{-1}.
\]

Gauge-specific density and velocity variables are not treated as universal coordinates. The production matter source is based on the comoving total-matter combination, and the project maintains explicit conservation and gauge-regression controls.

## 2.3 Block-aware comparison and masks

Not every model is informative on every physical domain. Thermal warm dark matter, for example, is nearly invisible in the frozen low-\(k\) block while producing a strong small-scale transfer signature. It would be statistically and physically misleading to fill an undefined or intentionally blind high-\(k\) block with zeros and then perform a global singular-value analysis. DSIR therefore treats the atlas as block aware: only coordinates that are physically defined for a given provider are used, and cross-family statements specify the common support on which they are made.

This point is not bookkeeping trivia. A zero can mean a true physical null, a numerical zero limit, or merely absence of a defined comparison. Conflating those cases can create artificial degeneracies or artificial rank.

# 3. Response geometry

## 3.1 Additive scale-time projection

For a response matrix on a fixed \((z,k)\) grid, define the additive projection

\[
R(z,k)=\mu+T(k)+\tau(z)+I(z,k),
\]

where \(\mu\) is a global mean component, \(T(k)\) is a scale-only contribution, \(\tau(z)\) is a time-only contribution, and \(I(z,k)\) is the residual interaction after the best additive projection under the frozen norm. The normalized interaction-power fraction is

\[
\chi_I=
\frac{\|I\|^2}{\|R\|^2}.
\]

A small \(\chi_I\) means that, on the specified grid and response definition, scale and time effects are nearly separable. A large \(\chi_I\) means that the shape of the scale dependence changes materially with redshift.

This is a representation diagnostic, not a microscopic parameter. In particular, the existence of \(I\) does not imply a fourth fundamental dark-sector degree of freedom.

## 3.2 Pairwise localization of separation

For two normalized response shapes \(A\) and \(B\), let \(d\) denote their difference and let \(d_I\) be the irreducible scale-time component of that difference under the same projection. Define

\[
\eta_I(A,B)=
\frac{\|d_I\|^2}{\|d\|^2}.
\]

The quantity \(\eta_I\) measures what fraction of the pairwise response-shape separation is localized in irreducible \(k\times z\) structure. It is not by itself a measure of how far apart the two models are: a large fraction of a very small distance remains a small distinction. We therefore report \(\eta_I\) together with total distance or angle.

## 3.3 Normalized trajectory curvature

For a nonzero family response \(r(\theta)\), define the normalized direction

\[
u(\theta)=\frac{r(\theta)}{\|r(\theta)\|}.
\]

Then

\[
\frac{du}{d\theta}
=
\frac{(I-uu^T)}{\|r\|}
\frac{dr}{d\theta}.
\]

Only changes orthogonal to the current response direction rotate the normalized trajectory. Pure amplitude rescaling does not. Consequently, a one-parameter microscopic family can trace a curved path whose sampled linear span contains several significant singular directions. This motivates keeping distinct

\[
N_{\rm micro},\qquad
N_{\rm manifold},\qquad
N_{\rm repr},\qquad
N_{\rm disc}.
\]

Here \(N_{\rm micro}\) is microscopic parameter count, \(N_{\rm manifold}\) is the dimension of the physical family manifold, \(N_{\rm repr}\) is a representation rank under a chosen linear compression, and \(N_{\rm disc}\) is the number of independent discriminants needed to separate a specified catalogue under specified channels.

# 4. Channel-conditional equivalence

## 4.1 Observational signature operator

For a chosen channel set \(B\), let

\[
K_B:\mathbb{R}^n\rightarrow\mathbb{R}^{m_B}
\]

be the physical projection/window operator. If the validated covariance is positive definite,

\[
C_B=L_BL_B^T,
\]

we define the whitener

\[
W_B=L_B^{-1}.
\]

Let \(U_{\eta,B}\) contain the retained whitened nuisance tangent directions and define

\[
Q_B=I-U_{\eta,B}U_{\eta,B}^T.
\]

The DSIR observational signature operator is

\[
A_B=Q_BW_BK_B,
\]

with signature

\[
s_B(\theta)=A_Br(\theta).
\]

Two theory states are **exactly channel-conditionally equivalent** when

\[
r_1\sim_B r_2
\quad\Longleftrightarrow\quad
A_B(r_1-r_2)=0.
\]

Equivalently, their difference lies in \(\ker A_B\). Thus exact observational equivalence is not an intrinsic property of a pair of microscopic model names. It is induced by the selected physical channels, windows, covariance weighting, and nuisance quotient.

## 4.2 Whitening and nuisance quotient

Because \(W_B\) is invertible for a positive-definite covariance,

\[
\ker(W_BK_B)=\ker K_B.
\]

Whitening changes the metric and statistical weighting but does not create or remove an exact pre-nuisance physical null.

Nuisance quotienting is different. Since \(Q_B\) projects out the retained nuisance subspace \(\mathcal{N}_B\),

\[
A_B\Delta r=0
\]

if and only if

\[
W_BK_B\Delta r\in\mathcal{N}_B.
\]

A physical response can therefore be nonzero yet observationally unidentifiable if its whitened displacement is absorbed entirely by the nuisance tangent space.

## 4.3 Compatible channel refinement

For two independently quotiented channel blocks \(B\) and \(C\), if the joint signature is formed by compatible stacking,

\[
A_{B\oplus C}=
\begin{bmatrix}
A_B\\
A_C
\end{bmatrix},
\]

then

\[
\ker A_{B\oplus C}=\ker A_B\cap\ker A_C.
\]

Under this compatibility condition, adding an independent retained channel can leave an exact equivalence class unchanged or split it, but cannot merge two states already distinguishable in one of the retained blocks. This formalizes the empirical DSIR pattern in which matter-response lookalikes separate after metric-slip/Weyl information is added.

A caveat is essential: if the combined analysis introduces a new shared nuisance model and recomputes a joint quotient, then \(Q_{B\cup C}\neq Q_B\oplus Q_C\) in general, and the simple kernel-refinement statement need not hold. For this reason DSIR treats the final multi-probe nuisance tangent SVD as a prospectively frozen observational step rather than inferring survey-level identifiability from theory-space angles.

# 5. Theory atlas

The current DSIR-I atlas uses \(\Lambda\)CDM/GR as the common response origin and compares several qualitatively different departures. The purpose is not to sample all viable dark-sector theories, but to stress the response representation with mechanisms that act through different physical channels.

| Class | Representative mechanism | Main response character used here |
|---|---|---|
| C0 | \(\Lambda\)CDM/GR | reference origin |
| C1 | smooth non-phantom dark energy | background active; weak low-\(k\) scale-time interaction |
| C2 | interacting dark sector (IDE) | exchange active; low-\(k\) structure nearly scale-time separable on tested rays |
| C3 | generalized dark matter, \(w=0\), pressure/viscosity rays | perturbation active with exact background/AP null; metric slip is an important separator |
| C4 | thermal warm dark matter | high-\(k\) free-streaming transfer; nearly time-separable on frozen linear high-\(k\) block |
| C5 | designer \(f(R)\) gravity | exact background/AP null in the frozen setup; strong low-\(k\) scale-time interaction and curved response trajectory |
| C6 | decaying dark matter to dark radiation | withheld mechanism with strong temporal localization and moving response epoch |

The construction deliberately includes directions that share background behavior but differ at perturbation level, directions that share a matter-response shape but differ in metric slip, and directions whose main signatures live on disjoint scale domains. These cases test whether the response geometry can retain physically meaningful distinctions without assuming a common microscopic parameterization.

# 6. Results

## 6.1 Matter-response degeneracy can be broken by metric channels

The clearest channel-conditional example inside the frozen atlas is provided by the C3 generalized-dark-matter pressure and viscosity directions. In the low-\(k\) comoving matter response, the two normalized rays are nearly collinear:

\[
\angle(r_{c_s^2},r_{c_v^2})=0.322616^\circ.
\]

A matter-only analysis would therefore regard the two perturbative mechanisms as strong lookalikes on this domain. The metric-slip block changes the conclusion. The frozen slip angle is

\[
137.9432^\circ,
\]

and an equalized combined Weyl+slip comparison gives

\[
56.9632^\circ.
\]

The important result is not the precise angular value in isolation, but the change in equivalence class when an independent physical channel is added. A parameter translation calibrated only in matter power would therefore not be expected to remain valid after metric information is included.

## 6.2 Scale-only similarity between GDM and designer-\(f(R)\) is broken by time evolution

A second example compares GDM with designer \(f(R)\). On the frozen low-\(k\) grid the leading scale modes are strikingly aligned: the GDM-\(c_s^2\)/\(f(R)\) scale-mode angle is \(0.07813^\circ\), and the GDM-\(c_v^2\)/\(f(R)\) value is \(0.10169^\circ\). Yet their time modes differ by approximately \(25.2^\circ\), and the full oriented response rays differ by about \(155^\circ\). Thus an apparent scale-domain translation is not a global equivalence.

This is precisely the situation that motivates a channel- and operator-conditional notion of model distance. A single scalar ``similarity'' score would erase the mechanism by which the degeneracy is broken.

## 6.3 The additive `(G,T,tau)` core is insufficient

The additive scale-time decomposition provides a direct test of whether a low-dimensional summary based on global amplitude, a scale-only shape, and a time-only evolution can represent the frozen response atlas. It cannot.

Representative hard \(\chi_I\) values are

| Direction | \(\chi_I\) |
|---|---:|
| smooth-\(w\) | \(1.0805\times10^{-3}\) |
| IDE negative-\(\alpha\) | \(1.57\times10^{-11}\) |
| IDE \(\beta\) | \(5.49\times10^{-11}\) |
| GDM \(c_s^2\) | \(4.5305\times10^{-2}\) |
| GDM \(c_v^2\) | \(4.3634\times10^{-2}\) |
| designer \(f(R)\) | \(2.99856\times10^{-1}\) |

For designer \(f(R)\), nearly 30% of the response power on this grid lies outside the best additive scale-plus-time representation. GDM retains a smaller but clearly non-negligible 4--5% interaction fraction, while the tested IDE directions are effectively separable at the morphology level.

The conclusion is deliberately limited: the tested low-\(k\) responses cannot in general be compressed into independent `scale' and `time' summaries without loss. It does not follow that \(I\) is a fundamental dark-sector parameter.

## 6.4 Finite-amplitude hierarchy and grid robustness

A local tangent-space pattern can be an artifact of the infinitesimal limit. We therefore sampled finite-amplitude rays using immutable solver products and recomputed the interaction fraction. The resulting envelopes are

| Family | sampled \(\chi_I\) range |
|---|---:|
| IDE | \(1.4351\times10^{-11}\) -- \(5.4945\times10^{-11}\) |
| smooth-\(w\) | \(1.08051\times10^{-3}\) -- \(1.08806\times10^{-3}\) |
| GDM | \(1.30105\times10^{-2}\) -- \(4.54103\times10^{-2}\) |
| designer \(f(R)\) | \(1.73327\times10^{-1}\) -- \(3.13326\times10^{-1}\) |

The envelopes remain non-overlapping across the sampled physical amplitudes, yielding the descriptive ordering

\[
\boxed{
\mathrm{IDE}<\mathrm{smooth\ DE}<\mathrm{GDM}<f(R)
}.
\]

The minimum gaps between adjacent sampled envelopes are large: smooth dark energy lies at least about \(2\times10^7\) above the tested IDE interaction fraction, GDM at least about a factor 12 above smooth dark energy, and designer \(f(R)\) at least about a factor 3.8 above GDM.

We then removed each of the five \(k\) nodes and each of the seven redshift nodes one at a time. The tier ordering survived all 12 deterministic deletions. The GDM--\(f(R)\) pairwise interaction localization also remained material, with \(\eta_I\) approximately \(0.55\)--\(0.65\) depending on the deleted node.

One caveat illustrates why this hierarchy is descriptive rather than universal. The absolute smooth-\(w\) interaction fraction is sensitive to the \(k=0.001\,h\,\mathrm{Mpc}^{-1}\) node; removing it lowers the scalar value substantially even though the family remains in the same qualitative tier. The robust statement is therefore the separation of response classes on the frozen tested domains, not a universal numerical threshold.

## 6.5 Irreducible scale-time structure carries GDM--\(f(R)\) separation

Using \(\eta_I\), the fraction of pairwise normalized separation power localized in the irreducible interaction component, we find

\[
\eta_I(\mathrm{GDM}\ c_s^2,f(R))=0.611982,
\]

\[
\eta_I(\mathrm{GDM}\ c_v^2,f(R))=0.613829.
\]

Thus roughly 61% of the response-shape distinction between these pairs on the frozen low-\(k\) grid resides specifically in how scale dependence changes with redshift. This is consistent with the earlier observation that the leading scale modes are almost parallel while time/full structure separates them.

For GDM \(c_s^2\) versus \(c_v^2\), \(\eta_I\) is even larger, about 0.73, but the total matter-response angle is only \(0.323^\circ\). This is a useful warning: localization fractions are meaningful only together with an absolute separation measure.

## 6.6 Curved one-parameter manifolds generate multi-mode response structure

Finite-amplitude scans show that some microscopic one-parameter families bend appreciably in normalized response space. The maximum sampled full-response turn relative to the smallest reliable amplitude is only \(0.155^\circ\) for smooth dark energy and \(0.028^\circ\) for the GDM pressure ray, but reaches approximately

\[
7.18^\circ
\]

for GDM viscosity and

\[
12.14^\circ
\]

for designer \(f(R)\). The interaction-only direction turns by as much as \(12.19^\circ\) and \(13.00^\circ\), respectively.

The corresponding interaction fraction is not constant along the family. For GDM viscosity it decreases from about 0.0438 to 0.0130 over the sampled amplitude range, while designer \(f(R)\) follows a non-monotonic sequence around 0.300, 0.313, 0.286, and 0.173 across \(B_0=10^{-6},10^{-5},10^{-4},10^{-3}\).

These results show why a raw SVD mode count cannot be read as microscopic parameter count. A curved one-dimensional manifold can require several linear basis vectors for accurate representation.

## 6.7 Warm dark matter: strong scale localization with almost no scale-time interaction

Thermal warm dark matter provides an important counterexample to any naive rule that a strong scale signature must imply strong scale-time nonseparability. On the frozen high-\(k\) linear atlas, masses 2, 3, and 5 keV show substantial suppression at small scales but extremely weak redshift drift. The measured interaction fractions are approximately

\[
\chi_I\simeq2.2\text{--}2.6\times10^{-10}.
\]

A mechanism-native cutoff coordinate \(k_{0.1}(z)\), defined by

\[
\ln(P_{\rm WDM}/P_{\rm CDM})=-0.1,
\]

was then tested prospectively on withheld interpolation masses 2.5, 3.5, 4.0, and 4.5 keV. At every frozen redshift, \(k_{0.1}\) increases monotonically with mass. At \(z=0.295\), the corresponding values are approximately 8.39, 12.19, 14.23, and 16.47 \(h\,\mathrm{Mpc}^{-1}\).

WDM therefore occupies a response class that is strongly scale dominated yet nearly time separable on the tested linear domain. This contrasts both with GDM viscosity and with designer \(f(R)\), where scale-time coupling is substantial.

## 6.8 Withheld decaying dark matter: temporal localization as a distinct mechanism

To test whether the organizing language learned from C1--C5 merely reflected interpolation within known families, DSIR introduced a decaying-dark-matter-to-dark-radiation family that was withheld from construction of the earlier characteristic-scale discussion. A temporal response centroid \(z_R\) was defined prospectively. For

\[
\Gamma/H_0=\{0.25,0.5,1,2\},
\]

the measured centroid moves

\[
0.6304573,\ 0.6343830,\ 0.6419613,\ 0.6562403,
\]

with every consecutive shift exceeding the frozen \(10^{-3}\) guard. The same family exhibits a descriptive \(\chi_I\) range of roughly 0.066--0.082 and a redshift-moving scale-sign pivot on the sampled low-\(k\) domain.

This is evidence that response localization can encode a genuinely different control mechanism---here a decay epoch/lifetime rather than a free-streaming cutoff or modified-gravity transition. However, because no single model-independent quantitative residual law had been frozen before this withheld-family test, the result is supporting evidence for the response-localization program rather than a completed withheld validation of a universal law.

# 7. Failure-resistant numerical validation

A central methodological requirement of DSIR is that a scientific failure remains part of the provenance even when a later, independently justified provider succeeds. Two examples are illustrative.

For the C3 GDM physical-power bridge, a first target-grid reconstruction produced a roughly 4.75% matter-power defect. Mechanism audit showed that the defect was interpolation dominated: reconstructing on the native provider grid closed the native \(P_{mm}\) relation to approximately \(2.8\times10^{-14}\), whereas the rejected amplitude interpolation reproduced the 0.0475-level error. A new native-grid provider was then prospectively specified and passed its frozen closure, coherence, signed-cross, repeatability, and schema controls. The original failed bridge was not reclassified.

For designer \(f(R)\), an initial low-accuracy bridge failed the frozen GR-limit criterion at approximately \(5.30\times10^{-6}\) against a \(5\times10^{-6}\) threshold. Rather than subtracting a floor or retuning the threshold, DSIR performed an explicit accuracy-convergence ladder. The zero-limit target residual decreased monotonically with numerical accuracy, and an independently frozen higher-accuracy provider subsequently passed exact-zero, tiny-positive continuity, production-signal, signed-spectrum, repeatability, source-integrity, and no-retrospective-correction checks. Again, the original failure remains a permanent result for the original provider contract.

These examples matter scientifically because small response differences are precisely where numerical representation errors can masquerade as physical effects. Preserving failed contracts, freezing thresholds before reruns, and separating infrastructure success from scientific pass/fail are therefore part of the inference method rather than software-engineering details.

# 8. Relation to existing dark-sector parameterizations

DSIR is complementary to, rather than a replacement for, established parameterized approaches. The dark-degeneracy argument already shows why the observable total gravitational influence need not identify a unique dark-component decomposition [@Kunz2007]. PPF provides a common description of modified-gravity perturbations and clarifies equivalences with generalized dark energy [@HuSawicki2007]. EFT approaches organize broad classes of dark-energy and modified-gravity theories by operators or time-dependent functions [@Gubitosi2012; @BelliniSawicki2014]. GDM isolates pressure and anisotropic-stress effects in a phenomenological stress tensor [@Hu1998]. Model-independent interacting-dark-sector reconstruction similarly illustrates the value of separating phenomenological inference from a fixed interaction ansatz [@vonMarttens2020].

The specific role of DSIR is different. It asks how heterogeneous model families populate a **common response atlas**, which channel combinations separate them, which directions are null, where scale-time nonseparability appears, and how response trajectories bend or migrate across finite observational domains. It also treats the observational operator itself as part of the definition of equivalence through \(A_B=Q_BW_BK_B\).

This operator view makes explicit a point that is sometimes hidden when model comparison is expressed only in parameter coordinates: two theories can be equivalent under one survey/channel construction and inequivalent under another. There is therefore no reason to expect a universal model-to-model parameter translator unless the response subspace and measurement operator are stated as part of the map.

# 9. Interpretation

## 9.1 What the hierarchy does mean

The observed hierarchy in \(\chi_I\) says that the tested mechanisms produce qualitatively different amounts of irreducible scale-time structure on the frozen domains. IDE is nearly separable, smooth dark energy is weakly nonseparable, GDM is moderately nonseparable, and designer \(f(R)\) is strongly nonseparable. Thermal WDM demonstrates that even a strong scale-dependent mechanism can remain almost perfectly time separable, while DCDM introduces a distinct temporal-localization pattern.

This hierarchy is useful because it is not merely a ranking of signal amplitudes. It asks **how the shape of the response evolves**, which is why it distinguishes some scale-mode lookalikes.

## 9.2 What the hierarchy does not mean

The hierarchy does not establish that the dark sector possesses a universal coordinate \(I\), nor that there are four fundamental influence ``hairs''. The values are conditional on response definition, scale/redshift domain, solver-certified providers, and masking. A future observation-space projection can change statistical distances even when the underlying theory-response morphology is unchanged.

Likewise, the fact that the current atlas can be separated by a small set of channel types is not a measurement of the fundamental number of dark-sector degrees of freedom. The minimum discriminant set for a finite catalogue, the rank of a whitened observational operator, and the dimension of a microscopic theory manifold answer different questions.

## 9.3 Why multi-channel measurements are structurally necessary

The GDM pressure/viscosity example gives a concrete reason to preserve metric information rather than compress all perturbations into matter power. The GDM/\(f(R)\) example gives an analogous reason to preserve temporal structure rather than a single scale-only summary. WDM requires access to sufficiently high \(k\), while DCDM emphasizes response timing.

The emerging picture is therefore not ``find the one best observable'', but construct a set of physically distinct channels whose kernels intersect as little as possible after realistic nuisance quotienting. This is the operational meaning of the DSIR discriminant program.

# 10. Limitations and claim boundary

Several limitations are essential to the interpretation of DSIR-I.

First, much of the numerical atlas is a **theory-response** comparison. Although DSIR has already validated data-layer ingredients and observational operators in separate stages, the final common support mask, covariance restriction/whitening, nuisance tangent SVD, and quotient-space relation test are not yet complete for the full cross-family comparison. Theory-space angles must therefore not be read as survey detection significances.

Second, the atlas is finite. It contains deliberately diverse families, but no finite catalogue can establish a universal law across all possible dark-sector theories. The DCDM withheld test increases mechanism diversity but does not eliminate this limitation.

Third, different mechanisms are informative on different scale domains. WDM high-\(k\) transfer cannot be compared to low-\(k\) responses by zero-padding. All cross-family rank and relation claims must remain block aware.

Fourth, current results are primarily in the linear or controlled quasi-linear response regime of the certified providers. Nonlinear screening, baryonic feedback, and strongly nonlinear structure can introduce new degeneracies or discriminants.

Fifth, numerical solvers are part of the measurement chain from theory to response. The failure-preservation examples show that interpolation, accuracy settings, unit conventions, or accessor semantics can create false response structure at the level relevant to DSIR. Cross-solver and provider-integrity controls must therefore remain active.

Finally, DSIR has not passed its discovery gates. There is no completed model-independent residual law with a fresh withheld-family prediction, and no reconstructed underlying dynamics/action. We therefore make no claim of new fundamental physics in this paper.

# 11. Outlook

The next DSIR stages follow directly from the formal operator definition. Certified physical providers must first be restricted to a prospectively frozen common physical support mask. The observational covariance is then restricted and whitened, nuisance tangent directions are identified under a frozen rank rule, and theory responses are compared only in the resulting quotient space. A candidate cross-channel relation can be promoted only after known identities and nuisance degeneracies have been removed.

If a nontrivial relation survives those steps, its mathematical form must be frozen before a fresh withheld-family or mechanism test. Only a relation that survives such a prospective test becomes a candidate for interpretation as a more universal dark-sector regularity. Reconstruction of an underlying action or dynamics is a still later question.

A parallel goal is to determine whether mechanism-native localization coordinates---viscous transitions, Compton-like transitions, free-streaming cutoffs, decay epochs, and others---can be mapped into a common observable coordinate without erasing the physical distinctions that make the atlas informative. The present results justify asking that question, but do not prejudge the answer.

# 12. Conclusions

We introduced DSIR as a model-agnostic response-space framework for comparing heterogeneous dark-sector mechanisms under explicitly specified physical channels and measurement operators. The current atlas yields four main conclusions.

First, model degeneracy is channel conditional. GDM pressure and viscosity are nearly indistinguishable in low-\(k\) matter power yet strongly separated by metric slip, while GDM and designer \(f(R)\) are nearly aligned in a scale-only mode but separated by temporal/full response structure.

Second, the scale and time dependence of the response cannot always be treated as independent additive summaries. The irreducible scale-time component is negligible for the tested IDE directions, weak for smooth dark energy, moderate for GDM, and strong for designer \(f(R)\); this descriptive tier ordering persists across finite amplitudes and all 12 single-node deletion tests.

Third, response-space complexity is not equivalent to microscopic parameter count. One-parameter physical families can curve substantially, producing several useful linear representation modes without introducing additional microscopic degrees of freedom.

Fourth, mechanism diversity matters. Thermal WDM exhibits a strong scale-localized but nearly time-separable response, whereas withheld DCDM produces a distinct temporal-localization flow. These cases support the use of response localization and trajectory geometry as organizing tools while simultaneously ruling out a naive universal scale-time template.

The scientific message is therefore deliberately constrained: the dark sector is not yet reconstructed, but its candidate mechanisms can already be organized by a reproducible geometry of observable influence. The next test is whether any relation in that geometry survives full observational quotienting and a genuinely fresh withheld prediction.