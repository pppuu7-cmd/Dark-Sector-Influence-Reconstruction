# Exp073EU — WW_S0_S1 sequential-spill serialized-public-BPW exact qualifier v0.1

**Prospectively preregistered:** 2026-09-06 after terminal Exp073ET v0.1 support FAIL, while Exp073EN remains unresolved/in progress and before any Exp073EL activation.

**Class:** hosted-only support qualifier, accounting `+0/+0`; no WW science authority.

## Motivation and immutable interpretation of Exp073ET
Exp073ET v0.1 must remain a terminal support FAIL because its preregistration required direct in-memory BPW to equal BPW after FITS serialization/reload. Its terminal evidence nevertheless localized the only mismatches to that cross-state comparison (`max_abs_difference = 1.1102230246251565e-16`). All arithmetic-equivalence comparisons before serialization passed exactly: ALM spill/reload, ordered mask PCL, full unbinned MCM, in-memory full BPW, and in-memory selected `EE<-EE`.

This is consistent with the pre-existing serialized-state investigation (DV/DY/etc.) and, critically, Exp073ET's low-route reload hashes equal the independently frozen earlier Exp073ER public-reload hashes. Exp073EU does not reclassify or weaken ET. It asks the correct state-matched question required by the future science route.

## Frozen source and geometry
- NaMaster/PyMaster exact source commit `24365fa59a38c15732f4f37e8b29265b75c442d5` (2.7).
- Ordered distinct spin-2 `S0 -> S1`.
- NSIDE=16, lmax=lmax_mask=47.
- Edges `[0,6,12,18,24,30,36,42,48]`.
- MASTER normalization, no purification, no Toeplitz approximation, unit beams, `is_teb=False`.
- Same deterministic distinct masks used by EK/ER/ET.

## Independently pre-existing expected post-serialization hashes
These values are frozen from Exp073ER terminal PASS, which predates Exp073EU and predates the ET interpretation above:
- full public BPW `[4,8,4,48]`: `bf656c5f0493dc44d6c42b31b804f04f6893b7fc4895e92b99cefc356b10b884`;
- selected public `EE<-EE [8,48]`: `336a0b57fe734a2f17a4a0844db1a18fc43887abf7556fb63009ee4a3de5f607`.

## Stock state and low-memory state
Stock route:
1. ordinary simultaneous public fields;
2. public `compute_coupling_matrix`;
3. capture stock in-memory MCM/BPW;
4. `write_to` FITS;
5. destroy workspace;
6. fresh public `read_from(..., read_unbinned_MCM=True)`;
7. public `get_bandpower_windows()`.

Low-memory route:
1. sequential exact ALM spill/reload;
2. ordered `healpy.alm2cl`;
3. exact internal `nmtlib.comp_coupling_matrix` argument sequence copied from PyMaster 2.7;
4. capture low in-memory MCM/BPW;
5. `write_to` a distinct FITS;
6. destroy workspace;
7. fresh public `read_from(..., read_unbinned_MCM=True)`;
8. public `get_bandpower_windows()`.

## Exact PASS requirements
`PASS_EXP073EU_WW_S0_S1_SEQUENTIAL_SPILL_SERIALIZED_PUBLIC_BPW_EXACT_V0_1` requires:
- ALM0 and ALM1 spill/reload exact by shape, canonical complex128 SHA256, `numpy.array_equal`, max diff 0.0;
- ordered stock-vs-low mask PCL exact;
- stock-vs-low in-memory full MCM exact;
- stock-vs-low in-memory full BPW exact;
- stock-vs-low in-memory selected EE exact;
- stock fresh-reload MCM equals low fresh-reload MCM exactly;
- stock fresh-reload full public BPW equals low fresh-reload full public BPW exactly;
- stock fresh-reload selected EE equals low fresh-reload selected EE exactly;
- both stock and low fresh-reload full/selected hashes equal the pre-existing Exp073ER hashes above;
- all arrays finite;
- masks distinct;
- no tolerance, allclose, rounding, smoothing, averaging or rescue.

The known pre-serialization-vs-post-serialization last-bit difference is recorded diagnostically but is explicitly **not** an equality being tested by this state-matched qualifier. This is not a relaxed numerical tolerance: both compared authority-candidate routes must still be exactly equal within the same serialized public state.

## Frontier effect
EU PASS would satisfy the arithmetic/state prerequisite for a superseding prospective Exp073EL resource-path admission. ET v0.1 remains historical FAIL `+0/+0`. Neither ET nor EU creates science authority.
