#!/usr/bin/env python3
"""Build a deterministic self-contained DSIR-I JCAP/arXiv source archive.

This script is release-facing rather than scientific. In normal mode it assumes
the audited JCAP source, pinned local JCAP style/BST, bibliography, and
publication-figure PDFs already exist. It copies only source inputs required for
a clean submission compile, rewrites repository-relative paths to archive-local
paths, writes an exact SHA256 manifest beside (not inside) the journal ZIP, and
creates a deterministic ZIP.

With ``--finalize-bbl-from PATH`` it copies a BibTeX-generated .bbl from a clean
archive verification compile back into the source package, rewrites the external
manifest, and rebuilds the deterministic ZIP without importing auxiliary/log/PDF
files. Scientific content, thresholds, figures, and bibliography records are
never modified by this script.
"""

from __future__ import annotations

import argparse
import hashlib
import shutil
import zipfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
JCAP = HERE / "jcap"
FIGDIR = HERE / "figures" / "generated"
RELEASE = HERE / "release"
PKG = RELEASE / "dsir1_submission"
ZIP = RELEASE / "dsir1_submission.zip"
# Provenance evidence is intentionally kept outside the editor-facing ZIP.
MANIFEST = RELEASE / "SUBMISSION_MANIFEST_SHA256.txt"

MASTER = JCAP / "dsir1_jcap.tex"
STYLE = JCAP / "jcappub.sty"
BST = JCAP / "JHEP.bst"
BIB = HERE / "references.bib"
FIGURES = [FIGDIR / f"fig0{i}_{name}.pdf" for i, name in [
    (1, "operator_architecture"),
    (2, "additive_core_failure"),
    (3, "chiI_hierarchy"),
    (4, "channel_conditional_degeneracy"),
    (5, "curvature_and_localization"),
    (6, "failure_resistant_science"),
    (7, "observation_space_support_closure"),
]]

FIXED_ZIP_TIME = (2026, 8, 28, 0, 0, 0)


def require(cond: bool, msg: str) -> None:
    if not cond:
        raise RuntimeError(msg)


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def copy_required(src: Path, dst: Path) -> None:
    require(src.is_file() and src.stat().st_size > 0, f"required release input missing/empty: {src}")
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(src, dst)


def archive_files() -> list[Path]:
    return sorted(p for p in PKG.rglob("*") if p.is_file())


def write_manifest() -> None:
    RELEASE.mkdir(parents=True, exist_ok=True)
    lines = []
    for path in archive_files():
        rel = path.relative_to(PKG).as_posix()
        lines.append(f"{sha256(path)}  {rel}")
    MANIFEST.write_text("\n".join(lines) + "\n", encoding="utf-8")


