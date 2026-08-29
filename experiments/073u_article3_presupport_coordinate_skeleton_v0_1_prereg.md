# Exp073U — Article 3 pre-support coordinate skeleton v0.1

**Frozen:** 2026-08-29, after genuine hosted Exp073R1 v0.8 and its preregistered Exp073P v0.5 authority receipt reached PASS, but **before any current Article-3 Layer-A or Layer-B support score is evaluated** and before covariance inspection.

## Purpose

Freeze the complete candidate coordinate identity and ordinal skeleton needed by the current Article-3 dual-support hierarchy without pretending that a broad finite survey bandpower has a unique scalar `(z,k)` representation.

This experiment is deliberately **non-classifying**. It freezes identities, block order, component identity and upstream provenance only. It does not construct the full physical finite-response operator, does not compute support leakage, does not compute Article-3 coordinate `f_invalid`, and therefore earns no readiness credit by itself.

## Scientific context

The controlling dual-support order is:

`hosted reproduction authority -> full pre-support finite observation operator / immutable candidate order -> Layer A broad operator-support leakage -> Layer B coordinate/common-response validity -> covariance/whitening -> nuisance quotient -> relation/null -> later gates`.

A pre-execution representation audit established that Wm/WW pseudo-C_ell rows have broad support kernels. Therefore Exp073U MUST NOT assign effective `z`, effective `k`, centroid `k`, midpoint `k`, effective-ell-derived `k`, or any other scalar physical proxy to these rows. Such fields remain unresolved until a separately frozen Layer-B representation contract exists.

## Frozen authority inputs

### Genuine hosted R1 and prerequisite receipt

- R1 run: `33270843577`
- R1 job: `99148916507`
- R1 head: `ef783ca941fb9b9b5f5eae537986c56ff06e6536`
- R1 artifact: `9720335366`
- R1 artifact name: `exp073r1-v08-hosted-wholestream-ef783ca941fb9b9b5f5eae537986c56ff06e6536`
- R1 artifact digest: `sha256:ff87d8fc7d53b16b786a4eb3d6ffeb103676efb8a548223a187b9f59689f8abd`
- hosted Exp073P v0.5 receipt run: `33271876425`
- receipt job: `99151650192`
- receipt artifact: `9720339539`
- receipt artifact digest: `sha256:dc63797a8bfe12a91c264eb5204182164e15d9f6441886ef79ab25f55b3040fc`
- receipt JSON SHA256: `52c9dc6f51078da430788a90551cba5069706481fe2d6cf68f2f879b8537fc45`

The receipt must be `PASS_EXP073P_PREREQUISITE_BINDING_V0_5_HOSTED` with `support_executor_authorized=true`.

### Exp073S source count-mask records

Bind exactly the four corrected v0.2 artifacts from run `33272641756`:

| source bin | artifact id | artifact ZIP digest | JSON SHA256 |
|---:|---:|---|---|
| 0 | `9720550961` | `sha256:2dcb16a310b8dad52dc2f93c5901734fe8996f6d546e1440d9baab5781399ef9` | `7ed9ee2730482f1fb225ec7d07a9221789a15ad03e866968176d01a2bf46bfce` |
| 1 | `9720550790` | `sha256:b0fab060d5c6c314854bab09c1f49b56feb6293129e768f1f323ee61d0a5a5f7` | `e38438052af992372ee2006a56fce3a417cc9dd5ee87c9487097c3c986575406` |
| 2 | `9720550823` | `sha256:8714d4503879fcf7f21669f3a94020c098fff35c110ed6821ec8a39ceeb2e1b1` | `b0dd293663325de82bf39cc970ac7b84c9c904163234ede451f2925778ff0edc` |
| 3 | `9720551316` | `sha256:0962775868f49891c522fa44966d680e58377eb08bdad46bc2b5af94b212d86a` | `5f1472e0f7e05426c16aaf416161059c67b056b3f155ab85701bf5c397e2d16d` |

Each record must preserve `physical_support_evaluated=false`, `science_gate_scored=false`, `f_invalid_computed=false`, and the exact R1 run/job/head identity.

### Exp073S metadata correction boundary

The unchanged Exp073S evaluator contains legacy hard-coded values for its internal `authority.r1_artifact_id` and `authority.r1_artifact_digest` (`9743987175` and `sha256:702151...`). These two internal fields conflict with the exact GitHub artifact metadata and with the preregistered hosted receipt above.

This is classified here, prospectively before Layer-A scoring, as a **metadata-only provenance defect**. It does not alter the downloaded R1 files, selected-row counts, pixel-record hashes, mask hashes or sparse-count fingerprints reproduced by Exp073S.

For Exp073U and all later Article-3 authority binding:

