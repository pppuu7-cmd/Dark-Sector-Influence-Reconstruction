#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, importlib.util, json, math, shutil, struct, sys
from pathlib import Path
import numpy as np

BASE_N=512
CAPACITY=640
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
    p=np.searchsorted(k,nodes); p=np.clip(p,0,len(k)-1); pm=np.maximum(p-1,0)
    choose_prev=np.abs(k[pm]-nodes) < np.abs(k[p]-nodes); idx=np.where(choose_prev,pm,p)
    actual=k[idx]; rel=np.abs(actual-nodes)/np.maximum(np.abs(nodes),np.finfo(np.float64).tiny)
    if np.any(rel>LOOKUP_REL_TOL):
        q=int(np.argmax(rel)); raise FloatingPointError(f'requested shared node absent i={q} rel={rel[q]:.3e}')
    return np.asarray(y[idx],dtype=np.float64),float(np.max(rel))


def cubic_centered(nodes,ynodes,targets):
    t=np.asarray(targets,dtype=np.float64); out=np.full(t.shape,np.nan,dtype=np.float64)
    j=np.searchsorted(nodes,t); valid=(t>0.0)&(j>=2)&(j<=len(nodes)-2)
    if not np.any(valid): return out,valid
    jj=j[valid]; xt=np.log(t[valid]); inds=np.stack((jj-2,jj-1,jj,jj+1),axis=1)
    xs=np.log(nodes[inds]); ys=ynodes[inds]; vv=np.zeros(len(xt),dtype=np.float64)
    for a in range(4):
        w=np.ones(len(xt),dtype=np.float64)
        for b in range(4):
            if a!=b: w *= (xt-xs[:,b])/(xs[:,a]-xs[:,b])
        vv += ys[:,a]*w
    out[valid]=vv
    return out,valid


class GeometrySuite:
    audit={}
    stream=None
    total=0
    min_k=math.inf
    max_k=-math.inf
    def __init__(self,baseline,precision,kpd):
        self.kpd=float(kpd); self.kkeys=set(); self.models=[]
        self.rec=self.audit.setdefault(format(self.kpd,'.17g'),{'response_calls':0,'target_evaluations':0,'min_target_k':None,'max_target_k':None})
    @classmethod
    def reset(cls):
        cls.audit={}; cls.stream=hashlib.sha256(); cls.total=0; cls.min_k=math.inf; cls.max_k=-math.inf
    def response(self,z,targets):
        t=np.asarray(targets,dtype=np.float64)
        call=int(self.rec['response_calls'])
        if t.size:
            mn=float(np.min(t)); mx=float(np.max(t));
            self.rec['min_target_k']=mn if self.rec['min_target_k'] is None else min(self.rec['min_target_k'],mn)
            self.rec['max_target_k']=mx if self.rec['max_target_k'] is None else max(self.rec['max_target_k'],mx)
            GeometrySuite.min_k=min(GeometrySuite.min_k,mn); GeometrySuite.max_k=max(GeometrySuite.max_k,mx)
            for i,x in enumerate(t): GeometrySuite.stream.update(struct.pack('>dQQd',self.kpd,call,int(i),float(x)))
        self.rec['response_calls']+=1; self.rec['target_evaluations']+=int(t.size); GeometrySuite.total+=int(t.size)
        return np.ones((t.size,2),dtype=np.float64)
    def close(self): pass


class GuardedCubicSuite:
    audit={}
    nodes_global=None
    def __init__(self,baseline,precision,kpd):
        from classy import Class
        if self.nodes_global is None: raise RuntimeError('guard lattice not frozen at runtime')
        self.kpd=float(kpd); self.models=[]; self.kkeys=set(); self.nodes=np.asarray(self.nodes_global,dtype=np.float64)
        rec=self.audit.setdefault(format(self.kpd,'.17g'),{'response_calls':0,'target_evaluations':0,'unsupported_target_evaluations':0,'max_requested_node_coordinate_rel_mismatch':0.0})
        self.rec=rec
        for alpha,beta in ((0.0,0.0),(-H,0.0),(0.0,H),(0.0,-H)):
            c=Class(); c.set(class_params(baseline,precision,alpha,beta,self.kpd,self.nodes)); c.compute(['transfer']); self.models.append(c)
    def response(self,z,targets):
        t=np.asarray(targets,dtype=np.float64); vals=[]; valid_ref=None
        for c in self.models:
            tk=c.get_transfer(z=float(z),output_format='class'); dm=[q for q in tk if q.strip()=='d_m']
            if len(dm)!=1: raise AssertionError(f'expected exact d_m key, got {list(tk)}')
            kkey=None; scale=None
            for q in tk:
                s=q.lower().replace(' ','')
                if s in {'k(h/mpc)','k[h/mpc]','k_h/mpc'} or ('k' in s and 'h/mpc' in s): kkey=q; scale=float(c.h()); break
                if s in {'k(1/mpc)','k[1/mpc]'} or ('k' in s and '1/mpc' in s): kkey=q; scale=1.0; break
            if kkey is None: raise AssertionError('unrecognized CLASS k key')
            self.kkeys.add(kkey); k=np.asarray(tk[kkey],dtype=np.float64)*scale; y=np.asarray(tk[dm[0]],dtype=np.float64)
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


