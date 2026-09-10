# Exp073JM / Exp073JN — recovered-JL branch-neutral compatibility audit v0.1

Date: 2026-09-11. Scope: DSIR Article III downstream implementation preparation only. Effect `+0/+0`.

This audit is frozen while recovered Exp073JL retry `34544293038` is still running and before any terminal JL scientific-support verdict is known. It is deliberately branch-neutral: it neither predicts nor selects JM/NOT_CONVERGED or JN/CONVERGED.

## Authorities already fixed before this audit

Recovered Exp073JL v0.2 science is prospectively frozen on the committed canonical 2049/4097 byte streams, strict `REL_TOL=1e-3`, `h=1e-4`, native kpd20 and unchanged Exp073IR 107-row accounting. Exp073JW independently verified the exact eight-build/max-one-live canonical lifecycle. The response-blind request-plan authority fixes exact 441 coarse and 569 fine transfer calls per role, 4040 total. The recovered JL helper is separately statically audited 35/35.

These are execution/provenance facts, not a JL convergence verdict.

## JM current-helper status

Existing preregistration `EXP073JM_ARTICLE3_LAYERB_COMMON_GRID_FOURTH_REFINEMENT_CONVERGENCE_V0_1.md` remains scientifically valid and branch-conditional only on an independently verified valid JL `COMMON_GRID_THIRD_REFINEMENT_NOT_CONVERGED_PLUS_0_PLUS_0`.

The prior `EXP073JM_ACTIVATION_ALIGNMENT_AUDIT_V0_1.md` already proved one implementation defect: current `ci/exp073jm_article3_layerb_common_grid_fourth_refinement_convergence_v0_1.py` adds `retained_after_layer_b==107` and `unsupported_target_evaluations==0` as JL activation predicates even though the preregistration does not. Those quantities belong to JM's own run criteria and cannot be added to activation.

Full recovered-route audit adds two independent execution defects:

1. the helper constructs the 4097 and 8193 lattices at runtime through `jj.guarded_lattice(4096/8192)`. The coarse 4097 lattice is already canonically committed by Exp073JT; it must be consumed from that exact byte stream, not host-regenerated. The fine 8193 lattice may be canonically materialized response-blind from the already-frozen JM rule before branch activation, but may not be selected or altered using a JL/JM response;
2. the helper inherits `jj.ResolutionSuite`, which creates four CLASS objects simultaneously for each inherited suite. Under the full Exp073IR traversal this reintroduces the historical four-live architecture. A JM implementation must instead use the already-audited role-major one-live lifecycle pattern, enlarged only for the frozen 4097/8193 grids and JM's prospectively frozen infrastructure capacities 9216/262144.

Therefore current JM helper remains **NOT EXECUTION-READY** even after the earlier activation-only repair is considered. If JL NOT_CONVERGED activates JM, the allowed repair is implementation/provenance alignment only: remove the two extra activation predicates; bind the coarse lattice to the existing canonical 4097 bytes; bind the fine lattice to a response-blind canonical 8193 authority if independently established; preserve exact JM `h`, `REL_TOL`, native kpd20, estimator, interpolation, domain, masks, 107-row accounting, GL64/GL128 semantics and all JM own support criteria; use exactly eight sequential role-major CLASS lifetimes/max one live; add a no-science static regression before production.

## JN current-helper status

Existing preregistration `EXP073JN_ARTICLE3_LAYERB_SHARED_GRID_SCIENTIFIC_CLOSURE_RERUN_V0_1.md` remains scientifically valid and branch-conditional only on an independently verified valid JL `COMMON_GRID_THIRD_REFINEMENT_CONVERGED_PLUS_0_PLUS_0`.

Current `ci/exp073jn_article3_layerb_shared_grid_scientific_closure_rerun_v0_1.py` is **NOT EXECUTION-READY** for the recovered JL lineage for three independent reasons:

1. activation/provenance parsing assumes the historical authority shape `jl["observations"]["max_atomic_coarse_vs_fine_relative_component_difference"]`. The recovered JL v0.2 result contract records the frozen comparison in its `convergence` block and a future durable authority must bind that recovered artifact explicitly. JN must consume the recovered authority schema actually emitted and independently verified, not rely on an invented historical compatibility field;
2. the helper regenerates 2049/4097 through `jj.guarded_lattice(2048/4096)`. JN preregistration says to use exactly the Exp073JL lattices; those lattices are now already canonical committed byte streams under Exp073JT. JN must consume those exact canonical files and verify their text/decoded hashes rather than regenerate them on the execution host;
3. the helper assigns `jj.ResolutionSuite` directly to Exp073IR, restoring four simultaneously live CLASS models per suite and the historical 16-construction/four-live execution layout. JN must use the independently validated recovered one-live architecture: exactly four coarse + four fine model-role solver constructions, max one live, with the inherited request ordering and same-process raw operands, then replay through unchanged Exp073IR accounting.

If JL CONVERGED activates JN, the only allowed repair is an implementation/provenance alignment preserving the frozen JN scientific decision exactly. It must bind the independently verified recovered JL artifact; consume canonical 2049/4097 byte streams; reuse the response-blind 441/569 call plan and eight/max-one lifecycle; preserve `h=1e-4`, `REL_TOL=1e-3`, native kpd20, centered-cubic arithmetic, domain, masks, 107 rows, row thresholds and forbidden downstream-read checks; and undergo a no-science static audit before any fresh science-authorizing JN execution.

## Branch-neutral anti-adaptation rule

No code repair described here may depend on the numerical value or sign of the pending JL result. Only the activation wrapper differs by branch token. The recovered execution/provenance principles are common to both branches and are fixed by authorities established before the JL verdict.

JM and JN must not be launched concurrently. Only the branch selected by a terminal independently verified JL scientific-support classification can advance. `INVALID_INFRA_PLUS_0_PLUS_0` activates neither.

## Readiness boundary

This audit creates no scientific authority and does not change `ARTICLE3_REPOSITORY_READINESS=68%` or funnel-freeze readiness `=67%`.
