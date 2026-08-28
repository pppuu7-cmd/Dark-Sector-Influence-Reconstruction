# DSIR-I authoritative bibliography metadata audit — 2026-08-28

**Purpose:** verify cited metadata against authoritative journal or arXiv records before release-candidate freeze. This file records verification state only; it does not promote scientific claims.

## Status convention

- `VERIFIED_JOURNAL` — title/authors/journal/volume/article or page range/DOI checked against the journal page.
- `VERIFIED_ARXIV` — title/authors/arXiv identifier checked against arXiv.
- `OPEN` — still requires authoritative verification before final freeze.

## Verified batch A

| BibTeX key | Status | Verified metadata |
|---|---|---|
| `ZanolettiLeonard2025` | VERIFIED_JOURNAL | Phys. Rev. D **112**, 063547 (2025); DOI `10.1103/ng53-k782`; title and authors match APS. |
| `PetriMarraVonMarttens2026` | VERIFIED_JOURNAL | Phys. Rev. D **113**, 023504 (2026); published 2026-01-06; DOI `10.1103/3k93-p1n8`; title and authors match APS. |
| `vonMarttens2020` | VERIFIED_JOURNAL | Phys. Rev. D **104**, 043515 (2021); DOI `10.1103/PhysRevD.104.043515`; title and journal metadata match APS. |
| `KoppSkordisThomas2016` | VERIFIED_JOURNAL + VERIFIED_ARXIV | Phys. Rev. D **94**, 043512 (2016); DOI `10.1103/PhysRevD.94.043512`; arXiv `1605.00649`. |
| `ThomasKoppMarkovic2019` | VERIFIED_JOURNAL | MNRAS **490**(1), 813--831 (2019); DOI `10.1093/mnras/stz2559`; title/authors/pages verified at Oxford Academic. |
| `PaceSakrTutusaus2020` | VERIFIED_JOURNAL + VERIFIED_ARXIV | Phys. Rev. D **102**, 043512 (2020); DOI `10.1103/PhysRevD.102.043512`; arXiv `1912.12250`. |
| `SakrLopezSanchez2026` | VERIFIED_ARXIV | arXiv `2601.16943`; title `Forecast on the generalised dark matter properties from a Euclid-like survey`; authors Ziad Sakr and Jessica N. López-Sánchez. |
| `Gubitosi2012` | VERIFIED_ARXIV | arXiv `1210.0201`; title and authors match the current BibTeX record. |
| `BelliniSawicki2014` | VERIFIED_ARXIV | arXiv `1404.3713`; title and authors match the current BibTeX record. |
| `Bashinsky2007DarkKinetics` | VERIFIED_ARXIV | arXiv `0707.0692`; title and author match. |
| `SaponeKunz2009Fingerprinting` | VERIFIED_ARXIV | arXiv `0909.0007`; title and authors match. |
| `EscamillaEtAl2023` | VERIFIED_ARXIV | arXiv `2305.16290`; title and author list match the current manuscript citation. |

## Metadata improvements identified

The current `references.bib` already carries correct journal DOI metadata for `KoppSkordisThomas2016` and `PaceSakrTutusaus2020`, but their arXiv identifiers are absent. Before the final freeze, add:

- `KoppSkordisThomas2016`: `eprint = {1605.00649}`, `archivePrefix = {arXiv}`, `primaryClass = {astro-ph.CO}`;
- `PaceSakrTutusaus2020`: `eprint = {1912.12250}`, `archivePrefix = {arXiv}`, `primaryClass = {astro-ph.CO}`.

These are bibliographic-completeness improvements only.

## Remaining work

1. Verify the remaining cited records against authoritative journal/arXiv pages.
2. Resolve whether every uncited BibTeX record belongs in the final submission bibliography.
3. Apply verified metadata corrections to `references.bib` in one controlled edit.
4. Re-run bibliography integrity and full JCAP compile after that edit.
5. Repeat a fresh literature/citation-forward search immediately before release-candidate freeze.

The bibliography gate remains **OPEN** until every cited record is verified and the final JCAP build remains green after metadata normalization.
