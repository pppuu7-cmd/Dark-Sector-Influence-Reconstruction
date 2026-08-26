# DSIR channel-conditional equivalence and quotient theorems

**Date:** 2026-08-27  
**Status:** mathematical synthesis / definitions; no new empirical gate and no discovery claim

## 1. Purpose

The numerical DSIR atlas repeatedly shows that two mechanisms may be nearly indistinguishable in one response block and strongly separated in another. This note gives the precise linear-algebraic meaning of that statement and connects theory-space responses to the later covariance/nuisance G7 construction.

The result is deliberately modest: it formalizes **identifiability under a specified measurement operator**. It does not assert a universal dark-sector law.

## 2. Response and observational operators

Let a model/family state be represented by a theory-response vector

\[
r(\theta)\in\mathbb R^n,
\]

where the coordinates may contain background, matter-growth, Weyl/slip, transfer or other explicitly defined response blocks.

For a chosen observable/channel set `B`, define the linearized physical projection/window operator

\[
K_B:\mathbb R^n\rightarrow\mathbb R^{m_B}.
\]

Let the released/validated covariance in that data space be positive definite,

\[
C_B=L_BL_B^T,
\]

with invertible whitener

\[
W_B=L_B^{-1}.
\]

Let the whitened nuisance tangent matrix have retained column space

\[
\mathcal N_B=\operatorname{col}(U_{\eta,B}),
\]

and define the orthogonal nuisance quotient projector

\[
Q_B=I-U_{\eta,B}U_{\eta,B}^T.
\]

The DSIR observational signature operator is then

\[
A_B=Q_BW_BK_B,
\]

and the quotient-space signature of a theory state is

\[
s_B(\theta)=A_Br(\theta).
\]

This formula is the formal target of the existing DSIR ordering

`physical provider -> support mask -> covariance/whitening -> nuisance SVD -> quotient -> relation/null test`.

## 3. Definition: exact channel-conditional equivalence

Two model states `r_1,r_2` are exactly equivalent under channel set `B` iff

\[
r_1\sim_B r_2
\quad\Longleftrightarrow\quad
A_B(r_1-r_2)=0.
\]

Equivalently,

\[
r_1-r_2\in\ker A_B.
\]

Therefore observational equivalence is not an intrinsic relation between microscopic model labels. It is an equivalence relation induced by the selected physical channels, windows, covariance and nuisance quotient.

This directly explains why a parameter translator must always state its response subspace. A map such as

\[
\theta_i\mapsto\theta_j^*(B)
\]

has no reason to agree with the map obtained from another channel set `C`.

## 4. Whitening theorem: whitening changes metric, not exact pre-nuisance nulls

Because `W_B` is invertible whenever the validated covariance is positive definite,

\[
\ker(W_BK_B)=\ker K_B.
\]

Thus covariance whitening changes distances and relative weighting but does not by itself create or remove an **exact** physical degeneracy before nuisance quotienting.

This distinction matters:

- exact physical null/equivalence is controlled by `K_B`;
- statistical distinguishability is controlled by the covariance-weighted norm;
- nuisance quotient can enlarge the effective observational degeneracy.

## 5. Nuisance-quotient theorem

Since `Q_B` removes the retained nuisance subspace,

\[
A_B\Delta r=0
\]

iff

\[
W_BK_B\Delta r\in\mathcal N_B.
\]

Therefore

\[
\ker(Q_BW_BK_B)
=
\{\Delta r: W_BK_B\Delta r\in\mathcal N_B\}.
\]

A physical response need not vanish to become observationally unidentifiable: it is enough for its whitened data-space displacement to lie entirely inside the nuisance tangent space.

This is the precise DSIR meaning of quotienting measurement/identity degeneracies before searching for a residual law.

## 6. Compatible channel-refinement theorem

Consider two independently represented channel blocks `B` and `C`. Suppose their joint signature is constructed by stacking their already-defined quotient signatures without redefining either nuisance quotient:

\[
A_{B\oplus C}
=
\begin{bmatrix}
A_B\\
A_C
\end{bmatrix}.
\]

Then

\[
\ker A_{B\oplus C}
=
\ker A_B\cap\ker A_C.
\]

Hence

\[
r_1\sim_{B\oplus C}r_2
\Longrightarrow
r_1\sim_B r_2
\quad\text{and}\quad
r_1\sim_C r_2.
\]

The converse need not hold for either channel separately.

### Consequence

Under compatible channel stacking, adding an independent channel can only

- leave an existing exact equivalence class unchanged, or
- split it into finer classes.

It cannot merge two states that were already distinguishable in one retained channel.

