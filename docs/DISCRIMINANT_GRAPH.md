# DSIR discriminant graph

A node is a frozen model instance or response-manifold patch. A degeneracy edge joins instances indistinguishable within the current response subset/tolerance. Candidate observable channels label edges they demonstrably break. Finding the minimum additional set is a minimum hitting-set problem (`src/dsir/discriminants.py`).

Evidence rule: a channel is allowed onto an edge only when separating power is established for the specific frozen representatives and validity domain. `possible`, `depends`, or implementation-dependent entries remain unknown.

Initial targets:
- LambdaCDM vs nontrivial WDM with same background: scale-dependent transfer/halo response.
- LambdaCDM vs nontrivial designer f(R): mu(a,k), slip, growth/lensing consistency, screening.
- minimally coupled dynamical DE vs background-mapped interacting sector: perturbation growth/velocity and momentum-transfer-sensitive observables after freezing Q^mu.
- LambdaCDM-like background vs nontrivial GDM/unified fluid: sound-speed/viscosity response in CMB/matter power.

Law discovery and the discriminant graph are dual: a proposed universal relation is stronger if it survives a channel chosen specifically for maximal degeneracy-breaking power.
