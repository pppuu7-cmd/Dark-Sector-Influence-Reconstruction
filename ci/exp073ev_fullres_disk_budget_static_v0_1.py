#!/usr/bin/env python3
import json
PASS='PASS_EXP073EV_WW_S0_S1_FULLRES_DISK_BUDGET_STATIC_V0_1'
NPIX=12*4096*4096
LMAX=12287; NL=LMAX+1; NCLS=4; ROWS=NCLS*NL
MCM=ROWS*ROWS*8
NALM=NL*(NL+1)//2
ALM=NALM*16
SELECTED=39*NL*8
FULL=4*39*4*NL*8
FLOOR=50*(2**30)
MIN_MARGIN=10*(2**30)
PEAK=2*MCM+2*ALM+FULL+SELECTED
MARGIN=FLOOR-PEAK
checks={
 'npix':NPIX==201326592,
 'nl':NL==12288,
 'rows':ROWS==49152,
 'mcm_bytes':MCM==19327352832,
 'mcm_exact_18_gib':MCM==18*(2**30),
 'nalm':NALM==75503616,
 'alm_bytes':ALM==1208057856,
 'two_alm_bytes':2*ALM==2416115712,
 'selected_bytes':SELECTED==3833856,
 'full_bpw_bytes':FULL==61341696,
 'floor_bytes':FLOOR==53687091200,
 'margin_at_least_10_gib':MARGIN>=MIN_MARGIN,
}
rec={'experiment':'Exp073EV','classification':'STATIC_RESOURCE_BUDGET_PASS' if all(checks.values()) else 'STATIC_RESOURCE_BUDGET_FAIL','token':PASS if all(checks.values()) else 'FAIL_EXP073EV_WW_S0_S1_FULLRES_DISK_BUDGET_STATIC_V0_1','accounting':'+0/+0','science_gate_scored':False,'ww_authority_created':False,'checks':checks,'bytes':{'npix_mask':NPIX*8,'mcm':MCM,'one_alm':ALM,'two_alms':2*ALM,'full_bpw':FULL,'selected':SELECTED,'conservative_peak':PEAK,'floor_50_gib':FLOOR,'margin':MARGIN,'margin_gib':MARGIN/(2**30)},'model':'2*MCM + 2*ALM + FULL_BPW + SELECTED; require >=10 GiB residual margin'}
print(rec['token']); print(json.dumps(rec,indent=2,sort_keys=True)); open('exp073ev_terminal_receipt.json','w').write(json.dumps(rec,indent=2,sort_keys=True)+'\n')
raise SystemExit(0 if all(checks.values()) else 3)