def build_guard_lattice(min_target,max_target):
    base=np.geomspace(KMIN,KMAX,BASE_N,dtype=np.float64); r=np.float64(base[1]/base[0])
    nlo=nhi=0
    def make(lo,hi):
        lower=np.asarray([np.float64(base[0]/(r**m)) for m in range(lo,0,-1)],dtype=np.float64)
        upper=np.asarray([np.float64(base[-1]*(r**m)) for m in range(1,hi+1)],dtype=np.float64)
        return np.concatenate((lower,base,upper))
    def valid(nodes,k):
        j=int(np.searchsorted(nodes,np.float64(k))); return bool(k>0.0 and j>=2 and j<=len(nodes)-2)
    nodes=make(nlo,nhi)
    while not valid(nodes,min_target):
        nlo+=1
        if BASE_N+nlo+nhi>CAPACITY: raise RuntimeError('lower guard capacity exceeded')
        nodes=make(nlo,nhi)
    while not valid(nodes,max_target):
        nhi+=1
        if BASE_N+nlo+nhi>CAPACITY: raise RuntimeError('upper guard capacity exceeded')
        nodes=make(nlo,nhi)
    if not (valid(nodes,min_target) and valid(nodes,max_target)): raise AssertionError('guard extrema remain unsupported')
    if not np.array_equal(nodes[nlo:nlo+BASE_N],base): raise AssertionError('base lattice identity changed')
    return nodes,r,nlo,nhi


def ir_argv(a,common,scratch,out):
    argv=['exp073ir']
    for x in common:
        val=scratch if x=='scratch' else getattr(a,x.replace('-','_'))
        argv += ['--'+x,str(val)]
    argv += ['--out',str(out)]
    return argv


def run_ir(ir,a,common,scratch,out,suite):
    ir.ResponseSuite=suite; old=sys.argv; sys.argv=ir_argv(a,common,scratch,out)
    try: rc=ir.main()
    finally: sys.argv=old
    if rc!=0 or not Path(out).exists(): raise RuntimeError('inner Exp073IR traversal failed')
    return json.loads(Path(out).read_text())


