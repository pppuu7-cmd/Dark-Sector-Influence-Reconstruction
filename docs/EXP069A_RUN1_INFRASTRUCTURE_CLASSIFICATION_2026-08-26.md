# Exp069A run #1 infrastructure classification — 2026-08-26

Run: `33008528749`  
Artifact: `9621694630`  
Artifact SHA256: `a72dd106ab25c0c2c2b0a16dc2b84e0378fed06b46b9c640863cd26cfae2b06d`

## Classification

The first Exp069A workflow is **not an evaluable scientific PASS/FAIL** for the frozen C5 bridge criteria A2–A8.

All six child cases entered the pinned H-EFTCAMB Python path, constructed `results`, and evaluated the direct physical power arrays before the diagnostic payload was serialized. Every child then raised the same Python-only exception:

```text
ValueError: invalid literal for int() with base 10: 'NonLinear_none'
```

at the diagnostic line

```python
"nonlinear_enum": int(pars.NonLinear)
```

The pinned wrapper represents `pars.NonLinear` as the string-like enum value `NonLinear_none`; converting it to integer was an instrumentation bug. Because each child crashed before writing its case JSON, the aggregate record contained no physical cases, and A3–A8 could not be numerically evaluated. The aggregate `FAIL_C5_DESIGNER_FR_PHYSICAL_POWER_BRIDGE_V0_1` token in that incomplete record is therefore an infrastructure-contaminated sentinel, not a scientific finding.

The later preservation step also raised `KeyError: 'pass'` only because A7 was necessarily empty when no GR case JSON existed. That second error does not change the classification.

## Permitted fix

The preregistration explicitly allows infrastructure repair when the frozen scientific contract is unchanged. The repair commit `31063fc03b253e4f31c9d447ee2afa9f199be995` changes only representation/serialization of the already-frozen nonlinear-mode control:

- serialize the enum as text;
- serialize the boolean identity `pars.NonLinear == model.NonLinear_none`;
- evaluate the already-frozen A3 statement “no nonlinear correction requested” from that boolean.

No solver commit, cosmology, designer settings, B0 grid, z/k grid, power pair, physical-unit flag, tolerance, negative control, or A2–A8 scientific criterion is changed.

The next run is the first run eligible to produce a complete Exp069A scientific outcome. This note and the run-1 artifact remain preserved for chronology.

**G7 OPEN, G8 OPEN, G9 OPEN.**
