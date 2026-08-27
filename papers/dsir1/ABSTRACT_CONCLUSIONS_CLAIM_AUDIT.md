# DSIR-I Abstract / Conclusions claim audit — v0.1

**Purpose:** ensure the two most visible manuscript sections never exceed frozen evidence. The JCAP-ready abstract in `JCAP_SUBMISSION_FRONT_MATTER.md` and the five high-level conclusions of manuscript v0.2 must remain inside this map.

## Abstract audit

| Abstract statement | Evidence class | Provenance / formal source | Allowed wording | Forbidden strengthening |
|---|---|---|---|---|
| DSIR compares heterogeneous dark-sector and modified-gravity mechanisms through observable response geometry rather than model labels alone. | framework definition | `docs/DSIR_METHOD.md`; quotient formalism | model-agnostic comparison framework | “complete theory of the dark sector”; “unique physical decomposition” |
| Atlas spans smooth DE, IDE, GDM, WDM, DCDM and designer modified gravity. | implemented atlas scope | C1--C6 repository families; `TABLES_DRAFT.md` | “spanning the tested families” | “exhaustive dark-sector theory space” |
| Additive scale-plus-time representation is insufficient on the frozen low-k atlas. | scientific FAIL | P1 / Exp045A | “insufficient on the tested/frozen atlas” | “mathematically impossible for dark-sector responses” |
| Irreducible scale-time morphology produces the descriptive ordering IDE < smooth DE < GDM < designer-f(R), preserved in all 12 single-node deletions. | descriptive + deterministic robustness | P3 / Exp047A; P5 / Exp047B | “robust descriptive hierarchy on sampled domains” | “universal hierarchy”; “new invariant” |
| Degeneracy is channel conditional: matter lookalikes can separate in metric slip; scale-mode lookalikes can separate in time/full response. | frozen theory-response comparisons | P6--P8 / Exp031--032 | “theory-response channel dependence” | “survey detection”; “observational exclusion significance” |
| Finite-amplitude response curves show microscopic parameter count, manifold dimension and linear representation rank need not coincide. | sampled trajectory geometry | P4 / Exp047A | “need not coincide for the tested rays” | fixed global model rank; new microscopic degrees of freedom |
| A formal observational quotient is used only after finite positive normalization, exact realized-operator reproducibility and physical support are certified before whitening/nuisance projection. | formal method + negative eligibility chain | quotient formalism; P16--P29 | prerequisite/admissibility rule | claim that the final quotient is already complete |
| Prospective audits expose failures at several layers and preserve them rather than repairing them retrospectively. | provenance methodology | P12--P14, P16, P19, P24, P26 plus permanent FAIL records | failure-resistant scientific provenance | implication that every infrastructure failure is a scientific FAIL |
| DSIR-I is response classification/identifiability, not a universal law or discovery of new fundamental physics. | hard claim boundary | `CLAIMS_LEDGER.md` | mandatory boundary | any new-fundamental-physics/discovery/no-hair wording |

## Conclusions audit

The assembled v0.2 manuscript uses five high-level conclusions. Each must stay within these evidence classes.

### Conclusion 1 — response morphology is not captured by a universal additive scale+time core

**Evidence:** P1--P5.  
**Allowed:** additive core fails for the tested low-k atlas; finite-amplitude `chi_I` hierarchy is robust descriptively under frozen tests.  
**Do not claim:** `(G,T,tau,I)` are fundamental hairs or that the hierarchy is universal.

### Conclusion 2 — equivalence is channel conditional

**Evidence:** P6--P8 plus the formal quotient theorem.  
**Allowed:** the same pair can be near-degenerate in matter/scale response and separated in slip/time/full response.  
**Do not claim:** current angles are survey significance or that adding every real survey channel monotonically improves separation after joint nuisance refitting.

### Conclusion 3 — response dimension is not microscopic parameter count

**Evidence:** P4 and sampled turns from Exp047A.  
**Allowed:** curved one-parameter response paths can occupy multiple linear modes.  
**Do not claim:** a fixed intrinsic rank such as `R_model=5` or additional microscopic degrees of freedom.

### Conclusion 4 — mechanism diversity requires mechanism-aware localization

**Evidence:** P9--P12.  
**Allowed:** WDM is scale-localized and nearly time-separable on its frozen high-k linear block; withheld DCDM passes a temporal-localization prediction; a proposed common centroid-slope law fails on withheld IDM-DR.  
**Do not claim:** one universal localization scalar, G8 closure, or a universal residual law.

### Conclusion 5 — a formal observational quotient can be physically inadmissible

**Evidence:** P16--P29 and the formal support/whitening order.  
**Allowed:** current ACTxunWISE support route fails on the certified domain; the tested enlarged linear route is ineligible; a tested positive absolute-response measure is nonnormalizable; an operator-class candidate can fail exact real-data provenance; replacement-route checksum/mask/pixelization prerequisites can pass while physical support remains unread.  
**Do not claim:** a completed DES/BOSS support PASS, covariance-whitened distance, nuisance-quotiented distance, G7 relation, G8 validation or G9 dynamics reconstruction.

## Numerical statements permitted in Abstract/Conclusions

Use numbers only when they materially sharpen the central claim and map directly to a provenance row. Preferred high-value candidates are:

- `12/12` deterministic leave-one-node hierarchy preservation — P5;
- `0/26` retained ACTxunWISE coordinates on the current certified support — P16;
- `7/64` pairwise perturbativity eligibility on the planning frontier — P19.

Avoid filling the abstract with provider run IDs, artifact IDs, detailed WDM masses, mask pixel counts or exact operator-provenance chronology. Those belong in Results/Supplement.

## Hard final gate

Before submission, a line-by-line diff of the actual LaTeX abstract and conclusions must be checked against this file. If a sentence cannot be mapped to one of the evidence classes above, either add immutable provenance first or weaken/remove the sentence.
