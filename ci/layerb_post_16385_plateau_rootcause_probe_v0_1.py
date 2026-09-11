#!/usr/bin/env python3
from __future__ import annotations
import argparse,hashlib,importlib.util,json
from pathlib import Path
import numpy as np
H=1e-4
LOOKUP_REL_TOL=1e-12
QIDX=np.asarray([1024,2048,4096,6144,7168],dtype=np.int64)
ZANCH=(float.fromhex('0x1.3851eb851eb85p-1'),float.fromhex('0x1.1c28f5c28f5c3p+0'))
RAW_PASS='POST_16385_FIXED_NODE_RAW_LOCALIZATION_PASS_PLUS_0_PLUS_0'
COND_PASS='POST_16385_FIXED_H_CANCELLATION_AUDIT_PASS_PLUS_0_PLUS_0'
INT_PASS='POST_16385_CANONICAL_INTERPOLATION_CONTROL_PASS_PLUS_0_PLUS_0'
FAIL='POST_16385_PLATEAU_ROOTCAUSE_DIAGNOSTIC_INFRA_FAIL_PLUS_0_PLUS_0'

def load(name,path):
 s=importlib.util.spec_from_file_location(name,Path(path)); m=importlib.util.module_from_spec(s); s.loader.exec_module(m); return m

def sha(a): return hashlib.sha256(np.ascontiguousarray(a,dtype='<f8').tobytes()).hexdigest()

def nearest_indices(nodes,targets):
 p=np.searchsorted(nodes,targets); p=np.clip(p,0,len(nodes)-1); pm=np.maximum(p-1,0); return np.where(np.abs(nodes[pm]-targets)<np.abs(nodes[p]-targets),pm,p)

def common(a):
 jo=load('jo',a.jo_script); jj=load('jj',a.jj_script); rp=load('rp',a.resource_script)
 n8=jo.load_nodes(a.coarse); n16=rp.load_nodes(a.fine)
 if jo.H!=H or jj.H!=H or rp.H!=H or jj.LOOKUP_REL_TOL!=LOOKUP_REL_TOL: raise RuntimeError('frozen constant mismatch')
 if len(n8)!=8193 or len(n16)!=16385: raise RuntimeError('canonical node-count mismatch')
 if np.any(QIDX<=1) or np.any(QIDX>=len(n8)-2): raise RuntimeError('quantile index guard mismatch')
 t=np.ascontiguousarray(n8[QIDX],dtype=np.float64)
 return jo,jj,rp,n8,n16,t

def run_grid(jo,jj,nodes,targets,a,capacity):
 from classy import Class
 jj.CAPACITY=capacity; raw={z:{} for z in ZANCH}; receipts=[]; life={'constructions':0,'live':0,'max_live':0}; unsupported=0; lookup=0.0
 for role,alpha,beta in jo.MODELS:
  c=None; life['constructions']+=1; life['live']+=1; life['max_live']=max(life['max_live'],life['live'])
  try:
   c=Class(); c.set(jj.class_params(Path(a.baseline),Path(a.precision),alpha,beta,nodes)); c.compute(['transfer'])
   rr={'role':role,'z':{}}
   for z in ZANCH:
    v,valid,mx,key=jo.evaluate(jj,c,nodes,z,targets); v=np.ascontiguousarray(v,dtype='<f8'); raw[z][role]=v
    u=int(np.count_nonzero(~valid)); unsupported+=u; lookup=max(lookup,float(mx)); rr['z'][float(z).hex()]={'values':[float(x) for x in v],'sha256':sha(v),'unsupported':u,'max_lookup':float(mx),'k_key':key}
   receipts.append(rr)
  finally:
   if c is not None:
    try:c.struct_cleanup()
    except Exception:pass
   life['live']-=1
 return raw,receipts,life,unsupported,lookup

