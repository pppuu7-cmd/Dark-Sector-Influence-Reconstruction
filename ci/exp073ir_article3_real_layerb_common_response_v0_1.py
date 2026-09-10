#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, importlib.util, json, math
from pathlib import Path
import numpy as np

PASS="PASS_PHYSICAL_SUPPORT_ARTICLE3"
FAIL="FAIL_PHYSICAL_SUPPORT_ARTICLE3"
UNRES="NUMERICALLY_UNRESOLVED_EXP073IR"
INVALID="INVALID_FOR_SCIENCE_ARTICLE3_SUPPORT"
LAYERA_PASS="PASS_ARTICLE3_OPERATOR_SUPPORT_V0_1"
EXPIM_PASS="PASS_EXP073IM_C2_REAL_RADIAL_SUPPORT_V0_2"
KMAX=0.06664762008318016
ZMIN=0.295
ZMAX=2.33
H=1e-4
FB_MAX=0.05
MIN_RETAINED=15
REL_TOL=1e-3
H_FID_BOSS=0.676
PARENT_RETAINED_SHA="44b57c6c910bc3612310ce415d773c8c180497528bfc5fc2927ce61da6ad40d7"
FULL_ORDER_SHA="bfaf582518cdbfd34b1e8392da83dac6b0885948bc31f2c29d4e48247c23af75"
EXPECTED_BOSS_SHA={
 "NGC":{"W":"a308dc562d1a7224cefcf91d32580877929e0daa33806517e0d2d53710236827","M":"3ac30e68f79deee59963c5c52f7585e0cde495393963210a3922c1c62513a042"},
 "SGC":{"W":"2a542a2d48f3e8c8299f58a885d5273238e4ade32c0f0de020d8b9f23afe7759","M":"3ac30e68f79deee59963c5c52f7585e0cde495393963210a3922c1c62513a042"},
}
EVEN_ROWS=(("P0",0,40),("P2",80,120),("P4",160,200))

def sha_bytes(b): return hashlib.sha256(b).hexdigest()
def sha_file(p):
    h=hashlib.sha256()
    with Path(p).open("rb") as f:
        for c in iter(lambda:f.read(1<<20),b""): h.update(c)
    return h.hexdigest()
def sha_lines(xs): return sha_bytes(("\n".join(xs)+"\n").encode())
def load_one_json(root,pred):
    hits=[]
    for p in Path(root).rglob("*.json"):
        try: d=json.loads(p.read_text())
        except Exception: continue
        if isinstance(d,dict) and pred(d): hits.append((p,d))
    if len(hits)!=1: raise AssertionError(f"expected one JSON, got {[str(p) for p,_ in hits]}")
    return hits[0][1]
def import_module(name,path):
    spec=importlib.util.spec_from_file_location(name,Path(path))
    if spec is None or spec.loader is None: raise AssertionError(f"cannot import {path}")
    m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m

def parse_kv(path):
    out={}
    for raw in Path(path).read_text().splitlines():
        s=raw.strip()
        if not s or s.startswith("#") or "=" not in s: continue
        k,v=s.split("=",1); k=k.strip(); v=v.split("#",1)[0].strip()
        if k and v: out[k]=v
    return out

def class_params(baseline,precision,alpha,beta,kpd):
    d=parse_kv(baseline); d.update(parse_kv(precision))
    for k in ["root","headers","write background","write thermodynamics","write primordial"]: d.pop(k,None)
    d["alpha_idm_iv"]=format(alpha,".17g")
    d["beta_idm_iv"]=format(beta,".17g")
    d["output"]="mTk"
    d["z_pk"]="2.34"
    d["P_k_max_h/Mpc"]="0.25"
    d["k_per_decade_for_pk"]=format(kpd,".17g")
    return d

