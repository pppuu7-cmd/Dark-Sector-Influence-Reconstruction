# DSIR Exp073R1 v0.5 live authority and G7 gate-order audit

Date: 2026-08-28 21:18 MSK
Branch audited: `main`
Main SHA at audit start: `a3cc148faecd2b03a6c94b7df4129038a565c11b`
Canonical run: https://github.com/pppuu7-cmd/Dark-Sector-Influence-Reconstruction/actions/runs/33175886694

## Live state

- Workflow: `Exp073R1 DESY1 sequential whole-stream reconstruction v0.5`.
- Run status at audit: `in_progress`.
- `source-index`: terminal `success`.
- `metacal-map`: `in_progress`.
- Current step: `Sequentially stream authoritative metacal object and execute frozen mapper`.
- No duplicate Exp073R1 heavy run was launched in this iteration.

## Stage-A verified state

The terminal Stage-A job passed all frozen no-Range identity checks:

- whole-object GET only; zero HTTP Range requests;
- identity content encoding;
- exact source byte count `2738626560`;
- frozen source SHA256 `491f623d9370d3e5657db67d410e7cfd0e89475827046e6cd82ef6b3dd88c7a5`;
- exact source row count `136930995`;
- row-aligned source index produced;
- no science selection applied at Stage A;
- no `f_invalid`, covariance, or G8 evaluation performed.

## Authority / immutability audit

The current v0.5 workflow still binds the immutable Exp073R0 parent run `33103083736`, requires that run to be terminal success, pins its workflow path and head SHA, and then requires the frozen R0 artifact before mapping.

The true Exp073R1 PASS assertion remains downstream of the full metacal whole-stream mapper and requires simultaneously:

- status `PASS_DESY1_FULL_ONEPASS_WEAK_LENSING_MASK_EXP073R1`;
- whole-object GET only and zero Range requests;
- exact metacal byte count `84075649920`;
- frozen metacal SHA256 `39a7fe03e54d96b85cee2fb523ea108c2a548ba1584368203f0464ed6241ebc8`;
- source identity binding to the frozen source SHA256;
- equal source-index/metacal row counts `136930995`;
- frozen selection `zbin_mcal == t AND dec >= -90 AND dec <= -35 AND flags_select == 0`;
- frozen HEALPix mapper `nside=4096`, `RING`, celestial coordinates, `lonlat=True`;
- zero out-of-range pixels;
- non-empty selected rows in all four bins;
- parent R0 checks all true;
- no science gate scoring, no `f_invalid`, no covariance, and no G8 read inside R1.

No frozen acceptance criterion was changed in this iteration.

## Scientific classification

Current state is **reproduction/infrastructure INCOMPLETE**, not scientific FAIL and not scientific PASS.

Stage-A success is an input-identity/reproducibility PASS only. It is insufficient to open the physical support-validity mask.

## Frozen downstream order

Do not dispatch or score downstream G7 stages until a genuine terminal Exp073R1 PASS exists.

Required order remains:

1. validated physical forward/power-input bridges;
2. genuine Exp073R1 reproduction PASS;
3. preregistered physical support-validity mask;
4. covariance restriction/whitening on that frozen mask;
5. nuisance tangent rank/SVD;
6. quotient/relation/null control;
7. only then fresh G8 withheld family.

Negative results at any scientific stage must be retained as scientific results. Transport, timeout, runner, download, or orchestration failures must remain classified as infrastructure failures unless a frozen scientific criterion was actually evaluated and failed.

## Next action

Keep run `33175886694` as the sole authoritative heavy Exp073R1 execution. On terminal completion, inspect the terminal assertion and artifact provenance before allowing any downstream dispatch. If it terminates for infrastructure reasons before the frozen R1 assertion is evaluated, do not label it scientific FAIL and do not silently relax or revise the acceptance criteria.
