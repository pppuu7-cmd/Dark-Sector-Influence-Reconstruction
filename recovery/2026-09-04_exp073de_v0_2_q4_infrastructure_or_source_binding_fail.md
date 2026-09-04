# DSIR recovery — Exp073DE v0.2 Q4 infrastructure/source-binding FAIL

Date: 2026-09-04. Scope DSIR only; RTK/RQIR excluded.

## Authority
- Prereg commit/blob: `01e1fc2b697e753c3d2d3ba65b0ecaeb7eed152c / 975ad3cbf446d7dd06cc227a245f97bbd4b57510`.
- Exact resume helper commit/blob: `b68dbbab705963365157d348c57f9e0e5537af06 / 210775ebf9b3f1aad9ade0ea0d095848c1481c0f`.
- Activation/head: `0df615853bf187e5dc4d27fa1679f3a98e8efdda`.
- Run/job: `33885325120 / 101063561505`.
- Artifact `9941575908`; Actions digest and independently downloaded ZIP SHA256 both `348a55e4754cb472f62bb95efdfacb4d5c783664a756245ddb57bf595eae5876`.

## Frozen classification
`Q4_INFRASTRUCTURE_OR_SOURCE_BINDING_FAIL +0/+0`.

The exactness gate was not evaluated. Source binding completed successfully. The execution wrapper step itself was allowed to return success for later fail-closed classification, but the raw artifact contains only an empty `exp073de_v02_stdout.log`; neither `exp073de_v02_receipt.json` nor `exp073de_v02_classification.json` exists. The classifier therefore failed before assigning Q1/Q2/Q3. Workflow/job failure is not treated as a scientific or arithmetic result.

Because the raw evidence does not expose stderr, the precise dependency/runtime exception cannot be proven retrospectively. The smallest prospective repair is to make the hosted runtime dependency (`numpy`) explicit before executing the unchanged helper, capture stderr together with stdout, and make missing receipt an explicit Q4 token. Do not change the helper arithmetic, shape, exact SHA/array/bytes criteria or fail-closed malformed-input checks.

No science numerics executed; no Wm_S3 authority was created; Exp073BU remains not activated by this gate.
