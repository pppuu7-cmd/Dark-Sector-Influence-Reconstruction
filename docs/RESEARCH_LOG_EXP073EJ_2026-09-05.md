# DSIR research log — Exp073EJ activation — 2026-09-05

Scope: DSIR only.

Exp073EI was fully consumed before this activation. Run/job `33988714617 / 101366943002`; artifact `9975963572`; GitHub digest and independently downloaded ZIP SHA256 both `52a77c087744e941bc27efb271cdf3047099aa1f5e7092f5296dda9733459def`; frozen classification `SOLVER_OPERATOR_MISMATCH +0/+0`. NumPy/public solver SHA256 are `0e5ac1d0a224ced720219fce5b92bcedd3eac61a1de0d30eecb3df554e2ee7f9` / `a7f161423662197eb7f7b9d751e54292f74348d11b6a76a705037d62782186c0`. No tolerance rescue and no WW authority.

Exp073EJ is prospectively frozen support-only `+0/+0`. It uses only the official PyMaster 2.7 `NmtWorkspace.decouple_cell` backend directly on every serialized->reloaded coupling-matrix column and compares the resulting composed operator bitwise against public `get_bandpower_windows()`. No manual P/Q, reconstructed inverse, alternate solver, alternate layout or tolerance is permitted. Frozen prereg blob `79b42e2fc2a7307a02f1fe6eb06808f60e50521a`; implementation blob `4451cfd7c35234303e7de9bc93e5d7a079626ecf`.

Exp073DT attempt 4 remains the sole authoritative self-hosted heavy process and must not be duplicated.