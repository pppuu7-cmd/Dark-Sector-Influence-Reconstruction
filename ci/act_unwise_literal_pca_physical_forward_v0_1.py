#!/usr/bin/env python3
from __future__ import annotations

import argparse
import importlib.util
import json
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
BASE_PATH = ROOT / "ci" / "act_unwise_physical_forward_reproduction_v0_1.py"
spec = importlib.util.spec_from_file_location("exp068a_base", BASE_PATH)
base = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(base)

N_SAMP = {"Blue": 3, "Green": 5}
PASS = "PASS_ACT_UNWISE_LITERAL_PCA_PHYSICAL_FORWARD_V0_1"
FAIL = "FAIL_ACT_UNWISE_LITERAL_PCA_PHYSICAL_FORWARD_V0_1"


def literal_source_semantics(upstream_repo: Path):
    helper = upstream_repo / "unWISExLens_lklh" / "theory_modules" / "model_helpers_unWISExLens.py"
    model = upstream_repo / "unWISExLens_lklh" / "theory_modules" / "unWISExkappa_model.py"
    ht = helper.read_text()
    mt = model.read_text()
    checks = {
        "helper_mean_first_documented": "First component must be mean" in ht,
        "helper_n_pcs_counts_interpolator_width": "return len(self.__delta_xcorr_dndz_pcs(0.0))" in ht,
        "evaluator_sampled_length_rule": "assert(len(pca_coeff[i])==n_pcs - 1)" in mt,
        "evaluator_fixed_fiducial_mean_pair": "np.concatenate([[1.0, 1.0], pca_coeff[i]])" in mt,
    }
    checks["pass"] = bool(all(checks.values()))
    return checks


def literal_tracer_node_check(cosmo, tracers, tracer_records):
    gx, _ = np.polynomial.legendre.leggauss(base.NINT)
    chi_min, chi_max = cosmo.chi(base.ZMIN), cosmo.chi(base.ZMAX)
    chi = (chi_max - chi_min) / 2.0 * gx + (chi_max + chi_min) / 2.0
    z = np.asarray(cosmo.z_of_chi(chi), dtype=np.float64)
    all_ok = True
    for i, sample in enumerate(("Blue", "Green")):
        n_samp = N_SAMP[sample]
        correction_width = 1 + n_samp
        expanded_width = 2 + n_samp
        tr = tracers[i]
        x = np.asarray(tr.dNdz(z), dtype=np.float64)
        b = np.asarray(tr.bdNdz(z, pcs=True), dtype=np.float64)
        pcs_shape = tracer_records[sample]["file_shapes"].get("pcs")
        file_width_ok = bool(pcs_shape and len(pcs_shape) == 2 and pcs_shape[1] == 2 + n_samp)
        ok = bool(
            tracer_records[sample]["exists"]
            and tracer_records[sample]["finite_files"]
            and file_width_ok
            and tracer_records[sample]["observed_n_pcs"] == correction_width
            and x.shape == z.shape
            and b.shape == (z.size, expanded_width)
            and np.all(np.isfinite(x))
            and np.all(np.isfinite(b))
            and np.count_nonzero(x) > 0
            and np.count_nonzero(b) > 0
        )
        all_ok &= ok
        tracer_records[sample].update({
            "sampled_pca_nuisance_count": n_samp,
            "expected_correction_basis_width_mean_plus_pcs": correction_width,
            "expected_expanded_bdndz_width_fiducial_plus_mean_plus_pcs": expanded_width,
            "correction_file_width_including_z": int(pcs_shape[1]) if pcs_shape and len(pcs_shape) == 2 else None,
            "correction_file_width_pass": file_width_ok,
            "projection_node_xmatch_shape": list(x.shape),
            "projection_node_bdNdz_shape": list(b.shape),
            "projection_node_xmatch_nonzero": int(np.count_nonzero(x)),
            "projection_node_bdNdz_nonzero": int(np.count_nonzero(b)),
            "pass": ok,
        })
    return bool(all_ok), tracer_records


