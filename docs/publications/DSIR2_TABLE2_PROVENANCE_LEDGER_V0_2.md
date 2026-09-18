# DSIR-2 Table 2 — provenance ledger v0.2

**Date:** 2026-08-28  
**Supersedes for active publication work:** `DSIR2_TABLE2_PROVENANCE_LEDGER_V0_1.md`  
**Rule:** only immutable identifiers recovered from repository records or GitHub Actions are listed.

## A. Core response/falsification chain

| Exp. | Role | Preregistration / binding | Run | Job | Artifact | SHA256 / digest | Status |
|---|---|---|---:|---:|---:|---|---|
| 071A | common certified C3/C5 signed `mm/Wm/WW`; 495/495 cells | prereg `e670bff76868efb469f129a95b9dd6ba548ac82d`; execution binding `276655e876bcfefa7a9351b372fa3adc040a8318`; output-path repair `f55c69015628ace2c030cdaadd5f61a26e720376` | `33027562195` | `98372366778` | `9629064009` | `4955a3a917992ad38423d9fe2dda3682822c7b86614950467faf5a46a7426675` | exact final rerun; `PASS_COMMON_PHYSICAL_SUPPORT_MASK_V0_1`, 495/495 retained |
| 071C | known-sector F30 falsification | prereg `4180661fe3187c710c363cdbafac12de2dc70d41`; result merge `da74d592fbcc2bba9cd223e924b245a3e52437e1` | `33020201997` | `98348450038` | `9626235928` | `ed486effa593a409640577f8cdde614d5fddfc95653eb4ca78c56ae69a234e5e` | exact artifact recovery; `F30_DARK_SPECIFICITY_WEAKENED_BY_KNOWN_SECTOR_CONTROL` |
| 071E | static Weyl+slip control | `220e73f6cd5b52746498731073bf7392f6917dd9` | `33177588360` | `98870121386` | `9688299959` | `8547908fdb215a444d29abbb797c3175ef5e51064e02dd7f59cec3903584581c` | exact terminal summary |
| 071F | static matter+Weyl+slip control | `85daeca416ce8ed1e691008fd4178fd6bbf94d15` | `33178154667` | `98872091411` | `9688506671` | `e03e72251ab8ed9e0fa820bdae31342dc718349d78713db5fcac06bf00cc6779` | exact terminal summary |
| 071H | finite-bin temporal K2+ control | `93bd51867d90fa346ce644deebe228e6d0d45697` | `33179056348` | `98875221176` | `9688888346` | `60d582b9f0249329c323066f248cbdc33f3c149966eb30317ecb2f3f22cda0a5` | exact terminal summary |
| 071I | source-audited CLASS `t_tot` K2+ control | prereg `30797f97f9ee4d295dcaf1905d3647230b6fa1cc`; I/O amendment `55ea3d6435767ecf570702b55d411a12eddd59b4` | `33181895623` | `98884913088` | `9690064470` | `ba41e25e6bcdfd2c23c4c9c8bc48bf9ddd85d7776a2e5bb7976e2e061d531e14` | exact terminal summary |
| 071J | projected velocity-shape control | `306c19a4286ffc459fc2886097a8b70fa6df89e9` | `33182705074` | `98887703171` | `9690361647` | `e77409ac72f1a28ad0808afcb6b4f6fdcc983501b452b9ab286aa049380bd805` | exact terminal summary |
| 071K | leave-one-k/z support robustness | `3910605e9b8f586ec8dcb8be045c37e83e5afdd3` | `33183729426` | `98891216832` | `9690784568` | `9ddf4c31219cad7b97f3aec569fcd50724b141404de8672daca7ab2606265948` | exact terminal summary |
| 071L | fresh K2− two-sided velocity-line falsification | `9927f46caefbcd991b2c2e7691f4923c6f7552f6` | `33184079909` | `98892438220` | `9690954372` | `6ec9cc4dfa7a94ecec8e4540cbecf034b19bfdc7b0c85b30ac92331b205f71d4` | exact terminal summary |
| 071M | K1 transfer-only representation-null control | `e3c0c7315ccb78d0a292db765eda172113f664bd` | `33185652795` | `98897856253` | `9691596312` | `d0878a71adb7bbf97d7b00a67e306c0ae9c86b8b2e705cbafd00b354ede23b21` | exact terminal summary; `INVALID_FOR_SCIENCE_EXP071M` |
| 071N | K1 velocity-power recovery / two-sided line falsification | `cfaf9d14fa734e155cab5dca028bc1a14d0afd46` | `33186048775` | `98899204160` | `9691720131` | `19ce8623c64faf2e9ebd1d38ce2db5eb394d0a941457b18a8b59508d558d00eb` | exact terminal summary |

### Exp071A infrastructure history

The earlier Exp071A run `33027159066` completed the unchanged frozen evaluator and printed the same 495/495 PASS, but a relative output path caused the subsequent packaging/assert stage to miss the summary JSON. It remains permanently recorded as `INFRASTRUCTURE_PACKAGING_FAILURE_AFTER_COMPLETED_EVALUATOR`. The only repair was the absolute workspace output path. The final successful rerun above (`33027562195`) completed the evaluator, assert and immutable artifact upload successfully. The run-1 artifact must never be substituted for the final scientific artifact.

## B. Observation-support / finite-operator boundary

