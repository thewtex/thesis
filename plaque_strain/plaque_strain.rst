=============================================================
Chapter 9 : *In vivo* Quantification of Carotid Plaque Strain
=============================================================

.. sectnum::
  :prefix: 9.

Finally, we present results from *in vivo* characterization of carotid plaque
strain with diagnostic ultrasound via an externally applied transducer.  First,
the algorithms to generate the strain images and reduce the results are
described.  This includes an explanation of how the algorithms described in detail
during chapters 3, 4, and 5 are applied to the integrated algorithm.
Additionally, new features are covered, including the hierarchical framework.
Finally, case studies of a few subjects are presented.

.. |scalespace| replace:: Fig. 9.1

.. |scalespace_long| replace:: **Figure 9.1**

.. |companding| replace:: Fig. 9.2

.. |companding_long| replace:: **Figure 9.2**

.. |displacement_sequence_options| replace:: Fig. 9.3

.. |displacement_sequence_options_long| replace:: **Figure 9.3**

.. |strain_sequence_options| replace:: Fig. 9.4

.. |strain_sequence_options_long| replace:: **Figure 9.4**

.. |plaque_regions| replace:: Fig. 9.5

.. |plaque_regions_long| replace:: **Figure 9.5**

.. |strain_plots| replace:: Fig. 9.6

.. |strain_plots_long| replace:: **Figure 9.6**

.. |hypoechoic| replace:: Fig 9.7

.. |hypoechoic_long| replace:: **Figure 9.7**

.. |geometry| replace:: Fig. 9.8

.. |geometry_long| replace:: **Figure 9.8**

.. |turbulence| replace:: Fig. 9.9

.. |turbulence_long| replace:: **Figure 9.9**

.. |wallshear| replace:: Fig. 9.10

.. |wallshear_long| replace:: **Figure 9.10**

.. |shadowing| replace:: Fig. 9.11

.. |shadowing_long| replace:: **Figure 9.11**

.. |out_of_plane| replace:: Fig. 9.12

.. |out_of_plane_long| replace:: **Figure 9.12**



.. |downsampling_schedule| replace:: Table 9.1

.. |downsampling_schedule_long| replace:: **Table 9.1**

~~~~~~~~~~~~~~~~~~~~~~
Hierarchical framework
~~~~~~~~~~~~~~~~~~~~~~

Multi-level motion tracking
===========================

Multi-resolution motion tracking methods have long been established as the way to
increase the speed and robustness of medical image registration
[Wu2003,Likar2001,Wu2000,Crum2004,Tzovaras1994,Schnabel2001,Vemuri1998,Zitova2003]_.
In general, a coarse-to-fine tracking scheme is applied by performing
registration of the image pair at multiple resolutions.  Results from
registration at a coarser resolution level are used to initialize the
registration problem at the next, finer resolution level.  The lower resolution
images are often subsampled, so motion tracking is faster.  Even
though multiple registration operations are performed at every level, including
the finest level is at the original image resolution, the overall motion tracking
method is often quicker than a single non-hierarchical registration.  By
initializing the search close to the true displacements at finer levels, the
solution space that must be examined in a more computationally taxing settings
is greatly reduced.  Also, local minima in the solution associated with the high
frequency content in the fine resolution images are avoided.  This improves
robustness of the algorithm.

Multi-resolution methods have been applied to ultrasound strain imaging.  Yeung
et al. and Pellot-Barakat et al. developed a multilevel regularized,
block-matching algorithm for tracking ultrasound speckle
[Yeung1998,Pellot-Barakat2004]_.  In Yeung et al., coarser level images
were not subsampled on the premise that high-frequency speckle information would
be lost.  Instead, the multi-resolution notion is applied by changing the
matching-block size and the search region extent.  Displacements are initially
found with a large matching-block and wide search region and are transition to a
small matching-block and confined search region.  The large matching-blocks are
not as sensitive to decorrelation noise.  Smaller matching-blocks are not as
affected by intra-block non-rigid motion and are capable of more precise
displacements.  Shi and Varghese discussed a multilevel where coarser levels
were downsampled versions of the envelope image [Shi2007]_.  Instead of only
using displacements at coarser levels to initialized the search region at finer
levels, Bai et al., combined the cross-correlation results from window lengths
at multiple levels to determined the displacements at the finest level
[Bai1999]_.  Basarab et al. found that iterative application of a
multi-resolution can improves results even more [Basarab2008]_.  Chen et al.
applied the multi-level approach to a quality-guided (seed propagation)
algorithm [Chen2010a]_.

