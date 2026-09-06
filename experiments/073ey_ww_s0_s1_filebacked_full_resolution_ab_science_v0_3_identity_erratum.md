# Exp073EY v0.3 identity erratum — prereg blob binding only

Date frozen: 2026-09-06, before any Exp073EY static-audit PASS or numerical execution.

The authoritative scientific preregistration file `experiments/073ey_ww_s0_s1_filebacked_full_resolution_ab_science_v0_1_prereg.md` has Git blob `5790f7502370abffc5c450278520cc73c1f901f8` on the repository authority used for Exp073EY preparation.

The v0.2 implementation preregistration text accidentally recorded that scientific-prereg blob as `a2970a4332d415817b011c6ce73049f0083ada93`. No computation or static-audit PASS occurred under that mistaken identifier. This v0.3 note prospectively supersedes only that identity typo.

All v0.2 implementation rules remain unchanged: effective production driver v0.1 blob `1db1eabbdba492c476cc61d3c4d71147aa688384`; v0.2 wrapper blob `066847006b2ed9d712d2c22d3576a0d8887fa7bf`; public `read_from(..., read_unbinned_MCM=True) -> get_bandpower_windows()` route; exact `19327352832`-byte backing-file proof via `/proc/self/maps`; ordered `S0->S1`; exact `[0,:,0,:]`; six-stage durable checkpoints; exact SHA + `numpy.array_equal`; no tolerance/rescue.

A valid hosted static audit must bind scientific prereg blob `5790f7502370abffc5c450278520cc73c1f901f8`, this v0.3 erratum, v0.1/v0.2 driver blobs, and the home envelope blob. No other scientific or acceptance criterion is changed.
