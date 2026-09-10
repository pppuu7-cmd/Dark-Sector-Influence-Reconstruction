# Pinned CLASS-IV C2 instance-locality source audit v0.1

Date: 2026-09-11. Scope: DSIR Article III process/support only. Effect `+0/+0`.

This audit was completed after Exp073JR v0.2 produced no fine numerical receipts because all four 4097-node four-live jobs were externally terminated during the numerical step. It does not reinterpret those process failures as numerical results and does not change any Exp073JL scientific rule.

## Bound source and configuration

- pinned CLASS-IV commit: `ac627d54e9ce196a08878d1ba33999819925d19c`;
- frozen baseline: `configs/dsir4/c2/ide0_reference_v0_1.ini`;
- frozen precision: `configs/dsir4/c2/dsir_ide_p8_v0_1.pre`;
- four finite-difference roles remain `(0,0),(-1e-4,0),(0,+1e-4),(0,-1e-4)`.

## Per-instance Python/C ownership

In pinned `python/classy.pyx`, `cdef class Class` owns the major solver structures as fields of each Python object (`precision`, `background`, `thermo`, `perturbs`, `primordial`, `nonlinear`, `transfers`, `spectra`, `lensing`, `output`, and parser/file-content state). `compute()` passes pointers to those object fields into the C modules, e.g. `&self.pr`, `&self.ba`, `&self.pt`, `&self.tr`; cleanup likewise operates on that object's structures. This is direct source evidence that the intended solver state is instance-owned rather than a single shared cosmology object.

## Identified file-scope exception and activation check

Pinned `include/background.h` declares a file-scope mutable pointer:

```c
gsl_integration_romberg_workspace * work_rom;
```

Pinned `source/background.c` allocates, uses and frees this pointer only under `pba->fluid_equation_of_state == IDM_IV`.

The frozen DSIR C2 baseline does **not** provide a `fluid_equation_of_state` input. Pinned `input_default_params()` sets `pba->fluid_equation_of_state = CLP`. The parser changes this enum to `IDM_IV` only if the explicit `fluid_equation_of_state` string contains `IDM_IV`/`idm_iv`.

The frozen `f_idm_iv=1` and `f_iv=1` inputs do activate nonzero interacting-DM/interacting-vacuum densities: `f_idm_iv` moves a fraction of CDM into `Omega0_idm_iv`, and `f_iv` moves a fraction of lambda into `Omega0_iv`. Those density assignments do not themselves assign `fluid_equation_of_state=IDM_IV`. Therefore the identified global Romberg workspace branch is inactive on the frozen C2 path.

This is deliberately a narrow conclusion. The global pointer is a real general reentrancy concern for explicit `fluid_equation_of_state=IDM_IV` configurations, but it is not evidence for the DSIR C2 runner shutdowns and is not used as a scientific argument.

## Dynamic evidence already available

- Exp073JR v0.1 coarse-2049 dynamically showed exact equality between the original four-live response engine and the one-live sequential engine for both frozen sample requests; max difference was exactly 0.0.
- Exp073JQ on the fine-4097 lattice showed exact same-run equality for repeated fresh instances and for a pre-query/history instance for all four model roles; max differences were exactly 0.0.
- Repeated fine-4097 four-live JR attempts were externally terminated before any equality receipt, so absence of a fine four-live receipt cannot be promoted either to exact equivalence or to numerical inequality.

## Remaining proof obligation

Source ownership plus the inactive identified workspace exception supports, but does not alone authorize, the one-live full JL execution. A prospective dynamic fine-4097 solver-isolation gate is still required. It must test whether lifecycle execution of the other FD models leaves the selected model's later fresh result bitwise unchanged while never holding more than one CLASS instance live. This directly tests residual cross-model global-state contamination under the resource-feasible execution architecture.

Only after that dynamic gate passes for all four model roles may a separate authority decide whether the accumulated coarse exact proof + fine same-run repeat/history proof + fine cross-model lifecycle-isolation proof are sufficient to authorize a prospectively frozen sequential one-live recovered JL. No tolerance or approximate equality is allowed.