#!/usr/bin/env python3
import argparse, json, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from dsir.discriminants import minimal_separating_channel_sets


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--input",required=True)
    ap.add_argument("--json",required=True)
    args=ap.parse_args()
    d=json.load(open(args.input))
    edges=d["edges"]
    if not edges:
        raise SystemExit("No hard-evidence edges")
    pair_to_channels={e["id"]: e["established_separators"] for e in edges}
    mins=minimal_separating_channel_sets(pair_to_channels)
    if not mins:
        raise SystemExit("No separating set")
    all_have_evidence=all(e.get("evidence",{}).get("run_id") and e.get("evidence",{}).get("artifact_digest") for e in edges)
    if not all_have_evidence:
        raise SystemExit("Missing provenance evidence")
    out={
        "schema":"dsir.discriminant_graph.result.v0.1",
        "edge_count":len(edges),
        "edges":edges,
        "minimum_separating_channel_sets":[list(x) for x in mins],
        "minimum_cardinality":len(mins[0]),
        "status":"PASS_HARD_EVIDENCE_DISCRIMINANT_GRAPH_V0_1",
        "interpretation_rule":"The minimum hitting set covers only the hard-established degeneracy edges currently catalogued. It is not a globally optimal survey design for all dark-sector theories."
    }
    json.dump(out,open(args.json,"w"),indent=2,sort_keys=True)
    print(json.dumps(out,indent=2,sort_keys=True))

if __name__=="__main__": main()
