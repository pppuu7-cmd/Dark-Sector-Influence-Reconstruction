# DSIR publication-facing research chronology v0.1

**Created:** 2026-08-27  
**Role:** index for manuscript reconstruction; the Git history, numbered experiments, `RESEARCH_LOG` and recovery manuals remain the authoritative full chronology.

## Chronology rules

1. Preregistration timestamp/commit must precede the scientific output it governs.
2. A later corrective experiment never rewrites an earlier FAIL/null.
3. Infrastructure failure is chronologically recorded separately from scientific classification.
4. Retrospective analysis is labelled retrospective even when scientifically useful.
5. Publication notes record when a result became manuscript-eligible but do not change its scientific status.
6. RTK remains an external sibling project; RTK chronology is not copied into the DSIR scientific ledger.

## Phase A — project separation and formal foundation

### 2026-08-23

- Dedicated DSIR repository established: `pppuu7-cmd/Dark-Sector-Influence-Reconstruction`.
- RTK explicitly excluded from the DSIR evidence chain.
- Recovery/manual architecture established so continuation does not depend on chat state.

### 2026-08-23 to 2026-08-24

- G1 conservation/gauge bookkeeping established.
- G2 response basis and same-solver/cross-solver quotient logic established.
- G3 background and beyond-background heterogeneous family atlas established with block-aware missing-domain semantics.
- Early novelty audit constrained broad claims: effective source tensors, PPF/EFT dictionaries, PCA/SVD and dark-sector degeneracy are prior art ingredients rather than DSIR inventions.

## Phase B — response geometry and failed simple compression

### 2026-08-25 to 2026-08-26

- GDM pressure/viscosity density-response near-degeneracy quantified; metric slip shown to supply an independent separator.
- GDM and designer-f(R) background/AP-null but perturbation-active patterns established.
- Simple additive `G(k)+T(z)+tau`-style compression rejected.
- Irreducible scale-time interaction `I(k,z)` and localization coordinates developed.
- Finite-amplitude trajectory curvature demonstrated: one microscopic parameter can generate more than one global representation/SVD mode.
- `N_micro`, `N_manifold`, `N_repr`, `N_disc` formally separated.

## Phase C — characteristic-scale and withheld directional tests

### 2026-08-26

- Exp049B: prospective GDM intermediate-point directional window-crossing test PASS.
- Exp049C: prospective designer-f(R) directional window-crossing test PASS.
- Exp050A: C4 thermal-WDM high-k time-dependent atlas established; response nearly time-separable on the frozen domain.
- Exp050B: withheld WDM mass/cutoff directional prediction PASS.
- Exp051A/052A: block-aware observability and discriminant coverage formalized without zero-imputing unsupported domains.
- Exp053A/F26: first genuinely withheld C6 DCDM→dark-radiation family directional mechanism test PASS.

These results strengthened the mechanism atlas but did not establish a universal law.

## Phase D — explicit falsification of over-simple cross-family laws

### 2026-08-26

- Exp054C/F27: preregistered cross-family source-response slope failed on withheld C7 IDM–DR — permanent prospective FAIL.
- Exp055A/F28: alternative endpoint-normalized crossing became retrospective candidate only.
- Exp056B/F29: fresh C8 IDM–photon broke that candidate — permanent prospective FAIL.
- Exp061A/F30: preregistered multicoordinate response-path rule survived genuinely fresh C9 IDM–baryon — prospective PASS, explicitly not a G7 law.
- Exp064A/F31: eligible DESI ShapeFit common-plane relation returned a hard statistical null; no retuning.

## Phase E — observational operator and convention preparation

### 2026-08-26

- ACT DR6 × unWISE selected covariance/window path progressively audited.
- Exact selected 26D covariance, shot-noise template and whitening operators were validated in separate prospective gates.
- CAMB↔CLASS matter/Weyl convention audits isolated a float32-first multiplication coherence floor and subsequently certified the corrected convention in a fresh experiment while preserving the original failure.
- Physical ACT×unWISE forward reproduction and PCA/source semantics were advanced without fitting a dark-sector law.

## Phase F — specificity control: matter-only geometry is not dark-specific

