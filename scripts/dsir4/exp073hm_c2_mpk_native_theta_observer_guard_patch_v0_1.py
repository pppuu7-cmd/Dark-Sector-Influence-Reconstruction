#!/usr/bin/env python3
"""Exp073HM post-HJ observer-only guard correction.

The immutable mPk baseline enables has_source_delta_m. In pinned CLASS that
same native total-matter path computes ppw->theta_m. This patch only removes
an unnecessary diagnostic requirement for the independent RSD theta source.
"""
from pathlib import Path
import hashlib
import sys

ROOT = Path(sys.argv[1] if len(sys.argv) > 1 else ".")
P = ROOT / "source/perturbations.c"
HJ_SHA256 = "f1a5619ea2dfb60e4e236349485dcffb58c1c2ef96358bd59b8a1207d77248d2"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


if sha256(P) != HJ_SHA256:
    raise RuntimeError(f"expected exact HJ source {HJ_SHA256}, got {sha256(P)}")

text = P.read_text()
old = 'class_test(ppt->has_source_delta_m != _TRUE_ || ppt->has_source_theta_m != _TRUE_,error_message,"DSIR C2 diagnostic requires native delta_m and theta_m sources enabled");'
new = 'class_test(ppt->has_source_delta_m != _TRUE_,error_message,"DSIR C2 diagnostic requires native mPk delta_m source path (which also computes theta_m)");'
count = text.count(old)
if count != 1:
    raise RuntimeError(f"observer guard anchor count must be 1, got {count}")
text = text.replace(old, new, 1)
P.write_text(text)
print(f"exp073hm_patched_perturbations_sha256={sha256(P)}")
print("EXP073HM_MPK_NATIVE_THETA_OBSERVER_GUARD_PATCH_APPLIED")
