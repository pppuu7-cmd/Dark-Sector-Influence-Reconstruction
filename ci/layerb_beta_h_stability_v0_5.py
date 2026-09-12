#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, importlib.util, json, math, struct
from pathlib import Path
import numpy as np

LOOKUP=1e-12

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
    a=ap.parse_args(); P=json.load(open(a.probes)); C=json.load(open(a.contract)); jj=load('jj_h_v05',a.jj_script)
    if sha(a.probes)!=C['probe_manifest_sha256']: raise RuntimeError('probe manifest sha mismatch')
    if jj.REL_TOL!=C['relative_tolerance'] or jj.NATIVE_KPD!=C['native_k_per_decade_for_pk']: raise RuntimeError('frozen constants mismatch')
    if C['production_h']!=jj.H: raise RuntimeError('production h identity mismatch')
    hs=[float(x) for x in C['h_values']]
    if hs != [4e-4,2e-4,1e-4,5e-5,2.5e-5]: raise RuntimeError('unexpected h grid')
    source=[x for x in P['items'] if x['d']==a.domain]
    uniq={}
    for x in source:
        key=(x['kind'],x['z'],x['k'])
        if key in uniq:
            if uniq[key]['c']!=x['c'] or uniq[key]['f']!=x['f']: raise RuntimeError('duplicate probe mismatch')
        else: uniq[key]=x
    rows=list(uniq.values())
    nodes=np.asarray(sorted(set(f64(x['k']) for x in rows)),dtype=np.float64); zs=sorted(set(f64(x['z']) for x in rows))
    from classy import Class
    responses={(f64(x['z']),f64(x['k'])):{} for x in rows}; max_lookup=0.0; kkeys=set(); solver_count=0
    for h in hs:
        models={}
        try:
            for label,beta in [('plus',h),('minus',-h)]:
                c=Class(); c.set(jj.class_params(Path(a.baseline),Path(a.precision),0.0,beta,nodes)); c.compute(['transfer']); models[label]=c; solver_count+=1
            byz={}
            for z in zs:
                bp,m1,k1=transfer_exact(jj,models['plus'],nodes,z); bm,m2,k2=transfer_exact(jj,models['minus'],nodes,z)
                max_lookup=max(max_lookup,m1,m2); kkeys.update((k1,k2)); byz[z]=(bp,bm)
            idx={float(k):i for i,k in enumerate(nodes)}
            for z,k in responses:
                bp,bm=byz[z]; responses[(z,k)][format(h,'.17g')]=abs(float(bp[idx[k]]-bm[idx[k]])/(2*h))
        finally:
            for c in models.values():
                try:c.struct_cleanup()
                except Exception:pass
    outrows=[]
    for x in rows:
        z=f64(x['z']); k=f64(x['k']); r=responses[(z,k)]; vals=list(r.values())
        if not all(math.isfinite(v) for v in vals): raise RuntimeError('nonfinite response')
        spread=max(rel(vals[i],vals[j]) for i in range(len(vals)) for j in range(i+1,len(vals)))
        prod=r[format(C['production_h'],'.17g')]
        outrows.append({
            'kind':x['kind'],'d':x['d'],'z':x['z'],'k':x['k'],'z_value':z,'k_value':k,
            'responses_by_h':r,'production_h_response':prod,'h_spread':spread,
            'coarse_reference':float(x['c']),'fine_reference':float(x['f'])
        })
    result={
        'schema':'LAYERB_BETA_H_STABILITY_DOMAIN_RESULT_V0_5','domain':a.domain,'effect':'+0/+0',
        'h_values':hs,'production_h':C['production_h'],'relative_tolerance':C['relative_tolerance'],
        'class_solver_invoked':True,'solver_construction_count':solver_count,'support_cubic_interpolation_used':False,
        'exact_target_k_inserted_via_k_output_values':True,'unique_node_count':len(nodes),'unique_z_count':len(zs),
        'row_count':len(outrows),'max_exact_target_binding_relative_mismatch':max_lookup,'native_transfer_k_keys':sorted(kkeys),
        'covariance_read':False,'whitening_read':False,'nuisance_read':False,'relation_null_read':False,'Wm_S3_opened':False,
        'science_gate_opened':False,'rows':outrows,'token':'PASS_LAYERB_BETA_H_STABILITY_DOMAIN_V0_5'
    }
    Path(a.out).parent.mkdir(parents=True,exist_ok=True); Path(a.out).write_text(json.dumps(result,indent=2,sort_keys=True)+'\n'); print(result['token'],a.domain,len(outrows),solver_count,max_lookup)

if __name__=='__main__': main()
