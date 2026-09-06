# Exp073EY v0.4 authority-binding erratum — Exp073EL artifact digest only

Date frozen: 2026-09-06, after the first Exp073EY launch attempt failed in hosted preflight and before any Exp073EY self-hosted numerical execution.

The first Exp073EY science workflow attempt `34006121336 / 101413506204` never reached the home runner (`home-science-ab` was skipped). The hosted preflight failed because the Exp073EL artifact digest copied into the EY prereg/workflow was wrong.

Authoritative live GitHub metadata for Exp073EL run `34005467421`, artifact `9980783193`, reports digest `sha256:c720233664be2e8a7666db6f95def0a2f13eb674732add6852f0c09e916e5e46`. An independent download of that exact artifact ZIP and independent SHA256 recomputation produced the same `c720233664be2e8a7666db6f95def0a2f13eb674732add6852f0c09e916e5e46`.

The raw Exp073EL receipt in that verified artifact remains unchanged and valid: token `PASS_EXP073EL_WW_S0_S1_FULLRES_RESOURCE_PATH_V0_2`, schema `dsir.exp073el.ww_s0_s1.resource_admission.v0.2`, classification `FULLRES_RESOURCE_PATH_READY`, accounting `+0/+0`, `science_gate_scored=false`, `ww_s0_s1_authority_created=false`, runner `DSIR-HOME-PC`, CPU affinity 8, configured WSL floor `memory>=6GB processors=8 swap>=16GB`, observed floors PASS, and no science result.

This v0.4 note prospectively supersedes only the incorrect EL artifact digest/string classification wording in the earlier EY preregistration. It does not change the Exp073EL run/artifact identity, token, resource criteria, or any Exp073EY scientific arithmetic, source order, geometry, checkpoint rule, exact comparison, or acceptance criterion.

The valid EY authority chain therefore binds:
- Exp073EO v0.2 admission run/artifact `34005373819 / 9980754356`, digest `sha256:0e1a4cff3b761fecc65d8e07df9e56f8109fd221fb4454746caa8c7d0f2fb4be`;
- Exp073EL run/artifact `34005467421 / 9980783193`, digest `sha256:c720233664be2e8a7666db6f95def0a2f13eb674732add6852f0c09e916e5e46`, token `PASS_EXP073EL_WW_S0_S1_FULLRES_RESOURCE_PATH_V0_2`.

Any rerun must first update only this provenance binding in the science workflow and then pass a new hosted workflow-inclusive static audit. The first failed preflight remains immutable infrastructure/provenance `+0/+0`; it is not a WW_S0_S1 scientific result.
