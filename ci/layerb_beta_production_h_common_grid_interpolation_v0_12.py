#!/usr/bin/env python3
from __future__ import annotations
import argparse, importlib.util, json, math, struct
from pathlib import Path
import numpy as np

def load(name, path):
    spec = importlib.util.spec_from_file_location(name, Path(path))
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import {path}")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m

def f64(h):
    return struct.unpack(">d", bytes.fromhex(h))[0]

def rel(a, b):
    return abs(a-b)/max(abs(a), abs(b), np.finfo(np.float64).tiny)

def extract(jj, c, requested, z):
    tk = c.get_transfer(z=float(z), output_format="class")
    dm = [q for q in tk if q.strip() == "d_m"]
    if len(dm) != 1:
        raise RuntimeError("exact d_m key missing")
    kkey = None; scale = None
    for q in tk:
        s = q.lower().replace(" ","")
        if s in {"k(h/mpc)","k[h/mpc]","k_h/mpc"} or ("k" in s and "h/mpc" in s):
            kkey=q; scale=float(c.h()); break
        if s in {"k(1/mpc)","k[1/mpc]"} or ("k" in s and "1/mpc" in s):
            kkey=q; scale=1.0; break
    if kkey is None:
        raise RuntimeError("unrecognized CLASS k key")
    k=np.asarray(tk[kkey],dtype=np.float64)*scale
    y=np.asarray(tk[dm[0]],dtype=np.float64)
    vals,mx=jj.requested_values(k,y,np.asarray(requested,dtype=np.float64))
    return np.asarray(vals,dtype=np.float64),float(mx),str(kkey)

