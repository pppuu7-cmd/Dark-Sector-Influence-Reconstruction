# Exp073EA — saved-LU exact equivalence to official serialized/reloaded PyMaster state

Date: 2026-09-05
Scope: DSIR only; RTK/RQIR excluded.
Accounting: `+0/+0` support-only; no science authority and no production authorization.

## Authority and provenance

- preregistration commit: `2ca967b7bbbfc1deb3ce8355b2d32c4043fd9b61`;
- preregistration blob: `79a0fd70fcae3b25f1d25b1f46f3d35b15626fb1`;
- activation/source head: `758759bb8a1e8d14685b14b97d672b1b5532b3d1`;
- GitHub Actions run/job: `33956292805 / 101280130448`;
- artifact: `9966484239`;
- GitHub artifact ZIP SHA256: `7850d7c01ece7c2cb3ed8ea11b208a5600aea4a3fd68da81e2e17db9d06a1f61`;
- independently downloaded ZIP SHA256: `7850d7c01ece7c2cb3ed8ea11b208a5600aea4a3fd68da81e2e17db9d06a1f61`.

The hosted log verified the prospectively frozen prereg, diagnostic and saved-LU blobs, installed PyMaster/NaMaster 2.7, verified the frozen `get_bandpower_windows` source lineage, and ran only on GitHub-hosted compute. It did not dispatch, cancel, rerun or modify Exp073DT.

## Raw result classification

Frozen token: `PASS_EXP073EA_SAVED_LU_EXACT_OFFICIAL_RELOAD_STATE_V0_1`.

The downloaded raw terminal receipt was independently read and is consistent with the preregistered PASS rule:

- direct in-memory repeatability: exact SHA equality and `numpy.array_equal=true`;
- reload repeatability: exact SHA equality and `numpy.array_equal=true`;
- serialized numerical extensions pre/post: exact equality for `WSP_PRIMARY`, `MCM_BINNED`, and `MCM_PERM`;
- official pre/post reload windows: exact equality;
- saved-LU full output versus official reload-pre output: exact SHA equality and `numpy.array_equal=true`;
- selected `EE<-EE` saved-LU versus official reload-pre: exact equality;
- no tolerance/rounding/smoothing/averaging rescue.

Canonical saved-LU/reload-pre SHA256 is `aa883a13c305641e6e1aab5feca4692a8da1cdbcca16e8c124f12e601608d628` for the frozen small-NSIDE diagnostic geometry.

A distinct and important negative control is preserved: the original in-memory state is not bitwise identical to the official serialized/reloaded state (`max_abs_difference=1.1102230246251565e-16`, 2694 differing full-array elements; selected EE max difference `5.551115123125783e-17`, 328 differing elements). This is not rescued or averaged away.

## Interpretation boundary

Exp073EA establishes that the serialized/reloaded PyMaster numerical state is itself deterministic and that the frozen saved-LU route reproduces that official reload state bit-for-bit. It does **not** establish exact equality to the original pre-serialization in-memory workspace and does **not** create Article-3/WW scientific authority or authorize a production route by itself.

Exp073DT attempt 3 remains the sole self-hosted scientific authority process while run/job `33940588308 / 101274118640` is queued or in progress. Do not launch a competing home workload.
