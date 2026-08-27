# DSIR recovery checkpoint — post Exp069H / pre Exp069I

**Date:** 2026-08-27  
**Purpose:** restore the exact active state after C5 provider certification and before the raw-k unit/provenance audit.

## Hard project boundaries

- DSIR and RTK remain independent evidence chains.
- No RTK PASS can close a DSIR gate and vice versa.
- No hidden/common RTK↔DSIR dark-sector statistic is authorized.
- A DSIR `mu`-like quantity, if used later, must be derived inside the DSIR basis/window/operator chain rather than supplied as an RTK-dependent external latent value.
- Missing theory/channel domains remain masked, never zero-imputed.
- Prior FAIL/null results remain immutable.

## Current scientific synthesis

1. Matter-only response geometry is a useful mechanism/transfer-shape taxonomy but not a unique dark-sector detector.
2. Exp071C K2 and reproducible retrospective Exp071D show that low PCA/SVD dimension does not imply a monotone/injective microscopic inverse.
3. Independent Weyl/slip/lensing channels are therefore central to stronger dark-specific identifiability.
4. Formal observation-space comparison is organized by `A_B=Q_B W_B K_B`, with equivalence determined by the channel/covariance/nuisance-dependent kernel.
5. No universal dark-sector residual law has yet survived the full physical-provider/support/covariance/nuisance chain because G7 is still OPEN.

## C3 provider — certified

Exp070C remains

`PASS_C3_GDM_NATIVE_GRID_PHYSICAL_POWER_PROVIDER_V0_1`.

Pinned solver:

`s-ilic/gdm_class_public@4c87916aab5ca124a68f1dd16f31846fc13d1829`.

Run `33017214292`, artifact `9625032179`, digest
`sha256:34cf89f2207c72b4e3d669f7e4e6419753b6b046ed7de9e3a9fa7fb144b4c081`.

Its native-grid physical `P_mm`, signed `P_Wm`, `P_WW` provider is eligible. Exp070A remains permanent FAIL and Exp070B remains `INTERPOLATION_DOMINATED`.

## C5 history preserved

- Exp069B: permanent `FAIL_C5_EXPLICIT_EFT_PYTHON_POWER_BRIDGE_V0_1`.
- Exp069E: exact-zero EFT-function subset amplitude `F0=4.7401579076280133e-17` while q=1 target power mismatch stayed `5.302921926164412e-6`.
- Exp069F: `GENERAL_ACCURACY_RECOVERS_FROZEN_GR_LIMIT`; q=2 first formal target PASS, q=3 first tested q with both target/raw maxima below `5e-6`.
- Exp069G minimum corrective-provider contract remains binding.

## Exp069H — certified C5 provider

Implementation merge:

`26162b0f2472dc1862eeb60b564a3563eaae12f9`.

Execution provenance:

- run `33024638764`;
- artifact `9628053962`;
- digest `sha256:fa61b504d31edeba2afcbed0f4b14bda688df82a96d2cba55eac034682b5382f`;
- pinned `EFTCAMB/EFTCAMB@16d9c4e9f85751e30efd0a53b177941713078904`.

Scientific classification:

`PASS_C5_Q3_UNMODIFIED_UPSTREAM_PHYSICAL_PROVIDER_V0_1`.

Frozen hard metrics:

- C1 target zero closure `1.7011186858522977e-6 <= 5e-6`;
- C1 raw same-node zero closure `2.8421302380756537e-6 <= 5e-6`;
- tiny-positive B0 `1e-12,1e-10,1e-8` continuity target/raw maxima all `0.0`;
- production `B0=1e-6` target signal `0.013249122882007408 >= 1e-3`;
- independent zero rerun target/raw differences `0.0 <= 1e-12`;
- signed cross-power/accessor semantics PASS;
- all seven fresh case payloads have 35/35 negative target `P_Wm` cells and no positive/zero cells;
- no source patch, residual floor subtraction or renormalization.

Therefore C5 is certified under Exp069G. Exp069B remains FAIL.

## Post-run raw-k field provenance issue

