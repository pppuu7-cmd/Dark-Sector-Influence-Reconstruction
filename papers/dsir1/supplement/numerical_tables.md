# DSIR-I supplementary numerical tables — v0.1

**Purpose:** retain exact frozen numerical detail removed from the compact JCAP main-text table set. Values are copied from manuscript-provenance-bound products summarized in `TABLES_DRAFT.md`. These tables do not alter any scientific classification or boundary.

## Supplementary Table S1. Theory-family atlas and tangent morphology

### S1a. Theory-family atlas and informative response blocks

| Class | Representative family | Background/AP | Low-k matter | Metric/Weyl/slip | High-k transfer | Main DSIR-I role |
|---|---|---|---|---|---|---|
| C0 | LambdaCDM/GR | reference | reference | reference | reference | common response origin |
| C1 | smooth non-phantom DE | active | weakly nonseparable | not central to current discriminator | not used | background-active, weak low-k scale-time coupling |
| C2 | interacting dark sector | active/exchange | nearly scale-time separable on tested rays | channel migration possible | not used | exchange-active near-separable low-k response |
| C3 | GDM, `w=0`, pressure/viscosity rays | exact null in frozen setup | active; pressure/viscosity nearly collinear | slip strongly separates pressure/viscosity | not used | perturbation-only flagship channel-degeneracy case |
| C4 | thermal WDM | approximately common for current purpose | low-k nearly blind | not central here | strongly active | scale-localized/free-streaming, nearly time-separable on frozen high-k linear block |
| C5 | designer `f(R)` | exact null in frozen setup | active; strong scale-time interaction | modified-gravity response | current article uses low-k block | strongest current low-k nonseparability/curvature example |
| C6 | DCDM -> dark radiation | active temporal evolution | active | not central here | not central here | genuinely withheld temporal-localization mechanism |

**Boundary:** “not used/not central” never means zero. Undefined or intentionally blind blocks remain masked.

### S1b. Representative low-k tangent interaction fractions

For `R(z,k)=mu+T(k)+tau(z)+I(z,k)` and `chi_I=||I||^2/||R||^2`:

| Direction | `chi_I` |
|---|---:|
| C2 IDE negative-alpha | `1.57e-11` |
| C2 IDE beta | `5.49e-11` |
| C1 smooth-w | `1.0805e-3` |
| C3 GDM `c_s^2` | `4.5305e-2` |
| C3 GDM `c_v^2` | `4.3634e-2` |
| C5 designer `f(R)` | `2.99856e-1` |

**Boundary:** these are frozen tangent-direction morphology values, not universal thresholds.

## Supplementary Table S2. Pairwise localization of irreducible separation

| Pair | full-grid `eta_I` | Leave-one-node range / caveat |
|---|---:|---|
| GDM `c_s^2` vs designer `f(R)` | `0.611982` | `0.5504 .. 0.6539` |
| GDM `c_v^2` vs designer `f(R)` | `0.613829` | `0.5520 .. 0.6554` |
| IDE-alpha vs designer `f(R)` | `0.571946` | descriptive only in current table |
| GDM `c_s^2` vs `c_v^2` | `0.731139` | total matter angle only `~0.323 deg`; large fraction of a tiny separation |

**Boundary:** `eta_I` is a localization fraction, not signal-to-noise or detectability.

## Supplementary Table S3. Channel-conditional response angles

### S3a. GDM pressure versus viscosity

| Response block | Angle |
|---|---:|
| low-k matter | `0.322616 deg` |
| Weyl amplitude | `0.300746 deg` |
| metric slip | `137.943199 deg` |
| equalized Weyl + slip | `56.963184 deg` |

### S3b. GDM versus designer `f(R)`

| Pair | leading scale-mode angle | time-mode angle | oriented full-response angle |
|---|---:|---:|---:|
| GDM `c_s^2` vs `f(R)` | `0.078132 deg` | `25.1839 deg` | `154.8161 deg` |
| GDM `c_v^2` vs `f(R)` | `0.101694 deg` | `25.4937 deg` | `154.5063 deg` |

**Boundary:** these are frozen theory-response angles, not survey posterior separations.

## Supplementary Table S4. Finite-amplitude trajectory turning

| Direction | max full-response turn | max interaction-direction turn |
|---|---:|---:|
| smooth-w | `0.155 deg` | `0.227 deg` |
| IDE alpha physical ray | `0.251 deg` | below morphology floor |
| IDE beta central | `0.0041 deg` | below morphology floor |
| GDM `c_s^2` | `0.0279 deg` | `0.0324 deg` |
| GDM `c_v^2` | `7.18 deg` | `12.19 deg` |
| designer `f(R)` | `12.14 deg` | `13.00 deg` |

**Boundary:** sampled direction turns are not continuous Frenet curvature; they show that one microscopic parameter can require several linear representation modes.

## Supplementary Table S5. Mechanism-localization and withheld tests

| Mechanism | Frozen coordinate/test | Result | Status boundary |
|---|---|---|---|
| thermal WDM | `k_0.1` where `ln(P_WDM/P_CDM)=-0.1` | withheld 2.5/3.5/4.0/4.5 keV masses move monotonically to higher `k_0.1`; at `z=0.295`: `8.38666, 12.19283, 14.23013, 16.47374 h/Mpc` | withheld interpolation inside represented WDM family, not universal law |
| DCDM -> dark radiation | temporal centroid `z_R` vs `Gamma/H0` | `0.6304573, 0.6343830, 0.6419613, 0.6562403`; all consecutive shifts exceed frozen `1e-3` guard | genuinely withheld mechanism for directional localization idea; not formal G8 closure |
| IDM-DR/C7 | common full-response centroid slope frozen from C3/C5 | withheld slopes `-1.3856,-0.6685,-0.2191,-0.07157` all outside frozen positive interval | prospective F27 FAIL; the specified common scalar law remains falsified |

## Supplementary Table S6. Observation-route eligibility status

| Stage | Status | Article meaning |
|---|---|---|
| Exp072A | support FAIL | current ACTxunWISE C3/C5 domain retains `0/26` coordinates at frozen 5% criterion |
| Exp073A | linear route INELIGIBLE | enlarged planning frontier is nonperturbative under tested linear/no-CLEFT route |
| Exp073L | NONNORMALIZABLE | frozen positive absolute-response measure cannot define support fraction |
| Exp073N | provenance FAIL | finite operator class lacks reproducible exact frozen Y3 real-data realization; no support statistic read |
| Exp073O | replacement FOUND | public DES Y1 pseudo-`C_ell` Wm selected prospectively under unchanged future support gate |
| Exp073P2/S0/R0 | prerequisite PASSes | checksum, mask/`n(z)`, and raw-row/HEALPix reproduction close; physical support remains unread |
| Exp073R1 | PRE-RESULT at the Paper-I scope snapshot | no PASS/FAIL inferred without a completed frozen output and explicit scope classification |

**Boundary:** no row implies covariance whitening, nuisance quotient, G7/G8/G9 closure, or survey detectability. Exact machine classifications, runs, artifacts and digests remain canonical in `OBSERVATION_ROUTE_LEDGER.md` and `PROVENANCE_MATRIX.md`.

## Supplementary-table claim boundary

The supplementary tables preserve numerical detail but do not promote descriptive, retrospective, withheld, prerequisite, or negative results into stronger claim classes. `G7=OPEN`, `G8=OPEN`, and `G9=OPEN` throughout.
