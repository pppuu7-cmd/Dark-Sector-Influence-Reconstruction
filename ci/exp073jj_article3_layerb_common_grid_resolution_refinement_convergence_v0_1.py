#!/usr/bin/env python3
from __future__ import annotations
import argparse, importlib.util, json, math, sys
from pathlib import Path
import numpy as np

KMIN=1e-4
KMAX=0.06664762008318016
H=1e-4
REL_TOL=1e-3
LOOKUP_REL_TOL=1e-12
CAPACITY=1152
NATIVE_KPD=20.0
TARGET_MIN=0.00033800000000000003
TARGET_MAX=0.06664596609379447
JI_GEOM_SHA='79bae6f3015ccf524402d7f0f357070a903126bfa8d3bd3f4cac5902afef093a'


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


def class_params(baseline,precision,alpha,beta,nodes):
    d=parse_kv(baseline); d.update(parse_kv(precision))
    for k in ['root','headers','write background','write thermodynamics','write primordial']: d.pop(k,None)
    d['alpha_idm_iv']=format(alpha,'.17g'); d['beta_idm_iv']=format(beta,'.17g')
    d['output']='mTk'; d['z_pk']='2.34'; d['P_k_max_h/Mpc']='0.25'
    d['k_per_decade_for_pk']=format(NATIVE_KPD,'.17g')
    d['k_output_values']=','.join(format(float(x),'.17g') for x in nodes)
    return d


def requested_values(k,y,nodes):
    p=np.searchsorted(k,nodes); p=np.clip(p,0,len(k)-1); pm=np.maximum(p-1,0)
    idx=np.where(np.abs(k[pm]-nodes)<np.abs(k[p]-nodes),pm,p)
    actual=k[idx]; rel=np.abs(actual-nodes)/np.maximum(np.abs(nodes),np.finfo(np.float64).tiny)
    if np.any(rel>LOOKUP_REL_TOL):
        q=int(np.argmax(rel)); raise FloatingPointError(f'requested shared node absent i={q} rel={rel[q]:.3e}')
    return np.asarray(y[idx],dtype=np.float64),float(np.max(rel))


def cubic_centered(nodes,ynodes,targets):
    t=np.asarray(targets,dtype=np.float64); out=np.full(t.shape,np.nan,dtype=np.float64)
    j=np.searchsorted(nodes,t); valid=(t>0.0)&(j>=2)&(j<=len(nodes)-2)
    if np.any(valid):
        jj=j[valid]; xt=np.log(t[valid]); inds=np.stack((jj-2,jj-1,jj,jj+1),axis=1)
        xs=np.log(nodes[inds]); ys=ynodes[inds]; vv=np.zeros(len(xt),dtype=np.float64)
        for a in range(4):
            w=np.ones(len(xt),dtype=np.float64)
            for b in range(4):
                if a!=b: w *= (xt-xs[:,b])/(xs[:,a]-xs[:,b])
            vv += ys[:,a]*w
        out[valid]=vv
    return out,valid


def guarded_lattice(n):
    base=np.geomspace(KMIN,KMAX,n,dtype=np.float64); r=np.float64(base[1]/base[0])
    nlo=nhi=0
    def make(lo,hi):
        lower=np.asarray([np.float64(base[0]/(r**m)) for m in range(lo,0,-1)],dtype=np.float64)
        upper=np.asarray([np.float64(base[-1]*(r**m)) for m in range(1,hi+1)],dtype=np.float64)
        return np.concatenate((lower,base,upper))
    def valid(nodes,k):
        j=int(np.searchsorted(nodes,np.float64(k))); return bool(k>0.0 and j>=2 and j<=len(nodes)-2)
    nodes=make(0,0)
    while not valid(nodes,TARGET_MIN): nlo+=1; nodes=make(nlo,nhi)
    while not valid(nodes,TARGET_MAX): nhi+=1; nodes=make(nlo,nhi)
    if n+nlo+nhi>CAPACITY: raise RuntimeError('capacity exceeded')
    if not (valid(nodes,TARGET_MIN) and valid(nodes,TARGET_MAX)): raise AssertionError('guard support failed')
    if not np.array_equal(nodes[nlo:nlo+n],base): raise AssertionError('base lattice identity changed')
    return nodes,r,nlo,nhi