Multi-resolution methods are particularly useful when imaging arteries, where
there is motion discontinuity at the artery wall.  Other block-matching motion
tracking algorithms often propagate match-block search regions from prior
displacements of high confidence [Jiang2009,Basarab2008]_.  These restricted
search regions reduce the detection of local minima in the similarity metric
(peak-hopping errors).  This continuity cannot be assumed when the artery walls
move apart, and search region initialization from a coarser level plays a
similar role.


In this work a multi-level block-matching algorithm is used for motion tracking
of carotid plaque images.  Displacements tracked at coarser levels are
interpolated to initialize the search region location at lower levels.  Image
sets at every level are created with a scale-space representation of the the
images [Lindeberg1994]_.  The scale-space representation is chosen because it
has many desireable properties including the *non-enhancement* property, i.e.
local extrema are not enhanced [Lindeberg1994]_.  If the local extrema are
enhanced, the artificial feature may be tracked by the similarity metric.  Each
level in the scale-space is created by filtering the input radio-frequency (RF)
image with discrete Gaussian that has a variance *(f/2)*\ :sup:`2` if *f* is
the decimation factor.  A three-level image pyramid is created.  The decimation
factor for each level is given in |downsampling_schedule|.  Since image content
is much more dense in the axial direction, higher decimation is allowed in that
direction.  An example set of scale-space images are shown in |scalespace|.

.. image:: images/scalespace.png
  :align: center
  :width: 16cm
  :height: 5.16cm
.. highlights::

  |scalespace_long|:  Scale-space images for multi-resolution motion tracking.
  Carotid plaque RF data in the longitudal view for subject 157 is shown.
  The levels, whose decimation factors are given in |downsampling_schedule|,
  are a) level 1, b) level 2, and c) level 3.

=========== ========================= ===========================
Level        Axial decimation factor  Lateral decimation factor
----------- ------------------------- ---------------------------
1            3                        2
2            2                        1
3            1                        1
=========== ========================= ===========================

.. highlights::

  |downsampling_schedule_long|: Downsampling schedule for the multi-resolution
  image registration.

Search region refinement
========================

As previously mentioned, restriction of a matching-block's search region as
finer levels in the pyramid are explored can increase the robustness of
tracking.  For the results explored in this chapter, a simple linear function
was applied the search region size from the coarsest level to the finest level.
The value of these parameters are shown in |displacement_sequence_options|.  The
search region size is expressed as a factor of the matching-block size, and it is
greater than 1.  Note that even if the search region factor was specified to be
the same at the top level and the bottom level, the search region still shrinks
in physical size since the matching-block size is specified in pixels and
decimation occurs between levels.

While search region restriction can improve robustness, this is not true if
there is poor motion tracking in the upper levels.  If inaccurate motion
tracking occurs at upper levels, the erroreous displacement will propagate to
levels.  To counter this phentomenon, erroreous displacements are detected and
replaced before using them to initialize the center of the search region at
lower levels.  Peak-hopping errors present themselves as irrationally high
strains because they cause a discontinuity in the estimated displacement field.
To prevent the propagation of peak-hopping errors, a strain image is generated
at the higher levels.  Pixels whose strain magnitude exceed a threshold are
marked for replacement.  Displacements are then linearly interpolated across a
cluster of errant pixels if the pixels are in the center of the image, or the
are extrapolated with the slope of the closest good displacement pixels at the
edge of the image.  This process is repeated to remove any outliers that remain
or were introduced.

Inter-level matching-block scaling
=====================================

De-correlation within a matching-block is partially caused by the strain within
the block [Varghese1996]_.  The de-correlation of the matching-block can be
reduced by scaling, 'companding',  the matching block by the local strain
[Chaturvedi1998,Chaturvedi1998]_.  In the hierarchical construct, the strain
found at higher levels can be used to stretch or compress the matching block
before performing cross-correlation at lower levels.  This is applied to this
algorithm by resampling the matching-block with windowed-sinc interpolation
after anisotropically scaling the block by a factor

.. math:: s_i = 1 + e_{ii}^*

where the scaling factor is one plus the normal strain in that direction if the
strain is small.  Improvement of the strain *SNRe*, described in detail in
Chapter 3 and 4, for a uniform phantom is demonstrated in |companding|.  There
is a significant improvement in the *SNRe* when scaling the matching block.  The
amount of this improvement increases with the increase in strain magnitude.

