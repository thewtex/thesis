==================================================
Chapter 7 : High-frequency Plaque Characterization
==================================================

.. sectnum::
  :prefix: 7.

High-frequency ultrasound imaging is useful for examining tissue structures and
inhomogeneitites like calcifications -- it
has the advantage of high resolution at the expense of low penetration.  In this
chapter new high frequency imaging techniques are explored for interrogation of
the excised plaques which result from carotid endarterectomy procedures.  First the materials and
methods used to create these images are described.  Note that many other details
are found in Appendix A.  Then, initial 3D parametric images of the excised
plaques are presented.

.. |apparatus| replace:: Fig. 7.1

.. |apparatus_long| replace:: **Figure 7.1**

.. |envelope| replace:: Fig. 7.2

.. |envelope_long| replace:: **Figure 7.2**

.. |pat142| replace:: Fig. 7.3

.. |pat142_long| replace:: **Figure 7.3**

.. |pat144| replace:: Fig. 7.4

.. |pat144_long| replace:: **Figure 7.4**

.. |pat154| replace:: Fig. 7.5

.. |pat154_start| replace:: Figure 7.5

.. |pat154_long| replace:: **Figure 7.5**

.. |pat158| replace:: Fig. 7.6

.. |pat158_long| replace:: **Figure 7.6**


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Creation of parametric images of excised plaque
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

As mentioned in the Chapter 2, strain imaging holds promise because it is a
direct measure of the local load the tissue is experiencing as opposed to
approaches where measurements or assumptions of composition, geometry, and
loading are used in a computational model or statistical classification to imply
loading.  An advantage to this approach is that errors from modeling
simplifications and parameter measurements do not accumulate as significantly.
The reference phantom method is analogous for ultrasonic tissue parameter
characterization.  Diffraction effects are measured empirically in a phantom
environment similar to that expected *in situ* with minimal modeling or
assumptions.

Approximately two weeks following the *in vivo* carotid ultrasound
examination and TCD recording, patients undergo surgery for plaque excision.
Endarterectomy specimens are retrieved immediately following surgery for
scanning and returned the same day to pathology for analysis and histology
preparation.  Samples are examined in a water bath and suspended between two
catheter sheaths.  A photograph  of the experimental setup is shown in |apparatus|.

.. image:: images/apparatus.png
  :align: center
  :width: 16cm
  :height: 6.33cm
.. highlights::

  |apparatus_long|: High-frequency apparatus.  The transducer is fixed to a 3D
  motion table and lowered into the water bath.  A disposable transducer cover
  is covered with coupling gel and held to the transducer with a rubber band for
  safety reasons.  The plaque is suspended between two catheter sheaths and the
  stepper motor moves the transducer parallel to the longitudinal direction of
  the plaque.

VisualSonics Vevo 770 is used for the high frequency ultrasound radiofrequency acquisition.  The
system for 3D collection and processing of RF data on the Vevo 770 is described
in Appendix A.

The transducer selected is a RMV710B that has a center frequency of 25 $MHz$,
which is on the lower end of the center frequency for available transducers.  This
transducer outputs frequencies up to 37.5 MHz, with an axial resolution of 70
μm, lateral resolution of 140 μm, focal length 15 mm, and a maximum
field of view of 20.0 mm.  The RMV710B is selected because the frequency is
low enough to penetrate the plaque and the field of view is large enough to
encompass the entire sample.

RF acquisition was previously limited to
single 2D frames, but we worked with VisualSonics engineers such that RF
acquisitions can be collected in 3D with the optional high-precision stepper
motor.  Each acquisition consists of 250 beam lines separated by
approximately 60 μm, 2128 samples (3.9 mm), and up to 250 frames
separated by 200 μm to 100 μm depending on the length of the plaque
specimen.  Some longer plaques may require larger inter-frame spacing because of
memory limitations, although the resolution in the elevational direction is
nominally 140 μm for the RMV710B transducer.

For the lengths of the plaques
scanned, which ranged from approximately 20 mm to 40 mm, this filled the
system limits on acquisition.  The collection of a single 3D data set covering an entire
plaque takes approximately one to two hours.  Resulting files are approximately 150 μm per
volumetric slice.  Three to five volumetric slices are required to encompass
the majority of an excised plaque's volume.  Some longer plaques may require
larger inter-frame spacing because of memory limitations, although the
resolution in the elevational direction is nominally 140 μm for the RMV710B
transducer.

Integrated backscatter coefficient (IBSC) images are created with a reference phantom created by Dr. Ernest L. Madsen, PhD
from UW-Madison.  The reference phantom is made of the 5000E material
characterized in Chapter 6.  The reference phantom was scanned with the same
transducer and system settings as utilized for scanning the plaque specimen.
This includes the plastic covering over the transducer that prevents
contamination of the transducer by plaque. Reference power spectra are obtained
by averaging 30 lines per plane over 60 planes.  Fourier spectra with 50%
overlap are calculated using a Fast Fourier Transform with 128 Hamming windowed
points (240 μm), and the bandwidth used ranged from 6.6 MHz to 29.6 MHz.
The BSC of the reference phantom is interpolated from
the values measured with the reference reflector in Chapter 6.  Attenuation in
the plaque specimen was assumed to be the same as reference phantom, which is reasonable
for arterial plaque specimens based on values reported in the literature
[Hoskins2007,Lockwood1991]_ The backscatter was calculated using the expression
[Liu2007]_, below:

