# Exp073AC2 — factorized Layer-A synthetic QA infrastructure repair v0.2

**Frozen:** 2026-08-30 after Exp073AC run `33279797219`, job `99172915404` failed before evaluator execution with `ModuleNotFoundError: No module named 'numpy'`.

Classification of v0.1: **INFRASTRUCTURE/ENVIRONMENT FAILURE, NOT NUMERICAL OR SCIENTIFIC**.

No synthetic control executed and no real data/support output was read.

Repair rule:

- keep original preregistration `experiments/073ac_article3_factorized_layera_synthetic_v0_1_prereg.md` unchanged at commit `c5fc9e21f6def22194c713fa70cf3100f2136667`;
- keep evaluator implementation `ci/exp073ac_article3_factorized_layera_synthetic_v0_1.py` byte-for-byte unchanged at commit `e7117d54ca43390b9da0452d99f92b7776ddfcf9`;
- add only an explicit environment setup step installing NumPy before execution;
- retain all 14 frozen controls and required token `PASS_EXP073AC_FACTORIZED_LAYERA_SYNTHETIC_V0_1`;
- retain `science_gate_scored=false`, `scientific_readiness_credit=false`, readiness `52%`, G7/G8/G9 OPEN.

The repair may not alter any evaluator formula, threshold, synthetic input, expected comparison or firewall rule.
