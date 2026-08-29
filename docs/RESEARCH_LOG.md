# DSIR research log

Scientific claims are controlled by `docs/GATES.md`.

## 2026-08-24 — repository separation and baseline gates
Dedicated DSIR repository initialized; RTK excluded. Experiments 001–006 cover synthetic rank, R_obs/R_model separation, identity quotient, DESI DR2 AP, relative expansion, and background equivalence.

## 2026-08-24 — G3B and real multi-channel response
Linear controls added. Incorrect per-model D(1)=1 power normalization was rejected. Corrected DESI DR1 ShapeFit erratum data were used for G6B after detecting the superseded Appendix-A growth values. Stable AP-growth covariance is classified as measurement identifiability, not physics. Conditional innovations show no significant aggregate residual; G7 remains open.

## 2026-08-24 — Experiment 011
Across 30 rank-3 synthetic cases with n_models=90/180/360 and strongly anisotropic/correlated feature transforms, covariance whitening recovered rank 3 in 30/30 and preserved the singular spectrum to 1.564e-15. Invalid unwhitened calibration produced ranks 20–35.

## 2026-08-24 — Experiment 012
Three independent response modes were represented by model-family counts 900/90/10. The catalog-multiplicity prior detected only 2 modes; an equal-family prior, with the exact same weights included in null calibration, recovered all 3. The third-to-first singular-value ratio rose from 0.259 to 0.853. DSIR therefore treats `R_model` as a prior-sensitivity profile `R_model(pi)`. Equal-family weighting is not assumed uniquely correct; stability across defensible priors/stratified bootstraps is the gate.

## 2026-08-24 — Recovery manual
Added `docs/RECOVERY_MANUAL.md` as the chat-independent restoration entry point. It records the DSIR architecture, formulas and derivations, response/rank methodology, failure modes, data provenance, solver pins, numbered experiments, exact next steps, and the hard boundary excluding RTK from DSIR development.

## 2026-08-24 — Experiment 013: interacting-vacuum source regression
Pinned `kaeonikc/class_iv@ac627d54e9ce196a08878d1ba33999819925d19c` was audited at source level. The implementation convention is `Q/H = alpha*rho_m + beta*rho_v`, implying `d rho_m/d ln a = -(3+alpha)rho_m - beta rho_v` and `d rho_v/d ln a = alpha rho_m + beta rho_v`. The analytic source solution agrees with direct ODE integration to about `5.9e-12` normalized maximum error over the tested controls; the alpha=beta=0 limit returns `rho_m~a^-3` and constant vacuum at machine precision. Eigen-exponents match the interaction matrix to machine precision. This freezes the source convention but does not replace a full Boltzmann regression.

## 2026-08-24 — Experiment 014: GDM zero-limit source regression
Pinned `s-ilic/gdm_class_public@4c87916aab5ca124a68f1dd16f31846fc13d1829` was audited. For `w=cs2=cv2=0`, the background reduces to `rho_gdm~a^-3`; `Pi_nad=0`; the GDM continuity/Euler equations reduce to pressureless CDM when shear is zero; dynamic shear with `cv2=0` preserves zero shear; and leading adiabatic GDM IC match CDM. A crucial numerical caveat was found: when GDM is enabled the upstream code deliberately drops finite-start matter-radiation corrections of order `omega*tau` in several IC expressions and requires an early start (`start_small_k_at_tau_c_over_tau_h <= 1e-6`).

## 2026-08-24 — GDM start sweep: negative result
A clean-room sweep of `start_small_k_at_tau_c_over_tau_h={1e-6,3e-7,1e-7,3e-8}` falsified the simple hypothesis that pushing this single parameter earlier monotonically improves the zero-GDM/CDM match. Values below `1e-6` worsened the full solver. The parameter participates in the coupled perturbation/tight-coupling start logic and is not an independent accuracy knob. `1e-6` is retained as the working start; this negative result prevents tolerance tuning by start-time manipulation.