def domain_mode(a,C):
    if a.grid not in C["grids"]:
        raise RuntimeError("unknown frozen grid")
    jj=load("jj",a.jj_script)
    if jj.H != C["production_h"] or jj.REL_TOL != C["relative_tolerance"] or jj.NATIVE_KPD != C["native_k_per_decade_for_pk"]:
        raise RuntimeError("frozen response constants mismatch")
    base_n=int(C["grids"][a.grid]["base_n"])
    common,ratio,nlo,nhi=jj.guarded_lattice(base_n)
    exp=C["grids"][a.grid]
    if [nlo,nhi,len(common)] != [exp["lower_guard_count"],exp["upper_guard_count"],exp["requested_node_count"]]:
        raise RuntimeError("guarded lattice mismatch")
    targets=[dict(x) for x in C["audit_targets"]]
    target_ks=np.asarray(sorted(set(f64(x["k"]) for x in targets)),dtype=np.float64)
    mixed=np.asarray(sorted(set(float(x) for x in common).union(float(x) for x in target_ks)),dtype=np.float64)
    expected_added=sum(1 for k in target_ks if not np.any(np.isclose(common,k,rtol=0.0,atol=0.0)))
    if len(mixed) != len(common)+expected_added:
        raise RuntimeError("mixed node count mismatch")
    hs=[float(x) for x in C["audit_h_values"]]
    from classy import Class
    cells=[]; max_lookup=0.0; kkeys=set(); solver_count=0; node_shift_max=0.0
    for h in hs:
        pure={}; mix={}
        try:
            for label,beta in [("plus",h),("minus",-h)]:
                for nodes,store in [(common,pure),(mixed,mix)]:
                    p=jj.class_params(Path(a.baseline),Path(a.precision),0.0,beta,nodes)
                    p["tol_perturb_integration"]=C["tol300_override"]
                    c=Class(); c.set(p); c.compute(["transfer"]); store[label]=c; solver_count += 1
            for t in targets:
                z=f64(t["z"]); k=f64(t["k"]); sign_data={}
                for label in ["plus","minus"]:
                    yp,m1,k1=extract(jj,pure[label],common,z)
                    ym,m2,k2=extract(jj,mix[label],common,z)
                    ye,m3,k3=extract(jj,mix[label],[k],z)
                    ip,vp=jj.cubic_centered(common,yp,np.asarray([k],dtype=np.float64))
                    im,vm=jj.cubic_centered(common,ym,np.asarray([k],dtype=np.float64))
                    if not bool(vp[0]) or not bool(vm[0]):
                        raise RuntimeError("unsupported frozen target")
                    max_lookup=max(max_lookup,m1,m2,m3); kkeys.update((k1,k2,k3))
                    scale=max(float(np.max(np.abs(yp))),float(np.max(np.abs(ym))),np.finfo(np.float64).tiny)
                    shift=float(np.max(np.abs(yp-ym))/scale); node_shift_max=max(node_shift_max,shift)
                    sign_data[label]={
                        "pure_interp_transfer":float(ip[0]),
                        "mixed_interp_transfer":float(im[0]),
                        "mixed_exact_transfer":float(ye[0]),
                        "pure_vs_mixed_interp_transfer_rel":rel(float(ip[0]),float(im[0])),
                        "mixed_interp_vs_exact_transfer_rel":rel(float(im[0]),float(ye[0])),
                        "common_node_array_shift_norm":shift
                    }
                pure_resp=(sign_data["plus"]["pure_interp_transfer"]-sign_data["minus"]["pure_interp_transfer"])/(2*h)
                mixed_interp_resp=(sign_data["plus"]["mixed_interp_transfer"]-sign_data["minus"]["mixed_interp_transfer"])/(2*h)
                mixed_exact_resp=(sign_data["plus"]["mixed_exact_transfer"]-sign_data["minus"]["mixed_exact_transfer"])/(2*h)
                cells.append({
                    "grid":a.grid,"h":h,"h_key":format(h,".17g"),
                    "kind":t["kind"],"d":t["d"],"z":t["z"],"k":t["k"],
                    "z_value":z,"k_value":k,"parent_role":t["parent_role"],
                    "pure_interp_response":pure_resp,"mixed_interp_response":mixed_interp_resp,
                    "mixed_exact_response":mixed_exact_resp,
                    "pure_vs_mixed_interp_response_rel":rel(pure_resp,mixed_interp_resp),
                    "mixed_interp_vs_exact_response_rel":rel(mixed_interp_resp,mixed_exact_resp),
                    "signs":sign_data
                })
        finally:
            for c in list(pure.values())+list(mix.values()):
                try: c.struct_cleanup()
                except Exception: pass
    out={
        "schema":"LAYERB_BETA_PRODUCTION_H_COMMON_GRID_INTERPOLATION_DOMAIN_V0_12",
        "grid":a.grid,"base_n":base_n,"effect":"+0/+0","production_h":C["production_h"],
        "audit_h_values":hs,"tol_perturb_integration":C["tol300"],
        "common_requested_node_count":len(common),"mixed_requested_node_count":len(mixed),
        "exact_targets_added":expected_added,"solver_construction_count":solver_count,
        "max_requested_node_coordinate_rel_mismatch":max_lookup,
        "max_common_node_array_shift_norm":node_shift_max,"native_transfer_k_keys":sorted(kkeys),
        "cells":cells,"production_h_mutated":False,"sampling_stepsize_changed":False,
        "global_65537_launched":False,"covariance_read":False,"whitening_read":False,
        "nuisance_read":False,"relation_null_read":False,"Wm_S3_opened":False,
        "science_gate_opened":False,
        "token":"PASS_LAYERB_BETA_PRODUCTION_H_COMMON_GRID_INTERPOLATION_DOMAIN_V0_12"
    }
    Path(a.out).parent.mkdir(parents=True,exist_ok=True)
    Path(a.out).write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
    print(out["token"],a.grid,len(cells),solver_count,max_lookup)

def key(r):
    return (r["kind"],r["d"],r["z"],r["k"])