def numeric(a,lane):
 jo,jj,rp,n8,n16,t=common(a); idx16=nearest_indices(n16,t); maprel=np.abs(n16[idx16]-t)/np.maximum(np.abs(t),np.finfo(float).tiny)
 r8,rec8,l8,u8,m8=run_grid(jo,jj,n8,t,a,9216); r16,rec16,l16,u16,m16=run_grid(jo,jj,n16,t,a,18432)
 base={'effect':'+0/+0','selection_rule':'canonical_8193_indices_[1024,2048,4096,6144,7168]','selected_indices_8193':QIDX.tolist(),'nearest_indices_16385':idx16.tolist(),'selected_k_binary64_hex':[float(x).hex() for x in t],'nearest_16385_k_binary64_hex':[float(x).hex() for x in n16[idx16]],'nearest_16385_relative_coordinate_mismatch':maprel.tolist(),'z_anchors_binary64_hex':[float(z).hex() for z in ZANCH],'h':H,'coarse_node_sha256':jo.NODE_SHA,'fine_node_sha256':rp.NODE_SHA,'lifecycle_8193':l8,'lifecycle_16385':l16,'unsupported_target_evaluations':u8+u16,'max_requested_node_coordinate_rel_mismatch':max(m8,m16),'full_107_row_traversal_executed':False,'scientific_authority_created':False,'next_rung_authorized':False,'covariance_restriction_authorized':False,'Wm_S3_opened':False}
 if l8!={'constructions':4,'live':0,'max_live':1} or l16!={'constructions':4,'live':0,'max_live':1} or u8+u16!=0 or max(m8,m16)>LOOKUP_REL_TOL: raise RuntimeError('structural execution mismatch')
 if lane=='raw':
  dif={}; mx=0.0
  for z in ZANCH:
   zk=float(z).hex(); dif[zk]={}
   for role,_,_ in jo.MODELS:
    x=r8[z][role]; y=r16[z][role]; d=np.abs(x-y); den=np.maximum(np.maximum(np.abs(x),np.abs(y)),np.finfo(float).tiny); rel=d/den; mx=max(mx,float(np.max(rel)))
    dif[zk][role]={'8193_values':x.tolist(),'16385_values':y.tolist(),'abs_difference':d.tolist(),'symmetric_relative_difference':rel.tolist(),'max_symmetric_relative_difference':float(np.max(rel)),'8193_sha256':sha(x),'16385_sha256':sha(y)}
  return base|{'schema':'LAYERB_POST_16385_FIXED_NODE_RAW_LOCALIZATION_V0_1','classification':RAW_PASS,'raw_differences':dif,'max_raw_symmetric_relative_difference':mx,'model_receipts_8193':rec8,'model_receipts_16385':rec16,'token':RAW_PASS}
 out={}; maxamp=0.0
 for label,raw in [('8193',r8),('16385',r16)]:
  out[label]={}
  for z in ZANCH:
   ref,am,bp,bm=(raw[z][r] for r in ('reference','alpha_minus','beta_plus','beta_minus')); na=am-ref; nb=bp-bm; ra=np.abs(na/(-H)); rb=np.abs(nb/(2*H)); sa=np.maximum(np.maximum(np.abs(am),np.abs(ref)),np.finfo(float).tiny); sb=np.maximum(np.maximum(np.abs(bp),np.abs(bm)),np.finfo(float).tiny); ca=np.abs(na)/sa; cb=np.abs(nb)/sb; aa=1.0/np.maximum(ca,np.finfo(float).tiny); ab=1.0/np.maximum(cb,np.finfo(float).tiny); maxamp=max(maxamp,float(max(np.max(aa),np.max(ab))))
   out[label][float(z).hex()]={'alpha_numerator':na.tolist(),'beta_numerator':nb.tolist(),'alpha_denominator':H,'beta_denominator':2*H,'alpha_response':ra.tolist(),'beta_response':rb.tolist(),'alpha_cancellation_ratio':ca.tolist(),'beta_cancellation_ratio':cb.tolist(),'alpha_amplification_indicator':aa.tolist(),'beta_amplification_indicator':ab.tolist()}
 return base|{'schema':'LAYERB_POST_16385_FIXED_H_CANCELLATION_AUDIT_V0_1','classification':COND_PASS,'conditioning':out,'max_cancellation_amplification_indicator':maxamp,'alternative_h_evaluated':False,'token':COND_PASS}

