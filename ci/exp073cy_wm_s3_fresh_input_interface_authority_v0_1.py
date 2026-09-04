#!/usr/bin/env python3
from __future__ import annotations
import json, subprocess, sys
from pathlib import Path

S3='3996f2bacf29d46278773530058d4f5666c0d590bf6cebc06459659166bc60ec'
LENS='DES_Y1A1_3x2pt_redMaGiC_MASK_HPIX4096RING.fits'
EDGES='[0,30,60,90,120,150,180,210,240,272,309,351,398,452,513,582,661,750,852,967,1098,1247,1416,1608,1826,2073,2354,2673,3035,3446,3914,4444,5047,5731,6508,7390,8392,9529,10821,12288]'
BOUND=['fresh_masks_complete','fresh_workspace_mcm_complete','mcm_fits_verified','full_window_complete','selected_te_complete','replica_receipt_complete']
TERMS={'s3_sha':S3,'lens_filename':LENS,'nmtfield':'NmtField','write_to':'write_to(','te_select':'TE<-TE'}

def tracked_text():
    files=subprocess.check_output(['git','ls-files','-z']).split(b'\0')
    for b in files:
        if not b: continue
        p=Path(b.decode())
        try:
            raw=p.read_bytes()
            if b'\0' in raw[:8192]: continue
            yield str(p),raw.decode('utf-8','ignore')
        except Exception:
            continue

def main():
    out=Path(sys.argv[1]); head=subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip()
    texts=list(tracked_text()); hits={k:[] for k in TERMS}
    for path,text in texts:
        for k,t in TERMS.items():
            if t in text: hits[k].append(path)
    boundary_hits={b:[] for b in BOUND}
    edge_hits=[]
    for path,text in texts:
        if EDGES in text: edge_hits.append(path)
        for b in BOUND:
            if b in text: boundary_hits[b].append(path)
    exact_inputs=bool(hits['s3_sha']) and bool(hits['lens_filename'])
    interfaces=bool(hits['nmtfield']) and bool(hits['write_to']) and bool(edge_hits) and all(boundary_hits[b] for b in BOUND)
    if exact_inputs and interfaces: status='Y1_FRESH_INPUT_INTERFACE_AUTHORITY_COMPLETE'
    elif exact_inputs: status='Y2_FRESH_INPUT_AUTHORITY_FOUND_INTERFACE_GAP'
    else: status='Y3_FRESH_INPUT_AUTHORITY_INCOMPLETE'
    r={'schema':'dsir.exp073cy.wm_s3.fresh_input_interface_authority.v0.1','status':status,'accounting':'+0/+0','science_gate_scored':False,'wm_s3_authority_created':False,'exp073bu_activated':False,'source_head':head,'hits':hits,'edge_hits':edge_hits,'boundary_hits':boundary_hits,'exact_inputs_found':exact_inputs,'interfaces_found':interfaces}
    out.parent.mkdir(parents=True,exist_ok=True); out.write_text(json.dumps(r,indent=2,sort_keys=True)+'\n')
    print(status); print(json.dumps(r,indent=2,sort_keys=True)); return 0
if __name__=='__main__': raise SystemExit(main())