Before any common physical support mask was constructed, source audit found that Exp069H raw arrays were produced by

`get_linear_matter_power_spectrum(..., hubble_units=False, nonlinear=False)`

without explicit `k_hunit`.

Pinned upstream has default `k_hunit=True` and transforms

`kh = ks/(H0/100)`

when true, versus `kh=ks` when false.

Therefore the historical artifact field name `raw_k_Mpc^-1` is not safe as a physical-k label. The old artifact is immutable and must not be rewritten.

Current impact assessment before Exp069I:

- target-grid Exp069H C1 is unaffected because the interpolator explicitly used `k_hunit=False`;
- raw GR/designer ratios were computed on exactly identical raw node arrays and are dimensionless, so a common axis relabeling is not by itself a residual change;
- nevertheless physical support selection depends on correct k units, so the support mask is blocked until a fresh prospective audit proves the defect is label-only.

## Exp069I — current next protocol

Prospective file:

`experiments/069i_exp069h_raw_k_unit_provenance_audit_prereg_v0_1.md`.

No Exp069I solver output existed when the protocol was frozen.

Frozen hard checks:

- U1 pinned-source/default binding plus implicit-vs-explicit-true exact equality;
- U2 `k_default * h_read -> k_physical` relative closure `<=5e-14`;
- U3 exact raw power-array invariance under default/true/false k-unit output convention;
- U4 exact raw residual-field invariance and unchanged explicit-physical raw maximum `<=5e-6`;
- U5 fresh explicit-physical target regression `<=5e-6`;
- U6 corrected schema: default/true raw k must never again be labeled physical `1/Mpc`; physical support must use explicit `k_hunit=False`.

Allowed complete outcomes:

- `PASS_EXP069H_RAW_K_UNIT_PROVENANCE_BUG_LOCALIZED_V0_1`;
- `FAIL_EXP069H_RAW_K_UNIT_PROVENANCE_AUDIT_V0_1`.

Incomplete execution remains infrastructure/incomplete, not a science FAIL.

If PASS, only then preregister the common C3+C5 physical support-validity mask using explicit physical-k semantics. If FAIL, suspend C5 downstream eligibility without rewriting the historical Exp069H classification.

## Publication state

- DSIR-1 observable-response geometry: `READY_FOR_DRAFTING`.
- DSIR-2 matter/Weyl physical discriminants: still `NOT_READY`; C3/C5 providers are now certified, but corrected physical-k provenance and common support mask remain incomplete.
- DSIR-3: `NOT_READY`; nuisance quotient/G7 chain incomplete.
- DSIR-4: `NOT_READY`; fresh G8 incomplete.
- RTK–DSIR synthesis: `NOT_READY`; independent evidence chains remain mandatory.

N1A close-competitor audit has narrowed novelty wording; N1B/full-text/citation-graph work remains before submission.

## Exact continuation order

1. Merge Exp069H result record and this recovery checkpoint.
2. Merge Exp069I preregistration before any Exp069I solver run.
3. Implement Exp069I exactly to U1–U6 with no changed tolerance.
4. Execute and classify Exp069I.
5. On PASS only: preregister the common C3+C5 physical support-validity mask using explicit `k_hunit=False` C5 coordinates and native physical C3 semantics.
6. Apply the mask only under its frozen rule.
7. Restrict/rebuild observational covariance/whitener only after support binding.
8. Freeze nuisance tangent SVD/rank rule.
9. Execute G7 quotient/relation/null control.
10. Only after a frozen G7 candidate choose a genuinely fresh G8 family.

G7/G8/G9 remain OPEN.

## Recovery read order

1. `docs/RECOVERY_MANUAL.md`.
2. `docs/RECOVERY_POST_EXP067E_2026-08-26.md`.
3. `docs/RECOVERY_POST_EXP069F_PUBLICATION_2026-08-27.md`.
4. this file.
5. `docs/publications/RESEARCH_CHRONOLOGY_V0_1.md`.
6. `docs/publications/ARTICLE_READINESS_LEDGER_V0_1.md`.
7. current numbered experiment/result.
