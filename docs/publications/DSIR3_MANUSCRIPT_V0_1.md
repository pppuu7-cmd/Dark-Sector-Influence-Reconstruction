# Dark-Sector Influence Reconstruction III: Covariance-whitened, nuisance-quotiented observation-space reconstruction

**Manuscript status:** v0.1, pre-G7 gate-aware draft  
**Date:** 2026-08-29  
**Branch:** `article3-manuscript-start-2026-08-29`  
**Scientific status:** Methods and interpretation architecture are draftable from prospectively frozen contracts. Real DES-Y1 physical-support, covariance/whitening, nuisance quotient, and G7 result text remains blocked until the corresponding gates terminate.

> Editorial rule: this manuscript must remain scientifically valid under either a positive, null, or negative G7 outcome. No result-dependent language may be promoted into the abstract, title, discussion, or conclusion before immutable terminal evidence exists.

## Abstract — pre-result scaffold

Cosmological model comparison is usually performed in parameter space or through a selected set of summary observables. Such comparisons can overstate physical specificity when different mechanisms produce similar responses, when nuisance freedom is represented by a selected one-sided direction, or when theoretical response geometry is interpreted before survey support and covariance are imposed. We develop the third stage of Dark-Sector Influence Reconstruction (DSIR), an observation-space framework that carries solver-validated physical responses through a prospectively frozen sequence of support selection, finite observation operators, covariance restriction and whitening, complete signed nuisance-subspace construction, and quotient-space reconstruction. The framework treats support failure, covariance invalidity, unresolved nuisance directions, and scientific null results as distinct terminal outcomes. For a support-restricted response vector $x_S$ and covariance $C_S=LL^T$, responses are whitened as $w=L^{-1}x_S$. Resolved nuisance tangents form a matrix $N_w$, whose thin singular-value decomposition defines the nuisance projector $P_N=U_rU_r^T$. The nuisance-orthogonal target response is then $y_\perp=(I-P_N)y$, with survival fraction $\eta_N=\|y_\perp\|_2/\|y\|_2$. We additionally separate geometric nuisance overlap from causal interpretation by distinguishing exogenous, mediated, and causally unresolved nuisance families. **[RESULT SLOT: insert terminal physical-support, covariance, nuisance-rank, quotient, and G7 classifications only after immutable gate closure.]** This construction provides a falsification-resistant route from theory-response equivalence to survey-conditioned identifiability without treating a favorable intermediate representation as observational evidence.

## 1. Introduction

The observational inference of dark-sector physics is an inverse problem with several distinct sources of non-identifiability. Different microscopic models can produce similar perturbation responses; different physical channels can carry different amounts of discriminatory information; known-sector parameter variations can mimic a target response; and the survey observation operator, window functions, finite support, covariance, and nuisance parameters can change which directions are actually distinguishable.

DSIR addresses this hierarchy by comparing models through their influence on a common response space rather than assuming that model labels themselves define observationally distinct hypotheses. Earlier stages established two lessons that motivate the present paper. First, response equivalence is representation- and channel-dependent: a direction can be apparently discriminating in one representation yet overlap a known-sector control after the physically correct sign freedom or missing response contribution is restored. Second, the correct nuisance object for an interior parameter is generally a line or higher-dimensional subspace, not a selected positive ray. These results imply that theory-space angles alone cannot establish survey distinguishability.

This paper moves the analysis into observation space. Its central question is deliberately narrower than a dark-sector detection claim:

**Which components of a solver-validated dark-sector response remain identifiable after the physical support, observation operator, released covariance, and the complete preregistered nuisance span are imposed?**

The construction is designed so that a null answer remains scientifically informative. If a target response is absorbed by the observational nuisance quotient, that is a result about identifiability rather than an infrastructure failure. Conversely, a response that survives the quotient is not automatically evidence for new fundamental physics; it must still pass the relation/null gate and later genuinely withheld-family falsification.

The methodological hierarchy used throughout the paper is

`causal status -> representation -> resolvability -> physical sign/subspace geometry -> physical support -> finite observation operator -> covariance restriction/whitening -> nuisance quotient -> relation/null -> later withheld falsification`.

This ordering is not rhetorical. Each arrow corresponds to a fail-closed gate whose output becomes an immutable parent of the next stage.

## 2. From physical response to observation space

### 2.1 Response vectors and observational representation

Let a physical model perturbation produce a finite response vector $r$ in a preregistered physical representation. Let $A$ denote the finite observation operator, including the frozen mapping from the physical response coordinates into the survey-level coordinate system. The pre-support observation response is

$$
x = A r.
$$

A model or nuisance direction is meaningful for comparison only in a representation that resolves it. Nullity in an intermediate transfer or theory representation is not sufficient to conclude physical irrelevance, because primordial, tracer, calibration, projection, or window factors may restore the response in the final observation representation.

