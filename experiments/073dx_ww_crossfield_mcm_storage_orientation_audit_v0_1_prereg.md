# Exp073DX — WW cross-field MCM storage/orientation audit v0.1

Status: prospectively preregistered diagnostic-only `+0/+0`; no science gate and no adapter acceptance gate.

## Motivation
Exp073DU and the prospectively repaired Exp073DW both failed exact adapter equality for a distinct spin-2 S0→S1 workspace, while auto-workspace and prior Wm routes had passed their own exact gates. Exp073DW rules out the pre-serialization/reload reference-state explanation. Before changing any production adapter, isolate whether the FITS `WSP_PRIMARY` payload consumed by the mmap adapter has a storage/orientation relation to PyMaster `get_coupling_matrix()` that is hidden by auto/symmetric cases.

## Frozen diagnostic
Using the same deterministic NSIDE=16 S0/S1 masks and edges `[0,6,12,18,24,30,36,42,48]`, build W01, W10, W00, W11; write and officially reload them. For each workspace record SHA256 and exact `numpy.array_equal` relations among:
1. official reloaded `get_coupling_matrix()`;
2. raw FITS `WSP_PRIMARY` array;
3. transpose of raw FITS array.
Also record exact symmetry of each official matrix and exact W01-vs-W10 transpose/equality relations.

No candidate relation is a PASS criterion; the audit is observational. It must not modify Exp073DU/DW outcomes, production adapter arithmetic, WW science thresholds, or any existing authority. Any successful diagnostic execution is `DIAGNOSTIC_COMPLETE +0/+0`; infrastructure failure is `INFRASTRUCTURE_FAIL +0/+0`.

Runtime: GitHub-hosted Ubuntu, PyMaster/NaMaster 2.7, synthetic data only. No self-hosted runner ownership.
