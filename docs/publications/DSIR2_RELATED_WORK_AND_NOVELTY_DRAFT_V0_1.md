# DSIR-2 — Related work and novelty boundary (draft v0.1)

**Date:** 2026-08-28  
**Intended manuscript placement:** end of Introduction or first part of Discussion.  
**Status:** publication prose; priority language remains deliberately narrow.

## Related work and novelty boundary

Generalized dark matter is an established phenomenological framework rather than a construction introduced here. Hu formulated GDM by parameterizing the stress properties of a cosmological component beyond the pressureless-perfect-fluid limit, and subsequent analyses developed the roles of the background equation of state, effective sound speed and viscosity in the CMB and large-scale structure [Hu 1998; Kopp, Skordis & Thomas 2016; Thomas, Kopp & Skordis 2016; Kunz, Nesseris & Sawicki 2016]. In particular, the limited ability of selected observables to distinguish the GDM sound-speed and viscosity parameters is already known. Our use of these directions is therefore as a controlled mechanism bank for testing response specificity, not as a claim to have discovered the underlying GDM degeneracy.

There is likewise substantial prior work on geometric and information-preserving representations of cosmological data. MOPED established Fisher-preserving parameter-aware linear compression under its stated assumptions [Heavens, Jimenez & Lahav 2000]. Nuisance-hardened score compression subsequently showed how leading nuisance sensitivities can be projected from compressed cosmological summaries [Alsing & Wandelt 2019], while model-specific singular-value subspaces have been used to compress large-scale-structure observables and reduce covariance noise [Philcox et al. 2021]. Information-geometric approaches formulate cosmological inference as a Fisher-metric manifold and analyze degeneracy directions geometrically [Giesel et al. 2021]. We therefore do not claim novelty for projection, principal-angle or subspace geometry, Fisher metrics, or nuisance hardening as mathematical operations.

A particularly close conceptual precedent is the observation that data compression optimized for a baseline physical model can suppress, or even remove, information needed to test physics outside that model [Heavens, Sellentin & Jaffe 2020]. This prior result is directly relevant to the interpretation of our representation-null control. Exp071M does not establish for the first time that a representation can hide physical information. Rather, it provides a fail-closed implementation of that concern inside the DSIR falsification chain: the primordial-tilt nuisance is exactly unresolved in transfer-only `t_tot`, the zero response is prevented from entering normalized-angle geometry, and the outcome is retained as `INVALID_FOR_SCIENCE` rather than converted into evidence for or against specificity.

The narrower contribution of DSIR-2 is the ordering imposed on these established ingredients. A response representation is declared before scoring; every candidate nuisance must pass a numerical resolvability gate before normalization; the physical nuisance freedom is represented as an oriented ray, a two-sided line, or a higher-dimensional subspace according to its allowed parameter freedom; and apparent specificity is retained only if it survives prospectively frozen known-sector controls. This ordering is tested rather than assumed. In the K2 sequence, a positive baryon/CDM-redistribution ray remains strongly separated after temporal and velocity transformations, amplitude removal and support deletion, yet a prospectively generated opposite-sign displacement reveals that the full nuisance line overlaps the tested GDM directions. In the independent K1 sequence, transfer-only response is exactly null; after the missing primordial-spectrum contribution is restored in a newly preregistered common velocity-power representation, the nuisance becomes resolvable but its two-sided line still overlaps the tested GDM directions.

Recent work has also applied Fisher information geometry directly to dark-matter inference, quantifying how lens and source nuisance freedom can absorb information about an unresolved dark-matter substructure population [Adam 2026]. This makes a broad priority claim for “dark-matter nuisance geometry” inappropriate. The distinction of the present study is instead operational and falsification-oriented: solver/provider provenance, representation resolvability, ray-versus-line semantics, independent known-sector controls, exact-null retention, recovery in a physically complete representation, and finite-support applicability are kept in one auditable chain.

Accordingly, the paper's novelty claim should remain at the workflow level. A safe formulation is:

> Our contribution is not a new projection or information-geometric formalism, but a fail-closed response-comparison workflow that makes representation resolvability and the physical nuisance object explicit before assigning specificity, and tests that workflow prospectively with independent known-sector falsification controls.

Any stronger priority sentence, including “to our knowledge” language concerning the complete conjunction of these steps, should remain outside the Abstract until a final full-text and citation-graph audit is completed immediately before submission.

## References for this section

- W. Hu, Astrophys. J. 506 (1998) 485–494, DOI `10.1086/306274`, arXiv:`astro-ph/9801234`.
- M. Kopp, C. Skordis, D. B. Thomas, Phys. Rev. D 94 (2016) 043512, DOI `10.1103/PhysRevD.94.043512`, arXiv:`1605.00649`.
- D. B. Thomas, M. Kopp, C. Skordis, Astrophys. J. 830 (2016) 155, DOI `10.3847/0004-637X/830/2/155`, arXiv:`1601.05097`.
- M. Kunz, S. Nesseris, I. Sawicki, Phys. Rev. D 94 (2016) 023510, DOI `10.1103/PhysRevD.94.023510`, arXiv:`1604.05701`.
- A. F. Heavens, R. Jimenez, O. Lahav, MNRAS 317 (2000) 965–972, DOI `10.1046/j.1365-8711.2000.03692.x`, arXiv:`astro-ph/9911102`.
- J. Alsing, B. Wandelt, MNRAS 488 (2019) 5093–5103, DOI `10.1093/mnras/stz1900`, arXiv:`1903.01473`.
- A. F. Heavens, E. Sellentin, A. H. Jaffe, MNRAS 498 (2020) 3440–3451, DOI `10.1093/mnras/staa2589`, arXiv:`2006.06706`.
- O. H. E. Philcox et al., Phys. Rev. D 103 (2021) 043508, DOI `10.1103/PhysRevD.103.043508`, arXiv:`2009.03311`.
- E. Giesel et al., JCAP 2021(01) 005, DOI `10.1088/1475-7516/2021/01/005`, arXiv:`2005.01057`.
- A. Akhmetzhanova, S. Mishra-Sharma, C. Dvorkin, MNRAS 527 (2024) 7459–7481, DOI `10.1093/mnras/stad3646`.
- A. Adam, arXiv:`2608.18224` (2026; publication status to be rechecked at submission).