## 2026-08-24 — GDM high-precision clean-room calibration
At fixed start `1e-6`, a high-precision calculation using the pinned solver's precision conventions substantially reduced the working-scale zero-limit residual. Scale-aware interpolation gives approximately `max |Delta P/P|=8.28e-4` for `k>=1e-3 h/Mpc`, `5.55e-4` for `k>=1e-2`, `1.44e-4` for `k>=0.03`, and `2.82e-5` for `k>=0.1` in the tested z output. Background quantities agree at numerical/interpolation level. The very large fractional residual at `k~1e-5` is retained as a separate ultra-large-scale IC-sensitive diagnostic and is not used to inflate or hide the linear-core metric. A multi-level precision sweep was launched to establish a plateau before any tolerance is frozen. Initial p2/p3/p4 jobs received GitHub runner shutdown signals (`exit 143`); this is classified as infrastructure failure, not scientific failure, and jobs are being rerun unchanged.

## 2026-08-24 — Experiment 016 / interacting-vacuum perturbation audit
The pinned `class_iv` explicit IDM_IV implementation supports the relevant perturbation path only in synchronous gauge. There, at `alpha=beta=0`, the interacting pressureless density equation reduces to the CDM equation and the upstream adiabatic IC use the same `delta=3/4 delta_gamma`. Upstream's own `test_idm_iv_lcdm.ini` confirms the intended separate-component zero-coupling configuration (`alpha=beta=0`, `f_idm_iv=f_iv=1`) with `fluid_equation_of_state=IDM_IV` commented out.

## 2026-08-24 — class_iv pinned-source build caveat
The exact pinned `class_iv@ac627d54...` source does not compile unmodified on the clean runner: in `background_w_fld()` a premature closing brace after `case EDE` leaves the following `case IDM_IV` outside the switch. This is a source syntax defect, not a cosmological result. PR #2 applies an assertion-checked compile-only repair that removes exactly that one brace, records the resulting `git diff` and repair-script SHA256, and changes no equation/coefficient. IDE-S1 remains OPEN until the repaired pinned source builds and the matched zero-coupling spectra/background comparison passes a justified numerical gate.

## 2026-08-24 — Experiment 017 / G2 response basis v0.1 frozen
Frozen `config/response_basis_v0_1.json`, `docs/RESPONSE_BASIS_V0_1.md`, and `src/dsir/response_basis.py`. The first six-family core uses anchored relative expansion `r_E=ln[(H/H*)/(H_ref/H_ref*)]` with `z*=0.51` and fixed-primordial matter-power `r_P=ln(P/P_ref)` on the linear k grid `{0.001,0.003,0.01,0.03,0.1} h/Mpc`. Derived identities are not double-counted; covariance whitening, component matching, and theory-prior propagation remain mandatory. Experiment 017 verifies common-H calibration cancellation, the AP log identity, preservation of fixed-As power amplitude, and covariance-metric orthogonality of the amplitude quotient. G2 was initially marked PASS.

## 2026-08-24 — GDM precision tail and hard solver gate
The lighter background+linear-`P(k)` workflow completed p1 through p8 without changing the physical zero-closure setup or the fixed start `1e-6`. On the full frozen linear core `1e-3<=k<=1e-1 h/Mpc`, the maximum zero-GDM/CDM residual fell from about `5.93e-4` at p1 to `4.70e-6`, `2.96e-6`, and `1.47e-6` at p6, p7, p8. The location of the maximum moved across k as precision increased, consistent with a numerical-floor interpretation rather than a stable physical transfer-function residual. A conservative hard tolerance `5e-6` was frozen from the observed high-precision envelope before the final hard rerun. The p8 hard regression passed with `global_linear_core_max_abs_relative=1.471014806e-6`. **GDM-S1 PASS.** Ultra-large `k<1e-3` remains a separate IC-sensitive diagnostic.

