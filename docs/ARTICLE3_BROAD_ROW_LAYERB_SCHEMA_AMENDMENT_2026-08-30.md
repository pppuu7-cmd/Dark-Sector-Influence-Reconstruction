# Article 3 broad-row Layer-B representation amendment

**Frozen:** 2026-08-30, after Exp073U froze the immutable 1410-observation-row order, but **before any real current Article-3 Layer-A or Layer-B support score is evaluated and before covariance inspection**.

## Why this amendment is required

The current Article-3 architecture correctly requires two different support gates:

1. **Layer A** — broad finite-operator leakage under the full positive observation-window envelope;
2. **Layer B** — common final-response numerical validity.

However, the older Layer-B contract in `docs/ARTICLE3_PHYSICAL_SUPPORT_GATE_CONTRACT_2026-08-28.md` was written for rows carrying one scalar canonical `z` and one scalar canonical `k_Mpc^-1`. That representation is not valid for the current finite survey observables:

- a DES Wm/WW pseudo-`C_ell` bandpower has a broad NaMaster bandpower window and a broad redshift kernel;
- a BOSS observed multipole row is a broad finite matrix row `C = W @ M` over true-`k` cells and also belongs to a finite survey redshift selection;
- Exp073U therefore correctly froze observation-row identity/order while deliberately leaving scalar `z`/`k` unbound.

Assigning an effective `ell`, effective `z`, weighted-mean `k`, midpoint `k`, centroid `k`, or any equivalent scalar proxy would erase broad out-of-domain support and could make a row pass Layer B even when its real finite operator fails Layer A. That shortcut is forbidden.

This amendment resolves the representation prospectively. No real Layer-A or Layer-B outcome exists at freeze time, so the correction is not conditioned on a result.

## Observation row versus physical support atom

From this point onward, distinguish two objects.

### Observation row

An observation row is the finite measured coordinate that later indexes the data vector and covariance. It keeps exactly:

- immutable `coordinate_id`;
- immutable inherited `ordinal`;
- observable block (`Wm`, `WW`, or `BOSS`);
- pointer/hash into its broad physical-support representation.

The observation row itself has **no scalar physical `z` or `k` field** for the current Wm/WW/BOSS route.

### Physical support atom

A support atom is one element of the deterministic quadrature/operator representation of an observation row. Every active atom carries canonical float64:

- `z`;
- `k_Mpc^-1`;
- non-negative `operator_abs_weight`;
- ordered `final_response_abs_values` for the prospectively frozen common response components.

The physical domain is evaluated on atoms, not on an invented point label for the observation row.

## Frozen physical domain

The physical rectangle is unchanged:

\[
D = \{(z,k): 0.295 \le z \le 2.33,\; 0 < k \le 0.06664762008318016\;{\rm Mpc}^{-1}\}.
\]

Boundary comparisons are exact on canonical float64 values. The Layer-A acceptance threshold remains exactly and inclusively `0.05`; the minimum retained observation-row dimension remains exactly `15`.

## Layer A — unchanged scientific quantity in broad-row form

For observation row `i` with support atoms `a` and non-negative positive-envelope weights `w_ia`, define

\[
f_{\rm op}(i)=
\frac{\sum_a w_{ia}\,\mathbf{1}[(z_{ia},k_{ia})\notin D]}
     {\sum_a w_{ia}}.
\]

Requirements:

- every atom coordinate and weight must be finite;
- all `k` values representing physical Fourier cells must be strictly positive;
- all weights must be non-negative;
- total row weight must be finite and strictly positive;
- no fiducial `P(k)`, nonlinear boost, covariance, nuisance, relation/null, G7 or G8 weighting may enter `w`;
- `f_op(i) <= 0.05` retains the observation row in `S_op`;
- `f_op(i) > 0.05` rejects it under the frozen scientific support criterion;
- the inherited Exp073U ordinal order is preserved exactly.

The measured Wm observable remains signed. Absolute value is used only for the support-envelope bookkeeping already preregistered for Layer A.

## Layer B — common response validity on the inherited broad support

Layer B receives only the already frozen Layer-A retained observation set `S_op` and its immutable support atoms. It may not rebuild, narrow, renormalize or recenter the Layer-A operator after seeing the support result.

For each `i in S_op`, define the active in-domain atom set

\[
A_i^D=\{a:\;w_{ia}>0\;\text{and}\;(z_{ia},k_{ia})\in D\}.
\]

The row has a valid common final-response field iff:

1. `A_i^D` is non-empty; and
2. for **every** atom `a in A_i^D` and every preregistered response component `c`, `R_{iac}=final_response_abs_values[a,c]` is finite and strictly positive.

No response component may be silently removed. Zero, NaN, `+Inf`, or `-Inf` in any required active in-domain response cell makes that observation row Layer-B invalid.

The Layer-B row-count invalid fraction is

\[
f_{\rm B}=\frac{N_{\rm invalid\ common\ response\ rows}}{|S_{\rm op}|}.
\]

