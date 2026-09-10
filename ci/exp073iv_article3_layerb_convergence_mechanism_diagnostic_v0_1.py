#!/usr/bin/env python3
from __future__ import annotations
import importlib.util, json, math, sys
from pathlib import Path
import numpy as np

PARENT_MAX=0.9998247463807295
TOKEN="PASS_EXP073IV_LAYERB_CONVERGENCE_MECHANISM_DIAGNOSTIC_V0_1"
UNRES="NUMERICALLY_UNRESOLVED_EXP073IR"

def load_module(path):
    spec=importlib.util.spec_from_file_location("exp073ir_frozen", Path(path))
    if spec is None or spec.loader is None: raise RuntimeError("cannot import frozen Exp073IR")
    m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m

def main():
    if len(sys.argv)<4 or sys.argv[1] != "--frozen-script" or sys.argv[3] != "--diagnostic-out":
        raise SystemExit("usage: --frozen-script PATH --diagnostic-out PATH [frozen Exp073IR args...]")
    frozen=Path(sys.argv[2]); diag_out=Path(sys.argv[4]); frozen_args=sys.argv[5:]
    m=load_module(frozen)
    state={"z":None,"targets":None}
    best=[None,None]
    original_response=m.ResponseSuite.response
    original_compare=m.compare_response

    def response(self,z,targets):
        out=original_response(self,z,targets)
        state["z"]=float(z); state["targets"]=np.asarray(targets,dtype=np.float64).copy()
        return out

    def compare(prod,dense,conv):
        p=np.asarray(prod,dtype=np.float64); d=np.asarray(dense,dtype=np.float64)
        if p.shape==d.shape and p.ndim==2 and p.shape[1]==2 and state["targets"] is not None and len(state["targets"])==len(p):
            for j in range(2):
                mask=np.isfinite(p[:,j])&np.isfinite(d[:,j])&(p[:,j]>0.0)&(d[:,j]>0.0)
                if np.any(mask):
                    idxs=np.flatnonzero(mask)
                    rel=np.abs(p[idxs,j]-d[idxs,j])/np.maximum(np.abs(p[idxs,j]),np.abs(d[idxs,j]))
                    q=int(np.argmax(rel)); ii=int(idxs[q]); rv=float(rel[q])
                    if best[j] is None or rv>best[j]["relative_difference"]:
                        best[j]={"component_index":j,"component_name":["abs_dDelta_m_dalpha_left","abs_dDelta_m_dbeta_symmetric"][j],"z":float(state["z"]),"k_Mpc^-1":float(state["targets"][ii]),"production_value":float(p[ii,j]),"dense_value":float(d[ii,j]),"relative_difference":rv,"response_vector_length":int(len(p))}
        return original_compare(prod,dense,conv)

    m.ResponseSuite.response=response
    m.compare_response=compare
    old=sys.argv
    try:
        sys.argv=[str(frozen)]+frozen_args
        rc=m.main()
    finally:
        sys.argv=old
    out_arg=frozen_args[frozen_args.index("--out")+1]
    parent=json.loads(Path(out_arg).read_text())
    global_best=max(x["relative_difference"] for x in best if x is not None)
    exact_match=(float(parent["convergence"]["max_relative_component_difference"])==float(PARENT_MAX)==float(global_best))
    firewall=(parent.get("covariance_read") is False and parent.get("whitening_read") is False and parent.get("nuisance_read") is False and parent.get("relation_null_read") is False)
    passed=(rc==0 and parent.get("status")==UNRES and all(x is not None for x in best) and exact_match and firewall)
    result={"experiment":"Exp073IV","schema":"EXP073IV_LAYERB_CONVERGENCE_MECHANISM_DIAGNOSTIC_RESULT_V0_1","classification":"SUPPORT_PLUS_0_PLUS_0" if passed else "SUPPORT_INVALID_PLUS_0_PLUS_0","token":TOKEN if passed else "INVALID_EXP073IV_LAYERB_CONVERGENCE_MECHANISM_DIAGNOSTIC_V0_1","parent":{"run":34432102035,"job":102729564736,"head":"38604061abe6cbcccbf9614b22e3ca0ca6a9ec0f","artifact":10134905199,"artifact_zip_sha256":"165a85c8348fc4fc4c52f3926aa1a46989179efc8413a059f9fc2d6aa9dfbb21","status":parent.get("status")},"parent_convergence":parent.get("convergence"),"component_maxima":best,"global_max_relative_difference":global_best,"exact_parent_max_match":exact_match,"covariance_firewall_intact":firewall,"scientific_authority_created":False,"covariance_restriction_authorized":False}
    diag_out.parent.mkdir(parents=True,exist_ok=True); diag_out.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
    print(result["token"])
    print("EXP073IV_COMPONENT_MAXIMA",json.dumps(best,sort_keys=True))
    return 0 if passed else 2

if __name__=="__main__": raise SystemExit(main())
