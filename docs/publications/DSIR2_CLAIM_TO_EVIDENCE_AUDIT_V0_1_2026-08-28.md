# DSIR-2 claim-to-evidence audit — v0.1

**Date:** 2026-08-28  
**Audited manuscript:** `DSIR2_MANUSCRIPT_V0_5.md`  
**Canonical science boundary:** `docs/ARTICLE2_CLAIM_MATRIX_CURRENT.md` and `docs/ARTICLE2_FINAL_SCIENCE_CLOSURE_AUDIT_2026-08-28.md` on `main`.

Legend:

- ✅ **SUPPORTED** — wording is within the current canonical evidence boundary.
- ⚠️ **SUPPORTED / PROVENANCE FOLLOW-UP** — scientific wording is supported, but release-candidate provenance or bibliography still needs a final exact audit.
- ❌ **NOT ALLOWED** — wording would exceed current evidence. No such wording should remain in the active manuscript.

## 1. Abstract audit

| Claim | Evidence | Verdict | Notes |
|---|---|---|---|
| K2 reproduces inherited matter-response morphology and therefore matter-only morphology is not generically dark-specific | Exp071C / Article-2 claim A2-C3 | ✅ | Negative-control interpretation is canonical. Do not upgrade to a universal theorem beyond tested controls. |
| Static response combinations retain a sound-speed-like K2 ambiguity near 19° | Exp071E/F | ✅ | Exact Table 1 values support the statement. |
| K2+ temporal angles are 138.10/137.10° | Exp071H | ✅ | Must remain explicitly an oriented-ray result. |
| K2+ raw `t_tot` angles are 165.95/164.71° | Exp071I | ✅ | `t_tot` is not tracer RSD or `f sigma_8`. |
| Projected K2+ velocity angles are 166.44/164.93° | Exp071J | ✅ | Approximately 83% raw norm retained. |
| All 24 leave-one-scale/redshift tests remain above 157.82° | Exp071K | ✅ | Applies to the positive-ray robustness test only. |
| K2 line from projected positive response is 13.56/15.07° | Exp071J line geometry | ✅ | Sign-invariant algebraic line interpretation. |
| Fresh K2− validates line geometry at 13.55/15.07° and is 179.91° from K2+ | Exp071L | ✅ | Central prospective falsification. |
| K1 is exactly null in transfer-only `t_tot` and no angle is scientifically defined | Exp071M | ✅ | Must retain `INVALID_FOR_SCIENCE`, not physical FAIL. |
| Restoring `Delta ln P_R + 2 Delta ln|t_tot|` resolves K1 | Exp071N | ✅ | Representation recovery is canonical. |
| K1 line remains at 36.06/37.85° (<45°) | Exp071N | ✅ | Independent known-sector two-sided overlap. |
| K1 projected response retains 62.55% raw norm | Exp071N | ✅ | Exact value 0.625535... |
| Fresh Exp071N parent `P` and `t_tot` reproduce with max relative difference 0.0 against `1e-10` | Exp071N | ✅ | Safe integrity statement. |
| Provider/finite-operator audits show theory geometry does not guarantee observational admissibility | Exp071A + Exp072/073 | ✅ | Must remain an admissibility statement, not observational detectability. |

**Abstract verdict:** `ALL_PRIMARY_SCIENCE_CLAIMS_WITHIN_FROZEN_BOUNDARY_V0_1`.

## 2. Introduction / novelty audit

