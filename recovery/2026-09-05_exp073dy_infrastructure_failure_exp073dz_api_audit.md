# DSIR immutable recovery — Exp073DY infrastructure failure / Exp073DZ continuation

Date: 2026-09-05. Scope: DSIR only.

Exp073DY run/job `33970593677 / 101318281168` failed before any numerical solver comparison. The first causal failure in the raw job log is `AttributeError: 'NmtWorkspace' object has no attribute 'bpws'` at `official_flat=canon(wr.bpws)`. Upstream frozen identity checks, PyMaster 2.7 installation and GSL comparator compilation succeeded. Evidence artifact `9970819324` was uploaded with GitHub ZIP SHA256 `c4f72f053e1d19ff6e66f060e68e0e672bdbd60369c47c2164f010f0ad7069c3`, but it is incomplete evidence only. Classification: `INFRASTRUCTURE/SOFTWARE_INCOMPLETE +0/+0`. No solver-backend diagnostic conclusion and no WW authority are admitted.

The smallest prospective continuation is Exp073DZ, a hosted-only API-state audit frozen before output. It records the exact PyMaster 2.7 workspace/public/low-level attributes and shapes required to repair the post-MCM diagnostic without guessing or tuning numerical acceptance. Prereg commit `df29d093b6c72f18d25e01109d26057cfa4df7a5`; script commit `b9d51f51876dd454491e99fc86cb9a3ce302d7e5`; workflow commit `34232b7b7cd3e9ec546a9f4c674ce0dc3942fab9`; activation head `7ee7ad66363af1462b0cddf34b218868221fc383`; run `33973350908`.

Exp073DT attempt 4 remains the sole authoritative self-hosted heavy process (`33940588308 / 101288014666`) and DSIR-HOME-PC remains reserved by it. No competing home task was launched.
