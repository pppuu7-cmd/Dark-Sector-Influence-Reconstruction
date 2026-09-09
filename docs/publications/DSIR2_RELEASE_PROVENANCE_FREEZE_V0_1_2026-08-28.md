# DSIR-2 release provenance freeze v0.1

**Date:** 2026-08-28  
**Scope:** repository-for-writing / internal manuscript release provenance.  
**Scientific values changed:** none.

This file closes the remaining provenance follow-ups identified in `DSIR2_CLAIM_TO_EVIDENCE_AUDIT_V0_1_2026-08-28.md`. It records exact immutable GitHub Actions identities for the manuscript-critical provider/support chain and the Exp071C prospective known-sector control.

## Publication QA binding

Latest audited manuscript-branch head before this provenance-only commit:

- branch: `article2-manuscript-start-2026-08-28`
- head: `10da3f6006597d85d73bebe4c857175435b5c17b`
- Article-2 publication-QA run: `33197314801`
- job: `98937646345`
- result: `success`
- QA artifact: `9696357137`
- artifact name: `dsir2-publication-qa-direct-v03-f6889621dde60000cd906cba8d2413a8e7237228`
- artifact SHA256: `02d86503b35d78f62e445bc1a2dd59a883b7866e1194f8ffd8ab06f93e7fdf47`

The QA job completed all frozen publication steps successfully:

1. generated Figures 1–4 v0.3;
2. verified figure inventory and file integrity;
3. compiled the journal-neutral LaTeX manuscript with BibTeX;
4. rejected unresolved citations/references;
5. recorded release-QA hashes;
6. uploaded the immutable QA bundle.

## Exp071A — common provider support

- run: `33027562195`
- job: `98372366778`
- artifact: `9629064009`
- artifact name: `exp071a-common-provider-support-f55c69015628ace2c030cdaadd5f61a26e720376`
- artifact SHA256: `4955a3a917992ad38423d9fe2dda3682822c7b86614950467faf5a46a7426675`
- run head SHA: `f55c69015628ace2c030cdaadd5f61a26e720376`
- manuscript role: certified common provider support, 495/495 frozen cells.

The earlier infrastructure-packaging failure remains historical and is not substituted for this successful scientific artifact.

## Exp071C — prospective known-sector F30 specificity control

- run: `33020201997`
- job: `98348450038`
- artifact: `9626235928`
- artifact name: `exp071c-known-sector-f30-specificity-da74d592fbcc2bba9cd223e924b245a3e52437e1`
- artifact SHA256: `ed486effa593a409640577f8cdde614d5fddfc95653eb4ca78c56ae69a234e5e`
- preregistered contract: `experiments/071c_known_sector_f30_specificity_control_prereg_v0_1.md`
- prospective freeze commit recorded by the job itself: `4180661fe3187c710c363cdbafac12de2dc70d41`
- checked-out DSIR tree recorded in the job: `da74d592fbcc2bba9cd223e924b245a3e52437e1`
- Actions artifact metadata head SHA: `7d3edf17dcc42731899a314ab9edde7a9c79b148`
- pinned upstream CLASS: `e85808324f51fc694d12e3ed7439552a3c3f9540`
- evaluator terminal status: `COMPLETE_KNOWN_SECTOR_F30_SPECIFICITY_CONTROL_V0_1`
- primary classification: `F30_DARK_SPECIFICITY_WEAKENED_BY_KNOWN_SECTOR_CONTROL`
- K1 full+leave-one-z PASS: `false`
- K2 full+leave-one-z PASS: `true`

The job log explicitly states that the K1/K2 grids and classification logic were frozen at commit `4180661f...` before the spectra were generated. The artifact digest above is the terminal ZIP digest and must not be conflated with a parent-training artifact digest.

## Exp072A — ACT x unWISE angular support leakage