def zero_displacement_control(reference):
    records = {}
    all_ok = True
    for i, sample in enumerate(("Blue", "Green")):
        n_samp = N_SAMP[sample]
        coeff = np.concatenate([np.array([1.0, 1.0]), np.zeros(n_samp)])
        kg_b = np.asarray(reference[i]["kg"]["kg_b"], dtype=np.float64)
        norm = np.asarray(reference[i]["bdndz_norm"], dtype=np.float64)
        shape_ok = bool(kg_b.ndim >= 2 and kg_b.shape[-1] == coeff.size and norm.shape == (coeff.size,))
        normalization = float(np.dot(norm, coeff)) if shape_ok else float("nan")
        ok = bool(shape_ok and np.all(np.isfinite(coeff)) and np.isfinite(normalization) and normalization != 0.0)
        all_ok &= ok
        records[sample] = {
            "sampled_pca_nuisance_count": n_samp,
            "coefficient_vector": coeff.tolist(),
            "kg_b_last_axis": int(kg_b.shape[-1]) if kg_b.ndim >= 1 else None,
            "bdndz_norm_shape": list(norm.shape),
            "normalization_dot": normalization,
            "pass": ok,
        }
    return bool(all_ok), records


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--upstream-repo", required=True)
    ap.add_argument("--camb-repo", required=True)
    ap.add_argument("--extracted-root", required=True)
    ap.add_argument("--archive", required=True)
    ap.add_argument("--output", required=True)
    args = ap.parse_args()

    upstream_repo = Path(args.upstream_repo).resolve()
    camb_repo = Path(args.camb_repo).resolve()
    extracted_root = Path(args.extracted_root).resolve()
    archive = Path(args.archive).resolve()
    output = Path(args.output).resolve()

    upstream_head = base.git_head(upstream_repo)
    camb_head = base.git_head(camb_repo)
    archive_hash = base.sha256(archive)
    provenance = {
        "upstream_commit": upstream_head,
        "expected_upstream_commit": base.UPSTREAM_PIN,
        "CAMB_commit": camb_head,
        "expected_CAMB_commit": base.CAMB_PIN,
        "archive_sha256": archive_hash,
        "expected_archive_sha256": base.ARCHIVE_SHA256,
    }
    provenance["pass"] = bool(
        upstream_head == base.UPSTREAM_PIN
        and camb_head == base.CAMB_PIN
        and archive_hash == base.ARCHIVE_SHA256
    )

    UpstreamModel, CosmoFromCamb, Dndz, DndzHelper, source_contract = base.load_exact_upstream(upstream_repo)
    literal_source = literal_source_semantics(upstream_repo)
    data_root = base.find_data_root(extracted_root)
    tracers, tracer_records = base.build_real_tracers(data_root, Dndz, DndzHelper)

    camb_results, pww, pwm, pmm = base.build_camb_physical()
    cosmo = CosmoFromCamb(camb_results, include_nu_OmegaM=True)
    tracer_pass, tracer_records = literal_tracer_node_check(cosmo, tracers, tracer_records)
    provider_pass, provider_cells = base.provider_probe(pww, pwm, pmm)

    ref_model = UpstreamModel(
        zmax=base.ZMAX,
        zmin=base.ZMIN,
        k_max=base.KMAX,
        N_integration=base.NINT,
        cross_correlation_redshift_correction=None,
        cleft_interp_helper=None,
        ell_vals=base.ELL,
        want_gg_cross=False,
        ell_vals_clkk=None,
    )
    reference = ref_model.compute_raw_spectra(
        cosmo,
        tracers,
        pww,
        pwm,
        pmm,
        cleft_interpolations_dtot_dnonu=None,
        cleft_interpolations_dnonu_dnonu=None,
        fid_bias_evol_list=None,
    )
    dsir = base.compute_raw_no_cleft(
        cosmo,
        tracers,
        pww,
        pwm,
        pmm,
        ell_vals=base.ELL,
        zmin=base.ZMIN,
        zmax=base.ZMAX,
        kmax=base.KMAX,
        n_integration=base.NINT,
    )

    ref_map = base.component_map(reference)
    dsir_map = base.component_map(dsir)
    equivalence_pass, equivalence = base.compare_maps(ref_map, dsir_map)
    nontrivial_pass, nontrivial = base.nontriviality(ref_map, dsir_map)
    zero_coeff_pass, zero_coeff = zero_displacement_control(reference)

    passed = bool(
        provenance["pass"]
        and source_contract["pass"]
        and literal_source["pass"]
        and tracer_pass
        and provider_pass
        and equivalence_pass
        and nontrivial_pass
        and zero_coeff_pass
    )

    result = {
        "experiment": "Exp068B",
        "date": "2026-08-26",
        "status": PASS if passed else FAIL,
        "scope": "corrective physical linear/no-CLEFT ACT x unWISE forward reproduction with literal pinned-upstream mean-plus-PCA tracer semantics; Exp068A FAIL remains permanent",
        "preregistration_parent": "experiments/068b_literal_pca_semantics_physical_forward_reproduction_v0_1.md",
        "exp068a_status_preserved": "FAIL_ACT_UNWISE_PHYSICAL_FORWARD_REPRODUCTION_V0_1",
        "provenance": provenance,
        "source_contract": source_contract,
        "literal_upstream_pca_source_semantics": literal_source,
        "frozen_domain": {
            "ell_first": int(base.ELL[0]),
            "ell_last": int(base.ELL[-1]),
            "ell_count": int(base.ELL.size),
            "zmin": base.ZMIN,
            "zmax": base.ZMAX,
            "projector_kmax_Mpc^-1": base.KMAX,
            "CAMB_internal_kmax_Mpc^-1": base.CAMB_KMAX,
            "Gauss_Legendre_order": base.NINT,
            "CAMB_redshift_grid_size": base.NZ_CAMB,
            "linear_no_CLEFT": True,
        },
        "tracer_binding": {"pass": tracer_pass, "data_root": str(data_root), "samples": tracer_records},
        "physical_provider_sanity": {"pass": provider_pass, "cells": provider_cells},
        "raw_component_equivalence": {"pass": equivalence_pass, "tolerance_factor": base.TOL, "components": equivalence},
        "nontrivial_physical_signal_control": {"pass": nontrivial_pass, "samples": nontrivial},
        "zero_displacement_coefficient_control": {"pass": zero_coeff_pass, "samples": zero_coeff},
        "interpretation": (
            "PASS validates the physical R0 linear/no-CLEFT raw forward bridge under the literal released upstream tracer convention, while preserving Exp068A as FAIL. "
            "Neither outcome closes G7/G8/G9."
        ),
        "next_step_if_pass": (
            "Preregister a physical survey-kernel validity/leakage mask before covariance restriction, whitening and no-CLEFT nuisance tangent SVD."
        ),
        "gate_state": {"G7": "OPEN", "G8": "OPEN", "G9": "OPEN"},
    }
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