## 2026-08-24 — interacting-vacuum hard solver gate
The assertion-checked one-brace source repair succeeded, after which two additional legacy build assumptions were isolated: the old fork expects pre-GCC-10 tentative-definition behavior (`-fcommon`) and link semantics equivalent to disabling modern `--as-needed` for GSL. These are toolchain compatibility adaptations; no cosmological equation is modified. Two clean-room calibration runs showed linear-core `P(k)` residuals below `~1e-8` and semantic background matching at `~8.1e-13` or better. Before the final run, hard tolerances were frozen at `2e-8` for `1e-3<=k<=1e-1 h/Mpc` and `2e-12` for semantic background quantities. Both hard gates passed on the redshift set `{0,0.295,0.51,0.706,0.934,1,1.317,1.491,2.33}`. **IDE-S1 PASS.**

## 2026-08-24 — G1 gauge audit: raw mPk rejected as common coordinate
A direct audit used the same pinned GDM_CLASS code, identical LambdaCDM parameters and identical output settings, changing only `gauge=newtonian` versus `gauge=synchronous`. Raw solver `mPk` differed by as much as `9.843415778e-5` on the frozen linear core `1e-3<=k<=1e-1 h/Mpc`; individual frozen nodes at `k=0.01-0.1` show differences of order `4e-5` to `8e-5`. This gauge effect is roughly twenty times larger than the frozen GDM zero-limit tolerance and orders of magnitude above the IDE zero-limit floor. Therefore raw cross-gauge `mPk` is rejected as a common six-family response coordinate. G1 becomes PARTIAL and G2 is **reopened**: the background/identity part of Experiment 017 remains valid, but the perturbation block must be upgraded to v0.1.1 with a gauge-invariant/comoving matter response or another explicitly observable perturbation channel. No G7 law search is allowed on the flawed raw-mPk matrix.

## 2026-08-24 — G1 conservation/gauge contract
Added `docs/CONSERVATION_GAUGE_V0_1.md`. Internal interacting-sector bookkeeping is frozen as `nabla_mu T_i^{mu nu}=Q_i^nu`, `sum_i Q_i^nu=0`, hence `nabla_mu T_tot^{mu nu}=0`; exact Bianchi/conservation identities are projected before rank discovery. Perturbations are treated covariantly through `delta T -> delta T - L_xi Tbar`, so raw gauge-specific density, velocity and metric variables are prohibited as common coordinates without an invariant mapping. A transfer-level Newtonian/synchronous audit has been launched to test a comoving/gauge-invariant matter-density extractor for response-basis v0.1.1.

## 2026-08-29 — Exp073P aggregate prerequisite join readiness

Repository/history recovery established canonical Exp073R1 v0.6 Stage-B run
`33212521957` as the sole admissible heavy route.  Superseded v0.4 run
`33160570463` was cancelled by successful cleanup run `33216480776`; no partial
v0.4 output is admissible.  Before inspecting any canonical R1 output, commit
`c947a30` froze an executable aggregate prerequisite-join contract.  Commit
`6d32ce3` implemented the fail-closed evaluator and synthetic mutation suite.
CI run `33217294341` passed and emitted artifact `9703832682`, while retaining
`support_executor_authorized=false`.  Real archived preflight, large-DES, P2,
S0 and BOSS parent schemas all passed compatibility validation; 44 repository
tests passed.  R1 remains queued, so no real join, support fraction, retained
dimension, covariance, nuisance or G8 quantity was evaluated.  G7/G8/G9 remain
OPEN.

## 2026-08-29 — actual Exp073P aggregate-join route readiness

Before any terminal canonical R1 output, commit `df9a9b0` preregistered the
manual real aggregate-join execution route.  Commit `0f9173e` then implemented
a live GitHub Actions metadata collector, a manual-only read-only production
workflow and a separate synthetic route self-test.  CI run `33220212976`, job
`99012479309`, completed successfully; artifact `9704867271` has digest
`sha256:25f242b3385842a8506b6d80985c033559297ee15820b8d0df1ce7b84c46fa64`
and internal status
`PASS_EXP073P_ACTIONS_METADATA_ROUTE_SYNTHETIC_SELFTEST_V0_1`.  Ten frozen
parents and ten fail-closed metadata mutations were exercised while retaining
`support_executor_authorized=false`; 44 repository tests also passed.  The real
workflow has not run because canonical R1 `33212521957` remains queued without
an artifact.  This is infrastructure readiness only: no support, covariance,
nuisance, relation/null or G8 quantity was evaluated, and G7/G8/G9 remain OPEN.

