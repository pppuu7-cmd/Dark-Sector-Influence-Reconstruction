# DSIR research log — heavy-chain repair and existing-model FAIL frontier

Date: 2026-09-07
Scope: DSIR only
Status: **INFRASTRUCTURE REPAIRED; SCIENTIFIC FAIL FRONTIER AUDITED; C2 SOURCE MAPPING ADVANCED; NO MODEL FAIL DECLARED**

## 1. Heavy-chain incident

Observed terminal heavy job:

- run: `34050657030`
- job: `101533574294`
- job name: `home-science`
- terminal result: `success`
- science artifact: `exp073fm-ww-s1-s1-filebacked-ab-v0-1`
- artifact ID: `9998932628`
- artifact size: `7380196`
- artifact digest: `sha256:db3aa00e060047f354c5374c78dba3808491cf61a1d810114d35b474badd49af`

The five-hour science calculation itself was not the failure.

The downstream consumer run `34065976761` successfully consumed and validated the terminal evidence, but then failed while attempting to create

`.github/workflows/exp073fr-ww-s1-s1-canonical-admission-v0-1.yml`

with GitHub API response

`HTTP 403: Resource not accessible by integration`.

Therefore the canonical admission/successor dispatch chain stopped after valid science. This was an orchestration-token permission failure, not a scientific/model failure and not a self-hosted-runner failure.

## 2. Repair performed

The missing canonical Exp073FR workflow was restored through the authorized repository connection using the already-frozen terminal provenance. The expensive science was **not rerun**.

Only the failed consumer job was rerun. It completed successfully and dispatched the already-frozen successor

`exp073fs-ww-s1-s2-home-science-v0-1.yml`.

Successor run:

- run ID: `34067352681`
- hosted launch audit: terminal `success`
- `home-science`: `in_progress` at the latest status check in this log
- active step: frozen `WW_S1_S2 A/B gate with durable checkpoints`

No competing/duplicate home-science job was started. No partial numerical checkpoint from the active scientific step was inspected.

## 3. Gate-1 bookkeeping correction discovered during the audit

An earlier same-day note had incorrectly promoted legacy theory-response evidence for IDE, GDM, and designer-f(R) to DSIR-4 `G_DOMAIN_MAPPING=PASS`.

The frozen DSIR-4 pilot and model-mapping contract require dedicated six-component residual mapping/prediction artifacts. At the time of that correction `docs/dsir4/mappings/` contained only the C0/C1 analytic mapping artifact.

Therefore the Gate-1 note was corrected in commit

`1e6c14903a7334d913283caecee9955e11e942be`.

Correct current Gate-1 states:

- C0 LambdaCDM: `PASS` (already mapped/admitted);
- C1 smooth-w control: `PASS` (already mapped/admitted);
- C2 IDE: `NOT_YET_TESTABLE` pending dedicated DSIR-4 admission authority;
- C3 GDM: `NOT_YET_TESTABLE`;
- C5 designer-f(R): `NOT_YET_TESTABLE`.

The old Exp030/031 hard results remain valid legacy theory evidence. Missing DSIR-4 mapping authority is not evidence against any model.

## 4. Scientific FAIL taxonomy

Frozen DSIR-4 mandatory order:

1. `G_DOMAIN_MAPPING`
2. `G_ANGULAR_AUTHORITY`
3. `G_ORDERED_JOIN`
4. `G_RADIAL_SUPPORT`
5. `G_PHYSICAL_SUPPORT`
6. `G_COV_WHITENING`
7. `G_NUISANCE_QUOTIENT`
8. `G_RELATION_NULL`
9. `G_FINAL_MODEL`

### Pre-discrimination / authority stages

`G_DOMAIN_MAPPING`, `G_ANGULAR_AUTHORITY`, and the ordered representation/join stages are primarily authority/domain/representation gates. Missing provenance or missing artifacts are `NOT_YET_TESTABLE`; a model that cannot validly predict the mandatory domain is `OUTSIDE_DOMAIN`; numerical ambiguity is `NUMERICALLY_UNRESOLVED` only under a frozen ambiguity rule. None of these may be converted into an observational model rejection by convenience.