class ResolutionSuite:
    audit={}
    coarse_nodes=None
    fine_nodes=None
    def __init__(self,baseline,precision,kpd):
        from classy import Class
        self.slot=float(kpd); self.kkeys=set(); self.models=[]
        if self.slot==10.0: self.nodes=np.asarray(self.coarse_nodes,dtype=np.float64); label='coarse'
        elif self.slot==20.0: self.nodes=np.asarray(self.fine_nodes,dtype=np.float64); label='fine'
        else: raise RuntimeError(f'unexpected inherited suite slot {self.slot}')
        self.rec=self.audit.setdefault(format(self.slot,'.17g'),{'slot_role':label,'native_k_per_decade_for_pk':NATIVE_KPD,'requested_node_count':int(len(self.nodes)),'response_calls':0,'target_evaluations':0,'unsupported_target_evaluations':0,'max_requested_node_coordinate_rel_mismatch':0.0})
        for alpha,beta in ((0.0,0.0),(-H,0.0),(0.0,H),(0.0,-H)):
            c=Class(); c.set(class_params(baseline,precision,alpha,beta,self.nodes)); c.compute(['transfer']); self.models.append(c)
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


def ir_argv(a,common,scratch,out):
    argv=['exp073ir']
    for x in common:
        val=scratch if x=='scratch' else getattr(a,x.replace('-','_')); argv += ['--'+x,str(val)]
    argv += ['--out',str(out)]; return argv


def run_ir(ir,a,common,scratch,out):
    ir.ResponseSuite=ResolutionSuite; old=sys.argv; sys.argv=ir_argv(a,common,scratch,out)
    try: rc=ir.main()
    finally: sys.argv=old
    if rc!=0 or not Path(out).exists(): raise RuntimeError('inner Exp073IR traversal failed')
    return json.loads(Path(out).read_text())


