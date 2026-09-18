# DSIR-I authoritative bibliography metadata audit — 2026-08-28

**Purpose:** verify every cited submission-bibliography record against an authoritative journal and/or arXiv record before release-candidate freeze. This is a publication-quality audit only; it does not promote scientific claims.

## Current verdict

`PASS_METADATA_VERIFIED_25_OF_25__FINAL_FRESH_LITERATURE_GATE_SEPARATE`

The current DSIR-I submission bibliography contains **25 unique BibTeX entries, all 25 are cited in the assembled manuscript, and there are 0 working-only uncited records**. Each cited record has now been checked against an authoritative journal page and/or arXiv record. Metadata normalization found and corrected two published-title issues and two missing arXiv identifiers. The separate final fresh literature/citation-forward novelty refresh remains mandatory immediately before release-candidate freeze.

## Status convention

- `VERIFIED_JOURNAL` — authors/title and available journal volume/article or page range/DOI checked against the journal record.
- `VERIFIED_ARXIV` — authors/title/arXiv identifier checked against arXiv.
- `VERIFIED_JOURNAL+ARXIV` — both publication and arXiv identities checked where useful for the release record.

## Complete cited-record audit

| BibTeX key | Status | Authoritative identity checked |
|---|---|---|
| `Kunz2007` | VERIFIED_JOURNAL+ARXIV | Phys. Rev. D **80**, 123001 (2009), DOI `10.1103/PhysRevD.80.123001`, arXiv `astro-ph/0702615`. The submission bibliography now uses the published PRD title. |
| `Hu1998` | VERIFIED_JOURNAL+ARXIV | Astrophys. J. **506**, 485--494 (1998), DOI `10.1086/306274`, arXiv `astro-ph/9801234`. |
| `HuSawicki2007` | VERIFIED_JOURNAL+ARXIV | Phys. Rev. D **76**, 104043 (2007), DOI `10.1103/PhysRevD.76.104043`, arXiv `0708.1190`. The submission bibliography now uses the published APS title `Parametrized post-Friedmann framework for modified gravity`. |
| `BertschingerZukin2008` | VERIFIED_JOURNAL+ARXIV | Phys. Rev. D **78**, 024015 (2008), DOI `10.1103/PhysRevD.78.024015`, arXiv `0801.2431`. |
| `Gubitosi2012` | VERIFIED_JOURNAL+ARXIV | JCAP **02** (2013) 032, DOI `10.1088/1475-7516/2013/02/032`, arXiv `1210.0201`. |
| `BelliniSawicki2014` | VERIFIED_JOURNAL+ARXIV | JCAP **07** (2014) 050, DOI `10.1088/1475-7516/2014/07/050`, arXiv `1404.3713`. |
| `HojjatiEtAl2012` | VERIFIED_JOURNAL+ARXIV | Phys. Rev. D **85**, 043508 (2012), DOI `10.1103/PhysRevD.85.043508`, arXiv `1111.3960`. |
| `AmaraRefregier2014` | VERIFIED_JOURNAL+ARXIV | Phys. Rev. D **89**, 083501 (2014), DOI `10.1103/PhysRevD.89.083501`, arXiv `1309.5955`. |
| `vonMarttens2020` | VERIFIED_JOURNAL+ARXIV | Phys. Rev. D **104**, 043515 (2021), DOI `10.1103/PhysRevD.104.043515`, arXiv `2011.10846`. |
| `EscamillaEtAl2023` | VERIFIED_JOURNAL+ARXIV | JCAP **11** (2023) 051, DOI `10.1088/1475-7516/2023/11/051`, arXiv `2305.16290`. |
| `ZanolettiLeonard2025` | VERIFIED_JOURNAL+ARXIV | Phys. Rev. D **112**, 063547 (2025), DOI `10.1103/ng53-k782`, arXiv `2503.20951`. |
| `PetriMarraVonMarttens2026` | VERIFIED_JOURNAL+ARXIV | Phys. Rev. D **113**, 023504 (2026), DOI `10.1103/3k93-p1n8`, arXiv `2508.17955`; publication date 2026-01-06. |
| `Naeem2026` | VERIFIED_JOURNAL | Annals of Physics **490**, 170466 (2026), DOI `10.1016/j.aop.2026.170466`. The BibTeX title preserves `Lambda`CDM with explicit math mode so the journal `.bbl` compiles safely. |
| `BodeOstrikerTurok2001` | VERIFIED_JOURNAL+ARXIV | Astrophys. J. **556**, 93--107 (2001), DOI `10.1086/321541`, arXiv `astro-ph/0010389`. |
| `VielEtAl2005` | VERIFIED_JOURNAL+ARXIV | Phys. Rev. D **71**, 063534 (2005), DOI `10.1103/PhysRevD.71.063534`, arXiv `astro-ph/0501562`. |
| `PoulinSerpicoLesgourgues2016` | VERIFIED_JOURNAL+ARXIV | JCAP **08** (2016) 036, DOI `10.1088/1475-7516/2016/08/036`, arXiv `1606.02073`. |
| `KoppSkordisThomas2016` | VERIFIED_JOURNAL+ARXIV | Phys. Rev. D **94**, 043512 (2016), DOI `10.1103/PhysRevD.94.043512`, arXiv `1605.00649`. |
| `ThomasKoppMarkovic2019` | VERIFIED_JOURNAL+ARXIV | MNRAS **490**(1), 813--831 (2019), DOI `10.1093/mnras/stz2559`, arXiv `1905.02739`. |
| `PaceSakrTutusaus2020` | VERIFIED_JOURNAL+ARXIV | Phys. Rev. D **102**, 043512 (2020), DOI `10.1103/PhysRevD.102.043512`, arXiv `1912.12250`. |
| `SakrLopezSanchez2026` | VERIFIED_ARXIV | arXiv `2601.16943`, `Forecast on the generalised dark matter properties from a Euclid-like survey`. |
| `Bashinsky2007DarkKinetics` | VERIFIED_ARXIV | arXiv `0707.0692`, `Mapping Cosmological Observables to the Dark Kinetics`. |
| `SaponeKunz2009Fingerprinting` | VERIFIED_JOURNAL+ARXIV | Phys. Rev. D **80**, 083519 (2009), DOI `10.1103/PhysRevD.80.083519`, arXiv `0909.0007`. |
| `SaponeKunzAmendola2010Fingerprinting` | VERIFIED_JOURNAL+ARXIV | Phys. Rev. D **82**, 103535 (2010), DOI `10.1103/PhysRevD.82.103535`, arXiv `1007.2188`. |
| `SaponeMajerotto2012Fingerprinting` | VERIFIED_JOURNAL+ARXIV | Phys. Rev. D **85**, 123529 (2012), DOI `10.1103/PhysRevD.85.123529`, arXiv `1203.2157`. |
| `ReboucasEtAl2026Sound` | VERIFIED_ARXIV | arXiv `2606.00411`, `The sound of dynamical dark energy and modified gravity`. |

