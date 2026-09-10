#!/usr/bin/env python3
from __future__ import annotations
import argparse, importlib.util, json, math, sys
from pathlib import Path
import numpy as np

N=512
KMIN=1e-4
KMAX=0.06664762008318016
H=1e-4
REL_TOL=1e-3
LOOKUP_REL_TOL=1e-12


def import_module(name,path):
    spec=importlib.util.spec_from_file_location(name,Path(path))
    if spec is None or spec.loader is None: raise RuntimeError(f'cannot import {path}')
    m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m


def parse_kv(path):
    out={}
    for raw in Path(path).read_text().splitlines():
        s=raw.strip()
        if not s or s.startswith('#') or '=' not in s: continue
        k,v=s.split('=',1); k=k.strip(); v=v.split('#',1)[0].strip()
        if k and v: out[k]=v
    return out


def class_params(baseline,precision,alpha,beta,kpd,nodes):
    d=parse_kv(baseline); d.update(parse_kv(precision))
    for k in ['root','headers','write background','write thermodynamics','write primordial']: d.pop(k,None)
    d['alpha_idm_iv']=format(alpha,'.17g'); d['beta_idm_iv']=format(beta,'.17g')
    d['output']='mTk'; d['z_pk']='2.34'; d['P_k_max_h/Mpc']='0.25'; d['k_per_decade_for_pk']=format(kpd,'.17g')
    d['k_output_values']=','.join(format(float(x),'.17g') for x in nodes)
    return d


def requested_values(k,y,nodes):
    p=np.searchsorted(k,nodes)
    p=np.clip(p,0,len(k)-1)
    pm=np.maximum(p-1,0)
    choose_prev=np.abs(k[pm]-nodes) < np.abs(k[p]-nodes)
    idx=np.where(choose_prev,pm,p)
    actual=k[idx]
    rel=np.abs(actual-nodes)/np.maximum(np.abs(nodes),np.finfo(np.float64).tiny)
    if np.any(rel>LOOKUP_REL_TOL):
        q=int(np.argmax(rel)); raise FloatingPointError(f'requested shared node absent i={q} rel={rel[q]:.3e}')
    return np.asarray(y[idx],dtype=np.float64),float(np.max(rel))


def cubic_centered(nodes,ynodes,targets):
    t=np.asarray(targets,dtype=np.float64)
    out=np.full(t.shape,np.nan,dtype=np.float64)
    j=np.searchsorted(nodes,t)
    valid=(t>0.0)&(j>=2)&(j<=len(nodes)-2)
    if not np.any(valid): return out,valid
    jj=j[valid]; xt=np.log(t[valid])
    inds=np.stack((jj-2,jj-1,jj,jj+1),axis=1)
    xs=np.log(nodes[inds]); ys=ynodes[inds]
    vv=np.zeros(len(xt),dtype=np.float64)
    for a in range(4):
        w=np.ones(len(xt),dtype=np.float64)
        for b in range(4):
            if a!=b: w *= (xt-xs[:,b])/(xs[:,a]-xs[:,b])
        vv += ys[:,a]*w
    out[valid]=vv
    return out,valid


class FixedCubicSuite:
    audit={}
    def __init__(self,baseline,precision,kpd):
        from classy import Class
        self.kpd=float(kpd); self.models=[]; self.kkeys=set(); self.nodes=np.geomspace(KMIN,KMAX,N,dtype=np.float64)
        rec=self.audit.setdefault(format(self.kpd,'.17g'),{'response_calls':0,'target_evaluations':0,'unsupported_target_evaluations':0,'max_requested_node_coordinate_rel_mismatch':0.0})
        self.rec=rec
        for alpha,beta in ((0.0,0.0),(-H,0.0),(0.0,H),(0.0,-H)):
            c=Class(); c.set(class_params(baseline,precision,alpha,beta,self.kpd,self.nodes)); c.compute(['transfer']); self.models.append(c)
    def response(self,z,targets):
        t=np.asarray(targets,dtype=np.float64)
        vals=[]; valid_ref=None
        for c in self.models:
            tk=c.get_transfer(z=float(z),output_format='class')
            dm=[q for q in tk if q.strip()=='d_m']
            if len(dm)!=1: raise AssertionError(f'expected exact d_m key, got {list(tk)}')
            kkey=None; scale=None
            for q in tk:
                s=q.lower().replace(' ','')
                if s in {'k(h/mpc)','k[h/mpc]','k_h/mpc'} or ('k' in s and 'h/mpc' in s): kkey=q; scale=float(c.h()); break
                if s in {'k(1/mpc)','k[1/mpc]'} or ('k' in s and '1/mpc' in s): kkey=q; scale=1.0; break
            if kkey is None: raise AssertionError('unrecognized CLASS k key')
            self.kkeys.add(kkey)
            k=np.asarray(tk[kkey],dtype=np.float64)*scale; y=np.asarray(tk[dm[0]],dtype=np.float64)
            if k.ndim!=1 or y.shape!=k.shape or np.any(~np.isfinite(k)) or np.any(~np.isfinite(y)) or np.any(k<=0) or np.any(np.diff(k)<=0): raise AssertionError('invalid transfer table')
            yn,mx=requested_values(k,y,self.nodes); self.rec['max_requested_node_coordinate_rel_mismatch']=max(self.rec['max_requested_node_coordinate_rel_mismatch'],mx)
            v,valid=cubic_centered(self.nodes,yn,t)
            if valid_ref is None: valid_ref=valid
            elif not np.array_equal(valid_ref,valid): raise AssertionError('model stencil-validity mismatch')
            vals.append(v)
        self.rec['response_calls']+=1; self.rec['target_evaluations']+=int(t.size); self.rec['unsupported_target_evaluations']+=int(np.count_nonzero(~valid_ref))
        ref,al,bp,bm=vals
        return np.column_stack((np.abs((al-ref)/(-H)),np.abs((bp-bm)/(2*H))))
    def close(self):
        for c in self.models:
            try: c.struct_cleanup()
            except Exception: pass
        self.models=[]


