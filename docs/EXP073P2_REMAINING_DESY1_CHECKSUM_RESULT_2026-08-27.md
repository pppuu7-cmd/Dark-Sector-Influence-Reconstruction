# Exp073P2 — remaining DES Y1 checksum binding result

**Date:** 2026-08-27  
**Classification:** `PASS_REMAINING_DESY1_RELEASE_CHECKSUM_BINDING_EXP073P2`

The four smaller DES Y1 release objects prospectively frozen by Exp073P2 were found at the official DES Y1 server and streamed completely through SHA256 before any physical support fraction was evaluated.

| Object | Exact bytes | SHA256 |
|---|---:|---|
| `DES_Y1A1_3x2pt_redMaGiC_MASK_HPIX4096RING.fits` | 104,595,840 | `a519b8522f899e4c33267bb0749f9734f8b7fa760d195636456d370f809a3d55` |
| `DES_Y1A1_3x2pt_redMaGiC_zerr_CATALOG.fits` | 31,383,360 | `4a0ed31a128c34aa0da17e1d826c76b5ac829ba1c2c2087b965977b89d43a177` |
| `2pt_NG_mcal_1110.fits` | 6,600,960 | `114035179b5a8e41090751e9a6478536d185128581d37b5a510eff5722f417ca` |
| `y1_redshift_distributions_v1.fits` | 109,440 | `b5d87138c35ae8bb4ecd02491972f544648398e606b3617039e6e54cb8ea943b` |

Together with the previously bound objects

- `y1_source_redshift_binning_v1.fits`: 2,738,626,560 bytes, SHA256 `491f4bb742762fefe3aaab6d53d4342b6ff4a65401bc7b588d2918fdce3ee6fd`;
- `mcal-y1a1-combined-riz-unblind-v4-matched.fits`: 84,075,649,920 bytes, SHA256 `39a7fe03e54d96b85cee2fb523ea108c2a548ba1584368203f0464ed6241ebc8`;

this completes checksum identity binding for every DES Y1 release object explicitly frozen in Exp073P section 2.

**P2 status:** CLOSED / PASS.  
**G7:** OPEN.  
**G8:** OPEN.  
**G9:** OPEN.

No mask, redshift kernel, bandpower, support fraction, covariance, nuisance direction or downstream relation output was used to obtain this classification.
