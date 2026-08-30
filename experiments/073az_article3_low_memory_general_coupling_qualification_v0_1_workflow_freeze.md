# Exp073AZ workflow freeze — low-memory general-coupling qualification v0.1

This file freezes the first hosted qualification step of the prospectively preregistered Exp073AZ authority succession.

- preregistration: `experiments/073az_article3_low_memory_general_coupling_authority_v0_1_prereg.md`
- preregistration commit: `279e09696263432def4ce20c15752b4832bba298`
- implementation: `ci/exp073az_article3_low_memory_general_coupling_v0_1.py`
- implementation commit: `d77b7ba88801f6788f3d386e72b445c7859c7153`
- workflow: `.github/workflows/exp073az-article3-low-memory-general-coupling-qualification-v0-1.yml`
- workflow_last_modifying_commit: `7ba874e48a7c3e6509d114745a301e63a06229a2`

Frozen hosted qualification scope:

1. nonclassifying small-resolution algebraic self-test;
2. two independent real DES-Y1 `Wm_S1` mask-PCL replicas at `NSIDE=4096`;
3. exact `<f8 [12288]` SHA and `numpy.array_equal` comparison;
4. canonical PCL emitted only if the two replicas are bitwise identical;
5. no low-memory Wm_S1 coupling authority is produced by this workflow yet;
6. Exp073AQ remains permanent hosted repeatability FAIL;
7. Wm_S2 remains blocked;
8. strict Article-3 readiness remains 52%, +0 for this workflow.

No tolerance/ULP/rounding equivalence is authorized. A PCL mismatch is preserved as `SCIENTIFIC_REPEATABILITY_FAIL_EXP073AZ_WM_S1_MASK_PCL_EXACT_V0_1`; a failure before comparison is infrastructure-INCOMPLETE.