| Claim | Basis | Verdict | Notes |
|---|---|---|---|
| GDM effective sound-speed/viscosity phenomenology and degeneracies are prior physics | Hu 1998; Kopp et al. 2016; Thomas et al. 2016; Kunz et al. 2016 | ✅ | Exact metadata verified. |
| MOPED establishes parameter-aware Fisher-preserving compression | Heavens et al. 2000 | ✅ | Prior-art positioning only. |
| Nuisance hardening projects nuisance sensitivities from compressed summaries | Alsing & Wandelt 2019 | ✅ | Do not claim DSIR invented nuisance projection. |
| Model-specific SVD subspace compression exists in cosmology | Philcox et al. 2021 | ✅ | Safe. |
| Fisher/information-geometric cosmological degeneracy analysis exists | Giesel et al. 2021 | ✅ | Safe. |
| Baseline-model compression can suppress non-standard-physics information | Heavens et al. 2020 | ✅ | Close conceptual prior art to Exp071M. |
| Recent dark-matter Fisher/nuisance information geometry exists | Adam 2026 | ⚠️ | arXiv record is current as of 2026-08-28; publication/DOI status must be rechecked at submission. |
| DSIR-2 novelty is workflow-level, not projection/information geometry itself | targeted novelty audit v0.2 | ✅ | Safe formulation. |
| No “first” or “to our knowledge” priority claim in Abstract | manuscript v0.5 | ✅ | Keep this rule until final citation-graph audit. |

**Novelty verdict:** `NARROW_WORKFLOW_LEVEL_CLAIM_SUPPORTED__GLOBAL_PRIORITY_NOT_CERTIFIED`.

## 3. Formalism audit

| Formal statement | Evidence / mathematical status | Verdict | Notes |
|---|---|---|---|
| `s_A = A r` declared representation | DSIR response/operator architecture | ✅ | Definition. |
| require `||A n||_M > epsilon_num` before normalized geometry | Exp071M fail-closed gate | ✅ | Important methodological rule. |
| oriented metric angle formula | standard linear algebra | ✅ | No novelty claim. |
| two-sided line angle uses absolute inner product / `min(theta,pi-theta)` | standard projective geometry; Exp071L validates physical use | ✅ | Central interpretation. |
| `P_N=N(N^T M N)^+N^T M` | standard M-orthogonal nuisance projector | ✅ | Do not claim invention. |
| Article 2 does not construct covariance-weighted observational nuisance subspace | declared scope | ✅ | Preserves Article-3 boundary. |

## 4. Results audit

### R1 — provider support

Claim: certified C3/C5 providers retain `495/495` frozen cells.

**Verdict:** ⚠️ **SUPPORTED / PROVENANCE FOLLOW-UP**.

Scientific value is canonical via Exp071A/current claim matrix. Release-candidate Table 2 still needs the exact Exp071A Actions tuple/immutable summary path if available.

### R2 — F30 known-sector falsification

Claim: K2 passes full F30 and leave-one-z gates; K1 does not.

**Verdict:** ⚠️ **SUPPORTED / PROVENANCE FOLLOW-UP**.

Science is canonical. Exp071C run `33020201997` and artifact `9626235928` are known, but the publication provenance pass has intentionally not guessed the missing preregistration/job/terminal-summary digest.

### R3 — static ambiguity

Exp071E:

- `18.9257°` to `cs2`;
- `58.9127°` to `cv2`.

Exp071F matter-only:

- `19.2231°` / `19.0371°`.

Exp071F equalized 3-channel:

- `19.0749°` / `50.1667°`.

**Verdict:** ✅ exact terminal summaries and provenance available.

### R4 — temporal positive-ray result

Exp071H:

- `138.1006°` / `137.0973°`.

Descriptive line angles:

- `41.8994°` / `42.9027°`.

**Verdict:** ✅ provided the manuscript never retroactively reclassifies Exp071H using the descriptive line diagnostic.

### R5 — raw/projected velocity positive ray

Exp071I:

- `165.9455°` / `164.7113°`.

Exp071J:

- `166.4387°` / `164.9271°`.

Exp071K:

- all 24 support-deletion primary tests >45°;
- global minimum `157.8212°`.

**Verdict:** ✅.

### R6 — K2 two-sided falsification

Exp071J line prediction:

- `13.5613°` / `15.0729°`.