### 2.2 Physical-support gate

The support decision is made before covariance or nuisance geometry is inspected. A coordinate is geometrically eligible only on the prospectively frozen physical domain

$$
0.295 \le z \le 2.33,
\qquad
0 < k \le 0.06664762008318016\,\mathrm{Mpc}^{-1}.
$$

For every geometrically eligible coordinate, all preregistered components of the final absolute response envelope must be finite and strictly positive. Define

$$
f_{\rm invalid}=
\frac{N_{\rm geom\ eligible\ but\ envelope\ invalid}}
{N_{\rm geom\ eligible}}.
$$

The frozen support criterion is

$$
f_{\rm invalid}\le 0.05,
$$

with at least 15 retained coordinates. The retained coordinate sequence is ordered only by the inherited immutable ordinal. Signal amplitude, covariance, nuisance alignment, relation score, or any later statistic is forbidden from influencing support selection.

The support gate has three semantically distinct outcomes: scientific PASS, scientific FAIL under valid provenance, and `INVALID_FOR_SCIENCE` for malformed provenance or forbidden downstream leakage. This separation prevents an execution-integrity failure from being misreported as evidence against a physical model.

## 3. Covariance restriction and whitening

Let $S$ be the immutable retained coordinate sequence after physical-support PASS, with dimension $d$. The observational covariance is restricted to exactly this coordinate sequence, yielding

$$
C_S\in\mathbb{R}^{d\times d}.
$$

The coordinate identity and ordering of $C_S$ must match the support manifest exactly, up to only a prospectively declared permutation. A mismatch is an invalid covariance binding, not a scientific null.

The covariance must pass finiteness, strictly positive diagonal, raw symmetry, and ordinary Cholesky positive-definiteness gates. With

$$
C_{\rm sym}=LL^T,
$$

whitening is defined by a triangular solve rather than explicit inversion:

$$
w=L^{-1}x_S,
$$

so that

$$
\|w\|_2^2=x_S^T C_S^{-1}x_S.
$$

No post-hoc diagonal jitter, eigenvalue clipping, nearest-SPD replacement, covariance-mode deletion, or target-informed repair is permitted. The symmetry, Cholesky reconstruction, and whitening residuals are recorded as numerical diagnostics under prospectively frozen tolerances.

This stage converts ordinary Euclidean response geometry into the metric implied by the released observational covariance. Crucially, covariance whitening is not allowed to retroactively modify the physical support.

## 4. Complete signed nuisance subspace

### 4.1 Two-sided finite responses

For each preregistered interior nuisance parameter $p_j$, both physically admissible signs are evaluated around the same reference point using a fixed step $\delta_j$:

$$
d_j^+=x_S(p_j+\delta_j)-x_S(\mathrm{ref}),
$$

$$
d_j^-=x_S(p_j-\delta_j)-x_S(\mathrm{ref}).
$$

The same Cholesky factor whitens both branches,

$$
q_j^+=L^{-1}d_j^+,
\qquad
q_j^-=L^{-1}d_j^-.
$$

A central local tangent is

$$
n_j=\frac{q_j^+-q_j^-}{2\delta_j}.
$$

Both signs are retained for diagnostics rather than assuming from one oriented ray that the local nuisance freedom is linear and two-sided.

### 4.2 Antisymmetry and local-line diagnostics

For every two-sided nuisance direction we report

$$
\epsilon_{\mathrm{anti},j}=
\frac{\|q_j^++q_j^-\|_2}
{(\|q_j^+\|_2+\|q_j^-\|_2)/2}.
$$

The mutual plus/minus angle and preregistered step-size stability are recorded when available. Failure of the frozen local-linearity criterion does not authorize selecting the more favorable sign; it triggers the preregistered nonlinear-nuisance handling state or an explicit invalidity classification.

### 4.3 Nuisance SVD and projector

Collect all resolved nuisance tangents into

$$
N_w=[n_1,n_2,\ldots,n_m].
$$

We compute the thin singular-value decomposition

$$
N_w=U\Sigma V^T.
$$

The prospectively defined numerical-rank rule selects $U_r$, giving the orthogonal nuisance projector in whitened space

$$
P_N=U_rU_r^T.
$$

This form avoids unnecessarily squaring the condition number through direct normal-equation inversion. The rank decision is independent of the target response. Singular values, retained rank, orthogonality error, projector idempotence error, null columns, and near-collinearity diagnostics are persisted.

Required software invariances include basis changes $N_w\to N_wA$ for nonsingular $A$, arbitrary nuisance-column sign flips, and simultaneous permutations of response, covariance, and nuisance coordinates.

## 5. Quotient-space reconstruction

Let the whitened target response be

