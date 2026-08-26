# DSIR-1 claim-to-evidence map v0.1

**Date:** 2026-08-27  
**Article:** `DSIR-1 observable-response geometry`

This file is the manuscript-facing map from candidate claims to the scientific record. It deliberately includes failed/null controls.

| Claim ID | Draft-safe claim | Main evidence | Evidence class | Mandatory caveat |
|---|---|---|---|---|
| A1-C1 | Heterogeneous dark-sector/MG models can be placed in a common response bookkeeping system without treating missing domains as zero. | G1/G2 contracts; G3A/G3B block-aware atlas; Exp051A mask | method + hard validation | common response representation is not itself new physics |
| A1-C2 | Background/AP null behavior and perturbation activity can coexist and therefore form part of model identity. | Exp037/038 and subsequent atlas | hard model comparison | null in one channel is not absence of new physics in all channels |
| A1-C3 | A simple additive scale+time description is insufficient for several tested mechanisms; irreducible `k×z` interaction structure is measurable. | Exp045A/046; Exp047A/B | hard negative + descriptive | interaction magnitude is representation/domain dependent |
| A1-C4 | Scale and time localization expose different equivalence relations: GDM and designer-f(R) can be scale-localization lookalikes while differing in temporal localization. | Exp048A/B | hard descriptive | this is partial observational/theory-response equivalence, not microscopic identity |
| A1-C5 | One microscopic parameter can trace a curved response trajectory, so global SVD modes need not equal microscopic degrees of freedom. | Exp047A; Exp071B/C synthesis | hard descriptive + control | keep `N_micro`, `N_manifold`, `N_repr`, `N_disc` distinct |
| A1-C6 | Characteristic response scales move predictably within several mechanisms, but a single universal scalar law has repeatedly failed. | Exp049B/C; Exp050B; Exp053A; Exp054C FAIL; Exp056B FAIL | prospective PASS + prospective FAIL | mechanism-specific directional rules are not G7 universal laws |
| A1-C7 | C4 thermal WDM occupies a distinct high-k scale-dominated block and must not be zero-imputed into the low-k atlas. | Exp050A/B; Exp051A | hard solver response + mask | support domains differ physically |
| A1-C8 | A multicoordinate response-path rule survived a genuinely fresh dark interaction family, but the same matter-only normalized-path behavior is not dark-specific. | Exp061A/F30 C9 PASS; Exp071C K2 known-sector PASS | prospective dark-family PASS + prospective known-sector specificity control | F30 is a response-direction/shape diagnostic, not a dark detector |
| A1-C9 | Cross-family parameter translation is intrinsically channel-conditional and can be many-to-one. | `CROSS_MODEL_TRANSLATOR_LIGHTWEIGHT_AUDIT_2026-08-27.md` | retrospective proof-of-concept | no unique global parameter identity; no observational posterior claim |
| A1-C10 | The strongest defensible current interpretation is a taxonomy of response mechanisms and channel-conditional equivalence classes, not a discovered universal dark-sector law. | full failure/pass chronology; novelty-boundary update | synthesis constrained by negative controls | G7/G8/G9 remain open |

## Quantitative figure/table source map

### Figure candidate F1 — response decomposition and interaction

Use frozen derived arrays from Exp045A/046/047A. Show representative `G(k)`, `T(z)` and irreducible `I(k,z)` for mechanisms with materially different nonseparability. Do not renormalize families after looking at plot aesthetics.

### Figure candidate F2 — localization complementarity

Use Exp048A/B `q_k`, `q_z`, `k_I^geo`, temporal-centroid products. A suitable central comparison is:

- GDM vs f(R): nearly degenerate scale localization, separated temporal localization;
- smooth-w vs f(R): complementary pattern;
- GDM `c_s^2` vs `c_vis^2`: localization lookalikes requiring an independent slip channel.

### Figure candidate F3 — curved one-parameter trajectories

Use finite-amplitude GDM/f(R) trajectory products plus the later known-sector K2 control. The caption must state that low-dimensionality and causal monotonicity are different properties.

### Figure candidate F4 — characteristic-scale/window-crossing sequence

Use Exp049B/C and Exp050B/Exp053A as examples of preregistered directional predictions. Pair with a panel/table containing Exp054C and Exp056B failures to prevent success-only selection.

### Figure candidate F5 — F30 specificity boundary

Show the fresh C9 F30 PASS next to the K2 known-sector PASS under the same normalized response-path operator. The scientific point is that matter-only geometry captures transfer/shape behavior but is not uniquely dark-sector specific.

### Table candidate T1 — family/block atlas

Build from block-aware observability atlas files. Every cell must retain status: available / near-null / unsupported / high-k-only / solver-limited. Never replace missing cells by zero.

### Table candidate T2 — prospective prediction ledger

Include at least:

- Exp049B PASS;
- Exp049C PASS;
- Exp050B PASS;
- Exp053A withheld-family PASS;
- Exp054C FAIL;
- Exp056B FAIL;
- Exp061A/F30 PASS;
- Exp071C K1/K2 specificity outcomes.

### Table candidate T3 — claim boundary / prior art

Summarize which ingredients are established prior art: effective source tensors, PPF/EFT dictionaries, PCA/SVD, model manifolds/information geometry, response ratios, model-independent dark-sector reconstruction. Reserve novelty language for the DSIR pipeline conjunction and only provisionally pending N1.

## Excluded evidence from DSIR-1 central claims

The following may appear only as future-work/technical-note material unless separately justified:

- direct C5 joint `P_mm/P_Wm/P_WW` provider claims before provider certification;
- ACT×unWISE dark-sector fit or observational law claim before G7;
- any G8 discovery language;
- retrospective fitted exponents promoted as universal laws;
- RTK numerical results as DSIR evidence.

## Manuscript conclusion boundary

The strongest current article-level conclusion is:

> heterogeneous dark-sector and modified-gravity models exhibit reproducible but channel-dependent response geometry; low-dimensional or partially equivalent matter-response trajectories do not uniquely identify dark physics, so robust discrimination requires explicit channel bookkeeping and, ultimately, independent matter/Weyl/observational information.

This statement is supportable without closing G7/G8/G9 and is the intended center of DSIR-1.