- authoritative R1 artifact identity is only `9720335366` / `sha256:ff87d8fc...` from GitHub plus the hosted receipt;
- the two conflicting internal Exp073S artifact-id/digest fields are legacy and non-authoritative;
- all other Exp073S R1 run/job/head and count-mask checks remain required;
- no scientific result is reclassified by this correction.

### Exp073T inventory and NaMaster order

Bind run `33272691162`:

- static inventory artifact `9720563095`, ZIP digest `sha256:4332ffa9d6b4385a48d3022a8afcedf0bf00a742cee8444fd6ca83842bf1e642`, JSON SHA256 `55f55d21eedd3779a729af387205ec7db360617c5e026406d21b3b542f355309`;
- NaMaster-order artifact `9720576202`, ZIP digest `sha256:0ed052aabc6ba908094396207031417ab076612e23b6211f1e08801e95b3388a`, JSON SHA256 `f6000b5e0b87a93ff31f9a22d7aa66ada64149885b126a73f38b6f0f82a59519`.

Required exact identities:

- Wm = 20 pairs x 39 bandpowers = `780` scalar coordinates;
- WW = 10 pairs x 39 bandpowers = `390` scalar coordinates;
- DES total = `1170`;
- frozen BOSS pre-support rows = `240`;
- total candidate count = `1410`;
- Wm scalar component = NaMaster `TE`, component index `0`;
- WW scalar component = NaMaster `EE`, component index `0`;
- Wm ordered-ID SHA256 = `dc20ff104c707d006992c1579ce9175295fae426b1c32ff47e56c53d9300603a`;
- WW ordered-ID SHA256 = `e0cc92706598a8ac6360d0fd669451e4816091f83c01e8744940e94a2b8593b5`;
- DES Wm->WW ordered-ID SHA256 = `736f80a6dd407b1a3891cb34f35262e415a4f0c9bbb200a9f376102b05988ee4`.

## Frozen BOSS coordinate identity

Use only the geometry already frozen before the legacy BOSS support output:

1. NGC `P0`, matrix rows 0..39;
2. NGC `P2`, matrix rows 80..119;
3. NGC `P4`, matrix rows 160..199;
4. SGC `P0`, matrix rows 0..39;
5. SGC `P2`, matrix rows 80..119;
6. SGC `P4`, matrix rows 160..199.

Canonical BOSS ID string:

`BOSS|{NGC|SGC}|{P0|P2|P4}|matrix_row={three-digit-row}`.

The legacy BOSS retained mask/support fractions MUST NOT be read to choose or order these 240 rows. All 240 are present in the pre-support skeleton.

## Frozen full coordinate order

Preserve the already frozen DES order, then append BOSS:

`Wm[780] -> WW[390] -> BOSS[240]`.

Offsets are exactly:

- Wm `[0,780)`;
- WW `[780,1170)`;
- BOSS `[1170,1410)`.

Ordered-ID serialization is UTF-8 `"\n".join(ids) + "\n"`.

The pre-execution reference implementation gives:

- BOSS ordered-ID SHA256: `7315944adea1a36c0bdb162d57c567330151018dd2058f80e2cb6cb20c153ea0`;
- full 1410-coordinate ordered-ID SHA256: `bfaf582518cdbfd34b1e8392da83dac6b0885948bc31f2c29d4e48247c23af75`.

## Frozen implementation

Builder path:

`ci/exp073u_article3_presupport_coordinate_skeleton_v0_1.py`

Git blob SHA1 at freeze: `5084e11ad905183510b7133a45a6353ce434c90c`.

Any production run must verify this blob exactly before execution.

## Mandatory science firewall

The output must state all of the following:

- `full_finite_operator_built=false`;
- `z_k_bound=false`;
- `final_response_abs_values_bound=false`;
- `physical_support_evaluated=false`;
- `science_gate_scored=false`;
- `f_invalid_computed=false`;
- `covariance_read=false`;
- `nuisance_geometry_read=false`;
- `relation_null_read=false`;
- `G8_read=false`;
- `G7=OPEN`, `G8=OPEN`, `G9=OPEN`;
- `readiness_credit_authorized=false`.

Positive output token:

`PASS_EXP073U_ARTICLE3_PRESUPPORT_COORDINATE_SKELETON_V0_1`.

This token is a provenance/order PASS only, **not** a physical-support PASS and not closure of the Article-3 55–57% full-manifest checkpoint.

## Next authorized scientific step

Use the frozen 1410-row skeleton to bind the real Layer-A finite-operator/window/kernel representation. Broad Wm/WW support must be evaluated from full positive bandpower/window envelopes under the unchanged 5% criterion; BOSS must preserve its previously frozen finite `C=W@M` geometry. No scalar `(z,k)` shortcut is authorized for broad DES rows.