$$
y=L^{-1}r_S.
$$

The component orthogonal to the complete resolved nuisance span is

$$
y_\perp=(I-P_N)y.
$$

We use two primary geometric summaries:

$$
\eta_N=\frac{\|y_\perp\|_2}{\|y\|_2},
$$

and

$$
\theta_N=\arcsin(\eta_N).
$$

Here $\eta_N=0$ means that, locally and in the frozen whitened observation representation, the target lies entirely inside the tested nuisance span; $\eta_N=1$ means it is orthogonal to that span. Intermediate values quantify surviving nuisance-orthogonal response norm. These quantities are geometry diagnostics, not by themselves detection significances.

Consistency requires

$$
\|U_r^Ty_\perp\|\simeq 0
$$

and

$$
\|y\|^2\simeq\|P_Ny\|^2+\|y_\perp\|^2.
$$

The quotient is evaluated only after support and covariance gates are terminal. No coordinate or nuisance direction may be removed because it decreases $\eta_N$.

## 6. Causal status of nuisance overlap

Geometric nuisance overlap and causal interpretation are not equivalent. A response direction that looks like known-sector physics can represent either an independent mimic

$$
K\rightarrow O,
$$

or a mediated dark-sector response

$$
D\rightarrow K(D)\rightarrow O.
$$

Accordingly, each nuisance family must be classified independently of the target residual into one of three causal-status sets:

- $N_{\rm exo}$: exogeneity justified for the declared dark-sector intervention;
- $N_{\rm med}$: explicitly modelled as a possible mediator;
- $N_{\rm unknown}$: causal status unresolved.

The full operational quotient remains well defined using $N_{\rm all}$, but interpretation distinguishes

$$
\eta_{\rm all}
$$

from

$$
\eta_{\rm exo},
$$

when a defensible exogenous subset exists. Overlap with mediated or causally unresolved directions is reported separately rather than labelled automatically as non-dark-sector contamination.

A direction may be promoted to mediated status only through an explicit coupled forward model or intervention-defined decomposition, not because it happens to align with the target.

## 7. Gate semantics and preregistered result logic

The Article-3 chain is fail closed:

1. exact upstream survey reconstruction;
2. physical-support classification;
3. finite observation-operator binding;
4. covariance coordinate binding and numerical validation;
5. Cholesky whitening;
6. full signed nuisance-family execution and rank determination;
7. nuisance quotient;
8. G7 relation/null test;
9. only subsequently, a genuinely fresh G8 withheld-family test.

The manuscript distinguishes three broad outcome types.

**Scientific PASS:** a preregistered criterion is satisfied under valid immutable provenance. This authorizes only the explicitly defined next stage.

**Scientific FAIL/NULL:** provenance and execution are valid, but the frozen scientific criterion is not met. This is preserved as scientific evidence and is not repaired by changing thresholds, coordinates, nuisance families, or covariance modes.

**INVALID FOR SCIENCE:** provenance, representation, coordinate binding, numerical integrity, or anti-leakage requirements fail. This blocks interpretation and must not be counted as evidence for or against dark-sector physics.

## 8. Results — terminal slots

This section is intentionally incomplete in v0.1. Values and classifications are inserted only from immutable terminal artifacts.

### 8.1 Upstream observation-space reconstruction

**[RESULT SLOT R1]** Record the terminal authoritative reconstruction run, job, artifact ID, artifact digest, exact PASS token, and retained survey coordinate manifest. If reconstruction remains infrastructure-incomplete, state that Article-3 scientific scoring is blocked and do not populate downstream result slots.

### 8.2 Physical support

**[RESULT SLOT R2]** Report candidate count, geometrically eligible count, invalid-envelope count, $f_{\rm invalid}$, retained count, ordered coordinate-manifest digest, and one frozen support classification.

### 8.3 Covariance validation and whitening

**[RESULT SLOT R3]** Report covariance source identity, support-coordinate binding digest, $d$, raw symmetry residual, Cholesky residual, whitening residual, diagnostic eigenvalue range and condition number, and terminal covariance classification.

### 8.4 Signed nuisance rank

**[RESULT SLOT R4]** Report preregistered nuisance families and steps, causal-status labels, plus/minus diagnostics, all singular values, numerical-rank threshold, retained nuisance rank, unresolved directions, projector diagnostics, and basis/sign/permutation invariance checks.

### 8.5 Quotient reconstruction

**[RESULT SLOT R5]** For each tested target response report $\|y\|$, $\|P_Ny\|$, $\|y_\perp\|$, $\eta_{\rm all}$, $\theta_{\rm all}$, and, where causally justified, $\eta_{\rm exo}$ plus mediated/unknown overlap diagnostics.

### 8.6 G7 relation/null test