## 2026-08-29 — Exp073R1 v0.6 attempt 1 infrastructure incomplete

Canonical run `33212521957`, attempt 1, executed on the correctly isolated
`DSIR-HOME-PC` runner.  Checkout, the unchanged evaluator-blob firewall and
both immutable parent metadata bindings passed.  Job `98988824629` then failed
before artifact download on pip's PEP 668 `externally-managed-environment`
guard while executing `python3 -m pip install --user numpy healpy`.  The 84 GB
GET never started, zero metacal rows were read, no mask or result artifact was
created, and no support/covariance/nuisance/relation/held-out quantity was
evaluated.  The outcome is `INCOMPLETE_EXP073R1`, not scientific FAIL.
Aggregate join v0.1 remains permanently fail-closed for that exact job.  A
runtime-only isolated-venv repair retained the unchanged evaluator and launched
replacement run `33222848695`, job `99020389131`.  G7/G8/G9 remain OPEN.

## 2026-08-29 — replacement R1 authority and aggregate join v0.2

While replacement R1 run `33222848695` was still inside the whole-object
84 GB mapper, before its terminal assertion and before any artifact existed,
commit `0f85b7c` froze the exact run/job/head/workflow/artifact authority for a
superseding aggregate prerequisite join.  New v0.2 adapters reuse and
hash-check every byte-frozen v0.1 semantic validator, changing only the R1
Actions identity and receipt version.  The failed v0.1 run/job/artifact are
explicitly rejected.  Evaluator and live-metadata mutation suites, manual-only
production-trigger firewall, YAML parsing and 44 repository tests pass.
Hosted self-test run `33234248213`, job `99052307444`, succeeded; artifact
`9709418334` has independently verified digest
`sha256:84a6a8c2740ad539c6a48a59e47b876122f6fd5bf4b5665e9653ecfc7c1debfc`.
The real join was not dispatched; no support, covariance, nuisance,
relation/null or G8 quantity was read, and `support_executor_authorized=false`.

## 2026-08-29 — repeated Exp073R1 remote EOF and transport-stabilized v0.7

Replacement run `33222848695` failed twice inside the unchanged frozen
whole-object reader after all evaluator and parent-integrity checks passed.
Attempt 1/job `99020389131` reached a last reported `37,748,736` rows before a
premature EOF; exact rerun attempt 2/job `99062223326` failed in its first row
chunk with `10839192/40239104` requested bytes received.  Both are classified
as repeated remote-transport infrastructure failures, not scientific FAILs.
Their independently verified uploads (`9709998972` and `9710626213`) are
inadmissible: neither contains a terminal summary or masks.  GitHub preserved
both under the same head-only artifact name despite `overwrite: false`; the
second ZIP contains only four zero-byte records.  Exp073P join v0.2 remains
fail-closed because its frozen R1 job failed and its byte-frozen collector
requires exactly one canonical-name artifact while two exist.  No partial map
or downstream quantity was evaluated.

Before another execution, commits `401b6bc`..`9a4606f` preregistered and
launched a transport-stabilized v0.7 route: independent whole-object attempts
restart at byte zero with no Range/resume; only the exact 84,075,649,920-byte
object with frozen SHA256 may be loopback-replayed to the unchanged evaluator.
Run `33240490287` attempt 1 lost the self-hosted runner during acquisition and
produced no artifact, an infrastructure outcome.  One exact rerun, attempt 2
job `99080934021`, is queued as the sole heavy candidate.

An executable audit of the frozen v0.7 snapshot records a prospective artifact
delivery risk: its single `always()` upload mixes diagnostic/result paths and
uses a SHA-only name without run-attempt identity.  This risk has not
materialized in the active run and does not alter it.  Any later new execution
after a failed upload must first freeze attempt-specific result/diagnostic
delivery.  No support fraction, `f_invalid`, retained dimension, covariance,
nuisance, relation/null or G8 quantity was read; G7/G8/G9 remain OPEN.
Hosted audit self-test run `33245678070` completed successfully and reproduced
the committed fail-closed/no-leakage record without launching a heavy mapper.

