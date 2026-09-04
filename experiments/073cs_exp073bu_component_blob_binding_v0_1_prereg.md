# Exp073CS v0.1 — Exp073BU executable component blob binding

Status: PROSPECTIVE / HOSTED-ONLY / SUPPORT +0/+0 / NO Wm_S3 AUTHORITY.

Collision authority: exact recursive repository tree at head `56ae01872478f72325b14feea244284ad35e9bbd` contained no `073cs` path before this preregistration. Search indexing is not accepted as sole collision evidence.

Purpose: freeze exact repository-native executable blobs that may be assembled into the future Exp073BU A/B driver. No numerical Wm_S3 science is executed.

Required path/blob pairs:
- `ci/exp073bu_fresh_wm_s3_pcl_v0_1.py` = `73ef04c479547dc8e2e89c9f511f1a55fae3ed64`
- `ci/exp073bx_full_mcm_stock_order_v0_1.py` = `ae0282cbbcdd298f00765d8de68545fe214cec0e`
- `ci/exp073ca_stock_write_fits_to_mmap_exact_chain_v0_1.py` = `d3c2e3a2ec42ddcb5811447499d80a4a1cfa3132`
- `ci/exp073cc_verify_fits_memmap_backing_v0_1.py` = `88d17ad76cabc1651df6b6035d897e9f42853ca5`
- `ci/exp073by_mmap_full_mcm_downstream_v0_1.py` = `a22d14ad9ae7e81ba6dd35c61b9ab35a05617d76`
- `ci/exp073cr_wm_s3_ll3_sharded_resource_v0_1.py` = `934c339bb01dd7f541e9191129bcdc8b3a7ad772`
- `ci/test_dsir_checkpoint_git_sync_v0_2.sh` = `39e90b4c1986f1972d43e9dce7b74f0082c39559`

The hosted audit must verify every path exists and its Git blob SHA is exact, and must fail closed if any source differs. It must also verify the fresh-PCL source hard-binds DES NSIDE=4096, ell/lmax=12287, S3 record SHA `3996f2bacf29d46278773530058d4f5666c0d590bf6cebc06459659166bc60ec`, S3 occupancy SHA `21e3776111de305c108463b02b0e3fd5e138cc97817d37e7b05330132d058094`, lens SHA `a519b8522f899e4c33267bb0749f9734f8b7fa760d195636456d370f809a3d55`, coupling signature `[0,2,0,2]`, and TE<-TE semantics.

PASS token: `B1_EXP073BU_COMPONENT_BLOB_BINDING_PASS`. Any path/blob/source-semantic mismatch is `B2_COMPONENT_BINDING_FAIL`; infrastructure failure is `B3_INFRASTRUCTURE_INCOMPLETE`. All outcomes +0/+0; Exp073BU remains NOT ACTIVATED.