Exp071L fresh K2−:

- `13.5503°` / `15.0709°`;
- K2−/K2+ mutual `179.9078°`;
- antisymmetry error `0.00299225`.

**Verdict:** ✅. This is the strongest direct evidence against promoting positive K2 velocity-ray separation to sign-invariant specificity.

### R7 — K1 representation kernel

Exp071M:

- K1+ transfer-only response exactly 0;
- K1− transfer-only response exactly 0;
- classification not scored;
- status `INVALID_FOR_SCIENCE_EXP071M`.

**Verdict:** ✅.

Forbidden interpretation: “primordial tilt has no physical effect.”

### R8 — K1 physical-representation recovery

Exp071N:

- K1+ `36.0622°/37.8458°`;
- K1− `143.9378°/142.1542°`;
- mutual `179.9999991°`;
- line `36.0622°/37.8458°`;
- antisymmetry error `0.0`;
- K1 retained norm `0.625535`;
- fresh-reference max relative differences `0.0`.

**Verdict:** ✅.

### R9 — observational-support boundary

Claims:

- ACT×unWISE retained dimension `0` under 5% leakage;
- joint frontier near `z_min=0.0087345858`, `k_max=4.8182610974 Mpc^-1`;
- BOSS finite operator has non-empty `54/240` component;
- examined KiDS finite-theta route fails frozen criterion.

**Verdict:** ⚠️ **SUPPORTED / PROVENANCE FOLLOW-UP**.

Science wording is canonical. Exact Exp072/073 Actions tuples should be recovered from immutable summaries before final supplementary provenance freeze.

## 5. Conclusions audit

All nine numbered conclusions in manuscript v0.5 are within the current science boundary.

Particularly important wording checks:

- ✅ “selected positive K2 ray” rather than generic K2 separation;
- ✅ “two-sided K2 nuisance line overlaps”;
- ✅ “K1 unresolved in transfer-only `t_tot`” rather than physically inactive;
- ✅ “K1 line overlaps after physical response recovery”;
- ✅ “provider-space geometry is not observational distinguishability”;
- ✅ Article 2 stops before covariance whitening;
- ✅ no G7/G8/G9 promotion.

## 6. Search-forbidden claim classes

The release-candidate manuscript must contain **zero unqualified occurrences** of the following scientific claims:

- ❌ “unique dark-sector fingerprint”;
- ❌ “velocity solves/removes the degeneracy” without ray/line qualification;
- ❌ “K1 has no effect” based on Exp071M;
- ❌ `t_tot` = tracer RSD or `f sigma_8`;
- ❌ survey distinguishability from Exp071 angles;
- ❌ covariance-whitened separation in Article 2;
- ❌ observational nuisance-marginalized separation;
- ❌ dark-sector or modified-gravity detection;
- ❌ G7/G8/G9 closure;
- ❌ “first”/global-priority claims for projection, information geometry, nuisance hardening, SVD subspaces or representation-dependent information loss.

## 7. Release-candidate blockers

### Scientific blockers

✅ None identified within the declared Article-2 scope.

### Publication/reproducibility blockers

⚠️ Recover exact immutable provenance for Exp071A where available.  
⚠️ Complete Exp071C prereg/job/summary-digest audit without conflating the parent K2 artifact with the terminal-summary ZIP digest.  
⚠️ Recover exact Exp072/073 Actions tuples for supplementary provenance.  
⚠️ Execute/visually approve figure-generator v0.2.  
⚠️ Final bibliography/citation-graph audit near submission, especially 2026 publications.  
⚠️ Final target-journal formatting and automated reference compilation check.

## 8. Audit verdict

`MANUSCRIPT_V0_5_PRIMARY_CLAIMS_PASS__RELEASE_PROVENANCE_AND_FIGURE_QA_REMAIN_V0_1`

The manuscript does not currently require an additional scientific response-angle experiment for its declared scope.