**[RESULT SLOT R6]** Insert only the preregistered G7 statistic, frozen threshold or null logic, complete immutable provenance, and terminal classification. A null G7 result is reported as an observational identifiability result, not suppressed.

## 9. Discussion — outcome-stable core

Several conclusions do not depend on the eventual sign of G7. First, observational distinguishability is a property of a model response **after** representation, support, observation operators, covariance metric, and nuisance freedom have been fixed. A large theory-space angle cannot be promoted directly to survey specificity.

Second, the nuisance quotient must remove a complete resolved subspace rather than a selected nuisance ray. This is both a geometric and numerical requirement: the projector is invariant to nuisance basis and sign, while a ray-level comparison is not.

Third, support and covariance choices are themselves potential sources of selection leakage. By freezing physical support before covariance access and freezing covariance validity before nuisance projection, the framework prevents the target response from influencing which coordinates or modes are admitted.

Fourth, a small quotient residual does not prove that the dark-sector mechanism is absent. It means that the tested observation response is locally representable by the operational nuisance span in the frozen metric. Causal interpretation requires distinguishing exogenous nuisance directions from possible mediators and unresolved causal status.

Fifth, a large quotient residual is not by itself evidence for new fundamental physics. It indicates that the tested response has a component outside the preregistered nuisance span under the frozen observational metric. The residual must still survive the G7 relation/null logic and a later genuinely withheld G8 family before stronger cross-family statements are entertained.

### 9.1 Positive-G7 branch

**[DISCUSSION SLOT D+]** If G7 passes, discuss only the surviving preregistered observational relation. Explicitly state that G8 remains fresh and that no new-law language is authorized by G7 alone.

### 9.2 Null/negative-G7 branch

**[DISCUSSION SLOT D0]** If G7 is null or fails under valid provenance, emphasize the resulting empirical bound on observation-space identifiability and identify which stage — support, covariance metric, nuisance rank, or quotient geometry — removes the apparent theory-space distinction. Do not redesign the relation on the same data.

### 9.3 Invalid/infrastructure branch

**[DISCUSSION SLOT DI]** If an integrity or infrastructure gate remains incomplete, report the precise blocking stage and preserve all downstream quantities as unevaluated rather than zero, null, or failed.

## 10. Limitations

The quotient is local in the preregistered nuisance tangent construction unless a nonlinear nuisance treatment is explicitly introduced prospectively. The tested nuisance family set is finite and cannot establish freedom from every conceivable systematic or known-sector deformation. The covariance metric is tied to a specific released observational representation and should not be interpreted as universal across surveys. Causal classification may remain unresolved for nuisance-like responses without an explicit coupled forward model. Finally, G7 is not a withheld-family falsification; that role is reserved for the subsequent G8 stage.

## 11. Conclusions — pre-result scaffold

We formulate an observation-space extension of Dark-Sector Influence Reconstruction in which physical responses are admitted only through a prospectively frozen sequence of support, observation-operator, covariance, and nuisance-subspace gates. The construction defines survey-conditioned response geometry through Cholesky whitening and removes the complete resolved nuisance span with a numerically stable SVD projector. It also separates geometric nuisance overlap from claims of causal exogeneity.

**[CONCLUSION RESULT SLOT]** Insert only the terminal Article-3 support, covariance, quotient, and G7 conclusions supported by immutable artifacts.

Regardless of the terminal G7 outcome, the framework establishes a falsification-resistant distinction between (i) response components that survive a declared observational nuisance quotient, (ii) components that are observationally degenerate with the tested nuisance span, and (iii) cases that are not scientifically classifiable because an upstream integrity gate failed. This separation is necessary before any stronger claim about a cross-model dark-sector regularity or new physics is considered.

## Appendix A. Frozen mathematical objects

For manuscript consistency, the canonical objects are:

$$
S=\text{ordered retained physical-support coordinate set},
$$

$$
C_S=LL^T,
$$

$$
w=L^{-1}x_S,
$$

$$
N_w=U\Sigma V^T,
$$

$$
P_N=U_rU_r^T,
$$

$$
y_\perp=(I-P_N)y,
$$

$$
\eta_N=\frac{\|y_\perp\|}{\|y\|},
\qquad
\theta_N=\arcsin\eta_N.
$$

## Appendix B. Manuscript claim firewall

Until the corresponding terminal evidence exists, this manuscript must not claim:

- a real DES-Y1 Article-3 physical-support PASS;
- real covariance whitening PASS;
- a measured nuisance rank;
- a measured $\eta_N$ or $\theta_N$;
- observational distinguishability of any dark-sector family;
- a completed G7 relation/null classification;
- a G8 withheld-family result;
- a discovery of dark-sector physics or a universal residual law.

Architecture-level claims may be made only as preregistered methodology, clearly separated from executed scientific results.