def transfer_arrays(cosmo,z):
    tk=cosmo.get_transfer(z=float(z),output_format="class")
    if not isinstance(tk,dict) or not tk: raise AssertionError(f"empty get_transfer at z={z}")
    dm_keys=[k for k in tk if k.strip()=="d_m"]
    if len(dm_keys)!=1: raise AssertionError(f"expected exact d_m key, got {list(tk)}")
    kkey=None; scale=None
    for k in tk:
        kl=k.lower().replace(" ","")
        if kl in {"k(h/mpc)","k[h/mpc]","k_h/mpc"} or ("k" in kl and "h/mpc" in kl):
            kkey=k; scale=float(cosmo.h()); break
        if kl in {"k(1/mpc)","k[1/mpc]"} or ("k" in kl and "1/mpc" in kl):
            kkey=k; scale=1.0; break
    if kkey is None: raise AssertionError(f"unrecognized CLASS k key(s): {list(tk)}")
    k=np.asarray(tk[kkey],dtype=np.float64)*scale
    dm=np.asarray(tk[dm_keys[0]],dtype=np.float64)
    if k.ndim!=1 or dm.shape!=k.shape or len(k)<4: raise AssertionError("bad transfer shapes")
    if np.any(~np.isfinite(k)) or np.any(~np.isfinite(dm)) or np.any(k<=0) or np.any(np.diff(k)<=0): raise AssertionError("invalid native transfer table")
    return k,dm,kkey

def interp_ln(k_native,y_native,targets):
    t=np.asarray(targets,dtype=np.float64)
    if t.size==0: return np.empty(0,dtype=np.float64)
    if np.any(t<k_native[0]) or np.any(t>k_native[-1]): raise FloatingPointError(f"unbracketed target [{t.min()},{t.max()}] native [{k_native[0]},{k_native[-1]}]")
    return np.interp(np.log(t),np.log(k_native),y_native)

class ResponseSuite:
    def __init__(self,baseline,precision,kpd):
        from classy import Class
        self.models=[]; self.kkeys=set(); self.kpd=kpd
        for alpha,beta in ((0.0,0.0),(-H,0.0),(0.0,H),(0.0,-H)):
            c=Class(); c.set(class_params(baseline,precision,alpha,beta,kpd)); c.compute(["transfer"]); self.models.append(c)
    def response(self,z,targets):
        vals=[]
        for c in self.models:
            k,y,key=transfer_arrays(c,z); self.kkeys.add(key); vals.append(interp_ln(k,y,targets))
        ref,al,bp,bm=vals
        return np.column_stack((np.abs((al-ref)/(-H)),np.abs((bp-bm)/(2*H))))
    def close(self):
        for c in self.models:
            try: c.struct_cleanup()
            except Exception: pass
        self.models=[]

def boss_geometry(root):
    root=Path(root); ids=[]; weights=[]
    for cap in ("NGC","SGC"):
        wp=root/f"W_{cap}_z3"; mp=root/f"M_{cap}_z3"
        if sha_file(wp)!=EXPECTED_BOSS_SHA[cap]["W"] or sha_file(mp)!=EXPECTED_BOSS_SHA[cap]["M"]: raise AssertionError(f"BOSS source hash mismatch {cap}")
        W=np.loadtxt(wp,dtype=np.float64); M=np.loadtxt(mp,dtype=np.float64)
        if W.shape!=(200,2000) or M.shape!=(2000,1200): raise AssertionError("BOSS shape mismatch")
        C=W@M
        for mult,lo,hi in EVEN_ROWS:
            for row in range(lo,hi):
                ids.append(f"BOSS|{cap}|{mult}|matrix_row={row:03d}"); weights.append(np.abs(C[row]))
    kh=0.0005+0.001*np.arange(400,dtype=np.float64)
    return ids,np.stack(weights),np.tile(H_FID_BOSS*kh,3)

def empty_summary(cid,ordinal,block):
    return {"coordinate_id":cid,"ordinal":int(ordinal),"block":block,"atom_count":0,"finite_nonzero":True,"min_components":[math.inf,math.inf]}
def update_summary(s,resp):
    finite=np.isfinite(resp); pos=resp>0.0
    s["atom_count"]+=int(resp.shape[0]); s["finite_nonzero"]=bool(s["finite_nonzero"] and np.all(finite&pos))
    for j in range(2):
        x=resp[:,j]
        if x.size and np.any(np.isfinite(x)): s["min_components"][j]=min(s["min_components"][j],float(np.min(x[np.isfinite(x)])))
