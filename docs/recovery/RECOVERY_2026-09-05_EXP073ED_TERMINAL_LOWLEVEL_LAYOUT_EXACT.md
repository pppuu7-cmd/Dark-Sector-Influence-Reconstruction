# DSIR immutable recovery — Exp073ED terminal LOWLEVEL_LAYOUT_EXACT

Date: 2026-09-05
Scope: DSIR only; RTK/RQIR excluded.
Accounting: +0/+0 support/diagnostic only.

Exp073ED hosted run/job `33976431383 / 101333833555` completed SUCCESS under frozen activation head `1b10a5ade1eb3e911da06269d452915f70e4959c`.

Artifact `9972458954` GitHub digest is `sha256:eb71f29599fe3b9a71848c65cc4bfd68fbee9e014c0149ff99b1fbde970431c9`; independently downloaded ZIP SHA256 is exactly the same.

Raw frozen token: `COMPLETE_EXP073ED_PYMASTER27_LOWLEVEL_BANDPOWER_WINDOW_LAYOUT_BRIDGE_V0_1`.
Frozen classification: `LOWLEVEL_LAYOUT_EXACT`.

Exact evidence:
- PyMaster version `2.7`;
- low-level raw dtype `float64`, raw shape `[6144]`;
- public shape `[4,8,4,48]`;
- source-defined rebuilt shape `[4,8,4,48]`;
- public SHA256 `aa883a13c305641e6e1aab5feca4692a8da1cdbcca16e8c124f12e601608d628`;
- rebuilt SHA256 `aa883a13c305641e6e1aab5feca4692a8da1cdbcca16e8c124f12e601608d628`;
- `sha_equal=true`;
- `array_equal=true`;
- `no_tolerance_rescue=true`;
- `science_gate_scored=false`;
- `ww_authority_created=false`.

Interpretation: the PyMaster 2.7 low-level `nmtlib.get_bandpower_windows` output, after only the prospectively frozen source-defined reshape `[n_bands,ncls,lmax+1,ncls]` and transpose `[1,0,3,2]`, is bitwise identical to public `NmtWorkspace.get_bandpower_windows()`. Therefore Python tensor layout / low-level-public bridge is excluded as the cause of the historical Exp073DU/Exp073DW distinct-field cross-workspace exact mismatch. This does not validate the saved-FITS production adapter as a whole and creates no WW scientific authority.

Live heavy reconciliation after consumption: Exp073DT attempt 4 run `33940588308`, hosted preflight job `101288015425` SUCCESS, self-hosted science job `101288014666` remains QUEUED. DSIR-HOME-PC remains RESERVED BY Exp073DT attempt 4; no competing self-hosted heavy process was launched.

Next permitted support work is prospectively narrowing the remaining mismatch to the saved-FITS reconstruction/post-MCM solver path, preserving exact arithmetic and no-tolerance governance. `WW_S0_S1` remains blocked until both valid `WW_S0_S0` authority/provenance closure and a separately validated exact cross-workspace adapter exist.
