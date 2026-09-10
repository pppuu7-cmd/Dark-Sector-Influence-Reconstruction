# Exp073JV — Article III sequential canonical JL execution authorization audit v0.1

Date frozen: 2026-09-11. Scope: DSIR Article III process/execution authorization only. Effect `+0/+0`.

Status: PROSPECTIVELY FROZEN while corrected Exp073JU run `34538302756` is still executing and before any Exp073JU numerical result has been consumed. This audit therefore cannot tune its acceptance rule to JU outcome.

## Question

May DSIR preregister a recovered Exp073JL execution that changes only solver-object lifetime from the resource-infeasible four-live layout to an exact canonical one-live layout, while preserving every scientific operand, estimator, observational traversal, support rule and convergence threshold of frozen Exp073JL?

Exp073JV is not the recovered JL experiment. It is a fail-closed audit of whether enough independent evidence exists to authorize preregistration of that execution architecture.

## Frozen evidence bundle

The audit may use only the following already frozen or prospectively frozen evidence classes:

1. **JR coarse direct equivalence.** `EXP073JR_COARSE_2049_SEQUENTIAL_EXACT_EQUIVALENCE_RECEIPT_V0_1`: independently verified direct four-live-vs-sequential exact equality on the 2049-node coarse lattice for both fixed requests, with zero unsupported evaluations and canonical coarse node SHA `6305c95025e52296b6cb623903f82dc45bb66ac692708b242fc354862ac54c46`.
2. **JQ fine same-run history/repeat independence.** `EXP073JQ_ARTICLE3_SLOT20_SAME_RUN_HISTORY_INDEPENDENCE_V0_1`: independently verified exact fresh/history/fresh equality for all four finite-difference roles on the canonical 4097-node fine SHA `f30556be2547732ed0b87b56368e01e46504a975f94fcbbc5e7bc8cfc525e5eb`.
3. **Pinned CLASS-IV C2 source audit.** `CLASSIV_C2_INSTANCE_LOCALITY_SOURCE_AUDIT_V0_1`: major solver state is per `Class` instance; the identified file-scope Romberg workspace is inactive on frozen C2 because the path retains `fluid_equation_of_state=CLP`; source evidence alone is not sufficient.
4. **JS canonical lifecycle coverage audit.** `EXP073JS_ARTICLE3_LIFECYCLE_GEOMETRY_COVERAGE_AUDIT_V0_1`: exact local lifecycle isolation exists for all four roles, but only `reference`, `alpha_minus`, and `beta_plus` were executed on the canonical fine grid; canonical coverage is conservatively 3/4.
5. **JT canonical geometry authority.** `EXP073JT_ARTICLE3_CANONICAL_SHARED_LATTICES_V0_1`: independently verified immutable coarse/fine canonical byte streams materialized from pre-existing JR/JQ authority SHAs and committed to main. Host-generated variants are evidence only and can never replace the canonical streams.
6. **JU targeted canonical beta-minus lifecycle result.** Activation requires a future independently verified authority derived from prospectively frozen Exp073JU v0.1. It must classify `CANONICAL_FINE_BETA_MINUS_LIFECYCLE_ISOLATION_PASS_PLUS_0_PLUS_0`, bind the committed canonical fine SHA, show exact A/B before/after equality, zero unsupported evaluations and lookup mismatch <=1e-12. Any valid JU bitwise FAIL forbids JV authorization. Missing/infra-invalid JU leaves JV `NOT_YET_AUTHORIZED`.
7. **Estimator-lifetime invariance.** `LAYERB_SEQUENTIAL_MODEL_LIFETIME_ESTIMATOR_INVARIANCE_V0_1`: with identical four raw target vectors supplied in the frozen model order, changing object lifetime does not alter the finite-difference estimator definition.
8. **Same-run atomic topology and associative reduction.** `LAYERB_SAME_RUN_ATOMIC_RECOVERY_TOPOLOGY_V0_1` and `LAYERB_CHUNK_REDUCTION_ASSOCIATIVITY_AUDIT_V0_1`: future raw coarse/fine scientific comparison operands must be generated/combined within the same runner process; only decision-neutral associative summaries may cross chunk boundaries.

