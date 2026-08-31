# DSIR-I observation-route eligibility ledger

**Status:** manuscript supplement candidate, 2026-08-27.

This table prevents several logically different statuses from being collapsed into a single statement such as “the observational operator passes.” Each row answers a different prerequisite question. A later PASS never rewrites an earlier FAIL.

| Stage | Frozen question | Result | What it establishes | What it does **not** establish |
|---|---|---|---|---|
| Exp072A | Does the current certified C3/C5 domain contain the ACTxunWISE kernel at `f_out<=0.05`? | **FAIL**, `0/26` retained | current-domain physical support is insufficient | no covariance/nuisance quotient may be read |
| Exp072B | Can upper-`k` extension alone repair that support? | **NO TARGET**, `0/26` finite k-only targets | the defect is not one-dimensional in support space | no extrapolation is authorized |
| Exp072C | Is there a joint lower-`z`/upper-`k` geometry satisfying the same support threshold? | **FRONTIER FOUND**, retained dimension 15 | planning geometry exists at `z_min=0.0087346`, `k_max=4.81826 Mpc^-1` | the theory providers are not certified on that domain |
| Exp073A | Is the enlarged frontier eligible under the frozen linear/no-CLEFT perturbativity route? | **INELIGIBLE**, `7/64` pairs pass `Delta^2<=1` | the tested linear route cannot support the frontier | DSIR itself is not falsified |
| Exp073B/C | Does the existing certified/public stack already provide an independent nonlinear `P_mm/P_Wm/P_WW` route? | **GAP / no complete candidate** | the projector is not the bottleneck; provider physics is missing | future nonlinear providers are not ruled out |
| Exp073D/E | Does frozen phenomenological C3 uniquely define, or admit a defensible finite ensemble of, nonlinear completions? | **NO UNIQUE COMPLETION / ensemble not feasible under frozen E1–E8** | nonlinear continuation can add model-defining assumptions | no universal nonlinear-GDM no-go theorem |
| Exp073L | Is the frozen KiDS positive absolute-response support measure normalizable? | **NONNORMALIZABLE**, `8/8` Wm + `8/8` WW | a finite positive support normalizer is itself a prerequisite | no post-hoc UV cutoff/weighting is authorized |
| Exp073M | Can a finite-positive harmonic operator class be identified prospectively? | **CANDIDATE FOUND** | a potentially usable class exists without downstream weighting | exact real-data reproducibility and physical support remain untested |
| Exp073N | Does the frozen DES Y3 candidate have a reproducible exact public real-data realization? | **PROVENANCE FAIL** | operator-class plausibility is insufficient; exact realization is mandatory | this is **not** a physical-support FAIL; no `f_invalid` was evaluated |
| Exp073O | Can a public finite real-data Wm replacement be selected prospectively without relaxing the future support gate? | **FOUND** | Cosmotheka DES Y1 redMaGiC×Metacal pseudo-`C_ell` satisfies O1–O8 | no physical support fraction/covariance/nuisance result |
| Exp073P2 | Are all frozen DES Y1 release inputs checksum-bound before support scoring? | **PASS** | exact public object identity is fixed | no mask/support/covariance conclusion by itself |
| Exp073S0 | Can the frozen redMaGiC mask and lens/source `n(z)` prerequisites be reproduced? | **PASS** | small-input operator prerequisites reproduce | no physical-support fraction or G7 result |
| Exp073R0 | Do raw catalogue rows reproduce the frozen HEALPix mapping convention? | **PASS** on `131072` sampled rows | exact required fields and pixel indices reproduce in all four source bins | artifact explicitly has `science_gate_scored=false`; this is not Exp073P support |
| Exp073R1 | Can the full one-pass weak-lensing mask construction reproduce under the already frozen contract? | **RUNNING / PRE-RESULT** in current article snapshot | preregistration and gating are preserved | no PASS/FAIL/article claim until a completed frozen result exists |

## Current logical order

```text
finite positive support measure
        ↓
exact reproducible real-data operator/input realization
        ↓
physical support eligibility on certified theory domain
        ↓
physically justified model/provider semantics
        ↓
covariance restriction and whitening
        ↓
nuisance quotient
        ↓
relation / null / detectability tests
```

The order is partly intertwined operationally—e.g. provider-domain feasibility can be diagnosed before a replacement survey operator is selected—but no downstream statistical quantity is manuscript-eligible unless every prerequisite on the realized route has passed.

## Status semantics

- **FAIL**: the frozen question was executed and failed. It remains permanently failed for that contract.
- **FOUND/CANDIDATE**: a prospectively admissible object has been identified, but its next gate is still unread.
- **PASS prerequisite**: one necessary reproduction/eligibility layer is closed; this does not imply later layers.
- **INCOMPLETE infrastructure**: execution did not reach the frozen science question and has no physical interpretation.
- **PRE-RESULT**: preregistered/implemented/possibly running, but no completed frozen output is used by the paper.

## Non-negotiable article boundary

As of this snapshot, the replacement DES/BOSS route has **not** produced a physical-support result, covariance-whitened distance, nuisance-quotiented distance, G7 relation, G8 withheld validation, or G9 dynamics reconstruction. Therefore `G7=OPEN`, `G8=OPEN`, `G9=OPEN`.
