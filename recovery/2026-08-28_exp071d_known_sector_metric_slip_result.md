# Exp071D — K2 known-sector metric/slip control result

**Date:** 2026-08-28

## Immutable provenance

- preregistration: `experiments/071d_k2_known_sector_metric_slip_control_prereg_v0_1.md`
- first attempt: run `33176399406` — infrastructure FAIL before science evaluation (`GITHUB_ENV` same-step visibility bug); scientific contract unchanged.
- workflow-only fix: exported already-resolved immutable artifact paths within the same shell step.
- evaluable retry: run `33176559280`
- job: `98866586563`
- result: workflow SUCCESS
- artifact id: `9687861012`
- artifact name: `exp071d-known-sector-metric-slip-e334254244768ee11a957bab1a72d28dc9ef527b`
- artifact digest: `sha256:3fcad77a7cdf8d6a18c155b4915c8bc1129dd296f0fb5edd462d1b09dcd5c01e`
- fresh known-sector solver: official `lesgourg/class_public@e85808324f51fc694d12e3ed7439552a3c3f9540`
- immutable parents:
  - Exp071C run `33020201997` known-sector F30 falsification;
  - GDM metric/slip run `32774198185`, hard status `PASS_GDM_SLIP_BREAKS_LOW_K_DEGENERACY`.

## Frozen classification

`K2_SLIP_TO_WEYL_RATIO_OVERLAPS_GDM_AXES_EXP071D`

The prospectively frozen quantity was

`q_slip/W = ||Delta_slip||_2 / ||r_W||_2`

on the identical flattened `(z,k)` grid.

### K2 values

For increasing baryon fraction at fixed `omega_m=0.1424`:

1. `1.4216648048116189e-08`
2. `1.3803745428933572e-08`
3. `1.3522853240693290e-08`
4. `1.3254583310045893e-08`
5. `1.3143575292683846e-08`

### Frozen GDM local-axis values

- `cs2_1e-7`: `9.617515757554794e-09`
- `cv2_1e-7`: `7.638683581854851e-05`

The classification is OVERLAP because the maximum K2 ratio is **not** strictly below both GDM local-axis ratios. Numerically K2 is close in order of magnitude to the pressure/sound-speed axis and enormously below the viscosity axis.

This is intentionally not reclassified after seeing the numbers.

## Additional preregistered diagnostics

The K2 family is itself geometrically stable in each metric channel:

- `r_W` tangent angles to the first K2 tangent: approximately `0, 0.0405, 0.0824, 0.1240, 0.0777 deg`;
- `Delta_slip` tangent angles: approximately `0, 1.9568, 2.4735, 2.5334, 2.2792 deg`.

Family-local SVD:

- `r_W`: first variance fraction `0.9658896701042765`, first two cumulative `0.9999848154522245`;
- `Delta_slip`: first variance fraction `0.9083859933574808`, first two cumulative `0.9924300286287324`.

Thus the K2 result is not driven by a wildly unstable family direction.

## Scientific consequence for Article 2

Exp071C already falsified the statement that matter-only F30 is dark-sector-specific. Exp071D now falsifies the stronger shortcut that a **single scalar relative-slip amplitude ratio** automatically restores generic specificity.

The defensible hierarchy is more precise:

- matter-only morphology: useful but known-sector mimic exists;
- metric/slip channel: contains genuinely new information (the GDM `cs2`/`cv2` separator remains real);
- relative slip amplitude alone: not universally dark-specific, because K2 overlaps the `cs2` scale under the frozen ordering test;
- full **directional geometry** in the joint `r_W + Delta_slip` space remains the next admissible question.

This motivates a prospective cross-family direction-angle control rather than retuning the scalar ratio.

## Forbidden claims

- Do not claim K2 reproduces the full GDM `cs2` response direction; Exp071D tested a norm ratio, not a vector angle.
- Do not claim K2 overlaps the `cv2` axis: its scalar ratio is many orders of magnitude below the frozen `cv2` ratio.
- Do not claim metric/slip information is useless; the prior GDM `cs2`/`cv2` hard separator remains PASS.
- Do not claim dark-sector detection or observational preference.

G7/G8/G9 remain OPEN.
