# Exp073BT — Article-3 NaMaster-2.7 Wigner linkage BJ-environment successor v0.3 — preregistration

**Project:** DSIR only. **Classification:** NONCLASSIFYING infrastructure/source-linkage diagnostic. **Accounting:** `+0/+0` for every outcome.

Frozen prospectively on 2026-09-03 after Exp073BT v0.2 run `33794333883` stopped at hosted `static-audit` job `100778260261`; the diagnostic job was skipped. The first causal failure is an audit-only false positive: the audit searched the entire workflow text for the malformed v0.1 command string, but that exact string occurred inside the audit's own forbidden-string assertion. The repaired diagnostic block itself was not executed and no BT scientific/source-linkage outcome was produced.

## Preserved state

- Exp073BJ Track-A exact PASS remains unchanged.
- Exp073AQ scientific FAIL remains unchanged.
- Exp073BS, Exp073BT v0.1 and Exp073BT v0.2 remain historical infrastructure/source-linkage incomplete `+0/+0` results.
- Inherited diagnostic remains exactly `ci/exp073br_namaster27_wigner_linkage_failure_capturing_v0_1.py` at `8a70892c9533206e4011eee041914ca89bae2290`.
- v0.1 preregistration: `07c17496597306ff410633264d1d050f833728b9`.
- v0.2 preregistration: `be0b8829cec0987ae98fa8ae7c001b4dc4784d5d`.
- v0.2 workflow implementation commit: `6f1d33b8c26f7717acabb5b19170a4915573300c`.

## Sole allowed v0.3 repair

Keep the v0.2 diagnostic job, environment, command block, receipt conversion and firewalls unchanged. Change only the hosted static audit so it verifies the required valid diagnostic block positively and does not embed/search the malformed v0.1 scalar as a raw self-referential substring.

The audit must still fail closed on immutable lineage and require:

```yaml
run: |
  "${NMT_PY}" ci/exp073br_namaster27_wigner_linkage_failure_capturing_v0_1.py
```

It must also require `ubuntu-24.04`, the exact conda-forge Python 3.11 / NaMaster 2.7 environment command, `needs: static-audit`, and all `+0/+0` authority firewalls. The diagnostic job may run only after this audit passes.

## Frozen interpretation and firewalls

Allowed statuses remain exactly `BT_Q1_EXTENSION_EXPORTS_DRC3JJ`, `BT_Q2_LINKED_DEPENDENCY_EXPORTS_DRC3JJ`, `BT_Q3_DYNAMIC_SYMBOL_ABSENT_SOURCE_REFERENCE_FOUND`, `BT_Q4_DYNAMIC_SYMBOL_AND_INSTALLED_SOURCE_REFERENCE_ABSENT`, or `BT_Q5_PARTIAL_DIAGNOSTIC_INCOMPLETE`, with the v0.1 frozen meanings.

Every outcome remains non-authoritative for Wm_S2, Wm_S3, WW, Layer-A/B, covariance/whitening, G7/G8 and new physics; `scientific_readiness_increment=0`, `draft_data_readiness_increment=0`. No tolerance/rounding/averaging/rescue; no home runner; no effect on the fresh-independent-PCL Wm_S3 A/B frontier.

**Readiness remains:** `Verified 52.0% | Draft/data 54.6%`.
