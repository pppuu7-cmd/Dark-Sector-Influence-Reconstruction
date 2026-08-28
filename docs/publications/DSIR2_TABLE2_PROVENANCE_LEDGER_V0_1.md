# DSIR-2 Table 2 — provenance ledger v0.1

**Date:** 2026-08-28  
**Rule:** only identifiers recovered from immutable experiment summaries or canonical Article-2 records are listed. Missing fields remain explicit.

| Exp. | Role | Preregistration / binding | Run | Job | Artifact | SHA256 | Status |
|---|---|---|---:|---:|---:|---|---|
| 071A | common certified C3/C5 signed `mm/Wm/WW`; 495/495 cells | canonical claim matrix / provider audit | — | — | — | — | document-level provenance; exact Actions tuple not re-extracted |
| 071C | K2 known-sector F30 falsification | canonical claim matrix | 33020201997 | — | 9626235928 | — | run/artifact verified; do not infer missing prereg/job/hash |
| 071E | static Weyl+slip control | 220e73f6cd5b52746498731073bf7392f6917dd9 | 33177588360 | 98870121386 | 9688299959 | 8547908fdb215a444d29abbb797c3175ef5e51064e02dd7f59cec3903584581c | exact terminal summary |
| 071F | static matter+Weyl+slip control | 85daeca416ce8ed1e691008fd4178fd6bbf94d15 | 33178154667 | 98872091411 | 9688506671 | e03e72251ab8ed9e0fa820bdae31342dc718349d78713db5fcac06bf00cc6779 | exact terminal summary |
| 071H | finite-bin temporal K2+ control | 93bd51867d90fa346ce644deebe228e6d0d45697 | 33179056348 | 98875221176 | 9688888346 | 60d582b9f0249329c323066f248cbdc33f3c149966eb30317ecb2f3f22cda0a5 | exact terminal summary |
| 071I | source-audited CLASS `t_tot` K2+ control | 30797f97f9ee4d295dcaf1905d3647230b6fa1cc; I/O amendment 55ea3d6435767ecf570702b55d411a12eddd59b4 | 33181895623 | 98884913088 | 9690064470 | ba41e25e6bcdfd2c23c4c9c8bc48bf9ddd85d7776a2e5bb7976e2e061d531e14 | exact terminal summary |
| 071J | projected velocity-shape control | 306c19a4286ffc459fc2886097a8b70fa6df89e9 | 33182705074 | 98887703171 | 9690361647 | e77409ac72f1a28ad0808afcb6b4f6fdcc983501b452b9ab286aa049380bd805 | exact terminal summary |
| 071K | leave-one-k/z support robustness | 3910605e9b8f586ec8dcb8be045c37e83e5afdd3 | 33183729426 | 98891216832 | 9690784568 | 9ddf4c31219cad7b97f3aec569fcd50724b141404de8672daca7ab2606265948 | exact terminal summary |
| 071L | fresh K2− two-sided velocity-line falsification | 9927f46caefbcd991b2c2e7691f4923c6f7552f6 | 33184079909 | 98892438220 | 9690954372 | 6ec9cc4dfa7a94ecec8e4540cbecf034b19bfdc7b0c85b30ac92331b205f71d4 | exact terminal summary |
| 071M | K1 transfer-only representation-null control | e3c0c7315ccb78d0a292db765eda172113f664bd | 33185652795 | 98897856253 | 9691596312 | d0878a71adb7bbf97d7b00a67e306c0ae9c86b8b2e705cbafd00b354ede23b21 | exact terminal summary; `INVALID_FOR_SCIENCE_EXP071M` |
| 071N | K1 velocity-power recovery / two-sided line falsification | cfaf9d14fa734e155cab5dca028bc1a14d0afd46 | 33186048775 | 98899204160 | 9691720131 | 19ce8623c64faf2e9ebd1d38ce2db5eb394d0a941457b18a8b59508d558d00eb | exact terminal summary |

## Velocity solver pins

Exp071I binds the velocity chain to:

- official CLASS `lesgourg/class_public@e85808324f51fc694d12e3ed7439552a3c3f9540`;
- GDM CLASS `s-ilic/gdm_class_public@4c87916aab5ca124a68f1dd16f31846fc13d1829`.

The I/O-only extension reproduces immutable parent matter spectra with maximum relative difference `0.0` against `1e-10`.

## Applicability chain — document-level provenance

| Group | Terminal fact | Publication source |
|---|---|---|
| Exp072A | ACT×unWISE first route: retained observational dimension 0 under frozen 5% leakage rule | current claim matrix / final science-closure audit |
| Exp072B/C + 073A | coupled low-z + high-k boundary; frontier near `z_min=0.0087345858`, `k_max=4.8182610974 Mpc^-1`; tested simple linear route remains ineligible through `Delta^2<=2` | current claim matrix / final closure audit |
| Exp073B–E | no independently certified nonlinear signed C3/C5 completion rescues the route | current claim matrix |
| Exp073I/J/K/L | finite operators alter admissibility: BOSS non-empty 54/240-row component; examined KiDS finite-theta route fails frozen criterion | final figure/table spec / current claim matrix |

Exact Actions tuples for this applicability chain should be copied into the release-candidate supplement only after a dedicated immutable-summary audit; they are not guessed here.

## Direct machine-readable evidence

`data/derived/exp071e_known_sector_joint_metric_direction_summary_v0_1.json`  
`data/derived/exp071f_known_sector_matter_weyl_slip_direction_summary_v0_1.json`  
`data/derived/exp071h_k2_finite_bin_growth_dual_provenance_summary_v0_1.json`  
`data/derived/exp071i_k2_gdm_total_velocity_direction_summary_v0_1.json`  
`data/derived/exp071j_total_velocity_shape_projection_summary_v0_1.json`  
`data/derived/exp071k_velocity_shape_support_localization_summary_v0_1.json`  
`data/derived/exp071l_two_sided_k2_velocity_shape_nuisance_summary_v0_1.json`  
`data/derived/exp071m_two_sided_k1_transfer_null_summary_v0_1.json`  
`data/derived/exp071n_two_sided_k1_velocity_power_shape_summary_v0_1.json`

## Release-candidate audit

Before submission, recover missing Exp071A/071C and Exp072/073 exact tuples from immutable summaries; verify every manuscript value against machine-readable data; recheck solver pins, units, k convention, redshift ordering, normalization and sign conventions; and preserve `INVALID_FOR_SCIENCE`, physical FAIL, null and infrastructure recovery as distinct states.

**Caption.** Provenance ledger for the experiments carrying the central DSIR-2 claims. Exact identifiers are shown only when recovered from immutable terminal summaries; document-level rows are labelled explicitly rather than reconstructed or guessed.
