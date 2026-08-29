# Exp073T — pinned Cosmotheka observation inventory and NaMaster component order v0.1 — preregistration

**Frozen:** 2026-08-29, before Exp073T implementation and before any Exp073T output.

## Purpose

Prospectively resolve the exact pre-support DES-Y1 Wm/WW scalar-coordinate inventory and the spin-component ordering needed by the future Article-3 finite observation operator. This is metadata/API QA only. It does not inspect physical-support fractions, real covariance values, nuisance geometry, G7, G8 or G9.

## Immutable Cosmotheka lineage

Bind exact upstream commit:

`Cosmotheka/Cosmotheka@7bde066626f66cd7bbe79cc46224d2342840e463`.

Bind the following files/blobs from that commit:

- `input/DESY1_eBOSS_P18CMBK.yml` blob `dd26bc74067bbe6da8274c60afcb2e6971e9c1f1`;
- `environment.yml` blob `e438a6c12697d92ba3a761cc5327ccd3f28f183b`;
- `cosmotheka/cls/data.py` blob `88827346e4c906359413efdb374fee7a369100cf`;
- `cosmotheka/cls/cl.py` blob `9767e6256f7e57c309f5d177c2bb20142842dd47`;
- `cosmotheka/mappers/mapper_DESY1wl.py` blob `d0b466f3cc740c5ef025d8029f0fb5340d0d58db`;
- `cosmotheka/mappers/utils.py` blob `0f7d104422ed3c7c9b8e5962faa2968d36aa9aec`.

The pinned environment requires `namaster=2.7`.

## Frozen external component convention

Before this execution, the published NaMaster mathematical vectorization and documentation establish:

- spin-0 × spin-2 spectrum order: `[TE, TB]`;
- spin-2 × spin-2 spectrum order: `[EE, EB, BE, BB]`.

For DSIR's scalar E-mode observation inventory, freeze:

- Wm uses component index `0` (`TE`, here scalar-density × shear-E);
- WW uses component index `0` (`EE`);
- TB/EB/BE/BB are not silently concatenated into the Article-3 scalar response vector. They remain diagnostics/null channels unless separately preregistered.

A dedicated NaMaster-2.7 synthetic runner must independently verify this package behavior. If the runtime package contradicts the frozen convention, the result is an API/lineage invalid state, not a science FAIL.

## Static inventory rules

From the exact pinned configuration and exact `Data.get_cl_trs_names()` ordering logic:

1. identify DES lens tracers `DESgc__0..4` and source tracers `DESwl__0..3` from the configuration;
2. require `DESgc-DESwl: compute=all` and `DESwl-DESwl: compute=all`;
3. preserve the tracer definition order from the YAML and the upper-triangular/non-inverted unique-pair rule from pinned `data.py`;
4. require exactly 40 bandpower edges and therefore 39 bandpowers;
5. build canonical Wm pair order from every lens-source pair admitted by pinned ordering;
6. build canonical WW pair order from every upper-triangular source-source pair admitted by pinned ordering;
7. assign one scalar E-mode coordinate per pair per bandpower in bandpower-index order.

Prospectively expected counts from those fixed combinatorics are:

- Wm pairs: `5*4 = 20`;
- WW pairs: `4*5/2 = 10`;
- bandpowers per pair: `39`;
- Wm scalar E coordinates: `780`;
- WW scalar EE coordinates: `390`;
- DES Wm+WW scalar coordinates before physical-support filtering: `1170`.

The already frozen BOSS Exp073J component has 240 mm coordinates, but Exp073T must not combine them into a final Article-3 retained vector or score support. The arithmetic `1170+240=1410` may be reported only as a pre-support inventory identity, not as a retained dimension.

## Independent jobs

Run at least two independent GitHub-hosted jobs:

- `static-inventory`: audits the pinned Cosmotheka source/config lineage and emits the exact canonical Wm/WW pair and coordinate order;
- `namaster-2p7-component-order`: installs exact NaMaster 2.7 lineage and uses deterministic synthetic spin-0/spin-2 fields to verify the expected output component ordering.

Neither job consumes Exp073S outputs or the other job's output.

## PASS tokens

- static: `PASS_EXP073T_PINNED_COSMOTHEKA_INVENTORY_V0_1`;
- component runtime: `PASS_EXP073T_NAMASTER_2P7_COMPONENT_ORDER_V0_1`.

The Exp073T package is complete only if both independent jobs pass. Installation/network failure is INCOMPLETE. Upstream blob/config/API mismatch is INVALID_FOR_OBSERVATION_INVENTORY. Neither is evidence for or against dark-sector physics.

## Firewall

Every output must preserve:

- `physical_support_evaluated=false`;
- `science_gate_scored=false`;
- `covariance_read=false`;
- `nuisance_geometry_read=false`;
- `G8_read=false`;
- `G7/G8/G9=OPEN`.
