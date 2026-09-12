#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, importlib.util, json, struct
from pathlib import Path
import numpy as np
H=1e-4; TOL=1e-3; LOOKUP=1e-12; KPD=20.0

def load(name,path):
    s=importlib.util.spec_from_file_location(name,Path(path)); m=importlib.util.module_from_spec(s); s.loader.exec_module(m); return m

def f64(h): return struct.unpack('>d',bytes.fromhex(h))[0]
def rel(a,b): return abs(a-b)/max(abs(a),abs(b),np.finfo(np.float64).tiny)
def sha(path): return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def transfer_exact(jj,c,nodes,z):
    tk=c.get_transfer(z=float(z),output_format='class'); dm=[q for q in tk if q.strip()=='d_m']
    if len(dm)!=1: raise RuntimeError('exact d_m key missing')
    kkey=None; scale=None
    for q in tk:
        s=q.lower().replace(' ','')
        if s in {'k(h/mpc)','k[h/mpc]','k_h/mpc'} or ('k' in s and 'h/mpc' in s): kkey=q; scale=float(c.h()); break
        if s in {'k(1/mpc)','k[1/mpc]'} or ('k' in s and '1/mpc' in s): kkey=q; scale=1.0; break
    if kkey is None: raise RuntimeError('unrecognized CLASS k key')
    k=np.asarray(tk[kkey],dtype=np.float64)*scale; y=np.asarray(tk[dm[0]],dtype=np.float64)
    yn,mx=jj.requested_values(k,y,nodes)
    if mx>LOOKUP: raise RuntimeError(f'exact target binding failed {mx}')
    return yn,float(mx),str(kkey)

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--domain',choices=['D','B'],required=True)
    for x in ['probes','contract','jj-script','baseline','precision','out']: ap.add_argument('--'+x,required=True)
    a=ap.parse_args(); P=json.load(open(a.probes)); C=json.load(open(a.contract)); jj=load('jj_direct_v04',a.jj_script)
    if sha(a.probes)!=C['probe_manifest_sha256']: raise RuntimeError('probe manifest sha mismatch')
    if (jj.H,jj.REL_TOL,jj.NATIVE_KPD)!=(H,TOL,KPD): raise RuntimeError('frozen JJ constants mismatch')
    rows=[x for x in P['items'] if x['d']==a.domain]
    nodes=np.asarray(sorted(set(f64(x['k']) for x in rows)),dtype=np.float64); zs=sorted(set(f64(x['z']) for x in rows))
    from classy import Class
    models={}; kkeys=set(); max_lookup=0.0
    try:
      for label,beta in [('beta_plus',H),('beta_minus',-H)]:
        c=Class(); c.set(jj.class_params(Path(a.baseline),Path(a.precision),0.0,beta,nodes)); c.compute(['transfer']); models[label]=c
      byz={}
      for z in zs:
        bp,m1,k1=transfer_exact(jj,models['beta_plus'],nodes,z); bm,m2,k2=transfer_exact(jj,models['beta_minus'],nodes,z)
        max_lookup=max(max_lookup,m1,m2); kkeys.update((k1,k2)); byz[z]=(bp,bm)
      idx={float(k):i for i,k in enumerate(nodes)}; outrows=[]
      for x in rows:
        z=f64(x['z']); k=f64(x['k']); bp,bm=byz[z]; direct=abs(float(bp[idx[k]]-bm[idx[k]])/(2*H))
        outrows.append({**x,'z_value':z,'k_value':k,'direct_beta_response':direct,'coarse_to_direct_relative_difference':rel(float(x['c']),direct),'fine_to_direct_relative_difference':rel(float(x['f']),direct)})
    finally:
      for c in models.values():
        try:c.struct_cleanup()
        except Exception:pass
    dup={}
    for r in outrows:
      key=(r['z'],r['k']); v=r['direct_beta_response']
      if key in dup and struct.pack('>d',dup[key])!=struct.pack('>d',v): raise RuntimeError('duplicate direct disagreement')
      dup[key]=v
    result={'schema':'LAYERB_TARGETED_DIRECT_K_BETA_DOMAIN_RESULT_V0_4','domain':a.domain,'effect':'+0/+0','h':H,'relative_tolerance':TOL,'native_k_per_decade_for_pk':KPD,'class_solver_invoked':True,'support_cubic_interpolation_used':False,'exact_target_k_inserted_via_k_output_values':True,'unique_node_count':len(nodes),'unique_z_count':len(zs),'row_count':len(outrows),'unique_coordinate_count':len(dup),'max_exact_target_binding_relative_mismatch':max_lookup,'native_transfer_k_keys':sorted(kkeys),'covariance_read':False,'whitening_read':False,'nuisance_read':False,'relation_null_read':False,'Wm_S3_opened':False,'rows':outrows,'token':'PASS_LAYERB_TARGETED_DIRECT_K_BETA_DOMAIN_V0_4'}
    Path(a.out).parent.mkdir(parents=True,exist_ok=True); Path(a.out).write_text(json.dumps(result,indent=2,sort_keys=True)+'\n'); print(result['token'],a.domain,len(outrows),len(dup),max_lookup)
if __name__=='__main__': main()
