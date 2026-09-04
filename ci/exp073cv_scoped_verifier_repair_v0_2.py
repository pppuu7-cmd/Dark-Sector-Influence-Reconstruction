#!/usr/bin/env python3
from __future__ import annotations
import ast, sys
from pathlib import Path

TARGET=Path(sys.argv[1] if len(sys.argv)>1 else 'ci/exp073cv_wm_s3_production_exact_adapter_v0_1.py')
OUT=Path(sys.argv[2] if len(sys.argv)>2 else 'ci/exp073cv_wm_s3_production_exact_adapter_v0_2_runtime.py')
src=TARGET.read_text()
tree=ast.parse(src)
production={'stream_fits_to_canonical_input','run_downstream','execute'}
seen=set()
for node in tree.body:
    if isinstance(node,(ast.FunctionDef,ast.AsyncFunctionDef)) and node.name in production:
        seen.add(node.name)
        for child in ast.walk(node):
            if isinstance(child,ast.Call) and isinstance(child.func,ast.Attribute) and child.func.attr=='get_coupling_matrix':
                raise SystemExit(f'forbidden production get_coupling_matrix in {node.name}')
if seen != production:
    raise SystemExit(f'production function set mismatch: {sorted(seen)}')
old="src=Path(__file__).read_text()\n    if '.get_coupling_matrix(' in src: raise RuntimeError('forbidden materialization pattern')"
new="src='SCOPED_VERIFIER_PASS_PRODUCTION_FUNCTIONS_ONLY'"
if src.count(old)!=1:
    raise SystemExit('expected exactly one v0.1 verifier defect site')
patched=src.replace(old,new)
if patched.count(new)!=1:
    raise SystemExit('scoped verifier patch count mismatch')
OUT.write_text(patched)
print('PASS_EXP073CV_V0_2_SCOPED_PRODUCTION_VERIFIER')
