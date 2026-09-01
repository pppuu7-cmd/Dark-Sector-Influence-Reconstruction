# 2026-09-01 — Post-Exp073CC full-scale Wm_S2 memory-budget audit

## Coordination and authority

At the start of this iteration, `docs/RECOVERY_LATEST.md` and the terminal Exp073CC recovery were re-read, recent commits were inspected, and all queued/in_progress DSIR Actions runs were checked. There were zero `in_progress` runs and exactly one queued run: Exp073CA attempt3 `33448843621`, whose replica B remains self-hosted queued. Home runner remains **OFFLINE/LOCKED** and was not touched.

Scientific authority is unchanged: Exp073BJ terminal Track-A exact Wm_S1 PASS; Exp073AQ permanent historical exact-repeatability scientific FAIL; Exp073BD provisional/incomplete and forbidden downstream; Exp073BV/BW/BZ authority preserved. Article-3 readiness remains **Verified 52.0% | Draft/data 53.7%**. This audit is infrastructure-only `+0/+0`.

## Frozen production source inspected

Exp073CA attempt3 binds `ci/exp073az_article3_low_memory_general_coupling_v0_1.py` at commit `d77b7ba88801f6788f3d386e72b445c7859c7153`. In its Wm mask-PCL path it performs, in order:

`a=lens_map(...)`; `b=source_map(...)`; `fa=NmtField(a,None,spin=0)`; `fb=NmtField(b,None,spin=2)`; `aa=fa.get_mask_alms()`; `ab=fb.get_mask_alms()`; `pcl=hp.alm2cl(aa,ab,...)`.

For `NSIDE=4096`, `NPIX=201,326,592`. One float64 map is exactly 1.500 GiB. For `lmax=12287`, one packed complex128 alm is about 1.12509 GiB.

NaMaster v2.7 source confirms that an isotropic input mask is converted with `mask.astype(np.float64)` and stored as `self.mask`, so even an already-float64 input receives a separate field-owned array. Hence the simultaneous frozen lifetime has an unavoidable persistent payload of roughly:

- two caller maps: 3.000 GiB;
- two field-owned masks: 3.000 GiB;
- two mask alms: about 2.25018 GiB;

for about **8.25018 GiB before spherical-transform workspace, Python/native allocator overhead, and the WSL/Linux process baseline**. The current 6 GiB WSL RAM cap is therefore structurally incompatible with the simultaneous lifetime, independent of any exact SHT workspace estimate.

## Exp073CC-supported sequential lifetime

Exp073CC `CC_Q1_EXACT_EQUIVALENCE_PASS` established exact `np.array_equal` plus canonical `<f8` SHA equality between simultaneous and corrected one-target-at-a-time mask lifetimes for prospectively frozen hosted NSIDE 64/128/256 cases. It also showed lower peak RSS in all three hosted cases, but did not establish full-scale NSIDE=4096 safety.

A production-compatible sequential lifetime can therefore be designed prospectively as:

1. create lens map `a`;
2. construct `fa`; immediately release `a` after `fa` owns its mask;
3. compute `aa`; release `fa` while retaining `aa`;
4. create source map `b`;
5. construct `fb`; immediately release `b` after `fb` owns its mask;
6. compute `ab`; release `fb`;
7. run the unchanged `hp.alm2cl(aa,ab,...)`.

Ignoring transform workspace, the critical deterministic persistent baselines become approximately:

- field-construction peak with retained first alm: `aa 1.12509 + b 1.500 + fb.mask 1.500 = 4.12509 GiB`;
- second-SHT post-output state: `aa 1.12509 + fb.mask 1.500 + ab 1.12509 = 3.75018 GiB`.

Thus a 6 GiB cap leaves at most about **1.875 GiB** above the worst deterministic baseline for SHT workspace plus interpreter/native/OS-resident overhead. That margin is too narrow to declare full-scale safety without measurement.

## Stronger prospective spill-to-disk option

A higher-value memory-only successor design is to spill the first mask alm to immutable local storage before computing the second SHT:

1. construct lens field sequentially;
2. compute `aa`;
3. save `aa` in canonical NumPy binary form and record SHA-256;
4. release lens field and in-memory `aa`;
5. construct source field sequentially and compute `ab`;
6. reopen `aa` read-only (preferably memory-mapped if the frozen healpy call path is proven not to force a full copy);
7. require exact stored/reloaded byte SHA identity before calling the unchanged `hp.alm2cl`;
8. compare final PCL against a simultaneous/simpler oracle in prospective hosted QA using `np.array_equal` and canonical `<f8` SHA only.

This can remove the retained ~1.12509 GiB first-alm payload from the second SHT phase. Before transform workspace, that phase would then be approximately `fb.mask 1.500 + ab 1.12509 = 2.62509 GiB` plus only whatever pages of the persisted first alm are actually resident. This is materially safer for a 6 GiB cap than sequential-lifetime alone.

This spill design is **not yet authorized for production**. It needs its own prospective hosted exact-equivalence QA because `healpy.alm2cl` copy/memory-map behavior under the production package lineage has not yet been frozen and measured. No scientific arithmetic, task, thresholds, comparator, acceptance criteria, or output semantics may change.

## Tomorrow home-runner repair plan

Do not alter WSL tonight. When the user explicitly re-enables the home runner:

1. keep Exp073CA attempt3 classified infrastructure incomplete and do not revive its stale replica B as authority;
2. prospectively freeze a new infrastructure-only successor, never a post-hoc edit of CA attempt3;
3. prefer the Exp073CC-supported sequential lifetime, and consider the separately QA-proven spill-to-disk first-alm design if exact hosted QA passes;
4. preserve the frozen thread policy, scientific inputs, exact comparators, checkpoint contract, binding/trigger discipline, and <=60 s heartbeat rule;
5. instrument `/usr/bin/time -v` and phase-specific RSS/elapsed receipts so full-scale peak memory is measured rather than inferred;
6. if the run dies before complete valid comparator inputs, classify infrastructure incomplete; if complete exact mismatch occurs, preserve scientific FAIL with no rescue.

## Exact next gate

While the home runner remains OFFLINE/LOCKED, the next highest-value permitted gate is **hosted-only prospective exact-equivalence and RSS QA of first-mask-alm spill/reload**, specifically verifying that canonical saved/reloaded alm bytes are identical and that the unchanged final `hp.alm2cl` result is exactly equal to the non-spill corrected-sequential oracle. The QA must be synthetic/nonclassifying `+0/+0` and must not claim real-survey closure.