def main():
    ap=argparse.ArgumentParser()
    common=['parent-root','parent-authority','manifest','angular-root','expim-root','boss-root','source','lens','camb-root','expz2-script','exp073iq-script','baseline','precision','scratch']
    for x in common: ap.add_argument('--'+x,required=True)
    ap.add_argument('--ir-script',required=True); ap.add_argument('--capacity-patch-record',required=True); ap.add_argument('--out',required=True)
    a=ap.parse_args(); patch=json.loads(Path(a.capacity_patch_record).read_text())
    if patch.get('old_capacity')!=30 or patch.get('new_capacity')!=CAPACITY or patch.get('replacement_count')!=1: raise SystemExit('invalid k-output capacity patch record')
    if patch.get('parser_old_argument_capacity')!=1024 or patch.get('parser_new_argument_capacity')!=32768 or patch.get('parser_replacement_count')!=1: raise SystemExit('invalid parser capacity patch record')
    ir=import_module('exp073ir_guard_parent',a.ir_script)
    if ir.H!=H or ir.REL_TOL!=REL_TOL or ir.KMAX!=KMAX or ir.ZMIN!=0.295 or ir.ZMAX!=2.33: raise SystemExit('Exp073IR frozen constants mismatch')

    # Phase A: exact inherited target traversal, response-blind.
    GeometrySuite.reset(); geom_scratch=Path(a.scratch)/'geometry'; geom_out=geom_scratch/'geometry_inner.json'; geom_scratch.mkdir(parents=True,exist_ok=True)
    gd=run_ir(ir,a,common,geom_scratch,geom_out,GeometrySuite)
    if gd.get('covariance_read') is not False or gd.get('whitening_read') is not False or gd.get('nuisance_read') is not False or gd.get('relation_null_read') is not False: raise SystemExit('forbidden downstream quantity read in geometry phase')
    gp=gd.get('parent',{}); exact_parent_geom=(gp.get('retained_count')==107 and gp.get('retained_id_sha256')==ir.PARENT_RETAINED_SHA and gp.get('full_order_sha256')==ir.FULL_ORDER_SHA)
    if not exact_parent_geom or GeometrySuite.total<=0 or not math.isfinite(GeometrySuite.min_k) or not math.isfinite(GeometrySuite.max_k): raise SystemExit('invalid geometry phase')
    nodes,r,nlo,nhi=build_guard_lattice(GeometrySuite.min_k,GeometrySuite.max_k)
    # Extrema are sufficient for monotone searchsorted stencil support; verify every observed bound per kpd too.
    for rec in GeometrySuite.audit.values():
        for k in (rec['min_target_k'],rec['max_target_k']):
            j=int(np.searchsorted(nodes,np.float64(k)))
            if not (k>0.0 and j>=2 and j<=len(nodes)-2): raise SystemExit('geometry exhaustive-bound check failed')
    geom_summary={
      'stream_encoding':'>dQQd big-endian: kpd_float64, response_call_ordinal_uint64, target_index_uint64, target_k_float64',
      'stream_sha256':GeometrySuite.stream.hexdigest(),'total_target_evaluations':GeometrySuite.total,'min_target_k':GeometrySuite.min_k,'max_target_k':GeometrySuite.max_k,
      'by_kpd':GeometrySuite.audit,'base_node_count':BASE_N,'base_k_min':KMIN,'base_k_max':KMAX,'base_ratio_binary64':float(r),
      'lower_guard_count':nlo,'upper_guard_count':nhi,'extended_node_count':int(len(nodes)),'extended_k_min':float(nodes[0]),'extended_k_max':float(nodes[-1]),
      'base_lattice_preserved_bitwise':bool(np.array_equal(nodes[nlo:nlo+BASE_N],np.geomspace(KMIN,KMAX,BASE_N,dtype=np.float64))),
      'post_guard_unsupported_extrema':0
    }
    shutil.rmtree(geom_scratch,ignore_errors=True)

    # Phase B: same inherited full-support response audit on geometry-derived guarded lattice.
    GuardedCubicSuite.nodes_global=nodes; GuardedCubicSuite.audit={}
    resp_scratch=Path(a.scratch)/'response'; inner=resp_scratch/'exp073ji_inner_ir.json'; resp_scratch.mkdir(parents=True,exist_ok=True)
    d=run_ir(ir,a,common,resp_scratch,inner,GuardedCubicSuite)
    if d.get('covariance_read') is not False or d.get('whitening_read') is not False or d.get('nuisance_read') is not False or d.get('relation_null_read') is not False: raise SystemExit('forbidden downstream quantity read')
    parent=d.get('parent',{}); layer=d.get('layer_b',{}); conv=d.get('convergence',{}); audit=GuardedCubicSuite.audit
    unsupported=sum(int(v.get('unsupported_target_evaluations',0)) for v in audit.values())
    exact_parent=(parent.get('retained_count')==107 and parent.get('retained_id_sha256')==ir.PARENT_RETAINED_SHA and parent.get('full_order_sha256')==ir.FULL_ORDER_SHA)
    feasible=bool(exact_parent and unsupported==0 and conv.get('finite_nonzero_status_changed') is False and conv.get('row_label_changed') is False and conv.get('boss_dense_z_disagreement') is False and isinstance(conv.get('max_relative_component_difference'),(int,float)) and math.isfinite(conv['max_relative_component_difference']) and conv['max_relative_component_difference']<REL_TOL and layer.get('invalid_row_fraction',1.0)<=ir.FB_MAX and layer.get('retained_after_layer_b',0)>=ir.MIN_RETAINED)
    classification='GUARD_NODE_FULL_SUPPORT_FEASIBLE_PLUS_0_PLUS_0' if feasible else 'GUARD_NODE_FULL_SUPPORT_NOT_FEASIBLE_PLUS_0_PLUS_0'
    result={
      'schema':'EXP073JI_ARTICLE3_LAYERB_GEOMETRY_DERIVED_GUARD_NODE_FEASIBILITY_RESULT_V0_1','experiment':'Exp073JI','classification':classification,'effect':'+0/+0',
      'scientific_authority_created':False,'covariance_restriction_authorized':False,'architecture':'GEOMETRY_DERIVED_GUARDED_SHARED_PHYSICAL_K_CUBIC_CENTERED_LN_K_V0_1',
      'h':H,'rel_tol':REL_TOL,'geometry':geom_summary,'capacity_ceiling':CAPACITY,'parent_identity_preserved':exact_parent,'response_engine_audit':audit,
      'unsupported_target_evaluations':unsupported,'inner_status_for_accounting_only':d.get('status'),'inner_covariance_authorization_ignored':bool(d.get('covariance_restriction_authorized',False)),
      'convergence':conv,'layer_b':layer,'native_transfer_k_keys':d.get('native_transfer_k_keys',[]),
      'token':'PASS_EXP073JI_GUARD_NODE_FULL_SUPPORT_FEASIBLE_V0_1' if feasible else 'PASS_EXP073JI_GUARD_NODE_FULL_SUPPORT_NOT_FEASIBLE_V0_1'
    }
    Path(a.out).parent.mkdir(parents=True,exist_ok=True); Path(a.out).write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(result['token']); print('GUARDS',nlo,nhi,'NODES',len(nodes),'RANGE',nodes[0],nodes[-1]); print('GEOMETRY',json.dumps(geom_summary,sort_keys=True)); print('UNSUPPORTED_TARGET_EVALUATIONS',unsupported); print('CONVERGENCE',json.dumps(conv,sort_keys=True)); print('LAYER_B',json.dumps(layer,sort_keys=True)); print('RESPONSE_ENGINE_AUDIT',json.dumps(audit,sort_keys=True))
    return 0

if __name__=='__main__': raise SystemExit(main())
