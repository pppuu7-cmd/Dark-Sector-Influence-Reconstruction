# Exp073AJ2 — narrow repair of Exp073AJ environment-provenance classifier v0.2

Frozen 2026-08-30 after hosted Exp073AJ run `33313517040` failed inside the synthetic self-test with `TypeError: unhashable type: 'dict'`, before any real Exp073AI receipt or numerical result was read.

Classification of AJ v0.1: `IMPLEMENTATION_FAILURE_UNHASHABLE_DICT_BEFORE_CLASSIFICATION_NOT_SCIENCE`.

AJ2 preserves the entire scientific/provenance contract and classifier labels from `experiments/073aj_article3_ai_environment_provenance_classifier_v0_1_prereg.md`. The only permitted implementation repair is to serialize resource SHA256 diagnostics under stable string replica keys `A` and `B` rather than attempting to use receipt dictionaries as Python dictionary keys.

No threshold, environment field, classifier branch, accounting rule, anti-leakage firewall, production authority, or numerical criterion may change. AJ2 remains synthetic/non-scientific and contributes +0 readiness.

Required token: `PASS_EXP073AJ2_AI_ENVIRONMENT_PROVENANCE_CLASSIFIER_SYNTHETIC_V0_2`.
