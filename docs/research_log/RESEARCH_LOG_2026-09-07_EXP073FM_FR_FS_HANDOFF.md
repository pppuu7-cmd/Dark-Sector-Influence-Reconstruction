# DSIR research log — Exp073FM -> Exp073FR -> Exp073FS

Date: 2026-09-07. Scope: DSIR only.

Exp073FM `WW_S1_S1` run/job `34050657030 / 101533574294` was consumed after terminal completion. Raw job evidence and artifact `9998932628` independently established both complete six-stage/prune chains, exact file-backed MCM backing `19,327,352,832` bytes, canonical A/B `<f8 [39,12288] EE<-EE`, all finite, selected SHA256 `ff7215d5e523134e10ef4c9b512c6829d66fd63af33dc5655bd8e88dfd0c33ff`, exact equality, and ZIP SHA256 `db3aa00e060047f354c5374c78dba3808491cf61a1d810114d35b474badd49af`. Candidate classification: exact scientific candidate PASS pending admission.

Terminal consumer `34065976761 / 101578311604` reverified evidence and remained support `+0/+0`. Canonical Exp073FR `34067345251 / 101578330386` then independently reverified it and emitted `PASS_EXP073FR_WW_S1_S1_FILEBACKED_PROVENANCE_ADMISSION_V0_1`, `classification=SCIENTIFIC_AUTHORITY_ADMITTED`, `ww_s1_s1_authority_created=true`. `WW_S1_S1` is therefore admitted.

FR dispatched frozen successor Exp073FS. Live state at log creation: run `34067352681`, hosted job `101578350681` SUCCESS support-only, home job `101578366531` IN_PROGRESS, head `f3e49041a5b869ddf22be8ca7a612901ec9f9458`, runner ownership exclusively `DSIR-HOME-PC`. Partial FS numerical output was not inspected. Exact next gate is terminal consumption of FS followed, only on candidate PASS, by the prospectively frozen Exp073FT provenance admission and then FU dispatch.
