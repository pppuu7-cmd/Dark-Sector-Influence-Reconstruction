#!/usr/bin/env python3
"""Experiment 052A: exact hard-edge coverage under the Exp051A evidence mask.

This is an observability/discrimination bookkeeping calculation, not a response-rank
estimator. It preserves missing blocks and computes exact minimum hitting sets only
for degeneracy edges that already have hard, pre-frozen separator evidence.
"""
from __future__ import annotations

import argparse
import itertools
import json
from pathlib import Path

BLOCK_MAP = {
    "small_scale_transfer": "M_highk",
    "metric_slip": "S_slip",
    "time_evolution_or_response_sign": "tau_or_full_kz",
}
VALID_STATES = {"active","hard_zero","near_null","degenerate"}


def powerset(items):
    items=sorted(items)
    for r in range(len(items)+1):
        for comb in itertools.combinations(items,r):
            yield set(comb)


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--atlas',required=True)
    ap.add_argument('--edges',required=True)
    ap.add_argument('--json',required=True)
    args=ap.parse_args()
    atlas=json.loads(Path(args.atlas).read_text())
    edges=json.loads(Path(args.edges).read_text())
    failures=[]

    if atlas.get('schema')!='dsir.block_aware_observability_atlas.v0.2': failures.append('atlas_schema')
    if edges.get('schema')!='dsir.discriminant_edges.v0.1': failures.append('edges_schema')

    directions=atlas.get('directions',{})
    # Exp051A stores seven non-reference response directions. C0 is an external
    # response origin in the old hard edge catalogue, not one of these seven rows.
    aliases={
      'C4_WDM_3keV':'C4_thermal_WDM',
      'C5_designer_fR':'C5_designer_fR',
      'C3_GDM_cs2':'C3_GDM_cs2',
      'C3_GDM_cv2':'C3_GDM_cv2'
    }

    normalized_edges=[]
    channels=set()
    for e in edges.get('edges',[]):
        seps=[]
        for s in e.get('established_separators',[]):
            if s not in BLOCK_MAP:
                failures.append('unknown_separator:'+s)
            else:
                seps.append(BLOCK_MAP[s]); channels.add(BLOCK_MAP[s])
        normalized_edges.append({
          'id':e['id'],
          'pair':[aliases.get(x,x) for x in e['pair']],
          'degenerate_in':e['degenerate_in'],
          'hard_separators':seps,
          'source_schema':'dsir.discriminant_edges.v0.1'
        })

    # Exact hitting sets use all hard edges, including C0-vs-C4.
    hitting=[]
    for subset in powerset(channels):
        if all(any(s in subset for s in e['hard_separators']) for e in normalized_edges):
            hitting.append(subset)
    if not hitting:
        failures.append('no_hitting_set')
        min_size=None; minima=[]
    else:
        min_size=min(len(x) for x in hitting)
        minima=[sorted(x) for x in hitting if len(x)==min_size]

    # Mask-aware pair inventory for the seven non-reference atlas directions.
    names=sorted(directions)
    pair_inventory=[]
    for a,b in itertools.combinations(names,2):
        ca,cb=directions[a],directions[b]
        jointly_audited=[]; masked=[]; cohardzero=[]; state_pairs={}
        for block in sorted(set(ca)&set(cb)):
            sa,sb=ca[block]['state'],cb[block]['state']
            state_pairs[block]=[sa,sb]
            if sa in VALID_STATES and sb in VALID_STATES:
                jointly_audited.append(block)
                if sa=='hard_zero' and sb=='hard_zero': cohardzero.append(block)
            else:
                masked.append(block)
        hard_edge_ids=[]
        for e in normalized_edges:
            if set(e['pair'])=={a,b}:
                hard_edge_ids.append(e['id'])
        pair_inventory.append({
          'pair':[a,b],
          'jointly_audited_blocks':jointly_audited,
          'masked_blocks':masked,
          'co_hard_zero_blocks':cohardzero,
          'hard_degeneracy_edge_ids':hard_edge_ids,
          'has_hard_edge_evidence':bool(hard_edge_ids)
        })

    hard_edges_internal=[e for e in normalized_edges if all(x in directions for x in e['pair'])]
    hard_edges_external=[e for e in normalized_edges if not all(x in directions for x in e['pair'])]
    hard_pair_count=sum(1 for x in pair_inventory if x['has_hard_edge_evidence'])
    unresolved_pair_count=len(pair_inventory)-hard_pair_count

    # Explicitly preserve the one external-reference edge in the current catalogue.
    if len(hard_edges_external)!=1 or set(hard_edges_external[0]['pair'])!={'C0_LCDM','C4_thermal_WDM'}:
        failures.append('unexpected_external_reference_edge_set')

    # C4 time completion must not silently create a new hard separator edge.
    c4_edges=[e for e in normalized_edges if 'C4_thermal_WDM' in e['pair']]
    if len(c4_edges)!=1 or c4_edges[0]['hard_separators']!=['M_highk']:
        failures.append('c4_edge_contract_changed_without_hard_gate')

    out={
      'schema':'dsir.masked_discriminant_coverage.v0.2',
      'status':'PASS_MASKED_DISCRIMINANT_COVERAGE_V0_2' if not failures else 'FAIL_MASKED_DISCRIMINANT_COVERAGE_V0_2',
      'failures':failures,
      'nonreference_direction_count':len(names),
      'nonreference_pair_count':len(pair_inventory),
      'hard_degeneracy_edge_count_total':len(normalized_edges),
      'hard_edges_internal_to_nonreference_atlas':len(hard_edges_internal),
      'hard_edges_with_external_reference_endpoint':len(hard_edges_external),
      'external_reference_edges':hard_edges_external,
      'hard_pair_count_in_nonreference_pair_inventory':hard_pair_count,
      'nonreference_pairs_without_hard_edge_evidence':unresolved_pair_count,
      'normalized_hard_edges':normalized_edges,
      'candidate_channel_universe':sorted(channels),
      'minimum_hitting_set_cardinality_current_hard_graph':min_size,
      'minimum_hitting_sets_current_hard_graph':minima,
      'pair_inventory_nonreference':pair_inventory,
      'interpretation':{
        'hard_lower_bound_on_separator_types_for_current_edge_catalogue':min_size,
        'scope':'all four existing hard-established degeneracy edges, including external reference edge C0-vs-C4; pair inventory itself contains only seven non-reference atlas directions',
        'c4_time_completion_effect':'strengthens C4 evidence mask but creates no new pairwise hard separator edge without a frozen comparison gate'
      },
      'not_a_claim':[
        'not N_micro, N_manifold, N_repr or an intrinsic numerical rank',
        'not proof that nonreference pairs without hard edges are degenerate or distinguishable',
        'not a survey-optimal channel set',
        'not zero-imputed matrix completion',
        'not G7/G8 closure'
      ]
    }
    Path(args.json).write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
    raise SystemExit(0 if not failures else 2)

if __name__=='__main__': main()