.. image:: images/companding.png
  :align: center
  :width: 8cm
  :height: 5.99cm
.. highlights::

  |companding_long|: Axial strain *SNRe* versus strain magnitude when scaling
  the matching-block according to the strain obtained in the previous level and
  without scaling.

~~~~~~~~~~~~~~~~~~~~~~~
Displacement estimation
~~~~~~~~~~~~~~~~~~~~~~~

Motion tracking is performed with a hierarchical block-matching technique,
implemented in C++.  A multi-resolution, multi-threaded block-matching
framework is implemented on top of the InsightToolkit [Ibanez2005,Yoo2002]_.
The similarity metric used for comparing a matching-block in the pre-deformation
image in its search region in the post-deformation image is normalized
cross-correlation.  Recursive Bayesian regularization, described in Chapter 3,
is used to improve the quality of the tracked displacements at each level.
Parabolic interpolation is used to find subsample displacements at the upper
levels, and windowed-sinc interpolation with numerical optimization, decribed in
Chapter 4, is used to find subsample displacements at the final level.  The
A central-difference gradient with an order of accuracy of 4, explained in
Section 5.2.1, is used to estimate strains at the higher levels where
displacement vector sampling is very coarse.  Strains at the higher levels are
used to remove peak-hopping pixels and scale the matching-block in subsequent
levels.  

Displacements are tracked from a continuous sequence of RF data collected on the
longitudinal views of the carotid with the Siemens Antares clinical ultrasound
system (Siemens Ultrasound, Mountain View, CA, USA).  Patients are scanned prior
to endarterectomy after receiving informed consent on a protocol approved by the
University of Wisconsin-Madison Institutional Review Board (IRB).  The Antares
VFX13-5 transducer is excited at 11.4 MHz to collect RF at a sampling rate of 40
MHz to a depth of 4 cm.  A dynamic frame skip and displacement interpolation
algorithm, explained in Section 5.4.1, generates a sequence incremental
displacement images that are evenly spaced in time.

Values of the parameters used in the algorithm are summarized in the
configuration file shown in |displacement_sequence_options|.
Upsampling on the input two byte signed integer input RF data is performed with
windowed-sinc interpolation.  The size of the matching-block is specified in
samples.  To ensure the window is center on a point, the length of the
matching-block is specified as a radius so that the length of the window is *2 r
+ 1* if *r* is the radius.

::

  # displacement-sequence options input file.
  ---
  files:
    # The input image.  It should be a 3D image where the first two dimensions
    # are space, and the third dimension is time.
    sequenceImage: @SEQUENCE_IMAGE@
    # File name prefix for output files.
    outputPrefix:  @OUTPUT_PREFIX@

  parameters:
    # Any point with a strain component above the given value in the higher levels
    # will have its displacement interpolated by surrounding areas.
    maximumAbsStrainAllowed: 0.075
    # Upsampling ratio of the input images.
    upsample: [ 2.0, 2.0 ]
    # Axial direction of the image.
    axialDirection: 1

    # Related to the matching block.
    block:
      # Block Radius at the top level.
      topBlockRadius:    [ 15, 28 ]
      # Block Radius in at the bottom level.
      bottomBlockRadius: [ 10, 18 ]
      # Block overlap. 1.0 is no overlap. 0.5 is 50% overlap.
      blockOverlap:      1.0
      # In the multiresolution method, scale the matching block by the strain
      # estimated at higher levels.
      scaleByStrain:     true

    # Related to the search region.
    searchRegion:
      # Search region radius at the top level is the following factor times the block radius.
      # The factors at intermediate levels between the top level and bottom level
      # are linearly interpolated.
      topFactor:     [ 2.2, 1.4 ]
      # Search region radius at the bottom level is the following factor times the block radius.
      bottomFactor:  [ 1.1, 1.1 ]

    # Related to the Bayesian regularization.
    regularization:
      # Strain regularization parameter.
      strainSigma: [ 0.07, 0.07 ]
      # Maximum number of iterations during regularization at the bottom level.
      maximumIterations: 3

    # Related to the sequential calculation of displacements.
    sequence:
      # The index of the first frame to use as the fixed image.  A value of -1
      # indicates the use of the first index available.  Counts from 0.
      startFrame: @START_FRAME@
      # The index of the last frame to use as the moving image.  A value of -1
      # indicates the use of the last index available.  Counts from 0.
      endFrame:   @END_FRAME@
      # In the case of a static frame skip, this value is the number of frames
      # to between the fixed and moving frame during analysis.  In the case of
      # a dynamic frame skip, i.e. doDynamicFrameSkip = true, the following
      # value is the maximum number of frames to skip.
      frameSkip:          6
      # Use a dynamic frame skip.  See also 'frameSkip'.  If this value is set
      # to true, the frame skip is varied throughout the sequence by using the
      # strain between the fixed and moving image.
      doDynamicFrameSkip: true
      # In a dynamic frame skip analysis, the maximum absolute strain *in the axial direction* that should be observed in
      # a frame skip for best quality.  This value should be the maximum strain
      # that good motion tracking is expected.  The the observed maximum strain is
      # smaller than this value, then the frame skip is increased.
      maximumAbsFrameStrain: 0.05
      # In a dynamic frame skip analysis, the percentage of pixels that are
      # allowed over the the maximumABSFrameStrain before the frame skip is
      # decreased.
      percentFrameStrainOverMaximumStrain: 2.0
      # We crop the region for the above two strain characteristics to be examined
      # by the following fractional values on both the upper and lower bounds of
      # both directions.
      dynamicStrainCharacteristicsCrop: [ 0.1, 0.30 ]
      # Number of iterations when calculating the inverse displacement for
      # calculating incremental displacements from larger frame skips.
      inverseDeformationIterations: 15
  ...

