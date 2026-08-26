#!/usr/bin/env python3
from __future__ import annotations

import argparse
import ast
import json
import subprocess
import sys
from pathlib import Path

import numpy as np

PINNED_COMMIT = "6302c30d9e70f8e4ff2d4a84a9977b4471705179"
ELL = np.array([10.0, 30.0, 80.0, 150.0, 300.0])
ZMIN = 0.0
ZMAX = 3.0
KMAX = 1000.0
NINT = 96
TOL = 5e-13

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from dsir.act_unwise_projection import compute_raw_no_cleft


class MockCosmo:
    """Analytic flat geometry with dchi/dz = 1/H in Mpc conventions."""

    def __init__(self):
        self._a = 3000.0
        self._H0 = 1.0 / self._a
        self._h = 0.67
        self._Omega_m = 0.31
        self._chi_star = 14000.0
        self._curvature = 0.0

    def chi(self, z):
        return self._a * np.log1p(np.asarray(z, dtype=float))

    def z_of_chi(self, chi):
        return np.expm1(np.asarray(chi, dtype=float) / self._a)

    def H(self, z):
        return (1.0 + np.asarray(z, dtype=float)) / self._a

    def comoving_angular_diameter_distance(self, chi):
        return np.asarray(chi, dtype=float)

    @property
    def H0(self):
        return self._H0

    @property
    def h(self):
        return self._h

    @property
    def Omega_m(self):
        return self._Omega_m

    @property
    def chi_star(self):
        return self._chi_star

    @property
    def curvature(self):
        return self._curvature


class MockDndz:
    def __init__(self, center, width, pc=False):
        self.center = float(center)
        self.width = float(width)
        self._pc = bool(pc)

    def dNdz(self, z):
        z = np.asarray(z, dtype=float)
        return np.exp(-0.5 * ((z - self.center) / self.width) ** 2)

    def _xcorr(self, z):
        z = np.asarray(z, dtype=float)
        return 1.08 * self.dNdz(z) * (1.0 + 0.025 * z)

    def bdNdz(self, z, pcs=False):
        z = np.asarray(z, dtype=float)
        base = self._xcorr(z)
        if not pcs:
            return base
        if not self._pc:
            return base[:, None]
        pc = 0.04 * base * (z - self.center) / self.width
        return np.column_stack([base, pc])

    @property
    def n_pcs(self):
        return 1 if self._pc else 0


class MockPower:
    def __init__(self, amp, zcoef, kcoef):
        self.amp = float(amp)
        self.zcoef = float(zcoef)
        self.kcoef = float(kcoef)

    def P(self, z, k, grid=False):
        z = np.asarray(z, dtype=float)
        k = np.asarray(k, dtype=float)
        return self.amp * (1.0 + self.zcoef * z) / (1.0 + self.kcoef * k)

    def scaled(self, factor):
        return MockPower(self.amp * factor, self.zcoef, self.kcoef)


def load_upstream_reference(repo: Path):
    model_path = repo / "unWISExLens_lklh" / "theory_modules" / "unWISExkappa_model.py"
    aux_path = repo / "unWISExLens_lklh" / "auxiliary" / "auxiliary_functions.py"

    # Execute the exact pinned evaluate_pk_kmax function in an isolated namespace.
    aux_tree = ast.parse(aux_path.read_text(), filename=str(aux_path))
    eval_node = next(
        n for n in aux_tree.body if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)) and n.name == "evaluate_pk_kmax"
    )
    eval_mod = ast.Module(body=[eval_node], type_ignores=[])
    ast.fix_missing_locations(eval_mod)
    eval_ns = {"np": np}
    exec(compile(eval_mod, str(aux_path), "exec"), eval_ns)

    # Execute the exact model class while removing only import statements. The
    # no-CLEFT branch under test needs numpy and evaluate_pk_kmax only.
    source = model_path.read_text()
    model_tree = ast.parse(source, filename=str(model_path))
    model_tree.body = [
        n for n in model_tree.body if not isinstance(n, (ast.Import, ast.ImportFrom))
    ]
    ast.fix_missing_locations(model_tree)
    model_ns = {"np": np, "evaluate_pk_kmax": eval_ns["evaluate_pk_kmax"]}
    exec(compile(model_tree, str(model_path), "exec"), model_ns)
    return model_ns["unWISExLens_theory_model"], source