.. math::   BSC_s(f) = \frac{BSC_r(f) S_s(f)}{S_r(f)}

Log compression and linear interpolation were applied to the displayed IBSC
images.
Identical dynamic ranges and color transform functions were used in all corresponding images.

~~~~~~~~~~~~~~~~~~~~~
B-Mode image creation
~~~~~~~~~~~~~~~~~~~~~

The received pulse-echo signal, that is RF data, is
highly oscillatory.  An envelope of the RF data reflects local scattering
amplitude, and this is what comprises a B-Mode image.

.. image:: images/envelope.png
  :align: center
  :width: 8cm
  :height: 5.25cm
.. highlights::

  |envelope_long|: Sample RF signal and its corresponding envelope.

Calculation of the RF envelope is often performed with the analytic signal.  The
analytic signal is used to decompose a signal into its local amplitude and 
phase [Felsberg2001,Woo2008a]_ [#]_.  The analytic signal, *f*\ :sub:`A`\ *(x)*, of a real
signal, *f(x)*, is defined to be

.. math::  f_A(x) = f(x) - i \, f_H (x)

.. [#] Local phase is a 1D concept, and the analytic signal is not defined for multi-dimensional signals.  To split a multi-dimensional image into structural and energetic information, see the monogenic signal [Felsberg2001]_.

.. epigraph::

  where *f*\ :sub:`H`\ *(x)* is the Hilbert Transform of *f(x)* given by

.. math::  f_H(x) = \frac{1} {\pi} \int_{-\infty}^{\infty} \frac {f(x')}{x' - x} \, dx'

The Hilbert Transform can be calculated without performing
convolution by applying the following property in Fourier space,

.. math::  F_H(\xi) = F(\xi) \cdot i \, \text{sgn} (\xi)

As a result, the analytic signal's representation in Fourier space is

.. image:: images/bmodeeqn1.png
  :align: center
  :width: 6cm
  :height: 1.70cm

Even though it does not have ideal properties when applied to a discrete
signal [Bracewell2000]_ an approach to calculate the analytic signal is then
to calculate the Fourier Transform, multiply the first half by two, multiply the
second half by zero, and take the inverse Fourier Transform.

For narrow band signals, the local phase, :math:`\phi(x)`, and the local energy,
*A(x)*, of *f(x)* can be interpreted as [Felsberg2001]_

.. image:: images/bmodeeqn2.png
  :align: center
  :width: 6cm
  :height: 1.65cm

After the envelope, *A(x)*, is calculated, post-processing can be performed.
The majority of an ultrasound image's content is speckle, random scattering
caused by scatterers much smaller than the excitation wavelength, which follow
a Rayleigh distribution [Wagner1983]_.  Since the Rayleigh distribution is
skewed to lower values and a very small proportion of the amplitudes having very large
values, a logarithmic intensity transform is commonly applied to the envelope to
improve image contrast.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
3D high frequency plaque volumes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Gross photographic images taken prior to ultrasound scanning, B-mode images
derived from the RF, and integrated backscatter coefficient (IBSC) images for two patients
are shown in the following figures.

.. image:: images/pat142.png
  :align: center
  :width: 15cm
  :height: 19.3cm
.. highlights::

  |pat142_long|: Images taken from the plaque excised from Subject 142.
  A large, diffuse hemorrhagic region shows decreased backscatter.
  a) Gross photographic image, b) close-up gross image, c) B-Mode
  volume rendering, d) integrated backscatter volume rendering, e) B-Mode
  tri-planar view, and f) IBSC tri-planar view.

.. image:: images/pat144.png
  :align:  center
  :width:  15cm
  :height: 19.0cm
.. highlights::

  |pat144_long|: Images of the excised plaque from Subject 144.  The gross
  photographs in a) and b) show a primarily fibrous plaque with some calcified
  areas.  The ultrasound B-Mode, c) and e), and IBSC, d) and f),  show the presence of fibrous
  and calcified areas well.  Segments from the catheter sheath are seen in the
  front and back of c) and d).  To reduce saturation from numerous calcified
  areas, data was collected with -10 dB gain relative to |pat142|\ a), which
  explains the larger impact of electronic noise in c).