This gives a rigorous form to the empirical DSIR pattern in which matter-response lookalikes separate once an independent slip/Weyl block is added.

## 7. Important caveat: joint nuisance re-fitting

The refinement theorem above requires compatible channel stacking. If the combined analysis introduces a **new shared nuisance parameterization** and recomputes one joint nuisance subspace,

\[
Q_{B\cup C}\neq Q_B\oplus Q_C,
\]

then kernel monotonicity is not automatic.

A new shared nuisance direction can absorb a cross-channel displacement that neither separately defined quotient absorbed, or conversely cross-channel coherence can break a degeneracy that existed separately.

Therefore a real multi-probe DSIR analysis must recompute the joint nuisance tangent rank under a prospectively frozen rule. It is not valid to infer joint identifiability from theory-space channel angles alone.

## 8. Covariance-weighted quotient distance

For two states define

\[
D_B(r_1,r_2)
=
\|A_B(r_1-r_2)\|_2.
\]

Then

\[
D_B^2
=
\Delta r^T K_B^T W_B^TQ_BW_BK_B\Delta r,
\]

because `Q_B=Q_B^T=Q_B^2`.

This distance is:

- physical-window aware;
- covariance weighted;
- nuisance quotiented;
- channel conditional.

It is the appropriate object for an observational cross-model translator once the physical providers and nuisance quotient are certified.

The existing lightweight translator based only on response summaries is therefore a theory-geometry proof of concept, not yet this observational metric.

## 9. Local identifiability and tangent Gram matrix

For a model family `r(\theta)` with Jacobian

\[
J_\theta=\frac{\partial r}{\partial\theta},
\]

the quotient-space local tangent matrix is

\[
T_B=A_BJ_\theta.
\]

The local Gram/Fisher-like matrix is

\[
G_B=T_B^TT_B
=J_\theta^TA_B^TA_BJ_\theta.
\]

Its rank gives the number of locally distinguishable parameter combinations **for that chosen channel/covariance/nuisance construction**.

Therefore

\[
N_{\rm observable,local}=\operatorname{rank}(T_B)
\]

must not be identified with

- microscopic parameter count `N_micro`,
- global manifold dimension,
- raw SVD representation rank `N_repr`, or
- minimum discriminant count `N_disc`.

This extends the existing DSIR dimension-bookkeeping rule into observation space.

## 10. Why a nearly one-dimensional path need not be invertible

Suppose a one-parameter family traces a curve `s_B(\theta)`. Even if its centered sampled covariance is almost rank one, the scalar coordinate along that line need not be monotone in `theta`.

If

\[
\frac{d s_B}{d\theta}
\]

changes sign along the same dominant direction, the path backtracks while remaining geometrically almost one-dimensional.

Thus low representation dimension does not imply an injective inverse map

\[
s_B\mapsto\theta.
\]

This is the mathematical interpretation of the post-unblinding K2 control and similar backtracking families: compression and identifiability are distinct questions.

## 11. Relation to normalized response-direction rotation

For a nonzero raw response `r(\theta)`, define

\[
u(\theta)=\frac{r(\theta)}{\|r(\theta)\|}.
\]

Then

\[
\frac{du}{d\theta}
=
\frac{(I-uu^T)}{\|r\|}\frac{dr}{d\theta}.
\]

Only the component of `dr/dtheta` orthogonal to the current response direction rotates the normalized path. Pure amplitude rescaling leaves `u` fixed.

Therefore normalized-path curvature/F30-type operators measure shape-direction evolution, not uniquely dark-sector physics. A known-sector transfer mechanism can rotate response direction for entirely ordinary reasons.

## 12. Falsifiable DSIR consequence

The formalism suggests the following prospective logic for later G7/G8 work:

1. identify a matter-space near-equivalence pair or family relation;
2. freeze an independent Weyl/lensing channel and observational quotient;
3. test whether the additional channel splits the matter-only equivalence class under `D_{matter+Weyl}`;
4. include known-sector controls under exactly the same operator;
5. only then ask whether any residual cross-channel relation is specific enough for a fresh withheld-family G8 test.

This is a research program, not a currently established law.

## 13. Current scientific conclusion

The central DSIR concept can now be stated mathematically as:

> models are not compared by a single global distance; they are compared through a hierarchy of channel-, covariance- and nuisance-dependent quotient signatures, whose kernels define observational equivalence classes.

The empirical atlas currently supports the need for this construction, especially the separation between matter-only lookalikes and independent slip/Weyl information. It does not yet establish a universal dark-sector invariant.

**Gate state remains:** `G7=OPEN`, `G8=OPEN`, `G9=OPEN`.
