# Exp073DW — WW_S0_S1 serialized→reloaded cross-field qualifier v0.1

Status: prospectively preregistered support-only repair of Exp073DU v0.1; accounting `+0/+0`; no science authority.

## Motivation and immutable predecessor
Exp073DU run `33955300558 / 101277450615` emitted `FAIL_EXP073DU_WW_S0_S1_CROSSFIELD_SMALLNSIDE_EXACT_ADAPTER_V0_1`. Its raw artifact showed that distinct S0/S1 construction, cross-vs-auto distinction, shapes, finiteness and no-tolerance checks passed; only exact adapter-vs-direct checks failed. The adapter consumed the serialized `w01.fits`, while DU v0.1 compared it to the pre-serialization in-memory workspace. Exp073EA had already established that the frozen saved-LU adapter is exact to the official PyMaster serialized→reloaded state and that pre-serialization state can differ at last bits. DU v0.1 remains historical QUALIFIER_FAIL `+0/+0`; it is never rewritten.

## Frozen purpose
Test the same distinct-field S0→S1 construction, but compare the production adapter only against an official PyMaster `NmtWorkspace().read_from(w01.fits)` reference. The pre-serialization in-memory result is retained as a diagnostic negative control and is not a PASS condition.

## Frozen geometry/runtime
Synthetic deterministic distinct masks; NSIDE=16; nl=48; band edges `[0,6,12,18,24,30,36,42,48]`; spin-2 fields; ncls=4; full shape `[4,8,4,48]`; selected `wins[0,:,0,:] = EE<-EE`; canonical selected `<f8 [8,48]`; PyMaster/NaMaster 2.7; no DES science data; hosted only.

## Frozen implementation lineage
Production adapter blob `d6f20600d6a206dd9fbb254b382e71a49c6b3c07`; shared adapter blob `dafe86086a470c852106f0d4ecccbda1d389e397`; downstream blob `be4f381de4c5c043a9c0fcd107e63ef3f2079578`; PyMaster `get_bandpower_windows` source SHA256 `442e23eb542087566689271ad1c897d5da45f5b76e39def05b37d93b0098178f`.

## PASS contract
Only token: `PASS_EXP073DW_WW_S0_S1_SERIALIZED_RELOAD_EXACT_ADAPTER_V0_1`.
PASS requires simultaneously: distinct masks and field objects; serialized/reloaded W01 coupling matrix differs exactly from W00 and W11; adapter full window `numpy.array_equal` to reloaded-W01 `get_bandpower_windows()`; adapter selected EE exact equal to reloaded selected EE; selected payload SHA256 exact equal; exact shapes; all values finite; adapter receipt `no_tolerance_rescue=true`; no tolerance/allclose/rounding/smoothing/averaging rescue. Pre-serialization-vs-reloaded equality is diagnostic only and must be recorded.

On PASS: `classification=QUALIFIER_PASS`, `science_gate_scored=false`, `ww_s0_s1_authority_created=false`, accounting `+0/+0`. Any failed required check is qualifier FAIL `+0/+0`; infrastructure/runtime failure is infrastructure `+0/+0`.

Exp073DW cannot alter Exp073DT or create WW authority. Full-resolution WW_S0_S1 remains blocked on valid WW_S0_S0 authority, required Exp073EB provenance closure, this repaired qualifier being consumed, and zero competing self-hosted heavy work.
