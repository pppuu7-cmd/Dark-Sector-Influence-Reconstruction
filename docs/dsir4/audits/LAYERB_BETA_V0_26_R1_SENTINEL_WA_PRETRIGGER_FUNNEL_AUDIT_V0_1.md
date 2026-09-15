# DSIR V0.26 R1 sentinel W/A pretrigger funnel audit

Status: **INDEPENDENT FUNNEL AUDIT — QUALIFIED**  
Date: 2026-09-15  
Effect: `+0/+0`.

## Reviewed object

Reviewed branch `research/v026-r1-sentinel-wa-pretrigger`, exact head `15e7dbfb9c05744c026d5b03e5466267d802a2c7`, against exact main `b7d65db1dacb355ddf2419a22cec38cc4b091c39`.

The candidate is exactly three commits ahead and adds exactly four files, with no deletions:

- active-path W copied byte-for-byte from frozen W candidate;
- final-path A copied byte-for-byte from frozen A candidate;
- response-blind W/A pretrigger static auditor;
- hosted pretrigger static-audit workflow.

Exact W blob: `19907175f0f3417ddee2aba6916d961c6be02e26`.  
Exact A blob: `4ba40e59e6a9d48636d95d07efab575e56ae0966`.

Final L and final Q paths are absent at the reviewed head. The inactive Q candidate and Q-funnel qualification authority are already present and exact on the reviewed base.

## Fail-closed trigger check

W remains exactly the already-audited workflow content. Its only trigger is push to `main` with path filter `docs/dsir4/launch/LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_V0_1.json`; it has no `workflow_dispatch` entry. Staging W/A therefore cannot itself trigger the sentinel because final L is absent and the W/A promotion changes do not create L.

A binds exact W but intentionally does not bind final L. A requires a separate package qualification Q. Its internal future one-run authorization does not become an executed run merely by storing A at its final authority path.

## Hosted response-blind pretrigger static audit

Static auditor: `ci/layerb_beta_v026_r1_sentinel_wa_pretrigger_static_audit_v0_1.py`, git blob `2dbc76f15ee3510111db2bbe7da3cefb496d027b`.

Static workflow: `.github/workflows/layerb-beta-v026-r1-sentinel-wa-pretrigger-static-audit-v0-1.yml`, git blob `f039472f7a94cda2ccf088f2e0e36b90ef08dc5d`.

Run `35017254145`, run #1 / attempt #1 / event `push`, exact head `15e7dbfb9c05744c026d5b03e5466267d802a2c7`; job `104543690375`, terminal success.

Artifact `10415689546`, `layerb-beta-v026-r1-sentinel-wa-pretrigger-static-audit-v0-1`, ZIP SHA256 `ac4d6b601e8f8b90cb0ae21bfbdc8f360949453784da51688a76318668076c72`.

Inner `wa_pretrigger_static_audit.json`: 1252 bytes, SHA256 `9f70c83f57f74805f073cbd0ef7b6bdf2fef0ac8028b01d503c6b54e7f46b681`.

Token: `PASS_LAYERB_BETA_V0_26_R1_SENTINEL_WA_PRETRIGGER_STATIC_AUDIT_PLUS_0_PLUS_0`.

The receipt records exact W/A, L absent, final Q absent, zero sentinel-workflow runs at the exact head, main-only/final-L-only W trigger, no workflow dispatch, A requires Q, A does not bind L, `class_solver_invoked=false`, `scientific_response_read=false`, `covariance_read=false`, and full-107 false.

## Independent funnel audit

Independent auditor: `ci/dsir_v026_r1_sentinel_wa_pretrigger_funnel_audit_v0_1.py`, git blob `6d32121ba347b5ffa130e61ed9533de946ae9a40`.

Independent workflow: `.github/workflows/dsir-v026-r1-sentinel-wa-pretrigger-funnel-audit-v0-1.yml`, git blob `8907c977eff4b89861b14e08d406417baa07f0ff`.

The independent auditor does not import or execute the candidate static auditor. It checks the exact base/head git relationship, exact four-added-file diff, W/A/Q identities, absence of final L/Q, W trigger/runtime guards, A boundaries, exact static-run uniqueness, and independently downloaded artifact bytes.

Hosted independent run `35017440323`, run #1 / attempt #1 / event `push`, execution head `13797538a828bfb1f208bec982dea6c3b95a9946`; job `104544327689`, terminal success.

Artifact `10415119864`, `dsir-v026-r1-sentinel-wa-pretrigger-funnel-audit-v0-1`, ZIP SHA256 `e023a71379dee09ecf203b7a687c0da9b092b5ad2e39afc68dda39836752d8c0`.

Inner `wa_pretrigger_funnel_audit.json`: 1343 bytes, SHA256 `dfc6219a1d766f38957d20185f3e5473f7c33260abcfbf607f48053f7224e025`.

Token: `QUALIFIED_DSIR_V0_26_R1_SENTINEL_WA_PRETRIGGER_FUNNEL_AUDIT_PLUS_0_PLUS_0`.  
Verdict: `QUALIFIED`.  
Classification: `SENTINEL_WA_STAGING_QUALIFIED_FOR_MAIN_PROMOTION_WITHOUT_L_OR_FINAL_Q`.

## Verdict and boundary

**QUALIFIED** for fail-closed W/A staging promotion only.

Required chronology:

1. persist the W/A pretrigger funnel qualification authority on main;
2. only then promote the exact reviewed W/A staging head, preserving the four audited blobs;
3. promotion must not create final L or final Q;
4. after promotion, independently re-audit main to confirm W/A exact, L/Q absent, and no sentinel run occurred;
5. only a later authority may permit exact final-Q promotion; final-L creation remains a separate one-run trigger gate.

This audit does not authorize sentinel science, final L, full 107-row replay, covariance, whitening, nuisance, relation-null, `Wm_S3`, global 65537, statistical/model inference, or physical dark-sector inference. Readiness and scientific frontier remain unchanged.