.. highlights::

  |displacement_sequence_options_long|: Relevant sections from the algorithm configuration file
  for motion tracking used to analyze the plaques studied in this chapter.

~~~~~~~~~~~~~~~~~
Strain estimation
~~~~~~~~~~~~~~~~~

Eulerian incremental frame-to-frame strains at the final level are estimated
using the modified least squares estimator described in Section 5.2.3.  Prior to
strain estimation, the displacements are filtered with a small 3×3 median filter
to remove outliers.  Parameters of the strain sequence estimation are shown in
the configuration file, |strain_sequence_options|.  Note that the output file
names contain a reference to the input data they were derived from, a version
stamp, and a description of their content.  The version stamp is from a source
code versioning system (VCS), and it is a unique identifier that can be used to
obtain the state of the source code when the given results were produced.  The
input data identifier, source code version, and algorithmic parameters in the
configuration file constitute full provenance of the analysis, which ensures
repeatability and reproducibility.

::

  # strain-sequence options input file.
  ---
  # The file path prefix.  The input is assumed to be
  #   <filePrefix>_Version_<version_stamp>_DisplacementVectorSequence.mha
  # or
  #   <filePrefix>_Version_<version_stamp>_TrackedMovingFrame*DisplacementVectors.mha
  # The output will be
  #   <filePrefix>_Version_<version_stamp>_StrainTensorSequence.mha
  #   <filePrefix>_Version_<version_stamp>_OrderedPrincipalStrainSequence.mha
  #   <filePrefix>_Version_<version_stamp>_EstimatedStrainTensorSequence.mha
  #   <filePrefix>_Version_<version_stamp>_EstimatedOrderedPrincipalStrainSequence.mha
  # or
  #   <filePrefix>_Version_<version_stamp>_TrackedMovingFrame*StrainTensors.mha
  #   <filePrefix>_Version_<version_stamp>_TrackedMovingFrame*OrderedPricipalStrains.mha
  #   <filePrefix>_Version_<version_stamp>_TrackedMovingFrame*EstimatedStrainTensors.mha
  #   <filePrefix>_Version_<version_stamp>_TrackedMovingFrame*EstimatedOrderedPrincipalStrains.mha
  filePrefix: @FILE_PREFIX@
  # The method used to calcuate the gradient.  Valid values are "GRADIENT" for a
  # numerical gradient calculation or "BSPLINE" for a B-spline approximation
  # gradient. "LEASTSQUARES" for modified linear least squares.
  method: LEASTSQUARES
  # The ratio of B-spline control points to displacement points.  One value for
  # each direction.  This parameter is only relevant when method = BSPLINE.
  bSplineControlPointRatio: [1.2, 1.1]
  # The radius for performing median filtering on the displacement components.
  # Each value with the isotropic radius for the corresponding radius component.
  # A value of 0 indicates no median filtering will be applied.
  displacementMedianFilterRadius: [1, 1]
  # The radius for calculating the linear least squares line fit when calculating
  # the displacement gradients.  This parameter is only relevant when method =
  # LEASTSQUARES.
  leastSquaresStrainRadius: [3, 3]
  ...