def main():
    ap=argparse.ArgumentParser(); common=['parent-root','parent-authority','manifest','angular-root','expim-root','boss-root','source','lens','camb-root','expz2-script','exp073iq-script','baseline','precision','scratch']
    for x in common: ap.add_argument('--'+x,required=True)
    ap.add_argument('--ir-script',required=True); ap.add_argument('--ji-authority',required=True); ap.add_argument('--capacity-patch-record',required=True); ap.add_argument('--out',required=True)
    a=ap.parse_args(); ji=json.loads(Path(a.ji_authority).read_text()); patch=json.loads(Path(a.capacity_patch_record).read_text())
    if ji.get('classification')!='GUARD_NODE_FULL_SUPPORT_FEASIBLE_PLUS_0_PLUS_0' or ji.get('artifact_verified_independently') is not True: raise SystemExit('invalid JI authority')
    if ji.get('geometry',{}).get('stream_sha256')!=JI_GEOM_SHA or ji.get('geometry',{}).get('min_target_k')!=TARGET_MIN or ji.get('geometry',{}).get('max_target_k')!=TARGET_MAX: raise SystemExit('JI geometry mismatch')
    if patch.get('old_capacity')!=30 or patch.get('new_capacity')!=CAPACITY or patch.get('replacement_count')!=1: raise SystemExit('invalid k-output capacity patch')
    if patch.get('parser_old_argument_capacity')!=1024 or patch.get('parser_new_argument_capacity')!=32768 or patch.get('parser_replacement_count')!=1: raise SystemExit('invalid parser capacity patch')
    ir=import_module('exp073ir_jj_parent',a.ir_script)
    if ir.H!=H or ir.REL_TOL!=REL_TOL or ir.KMAX!=KMAX or ir.ZMIN!=0.295 or ir.ZMAX!=2.33: raise SystemExit('Exp073IR frozen constants mismatch')
    coarse,r512,l512,u512=guarded_lattice(512); fine,r1024,l1024,u1024=guarded_lattice(1024)
    if (l512,u512,len(coarse))!=(0,1,513) or (l1024,u1024,len(fine))!=(0,1,1025): raise SystemExit('frozen guard construction mismatch')
    ResolutionSuite.coarse_nodes=coarse; ResolutionSuite.fine_nodes=fine; ResolutionSuite.audit={}
    scratch=Path(a.scratch)/'resolution'; out_inner=scratch/'exp073jj_inner_ir.json'; scratch.mkdir(parents=True,exist_ok=True)
    d=run_ir(ir,a,common,scratch,out_inner)
    if any(d.get(k) is not False for k in ('covariance_read','whitening_read','nuisance_read','relation_null_read')): raise SystemExit('forbidden downstream quantity read')
    parent=d.get('parent',{}); layer=d.get('layer_b',{}); conv=d.get('convergence',{}); audit=ResolutionSuite.audit
    exact_parent=(parent.get('retained_count')==107 and parent.get('retained_id_sha256')==ir.PARENT_RETAINED_SHA and parent.get('full_order_sha256')==ir.FULL_ORDER_SHA)
    unsupported=sum(int(v['unsupported_target_evaluations']) for v in audit.values()); lookup=max(float(v['max_requested_node_coordinate_rel_mismatch']) for v in audit.values())
    converged=bool(exact_parent and unsupported==0 and lookup<=LOOKUP_REL_TOL and conv.get('finite_nonzero_status_changed') is False and conv.get('row_label_changed') is False and conv.get('boss_dense_z_disagreement') is False and isinstance(conv.get('max_relative_component_difference'),(int,float)) and math.isfinite(conv['max_relative_component_difference']) and conv['max_relative_component_difference']<REL_TOL and layer.get('invalid_row_fraction',1.0)<=ir.FB_MAX and layer.get('retained_after_layer_b',0)>=ir.MIN_RETAINED)
    classification='COMMON_GRID_RESOLUTION_REFINEMENT_CONVERGED_PLUS_0_PLUS_0' if converged else 'COMMON_GRID_RESOLUTION_REFINEMENT_NOT_CONVERGED_PLUS_0_PLUS_0'
    result={'schema':'EXP073JJ_ARTICLE3_LAYERB_COMMON_GRID_RESOLUTION_REFINEMENT_CONVERGENCE_RESULT_V0_1','experiment':'Exp073JJ','classification':classification,'effect':'+0/+0','scientific_authority_created':False,'covariance_restriction_authorized':False,'h':H,'rel_tol':REL_TOL,'native_k_per_decade_for_pk_frozen':NATIVE_KPD,'inherited_slot_remapping':{'10':'coarse_guarded_C512_513_nodes','20':'fine_guarded_F1024_1025_nodes'},'ji_geometry_stream_sha256':JI_GEOM_SHA,'lattices':{'coarse':{'base_n':512,'ratio_binary64':float(r512),'lower_guard_count':l512,'upper_guard_count':u512,'requested_node_count':len(coarse),'extended_k_min':float(coarse[0]),'extended_k_max':float(coarse[-1])},'fine':{'base_n':1024,'ratio_binary64':float(r1024),'lower_guard_count':l1024,'upper_guard_count':u1024,'requested_node_count':len(fine),'extended_k_min':float(fine[0]),'extended_k_max':float(fine[-1])}},'parent_identity_preserved':exact_parent,'response_engine_audit':audit,'unsupported_target_evaluations':unsupported,'convergence':conv,'layer_b':layer,'inner_status_for_accounting_only':d.get('status'),'inner_covariance_authorization_ignored':bool(d.get('covariance_restriction_authorized',False)),'token':'PASS_EXP073JJ_COMMON_GRID_RESOLUTION_REFINEMENT_CONVERGED_V0_1' if converged else 'PASS_EXP073JJ_COMMON_GRID_RESOLUTION_REFINEMENT_NOT_CONVERGED_V0_1'}
    Path(a.out).parent.mkdir(parents=True,exist_ok=True); Path(a.out).write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(result['token']); print('LATTICES',json.dumps(result['lattices'],sort_keys=True)); print('UNSUPPORTED',unsupported); print('CONVERGENCE',json.dumps(conv,sort_keys=True)); print('LAYER_B',json.dumps(layer,sort_keys=True)); print('AUDIT',json.dumps(audit,sort_keys=True)); return 0

if __name__=='__main__': raise SystemExit(main())
