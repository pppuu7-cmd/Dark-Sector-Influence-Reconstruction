#!/usr/bin/env python3
"""Apply the single compile-only repair required by pinned class_iv ac627d54.

The pinned upstream source closes the first `switch (fluid_equation_of_state)`
in `background_w_fld()` immediately after `case EDE`, leaving `case IDM_IV`
outside the switch. This script removes exactly that one premature brace.

Scientific constraint: no equation, coefficient, parameter value, or branch body
is altered. The script aborts unless the exact pinned-source context occurs once.
"""
from pathlib import Path
import sys

path = Path(sys.argv[1] if len(sys.argv) > 1 else "source/background.c")
text = path.read_text()

needle = """    *w_fld = - dOmega_ede_over_da*a/Omega_ede/3./(1.-Omega_ede)+a_eq/3./(a+a_eq);\n    break;\n  }\n\n  case IDM_IV:"""
replacement = """    *w_fld = - dOmega_ede_over_da*a/Omega_ede/3./(1.-Omega_ede)+a_eq/3./(a+a_eq);\n    break;\n\n  case IDM_IV:"""

count = text.count(needle)
if count != 1:
    raise SystemExit(f"Refusing repair: expected exact pinned context once, found {count}")

fixed = text.replace(needle, replacement, 1)
if fixed.count("case IDM_IV:") != text.count("case IDM_IV:"):
    raise SystemExit("Refusing repair: case-label count changed")
if len(text) - len(fixed) != 4:  # two spaces + '}' + newline
    raise SystemExit("Refusing repair: unexpected edit size")

path.write_text(fixed)
print("Applied compile-only class_iv repair: removed exactly one premature closing brace")
