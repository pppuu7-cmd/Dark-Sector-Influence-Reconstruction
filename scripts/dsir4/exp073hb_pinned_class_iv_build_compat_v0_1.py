#!/usr/bin/env python3
"""Exact non-scientific build-compatibility shim for Exp073HB.

The pinned class_iv source has one stray switch-closing brace immediately
before `case IDM_IV` in background_w_fld, making the pinned commit
uncompilable. This shim removes exactly that one brace and changes no token
inside any equation/expression. It is permitted only after exact upstream
commit/blob verification by the hosted workflow.
"""
from pathlib import Path
import sys

root = Path(sys.argv[1] if len(sys.argv) > 1 else ".")
p = root / "source/background.c"
s = p.read_text()
old = """    *w_fld = - dOmega_ede_over_da*a/Omega_ede/3./(1.-Omega_ede)+a_eq/3./(a+a_eq);\n    break;\n  }\n\n  case IDM_IV:"""
new = """    *w_fld = - dOmega_ede_over_da*a/Omega_ede/3./(1.-Omega_ede)+a_eq/3./(a+a_eq);\n    break;\n\n  case IDM_IV:"""
count = s.count(old)
if count != 1:
    raise RuntimeError(f"expected exact stray-brace anchor once, got {count}")
s = s.replace(old, new, 1)
p.write_text(s)
print("EXP073HB_PINNED_UPSTREAM_STRAY_BRACE_REMOVED_EXACTLY_ONCE")