## Controlled normalization already applied

The following release-facing corrections were made without changing scientific use of the references:

1. `Kunz2007`: switched the title from the arXiv/preprint wording to the published PRD title.
2. `HuSawicki2007`: switched the title to the published APS title.
3. `KoppSkordisThomas2016`: added arXiv `1605.00649`.
4. `PaceSakrTutusaus2020`: added arXiv `1912.12250`.
5. `Naeem2026`: retained the published `Lambda`CDM title while placing the Lambda symbol in explicit BibTeX math mode so `JHEP.bst` produces compilable LaTeX.
6. Four working-only uncited records (`HeymansEtAl2021`, `BarthelemyEtAl2022`, `GuEtAl2025`, `GuEtAl2026`) were removed from the **submission** bibliography rather than cited artificially.

## Machine integrity state

A deterministic paper-build after submission-bibliography cleanup reported:

- `25` unique cited keys;
- `35` citation-key occurrences;
- `25` unique BibTeX entries;
- `0` duplicate keys;
- `0` missing cited keys;
- `0` uncited submission-bibliography entries.

The JCAP and self-contained archive gates are required to remain green after the final BibTeX normalization; they are not replaced by this metadata audit.

## Gate boundary

### Closed by this file

- authoritative metadata review for every **currently cited** submission record;
- removal of working-only uncited records from the submission bibliography;
- controlled normalization of identified metadata issues.

### Still open and intentionally separate

- **final fresh 2026 literature and citation-forward novelty refresh immediately before release-candidate freeze**;
- final JCAP/offline-archive confirmation on the exact release-candidate content identity.

No novelty priority claim is strengthened by this metadata audit. G7, G8 and G9 remain OPEN.