def compare_response(prod,dense,conv):
    if prod.shape!=dense.shape: raise AssertionError("response shape mismatch")
    fp=np.isfinite(prod); fd=np.isfinite(dense); pp=prod>0.0; pd=dense>0.0
    if not np.array_equal(fp,fd) or not np.array_equal(pp,pd): conv["finite_nonzero_status_changed"]=True; return
    m=fp&fd&pp&pd
    if np.any(m):
        rel=np.abs(prod[m]-dense[m])/np.maximum(np.abs(prod[m]),np.abs(dense[m]))
        conv["max_relative_component_difference"]=max(conv["max_relative_component_difference"],float(np.max(rel)))
def gl_nodes(n,lo=0.5,hi=0.75):
    x,w=np.polynomial.legendre.leggauss(n); z=(lo+hi)/2+(hi-lo)*x/2; ww=(hi-lo)*w/2
    if not (np.all(z>lo)&np.all(z<hi)&np.all(ww>0)): raise AssertionError("bad GL nodes")
    return z.astype(np.float64),ww.astype(np.float64)

def main():
    ap=argparse.ArgumentParser()
    for x in ["parent-root","parent-authority","manifest","angular-root","expim-root","boss-root","source","lens","camb-root","expz2-script","exp073iq-script","baseline","precision","scratch","out"]: ap.add_argument("--"+x,required=True)
    a=ap.parse_args(); outp=Path(a.out); scratch=Path(a.scratch); scratch.mkdir(parents=True,exist_ok=True)
    result={"experiment":"Exp073IR","status":INVALID,"covariance_read":False,"whitening_read":False,"nuisance_read":False,"relation_null_read":False,"selection_reads":[]}
    try:
        auth=json.loads(Path(a.parent_authority).read_text())
        assert auth["status"]==LAYERA_PASS and auth["workflow_run"]==34423479633 and auth["workflow_job"]==102703685034
        assert auth["artifact_id"]==10131794281 and auth["combined_retained_count"]==107 and auth["retained_id_sha256"]==PARENT_RETAINED_SHA and auth["full_order_sha256"]==FULL_ORDER_SHA
        parent=load_one_json(a.parent_root,lambda d:d.get("schema")=="EXP073IQ_ARTICLE3_REAL_LAYERA_SUPPORT_RESULT_V0_1")
        retained=parent["retained_coordinate_ids"]
        assert parent["status"]==LAYERA_PASS and len(retained)==107 and len(set(retained))==107 and sha_lines(retained)==PARENT_RETAINED_SHA and parent["full_order_sha256"]==FULL_ORDER_SHA

        iq=import_module("exp073iq_parent",a.exp073iq_script)
        manifest=json.loads(Path(a.manifest).read_text()); assert manifest["schema"]=="EXP073IM_C2_REAL_INPUT_MANIFEST_V0_4"
        angular={s["slot"]:iq.find_angular(Path(a.angular_root)/s["slot"],s) for s in manifest["angular"]}
        expim=load_one_json(a.expim_root,lambda d:d.get("status")==EXPIM_PASS); assert len(expim["rows"])==1170 and expim["scientific_radial_pass"] is True
        expim_map={r["coordinate_id"]:r for r in expim["rows"]}
        rad=iq.reconstruct_radials(iq.import_expz2(Path(a.expz2_script)),a.source,a.lens,a.camb_root,manifest)["fine"]
        zdes=np.asarray(rad["z"],dtype=np.float64); chides=np.asarray(rad["chi"],dtype=np.float64); assert zdes.shape==(2001,) and chides.shape==(2001,)
        des_parent={r["coordinate_id"]:r for r in parent["des_rows"] if r["retained"]}; assert len(des_parent)==53
        des_meta=[expim_map[cid] for cid in retained if cid in des_parent]; assert len(des_meta)==53

        boss_ids,boss_w,boss_k=boss_geometry(a.boss_root); boss_index={cid:i for i,cid in enumerate(boss_ids)}
        boss_ret=[cid for cid in retained if cid in boss_index]; assert len(boss_ret)==54
        rows={}
        for cid in retained:
            if cid in des_parent:
                r=des_parent[cid]; rows[cid]=empty_summary(cid,r["ordinal"],r["block"])
            else:
                i=boss_index[cid]; rows[cid]=empty_summary(cid,1170+i,"BOSS")

        conv={"production_k_per_decade_for_pk":10.0,"dense_k_per_decade_for_pk":20.0,"max_relative_component_difference":0.0,"finite_nonzero_status_changed":False,"row_label_changed":False,"boss_dense_z_disagreement":False}
        prod_store=np.memmap(scratch/"des_prod_response.f64",mode="w+",dtype="<f8",shape=(len(zdes),12288,2))
        native_k_keys=set(); prod=ResponseSuite(Path(a.baseline),Path(a.precision),10.0)
        try:
            for iz,z in enumerate(zdes):
                k=(np.arange(12288,dtype=np.float64)+0.5)/chides[iz]; inD=(k>0.0)&(k<=KMAX)&(z>=ZMIN)&(z<=ZMAX)
                union=np.zeros(12288,dtype=bool); active_by_row={}
                for r in des_meta:
                    B=rad["wm" if r["block"]=="Wm" else "ww"][int(r["radial_index"])]
                    if not (float(B[iz])>0.0): continue
                    active=(np.abs(angular[r["slot"]][int(r["band_index"])])>0.0)&inD
                    if np.any(active): active_by_row[r["coordinate_id"]]=active; union|=active
                rr=np.full((12288,2),np.nan,dtype=np.float64)
                if np.any(union): rr[union]=prod.response(float(z),k[union]); native_k_keys|=prod.kkeys
                prod_store[iz]=rr
                for cid,active in active_by_row.items(): update_summary(rows[cid],rr[active])
        finally: prod.close()
        prod_store.flush()

        zb64,_=gl_nodes(64); bprod={}; prod=ResponseSuite(Path(a.baseline),Path(a.precision),10.0)
        try:
            needed=np.zeros(1200,dtype=bool)
            for cid in boss_ret:
                i=boss_index[cid]; needed|=(boss_w[i]>0.0)&(boss_k>0.0)&(boss_k<=KMAX)
            kt=boss_k[needed]
            for z in zb64:
                rr=prod.response(float(z),kt); native_k_keys|=prod.kkeys; bprod[float(z)]=rr.copy()
                for cid in boss_ret:
                    i=boss_index[cid]; am=((boss_w[i]>0.0)&(boss_k>0.0)&(boss_k<=KMAX))[needed]
                    if np.any(am): update_summary(rows[cid],rr[am])
        finally: prod.close()
        prod_labels={cid:(s["atom_count"]>0 and s["finite_nonzero"]) for cid,s in rows.items()}

        dense_rows={cid:empty_summary(cid,s["ordinal"],s["block"]) for cid,s in rows.items()}; dense=ResponseSuite(Path(a.baseline),Path(a.precision),20.0)
        try:
            for iz,z in enumerate(zdes):
                k=(np.arange(12288,dtype=np.float64)+0.5)/chides[iz]; inD=(k>0.0)&(k<=KMAX)&(z>=ZMIN)&(z<=ZMAX)
                union=np.zeros(12288,dtype=bool); active_by_row={}
                for r in des_meta:
                    B=rad["wm" if r["block"]=="Wm" else "ww"][int(r["radial_index"])]
                    if not (float(B[iz])>0.0): continue
                    active=(np.abs(angular[r["slot"]][int(r["band_index"])])>0.0)&inD
                    if np.any(active): active_by_row[r["coordinate_id"]]=active; union|=active
                rr=np.full((12288,2),np.nan,dtype=np.float64)
                if np.any(union): rr[union]=dense.response(float(z),k[union]); native_k_keys|=dense.kkeys; compare_response(np.asarray(prod_store[iz][union]),rr[union],conv)
                for cid,active in active_by_row.items(): update_summary(dense_rows[cid],rr[active])
            needed=np.zeros(1200,dtype=bool)
            for cid in boss_ret:
                i=boss_index[cid]; needed|=(boss_w[i]>0.0)&(boss_k>0.0)&(boss_k<=KMAX)
            kt=boss_k[needed]
            for z in zb64:
                rr=dense.response(float(z),kt); native_k_keys|=dense.kkeys; compare_response(bprod[float(z)],rr,conv)
                for cid in boss_ret:
                    i=boss_index[cid]; am=((boss_w[i]>0.0)&(boss_k>0.0)&(boss_k<=KMAX))[needed]
                    if np.any(am): update_summary(dense_rows[cid],rr[am])
        finally: dense.close()
        dense_labels={cid:(s["atom_count"]>0 and s["finite_nonzero"]) for cid,s in dense_rows.items()}; conv["row_label_changed"]=prod_labels!=dense_labels

        zb128,_=gl_nodes(128); boss_dense_z={cid:True for cid in boss_ret}; dense=ResponseSuite(Path(a.baseline),Path(a.precision),20.0)
        try:
            needed=np.zeros(1200,dtype=bool)
            for cid in boss_ret:
                i=boss_index[cid]; needed|=(boss_w[i]>0.0)&(boss_k>0.0)&(boss_k<=KMAX)
            kt=boss_k[needed]
            for z in zb128:
                rr=dense.response(float(z),kt); native_k_keys|=dense.kkeys
                for cid in boss_ret:
                    i=boss_index[cid]; am=((boss_w[i]>0.0)&(boss_k>0.0)&(boss_k<=KMAX))[needed]
                    if not np.any(am) or not np.all(np.isfinite(rr[am])&(rr[am]>0.0)): boss_dense_z[cid]=False
        finally: dense.close()
        for cid in boss_ret:
            if boss_dense_z[cid]!=prod_labels[cid]: conv["boss_dense_z_disagreement"]=True

        unresolved=conv["finite_nonzero_status_changed"] or conv["row_label_changed"] or conv["boss_dense_z_disagreement"] or conv["max_relative_component_difference"]>REL_TOL
        invalid_ids=[cid for cid in retained if not prod_labels[cid]]; ninvalid=len(invalid_ids); nremain=107-ninvalid; fb=ninvalid/107.0
        status=UNRES if unresolved else (PASS if fb<=FB_MAX and nremain>=MIN_RETAINED else FAIL)
        ordered=[]
        for cid in retained:
            q=rows[cid].copy(); q["valid_common_response"]=bool(prod_labels[cid]); q["min_components"]=[None if math.isinf(x) else x for x in q["min_components"]]; ordered.append(q)
        result={"experiment":"Exp073IR","schema":"EXP073IR_ARTICLE3_REAL_LAYERB_COMMON_RESPONSE_RESULT_V0_1","status":status,
          "parent":{"run":34423479633,"job":102703685034,"artifact":10131794281,"retained_count":107,"retained_id_sha256":PARENT_RETAINED_SHA,"full_order_sha256":FULL_ORDER_SHA},
          "response_components":["abs_dDelta_m_dalpha_left","abs_dDelta_m_dbeta_symmetric"],"h":H,
          "solver":"kaeonikc/class_iv@ac627d54e9ce196a08878d1ba33999819925d19c","source_route":"public get_transfer(z, output_format='class') / gauge-invariant d_m directly; no second gauge correction",
          "native_transfer_k_keys":sorted(native_k_keys),"domain":{"z_min":ZMIN,"z_max":ZMAX,"k_positive":True,"k_max_Mpc^-1":KMAX},
          "des_atomization":{"radial_nodes":2001,"representation":"FACTORIZED_BROAD_SUPPORT_V0_2"},
          "boss_atomization":{"z_support_open":[0.5,0.75],"production_quadrature":"Gauss-Legendre-64","dense_z_control":"Gauss-Legendre-128","effective_z_used":False},
          "convergence":{**conv,"relative_tolerance":REL_TOL,"pass":not unresolved},
          "layer_b":{"invalid_row_count":ninvalid,"invalid_row_fraction":fb,"invalid_coordinate_ids":invalid_ids,"retained_after_layer_b":nremain,"threshold_inclusive":FB_MAX,"minimum_retained":MIN_RETAINED},
          "rows":ordered,"covariance_read":False,"whitening_read":False,"nuisance_read":False,"relation_null_read":False,"selection_reads":[],"covariance_restriction_authorized":status==PASS}
    except FloatingPointError as e: result.update({"status":UNRES,"error":f"{type(e).__name__}: {e}","covariance_restriction_authorized":False})
    except Exception as e: result.update({"status":INVALID,"error":f"{type(e).__name__}: {e}","covariance_restriction_authorized":False})
    outp.parent.mkdir(parents=True,exist_ok=True); outp.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
    print(result["status"])
    if "layer_b" in result: print("INVALID_ROWS",result["layer_b"]["invalid_row_count"],"FB",result["layer_b"]["invalid_row_fraction"],"REMAIN",result["layer_b"]["retained_after_layer_b"])
    if "convergence" in result: print("CONVERGENCE",result["convergence"])
    return 0

if __name__=="__main__": raise SystemExit(main())
