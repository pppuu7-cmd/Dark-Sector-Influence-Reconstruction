# Exp069H result — C5 q=3 unmodified-upstream physical provider

Date: 2026-08-27

Scientific classification:

`PASS_C5_Q3_UNMODIFIED_UPSTREAM_PHYSICAL_PROVIDER_V0_1`

Immutable run: `33024638764`; artifact: `9628053962`; digest: `sha256:fa61b504d31edeba2afcbed0f4b14bda688df82a96d2cba55eac034682b5382f`.

Frozen exact-zero closures:

- target: `1.7011186858522977e-6 <= 5e-6`;
- same-node raw: `2.8421302380756537e-6 <= 5e-6`.

Tiny-positive B0 continuity points `1e-12,1e-10,1e-8` report zero stored difference from the q=3 zero branch. Production `B0=1e-6` has target response about `1.32491e-2`, above frozen `1e-3`. Independent zero rerun target/raw differences are `0.0`; signed `P_Wm` is preserved; accessor-order repeatability passes.

Exp069B remains permanent FAIL and Exp069F remains a separate mechanism PASS.

A post-result provenance issue was identified before common-support construction: Exp069F/H raw accessor omitted `k_hunit`, whose pinned CAMB default is `True`; therefore the historical field label `raw_k_Mpc^-1` may denote `k/h`. This does not change Exp069H target metrics, which used explicit `k_hunit=False`, or raw same-node ratios. Exp069I is preregistered to resolve that metadata/unit issue before support masking.

Current state: C3 provider certified, C5 provider certified, common support mask blocked pending Exp069I, G7/G8/G9 OPEN.