## 2026-08-29 — prospective Exp073P v0.3 authority for v0.7 attempt 2

At `2026-08-29T10:15:42Z`, while Exp073R1 v0.7 run `33240490287`, attempt 2,
job `99080934021` was still queued and its artifact list was empty, PR #166
commit `940fbca` froze a new aggregate prerequisite authority.  It admits only
that exact attempt/job/head/workflow and never repoints historical joins v0.1
or v0.2.  Commit `6f46375` implemented a manual-only v0.3 route that reuses the
byte-frozen v0.1 parent/R1 validators and adds run-attempt validation, the
attempt-specific jobs endpoint, unique artifact ID/digest binding, full-from-
zero acquisition-provenance checks and byte/hash validation of the complete
summary/acquisition/runtime plus four record and four mask files.  Partial,
duplicate, later-attempt, empty or cross-inconsistent evidence fails closed.

Local inherited and new mutation suites, JSON/YAML/compile checks and all 44
repository tests passed.  Hosted v0.3 self-test run `33248034308`, job
`99088793819`, completed successfully; artifact `9713466820` has digest
`sha256:d53b87eec234c3533fd9d167bfdae7433db27e4aa106a614c2dd5812a9f6019e`.
All receipts were synthetic and retained `support_executor_authorized=false`.
At `2026-08-29T10:30:49Z` the heavy job remained queued with no artifact; the
real v0.3 join was not dispatched.  No support fraction, `f_invalid`, retained
dimension, covariance, nuisance, relation/null or G8 quantity was read, and
G7/G8/G9 remain OPEN.

## 2026-08-29 — canonical Exp073P v0.3 guards integrated into production route

A fresh history comparison found that `main` had advanced independently to
`72c0278` while PR #166 was in development. Main already contained the
canonical prospective v0.3 preregistration (`e58bddf`, SHA256
`e27761b2db4a81283bb9fbac1decb95f62fadb785c40cb3e3f676f8651711f40`)
and hosted authority, live-metadata-set, and archive-member fail-closed guards.
The PR was merged with current main rather than merged blindly or duplicated;
the canonical preregistration bytes were preserved exactly. The earlier
independent PR preregistration remains historical chronology, not current byte
authority.

The actual manual-only v0.3 route now validates exact attempt/job branch,
event, workflow ID and job-level attempt; downloads the raw artifact ZIP by
numeric ID; verifies its canonical SHA256 before extraction; rejects token
forwarding to the signed redirect; and requires the exact 11-file archive set
before existing acquisition, payload, R1, and unchanged-parent semantic
validation. Synthetic suites rejected 23 evaluator, 9 route, 4 downloader, 4
payload and 3 integrated archive mutations. All three main supplemental guards
passed locally and `44` repository tests passed. Hosted integration run
`33257888770`, job `99114673638`, then completed successfully on the exact
two-parent integration tree. Its artifact `9716362579` has digest
`sha256:f78ed9f12c54bd585c9f5b8022e8fcb468dee7583e842c0c76363af2dfde7b33`.

At `2026-08-29T14:27:27Z`, Exp073R1 v0.7 run `33240490287`, attempt 2/job
`99080934021`, remained queued with no artifacts. No duplicate heavy run and no
real aggregate join were dispatched. No support fraction, `f_invalid`,
retained dimension, covariance, nuisance, relation/null, held-out, or G8 value
was read. `support_executor_authorized=false`; G7/G8/G9 remain OPEN.

During final synchronization, `main` advanced again to `f2d1043` with an
independent cross-member consistency guard. That guard's hosted run
`33257187305` had already rejected 19 summary/acquisition/runtime/row-accounting
mutations. Its unchanged files were merged into PR #166 and the suite passed
locally. This is additive implementation validation and does not alter the
canonical preregistration or any scientific boundary. A new exact-head hosted
check is required after this second main merge.