### First explicit scientific-support FAIL

The prospective Article-3 physical-support contract is the first audited contract in the chain with an explicit scientific-failure class under otherwise valid provenance.

For geometrically eligible coordinates it freezes

`f_invalid <= 0.05`

and at least

`15 retained coordinates`.

With valid parent/provenance/schema, violation of those criteria is

`FAIL_PHYSICAL_SUPPORT_ARTICLE3`,

not an infrastructure error. Thresholds may not be changed after seeing the result.

This is a genuine mandatory scientific-support failure, although it is still a support/admissibility failure rather than a goodness-of-fit rejection against the final observational residual.

### Covariance/whitening is not a model-rejection gate

The covariance contract explicitly classifies coordinate mismatch, wrong dimension, nonfinite entries, material nonsymmetry, non-positive-definiteness, Cholesky/factorization failure, and catastrophic whitening residual as `INVALID_FOR_SCIENCE_*` states.

They block downstream science but are not evidence for or against dark-sector physics.

### Nuisance quotient is also fail-closed infrastructure/geometry before G7

The signed nuisance-subspace contract requires a prospectively frozen full nuisance span, two-sided signed directions when physically available, common whitening, target-independent SVD rank selection, and basis/sign invariance.

A failed local nuisance-linearity diagnostic invokes a preregistered nonlinear handling rule or `INVALID_FOR_NUISANCE_LINEARIZATION`; it may not be repaired by keeping whichever nuisance sign makes the target residual look favorable.

The causal-nuisance amendment further requires nuisance directions to be classified independently as exogenous, mediated, or causally unknown. Geometric overlap with a nuisance span is not automatically proof that the removed response is non-dark physics.

### First direct post-cleaning model-physics rejection frontier

After valid support, valid covariance/whitening, and valid nuisance quotient, the first gate that can compare a cleaned residual/cross-channel structure against a frozen scientific relation/null prediction is `G_RELATION_NULL` (legacy G7 role).

A frozen hypothesis that makes an authoritative prediction and fails the prospectively frozen relation/null criterion can receive a genuine model scientific `FAIL` under the DSIR-4 aggregation rule.

`G_FINAL_MODEL` is the terminal prospective model-comparison gate. A mandatory FAIL there yields overall FAIL for that frozen `hypothesis_id`.

Legacy G8 discipline remains scientifically important: a relation discovered/calibrated on represented mechanisms must survive a genuinely fresh withheld prediction before any discovery/new-law claim is allowed.

## 5. Existing-model vulnerability map

### C2 IDE

- `alpha>0` points that violate full-history `rho_iv>=0` are not observational model failures; they are outside the physically valid branch/domain.
- The valid negative-alpha ray and beta tangent have distinct structure responses, while background geometry can be substantially more degenerate.
- Therefore the strongest real rejection opportunity is downstream structure/time/cross-channel relation testing after nuisance cleaning, not a background-only comparison.
- A failed frozen IDE parameter point does not automatically reject the entire IDE class; family-level rejection requires a prospectively defined equivalence class or complete parameter-domain statement.

### C3 GDM

- low-k `cs2/cv2` near-collinearity (`~0.3226 deg`) is an identifiability weakness, not a model FAIL;
- the existing theory atlas contains a strong metric-slip separator, so an additional channel can break that degeneracy;
- the genuine model-risk frontier is whether the joint growth/slip/time pattern survives the authoritative observation operator, covariance metric and nuisance quotient;
- unresolved separation after those steps may be an identifiability/numerical state rather than a rejection unless the frozen relation/null criterion says otherwise.

### C5 designer-f(R)

- stability/branch failures and points inside the pinned solver Return-to-GR threshold are domain/independence issues, not observational rejections;
- the chosen designer branch has LambdaCDM background expansion (`EFTwDE=0`), so background/radial geometry alone is intentionally weak for rejection;
- its strongest prospective vulnerability is the correlated scale/time/growth/slip enhancement pattern after observational kernels and whitening;
- a frozen B0 point can genuinely fail at the relation/null/final comparison stage if that predicted pattern is incompatible with the cleaned data-space residual.

