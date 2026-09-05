# DSIR research log — Exp073DY infrastructure failure and Exp073DZ activation — 2026-09-05

Scope: DSIR only; RTK/RQIR excluded.

Exp073DY run/job `33970593677 / 101318281168` completed FAILURE before any numerical solver comparison. First causal failure from raw log: `AttributeError: 'NmtWorkspace' object has no attribute 'bpws'` at the diagnostic access `wr.bpws`. Identity checks, PyMaster 2.7 environment installation and GSL comparator compilation had already succeeded. Artifact `9970819324` was uploaded with GitHub ZIP SHA256 `c4f72f053e1d19ff6e66f060e68e0e672bdbd60369c47c2164f010f0ad7069c3` but contains incomplete evidence only. Classification: `INFRASTRUCTURE/SOFTWARE_INCOMPLETE +0/+0`; no solver-backend scientific/diagnostic classification is admitted.

The smallest safe continuation is Exp073DZ, prospectively frozen support-only API-state audit. It records the exact PyMaster 2.7 workspace attributes/public shapes needed to design a corrected post-MCM reconstruction without guessing or tuning against numerical output. No WW authority can be created.

Authoritative self-hosted heavy process remains Exp073DT attempt 4 run/job `33940588308 / 101288014666`, currently queued. DSIR-HOME-PC remains reserved by Exp073DT; Exp073DZ is hosted-only and noncompeting.