### 2026-08-26 to 2026-08-27

- Exp071B: retrospective F30 specificity/manifold audit.
- Exp071C preregistration commit: `4180661fe3187c710c363cdbafac12de2dc70d41`.
- Exp071C known-sector controls executed prospectively.
- Ordinary baryon-fraction control K2 passes the same normalized response-path behavior used by F30.

Resulting interpretation:

- F30 remains a valid prospective response-geometry PASS on C9;
- F30 is **not** dark-specific;
- normalized matter-response trajectories are interpreted as response-direction rotation / transfer-shape geometry;
- independent Weyl/slip information becomes central to any stronger dark-sector claim.

Synthesis merge: `8f607ca075e95fdba453c88f7d1d60c1b4e4e7e9`.

## Phase G — C5 direct physical-power provider audits

### 2026-08-26 to 2026-08-27

1. **Exp069B** — permanent scientific FAIL of the explicit-EFT Python physical-power bridge at the frozen exact-zero criterion; target discrepancy slightly exceeds `5e-6`.
2. **Exp069C** — same-node raw residual persists and does not converge away with `k_per_logint=40..320`; k-grid interpolation is not an authorized correction.
3. **Exp069D** — background-grid/RGR mechanism audit; formal completeness limited by an unstable skip-RGR case. Background geometry and RGR-threshold variation do not explain the floor.
4. **Exp069E** — exact-zero source-native RGR subset audit. Key result:
   - `F0=4.7401579076280133e-17`;
   - power residual `M0=5.302921926164412e-6`.
   The EFT-function residue is far too small to explain the ppm power floor by amplitude.
5. Pinned-source theorem establishes an exact analytic designer `A=0` GR boundary while literal `B0=0` is routed through numerical inversion. Merge: `f827e80740ed4d5d27d8a1f4c6982ba412c8895e`.
6. **Exp069F** preregistration: `43ef913645a43f091e728623291bc21642a56ab9`.
7. Exp069F execution merge: `30706773a0069b6bbe3144443debeeffa6fba328`.
8. Exp069F run `33023027901`, artifact `9627458877`, digest `sha256:d8e1a42bf813d5ae105ea33e723868d454ff7584424373ecfe4594a2dfe49358`.
9. Exp069F scientific classification:
   `GENERAL_ACCURACY_RECOVERS_FROZEN_GR_LIMIT`.
   Frozen target maxima:
   - q=1: `5.3029219262e-6`;
   - q=2: `2.9044035686e-6`;
   - q=3: `1.7011186859e-6`;
   - q=4: `1.3107890274e-6`.
   First preregistered target PASS: q=2.
10. Same-node raw maxima also decrease monotonically; q=3 is the first tested point with both target and raw maxima below `5e-6`.
11. Exp069G minimum certification burden for any future corrective C5 provider was frozen before Exp069F output was inspected. Commit: `731f0824379a977ed9a8a3f9107538854c24de65`.

Exp069B remains FAIL; Exp069F is a separate mechanism result; C5 is still not certified until a new provider experiment passes the Exp069G contract.

## Phase H — publication architecture

### 2026-08-27

A manuscript-oriented layer was added without modifying science gates:

- RTK↔DSIR separation boundary;
- staged DSIR-1 through DSIR-4 article series plus later RTK–DSIR synthesis;
- claim-to-evidence matrix;
- readiness criteria;
- publication chronology.

At this point DSIR-1 is classified `READY_FOR_DRAFTING`, but not `READY_FOR_SUBMISSION`.

## Current scientific state at this chronology cut

- C3 physical provider: eligible from its validated native route.
- C5 physical provider: not yet certified.
- common physical support-validity mask: not authorized yet.
- G7: OPEN.
- G8: OPEN.
- G9: OPEN.
- no universal dark-sector law or discovery claim is allowed.

## Append protocol

Every future research iteration that changes a manuscript-relevant conclusion must add a new dated subsection or superseding version of this index containing:

- experiment/result ID;
- preregistration commit when applicable;
- execution run/artifact/digest when applicable;
- immutable scientific classification;
- whether the result changes an article readiness state;
- any new claim that becomes allowed or prohibited.