| Exp. | Role / terminal fact | Run | Job | Artifact | Artifact digest | Exact scientific boundary |
|---|---|---:|---:|---:|---|---|
| 072A | ACT×unWISE angular support leakage, 0/26 retained at frozen 5% | `33029362485` | `98378044465` | `9629763833` | `9ecf7d61b4db5e091392a23f508cd5dd3d04dafe32a4a66d1256a70d9947701d` | permanent `FAIL_ACT_UNWISE_ANGULAR_SUPPORT_LEAKAGE_MASK_V0_1`; extracted JSON SHA `56b96c096830bf8399ef18df41251a14ded00101a1f206b4419ccb6b5730abe3` |
| 072C | unique coupled low-z/high-k planning frontier | `33031427090` | `98384598473` | `9630407069` | `0e726d9f12b2b8951a4d2598b3723d54db1a14c09070d8e8770d5256773f2a71` | `z_min=0.0087345857837422`, `k_max=4.818261097432861 Mpc^-1`, 15/26 geometric route; planning geometry only, not provider certification |
| 073A | linear/no-CLEFT perturbativity eligibility | `33032781761` | `98388840817` | `9630897385` | `0f2212d691c38c3e953d2a0d823b498a5557b9485fc759079719000cdc48cb25` | `INELIGIBLE_GR_REFERENCE_LINEAR_ROUTE_EXP073A`; 0/26 retained for `Delta2<=0.5,1,2` |
| 073I | finite BOSS true-k matrix source binding | `33039228551` | `98408810891` | `9633204048` | `de203dc675ecac48ee2dfa42b79302459810b8bc5fc03eac6c112f1f79b61248` | source/matrix binding PASS; support fraction intentionally not computed at this stage |
| 073J BOSS component | finite-matrix physical-support component | `33042052616` | `98417620281` | `9634226231` | `239b198c1adfc21333779ef1efb597885710bddd593b380a67ac6dd1399daa65` | non-classifying component result: 54/240 rows retained; full Exp073J not classified by BOSS alone |
| 073J KiDS component | KiDS-BNT finite-theta support attempt | `33045812989` | `98429422683` | `9635628042` | `907ac6130afb2292eac6e8cdd03493bb0f3b4507d5042e1ac15c282bbb901d3b` | numerical completeness/convergence FAIL; reported 0/72 is explicitly non-classifying |
| 073L | KiDS absolute-response normalizability mechanism | `33049366874` | `98440829219` | `9637070322` | `03a8f63155c40180c81b6472828210408b472463aec244fff8c442ad7cd7c684` | `EXTENDED_LADDER_SUPPORTS_NONNORMALIZABLE_ABSOLUTE_RESPONSE_EXP073L`; absolute positive-support normalization grows ~`ell_max^(3/2)` |

### Observation-boundary interpretation

- Exp072A is a **scientific support FAIL**, not an infrastructure failure.
- Exp072C's frontier is a planning/geometry result only and must not be described as a validated linear science region.
- Exp073A blocks blind linear extension to the Exp072C frontier even under the relaxed `Delta2<=2` diagnostic.
- Exp073I only certifies the finite BOSS matrix/source binding; the 54/240 support count belongs to the later Exp073J BOSS component.
- The Exp073J KiDS component is a numerical-completeness failure, not a valid 0/72 physical-support classification.
- Exp073L supplies the stronger terminal mechanism result for the attempted KiDS P-independent absolute positive-support definition: it is non-normalizable under the frozen extended asymptotic test.

## C. Velocity solver pins

Exp071I binds the velocity chain to:

- official CLASS `lesgourg/class_public@e85808324f51fc694d12e3ed7439552a3c3f9540`;
- GDM CLASS `s-ilic/gdm_class_public@4c87916aab5ca124a68f1dd16f31846fc13d1829`.

The I/O-only extension reproduces immutable parent matter spectra with maximum relative difference `0.0` against `1e-10`.

## D. Direct evidence records

Core response chain:

- `recovery/2026-08-28_exp071c_known_sector_f30_exact_result_recovery.md`
- `data/derived/exp071e_known_sector_joint_metric_direction_summary_v0_1.json`
- `data/derived/exp071f_known_sector_matter_weyl_slip_direction_summary_v0_1.json`
- `data/derived/exp071h_k2_finite_bin_growth_dual_provenance_summary_v0_1.json`
- `data/derived/exp071i_k2_gdm_total_velocity_direction_summary_v0_1.json`
- `data/derived/exp071j_total_velocity_shape_projection_summary_v0_1.json`
- `data/derived/exp071k_velocity_shape_support_localization_summary_v0_1.json`
- `data/derived/exp071l_two_sided_k2_velocity_shape_nuisance_summary_v0_1.json`
- `data/derived/exp071m_two_sided_k1_transfer_null_summary_v0_1.json`
- `data/derived/exp071n_two_sided_k1_velocity_power_shape_summary_v0_1.json`

Applicability/support records include the Exp072A hard-fail result, Exp072C frontier result, Exp073A perturbativity result, `data/derived/g7/exp073i_finite_true_k_window_matrix_binding_result_v0_1.json`, `data/derived/g7/exp073j_boss_finite_matrix_component_support_v0_1_key_metrics.json`, `data/derived/g7/exp073j_kids_bnt_component_support_v0_1_key_metrics.json`, and `experiments/073l_kids_absolute_response_extended_asymptotic_result_v0_1.md`.

## E. Provenance closure state

All manuscript-critical Table-2 rows now have recovered immutable run/job/artifact provenance. The historical Exp071A run-1 packaging failure remains explicitly separate from the final successful rerun.

`ARTICLE2_MANUSCRIPT_CRITICAL_PROVENANCE_RECOVERED_V0_2`

## Caption draft

**Table 2.** Immutable provenance for the central DSIR-2 falsification and applicability chain. Run, job, artifact and cryptographic digests are reported from GitHub Actions or committed immutable result records. The ledger explicitly separates the first Exp071A infrastructure-packaging failure from its later successful frozen rerun, and distinguishes source-binding PASS, non-classifying component results, numerical-completeness failures and terminal scientific negative results.
