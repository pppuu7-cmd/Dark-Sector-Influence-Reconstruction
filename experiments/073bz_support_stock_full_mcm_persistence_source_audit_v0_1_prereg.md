# Exp073BZ v0.1 — NaMaster 2.7 stock full-MCM construction/persistence source audit

Date frozen: 2026-09-04
Scope: DSIR only; hosted/static support audit; accounting always `+0/+0`.

## Purpose
After Exp073BY M1 established exact file-backed downstream consumption of a serialized complete MCM without a second full-MCM heap/read copy, identify the exact NaMaster 2.7 source/lifecycle route for construction, retention and persistence of the spherical workspace full unbinned MCM. This audit is source-only and cannot create Wm_S3 authority.

## Frozen upstream lineage
Repository: `LSSTDESC/NaMaster`
Tag/version: `v2.7`
Exact commit: `24365fa59a38c15732f4f37e8b29265b75c442d5`.

## Questions
1. Where and how is the spherical full unbinned coupling matrix allocated and retained in the workspace?
2. Which stock function(s) serialize/write the workspace or MCM, and do they operate directly on the workspace-owned full MCM rather than first materializing a second complete contiguous `ncls*lmax^2` array?
3. Does the public Python persistence route call the direct stock writer, or require `get_coupling_matrix()` / another full Python copy first?
4. At what point can the workspace-owned full MCM be freed after durable persistence, while preserving the exact downstream operation order established by Exp073BX/Exp073BY?

## Frozen outcomes
- `P1_DIRECT_STOCK_PERSISTENCE_WITHOUT_SECOND_FULL_MCM_COPY_IDENTIFIED`: exact source proves a direct stock write/persistence route from workspace-owned full MCM without another complete full-MCM materialization.
- `P2_STOCK_PERSISTENCE_REQUIRES_SECOND_FULL_MCM_COPY`: exact source proves persistence necessarily materializes another complete full MCM before durable write.
- `P3_SOURCE_LIFECYCLE_AMBIGUOUS`: source evidence is insufficient to decide P1/P2; no implementation authorization.
- `P4_SOURCE_LINEAGE_MISMATCH`: exact v2.7 commit/source identity cannot be verified.
- `P5_INFRASTRUCTURE_INCOMPLETE`: audit fails before a valid source classification.

## Acceptance discipline
Workflow success alone is not P1/P2/P3. The raw audit receipt must include exact upstream commit, paths/functions inspected, allocation/persistence evidence, and one frozen status. No numerical DES/historical data may be read. No scientific gate is scored.

## Consequence
P1 permits a later prospective synthetic/runtime QA of direct workspace persistence + mmap downstream exact equivalence. P2 permits only prospective design of an exact streaming/direct-write construction path that preserves stock arithmetic. P3 requires a narrower source/runtime diagnostic. P4/P5 require causal repair only. Exp073BU remains NOT ACTIVATED until a complete DES-scale exact full-stock memory architecture is prospectively validated.
