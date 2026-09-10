#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, math
from pathlib import Path
import numpy as np

H=1e-4
REL_TOL_REFERENCE=1e-3
LOOKUP_REL_TOL=1e-12
KPDS=(10.0,20.0)
PROBES=(("alpha_left",0.7000000000000001,0.002502504647141259),("beta_symmetric",0.9351,0.01860440444314368))
MODELS=(("ref",0.0,0.0),("alpha_left",-H,0.0),("beta_plus",0.0,H),("beta_minus",0.0,-H))
TARGETS=tuple(p[2] for p in PROBES)

def parse_kv(path):
    out={}
    for raw in Path(path).read_text().splitlines():
        s=raw.strip()
        if not s or s.startswith('#') or '=' not in s: continue
        k,v=s.split('=',1); k=k.strip(); v=v.split('#',1)[0].strip()
        if k and v: out[k]=v
    return out

def params(baseline,precision,alpha,beta,kpd):
    d=parse_kv(baseline); d.update(parse_kv(precision))
    for k in ['root','headers','write background','write thermodynamics','write primordial']: d.pop(k,None)
    d['alpha_idm_iv']=format(alpha,'.17g'); d['beta_idm_iv']=format(beta,'.17g')
    d['output']='mTk'; d['z_pk']='2.34'; d['P_k_max_h/Mpc']='0.25'; d['k_per_decade_for_pk']=format(kpd,'.17g')
    d['k_output_values']=','.join(format(x,'.17g') for x in TARGETS)
    return d

def exact_dm_record(c,z,target):
    tk=c.get_transfer(z=float(z),output_format='class')
    dm=[k for k in tk if k.strip()=='d_m']
    if len(dm)!=1: raise AssertionError(f'expected exact d_m key, got {list(tk)}')
    kkey=None; scale=None
    for key in tk:
        kl=key.lower().replace(' ','')
        if kl in {'k(h/mpc)','k[h/mpc]','k_h/mpc'} or ('k' in kl and 'h/mpc' in kl):
            kkey=key; scale=float(c.h()); break
        if kl in {'k(1/mpc)','k[1/mpc]'} or ('k' in kl and '1/mpc' in kl):
            kkey=key; scale=1.0; break
    if kkey is None: raise AssertionError('unrecognized CLASS k key')
    k=np.asarray(tk[kkey],dtype=np.float64)*scale
    y=np.asarray(tk[dm[0]],dtype=np.float64)
    if k.ndim!=1 or y.shape!=k.shape or len(k)<4 or np.any(~np.isfinite(k)) or np.any(~np.isfinite(y)) or np.any(k<=0) or np.any(np.diff(k)<=0):
        raise AssertionError('invalid transfer table')
    idx=int(np.argmin(np.abs(k-np.float64(target))))
    k_actual=float(k[idx]); abs_mismatch=float(abs(k_actual-target)); rel_mismatch=float(abs_mismatch/max(abs(target),np.finfo(np.float64).tiny))
    if rel_mismatch>LOOKUP_REL_TOL:
        raise FloatingPointError(f'exact injected k not found: target={target:.17g} actual={k_actual:.17g} rel={rel_mismatch:.17g}')
    return {
        'native_count':int(len(k)),
        'native_k_key':kkey,
        'native_k_min':float(k[0]),
        'native_k_max':float(k[-1]),
        'injected_index':idx,
        'target_k_mpc_inv':float(target),
        'actual_k_mpc_inv':k_actual,
        'coordinate_abs_mismatch':abs_mismatch,
        'coordinate_rel_mismatch':rel_mismatch,
        'lookup_rel_tol':LOOKUP_REL_TOL,
        'direct_dm':float(y[idx]),
    }

def rel(a,b):
    if not (math.isfinite(a) and math.isfinite(b) and a>0 and b>0): return None
    return abs(a-b)/max(abs(a),abs(b))

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--baseline',required=True); ap.add_argument('--precision',required=True); ap.add_argument('--out',required=True)
    a=ap.parse_args(); from classy import Class
    result={
        'schema':'EXP073JD_ARTICLE3_LAYERB_EXACT_K_INJECTION_ORIGINAL_PAIR_RESULT_V0_1',
        'experiment':'Exp073JD',
        'classification':'INVALID_INFRA_PLUS_0_PLUS_0',
        'h':H,
        'historical_rel_tol_reference':REL_TOL_REFERENCE,
        'lookup_rel_tol':LOOKUP_REL_TOL,
        'k_per_decade_ladder':list(KPDS),
        'k_output_values_mpc_inv':list(TARGETS),
        'probes':{},
        'scientific_authority_created':False,
        'covariance_restriction_authorized':False,
        'effect':'+0/+0',
        'interpolation_in_k_used':False,
    }
    try:
        for kpd in KPDS:
            cs={}
            try:
                for name,alpha,beta in MODELS:
                    c=Class(); c.set(params(a.baseline,a.precision,alpha,beta,kpd)); c.compute(['transfer']); cs[name]=c
                for component,z,target in PROBES:
                    rec=result['probes'].setdefault(component,{'z':z,'k_mpc_inv':target,'by_kpd':{}})
                    raw={}
                    for name,_,_ in MODELS:
                        raw[name]=exact_dm_record(cs[name],z,target)
                    if component=='alpha_left':
                        signed=(raw['alpha_left']['direct_dm']-raw['ref']['direct_dm'])/(-H)
                    else:
                        signed=(raw['beta_plus']['direct_dm']-raw['beta_minus']['direct_dm'])/(2*H)
                    rec['by_kpd'][format(kpd,'.17g')]={
                        'models':raw,
                        'signed_exact_k_response':float(signed),
                        'exact_k_response':float(abs(signed)),
                    }
            finally:
                for c in cs.values():
                    try: c.struct_cleanup()
                    except Exception: pass
        all_below=True
        for component,_,_ in PROBES:
            rec=result['probes'][component]
            r={float(k):v['exact_k_response'] for k,v in rec['by_kpd'].items()}
            d=rel(r[10.0],r[20.0])
            rec['exact_k_10_to_20_relative_difference']=d
            rec['below_historical_rel_tol_reference']=(d is not None and d<REL_TOL_REFERENCE)
            all_below=all_below and bool(rec['below_historical_rel_tol_reference'])
        result['all_probes_below_historical_rel_tol_reference']=all_below
        result['classification']='EXACT_K_ORIGINAL_PAIR_OBSERVED_PLUS_0_PLUS_0'
        result['token']='PASS_EXP073JD_EXACT_K_ORIGINAL_PAIR_OBSERVED_V0_1'
    except Exception as e:
        result['error']=repr(e); result['token']='INVALID_EXP073JD_EXACT_K_ORIGINAL_PAIR_V0_1'
    Path(a.out).parent.mkdir(parents=True,exist_ok=True); Path(a.out).write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(result['token']); print(json.dumps(result,sort_keys=True))
    raise SystemExit(0 if result['classification']=='EXACT_K_ORIGINAL_PAIR_OBSERVED_PLUS_0_PLUS_0' else 2)

if __name__=='__main__': main()