### C4 WDM

- low-k blindness is not model acceptance or failure; the response becomes informative only in its valid high-k block;
- lack of a valid high-k observational operator is `NOT_YET_TESTABLE`, never PASS;
- a true rejection requires a frozen high-k/temporal prediction confronted with an authoritative relation/final gate.

### C0/C1

Even the LambdaCDM reference and smooth-w control receive no automatic scientific immunity. Once the complete funnel exists, a frozen reference/control hypothesis can fail the same prospectively defined relation/null/final comparison if the authoritative residual requires structure it cannot produce.

## 6. C2 IDE source-level mapping advance — 2026-09-07

The pinned implementation `kaeonikc/class_iv@ac627d54e9ce196a08878d1ba33999819925d19c` was re-audited directly at source level while the heavy WW_S1_S2 job remained active.

Exact findings:

- `source/background.c` adds `rho_idm_iv` to total density with zero pressure, and adds `rho_iv` to total density with pressure `-rho_iv`; hence `rho_X=rho_idm+rho_iv`, `p_X=-rho_iv` for the frozen C2 implementation.
- `source/perturbations.c` explicitly refuses Newtonian-gauge IDM-IV perturbation evolution; the source-native mapping is synchronous-gauge only.
- In synchronous gauge, only `delta_idm_iv` is evolved, with the interaction term proportional to `a H (alpha rho_idm + beta rho_iv)`.
- The Einstein stress-energy assembly adds `rho_idm * delta_idm` to `delta_rho` for the dark pair, but adds no separate IV density perturbation, no IDM-IV pressure perturbation and no IDM-IV shear.
- The source comments state the IDM-IV velocity is set to zero by the synchronous gauge definition; the IV background satisfies `rho_iv+p_iv=0`.

Therefore all six required source-native components are now source-audited in the pinned synchronous frame:

- `rho_X = rho_idm + rho_iv`;
- `p_X = -rho_iv`;
- `delta rho_X = rho_idm * delta_idm_iv`;
- `q_X = 0` in the pinned source-native synchronous frame;
- `delta p_X = 0` in the pinned implementation;
- `pi_X = 0` in the pinned implementation.

These zeros are implementation- and frame-qualified and must not be generalized to arbitrary IDE models or copied to another gauge.

The dedicated audit document was updated in commit

`c42809c140caa4eb10aa073d4c03e09e99ac0d46`

(`Complete pinned C2 IDE source-level component audit`).

Scientific consequence: **no model PASS/FAIL changed**. C2 remains `G_DOMAIN_MAPPING = NOT_YET_TESTABLE` until the source-native mapping is bound to the frozen common observable/gauge bridge, exact domain/provenance, deterministic prediction payload/hash, and formal Gate-1 admission procedure.

## 7. Current conclusion

No existing model receives a scientific `FAIL` in this iteration.

The strongest corrected statement is:

1. the prior heavy computation was healthy; its orchestration permission failure was repaired without rerunning expensive science;
2. the next heavy WW_S1_S2 task remains active and must not be duplicated;
3. C2 now has a complete six-component **source-native** audit, but still lacks final Gate-1 observable/provenance admission authority;
4. C3 GDM and C5 designer-f(R) still require formal DSIR-4 Gate-1 mapping artifacts;
5. `G_PHYSICAL_SUPPORT` is the earliest audited mandatory gate with an explicit scientific-support FAIL class;
6. the decisive 'model physics disagrees with cleaned observations' frontier is `G_RELATION_NULL`, followed by `G_FINAL_MODEL` and fresh withheld falsification discipline.

## 8. Next prospective work

While the active WW_S1_S2 heavy job runs independently, safe static work remains:

1. finish the C2 common observable/gauge/provenance binding and formal Gate-1 admission audit;
2. then continue the frozen no-cherry-picking mapping order `C3 GDM -> C5 designer-f(R)`;
3. only after Gate-1 authority may the corresponding hypotheses enter `G_ANGULAR_AUTHORITY` and subsequent gates.

No partial heavy-job checkpoint may be interpreted, no duplicate heavy run may be launched, and no threshold/model definition may be altered to rescue a result.