.. highlights::

  |strain_sequence_options_long|: Configuration file showing the parameters used
  to calculate incremental strain tensor images from the sequence if incremental
  tracked displacements.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Calculation of derived quantities
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The final purpose of non-invasive *in vivo* characterization of carotid plaque
deformation is to generate a quantity that indicates vulnerability to failure,
thrombogenesis, and ultimately ischemic burden.  A number of quantities are
derived from the strain tensor over the cardiac cycle as potential indicators of
vulnerability.  First, ROIs that segment the plaque are created by a
radiologist.  These ROIs are drawn in a B-Mode image generated from the same RF
data used to perform motion tracking.  B-Modes and color flow images taken with
clinical imaging features of the scanning system at the time of acquisition are
also available to the radiologist to help distingush atherosclerotic plaque from
the lumen and surrounding tissues.  Three end-diastolic frames in a dataset are
segemented, which delineates two complete cardiac cycles.  Contiguous regions are segmented in the
image at end-diastole.   Often
there will be two components corresponding to an anterior and posterior
component.  However, a highly stenotic plaque may be segmented as a single
connected component.  Also, due to acoustic shadowing, a plaque may be subdivided into
more than two connected components where signal has a reasonable amplitude.

A binary connected component image is transformed into a mesh.  Strains tensors
and displacement vectors are accumulated on particles in the mesh as described
in Section 5.4.2.  Eigenanalysis is performed on the accumulated strain tensors
to calculate the principal strains, Section 5.3.1.  The principal strains are
used to evaluate the strain metrics described in Section 5.3.3: maximum
principal strain, maximum shear strain, total strain energy, and distortional
energy.

Plots of the strain components and strain metrics for subject 157 are shown in
|strain_plots|.  Twenty randomly selected particles in a plaque ROI are selected
and theirs accumulated strain values plotted again time.  Possibly due to
movement in and out of the imaging plane or motion tracking errors, a drift in
the accumulated strain is often observed [Shi2007]_.  If there is out-of-plane
motion, a particle is neither accumulating over the same volume of tissue.  To
compensate for this, the offset at the end of the cycle is linearly removed from
every curve.  All quantities should start from zero and return to zero if the
system is steady-state.  While is true in that the tissue obviously remains in
tact over the examination, some real drift may exist due to breathing, muscle
tone, etc.  Components of the strain tensor can have positive or negative
sign, but all strain metrics should be strictly positive.

.. image:: images/strain_plots.png
  :align: center
  :width: 16cm
  :height: 13.9cm
.. highlights::

  |strain_plots_long|: Strain components and strain metrics for data collected
  on the left side of subject 157.  Curves are shown for twenty randomly
  selected particles in the ROI.  a) Maximum principal strain, b) maximum shear
  strain, c) total strain energy, d) distortional energy, e) axial strain, f)
  lateral strain, and g) shear strain.

Over the cardiac, the three components of the strain tensor, the maximum
principal strain, maximum shear strain, total strain energy, and distortional
energy vary over time and over a contiguous region.  For each of these values,
three scalar statistics are calculated per cardiac cycle.  The mean peak-to-peak
value reflects the average strain in a region.  Since material failure is likely
to occur at a location of high strain, the 90\ :sup:`th` percentile of the
peak-to-peak value is also calculated.  A 90\ :sup:`th` percentile is used
instead of the absolute maximum because outliers sometimes arise from part of
the ROI crossing into the lumen or movement out-of-plane.  Third, the standard
deviation of the particle peak-to-peak value is found.  This is because strain
heterogenaity may mark the presence of highly varying strains beyond the
resolution of the system.  These three values are found for all strain metrics
and strain components, but also for the magnitude of the time-derivative of all
strain metrics and strain components.  The time-derivative is considered because
it is hypothesized that viscoelastic behavior may also contribute to the
fatigue failure process.  Strain values for five subjects are tabulated in
Appendix B.

~~~~~~~~~~~~~~~~~~~~~~
*In vivo* case studies
~~~~~~~~~~~~~~~~~~~~~~