Note the presence of the catheter used to suspend the plaques in these
images.  It is clearly visible as a high intensity cylinder.  In Subject 142,
as seen in |pat142|, it is visible on the right and rear in the volume renderings.  The
catheter protrudes from the tips along the axis of the internal carotid artery
(ICA) segment for Subject 144, shown in |pat144|.  It extends deeply into the bulb and
ICA segment of Subject 154, as seen in |pat154|.  It reaches from the start of the bulb up
into the bifurcation on one side and only slightly penetrates the ICA for Subject
158, in |pat158|.  In general, the IBSC images look 'cleaner' than the B-Mode
images with similar spatial resolution.  This can be attributed to the
removal of speckle in the IBSC.

Subject 142 shows a possible high-risk plaque with an extensive hemorrhagic area
that may have been the result of recent rupture events.  There were strong
indications of inflammation when this plaque was removed.  The backscatter
coefficient is consistently low throughout the hemorrhagic areas.  This
condition that is typically considered high risk and the high risk assessment is
re-enforced by the fact that microembolic signals were detected with
transcranial Doppler for Subject 142 (Table 8.1).  The result for Subject 144 on
the other hand, depicts a likely stable plaque with smooth, un-ulcerated walls
and strong fibrous and calcified tissue throughout.  Note the abundance of very
high magnitude IBSC in Subject 144 because of calcifications.  In a pathologist's
independent assessment of the histopathological slides of the same specimens,
Subject 142 was found to have approximately 5% calcified content, while Subject
144 was found to have 55% calcified content.  This is consistent with the
ultrasound results in |pat142| and |pat144|.

The system receive gain was set 10 dB higher during the acquisition of plaques
in |pat142|
than that for |pat144|.  This reduced the amount of saturated signal due to the
calcifications.  However, this also increases the relative amplitude of
electronic noise, which is most evident in the B-Mode volume rendering,
shown in |pat144|\ c).  The purpose and benefits of the reference phantom methods are
clearly illustrated in |pat144|\ d), which is not duly affected by this change in the system
settings.  Since the electronic noise is equivalently elevated in the reference
phantom signal, the change is nullified in terms of the output image.  In
comparison to the B-Mode image, the IBSC image is a more consistent
representation of the object being profiled.

The tip of the flow divider, also known as the tuning fork, can be easily
located in these images.  This fiducial marker can be used to identify the
corresponding region within *in vivo* data.

.. image:: images/pat154.png
  :align: center
  :width: 15cm
  :height: 18.7cm
.. highlights::

  |pat154_long|: The excised plaque from Subject 154.  *In vivo* strain
  characterization of this subject is shown in Figure 9.10.
  a) Gross photographic image, b) close-up gross image, c) B-Mode
  volume rendering, d) integrated backscatter volume rendering, e) B-Mode
  tri-planar view, and f) IBSC tri-planar view.

.. image:: images/pat158.png
  :align: center
  :width: 15cm
  :height: 19.07cm
.. highlights::

  |pat158_long|: The excised plaque from Subject 158.  *In vivo* strain
  characterization of this subject is shown in Figure 9.14.
  a) Gross photographic image, b) close-up gross image, c) B-Mode
  volume rendering, d) integrated backscatter volume rendering, e) B-Mode
  tri-planar view, and f) IBSC tri-planar view.

|pat154_start| and |pat158| show plaques attained from surgery that are used as
strain case
studies in Chapter 9.  Subject 154, in |pat154| and Fig. 9.10, is used as an example of a plaque
with a 'soft' hypoechoic presentation and that has high strain.  Both the gross
pathological appearance corroborates this assessment as does the 3D ultrasound
characterization.  The gross pathology shows a smooth, relatively homogeneous
lipid and fibrous color.  It is evident that the structure deforms under its own
weight in comparison to the gross pathological image in |pat144|.  The IBSC image
has low backscatter coefficients and is homogeneous with the exception of a few
small pockets.

In contrast to Subject 154, a large acoustic shadow marks the B-Mode in Fig. 9.14.  Very
little strain is seen in the calcific region.  However, other regions of the
plaque do not exhibit the same shadowing, and some have very high strains.
The gross pathology in |pat158|\ a) and b) give a complex presentation with at
least one region of hemorrhage/necrosis clearly visible in |pat158|\ b).  The ultrasound also
shows a complex presentation with IBSC values consistent with calcific regions
at the bifurcation and along one side of the ICA segment.  It is possible that
the focal, calcific region may explain the shadowing in Fig. 9.14 while the
hemorrhagic regions could be the source of high strains.  The noise present
in the ultrasound images of Subject 158 is explained by a known malfunction of the
transducer at that time.

In conclusion, 3D, high-frequency parametric ultrasound images may be a useful
tool for plaque characterization.  At a minimum, calcific areas can be
identified.  It was shown that the use of the reference phantom method improved
the quality and content of the images.  With a 3D volume, easy correlations are
made between shapes in the gross pathology images and the ultrasound images.  In
the future, this data may be useful for registering histopathology slides
against regions within *in vitro* high-frequency ultrasound images, which in turn
may be registered again external ultrasound to quantify the composition in the
latter.

~~~~~~~~~~
References
~~~~~~~~~~

