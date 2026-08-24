# DSIR observational-whitening research log — 2026-08-25

This log continues `docs/RESEARCH_LOG_OBSERVATIONAL_2026-08-24.md`. Scientific claim status remains controlled by `docs/GATES.md`; interpretation status is mirrored in `docs/SCIENTIFIC_FINDINGS_REGISTER.md`.

## Experiment 036 — pinned-artifact AP family geometry v0.1

### Goal

Use the exact frozen full-background solver artifacts already responsible for the C1 smooth-w and C2 interacting-vacuum local response atlas, map their dense `H(z)` histories through the hard-validated Experiment 035 AP operator, and quantify the corrected DESI DR1 ShapeFit `DH/DM` geometry directions without extrapolating the seven-node structure atlas below `z=0.295`.

The tested nonzero background directions are:

- C1 smooth non-phantom `epsilon_w=1+w -> 0+`;
- C2 physical IDE coordinate `u=-alpha>=0` on the negative-alpha ray;
- C2 beta central line.

C0 is the origin by definition. C3 GDM and C5 designer f(R) expected zero-geometry contracts are **not** zero-imputed here; their numeric audits are deferred. C4 WDM remains in its separate small-scale block.

### Frozen inputs

C1 source:

- workflow run `32771133024`;
- artifact ID `9536242626`;
- digest `sha256:ece064524a3efe0bc83d19dc98cc674a9a88f405aa56e9886cdf4ebd30d8134b`;
- upstream `s-ilic/gdm_class_public@4c87916aab5ca124a68f1dd16f31846fc13d1829`.

C2 source:

- workflow run `32760042765`;
- artifact ID `9532491954`;
- digest `sha256:408322a2ee79907dd98cdd0e532daaed1e1aeeb1b633f42ab5321cb32149ab6d`;
- upstream `kaeonikc/class_iv@ac627d54e9ce196a08878d1ba33999819925d19c`.

Corrected DESI DR1 ShapeFit geometry order is inherited from the frozen erratum product. The five geometry bins are `LRG1, LRG2, LRG3, ELG2, QSO` at `z_eff=(0.51,0.71,0.92,1.32,1.49)`.

### Hard thresholds

Before the CI hard execution the finite-difference convergence ceiling was frozen at relative L2 `<0.005` for the `1e-3` versus production `1e-4` tangent comparison in all three directions. This is the same 0.5% readiness scale used previously. Pairwise model angles were descriptive outputs only: **no angular pass/fail threshold and no rank threshold were defined**.

### Infrastructure-only first attempt

PR #17 triggered run `32782445280`. It stopped before the scientific script because the workflow incorrectly supplied an unsupported `artifact-ids` input to `actions/download-artifact@v4`. No hard calculation ran and no scientific threshold was changed.

The workflow was corrected to pin the exact prior workflow `run-id` values while keeping `actions:read` permission and the same expected full-background file audit. This was an infrastructure repair only.

### Successful hard run

Run `32782545098` completed successfully with status

`PASS_AP_FAMILY_GEOMETRY_V0_1`.

Result artifact:

- artifact ID `9540273287`;
- artifact SHA256 `553faa2ef7ddbc44e25ddd6faca237d0be7fc265b9c23cfafb2a32570534d126`;
- frozen repository result: `data/derived/observational_whitening/experiment_036_ap_family_geometry_v0_1.json`.

The locally re-downloaded ZIP reproduced the same SHA256 exactly.

### Tangent convergence

Relative L2 difference between `1e-3` and production `1e-4` tangents:

- C1 smooth-w: `0.0015563369067206232`;
- C2 negative-alpha physical ray: `0.00013881893807444795`;
- C2 beta: `2.2598694354308047e-07`.

All are below the frozen `0.005` ceiling. Corresponding angular changes are `0.0760677 deg`, `0.000427325 deg`, and `4.75e-06 deg`.

### Corrected DESI DH/DM marginal whitening

Marginal geometry errors used:

`(0.0986153, 0.0602861, 0.0403126, 0.0321081, 0.0241781)`.

The production marginal-whitened local directions are:

- C1 smooth-w: `(-1.41304,-1.31463,-0.894084,+0.0738609,+0.390460)`;
- C2 negative-alpha: `(+0.508495,+1.03058,+1.65433,+1.86211,+2.57806)`;
- C2 beta: `(-0.820339,-1.45008,-2.05131,-1.88235,-2.41677)`.

Their norms are reported only per heterogeneous local parameter unit and **must not** be interpreted as detection significance or parameter constraints.

### Pairwise geometry

Marginally whitened angles:

- smooth-w vs IDE negative-alpha: oriented `107.196507 deg`, acute `72.803493 deg`;
- smooth-w vs IDE beta: oriented/acute `64.151094 deg`;
- IDE negative-alpha vs IDE beta: oriented `170.962099 deg`, acute `9.037901 deg`.

The key new hard result is therefore

\[
\boxed{\theta_{AP}^{acute}(\alpha_-,\beta)=9.0379006^\circ}
\]

while the already frozen IDE structure-block angle is about `58.9338 deg`.

### Scientific interpretation

This hard-confirms a new independent example of channel-dependent degeneracy: two IDE mechanism directions that are substantially separated in structure become nearly antiparallel in AP background geometry. AP therefore cannot replace growth/structure for distinguishing these C2 interaction directions.

This strengthens the DSIR working meta-hypothesis that model identity is encoded by a **multi-channel influence trajectory**, not by one observable response shape. It remains a supported hypothesis, not a law, because family-complete joint observational whitening and holdout prediction gates are still absent.

### Claim boundary / gate consequences

Experiment 036 is:

- not a full four-coordinate ShapeFit likelihood;
- not a parameter constraint or detection significance;
- not yet a family-complete C0-C5 AP geometry claim;
- not an intrinsic-rank result;
- not a residual law.

Therefore G5 remains **PARTIAL**, G7 remains **OPEN**, and G8 remains **OPEN**.

## Immediate continuation after Experiment 036

1. Audit the expected exact/near-zero AP response for C3 GDM `cs2/cv2` numerically from the pinned solver lineage; do not equate an unavailable response with zero.
2. Audit C5 designer f(R) Lambda-like background numerically from the pinned H-EFTCAMB lineage, creating a dedicated background-output workflow if the existing artifact is insufficient.
3. Only then form the family-complete AP geometry cell.
4. Build the family-complete gauge-safe corrected-ShapeFit growth operator.
5. Replace/calibrate the finite-node `m+n` proxy with a survey/window-aware shape operator or explicit compression-model error.
6. Continue updating `SCIENTIFIC_FINDINGS_REGISTER.md`, `STATUS.md`, and `RECOVERY_LATEST.md` on every substantive iteration; preserve any future contradiction as `SUPERSEDED/RETRACTED` rather than deleting it.
