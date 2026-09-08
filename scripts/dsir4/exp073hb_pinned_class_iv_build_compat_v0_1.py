#!/usr/bin/env python3
"""Exact non-scientific build-compatibility shim for Exp073HB.

The pinned class_iv commit has three modern-toolchain build defects that are
orthogonal to DSIR science: one stray switch-closing brace before `case IDM_IV`,
a tentative global definition that needs legacy -fcommon semantics, and GSL
libraries placed before objects on the final link line. This shim repairs only
those exact build surfaces and changes no equation/expression token.
It is permitted only after exact upstream commit/blob verification.
"""
from pathlib import Path
import sys

root = Path(sys.argv[1] if len(sys.argv) > 1 else ".")

# 1) exact stray brace in background_w_fld
p = root / "source/background.c"
s = p.read_text()
old = """    *w_fld = - dOmega_ede_over_da*a/Omega_ede/3./(1.-Omega_ede)+a_eq/3./(a+a_eq);\n    break;\n  }\n\n  case IDM_IV:"""
new = """    *w_fld = - dOmega_ede_over_da*a/Omega_ede/3./(1.-Omega_ede)+a_eq/3./(a+a_eq);\n    break;\n\n  case IDM_IV:"""
if s.count(old) != 1:
    raise RuntimeError(f"expected exact stray-brace anchor once, got {s.count(old)}")
p.write_text(s.replace(old, new, 1))
print("EXP073HB_PINNED_UPSTREAM_STRAY_BRACE_REMOVED_EXACTLY_ONCE")

# 2-3) exact Makefile compatibility only: retain all optimization/science flags,
# add legacy common-symbol behavior, and put GSL libraries after object files.
m = root / "Makefile"
t = m.read_text()
old_opt = "OPTFLAG = -O2 #-ffast-math #-march=native"
new_opt = "OPTFLAG = -O2 -fcommon #-ffast-math #-march=native"
if t.count(old_opt) != 1:
    raise RuntimeError(f"expected OPTFLAG anchor once, got {t.count(old_opt)}")
t = t.replace(old_opt, new_opt, 1)
old_ld = "LDFLAG = -g -fPIC -lgsl -lgslcblas"
new_ld = "LDFLAG = -g -fPIC"
if t.count(old_ld) != 1:
    raise RuntimeError(f"expected LDFLAG anchor once, got {t.count(old_ld)}")
t = t.replace(old_ld, new_ld, 1)
old_class = "\t$(CC) $(OPTFLAG) $(OMPFLAG) $(LDFLAG) -o class $(addprefix build/,$(notdir $^)) -lm"
new_class = "\t$(CC) $(OPTFLAG) $(OMPFLAG) $(LDFLAG) -o class $(addprefix build/,$(notdir $^)) -lgsl -lgslcblas -lm"
if t.count(old_class) != 1:
    raise RuntimeError(f"expected class link anchor once, got {t.count(old_class)}")
t = t.replace(old_class, new_class, 1)
m.write_text(t)
print("EXP073HB_PINNED_UPSTREAM_MODERN_LINK_COMPAT_APPLIED_EXACTLY")
