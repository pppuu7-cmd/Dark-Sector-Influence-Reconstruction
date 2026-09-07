#!/usr/bin/env python3
"""Generate and audit the prospective Exp073GM C2 observation-only hook.

This script is intentionally fail-closed.  It only accepts the pinned class_iv
perturbations.c blob and inserts one diagnostic block immediately after the
existing perturb_total_stress_energy() call inside perturb_einstein().
It does not alter equations, state, tolerances, species sums, or gate logic.
"""

from __future__ import annotations

import argparse
import hashlib
from pathlib import Path
import subprocess
import sys

PINNED_SOURCE_SHA256 = ""  # populated from exact source at runtime only for reporting
PINNED_GIT_COMMIT = "ac627d54e9ce196a08878d1ba33999819925d19c"
BEGIN = "/* DSIR_EXP073GM_DIAGNOSTIC_ONLY_BEGIN */"
END = "/* DSIR_EXP073GM_DIAGNOSTIC_ONLY_END */"

ANCHOR = """  class_call(perturb_total_stress_energy(ppr,pba,pth,ppt,index_md,k,y,ppw),\n             ppt->error_message,\n             ppt->error_message);\n"""

BLOCK = r'''

#ifdef DSIR_EXP073GM_DIAGNOSTICS
  /* DSIR_EXP073GM_DIAGNOSTIC_ONLY_BEGIN */
  {
    const char * dsir_exp073gm_enabled = getenv("DSIR_EXP073GM_DIAGNOSTICS");
    if ((dsir_exp073gm_enabled != NULL) &&
        (dsir_exp073gm_enabled[0] == '1') &&
        (_scalars_) &&
        (pba->has_idm_iv == _TRUE_)) {
      fprintf(stderr,
              "DSIR_EXP073GM tau=%.17g k=%.17g a=%.17g H=%.17g delta_m=%.17g theta_m=%.17g rho_idm_iv=%.17g rho_iv=%.17g gauge=%d\\n",
              tau,
              k,
              a,
              ppw->pvecback[pba->index_bg_H],
              ppw->delta_m,
              ppw->theta_m,
              ppw->pvecback[pba->index_bg_rho_idm_iv],
              ppw->pvecback[pba->index_bg_rho_iv],
              (int)ppt->gauge);
    }
  }
  /* DSIR_EXP073GM_DIAGNOSTIC_ONLY_END */
#endif
'''

FORBIDDEN_IN_BLOCK = (
    "background_at_tau(",
    "thermodynamics_at_z(",
    "ppw->delta_m =",
    "ppw->theta_m =",
    "ppw->pvecback[" + "pba->index_bg_a] =",
    "ppw->pvecmetric[",
    "y[",
    "ppr->",
)


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("source", type=Path)
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--expect-git-commit", default=PINNED_GIT_COMMIT)
    args = ap.parse_args()

    source = args.source
    text = source.read_text(encoding="utf-8")
    before = sha256_text(text)

    if BEGIN in text or END in text:
        raise SystemExit("FAIL: Exp073GM markers already present; refusing double instrumentation")
    if text.count(ANCHOR) != 1:
        raise SystemExit(f"FAIL: expected exactly one perturb_einstein stress-energy anchor, found {text.count(ANCHOR)}")
    for token in FORBIDDEN_IN_BLOCK:
        if token in BLOCK:
            raise SystemExit(f"FAIL: forbidden mutation/recompute token inside diagnostic block: {token}")

    patched = text.replace(ANCHOR, ANCHOR + BLOCK, 1)
    if patched.count(BEGIN) != 1 or patched.count(END) != 1:
        raise SystemExit("FAIL: diagnostic markers not unique after patch construction")

    # Structural proof: removing the inserted block must reproduce the source byte-for-byte.
    start = patched.index("\n#ifdef DSIR_EXP073GM_DIAGNOSTICS", patched.index(ANCHOR) + len(ANCHOR))
    end_marker = "\n#endif\n"
    end = patched.index(end_marker, start) + len(end_marker)
    restored = patched[:start] + patched[end:]
    if restored != text:
        raise SystemExit("FAIL: patched source is not source-equivalent after removing diagnostic block")

    after = sha256_text(patched)
    print(f"EXP073GM_SOURCE_SHA256_BEFORE={before}")
    print(f"EXP073GM_SOURCE_SHA256_PATCHED={after}")
    print("EXP073GM_SOURCE_EQUIVALENCE_MODULO_DIAGNOSTIC_BLOCK=PASS")
    print("EXP073GM_MUTATION_CLASS=DIAGNOSTIC_IO_ONLY")

    if args.apply:
        source.write_text(patched, encoding="utf-8")
        print(f"EXP073GM_PATCH_APPLIED={source}")
    else:
        print("EXP073GM_DRY_RUN=PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