In this section, six *in vivo* plaque case studies are examined that demonstrate
different behaviors.  These results suggest that strain imaging may measure the end
effect of many factors that influence plaque vulnerability: composition
(|hypoechoic|), morphology, (|geometry|), hemodynamics (|turbulence|), and
angiogenesis (|wallshear|).  Limitations due to shadowing, |shadowing|, and
out-of-plane motion, |out_of_plane|, are also illustrated.

Hypoechoic plaque with high strain
==================================

.. image:: images/pat154rightbulblongcont_20091019090048_Cycle1_Version_963d653_hypoechoic.png
  :align: center
  :width: 14cm
  :height: 17.0cm
.. highlights::

  |hypoechoic_long|: Hypoechoic plaque, often classified as 'soft' plaque, that
  exhibits high strain throughout the plaque.  a) Accumulated displacement
  vectors (movement is primarily in superior direction), b) strain tensor
  ellipses, c) maximum absolute principal strain, d) maximum shear strain, e)
  total strain energy, and f) distortional energy.

As discussed in Section 2.3.1, hypo-echoic B-Mode presentation is associated
with lipid or hemorrhagic plaque content.  It has traditionally been
hypothesized that soft plaques may be a sign of vulnerability.  In |hypoechoic|,
a hypoechoic plaque from the right side of Subject 154 is shown to have high strains throughout the plaque.  Strain
in the posterior plaque segment (found at deeper in the image), is higher than
the anterior plaque segment.  This pattern is common, and could be related to
material properties of the tissue surrounding the anterior
segment compared to the material properties surrounding the posterior segment,
or it could be related to the compression supplied by the transducer
[Maurice2008a]_.  The mean peak-to-peak maximum absolute principal strain is
0.23 and the 90\ :sup:`th` percentile is 0.41 in the posterior segment (Table B.1).
There is little difference in the distribution of the strain metrics in this
case with the possible exception of the total strain energy, which is more
reserved in the anterior segment.  Displacements illustrated in |hypoechoic|\ a)
are large and predominantly lateral, which underscores the need for good lateral
tracking.

Importance of geometry
======================

.. image:: images/pat157lefticalongcont_20100111092227_Cycle1_Version_963d653_geometry.png
  :align: center
  :width: 14cm
  :height: 17.23cm
.. highlights::

  |geometry_long|: Strain pattern in an echogenically homogeneous plaque that
  varies depending on the geometry of the plaque and its position relative to
  blood flow. a) Displacement vectors, b) strain tensor ellipses, c) maximum
  absolute principal strain, d) maximum shear strain, e) total strain energy,
  and f) distortional energy.

As discussed in Section 2.2 and 2.3, the dominant focus of various imaging and other
diagostic techniques is on identification of plaque composition.  While
composition may be an important factor in plaque vulnerability, it is not the
only factor.  In |geometry|, a plaque with a relatively homogeneous B-Mode
echogenicity is shown, which implies that its composition may be homogeneous.
However, when mechanical loading is applied via the pulse pressure, a
hetergeneous strain distribution results.  Strain in highest in the center of
the larger anterior plaque region and fallos off towards it edges.  The area of
the posterior plaque segment that protrudes into the lumen experiences much
higher strain than other areas.

Subtle but significant differences in the strain metrics shown in |geometry|\
c)-f) are apparent.  The squared terms in the total strain energy and
distortional energy accentuate the locations of highest strain compared to the
maximum absolute principal strain and the maximum shear strain.  These images
are from the left side of Subject 157.

Strain with turbulent flow
==========================

.. image:: images/153.US.CV.1.13.2009.10.07.13.14.20.15625.23705888_turbulence.png
  :align: center
  :width: 14cm
  :height: 17.3cm
.. highlights::

  |turbulence_long|: High strain adjacent to turbulent flow that follows a
  narrow inlet in the ICA.  a) Color flow from the scanner interface, b) strain
  tensor ellipses, c) maximum absolute principal strain, d) maximum shear strain, e)
  total strain energy, and f) distortional energy.

|geometry| emphasizes that geometry is a factor in plaque vulnerability, and
strain imaging captures that factor.  |turbulence| suggests that hemodynamics
are also a factor in vulnerability.  Aliasing in the color flow image,
|turbulence|\ a), can be attributed to the turbulent flow that occurs as the
blood squeezes through the small patency in the plaque at the base of the
internal carotid artery (ICA).  High strain is seen in the plaque immediately
adjacent to this location of turbulent flow.

