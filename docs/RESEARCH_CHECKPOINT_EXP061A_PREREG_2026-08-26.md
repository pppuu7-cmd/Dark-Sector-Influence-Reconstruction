# DSIR recovery checkpoint — Exp061A preregistration

Date: 2026-08-26

Current main after merging Exp060A: `c552e40ad4455d4e2fd3701bd840f05b278de10e`.

The next legal scientific action is Exp061A: generate the first C9 IDM–baryon matter-power response and evaluate the already frozen Exp058A/Exp060A `(ell,q)` path gate. C9 was source-only frozen in Exp059A; Exp060A passed workflow run 32947173401 with no C9 response contamination.

Frozen C9 grid: `cross_idm_b={1e-30,1e-29,1e-28,1e-27,1e-26} cm^2`, `n_index_idm_b=0`, `m_idm=1e9 eV`. Frozen response nodes: k=`[0.001,0.003,0.01,0.03,0.1] h/Mpc`; z=`[0.295,0.51,0.706,0.934,1.317,1.491,2.33]`. Exact operator: Exp060A training-only PC2/sign/standardization, step tolerance `1e-10`, intersection tolerance `1e-10`, full plus all seven leave-one-redshift rebuilds.

Do not modify any scientific threshold, coordinate, sign, k/z domain, C9 coupling, model order, or leave-one-z semantics after first C9 response. Preserve scientific FAIL exactly if obtained. Infrastructure success is distinct from scientific PASS.

Current scientific state before C9 unblinding: F27 HARD FAIL; F28 retrospective only; F29 HARD PROSPECTIVE FAIL; G7 OPEN; G8 OPEN; G9 OPEN.