def decision_mode(a,C):
    direct_docs=[json.load(open(p)) for p in a.direct_inputs]
    if sorted(x.get("domain") for x in direct_docs)!=["B","D"]:
        raise RuntimeError("direct domain mismatch")
    direct={key(r):r for d in direct_docs for r in d["rows"]}
    prior_docs=[json.load(open(p)) for p in a.prior_grid_inputs]; prior={}
    for d in prior_docs:
        if d.get("token") not in {"PASS_LAYERB_BETA_TOL300_LOCAL_COMMON_GRID_DOMAIN_V0_10","PASS_LAYERB_BETA_COMMON_GRID_DISCREPANCY_DOMAIN_V0_11"}:
            raise RuntimeError("prior grid token mismatch")
        for r in d["rows"]: prior[(d["grid"],)+key(r)]=r
    new=[json.load(open(p)) for p in a.inputs]
    if sorted(x["grid"] for x in new)!=sorted(C["grids"]):
        raise RuntimeError("V0.12 grid set mismatch")
    cells=[]; max_lookup=0.0
    for d in new:
        if d.get("token")!="PASS_LAYERB_BETA_PRODUCTION_H_COMMON_GRID_INTERPOLATION_DOMAIN_V0_12":
            raise RuntimeError("V0.12 token mismatch")
        max_lookup=max(max_lookup,float(d["max_requested_node_coordinate_rel_mismatch"]))
        for r in d["cells"]:
            k=key(r); h=r["h_key"]; pr=prior[(d["grid"],)+k]["signed_centered_d2_by_h"][h]; dr=direct[k]["signed_centered_d2_by_h"][h]
            q=dict(r); q["prior_common_response"]=float(pr); q["independent_direct_response"]=float(dr)
            q["pure_vs_prior_common_response_rel"]=rel(q["pure_interp_response"],float(pr))
            q["pure_vs_direct_response_rel"]=rel(q["pure_interp_response"],float(dr))
            q["mixed_interp_vs_direct_response_rel"]=rel(q["mixed_interp_response"],float(dr))
            q["mixed_exact_vs_direct_response_rel"]=rel(q["mixed_exact_response"],float(dr)); cells.append(q)
    all_replay_bad=[r for r in cells if r["pure_vs_prior_common_response_rel"]>=C["replay_relative_tolerance"]]
    cellmap={(r["grid"],r["h_key"],r["z"],r["k"]):r for r in cells}
    violations=[]; interp_supported=[]; node_set_supported=[]
    for v in C["parent_violation_cells"]:
        ck=(v["grid"],format(float(v["h"]),".17g"),v["z"],v["k"]); r=cellmap[ck]
        replicated=r["pure_vs_direct_response_rel"]>=C["response_relative_tolerance"]
        replay=r["pure_vs_prior_common_response_rel"]<C["replay_relative_tolerance"]
        interp=(r["mixed_interp_vs_exact_response_rel"]>=C["response_relative_tolerance"] and r["mixed_exact_vs_direct_response_rel"]<C["response_relative_tolerance"] and r["pure_vs_mixed_interp_response_rel"]<C["response_relative_tolerance"])
        nodeset=(r["mixed_exact_vs_direct_response_rel"]>=C["response_relative_tolerance"] or r["pure_vs_mixed_interp_response_rel"]>=C["response_relative_tolerance"])
        violations.append({
            "grid":v["grid"],"h":v["h"],"z":v["z"],"k":v["k"],"replicated":replicated,
            "replay_ok":replay,"interpolation_mechanism_supported":interp,"node_set_dependence_supported":nodeset,
            "pure_vs_direct_response_rel":r["pure_vs_direct_response_rel"],
            "mixed_interp_vs_exact_response_rel":r["mixed_interp_vs_exact_response_rel"],
            "mixed_exact_vs_direct_response_rel":r["mixed_exact_vs_direct_response_rel"],
            "pure_vs_mixed_interp_response_rel":r["pure_vs_mixed_interp_response_rel"]
        })
        interp_supported.append(interp); node_set_supported.append(nodeset)
    finite=all(math.isfinite(float(v)) for r in cells for v in [r["pure_interp_response"],r["mixed_interp_response"],r["mixed_exact_response"],r["pure_vs_prior_common_response_rel"],r["mixed_interp_vs_exact_response_rel"],r["mixed_exact_vs_direct_response_rel"]])
    invariant_ok=(finite and max_lookup<=C["exact_target_binding_tolerance"] and not all_replay_bad)
    all_reproduced=all(x["replicated"] for x in violations)
    all_interp=all(interp_supported); all_nodeset=all(node_set_supported)
    fully_accounted=all(i or n for i,n in zip(interp_supported,node_set_supported))
    if not invariant_ok: cls="PRODUCTION_H_COMMON_GRID_INTERPOLATION_AUDIT_INCONCLUSIVE"
    elif all_reproduced and all_interp and not any(node_set_supported): cls="COMMON_GRID_CUBIC_INTERPOLATION_MECHANISM_SUPPORTED"
    elif all_reproduced and all_nodeset and not any(interp_supported): cls="K_OUTPUT_NODE_SET_SOLVER_DEPENDENCE_SUPPORTED"
    elif all_reproduced and fully_accounted and any(interp_supported) and any(node_set_supported): cls="MIXED_INTERPOLATION_AND_NODE_SET_DEPENDENCE_SUPPORTED"
    elif not all_reproduced: cls="PARENT_COMMON_GRID_VIOLATIONS_NOT_REPRODUCED"
    else: cls="PRODUCTION_H_COMMON_GRID_INTERPOLATION_PATTERN_UNRESOLVED"
    nxt={
        "COMMON_GRID_CUBIC_INTERPOLATION_MECHANISM_SUPPORTED":"PROSPECTIVELY_FROZEN_COMMON_GRID_INTERPOLATION_REMEDY_BENCHMARK",
        "K_OUTPUT_NODE_SET_SOLVER_DEPENDENCE_SUPPORTED":"PROSPECTIVELY_FROZEN_K_OUTPUT_NODE_SET_SOLVER_SENSITIVITY_AUDIT",
        "MIXED_INTERPOLATION_AND_NODE_SET_DEPENDENCE_SUPPORTED":"PROSPECTIVELY_FROZEN_MIXED_COMMON_GRID_NUMERICAL_MECHANISM_AUDIT",
        "PARENT_COMMON_GRID_VIOLATIONS_NOT_REPRODUCED":"PROSPECTIVELY_FROZEN_CROSS_RUN_COMMON_GRID_REPRODUCIBILITY_AUDIT",
        "PRODUCTION_H_COMMON_GRID_INTERPOLATION_PATTERN_UNRESOLVED":"PROSPECTIVELY_FROZEN_TARGET_STENCIL_GEOMETRY_AUDIT",
        "PRODUCTION_H_COMMON_GRID_INTERPOLATION_AUDIT_INCONCLUSIVE":"NO_SCIENTIFIC_PROMOTION_DIAGNOSE_V0_12_INVARIANT_FAILURE"
    }[cls]
    out={
        "schema":"LAYERB_BETA_PRODUCTION_H_COMMON_GRID_INTERPOLATION_DECISION_V0_12",
        "classification":cls,"effect":"+0/+0","violations":violations,"invariant_ok":invariant_ok,
        "max_requested_node_coordinate_rel_mismatch":max_lookup,"all_cells_replay_ok":not all_replay_bad,
        "replay_failure_count":len(all_replay_bad),"all_parent_violations_reproduced":all_reproduced,
        "interpolation_supported_count":sum(interp_supported),"node_set_dependence_supported_count":sum(node_set_supported),
        "production_h":C["production_h"],"tol_perturb_integration":C["tol300"],"production_h_mutated":False,
        "sampling_stepsize_changed":False,"global_65537_launched":False,"covariance_read":False,
        "whitening_read":False,"nuisance_read":False,"relation_null_read":False,"Wm_S3_opened":False,
        "science_gate_opened":False,"next_stage":nxt,
        "token":"PASS_LAYERB_BETA_PRODUCTION_H_COMMON_GRID_INTERPOLATION_DECISION_V0_12"
    }
    Path(a.out).parent.mkdir(parents=True,exist_ok=True); Path(a.out).write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
    print(out["token"],json.dumps({"classification":cls,"next_stage":nxt,"interpolation_supported_count":sum(interp_supported),"node_set_dependence_supported_count":sum(node_set_supported),"replay_failure_count":len(all_replay_bad)},sort_keys=True))

def main():
    p=argparse.ArgumentParser(); p.add_argument("--mode",choices=["domain","decision"],required=True)
    p.add_argument("--grid"); p.add_argument("--contract",required=True); p.add_argument("--jj-script")
    p.add_argument("--baseline"); p.add_argument("--precision"); p.add_argument("--direct-inputs",nargs="*",default=[])
    p.add_argument("--prior-grid-inputs",nargs="*",default=[]); p.add_argument("--inputs",nargs="*",default=[])
    p.add_argument("--out",required=True); a=p.parse_args(); C=json.load(open(a.contract))
    domain_mode(a,C) if a.mode=="domain" else decision_mode(a,C)

if __name__=="__main__": main()