def interpolation(a):
 jo,jj,rp,n8,n16,t=common(a); idx16=nearest_indices(n16,t); exact_global=int(np.intersect1d(n8.view('<u8'),n16.view('<u8')).size); exact_selected=bool(np.array_equal(n16[idx16].view('<u8'),t.view('<u8'))); j8=np.searchsorted(n8,t); j16=np.searchsorted(n16,t)
 stencils=[]
 for q,i8,i16 in zip(t,j8,j16):
  s8=n8[i8-2:i8+2]; s16=n16[i16-2:i16+2]; stencils.append({'target_binary64_hex':float(q).hex(),'8193_stencil':[float(x).hex() for x in s8],'16385_stencil':[float(x).hex() for x in s16],'stencil_binary64_identical':bool(np.array_equal(s8.view('<u8'),s16.view('<u8')))})
 funcs={'log_cubic':lambda x:1.0+0.2*np.log(x)-0.03*np.log(x)**2+0.004*np.log(x)**3,'smooth':lambda x:np.sin(0.7*np.log(x))+0.1*np.cos(1.3*np.log(x))}; controls={}; mx=0.0
 for name,f in funcs.items():
  y8=f(n8); y16=f(n16); v8,ok8=jj.cubic_centered(n8,y8,t); v16,ok16=jj.cubic_centered(n16,y16,t); truth=f(t)
  if not(np.all(ok8)&np.all(ok16)): raise RuntimeError('selected interpolation target unsupported')
  e8=np.abs(v8-truth); e16=np.abs(v16-truth); cross=np.abs(v8-v16); mx=max(mx,float(np.max(cross))); controls[name]={'8193_abs_residual':e8.tolist(),'16385_abs_residual':e16.tolist(),'cross_grid_abs_difference':cross.tolist(),'max_8193_abs_residual':float(np.max(e8)),'max_16385_abs_residual':float(np.max(e16)),'max_cross_grid_abs_difference':float(np.max(cross))}
 return {'schema':'LAYERB_POST_16385_CANONICAL_INTERPOLATION_CONTROL_V0_1','classification':INT_PASS,'effect':'+0/+0','exact_full_array_every_other_nesting':bool(len(n16[::2])==len(n8) and np.array_equal(n8.view('<u8'),n16[::2].view('<u8'))),'exact_binary64_shared_node_count':exact_global,'exact_selected_target_membership_in_16385':exact_selected,'selection_rule':'canonical_8193_indices_[1024,2048,4096,6144,7168]','selected_indices_8193':QIDX.tolist(),'nearest_indices_16385':idx16.tolist(),'selected_k_binary64_hex':[float(x).hex() for x in t],'nearest_16385_relative_coordinate_mismatch':(np.abs(n16[idx16]-t)/np.maximum(np.abs(t),np.finfo(float).tiny)).tolist(),'centered_cubic_stencils':stencils,'controls':controls,'max_cross_grid_control_difference':mx,'science_result_read':False,'class_solver_invoked':False,'scientific_authority_created':False,'next_rung_authorized':False,'covariance_restriction_authorized':False,'Wm_S3_opened':False,'token':INT_PASS}

def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--lane',choices=['raw','conditioning','interpolation'],required=True)
 for x in ('resource-script','coarse','fine','jo-script','jj-script','baseline','precision','out'): ap.add_argument('--'+x,required=True)
 a=ap.parse_args(); p=Path(a.out)
 try:r=interpolation(a) if a.lane=='interpolation' else numeric(a,a.lane)
 except Exception as e:r={'schema':'LAYERB_POST_16385_PLATEAU_ROOTCAUSE_DIAGNOSTIC_V0_1','classification':FAIL,'effect':'+0/+0','lane':a.lane,'error':f'{type(e).__name__}: {e}','scientific_authority_created':False,'next_rung_authorized':False,'covariance_restriction_authorized':False,'Wm_S3_opened':False,'token':FAIL}
 p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(r,indent=2,sort_keys=True)+'\n'); print(r['token']); return 0
if __name__=='__main__': raise SystemExit(main())
