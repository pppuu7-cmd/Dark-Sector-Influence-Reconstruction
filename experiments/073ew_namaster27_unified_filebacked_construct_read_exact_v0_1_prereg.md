# Exp073EW — NaMaster 2.7 unified file-backed construction + FITS-read exact qualifier v0.1

Prospectively preregistered 2026-09-06 while Exp073EN remains unresolved. Hosted-only support, accounting `+0/+0`; no science authority.

## Question
Can the already ER-qualified v0.2 read-storage patch be used as a **single build** for both MCM construction and serialized public reload without any numerical change relative to stock PyMaster 2.7?

This matters operationally because Exp073EL v0.2 otherwise requires one Exp073EM/v0.1 build for construction and a second v0.2 build for readback.

## Frozen identities
- exact NaMaster/PyMaster source `24365fa59a38c15732f4f37e8b29265b75c442d5`;
- patch `patches/namaster-v2.7-dsir-filebacked-mcm-read-v0.2.patch`;
- patch blob `d534b698f9131688d263eedcef27260386c58641`;
- ordered distinct spin-2 S0->S1 small-NSIDE geometry identical to ER/EU: NSIDE=16, lmax=47, 8 bands edges `[0,6,12,18,24,30,36,42,48]`;
- expected unbinned MCM backing bytes `294,912`;
- pre-existing ER serialized-public expected hashes: full BPW `bf656c5f0493dc44d6c42b31b804f04f6893b7fc4895e92b99cefc356b10b884`, selected EE `336a0b57fe734a2f17a4a0844db1a18fc43887abf7556fb63009ee4a3de5f607`.

## Stock route
Using an unmodified exact-source build:
1. public `NmtWorkspace.compute_coupling_matrix(f0,f1,b)`;
2. capture in-memory full MCM, full public BPW and selected EE;
3. `write_to` FITS;
4. destroy workspace;
5. fresh `read_from(..., read_unbinned_MCM=True)`;
6. capture reload MCM/full BPW/selected EE.

## Patched unified route
Using one exact-source build with the v0.2 patch and `DSIR_NMT_FILEBACKED_MCM=1`:
1. public `compute_coupling_matrix(f0,f1,b)`;
2. while workspace is alive, prove exactly one regular mapped `dsir-nmt-mcm-*` file, exact size `294,912`, visible in `/proc/self/maps`;
3. capture in-memory MCM/full BPW/selected EE and `write_to` FITS;
4. destroy workspace and prove construction backing cleanup;
5. in the same patched build but a fresh workspace, public `read_from(..., read_unbinned_MCM=True)`;
6. independently prove a new exact-size regular-file mmap for the read path;
7. capture reload MCM/full BPW/selected EE;
8. destroy workspace and prove read-backing cleanup.

## Exact PASS
`PASS_EXP073EW_NAMASTER27_UNIFIED_FILEBACKED_CONSTRUCT_READ_EXACT_V0_1` requires:
- stock construction-state MCM == patched construction-state MCM exactly;
- stock construction-state full BPW == patched construction-state full BPW exactly;
- stock construction-state selected EE == patched construction-state selected EE exactly;
- stock reload MCM == patched reload MCM exactly;
- stock reload full BPW == patched reload full BPW exactly;
- stock reload selected EE == patched reload selected EE exactly;
- patched construction and patched read each independently prove exact regular-file mmap size and complete cleanup;
- both reload full/selected hashes equal the older ER expected hashes;
- all arrays finite, masks distinct;
- no tolerance/allclose/rounding/smoothing/averaging/rescue.

Cross-state in-memory-vs-reload equality is not a criterion; its known last-bit difference is a separate serialized-state property already established independently. Every equality above is state-matched.

A failure is storage support FAIL `+0/+0`, never dark-sector science failure.

## Frontier effect
A PASS permits future Exp073EL v0.2 / WW_S0_S1 science implementation to use one v0.2 patched PyMaster build for both construction and reload, subject to all other EL/EO/frontier constraints.
