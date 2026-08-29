#!/usr/bin/env python3
from __future__ import annotations
import json, math

K_MAX=0.06664762008318016
THRESH=0.05


def operator_invalid(ks, ws):
    if len(ks)!=len(ws) or not ks:
        raise ValueError("bad support atoms")
    if any((not math.isfinite(k)) or (not math.isfinite(w)) or w<0 for k,w in zip(ks,ws)):
        raise ValueError("nonfinite/negative support atom")
    den=sum(ws)
    if den<=0:
        raise ValueError("nonpositive envelope normalization")
    return sum(w for k,w in zip(ks,ws) if not (0.0 < k <= K_MAX))/den


def weighted_mean_k(ks,ws):
    return sum(k*w for k,w in zip(ks,ws))/sum(ws)


def layerb_envelope_valid(values):
    return bool(values) and all(math.isfinite(x) and x>0.0 for x in values)


def main():
    ks=[0.04,0.10]
    wsA=[0.90,0.10]
    fA=operator_invalid(ks,wsA)
    kA=weighted_mean_k(ks,wsA)
    pointA=(0.0<kA<=K_MAX) and layerb_envelope_valid([1.0,2.0])
    testA=(fA>THRESH and pointA)

    wsB=[0.95,0.05]
    fB=operator_invalid(ks,wsB)
    testB=(fB==0.05 and fB<=THRESH)

    ksC=[0.02,0.04]
    wsC=[0.4,0.6]
    fC=operator_invalid(ksC,wsC)
    opC=fC<=THRESH
    layerbC=layerb_envelope_valid([1.0,0.0])
    testC=(opC and not layerbC)

    tests={
        "A_point_pass_does_not_imply_operator_pass":{
            "pass":testA,"operator_f_invalid":fA,"naive_weighted_mean_k":kA,
            "operator_pass":fA<=THRESH,"point_geometry_envelope_pass":pointA,
        },
        "B_operator_exact_0p05_boundary_passes":{
            "pass":testB,"operator_f_invalid":fB,"operator_pass":fB<=THRESH,
        },
        "C_operator_pass_does_not_imply_layerb_envelope_pass":{
            "pass":testC,"operator_f_invalid":fC,"operator_pass":opC,
            "layerb_response_vector":[1.0,0.0],"layerb_envelope_pass":layerbC,
        },
    }
    if not all(v["pass"] for v in tests.values()):
        raise AssertionError(tests)
    result={
        "status":"PASS_ARTICLE3_DUAL_SUPPORT_NON_EQUIVALENCE_SYNTHETIC_V0_1",
        "scope":"SYNTHETIC_ONLY_NO_REAL_SURVEY_DATA",
        "scientific_credit":False,
        "constants":{"k_max_Mpc^-1":K_MAX,"max_invalid_fraction":THRESH},
        "conclusions":[
            "point-coordinate PASS does not imply broad operator-support PASS",
            "broad operator-support PASS does not imply Layer-B common-response-envelope PASS",
        ],
        "tests":tests,
        "gate_state":{"G7":"OPEN","G8":"OPEN","G9":"OPEN"},
        "downstream_authorized":False,
    }
    print(json.dumps(result,indent=2,sort_keys=True))

if __name__=="__main__":
    main()
