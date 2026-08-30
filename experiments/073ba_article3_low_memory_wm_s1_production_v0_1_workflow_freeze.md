# Exp073BA workflow freeze — low-memory Wm_S1 production v0.1

Prospectively frozen before Exp073AZ Wm_S1 PCL result was known.

- preregistration: `experiments/073ba_article3_low_memory_wm_s1_production_v0_1_prereg.md`
- preregistration commit: `b445066a36c838b18e4cea2ca56f2f6abee56406`
- low-memory implementation: `ci/exp073az_article3_low_memory_general_coupling_v0_1.py`
- implementation commit: `d77b7ba88801f6788f3d386e72b445c7859c7153`
- exact BA comparator: `ci/exp073ba_compare_low_memory_wm_s1_v0_1.py`
- comparator commit: `a0b5bd8065c590e20c648215b8d993452fb7339c`
- workflow: `.github/workflows/exp073ba-article3-low-memory-wm-s1-production-v0-1.yml`
- workflow_last_modifying_commit: `fc0ca8b4c0e31673c1470418060a95ac507b3759`

Execution remains forbidden until a valid Exp073AZ exact mask-PCL PASS exists and a separate immutable AZ binding receipt is committed. Adding that receipt does not alter this workflow and does not trigger it.

The frozen production sequence is:

1. two independent compact Wm_S1 replicas from the same admitted canonical AZ PCL;
2. exact compact SHA/`array_equal` comparator;
3. if and only if compact PASS, two fresh finalizer jobs on the admitted compact authority;
4. exact selected-window comparator;
5. final task authority only on exact final PASS.

No tolerance, ULP, rounding, majority-vote, preferred replica or AQ-value targeting is permitted. Exp073AQ remains permanent FAIL. Wm_S2 remains blocked until a valid Exp073BA final PASS. Readiness remains 52%, +0 for this task.