Strain at the plaque-adventitia interface
=========================================

.. image:: images/pat156lefticalongcont_20100113095826_Cycle0_Version_963d653_wallshear.png
  :align: center
  :width: 14cm
  :height: 17.2cm
.. highlights::

  |wallshear_long|: High strain near the interface of the plaque with the
  surrounding tissue that occurs with lateral motion of the plaque.  a) strain
  tensor ellipses, b) maximum absolute principal strain, c) maximum shear
  strain, d) axial strain, e) shear strain, f) and lateral strain.

Recall that angiogenesis has also been proposed as a possible factor leading to
plaque vulnerability [McCarthy1999,Lusby1982,Hiyama2010,Vicenzini2007]_.  As
plaques become larger, the vasa vasorum that provided blood to the artery wall
can grow to feed the enlarged tissue.  This fissues are expected to cause
instability associated with the adventitia-plaque boundary where the angiogenesis
originates.  |wallshear| shows high strains at this location occuring during
lateral motion of the plaque that may be associated with this phenomena.  These
images are from the left side of Subject 156.

Examining the strain tensor ellipses or the strain metric images, we easily
locate the areas of high strain.  A single component of the strain tensor does
not always provide sufficient information.  In this case, for example, the high
strain is not apparent in the axial or lateral strain images.  Note that the
ellipses are orientated at an angle of 3π/4 because of the orientation and
deformation of the plaque.  This off-axis orientation explains why the strain is
best reflected in the shear strain component in this case.  If the plaque was
orientated in a more horizonal direction relative to the transducer, the strain
would then arise in the lateral component.

Again, not that the area of the anterior plaque that protrudes into the lumen is
subject to high strains.

Calcific plaque with shadowing
==============================

.. image:: images/pat158leftbulblongcont_20100315132656_Cycle1_Version_963d653_shadowing.png
  :align: center
  :width: 15cm
  :height: 17.8cm
.. highlights::

  |shadowing_long|: Low strain in a calcific plaque, but high strain in other
  areas.  a) Displacement vectors, b) strain tensor ellipses, c) maximum
  absolute principal strain, d) maximum shear strain, e) total strain energy,
  and f) distortional energy.

It is well know that calcific plaques are associated with high acoustic
attenuation and that they are extremely hard.  The high attenuation explains the
acoustic shadowing on these images of the left side of Subject 158.  As the
displacement vectors indicate in |shadowing|\ a), this plaque undergoes a
torsional motion when subject to the pressure pulse.  Very little strain occurs
in the highly calcified region that causes the shadowing.  In other areas of the
the plaque that appear to have heterogenous calcification, very high strains
occur.  Examination of the strain time series suggest that this may result from a
combination of heterogenous calcification, morphology, and hemodynamics.

This case also illustrates a limitation of non-invasive externally applied
ultrasound imaging.  Motion tracking cannot be performed when calcific plaques
attenuate the ultrasound beam to undetectable levels.  Furthermore, the 2D
imaging method can only capture a small subset of the imaging planes available.
For a heterogenous structure like carotid plaques, a critical region may be
overlooked.  Additionally, not all components of the 3D strain tensor are
captured.  Strain imaging in the transverse plaque is made more difficult by the
motion pattern that occurs in this direction and refraction of the beam by the
artery wall [Hansen2009a,Hansen2010a]_.

Artifact from out-of-plane motion
=================================

.. image:: images/pat153lefticalongcont_20091007094020_Cycle0_Version_963d653_out_of_plane.png
  :align: center
  :width: 14cm
  :height: 17.1cm
.. highlights::

  |out_of_plane_long|: High accumulated strain artifacts attributable to
  out-of-plane motion. a) Displacement vectors, b) strain tensor ellipses, c) maximum
  absolute principal strain, d) maximum shear strain, e) total strain energy,
  and f) distortional energy.

Finally, a case where artifactually high strains occur with data from the left
side of Subject 153 is displayed in |out_of_plane|.  At the edge of ROIs such as
this on, the vessel is twisting away from the plane of the transducer.  This has
multiple negative effects.  Out-of-plane motion is increased, which causes
tracking image decorrelation and increases strain image noise.  Out-of-plane
motion also means a particle does not track the same volume of tissue over time.
Furthermore, orientation of the principal axes of the strains accumulated may
change over the cardiac cycle, which will not result in the correct
accumulation.


~~~~~~~~~~
References
~~~~~~~~~~

