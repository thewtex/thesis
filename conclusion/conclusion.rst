========================
Chapter 10 : Conclusions
========================

.. sectnum::
  :prefix: 10.

~~~~~~~
Summary
~~~~~~~

This dissertation described diagnostic ultrasound methods for characterization
of carotid atherosclerosis.  Carotid characterization is important because of
carotid plaque's role in stroke.  Vulnerable carotid plaques generate emboli
that cause cerebral ischemia.  The purpose of *in vivo* ultrasonic characterization is
to determine which plaques are likely to cause future events.

In the literature review, the imaging techniques that have been applied to this
problem are examined.  A number of modalities have tried to associate features
of composition, ulceration, hemodynamic stress, inflammation, morphology, or the
vasa vasorum with vascular vulnerability.  By examining the theory of solid-body
mechanics, it was hypothesized that the quantity that summarizes the combined
effect of all the previously studied features is strain, a measure of the
material deformation.

Noise due to out-of-plane motion, image decorrelation, discretization, and
limited image frequency content make it difficult to robustly quantify plaque
strain *in vivo*.  A number of techniques were described to improve the
robustness of the strain images.  A Bayesian regularization technique was
described that greatly improves the robustness of the tracked images.  This
regularization technique was parameterized by the amount of expected strain.  An
unbiased subsample displacement interpolation method that reduces bias errors,
especially in the lateral direction, was explored.  Furthermore, strain calculation was
improved around the discontinuity that can occur at the wall-lumen boundary by
detecting and accounting for this discontinuity.  The quality of the strain
images were kept high by using a dynamic incremental frame skip, while an
algorithm was presented to still obtain the incremental strain at equal time
steps.  A multi-level motion tracking framework further improved algorithm
robustness.  Tracking lower frequency image content with large matching-blocks
reduced peaking-hopping errors.  Search region reduction over levels also
decreased peak-hopping errors.  Inter-level scaling of the matching block
improved overall tracking quality.  In prior strain imaging work, obtaining all
components of the strain tensor proved difficult because of the lower
resolution in the lateral direction.  Because of the algorithmic methods
employed, effective quantification of all components of the 2D strain tensor was
achieved.  It was shown how the strain tensor can be represented with an
elliptical glyph.  New quantities derived from the strain tensor that have been used
in other contexts as material failure criteria were proposed as indices of
plaque vulnerability.

Five case studies were examined that demonstrated strain image features and how
they correspond to different conditions associated with plaque vulnerability.  A
hypoechoic plaque, associated with soft, weak materials, exhibited high strain.
High strain was also observed in a region where a plaque protruded into the lumen.
In the third case, high strain was observed local to a post-stenotic region with turbulent
flow.  A large of amount of longitudinal deformation at the base of a plaque was
also observed, which possibly may be attributed to the shape of the plaque or
vasa vasorum.  Finally, a plaque that had many abrupt transitions between
calcified and soft areas was presented high strain in these transition
regions.

*Ex vivo* plaque characterization methods were also explored with high-frequency
quantitative ultrasound.  Most quantitative methods require spectral
information, and calculation of a characteristic local power spectrum requires a
window of relatively homogenous tissue.  Since plaque is relatively small and
heterogeneous, high transmit frequencies are desirable.  Techniques for using a
commercial high-frequency system to create 3D integrated backscatter
coefficient images with the reference phantom method were developed.
Experimental techniques for estimating the acoustic properties of the reference
phantom were improved and adjusted from the low-frequency techniques.

Finally, transcranial Doppler ultrasound (TCD) was performed with the aim of
detecting micro-emboli to validate strain image derived metrics of
vulnerability.  While microemboli were successfully detected, general
confidence in the results was compromised by challenges such as motion
artifacts.  A number of approaches to improve the quality of TCD data were
discussed.

~~~~~~~~~~~
Future Work
~~~~~~~~~~~

With a larger cohort of subject data, various measures of ischemic burden, such
as TCD microembolic signals, can be used in the future to validate the
hypothesis that carotid plaque strain is correlated with risk of adverse
ischemic events.  Not all subjects that receive carotid endarterectomy (CEA)
have had previous ischemic events, and those that are classified as symptomatic
as opposed to asymptomatic should be considered higher risk.  Neural MRI data
can be used to quantify atrophy and ischemic regions.  Strain results can also
be compared to neuropsychological assessments that index executive function and
activation, visio-spatial ability, language and lexical retrieval, and memory
and learning.  It remains to be seen how effective ultrasound strain imaging is
at differentiating high-risk plaque, and which strain metric or combination of
metrics are the most effective.

Preliminary work has found that it is feasible to create closely spaced (50 μm),
serial, longitudinal histopathological slides of an *in vitro* plaque.  If these
slides can be registered against each other to create a 3D volume, the
histopathological images can be registered against the high-frequency plaque
volume.  If the histopathological slides are segmented by composition, the
correspondence between quantitative ultrasound image values and tissue types can
be quantified.  Also, a fully sampled 3D ultrasound volume may be used to
determine the histopathological slices that correspond to the 2D *in vivo*
ultrasound images.