def component_map(outputs):
    out = {}
    for i, rec in enumerate(outputs):
        for section in ("kg", "gg"):
            for key, value in rec[section].items():
                out[f"sample{i}/{section}/{key}"] = np.asarray(value, dtype=float)
        out[f"sample{i}/bdndz_norm"] = np.asarray(rec["bdndz_norm"], dtype=float)
    return out


def compare_maps(ref_map, dsir_map):
    records = {}
    passed = set(ref_map) == set(dsir_map)
    if not passed:
        return False, {"key_mismatch": {"reference": sorted(ref_map), "dsir": sorted(dsir_map)}}
    for key in sorted(ref_map):
        a = ref_map[key]
        b = dsir_map[key]
        shape_ok = a.shape == b.shape
        finite = bool(np.all(np.isfinite(a)) and np.all(np.isfinite(b)))
        if shape_ok:
            max_ref = float(np.max(np.abs(a))) if a.size else 0.0
            max_abs = float(np.max(np.abs(a - b))) if a.size else 0.0
            threshold = TOL * max(1.0, max_ref)
            value_ok = finite and max_abs <= threshold
        else:
            max_ref = None
            max_abs = None
            threshold = None
            value_ok = False
        zero_ref = bool(shape_ok and np.count_nonzero(a) == 0)
        zero_dsir = bool(shape_ok and np.count_nonzero(b) == 0)
        zero_consistent = (not zero_ref) or zero_dsir
        ok = bool(shape_ok and finite and value_ok and zero_consistent)
        passed &= ok
        records[key] = {
            "shape_reference": list(a.shape),
            "shape_dsir": list(b.shape),
            "finite": finite,
            "max_abs_reference": max_ref,
            "max_abs_difference": max_abs,
            "threshold": threshold,
            "reference_identically_zero": zero_ref,
            "dsir_identically_zero": zero_dsir,
            "pass": ok,
        }
    return bool(passed), records


def relative_change(base, changed):
    denom = max(float(np.max(np.abs(base))), 1e-300)
    return float(np.max(np.abs(changed - base)) / denom)


