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

## Experiment 037 — hard GDM AP-zero audit v0.1

### Goal

Convert the expected C3 `cs2/cv2` zero-background geometry cell from a theory expectation into an explicit solver-level fact before inserting it into the AP response block.

The exact frozen GDM_CLASS artifact from run `32759738560` was reused. Source artifact ID `9532247349`, digest `sha256:126c839ce948b5b25ec46b687af70e230c31d87071e6526727d1551a3c0f136d`, upstream `s-ilic/gdm_class_public@4c87916aab5ca124a68f1dd16f31846fc13d1829`.

### Audited parameter contract

Reference INI: `w_gdm=cs2=cv2=0`.

Audited nonzero closure directions:

- `cs2={1e-8,1e-7,1e-6}`, with `w=0`, `cv2=0`;
- `cv2={1e-8,1e-7,1e-6,1e-5,1e-4}`, with `w=0`, `cs2=0`.

The hard script parsed and checked each INI rather than trusting the filenames.

### Pre-frozen hard thresholds

Before CI execution:

- maximum background redshift-grid mismatch `<=1e-12`;
- maximum relative `H(z)` mismatch `<=1e-12`;
- maximum absolute `Delta ln(DH/DM)` at `z=(0.51,0.71,0.92,1.32,1.49)` `<=1e-12`;
- configuration contract required.

Bitwise equality of the full saved numeric background table was recorded only as a diagnostic, not required for PASS.

The protocol disclosed that an exploratory inspection had already found printed-precision equality. The threshold itself was not chosen from an angle/rank result and remained a tolerance-based hard zero test.

### Hard result

GitHub Actions run `32783243120` passed with status

`PASS_GDM_AP_ZERO_AUDIT_V0_1`.

Result artifact:

- artifact ID `9540510596`;
- SHA256 `ba1fa93e348f9685d84a675311c79f9c746574463086710b4a46911d125f4edf`;
- the locally downloaded ZIP reproduced that SHA256 exactly;
- frozen repository result: `data/derived/observational_whitening/experiment_037_gdm_ap_zero_audit_v0_1.json`.

For **every** audited nonzero `cs2/cv2` variant:

- `z_grid_max_abs = 0`;
- `max_abs_H = 0` in saved solver units;
- `max_relative_H = 0`;
- all saved numerical background columns were exactly equal to the reference table;
- `Delta ln(DH/DM)=(0,0,0,0,0)` at the five DESI target redshifts.

### Scientific interpretation

Within the frozen C3 manifold with `w_gdm=0`, the `cs2/cv2` directions are **background/AP-null but perturbation-active**. The same parameters have established nonzero matter-power/metric responses, so the zero geometry coordinate does not mean proximity to the common response origin in the full multi-channel space.

This provides a particularly clean hard example of **channel nullity / block-sparse influence**:

\[
K_{AP}t_{cs2}=K_{AP}t_{cv2}=0,
\]

while perturbation operators satisfy

\[
K_{structure}t_{cs2}\neq0,\qquad K_{structure}t_{cv2}\neq0.
\]

It strengthens, but does not prove universally, the DSIR meta-hypothesis that model identity is a multi-channel influence trajectory rather than a single observable response.

The C3 AP geometry cell may now be encoded as a validated zero rather than as missing data. This is qualitatively different from zero-imputation.

### Claim boundary / gates

The result applies only to the sampled frozen `w_gdm=0` C3 manifold. It does not cover arbitrary nonzero/time-dependent `w_gdm`, and it does not imply that GDM is observationally null.

G5 remains **PARTIAL** because C5 AP geometry and the family-complete growth/shape observation operators are still missing. G7 and G8 remain **OPEN**.

## Immediate continuation after Experiment 037

1. Numerically audit the C5 designer-f(R) background/AP contract. The frozen H-EFTCAMB artifact preserves `EFTwDE=0` configs and indicates background writing was enabled, but no immediately usable full background table was found in the preserved artifact; use the same pinned H-EFTCAMB setup in a dedicated background-output hard workflow if needed.
2. After C5, form the family-complete AP geometry cell (C0 origin, C1/C2 measured tangents, C3 hard zero, C5 audited result; C4 remains a separate small-scale block unless a validated AP mapping is defined).
3. Build the family-complete gauge-safe corrected-ShapeFit growth operator.
4. Replace/calibrate the finite-node `m+n` proxy with a survey/window-aware shape operator or propagate explicit compression-model error.
5. Continue updating `SCIENTIFIC_FINDINGS_REGISTER.md`, `STATUS.md`, and `RECOVERY_LATEST.md` on every substantive iteration; preserve future contradictions as `SUPERSEDED/RETRACTED` rather than deleting them.
