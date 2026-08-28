# DSIR checkpoint — Exp071H terminal science result + canonical Exp073R1 v0.5 live state

**Date:** 2026-08-28

## 1. Exp071H terminal result

Frozen preregistration: `experiments/071h_k2_finite_bin_growth_dual_provenance_control_prereg_v0_1.md`, commit `93bd51867d90fa346ce644deebe228e6d0d45697`.

Execution run: `33179056348`, job `98875221176`.

Workflow conclusion: `success`.

Frozen primary classification:

`K2_FINITE_BIN_GROWTH_SEPARATED_FROM_BOTH_GDM_1E7_AXES_EXP071H`

Primary oriented finite-bin-growth angles:

- K2 bar1 vs GDM `cs2=1e-7`: `138.10058532621147 deg`;
- K2 bar1 vs GDM `cv2=1e-7`: `137.0972592611391 deg`.

Both exceed the prospectively frozen `45 deg` separation threshold, so this is a genuine preregistered science PASS for the Exp071H question.

### Provenance sensitivity, non-classifying

Using the older Exp040 averaged C3 parents:

- K2 bar1 vs averaged cs2-growth axis: `138.11067377964937 deg`;
- K2 bar1 vs averaged cv2-growth axis: `137.071079544195 deg`;
- change relative to the primary single-step parents: `+0.01008845343790199 deg` and `-0.026179716944113807 deg`;
- primary GDM cs2/cv2 growth acute angle: `1.2926742378147884 deg`;
- Exp040-averaged GDM cs2/cv2 growth acute angle: `1.334012803561052 deg`.

Thus the primary K2 separation result is insensitive at the few-hundredths-of-a-degree level to this frozen parent-provenance choice.

### K2-family robustness, non-classifying

- maximum growth-direction drift among bar2..bar5 relative to bar1: `0.4195723137751324 deg`;
- centered growth-family SVD first-component variance fraction: `0.9999902495030846`;
- first two cumulative variance fraction: `0.999999994523`.

This supports the interpretation that the K2 finite-bin temporal-response family is effectively one-dimensional on the frozen support, while remaining strongly separated from both local GDM 1e-7 growth axes.

### Integrity/provenance

The workflow re-bound immutable parent artifacts from Exp071C run `33020201997` and GDM metric run `32774198185`, reproduced Exp071F raw-matter angles, passed endpoint/constant-mode/linearity controls, and uploaded artifact ID `9688888346` with artifact ZIP SHA256

`60d582b9f0249329c323066f248cbdc33f3c149966eb30317ecb2f3f22cda0a5`.

Exp071G v0.1 remains retired without science classification because of its parent-binding mismatch; Exp071H is the corrected prospectively frozen dual-provenance control.

## 2. Scope of the Exp071H result

Exp071H is a theory-space temporal-response discrimination result. It is not an observational tracer/RSD or `f sigma8` result and it does not close G7, G8, or G9.

No acceptance criterion was modified after seeing the result.

## 3. Canonical Exp073R1 v0.5 state observed in the same iteration

Run `33175886694` remains the authoritative heavy G7 reconstruction route.

Stage A `source-index`, job `98864259826`, is terminal `success` with

`PASS_EXP073R1_V05_SOURCE_WHOLE_STREAM_INDEX_BINDING`.

It exactly bound the authoritative source-redshift object by whole-object byte count and SHA256, with zero HTTP Range requests, and produced the row-aligned source index.

Job `metacal-map` (`98873808534`) remains `in_progress` in the step

`Sequentially stream authoritative metacal object and execute frozen mapper`.

No duplicate Exp073R1 heavy run was launched.

No Exp073P support fraction, covariance, whitening, nuisance tangent SVD/rank, quotient/relation/null control, or G8 withheld-family statistic was evaluated.

## 4. Gate ordering preserved

The authoritative G7 chain remains:

`validated physical forward/power-input bridges -> canonical Exp073R1 reproduction PASS -> preregistered Exp073P physical support-validity mask -> covariance restriction/whitening -> nuisance tangent rank/SVD -> quotient/relation/null control -> fresh G8 withheld family`.

Until `PASS_DESY1_FULL_ONEPASS_WEAK_LENSING_MASK_EXP073R1` is terminally produced by the canonical run, Exp073P remains blocked.
