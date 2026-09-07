# DSIR recovery V17 — Exp073FX S2S2 admitted; Exp073FY direct-FA heavy active

Date: 2026-09-07. Scope: **DSIR only**. RTK/RQIR excluded.

## Newly admitted scientific authority — WW_S2_S2

Exp073FW final recovery run **`34146468135`**, head `d7fdb410819dcec14276e0423c25c0d2f1b29b3b`, completed SUCCESS after checkpoint-only restoration of the already-complete A/B replicas. The home run reselected terminal-pruned durable checkpoints, the frozen comparator revalidated their complete stage/receipt chains and exact equality, and the unchanged frozen Exp073FX admission verifier admitted the candidate.

Authoritative jobs/artifact:

- hosted launch audit job `101819480467`: SUCCESS;
- home-science job `101819517843`: SUCCESS;
- hosted Exp073FX provenance admission job **`101819621240`**: SUCCESS;
- artifact **`10027835016`**, GitHub digest `sha256:ef36ddafc5f30d33206fbf952deea5c0f58f5465370a9c8bd96c2b2d61b1ecef`;
- unchanged Exp073FX verifier blob `eb907944eac68b9fd13c405399cf238a8cb5bc96`.

Raw admission emitted exactly:

- `PASS_EXP073FX_WW_S2_S2_FILEBACKED_PROVENANCE_ADMISSION_V0_1`;
- `classification=SCIENTIFIC_AUTHORITY_ADMITTED`;
- `ww_s2_s2_authority_created=true`.

Preserved candidate evidence remains frozen `S2->S2`, ordered `[2,2]`, same-field handoff, DES NSIDE=4096, ell 0..12287, 39 bands, canonical `<f8 [39,12288] EE<-EE`, exact `19,327,352,832`-byte file-backed MCM proof, finite A/B payloads, and byte/array-exact equality. The complete A/B canonical SHA256 remains `3daa7894648cc44d3ee822fe5f9b02aa0ccb756b11abfa0852a08b57d4ba75c9`.

Therefore **`WW_S2_S2` is now admitted scientific authority**. All previously admitted WW authority (`S0_S0`, `S0_S1`, `S0_S2`, `S0_S3`, `S1_S1`, `S1_S2`, `S1_S3`) and all preserved Wm authority remain unchanged.

## Historical FW failures remain historical +0/+0

They are not rewritten by the final admission:

1. run `34135965569`: terminal comparator omitted hyphenated checkpoint namespace transform; both expensive replicas were already complete; implementation/infrastructure `+0/+0`;
2. run `34145888831`: full-stage restore was incorrectly attempted on intentionally terminal-pruned checkpoints; implementation/infrastructure `+0/+0`;
3. run `34146286785`: frozen comparator passed, but the resume log lacked the historical pre-prune proof tokens required by unchanged Exp073FX verifier; implementation/admission-harness `+0/+0`.

The final repair re-attested those frozen historical proof tokens only after the frozen comparator had revalidated post-prune receipts/manifests/payloads. No Exp073FX criterion, science arithmetic, domain, tolerance or threshold was weakened.

## GitHub-native successor — Exp073FY WW_S2_S3

Successful Exp073FX admission dispatched the already-frozen successor `exp073fy-ww-s2-s3-home-science-v0-1.yml`.

Frozen FY prereg blob: `8aacb4e7f6615fe7e30a88ae02eb02ee5f4dba24`. Frozen target: ordered **`S2->S3`**, indices `[2,3]`, reconstruct S2 once and S3 once per replica, two distinct spin-2 fields, `compute_coupling_matrix(f2,f3,b)`, canonical `<f8 [39,12288] EE<-EE`, exact A/B equality and exact file-backed MCM proof. Reverse order, same-field object, tolerance rescue, effective coordinates and historical result import are forbidden. Only separate frozen Exp073FZ may create `WW_S2_S3` authority.

### Pre-science FY implementation failures

All occurred before expensive science/checkpoints and are `INFRASTRUCTURE/IMPLEMENTATION_FAILURE +0/+0`, not scientific FAIL:

- run `34146528784`: home wrapper incorrectly required Python-driver literals `source_pair=S2->S3` / `[2,3]` to occur in generated shell text;
- run `34146669028`: inherited generated-shell no-rescue vocabulary scanner self-matched its own guard literals;
- run `34146860145`: nested FS->FA transformation rewrote the same temp shell that Bash was executing, yielding a syntax error before science.

Minimal repairs:

- `143723e842104ae62ab426f146dbeceec04207b7`: remove invalid shell-only source-pair lexical assumption;
- `0b7812be611ec72f7dbeb30336e9727e1aa0dfc5`: remove generated-shell self-matching vocabulary scan while keeping the hosted audit of frozen driver/prereg/admission files;
- **`ed517b6652dc8172c64e5324b842e047c575b2cb`**: replace recursive FS generator with the already-proven direct frozen FA-base architecture, preserving the frozen FY Python driver and scientific arithmetic;
- workflow binding **`f04346a8e6909cb4342e536a0e7328f5ca5e54c9`**, FY home blob `63132e199c0af956f27218393240d5f85c681f88`.

No FY scientific arithmetic, source order, domain, thresholds, exact-equality acceptance, file-backed proof or provenance contract changed.

## Authoritative current process

Exp073FY recovery run **`34147009217`**, head **`f04346a8e6909cb4342e536a0e7328f5ca5e54c9`**.

- hosted audit job **`101821110137`**: SUCCESS; raw token `PASS_EXP073FY_HOSTED_LAUNCH_AUDIT_V0_4`; classification `SUPPORT_PLUS_0_PLUS_0`;
- home-science job **`101821144414`**: IN_PROGRESS at this recovery write, specifically inside `Run frozen WW_S2_S3 A/B gate with durable checkpoints`;
- runner owner: `DSIR-HOME-PC-2` / `win-ws338`;
- checkpoint namespace/root: `~/.cache/dsir/exp073fy-ww-s2-s3-filebacked-ab-v0-1`;
- expected scientific-candidate token: `PASS_EXP073FY_WW_S2_S3_FILEBACKED_AB_EXACT_REPEATABILITY_V0_1`;
- authority token, allowed only after independent hosted admission: `PASS_EXP073FZ_WW_S2_S3_FILEBACKED_PROVENANCE_ADMISSION_V0_1`.

No competing home job may be launched. Do not inspect partial numerical output. On terminal success, independently download/verify the exact artifact digest, complete A/B durable chains, restored-vs-new provenance, ordered distinct-field S2->S3 semantics, exact MCM proof, finiteness and exact A/B equality before accepting Exp073FZ authority. On failure, preserve all complete checkpoints and diagnose the first causal defect before any resume.

The FY workflow currently retains a temporary path-scoped push trigger used solely for one-shot repair launches. Do not edit that workflow while `34147009217` is active; restore dispatch-only semantics at a safe terminal transition.

The older FW workflow also retains its recovery path trigger; it is no longer the active frontier and must be returned to dispatch-only semantics at a safe non-triggering maintenance point without launching a competing heavy run.

## Independent C2 frontier

Exp073GW/GX/GY remain hosted support-only `+0/+0`. Exp073GY created no real record-set or model authority. The next meaningful C2 step remains real runtime generation/admission of the frozen 28-packet set. It is **BLOCKED while Exp073FY owns the home runner**; do not replace it with further metadata-only scaffolding.

## Frozen global boundaries

Unless prospectively superseded by explicit repository authority: `0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; exact-threshold ambiguity `numerically_unresolved`; no tolerance, rounding, smoothing, averaging, effective ell/z/k or fiducial-P shortcut.