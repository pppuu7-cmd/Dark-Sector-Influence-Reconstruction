# Layer-B canonical 16385 host-variant diagnostic v0.1

Date: 2026-09-11. Scope: reproducibility diagnostic only; `+0/+0`. No CLASS/scientific response is involved.

The response-blind 16385 canonicalization run `34546913426` admitted five anchor-matched replicas `[1,3,4,7,8]` and excluded three host variants `[2,5,6]`. The admitted canonical payload is decoded SHA256 `3e10cea6e46a6d0c07eac825a4e508829727914c8690d42b187ef894eaa2c975`, u64hex SHA256 `7e8f13abe29617bc0d331f07143e6680f50512e2f3811e017bbc74ea847dff69`.

For an explicit diagnostic comparison, replica 1 (anchor-matched) artifact `10179344065`, ZIP SHA256 `a74f1f32b7f4ffcc074369b01faef50c11c8239401aa2a49dd3b2dc8a447b149`, was compared against excluded replica 2 artifact `10179344713`, ZIP SHA256 `1841d0bdbcaa228e676aa998a287fc0f580177f3428681bb8161c0737353b777`.

Replica 2 candidate decoded SHA256 is `0532963da18a854b5e73e8682bbd0a2e938ce6738c97130b31526e367a889e00`, u64hex SHA256 `8f77cff26d0befa5e6d4d9578435c7a4c38a31260e99ab8a80d7a4230b11ce0d`.

Exact binary64 comparison of the two 16385-node candidate streams finds:
- differing nodes: **4512 / 16385**;
- maximum integer ULP distance at any differing node: **1 ULP**;
- maximum relative coordinate difference: approximately **2.219183213000222e-16**.

Thus the same host-sensitive last-bit effect already observed at 4097/8193 persists and affects a substantial fraction of nodes at 16385 while remaining one-ULP in amplitude. This is numerically tiny but provenance-critical: runtime regeneration cannot be used as a canonical-grid identity mechanism. The frozen anchor-selected byte authority is therefore retained.

This diagnostic does not activate the successor rung, does not alter any lattice, threshold, estimator or physical support, and does not authorize covariance restriction or Wm_S3. Article III repository readiness remains 68%; funnel-freeze readiness remains 67%.