- run: `33029362485`
- job: `98378044465`
- artifact: `9629763833`
- artifact name: `exp072a-act-unwise-angular-support-leakage-d25431771dcfbd863c37057b3e9b3e13184e3bc7`
- artifact SHA256: `9ecf7d61b4db5e091392a23f508cd5dd3d04dafe32a4a66d1256a70d9947701d`
- run head SHA: `553f6867f1cf71d4661a9f7b1f739a970648d05d`
- manuscript role: retained observational dimension 0/26 under the frozen 5% leakage rule.

## Exp072C — coupled low-z / high-k frontier

- run: `33031427090`
- job: `98384598473`
- artifact: `9630407069`
- artifact name: `exp072c-joint-lowz-highk-frontier-b442cddd6ba032d1261a0994bc1c4f5cf899a9f7`
- artifact SHA256: `0e726d9f12b2b8951a4d2598b3723d54db1a14c09070d8e8770d5256773f2a71`
- run head SHA: `b442cddd6ba032d1261a0994bc1c4f5cf899a9f7`
- manuscript role: planning frontier near `z_min=0.0087345858`, `k_max=4.8182610974 Mpc^-1`.

## Exp073A — linear-route eligibility

- run: `33032781761`
- job: `98388840817`
- artifact: `9630897385`
- artifact name: `exp073a-gr-linear-perturbativity-eligibility-03c9d0281a6ea780d29c6fb4a689dbd55e51fdf5`
- artifact SHA256: `0f2212d691c38c3e953d2a0d823b498a5557b9485fc759079719000cdc48cb25`
- run head SHA: `03c9d0281a6ea780d29c6fb4a689dbd55e51fdf5`
- manuscript role: current linear/no-CLEFT observational route ineligible under the frozen criterion.

## Exp073J-BOSS — finite operator component

- run: `33042052616`
- job: `98417620281`
- artifact: `9634226231`
- artifact name: `exp073j-boss-component-support-1bd022ffca543361d265a72b782ef96fe069d2ce`
- artifact SHA256: `239b198c1adfc21333779ef1efb597885710bddd593b380a67ac6dd1399daa65`
- run head SHA: `1bd022ffca543361d265a72b782ef96fe069d2ce`
- manuscript role: non-classifying finite-matrix BOSS component with 54/240 retained rows.

## Exp073L — KiDS extended-asymptotic support

- run: `33049366874`
- job: `98440829219`
- artifact: `9637070322`
- artifact name: `exp073l-kids-extended-asymptotic-1c7064bf88afb868af7691eb33520c165ac3a245`
- artifact SHA256: `03a8f63155c40180c81b6472828210408b472463aec244fff8c442ad7cd7c684`
- run head SHA: `1c7064bf88afb868af7691eb33520c165ac3a245`
- manuscript role: examined KiDS finite-theta absolute-support route is non-normalizable under the frozen extended asymptotic test.

## Central Exp071E-N provenance

The exact manuscript table remains authoritative for the central response-space chain:

`docs/publications/latex/article2/table2_provenance.tex`

It binds Exp071E/F/H/I/J/K/L/M/N to exact run, job, artifact and digest prefix. Full-digest terminal summaries remain preserved in the repository / Actions artifacts; no value in that table is modified by this freeze.

## Release interpretation boundary

This provenance closure does not promote any scientific claim. In particular it does not convert:

- oriented K2 ray separation into nuisance-line specificity;
- Exp071M transfer-null into physical inactivity;
- Exp071N theory-space overlap into survey inference;
- provider/support results into covariance-whitened distinguishability;
- any Article-2 result into G7/G8/G9 closure.

Current gate state remains:

- `G7=OPEN`
- `G8=OPEN`
- `G9=OPEN`

## Provenance verdict

`DSIR2_RELEASE_PROVENANCE_COMPLETE_FOR_REPOSITORY_WRITING_SCOPE_V0_1`

All provenance follow-ups previously marked for the manuscript-critical Article-2 evidence chain are now explicitly addressable from repository records without guessing missing run/artifact identities.