def deterministic_zip() -> None:
    if ZIP.exists():
        ZIP.unlink()
    files = archive_files()
    with zipfile.ZipFile(ZIP, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
        for path in files:
            rel = path.relative_to(PKG).as_posix()
            info = zipfile.ZipInfo(rel, FIXED_ZIP_TIME)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            zf.writestr(info, path.read_bytes(), compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)


def verify_package_contract(require_bbl: bool) -> None:
    required = [
        PKG / "dsir1_jcap.tex",
        PKG / "jcappub.sty",
        PKG / "JHEP.bst",
        PKG / "references.bib",
        *[PKG / "figures" / p.name for p in FIGURES],
    ]
    if require_bbl:
        required.append(PKG / "dsir1_jcap.bbl")
    for path in required:
        require(path.is_file() and path.stat().st_size > 0, f"release package file missing/empty: {path}")

    tex = (PKG / "dsir1_jcap.tex").read_text(encoding="utf-8")
    require("../" not in tex, "parent-directory dependency remains in release TeX")
    require(r"\bibliography{references}" in tex, "archive-local bibliography binding missing")
    for fig in FIGURES:
        require(f"figures/{fig.name}" in tex, f"archive-local figure binding missing: {fig.name}")

    # Editor-facing package must contain only source inputs and figures, not a
    # compiled article PDF or internal provenance/checksum helper files.
    rels = [p.relative_to(PKG).as_posix() for p in archive_files()]
    require("dsir1_jcap.pdf" not in rels, "compiled article PDF leaked into source package")
    require("SUBMISSION_MANIFEST_SHA256.txt" not in rels, "provenance manifest leaked into journal package")
    require(all(" " not in rel for rel in rels), "archive member name contains a space")


def build_initial_package() -> None:
    for path in [MASTER, STYLE, BST, BIB, *FIGURES]:
        require(path.is_file() and path.stat().st_size > 0, f"release input missing/empty: {path}")

    if PKG.exists():
        shutil.rmtree(PKG)
    RELEASE.mkdir(parents=True, exist_ok=True)
    if MANIFEST.exists():
        MANIFEST.unlink()
    PKG.mkdir(parents=True, exist_ok=True)
    (PKG / "figures").mkdir(parents=True, exist_ok=True)

    tex = MASTER.read_text(encoding="utf-8")
    require("../figures/generated/" in tex, "expected repository figure path not found in master TeX")
    require(r"\bibliography{../references}" in tex, "expected repository bibliography path not found in master TeX")

    tex = tex.replace("../figures/generated/", "figures/")
    tex = tex.replace(r"\bibliography{../references}", r"\bibliography{references}")

    require("../" not in tex, "parent-directory dependency remains in release TeX")
    require("paper/dsir-i-observable-response-geometry" not in tex, "paper branch path leaked into release TeX")

    (PKG / "dsir1_jcap.tex").write_text(tex, encoding="utf-8")
    copy_required(STYLE, PKG / "jcappub.sty")
    copy_required(BST, PKG / "JHEP.bst")
    copy_required(BIB, PKG / "references.bib")
    for fig in FIGURES:
        copy_required(fig, PKG / "figures" / fig.name)

    verify_package_contract(require_bbl=False)
    write_manifest()
    deterministic_zip()


def finalize_with_bbl(source_bbl: Path) -> None:
    require(PKG.is_dir(), "submission package does not exist; run initial build first")
    copy_required(source_bbl, PKG / "dsir1_jcap.bbl")
    verify_package_contract(require_bbl=True)
    write_manifest()
    deterministic_zip()


def report(label: str) -> None:
    require(ZIP.is_file() and ZIP.stat().st_size > 0, "submission ZIP missing/empty")
    require(MANIFEST.is_file() and MANIFEST.stat().st_size > 0, "external submission manifest missing/empty")
    require(ZIP.stat().st_size < 10 * 1024 * 1024, "submission ZIP exceeds 10 MiB")
    with zipfile.ZipFile(ZIP, "r") as zf:
        names = zf.namelist()
    require("dsir1_jcap.tex" in names, "master TeX is not at archive root")
    require("dsir1_jcap.pdf" not in names, "compiled article PDF is present in journal ZIP")
    require("SUBMISSION_MANIFEST_SHA256.txt" not in names, "external manifest is present in journal ZIP")
    require(all(" " not in name for name in names), "journal ZIP contains member name with spaces")
    print(f"mode={label}")
    print(f"package_dir={PKG}")
    print(f"zip={ZIP}")
    print(f"manifest={MANIFEST}")
    print(f"zip_sha256={sha256(ZIP)}")
    print(f"zip_bytes={ZIP.stat().st_size}")
    print(f"source_files={len(archive_files())}")
    print("PASS: self-contained DSIR-I submission source package assembled")
    print("PASS: editor-facing ZIP excludes article PDF and provenance manifest")
    print("PASS: master TeX at archive root; archive member names contain no spaces")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--finalize-bbl-from",
        type=Path,
        default=None,
        help="copy only this verified generated .bbl into the source package and rebuild external manifest/ZIP",
    )
    args = parser.parse_args()

    if args.finalize_bbl_from is None:
        build_initial_package()
        report("initial")
    else:
        finalize_with_bbl(args.finalize_bbl_from)
        report("finalized-with-bbl")


if __name__ == "__main__":
    main()
