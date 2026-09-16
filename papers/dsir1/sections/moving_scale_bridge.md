## 3.4 Moving characteristic scales and scale-time nonseparability

The response atlas suggests a useful distinction between the existence of a characteristic scale and the appearance of irreducible scale-time structure. A local translated-feature ansatz makes that distinction explicit. Let \(x=\ln k\) and write

\[
R(x,z)=a(z)+F[x-\delta(z)],
\qquad
\delta(z)=\ln k_*(z),
\]

where \(k_*(z)\) is a mechanism-native characteristic scale and \(F\) is the local scale profile of the response feature. Then

\[
\frac{\partial^2R}{\partial x\,\partial z}
=-\delta'(z)F''[x-\delta(z)].
\]

An exactly additive response \(T(x)+\tau(z)\) has zero mixed derivative. Within this local ansatz, a translated feature therefore becomes intrinsically scale-time nonseparable only where the characteristic scale moves with redshift and the profile has nonzero curvature in \(\ln k\). A stationary cutoff can be strongly scale dependent while remaining almost perfectly time separable.

The same statement connects directly to the discrete DSIR interaction matrix. Writing \(\delta_i=\bar\delta+\epsilon_i\) and expanding to first order,

\[
F(x_j-\delta_i)
=F_j-\epsilon_iF'_j+O(\epsilon_i^2),
\]

then applying the equal-weight double-centering operator of the decomposition \(R_{ij}=\mu+T_j+\tau_i+I_{ij}\) gives

\[
I_{ij}
\simeq
-(\epsilon_i-\bar\epsilon)
\left(F'_j-\overline{F'}\right).
\]

Thus the leading interaction is an outer product and has rank one. Its temporal singular direction follows the centered motion of \(\ln k_*\), while its scale singular direction follows the centered derivative of the feature profile. Higher-order drift, profile-shape evolution, multiple moving scales, or coupled amplitude evolution can generate higher-rank corrections.

Thermal WDM supplies a retrospective consistency check rather than a new withheld test. On the immutable high-\(k\) WDM matrices, the span of \(\ln k_{0.1}(z)\) is only \(1.81\times10^{-5}\) to \(3.25\times10^{-5}\) across the tested masses, consistent with the extremely small \(\chi_I\simeq2.2\times10^{-10}\)--\(2.6\times10^{-10}\). Nevertheless the small residual interaction is almost one-dimensional: the first singular component contains at least 99.9% of the interaction energy, its temporal direction has absolute cosine above 0.998 with the measured cutoff drift, and the full first-order outer-product template has Frobenius cosine about 0.916--0.919 with the measured \(I\) matrix.

This bridge is explanatory, not universal. It does not imply a calibrated law \(\chi_I=f(\Delta\ln k_*)\), does not justify comparing absolute \(\chi_I\) values across unlike scale domains, and does not close G7/G8/G9. Its role in DSIR-I is narrower: it explains why a strong scale-dependent mechanism can have tiny scale-time interaction, and why moving characteristic scales can naturally generate low-rank nonseparable response structure.
