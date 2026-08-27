# DSIR recovery checkpoint — Exp073G operator/BNT binding

**Date:** 2026-08-27

Exp073G remains preregistered and scientifically unevaluated. The exact public
source/operator identities, BNT convention, R0 geometry and pre-support
channel selections are now frozen in
`data/derived/g7/exp073g_kids_boss_bnt_operator_binding_v0_1.json`.

Key frozen choices:

- KiDS source: `KiDS-WL/Cat_to_Obs_K1000_P1@36676da44471979dacb779155d7e6e7212ae1f4f`;
- BNT source: `pltaylor16/x-cut@fcab1439c896ff4bff0fa21300366eef8107578c`;
- exact SHA256 identities for five source n(z), lens-bin-2 n(z), KiDS
  bandpower/operator files, and BOSS high-z radial/window files;
- source n(z) values interpreted at histogram midpoints and normalized before
  the continuous-bin BNT construction;
- localized BNT rows `[2,3,4]` retained; rows `[0,1]` excluded before leakage;
- only released BOSS high-z clustering and GGL lens bin 2 (`0.5<z<0.75`);
- exact KiDS bandpower filters: 8 log bands, ell 100--1500, theta 0.5--300
  arcmin, apodization width 0.5;
- exact BOSS high-z wedge radial/window operator;
- R0 geometry and physical `Mpc^-1` units inherited from Exp068B.

The pre-support candidate inventory is 156 coordinates. This is not a retained
dimension and no support fraction has been computed.

The new `src/dsir/bnt.py` module reproduces the public continuous-bin moment
construction and exposes deterministic nulling controls. Its focused tests pass
when invoked directly in the current environment; standard pytest remains for
repository CI.

Next permitted action: implement the exact positive broad-window support
envelopes, then run the frozen Exp073G 5% gate. Covariance and downstream G7/G8
quantities remain forbidden until a scientific support PASS.

G7 OPEN. G8 OPEN. G9 OPEN.
