#!/usr/bin/env python3
from __future__ import annotations
import importlib.util,json
from pathlib import Path
PARSER=1048576; MEM=16373452; BUILD="b5cd7304c110962dc3baef8d04ef67d5a8042e5f"; BUILD_CLASS="LAYERB_32769_CLASS_CAPACITY_BUILD_ENVELOPE_V0_2_PASS_PLUS_0_PLUS_0"; WORKFLOW=".github/workflows/layerb-16385-to-32769-canonical-scientific-v0-2.yml"; TERMINAL="e441c54f8ad4a0590ad521710d4b9dbf37f111ba"
def load_parent():
 p=Path(__file__).with_name('layerb_16385_to_32769_canonical_one_live_refinement_v0_1.py'); spec=importlib.util.spec_from_file_location('layerb_science_v01_frozen',p); m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m
def validate_build_v02(path):
 p=Path(path); b=p.read_bytes(); d=json.loads(b); blob=__import__('hashlib').sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
 if blob!=BUILD or d.get('classification')!=BUILD_CLASS or d.get('artifact_verified_independently') is not True or d.get('class_commit')!='ac627d54e9ce196a08878d1ba33999819925d19c' or d.get('new_capacity')!=32769 or d.get('parser_new_argument_capacity')!=PARSER or d.get('canonical_32769_payload_bytes_including_nul')!=719273 or d.get('parser_margin_bytes')!=329303 or d.get('only_delta_from_v0_1_32769_tree_is_parser_capacity_constant') is not True or d.get('functional_payload_sufficiency_static') is not True or d.get('scientific_response_read') is not False or d.get('scientific_execution_authorized') is not False:
  raise RuntimeError('invalid parser-corrected 32769 CLASS build authority V0.2')
 return d
def main():
 m=load_parent(); m.PARSER_CAPACITY=PARSER; m.HOSTED_MEMTOTAL_KB=MEM; m.BUILD_AUTH_BLOB=BUILD; m.BUILD_AUTH_CLASS=BUILD_CLASS; m.PRODUCTION_WORKFLOW=WORKFLOW; m.TERMINAL_CONTRACT_BLOB=TERMINAL; m.validate_build=validate_build_v02
 return m.main()
if __name__=='__main__': raise SystemExit(main())
