# DSIR research log — 2026-09-06 — Exp073EN -> EO -> EL -> EY

Scope: DSIR only.

- Consumed terminal Exp073EN `33994398927 / 101382229273`; verified artifact `9980311204`, ZIP/GitHub SHA256 `54db5c1c213a041616111071c23ce2710e88c0f085efc9e625dd51538e71dd49`, complete A/B six-stage provenance, exact selected SHA `244f8f831ac7041af00f9cddca0ea93a04298fb0b1b029af5030376ce93da647`, exact array equality. Classified candidate PASS pending provenance admission.
- Exp073EO real v0.1 first exposed missing hosted NumPy, then a string-vs-int Exp073EM artifact-ID representation bug. Both preserved as `+0/+0`; no science criteria changed.
- Prospectively frozen EO v0.2 representation-only repair passed run/job `34005373819 / 101411448176`, artifact `9980754356`, digest `0e1a4cff3b761fecc65d8e07df9e56f8109fd221fb4454746caa8c7d0f2fb4be`; `WW_S0_S0` scientific authority admitted.
- Activated Exp073EL under governance-only v0.3 binding. Run `34005467421` passed. Authoritative artifact `9980783193` digest was independently corrected/verified as `c720233664be2e8a7666db6f95def0a2f13eb674732add6852f0c09e916e5e46`; raw classification `FULLRES_RESOURCE_PATH_READY +0/+0`. Earlier copied `f66da690...` was provenance transcription error.
- Prospectively froze Exp073EY ordered distinct-field `S0->S1` full-resolution A/B science gate. Pre-data audits caught and repaired two implementation issues: historical reconstruction adapter use and hidden `wsp.mcm` proof. Qualified route is file-backed serialized `read_from(..., read_unbinned_MCM=True) -> get_bandpower_windows()` with exact backing-file `/proc/self/maps` proof.
- Static audits PASS: `34006046818 / 101413292411` v0.1; `34006100427 / 101413444610` workflow-inclusive v0.2; `34006195574 / 101413721477` corrected-binding v0.3.
- First EY activation `34006121336 / 101413506204` failed hosted preflight only because of stale wrong EL digest; home job skipped, so no science ran. Prospectively corrected only EL artifact binding and re-audited.
- Current corrected Exp073EY run `34006214398`, head `0476ce61a84a97392abb80afadad188a588bbe1f`: hosted preflight `101413770925` SUCCESS; home science `101413789646` IN_PROGRESS at log write. Checkpoints: `checkpoints/exp073ey-ww-s0-s1-a-v0-1`, `checkpoints/exp073ey-ww-s0-s1-b-v0-1`.

Next: terminal-consume EY raw artifact. Exact A/B PASS remains candidate pending separate provenance admission; exact completed mismatch is scientific FAIL; infra/resource/provenance failure is checkpoint-preserving `+0/+0` repair/resume.
