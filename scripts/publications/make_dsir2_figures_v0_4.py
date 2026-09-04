#!/usr/bin/env python3
"""Generate DSIR-2 Figures 1--4 v0.4 with deterministic vector metadata.

v0.4 is reproducibility-only relative to v0.3: it reuses the accepted v0.3
visual/scientific construction unchanged, but removes volatile PDF/SVG metadata,
fixes the SVG hash salt, and emits v0.4 filenames. Scientific values,
thresholds, labels, geometry, and classifications are unchanged.
"""
from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt

import make_dsir2_figures_v0_3 as base


# Stable SVG element IDs across repeated executions with the same Matplotlib build.
mpl.rcParams["svg.hashsalt"] = "dsir2-article2-figures-v0.4"

PDF_METADATA = {
    "CreationDate": None,
    "ModDate": None,
    "Creator": "DSIR-2 deterministic figure generator v0.4",
    "Producer": "Matplotlib",
}
SVG_METADATA = {
    "Date": None,
    "Creator": "DSIR-2 deterministic figure generator v0.4",
}


def deterministic_save(fig, outdir: Path, stem: str):
    """Save v0.3 visual content as deterministic v0.4 PDF/SVG artifacts."""
    outdir.mkdir(parents=True, exist_ok=True)
    stem_v04 = stem.replace("_v0_3", "_v0_4")
    fig.savefig(
        outdir / f"{stem_v04}.pdf",
        bbox_inches="tight",
        metadata=PDF_METADATA,
    )
    fig.savefig(
        outdir / f"{stem_v04}.svg",
        bbox_inches="tight",
        metadata=SVG_METADATA,
    )
    plt.close(fig)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--manifest",
        type=Path,
        default=Path("docs/publications/DSIR2_FIGURE_NUMERIC_MANIFEST_V0_1.json"),
    )
    parser.add_argument(
        "--outdir",
        type=Path,
        default=Path("artifacts/publications/article2/figures"),
    )
    args = parser.parse_args()

    # Replace only the serialization layer. All four figure constructors remain
    # exactly the accepted v0.3 implementations.
    base.save = deterministic_save
    manifest = base.load_manifest(args.manifest)
    base.figure1(manifest, args.outdir)
    base.figure2(manifest, args.outdir)
    base.figure3(manifest, args.outdir)
    base.figure4(manifest, args.outdir)
    print(f"Wrote deterministic DSIR-2 publication Figures 1-4 v0.4 to {args.outdir}")


if __name__ == "__main__":
    main()