No later numerical result may add a new evidence category to this v0.1 authorization rule.

## Authorization PASS

`SEQUENTIAL_CANONICAL_JL_EXECUTION_AUTHORIZED_PLUS_0_PLUS_0` requires all of the following:

- JR receipt independently verified and exact PASS, canonical coarse SHA exactly as above;
- JQ authority independently verified and exact same-run PASS, canonical fine SHA exactly as above, all four roles valid;
- source audit present and unchanged, with its narrow conclusion only (no claim of global reentrancy beyond the audited C2 path);
- JS coverage audit independently verified, canonical roles exactly `reference`, `alpha_minus`, `beta_plus`, only missing role exactly `beta_minus`, and all three canonical-covered local lifecycle controls exact;
- JT authority independently verified PASS; exact committed canonical files and decoded SHAs reproduce the authority; coarse requested count 2049 and fine 4097; guard counts `[0,1]` for both;
- JU independently verified valid PASS on the committed canonical fine grid, closing canonical lifecycle coverage to exactly 4/4;
- estimator-lifetime invariance note unchanged;
- same-run atomic topology and chunk-reduction associativity notes unchanged;
- no evidence in this bundle contains a valid exact inequality between compared lifecycle/equivalence operands on the canonical geometry;
- future recovered-JL preregistration is explicitly constrained by the execution ceiling below.

If JU is missing or infrastructure-invalid, classification is `SEQUENTIAL_CANONICAL_JL_EXECUTION_NOT_YET_AUTHORIZED_PLUS_0_PLUS_0`. If JU or any other required canonical exact control gives a valid inequality, classification is `SEQUENTIAL_CANONICAL_JL_EXECUTION_FORBIDDEN_PLUS_0_PLUS_0`. Provenance/schema/hash inconsistency is `INVALID_INFRA_PLUS_0_PLUS_0`.

## Execution ceiling authorized by PASS

JV PASS permits only **preregistration** of a recovered Exp073JL execution satisfying every item below:

- frozen Exp073JL science is unchanged: 2049-vs-4097, native kpd20, `h=1e-4`, centered-cubic interpolation, identical IR traversal/support/accounting, `REL_TOL=1e-3`, identical invalid-row/retained-dimension/status rules and anti-rescue rules;
- coarse and fine grids are decoded from the exact committed JT canonical `u64hex` payloads; neither `np.geomspace` nor another floating grid generator may reconstruct them at execution time;
- at most one CLASS instance is live at a time;
- the four model roles and their parameters remain exactly `(0,0),(-1e-4,0),(0,+1e-4),(0,-1e-4)`;
- for every scientific coarse/fine comparison atom, all raw target vectors required to form that atom are produced and combined within one runner/process execution domain; raw scientific operands may not cross runner/process boundaries;
- raw model/response operands may exist on local disk only transiently inside the same running job/process domain that will consume them. They may not be uploaded, checkpointed, restored, or consumed by a different runner/process to form a scientific coarse/fine comparison;
- a completed fixed chunk may persist across process boundaries only the already audited decision-neutral associative summaries, counters, row/status receipts and provenance needed for exact final reduction. No raw operand or partially formed cross-lattice comparison may be reconstructed from different processes;
- no tolerance, ULP allowance, rounding, smoothing, averaging, effective coordinate, changed finite-difference step, changed grid density, changed interpolation, changed native kpd, or fiducial-P rescue is allowed;
- the ordinary recovered output must be judged by the original JL scientific classifier, not a new JV-specific convergence criterion.

JV PASS does **not** authorize execution until a separate recovered-JL preregistration/implementation is itself frozen and audited prospectively.

## Interpretation ceiling

Exp073JV is process-only `+0/+0`. It cannot declare Layer-B converged/nonconverged, cannot authorize covariance restriction, cannot open Wm_S3, and cannot increase `ARTICLE3_REPOSITORY_READINESS` by itself. Repository readiness for preparing Article III remains 68%; funnel-freeze readiness remains 67% until a scored scientific/repository milestone closes.