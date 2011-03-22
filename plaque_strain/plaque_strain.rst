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

~~~~~~~~~~
References
~~~~~~~~~~

