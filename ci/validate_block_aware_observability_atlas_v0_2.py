#!/usr/bin/env python3
"""Validate DSIR block-aware observability atlas v0.2.

This validator enforces evidence-mask semantics only. It does not infer missing
responses, compute SVD rank, or turn block labels into physical parameters.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ALLOWED={"active","hard_zero","near_null","degenerate","unknown","solver_limited"}
REQUIRED_BLOCKS={"B_AP","G_lowk","tau_lowk","I_kz","S_slip","M_highk","C_dv"}


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--atlas',required=True); ap.add_argument('--json',required=True)
    a=ap.parse_args(); data=json.loads(Path(a.atlas).read_text())
    failures=[]
    if data.get('schema')!='dsir.block_aware_observability_atlas.v0.2': failures.append('schema')
    blocks=set(data.get('blocks',{}))
    if blocks!=REQUIRED_BLOCKS: failures.append('block_set')
    state_counts={s:0 for s in ALLOWED}
    for direction,cells in data.get('directions',{}).items():
        if set(cells)!=REQUIRED_BLOCKS:
            failures.append(f'{direction}:missing_or_extra_blocks')
        for block,cell in cells.items():
            st=cell.get('state');
            if st not in ALLOWED:
                failures.append(f'{direction}:{block}:bad_state'); continue
            state_counts[st]+=1
            if not cell.get('domain'): failures.append(f'{direction}:{block}:missing_domain')
            ev=cell.get('evidence')
            if st in {'active','hard_zero','near_null','degenerate','solver_limited'} and not ev:
                failures.append(f'{direction}:{block}:evidence_required')
            if st=='unknown' and ev is not None:
                failures.append(f'{direction}:{block}:unknown_with_evidence')
            if st=='hard_zero':
                # A hard null must be named as such, never inferred from a tiny scalar.
                if 'chi_I_reference' in cell or 'chi_I_range' in cell:
                    failures.append(f'{direction}:{block}:hard_zero_with_smallness_proxy')
            if st=='near_null' and cell.get('reference')==0:
                failures.append(f'{direction}:{block}:near_null_imputed_zero')
            if st=='degenerate' and not cell.get('degenerate_with'):
                failures.append(f'{direction}:{block}:missing_degenerate_partner')
    # Explicit discipline strings are part of the machine contract.
    discipline=set(data.get('discipline',[]))
    for phrase in ['unknown is never zero','solver_limited is never zero','near_null is not hard_zero']:
        if phrase not in discipline: failures.append('discipline:'+phrase)
    # The current graph must preserve each old hard separator class after adding C4 time evidence.
    seps={e.get('separator') for e in data.get('pairwise_hard_geometry',[])}
    for need in ['M_highk','S_slip','tau_lowk/full k-z']:
        if need not in seps: failures.append('missing_separator:'+need)
    out={
      'schema':'dsir.block_aware_observability_atlas.validation.v0.2',
      'status':'PASS_BLOCK_AWARE_OBSERVABILITY_ATLAS_V0_2' if not failures else 'FAIL_BLOCK_AWARE_OBSERVABILITY_ATLAS_V0_2',
      'failures':failures,
      'direction_count':len(data.get('directions',{})),
      'block_count':len(blocks),
      'state_counts':state_counts,
      'hard_zero_cells':[
        [d,b] for d,cells in data.get('directions',{}).items() for b,c in cells.items() if c.get('state')=='hard_zero'
      ],
      'solver_limited_cells':[
        [d,b] for d,cells in data.get('directions',{}).items() for b,c in cells.items() if c.get('state')=='solver_limited'
      ],
      'unknown_cells':sum(1 for cells in data.get('directions',{}).values() for c in cells.values() if c.get('state')=='unknown'),
      'not_a_claim':[
        'not an intrinsic-rank estimate',
        'not a universal parameter count',
        'not a zero-imputed common response matrix',
        'not survey detectability'
      ]
    }
    Path(a.json).write_text(json.dumps(out,indent=2)+'\n'); print(json.dumps(out,indent=2))
    raise SystemExit(0 if not failures else 2)

if __name__=='__main__': main()
