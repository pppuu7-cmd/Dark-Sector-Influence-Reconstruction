# Experiment 037 — GDM AP-zero audit v0.1

## Purpose

Hard-test the C3 geometry contract that the frozen generalized-dark-matter perturbation directions `cs2_gdm` and `cv2_gdm`, with `w_gdm=0`, do not alter the background expansion and therefore have zero Alcock–Paczynski response.

This closes a specific missing-response ambiguity left by Experiment 036. The result is allowed to enter the family-complete AP block as zero **only if the exact pinned solver artifact numerically validates the zero response**. Missing data are never replaced by zero.

## Frozen source

Use the immutable artifact that already generated the frozen C3 `cv2` manifold and contains the local `cs2` controls:

- workflow run `32759738560`;
- artifact ID `9532247349`;
- artifact name `gdm-cv2-manifold-15c7128d4220b954783a8ba7cce7c06744f7f0ac`;
- digest `sha256:126c839ce948b5b25ec46b687af70e230c31d87071e6526727d1551a3c0f136d`;
- upstream `s-ilic/gdm_class_public@4c87916aab5ca124a68f1dd16f31846fc13d1829`.

The artifact contains full `background.dat` histories and matching INI files for the reference plus nonzero `cs2/cv2` controls.

## Audited directions

Reference:

- `w_values_gdm=0`, `cs2_values_gdm=0`, `cv2_values_gdm=0`.

Nonzero perturbation directions:

- `cs2={1e-8,1e-7,1e-6}` with `w=0`, `cv2=0`;
- `cv2={1e-8,1e-7,1e-6,1e-5,1e-4}` with `w=0`, `cs2=0`.

The INI contract is checked by the hard script rather than inferred from filenames.

## Observation operator

Reuse `src/dsir/ap_operator.py` from Experiment 035. For each variant,

\[
r_E(z)=\ln[H_{model}(z)/H_{ref}(z)]
\]

is constructed from the full same-solver history and mapped to

\[
\Delta\ln(D_H/D_M)=-\Delta\ln F_{AP}
\]

on `z=(0.51,0.71,0.92,1.32,1.49)`.

No seven-node structure-history extrapolation is used.

## Hard thresholds frozen before CI execution

The production hard gate is tolerance-based, not bitwise-equality based:

- maximum redshift-grid mismatch `<=1e-12`;
- maximum relative `H(z)` difference `<=1e-12`;
- maximum absolute `Delta ln(D_H/D_M)` at the five target redshifts `<=1e-12`;
- INI configuration contract must pass exactly.

The numeric-table bitwise equality flag is recorded only as a diagnostic and is **not** required for PASS.

These thresholds are chosen as a stringent solver/observation-operator zero test while remaining far looser than machine exactness. They are not adjusted based on any pairwise model angle or rank outcome.

## Exploratory inspection disclosure

Before writing the hard workflow, the exact artifact was manually inspected to confirm that the required full background files exist. A private exploratory numeric comparison found the sampled background tables identical at printed solver precision. This observation motivated running the explicit hard audit; it is **not** itself the frozen result. The CI thresholds above are deliberately tolerance-based and the scientific status remains preliminary until the GitHub hard run passes.

## Claim boundary

A PASS establishes only that, **within this frozen C3 GDM manifold and solver realization**, the sampled `cs2/cv2` perturbation directions leave the background/AP geometry zero to the stated tolerance.

It does not prove:

- zero AP response for arbitrary time-dependent `w_gdm` histories;
- zero perturbation response (the same directions have large nonzero matter-power responses);
- a full C0-C5 geometry completion until the C5 designer-f(R) background is also audited;
- any rank, residual law, parameter constraint, or discovery.

## Required repository updates after hard PASS

1. Freeze the CI JSON under `data/derived/observational_whitening/`.
2. Update `docs/SCIENTIFIC_FINDINGS_REGISTER.md`.
3. Update `docs/STATUS.md`.
4. Update `docs/RECOVERY_LATEST.md`.
5. Append the dated observational research log.
6. Keep G5 PARTIAL and G7/G8 OPEN unless a separate gate criterion is satisfied.