Here `S_op` is the broad-row replacement for the older contract's geometrically eligible row set: broad physical geometry has already been certified row-by-row by Layer A, rather than by a scalar point predicate. The acceptance boundary remains exactly and inclusively

\[
f_{\rm B}\le 0.05.
\]

After removing Layer-B-invalid rows, at least `15` observation rows must remain. Their order is inherited from Exp073U through `S_op`; amplitude, covariance, uncertainty, nuisance alignment or relation statistics may not reorder them.

## Exact scope of supersession

For the current Wm/WW/BOSS broad-observation route, this document prospectively supersedes only those clauses of the older Layer-B contract that require a single row-level scalar `z` and `k_Mpc^-1` or derive geometric eligibility from those scalar fields.

It does **not** loosen:

- the physical `z` bounds;
- the physical `k` bound;
- either inclusive `0.05` acceptance boundary;
- the minimum retained dimension `15`;
- the finite/strictly-positive common-response rule;
- inherited coordinate identity/order;
- anti-leakage rules;
- PASS / scientific FAIL / INVALID_FOR_SCIENCE separation;
- the requirement that both Layer A and Layer B pass before covariance restriction.

A future genuinely point-localized observable may use a separately frozen scalar-coordinate representation, but that does not authorize scalarization of the present broad rows.

## Canonical production-array contract

The later real broad-operator producer must serialize the physical representation without duplicating a huge JSON object. For each block it must bind canonical logical arrays:

- `row_ptr`: little-endian int64 CSR offsets, shape `[n_rows+1]`;
- `z`: little-endian float64 atom array;
- `k_Mpc^-1`: little-endian float64 atom array;
- `operator_abs_weight`: little-endian float64 atom array;
- `final_response_abs_values`: little-endian float64 matrix `[n_atoms,n_components]`;
- ordered response-component names and their SHA256;
- inherited ordered observation IDs and their SHA256.

Authority is the SHA256 of each canonical logical byte buffer together with dtype/shape metadata, not ZIP/NPZ container metadata. A transport container such as NPZ is allowed only as a carrier.

The full current observation order must remain exactly the Exp073U order SHA256

`bfaf582518cdbfd34b1e8392da83dac6b0885948bc31f2c29d4e48247c23af75`.

## Block construction semantics

### DES Wm / WW

The real producer must derive support atoms from the pinned Cosmotheka/NaMaster finite bandpower-window operator and the exact released redshift kernels. Structurally, a positive support atom is the deterministic quadrature contribution of an unbinned harmonic cell and a redshift-kernel cell to the absolute bandpower response. No fiducial matter power spectrum is allowed in that support weight.

The classifying route remains `nside=4096` with the already frozen bandpower edges and component identities (`TE` for Wm, `EE` for WW).

### BOSS

The real producer must preserve the frozen `C=W@M` row geometry and its true-`k` cells. A weighted-mean or midpoint `k` is forbidden. The redshift part must be bound to the actual frozen BOSS survey-bin support/provenance before the final real broad manifest is classifying; the earlier k-only component audit is not by itself a full broad `(z,k)` producer.

This last point is a newly exposed implementation dependency, not a scientific FAIL.

## Anti-leakage firewall

Neither broad-operator construction nor Layer A/B may read or depend on:

- covariance or inverse covariance;
- whitening/Cholesky products;
- nuisance vectors, SVD/rank or quotient geometry;
- relation/null residuals;
- p-values or chi-squared;
- G7/G8/G9 outputs;
- article/claim selection metadata.

Required metadata remains:

- `normalization_scope=FULL_PRE_SUPPORT_COORDINATE_SET`;
- `crop_before_normalization=false`;
- `fiducial_P_weighting=false`;
- `effective_ell_override=false`;
- `effective_z_override=false`;
- `effective_k_override=false`;
- `signed_Wm=true`;
- `selection_reads=[]`.

## Classification and covariance authorization

Layer A labels remain:

- `PASS_ARTICLE3_OPERATOR_SUPPORT_V0_1`;
- `FAIL_ARTICLE3_OPERATOR_SUPPORT_V0_1`;
- `INVALID_FOR_SCIENCE_ARTICLE3_OPERATOR_SUPPORT_V0_1`.

Layer B labels remain:

- `PASS_PHYSICAL_SUPPORT_ARTICLE3`;
- `FAIL_PHYSICAL_SUPPORT_ARTICLE3`;
- `INVALID_FOR_SCIENCE_ARTICLE3_SUPPORT`.

Covariance restriction is authorized only after a real artifact chain proves **both** Layer-A PASS and Layer-B PASS on the same inherited Exp073U authority. This amendment and its synthetic QA authorize no covariance access and earn no scientific-readiness credit by themselves.

## Immediate next step

Run Exp073V synthetic architecture QA against this broad-row schema. If it passes, the next real implementation task is to bind the actual DES broad NaMaster-window × redshift-kernel atomization and the BOSS true-`k` × survey-redshift support into a content-hashed pre-support operator manifest. Only after that manifest is frozen may the first real Layer-A score be computed.