def main():
    ap=argparse.ArgumentParser()
    common=['parent-root','parent-authority','manifest','angular-root','expim-root','boss-root','source','lens','camb-root','expz2-script','exp073iq-script','baseline','precision','scratch']
    for x in common: ap.add_argument('--'+x,required=True)
    ap.add_argument('--ir-script',required=True); ap.add_argument('--capacity-patch-record',required=True); ap.add_argument('--out',required=True)
    a=ap.parse_args()
    patch=json.loads(Path(a.capacity_patch_record).read_text())
    if patch.get('old_capacity')!=30 or patch.get('new_capacity')!=512 or patch.get('replacement_count')!=1: raise SystemExit('invalid k-output capacity patch record')
    if patch.get('parser_old_argument_capacity')!=1024 or patch.get('parser_new_argument_capacity')!=32768 or patch.get('parser_replacement_count')!=1: raise SystemExit('invalid parser capacity patch record')
    ir=import_module('exp073ir_full_support_parent',a.ir_script)
    if ir.H!=H or ir.REL_TOL!=REL_TOL or ir.KMAX!=KMAX or ir.ZMIN!=0.295 or ir.ZMAX!=2.33: raise SystemExit('Exp073IR frozen constants mismatch')
    FixedCubicSuite.audit={}; ir.ResponseSuite=FixedCubicSuite
    inner=Path(a.scratch)/'exp073jh_inner_ir.json'; inner.parent.mkdir(parents=True,exist_ok=True)
    argv=['exp073ir']
    for x in common:
        argv += ['--'+x,str(getattr(a,x.replace('-','_')))]
    argv += ['--out',str(inner)]
    old=sys.argv; sys.argv=argv
    try:
        rc=ir.main()
    finally:
        sys.argv=old
    if rc!=0 or not inner.exists(): raise SystemExit('inner Exp073IR accounting execution failed')
    d=json.loads(inner.read_text())
    if d.get('covariance_read') is not False or d.get('whitening_read') is not False or d.get('nuisance_read') is not False or d.get('relation_null_read') is not False:
        raise SystemExit('forbidden downstream quantity read')
    parent=d.get('parent',{}); layer=d.get('layer_b',{}); conv=d.get('convergence',{})
    audit=FixedCubicSuite.audit
    unsupported=sum(int(v.get('unsupported_target_evaluations',0)) for v in audit.values())
    exact_parent=(parent.get('retained_count')==107 and parent.get('retained_id_sha256')==ir.PARENT_RETAINED_SHA and parent.get('full_order_sha256')==ir.FULL_ORDER_SHA)
    feasible=bool(exact_parent and unsupported==0 and conv.get('finite_nonzero_status_changed') is False and conv.get('row_label_changed') is False and conv.get('boss_dense_z_disagreement') is False and isinstance(conv.get('max_relative_component_difference'),(int,float)) and math.isfinite(conv['max_relative_component_difference']) and conv['max_relative_component_difference']<REL_TOL and layer.get('invalid_row_fraction',1.0)<=ir.FB_MAX and layer.get('retained_after_layer_b',0)>=ir.MIN_RETAINED)
    classification='FULL_SUPPORT_GRID_INVARIANT_FEASIBLE_PLUS_0_PLUS_0' if feasible else 'FULL_SUPPORT_GRID_INVARIANT_NOT_FEASIBLE_PLUS_0_PLUS_0'
    result={
      'schema':'EXP073JH_ARTICLE3_LAYERB_FULL_SUPPORT_GRID_INVARIANT_FEASIBILITY_RESULT_V0_1','experiment':'Exp073JH','classification':classification,'effect':'+0/+0',
      'scientific_authority_created':False,'covariance_restriction_authorized':False,'architecture':'N512_SHARED_PHYSICAL_K_CUBIC_CENTERED_LN_K_V0_1','h':H,'rel_tol':REL_TOL,
      'fixed_k_min':KMIN,'fixed_k_max':KMAX,'node_count':N,'parent_identity_preserved':exact_parent,'response_engine_audit':audit,'unsupported_target_evaluations':unsupported,
      'inner_status_for_accounting_only':d.get('status'),'inner_covariance_authorization_ignored':bool(d.get('covariance_restriction_authorized',False)),
      'convergence':conv,'layer_b':layer,'native_transfer_k_keys':d.get('native_transfer_k_keys',[]),
      'token':'PASS_EXP073JH_FULL_SUPPORT_GRID_INVARIANT_FEASIBLE_V0_1' if feasible else 'PASS_EXP073JH_FULL_SUPPORT_GRID_INVARIANT_NOT_FEASIBLE_V0_1'
    }
    Path(a.out).parent.mkdir(parents=True,exist_ok=True); Path(a.out).write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(result['token']); print('UNSUPPORTED_TARGET_EVALUATIONS',unsupported); print('CONVERGENCE',json.dumps(conv,sort_keys=True)); print('LAYER_B',json.dumps(layer,sort_keys=True)); print('RESPONSE_ENGINE_AUDIT',json.dumps(audit,sort_keys=True))
    return 0

if __name__=='__main__': raise SystemExit(main())
