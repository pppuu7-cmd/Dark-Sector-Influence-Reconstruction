#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

EXPECTED = {
    "JJ": ("COMMON_GRID_RESOLUTION_REFINEMENT_NOT_CONVERGED_PLUS_0_PLUS_0", 0.037280144773915974),
    "JK": ("COMMON_GRID_SECOND_REFINEMENT_NOT_CONVERGED_PLUS_0_PLUS_0", 0.016330535730270664),
    "JL": ("COMMON_GRID_THIRD_REFINEMENT_NOT_CONVERGED_PLUS_0_PLUS_0", 0.012273497268380687),
    "JM": ("COMMON_GRID_FOURTH_REFINEMENT_NOT_CONVERGED_PLUS_0_PLUS_0", 0.01070806986822778),
}
REL_TOL = 1e-3


def aitken(x0: float, x1: float, x2: float) -> float | None:
    den = x2 - 2.0*x1 + x0
    if den == 0.0 or not math.isfinite(den):
        return None
    y = x0 - (x1-x0)**2/den
    return y if math.isfinite(y) else None


def main() -> int:
    ap=argparse.ArgumentParser()
    for k in ("jj","jk","jl","jm","out"):
        ap.add_argument("--"+k,required=True)
    a=ap.parse_args()
    paths={k.upper():Path(getattr(a,k)) for k in ("jj","jk","jl","jm")}
    vals=[]
    source={}
    for key in ("JJ","JK","JL","JM"):
        d=json.loads(paths[key].read_text())
        cls,exp=EXPECTED[key]
        if d.get("classification") != cls or d.get("artifact_verified_independently") is not True:
            raise RuntimeError(f"{key} authority mismatch")
        if key in ("JJ","JK"):
            v=float(d["observations"]["max_atomic_coarse_vs_fine_relative_component_difference"])
        elif key=="JL":
            v=float(d["observations"]["max_atomic_coarse_vs_fine_relative_component_difference"])
        else:
            v=float(d["convergence"]["max_relative_component_difference"])
        if v != exp:
            raise RuntimeError(f"{key} maximum mismatch {v} != {exp}")
        vals.append(v)
        source[key]={"classification":cls,"max_relative_component_difference":v}

    ratios=[vals[i-1]/vals[i] for i in range(1,len(vals))]
    effective_orders=[math.log(r,2.0) for r in ratios]
    aitken_jj_jk_jl=aitken(*vals[:3])
    aitken_jk_jl_jm=aitken(*vals[1:])
    monotone=all(vals[i] < vals[i-1] for i in range(1,len(vals)))
    reduction_factors_decreasing=all(ratios[i] < ratios[i-1] for i in range(1,len(ratios)))
    orders_decreasing=all(effective_orders[i] < effective_orders[i-1] for i in range(1,len(effective_orders)))

    out={
      "schema":"LAYERB_REFINEMENT_SEQUENCE_DESCRIPTIVE_AUDIT_RESULT_V0_1",
      "classification":"LAYERB_REFINEMENT_SEQUENCE_DESCRIPTIVE_AUDIT_PASS_PLUS_0_PLUS_0",
      "effect":"+0/+0",
      "source":source,
      "sequence":vals,
      "strict_rel_tol":REL_TOL,
      "threshold_ratios":[v/REL_TOL for v in vals],
      "successive_reduction_factors":ratios,
      "effective_orders_if_zero_limit_assumed":effective_orders,
      "monotonically_decreasing":monotone,
      "successive_reduction_factors_decreasing":reduction_factors_decreasing,
      "effective_orders_decreasing":orders_decreasing,
      "aitken_estimate_JJ_JK_JL":aitken_jj_jk_jl,
      "aitken_estimate_JK_JL_JM":aitken_jk_jl_jm,
      "latest_aitken_over_threshold_factor":None if aitken_jk_jl_jm is None else aitken_jk_jl_jm/REL_TOL,
      "interpretation_only":"Observed maxima decrease monotonically, but the reduction factor weakens strongly across successive doublings. The latest three-point Aitken estimate is descriptive evidence consistent with a nonzero numerical plateau; it is not a scientific classifier and must not alter the preregistered refinement ladder or tolerance.",
      "stopping_rule_changed":False,
      "next_rung_changed":False,
      "scientific_authority_created":False,
      "covariance_restriction_authorized":False,
      "Wm_S3_opened":False,
      "article3_repository_readiness_percent":68,
      "funnel_freeze_readiness_percent":67,
      "token":"LAYERB_REFINEMENT_SEQUENCE_DESCRIPTIVE_AUDIT_PASS_PLUS_0_PLUS_0"
    }
    Path(a.out).parent.mkdir(parents=True,exist_ok=True)
    Path(a.out).write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
    print(out["token"])
    print(json.dumps(out,sort_keys=True))
    return 0

if __name__=="__main__":
    raise SystemExit(main())