def independence_control(cosmo, tracers, pww, pwm, pmm):
    base = component_map(
        compute_raw_no_cleft(
            cosmo, tracers, pww, pwm, pmm,
            ell_vals=ELL, zmin=ZMIN, zmax=ZMAX, kmax=KMAX, n_integration=NINT,
        )
    )
    controls = {
        "P_WW": component_map(compute_raw_no_cleft(cosmo, tracers, pww.scaled(1.1), pwm, pmm, ell_vals=ELL, zmin=ZMIN, zmax=ZMAX, kmax=KMAX, n_integration=NINT)),
        "P_Wm": component_map(compute_raw_no_cleft(cosmo, tracers, pww, pwm.scaled(1.1), pmm, ell_vals=ELL, zmin=ZMIN, zmax=ZMAX, kmax=KMAX, n_integration=NINT)),
        "P_mm": component_map(compute_raw_no_cleft(cosmo, tracers, pww, pwm, pmm.scaled(1.1), ell_vals=ELL, zmin=ZMIN, zmax=ZMAX, kmax=KMAX, n_integration=NINT)),
    }
    expected_suffixes = {
        "P_WW": {"kg/kmu", "gg/mumu"},
        "P_Wm": {"kg/kg_b", "gg/gmu_b"},
        "P_mm": {"gg/gg_bsq"},
    }
    result = {}
    all_ok = True
    for name, cmap in controls.items():
        changed_suffixes = set()
        details = {}
        for key in sorted(base):
            rel = relative_change(base[key], cmap[key])
            # A 10% input scaling gives exactly 10% for a linearly dependent
            # nonzero raw basis component. Numerical zeros remain exactly fixed.
            changed = rel > 1e-6
            suffix = "/".join(key.split("/")[1:]) if "/" in key else key
            if changed:
                changed_suffixes.add(suffix)
            details[key] = rel
        ok = changed_suffixes == expected_suffixes[name]
        all_ok &= ok
        result[name] = {
            "expected_changed_component_suffixes": sorted(expected_suffixes[name]),
            "observed_changed_component_suffixes": sorted(changed_suffixes),
            "relative_changes": details,
            "pass": ok,
        }
    return bool(all_ok), result


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--external-repo", required=True)
    ap.add_argument("--output", required=True)
    args = ap.parse_args()
    repo = Path(args.external_repo).resolve()
    outpath = Path(args.output).resolve()

    commit = subprocess.check_output(["git", "-C", str(repo), "rev-parse", "HEAD"], text=True).strip()
    UpstreamModel, source = load_upstream_reference(repo)

    source_tokens = [
        "pk_weyl_weyl", "pk_weyl_dnonu", "pk_dnonu_dnonu",
        "cosmo.chi", "cosmo.z_of_chi", "cosmo.H",
        "cosmo.comoving_angular_diameter_distance", "cosmo.Omega_m",
        "cosmo.H0", "cosmo.curvature", "cosmo.chi_star",
    ]
    source_checks = {token: token in source for token in source_tokens}
    source_pass = all(source_checks.values())

    cosmo = MockCosmo()
    tracers = [MockDndz(0.75, 0.42, pc=False), MockDndz(1.35, 0.55, pc=True)]
    pww = MockPower(2.2e-8, 0.11, 0.0010)
    pwm = MockPower(1.7e-4, 0.17, 0.0015)
    pmm = MockPower(1800.0, 0.08, 0.0008)

    ref_model = UpstreamModel(
        zmax=ZMAX,
        zmin=ZMIN,
        k_max=KMAX,
        N_integration=NINT,
        cross_correlation_redshift_correction=None,
        cleft_interp_helper=None,
        ell_vals=ELL,
        want_gg_cross=False,
        ell_vals_clkk=None,
    )
    reference = ref_model.compute_raw_spectra(
        cosmo, tracers, pww, pwm, pmm,
        cleft_interpolations_dtot_dnonu=None,
        cleft_interpolations_dnonu_dnonu=None,
        fid_bias_evol_list=None,
    )
    dsir = compute_raw_no_cleft(
        cosmo, tracers, pww, pwm, pmm,
        ell_vals=ELL, zmin=ZMIN, zmax=ZMAX, kmax=KMAX, n_integration=NINT,
    )

    equivalence_pass, equivalence = compare_maps(component_map(reference), component_map(dsir))
    independence_pass, independence = independence_control(cosmo, tracers, pww, pwm, pmm)
    provenance_pass = commit == PINNED_COMMIT
    passed = bool(provenance_pass and source_pass and equivalence_pass and independence_pass)
    status = (
        "PASS_SOLVER_NEUTRAL_RAW_PROJECTION_EQUIVALENCE_V0_1"
        if passed else "FAIL_SOLVER_NEUTRAL_RAW_PROJECTION_EQUIVALENCE_V0_1"
    )

    result = {
        "experiment": "Exp066A",
        "status": status,
        "scope": "algebraic raw-projection bridge only; no ACT fit, no G7 law, no withheld family",
        "pinned_external_repo": "ACTCollaboration/unWISExLens_lklh",
        "pinned_commit": commit,
        "frozen_numerics": {
            "ell": ELL.tolist(), "zmin": ZMIN, "zmax": ZMAX,
            "kmax_Mpc^-1": KMAX, "gauss_legendre_order": NINT,
            "equivalence_tolerance": TOL,
        },
        "checks": {
            "provenance": {"pass": provenance_pass, "expected_commit": PINNED_COMMIT},
            "source_interface": {"pass": source_pass, "tokens": source_checks},
            "raw_component_equivalence": {"pass": equivalence_pass, "components": equivalence},
            "independent_spectrum_controls": {"pass": independence_pass, "controls": independence},
        },
        "solver_neutral_interface": {
            "geometry": ["chi(z)", "z_of_chi(chi)", "H(z)[Mpc^-1]", "f_K(chi)[Mpc]", "H0[Mpc^-1]", "h", "Omega_m", "curvature[Mpc^-2]", "chi_star[Mpc]"],
            "spectra": ["P_WW(k,z)", "P_Wm(k,z)", "P_mm(k,z)"],
            "spectral_k_unit": "Mpc^-1",
            "poisson_reconstruction_forbidden": True,
        },
        "next_step": "If PASS, Exp066B may bind nuisance/CLEFT evaluation and official bandwindow/transfer operators on a reference cosmology before any G7 relation search.",
        "gate_state": {"G7": "OPEN", "G8": "OPEN", "G9": "OPEN"},
    }
    outpath.parent.mkdir(parents=True, exist_ok=True)
    outpath.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
