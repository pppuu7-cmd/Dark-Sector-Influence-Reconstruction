#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, math
from pathlib import Path
import numpy as np

H=1e-4
KPDS=(80.0,160.0,320.0,640.0)
PROBES=(("alpha_left",0.7000000000000001,0.002502504647141259),("beta_symmetric",0.9351,0.01860440444314368))
MODELS=(("ref",0.0,0.0),("alpha_left",-H,0.0),("beta_plus",0.0,H),("beta_minus",0.0,-H))

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
    return d

def native(c,z):
    tk=c.get_transfer(z=float(z),output_format='class')
    dm=[k for k in tk if k.strip()=='d_m']
    if len(dm)!=1: raise AssertionError(f'expected exact d_m key, got {list(tk)}')
    kkey=None; scale=None
    for key in tk:
        kl=key.lower().replace(' ','')
        if kl in {'k(h/mpc)','k[h/mpc]','k_h/mpc'} or ('k' in kl and 'h/mpc' in kl): kkey=key; scale=float(c.h()); break
        if kl in {'k(1/mpc)','k[1/mpc]'} or ('k' in kl and '1/mpc' in kl): kkey=key; scale=1.0; break
    if kkey is None: raise AssertionError('unrecognized CLASS k key')
    k=np.asarray(tk[kkey],dtype=np.float64)*scale; y=np.asarray(tk[dm[0]],dtype=np.float64)
    if k.ndim!=1 or y.shape!=k.shape or len(k)<4 or np.any(~np.isfinite(k)) or np.any(~np.isfinite(y)) or np.any(k<=0) or np.any(np.diff(k)<=0): raise AssertionError('invalid native table')
    return k,y,kkey

def interp_record(k,y,t):
    if not (k[0] <= t <= k[-1]): raise FloatingPointError('unbracketed target')
    hi=int(np.searchsorted(k,t,side='left'))
    if hi==0: lo=hi=0
    elif hi==len(k): lo=hi=len(k)-1
    elif k[hi]==t: lo=hi=hi
    else: lo=hi-1
    if lo==hi:
        frac=0.0; val=float(y[lo])
    else:
        frac=float((np.log(t)-np.log(k[lo]))/(np.log(k[hi])-np.log(k[lo])))
        val=float(np.interp(np.log(np.float64(t)),np.log(k),y))
    return {'native_count':int(len(k)),'native_k_min':float(k[0]),'native_k_max':float(k[-1]),'lo_index':lo,'hi_index':hi,'k_lo':float(k[lo]),'k_hi':float(k[hi]),'dm_lo':float(y[lo]),'dm_hi':float(y[hi]),'logk_fraction':frac,'interpolated_dm':val}

def interp_value(k,y,t):
    if not (k[0] <= t <= k[-1]): raise FloatingPointError('unbracketed transport coordinate')
    return float(np.interp(np.log(np.float64(t)),np.log(k),y))

def rel(a,b):
    if not (math.isfinite(a) and math.isfinite(b) and a>0 and b>0): return None
    return abs(a-b)/max(abs(a),abs(b))

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--baseline',required=True); ap.add_argument('--precision',required=True); ap.add_argument('--out',required=True)
    a=ap.parse_args(); from classy import Class
    result={'schema':'EXP073JB_ARTICLE3_LAYERB_COMMON_PHYSICAL_BRACKET_TRANSPORT_RESULT_V0_1','experiment':'Exp073JB','classification':'INVALID_INFRA_PLUS_0_PLUS_0','h':H,'k_per_decade_ladder':list(KPDS),'probes':{},'scientific_authority_created':False,'covariance_restriction_authorized':False,'effect':'+0/+0'}
    try:
        for kpd in KPDS:
            cs={}; tables={}
            try:
                for name,alpha,beta in MODELS:
                    c=Class(); c.set(params(a.baseline,a.precision,alpha,beta,kpd)); c.compute(['transfer']); cs[name]=c
                for component,z,target in PROBES:
                    rec=result['probes'].setdefault(component,{'z':z,'k_mpc_inv':target,'by_kpd':{},'native_adjacent_relative_differences':{},'common_adjacent_relative_differences':{}})
                    raw={}; tables={}
                    for name,_,_ in MODELS:
                        k,y,kkey=native(cs[name],z); tables[name]=(k,y); q=interp_record(k,y,target); q['native_k_key']=kkey; raw[name]=q
                    rr=raw['ref']; klo=rr['k_lo']; khi=rr['k_hi']; frac=rr['logk_fraction']
                    transported={}
                    for name,_,_ in MODELS:
                        k,y=tables[name]
                        vlo=interp_value(k,y,klo); vhi=interp_value(k,y,khi)
                        vtar=float(vlo + frac*(vhi-vlo))
                        transported[name]={'reference_k_lo':klo,'reference_k_hi':khi,'reference_logk_fraction':frac,'transported_dm_lo':vlo,'transported_dm_hi':vhi,'common_bracket_interpolated_dm':vtar}
                    if component=='alpha_left':
                        native_signed=(raw['alpha_left']['interpolated_dm']-raw['ref']['interpolated_dm'])/(-H)
                        common_signed=(transported['alpha_left']['common_bracket_interpolated_dm']-transported['ref']['common_bracket_interpolated_dm'])/(-H)
                    else:
                        native_signed=(raw['beta_plus']['interpolated_dm']-raw['beta_minus']['interpolated_dm'])/(2*H)
                        common_signed=(transported['beta_plus']['common_bracket_interpolated_dm']-transported['beta_minus']['common_bracket_interpolated_dm'])/(2*H)
                    rec['by_kpd'][format(kpd,'.17g')]={'models':raw,'transported_models':transported,'signed_native_response':float(native_signed),'native_response':float(abs(native_signed)),'signed_common_bracket_response':float(common_signed),'common_bracket_response':float(abs(common_signed)),'signed_native_minus_common':float(native_signed-common_signed)}
            finally:
                for c in cs.values():
                    try: c.struct_cleanup()
                    except Exception: pass
        for component,_,_ in PROBES:
            rec=result['probes'][component]
            n={float(k):v['native_response'] for k,v in rec['by_kpd'].items()}; c={float(k):v['common_bracket_response'] for k,v in rec['by_kpd'].items()}
            for x,y in ((80.0,160.0),(160.0,320.0),(320.0,640.0)):
                key=f'{int(x)}_to_{int(y)}'; rec['native_adjacent_relative_differences'][key]=rel(n[x],n[y]); rec['common_adjacent_relative_differences'][key]=rel(c[x],c[y])
        result['classification']='COMMON_BRACKET_TRANSPORT_OBSERVED_PLUS_0_PLUS_0'; result['token']='PASS_EXP073JB_COMMON_BRACKET_TRANSPORT_OBSERVED_V0_1'
    except Exception as e:
        result['error']=repr(e); result['token']='INVALID_EXP073JB_COMMON_BRACKET_TRANSPORT_V0_1'
    Path(a.out).parent.mkdir(parents=True,exist_ok=True); Path(a.out).write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(result['token']); print(json.dumps(result,sort_keys=True))
    raise SystemExit(0 if result['classification']=='COMMON_BRACKET_TRANSPORT_OBSERVED_PLUS_0_PLUS_0' else 2)

if __name__=='__main__': main()
