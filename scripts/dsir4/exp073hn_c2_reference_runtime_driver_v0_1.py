#!/usr/bin/env python3
import argparse, json
Z=['0.295','0.51','0.706','0.934','1.317','1.491','2.33']
K=['0.00067','0.00201','0.0067','0.0201']
BASELINE='configs/dsir4/c2/ide0_reference_v0_1.ini'
P8='configs/dsir4/c2/dsir_ide_p8_v0_1.pre'
MODEL='reference_alpha0_beta0'

def plan():
    out=[]
    for zi,z in enumerate(Z):
        for ki,k in enumerate(K):
            out.append({'request_id':f'z{zi:02d}k{ki:02d}','z_literal':z,'k_mpc_literal':k,'model_point':MODEL,'baseline':BASELINE,'precision':P8,'invocation':['./class','ide0.ini','dsir_ide_p8.pre'],'diagnostic_env':{'DSIR_C2_EXACT_Z':z},'native_k_output_values':k})
    return out

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--plan-only',action='store_true',required=True); a=ap.parse_args()
    for r in plan(): print(json.dumps(r,separators=(',',':'),sort_keys=True))
if __name__=='__main__': main()
