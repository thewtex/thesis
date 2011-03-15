===============================================
Chapter 5: Calculating Strain from Displacement
===============================================

In this chapter, theory and techniques necessary to create strain tensor images
from displacement images are covered with attention paid towards issues relevant
to strain imaging of the carotid artery with external ultrasound.  First, how
the definition of the strain tensor arises in continuum mechanics and the
physical explanation that follows is reviewed.  The nomenclature as it is
applies to diagnostic ultrasound strain imaging is covered.  Next, a number of
methods to estimate the displacement gradient, which is needed to calculate the
strain tensor, are presented.  Once the strain tensor has been estimated,
permutations can be computed that ease interpretation and derived scalar quantities
that be used for statistical analysis of plaque vulnerability.  Finally, methods
to calculate accumulated strain in digital ultrasound strain images over the
cardiac cycle are explained.

.. |points| replace:: Fig. 5.1

.. |points_long| replace:: **Figure 5.1**

.. |segments| replace:: Fig. 5.2

.. |segments_long| replace:: **Figure 5.2**

.. |two_segments| replace:: Fig. 5.3

.. |two_segments_long| replace:: **Figure 5.3**

.. |ds_normal_dia| replace:: Fig. 5.4

.. |ds_normal_dia_long| replace:: **Figure 5.4**

.. |ds_perpendicular_dia| replace:: Fig. 5.5

.. |ds_perpendicular_dia_long| replace:: **Figure 5.5**

.. |ds_normal_eulerian_dia| replace:: Fig. 5.6

.. |ds_normal_eulerian_dia_long| replace:: **Figure 5.6**

.. |linear_array| replace:: Fig. 5.7

.. |linear_array_long| replace:: **Figure 5.7**

.. |input_known_displacements| replace:: Fig. 5.8

.. |input_known_displacements_long| replace:: **Figure 5.8**

~~~~~~~~~~~~~~~~~~~~~
5.1 The strain tensor
~~~~~~~~~~~~~~~~~~~~~

5.1.1 Mechanical model
======================

An *in situ* plaque prior to failure is a continuous, solid-body at a gross
level, and solid-body continuum mechanics can be applied.  Solid-body continuum
mechanics treats a body as a collection of infinitesimal volumes of material.
We are concerned with the motion of this collection of infinitesimal volumes
over time.  This may be rigid body motion, translation and rotation, or
deformation of the body.

.. image:: images/points.png
  :align: center
  :width: 11cm
  :height: 7.964cm
.. highlights::

  |points_long|: 2D solid body at reference time *t*\ :sub:`0`, and after motion
  at time *t*.  The vector **X** defines the position of point P(t\ :sub:`0`\ )
  in the reference configuration, and the vector **x** defines the point's
  position after motion.  The vector **u** is the difference between the two
  vectors and the displacement of P.

Consider a point, P, within a body at the time t\ :sub:`0` whose location is
defined by the vector **X**.  Motion occurs and P(t) is now located at **x**.
That is, :math:`\mathbf{x} = \mathbf{x}( \mathbf{X}, t )` and
:math:`\mathbf{x} ( \mathbf{X}, t_0 ) = \mathbf{X} )`.  Here **X** defines the
reference configuration.  We will consider the location of P after motion occurs
to be the reference location plus a displacement, **u**, i.e.

.. math:: \mathbf{x} = \mathbf{X} + \mathbf{u}( \mathbf{X}, t )

.. image:: images/segments.png
  :align: center
  :width: 11cm
  :height: 7.965cm
.. highlights::

  |segments_long|:  A different length segment extending from point P to point Q
  in the reference configuration, d\ **X**, and after deformation, d\ **x**.

Let us examine the motion of infinitesimally small line segments within the
body.  The line segment at **X**, d\ **X**, at time *t* becomes d\ **x**.  This
is illustrated in |segments|.  The nearby point Q is located in the post- and
pre-deformation states at

.. math:: \mathbf{x} + d\mathbf{x} = \mathbf{X} + d\mathbf{X} + \mathbf{u}( \mathbf{X} + d\mathbf{X}, t )

.. epigraph::

  It is clear from |segments| that

.. math:: d\mathbf{x} = d\mathbf{X} + \mathbf{u}( \mathbf{X} + d\mathbf{X}, t) - \mathbf{u}( \mathbf{X}, t)

.. epigraph::

  This can be expressed with the second-order tensor called the displacement
  gradient [Lai1993]_, :math:`\nabla \mathbf{u}`.  In 2D Cartesian coordinates,

  In 2D Cartesian coordinates,

.. math:: \nabla \mathbf{u} = \begin{bmatrix} \dfrac{\partial u_1}{\partial X_1} & \dfrac{\partial u_1}{\partial X_2} \\ \dfrac{\partial u_2}{\partial X_1} & \dfrac{\partial u_2}{\partial X_2} \end{bmatrix}

.. epigraph::

  If **F**, the *deformation gradient* [Lai1993]_ is defined by :math:`\mathbf{F} \equiv I + \nabla \mathbf{u}`, then

.. math:: d \mathbf{x} = d \mathbf{X} + \nabla \mathbf{u} \, d \mathbf{X} = \mathbf{F} d \mathbf{X}

Strain, which quantifies the distortion that occurs in a material, is defined
when investigating the expression for the inner product between two differential
segments before and after deformation.  When we compare the two segments
:math:`d \mathbf{x}^{(1)}` and :math:`d \mathbf{x}^{(2)}`

.. image:: images/two_segments.png
  :align: center
  :width: 6cm
  :height: 1.09cm

.. image:: images/two_segments_dia.png
  :align: center
  :width: 11cm
  :height: 7.97cm
.. highlights::

  |two_segments_long|: Two differential segments in the reference configuration,
  :math:`d \mathbf{x}^{(1)}` and :math:`d \mathbf{x}^{(2)}`,
  and after motion occurs. :math:`d \mathbf{X}^{(1)}` and :math:`d \mathbf{X}^{(2)}`

Observe that

.. image:: images/two_segments2.png
  :align: center
  :width: 6cm
  :height: 1.0cm

.. epigraph::

  It is from this model that the different expressions for the strain tensor
  arise.

5.1.1.1 Infinitesimal strain
----------------------------

If we have very small deformations, :math:`(\nabla \mathbf{u})^T \nabla \mathbf{u}`
becomes negligible, and

.. math:: \mathbf{F}^T \mathbf{F} \approx \mathbf{I} + \nabla \mathbf{u} + (\nabla \mathbf{u})^T \equiv \mathbf{I} + 2 \mathbf{E}

.. epigraph::

  where

.. math:: \mathbf{E} = \frac{1}{2} ( (\nabla \mathbf{u} )^T + \nabla \mathbf{u})

Note that **E** is a second-rank tensor since :math:`\nabla \mathbf{u}` is a
second-rank tensor, and it is symmetric because we have the transpose added to
itself.  The tensor **E** is the *infinitesimal strain* [Lai1993]_, also known as
*engineering strain* or *small strain*.  We then have

.. math:: d \mathbf{x}^{(1)} \cdot d \mathbf{x}^{(2)} = d \mathbf{X}^{(1)} \cdot d \mathbf{X}^{(2)} + 2 d \mathbf{X}^{(1)} \cdot \mathbf{E} d \mathbf{X}^{(2)}

.. epigraph::

  Therefore, the change in the inner product is an additive term with
  transformation of the original vectors being performed by the strain tensor.

For Cartesian coordinates in Einstein notation,

.. math:: E_{ij} = \frac{1}{2} ( \frac{\partial u_i}{\partial X_j} + \frac{\partial u_j}{\partial X_i} )

.. epigraph::

  and in 2D the infinitesimal strain tensor is explicitly defined as,

.. math:: \mathbf{E} = \begin{bmatrix} \dfrac{\partial u_1}{\partial X_1} & \dfrac{1}{2}( \dfrac{\partial u_1}{\partial X_2} + \dfrac{\partial u_2}{\partial X_1}) \\ \dfrac{1}{2}( \dfrac{\partial u_1}{\partial X_2} + \dfrac{\partial u_2}{\partial X_1}) & \dfrac{\partial u_2}{\partial X_2} \end{bmatrix}

We can elucidate the physical meaning of the infinitesimal strain tensor by
examining special cases for :math:`d \mathbf{X}^{(1)}` and :math:`d
\mathbf{X}^{(2)}`.  First, let us consider when :math:`d \mathbf{X}^{(1)} = d
\mathbf{X}^{(2)} = dS \, \mathbf{e_1}` where :math:`\mathbf{e_1}` is the unit
basis in direction 1 and *dS* is the length of :math:`d \mathbf{X}`, and *ds* is
the deformed length of :math:`d \mathbf{x}^{(1)} = d \mathbf{x}^{(2)}`.

.. image:: images/ds_normal.png
  :align: center
  :width: 8cm
  :height: 1.698cm

.. image:: images/ds_normal_dia.png
  :align: center
  :width: 11cm
  :height: 7.967cm
.. highlights::

  |ds_normal_dia_long|: Two line segments, :math:`d \mathbf{X}^{(1)} = d
  \mathbf{X}^{(2)} = dS \, \mathbf{e_1}` get transformed to a segement of length
  *ds* after deformation.

For small deformations, :math:`(ds + dS)( ds - dS) \approx 2 dS( ds - dS )`, and

.. math:: \frac{ ds - dS }{dS} = \mathbf{e_1} \cdot \mathbf{E} \mathbf{e_1} = E_{11}

Therefore, :math:`E_{11}` is equal to the unit elongation (or shortening) for the segment
in the direction of :math:`\mathbf{e_1}`.  Similarily, :math:`E_{22}` is the
unit elongation for the segment that is in the direction of
:math:`\mathbf{e_2}`.  These diagonal elements of **E** constitute the
*normal strains* [Lai1993]_.  Note that

.. math:: 100 \, \frac{ds - dS}{dS} \equiv \% \mbox{ elongation of } dS

Therefore, in the small strain case, a normal strain component multiplied by 100 is equal to
the percent elongation.  A positive normal strain indicates an extension of
*dS*, and a negative normal strain indicates a shortening of *dS*.

Secondly, instead of examining parallel segments centered at **X**, let us
investigate perpendicular segments.

.. image:: images/ds_perpendicular_dia.png
  :align: center
  :width: 11cm
  :height: 7.97cm
.. highlights::

  |ds_perpendicular_dia_long|:  Relative change that occurs that are orthogonal
  in the reference configuration.

Let :math:`d \mathbf{X}^{(1)} = dS_1 \, \mathbf{e_2}` and :math:`d
\mathbf{X}^{(2)} = dS_2 \, \mathbf{e_2}`, :math:`\Vert d \mathbf{x}^{(1)} \Vert = ds_1`,
:math:`\Vert d \mathbf{x}^{(2)} \Vert = ds_2`, and the angle between
:math:`\mathbf{x}^{(1)}` and :math:`\mathbf{x}^{(2)}` is :math:`\theta`.

.. image:: images/ds_perpendicular.png
  :align: center
  :width: 6cm
  :height: 1.424cm

.. epigraph::

  If we define :math:`\theta = \pi / 2 - \gamma`, then :math:`\gamma` is the
  change in argle that occurs between :math:`\mathbf{x}^{(1)}` and :math:`\mathbf{x}^{(2)}`.

.. math:: \sin \gamma = \cos( \pi / 2 - \gamma )

.. epigraph::

  For small strain

.. math:: \sin \gamma \approx \gamma, \; \frac{dS_1}{ds_1} \approx 1, \; \frac{dS_2}{ds_2} \approx 1

.. math:: \gamma = 2 \, E_{12} = 2 \, E_{21}

That is, for infinitesimal strain, the decrease in angle between orthogonal
segments is equal to twice the diagonal component of the strain tensor, the
*shear strain* [Lai1993]_.

5.1.1.2 Lagrangian strain
-------------------------

Beginning again without the intention to presume there are very small
deformations, we start at |two_segments| and subtract
:math:`d \mathbf{X}^{(1)} \cdot d \mathbf{X}^{(2)}` from both sides of the
equation,

.. image:: images/lagrangian.png
  :align: center
  :width: 11cm
  :height: 1.634cm

.. epigraph::

  where :math:`\mathbf{E}^* = \frac{1}{2} ( \mathbf{F}^T \mathbf{F} - \mathbf{I})`
  is the *Green-Lagrangian strain tensor* [Lai1993,Haupt2002]_.  This is a
  finite strain tensor that specifies strain in terms of the reference
  configuration.

Again examininig the situation in |ds_normal_dia|, where
:math:`d \mathbf{X}^{(1)} = d \mathbf{X}^{(2)} = d \mathbf{X} = dS \mathbf{e}_1`
and :math:`||d\mathbf{x}|| = ds`,

.. math:: ds^2 - dS^2 = 2 dS \mathbf{e}_1 \cdot \mathbf{E}^* dS \mathbf{e}_1

.. math:: E_{11}^* = \frac{ ds^2 - dS^2}{2 dS^2}

Similarily, if :math:`d \mathbf{X} = ds \mathbf{e}_2`,

.. math:: E_{22}^* = \frac{ds^2 - dS^2}{2 dS^2}

And, if we again look at |ds_perpendicular_dia|, where
:math:`d \mathbf{X}^{(1)} = ds_1 \mathbf{e}_1` and :math:`d \mathbf{X}^{(2)} =
dS_2 \mathbf{e_2}` deform to :math:`d \mathbf{x}^{(1)} = ds_1 \mathbf{m}` and
:math:`d \mathbf{x}^{(2)} = ds_2 \mathbf{n}` where **m** and **n** are unit
vectors,

.. math:: ds_1 ds_2 \mathbf{m} \cdot \mathbf{n} = 2 dS_1 dS_2 \mathbf{e}_1 \cdot \mathbf{E}^* \mathbf{e}_2

.. math:: E_{12}^* = \frac{ds_1 ds_2}{2 dS_1 dS_2} \cos( \mathbf{m}, \mathbf{n})

The expression of :math:`\mathbf{E}^*` in terms of the displacement gradient is

.. math:: \mathbf{E}^* = \frac{1}{2}( \nabla \mathbf{u} + (\nabla \mathbf{u})^T + (\nabla \mathbf{u})^T \nabla \mathbf{u} )

In Einstein summation notation,

.. math:: E_{ij}^* = \frac{1}{2}(\frac{\partial u_i}{\partial X_i} + \frac{\partial u_j}{\partial X_i} + \frac{1}{2} \frac{\partial u_m}{\partial X_i} \frac{\partial u_m}{\partial X_j}

The explicit components in a 2D Cartesian coordinate system are,

.. image:: images/lagrangian_explicit.png
  :align: center
  :width: 9.5cm
  :height: 3.07cm

5.1.1.3 Eulerian strain
-----------------------

Instead of specifying motion in terms of the reference configuration, it can be
specified in the deformed configuration,

.. math:: d \mathbf{X} = \mathbf{F}^{-1} d \mathbf{x}

where :math:`\mathbf{F}^{-1}` is the inverse of :math:`\mathbf{F}` [Lai1993]_,

.. math:: \mathbf{F} = \begin{bmatrix} \dfrac{\partial X_1}{\partial x_1} & \dfrac{\partial X_1}{\partial x_2} \\ \dfrac{\partial X_2}{\partial x_1} & \dfrac{\partial X_2}{\partial x_2} \end{bmatrix}

Again considering the deformation of two small segments in the volume,

.. image:: images/eulerian1.png
  :align: center
  :width: 7cm
  :height: 1.74cm

Subtracting the above from :math:`d \mathbf{x}^{(1)} \cdot d \mathbf{x}^{(2)}`
to again obtain an expression for the change in the inner product between the
two segments,

.. image:: images/eulerian2.png
  :align: center
  :width: 11cm
  :height: 1.62cm

where :math:`\mathbf{e}^* = \frac{1}{2} (\mathbf{I} - (\mathbf{FF}^T)^{-1})` is
the *Eulerian-Almansi strain tensor* [Lai1993,Haupt2002]_. This is a finite
strain tensor that specifies strain in terms of the deformed configurations.

.. image:: images/ds_normal_eulerian_dia.png
  :align:  center
  :width:  11cm
  :height: 7.97cm
.. highlights::

  |ds_normal_eulerian_dia_long|:  Two identical line segments, this time in the
  deformed configuration, were transformed from a segment of length *dS*.

As shown in |ds_normal_eulerian_dia|, if
:math:`d \mathbf{x}^{(1)} = d\mathbf{x}^{(2)} = d \mathbf{x} = ds \mathbf{e}_1`
and :math:`||d \mathbf{x}|| = dS`, then

.. math:: ds^2 - dS^2 = 2 dS \mathbf{e}_1 \mathbf{e}^* dS \mathbf{e}_1

.. math:: e_{11}^* = \frac{ds^2 - dS^2}{2 dS^2}

And, when considering two segments :math:`d\mathbf{x}^{(1)} = ds_1 \mathbf{e}_1`
and :math:`d\mathbf{x}^{(2)} = ds_2 \mathbf{e}_2` that deformed from
:math:`d\mathbf{X}^{(1)} = dS_1 \mathbf{n}` and
:math:`d \mathbf{X}^{(2)} = dS_2 \mathbf{m}` where **n** and **m** are unit
vectors,

.. math:: - dS_1 dS_2 \, \mathbf{n} \cdot \mathbf{m} = 2 \, ds_1 ds_2 \, \mathbf{e}_1 \cdot \mathbf{e}^* \mathbf{e}_2

.. math:: e_{12}^* = \frac{ -dS_1 dS_2 \cos( \mathbf{n}, \mathbf{m} )}{2 ds_1 ds_2}

Since :math:`\mathbf{F}^{-1} = \mathbf{I} - \nabla_x \mathbf{u}` [Lai1993]_
(:math:`\nabla_x` indicates differentiation with respect to coordinates of the
deformed configuration),

.. image:: images/inverse_deformation_gradient.png
  :align: center
  :width: 9cm
  :height: 1.23cm

and

.. math:: \mathbf{e}^* = \frac{1}{2}( \nabla_x \mathbf{u} + (\nabla_x \mathbf{u})^T - (\nabla_x \mathbf{u})^T \nabla_x \mathbf{u}

In Einstein summation notation,

.. math:: e_{ij}^* = \frac{1}{2}(\frac{\partial u_i}{\partial x_i} + \frac{\partial u_j}{\partial x_i} - \frac{1}{2} \frac{\partial u_m}{\partial x_i} \frac{\partial u_m}{\partial x_j}

Explicitly in 2D Cartesian coordinates,

.. image:: images/eulerian_explicit.png
  :align:  center
  :width:  9.5cm
  :height: 3.3cm


5.1.2 Application in ultrasound
===============================

By applying various medical imaging modalities, strain images of tissues can be
created by performing deformable image registration of the tissue image after
deformation to another pre-deformation image.  This technique has been applied
in multiple imaging modalities.  Strain in atherosclerotic tissues was imaged by
Rogowska et al. [Rogowska2004,Rogowska2006]_ with optical coherence tomography
and well as by others [Stamper2006,Chan2004]_.  Recently, the high resolutions
of X-ray computed tomography (CT) were used to create high quality strain images
of a breast phantom [Han2010]_.  Creation of displacement images in magnetic
resonance imaging (MRI) is unique in that does not need to use traditional image
registration techniques, but pulse sequences can generate displacement
images using the physics of image acquisition [Fowlkes1995,Bishop1995,Hardy1995,Plewes2000,Lin2008,Korosoglou2008,Neizel2009,Shehata2010]_.

Diagostic ultrasound has the longest history of calculating strain
[Ophir2001,Ophir2000,Parker1996,Parker2011]_.  In one of the earliest papers,
Ophir et. al. calculated strain with [Ophir1991]_

.. math:: s_i = \frac{t_{i+1} - t_i}{2dz/c}

.. epigraph::

  where the *s*\ :sub:`i` is the strain, *t*\ :sub:`i+1` and *t*\ :sub:`i` are
  the time shifts of windows on an A-line, *dz* is the distance between the
  windows, and *c* is the speed of sound in tissue.  As shown in |linear_array|,
  an A-line, an amplitude line of the signal created by sending a beam of
  ultrasound into a tissue.  If the speed of sound in tissue is constant, this
  dimensionless quantity is equivalent to one component of the infinitesimal
  strain tensor described in Section 5.1.1.1.  Since this component of strain is
  along the beam axis, it is called *axial strain*.  In an a linear array where
  all A-lines are sent parallel directions, |linear_array|, the axial refers to
  the same direction across the entire image.  Note that for sector arrays, this
  may not be the case.  In the usual operation and clinical presentation of
  linear array data, the axial direction is the vertical direction in an image.
  If the beam steering occurs, the beams will remain parallel, but the axial
  direction no longer corresponds to the vertical direction of the image.  

.. image:: images/linear_array.png
  :align:  center
  :width:  11cm
  :height: 8.89cm
.. highlights::

  |linear_array_long|: Diagram of a medical linear ultrasound array.  Small
  transducer elements on the surface of the handheld transducer send sound
  concentrated over a beam in the tissue, which creates a line in the image.
  The axis of this beam determines the *axial direction* of the strain tensor,
  and the direction orthogonal is the *lateral direction*.

In conventional ultrasound imaging, a B-Mode image is formed by repeatedly
changing the location the A-line is sent into the tissue.  In a linear array,
the spacing of the A-lines is determined by the transducer element spatial
density.  This direction which is orthogonal to the axial direction is the
*lateral direction*.  In the carotid images shown in this work, the lateral
direction corresponds to the horizontal direction.  Resolution in this direction
is not directly determined by the excitation frequency as it is in the axial
direction, but by the beam width.  As a consequence, resolution in this
direction is much lower [Hansen2010]_.  Also, shifts do not depend on sound
speed assumptions; they are statically determined by the geometry of the
transducer.  In an *in vivo* carotid image used in this study, for example, the
number of samples in a 40×40 mm image in the axial direction is 2076 in the
axial direction and 244 in the lateral direction.  This near ten-fold disparity
in the resolution is associated with the difficulty in calculating lateral
strains.  The majority of the literature has focused on axial strains because
the lateral strains do exhibit a useable signal-to-noise ratio.  Only recently
algorithmic improvements, regularization such as those described in Chapter 3 or
other improvements described in Chapters 4 and 9.

*Shear strain* in ultrasound strain imaging usually refers to the strain between
the axial and lateral directions.  Since displacement estimates in the axial direction
are higher quality than those in the lateral directions, some have only
calculated the derivative of displacement in the axial direction with respect to
the lateral direction and called this *axial shear* [Thitaikumar2008a]_.

Of course, while axial, lateral, and shear strain provide all components of a 2D
strain tensor, physical tissues are 3D.  The number of independent components in a
symmetric, second-rank tensor are

.. math:: n_c = D \frac{D+1}{2}

.. epigraph::

  There are six components in the 3D strain tensor; two addition shear strain
  components and one additional normal strain component.  While there is on-going
  research to obtain these components, there are a number of technological
  limitations at this time that prevent full population of the strain tensor with
  ultrasound.  The third direction of a linear array, the *elevational
  direction*, has a resolution at the level of or worse than the lateral
  resolution.  Technology to commercially develop a 2D matrix-array of transducer
  elements is only emerging.  Challenges here include creation of the 2D array
  elements and acquiring the appropriate signal channel count
  [Wygant2008,Martinez-Graullera2010]_.  In terms of motion tracking,
  computational challenges exist in terms of data storage and processing.  Also,
  frames rates are slower with volumetric imaging, which in some cases can allows
  to much motion to take place in-between image sets.  However, progress in 3D
  strain imaging is taking place [Byram2010,Po2010,Lopata2007,Rao2008,Fisher2010]_.
  Currently, the primary benefit of 3D imaging systems is not to obtain all components
  of the strain tensor, but to prevent tissue from moving outside of the imaging
  plane, which makes motion tracking difficult.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
5.2 Methods for estimating strain from displacement
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In Section 5.1.1, it was shown how strain tensors are composed of the symmetric part of
the displacement gradient.  Therefore, in order to compute the strain tensor,
the displacement gradient must first be estimated.  Accurate calculation of the
displacement gradient is a challenge for two reasons.  First, the output
block-matching methods is a discrete instead of continuous displacement field.
Secondly, displacement estimates are often noisy, and the differential operation
of gradient calculation magnifies the noise.  In this section, a number of
methods to compute the displacement gradient are examined.

A common test case for ultrasound strain imaging is the model of a hard
cylindrical inclusion (high elastic modulus) in a soft background (low elastic
modulus).  The inclusion exists in a cubic block, and is subject to uniform
compression from the top while being unconstrained at the side (zero-traction
stress boundary conditions).  Displacement is assumed to start from zero at the
top and center of the model as if an ultrasound transducer exists there as a
point of reference.  Details on methods to create the mechanical finite element
and ultrasound scattering pieces of a simulation that represents this model are
given in Chapter 3.  In this section, images resulting from 3% compression along
the axis of deformation in this model will be used to evaluate the behavior of
different methods to calculate the strain tensor from tracked displacement
vectors.

.. image:: images/input_known_displacements.png
  :align: center
  :width: 16cm
  :height: 4.91cm
.. highlights::

  |input_known_displacements_long|:  Ideal input displacements resulting from
  the mechanical model.  a) Axial displacements, b) lateral displacements, c)
  displacement the displacement vectors represented by arrows scaled by and
  colored by their magnitude.

The ideal, known displacements are shown in |input_known_displacements|.  Axial
displacements start from zero at the transducer surface and increase further
into the body.  Lateral displacements are assumed to be zero along the center
axis of the transducer and diverge to the edges of the body.

5.2.1 Finite difference based methods
=====================================

B-spline fitting
================

The least squares strain estimator
==================================


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Useful quantities derived from the strain tensor
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Principal strains
=================

Representation of the 2D strain tensor as an ellipse
====================================================

Combination of normal strains and shear strain into a single strain index
=========================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Generating accumulated strain from a time series
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Dynamic frame skip
==================

Eulerian approach to accumulated strain
=======================================

Since strain is a measure of the distortion of an object relative to a reference
strain, the *reference state* must be defined.  Experimentalists whom attempt to
measure the *in vitro* mechanical properties will sometimes try to find a
complete stress-free state of the artery and use this as the reference state.
When removed from the tethering provided by surrounding tissue, arteries will
shrink dramatically in size [Fung1993]_.  A *no-load* [Fung1993]_ condition
occurs when excised vessels are removed and blood pressure and longitudinal
tensile stresses are removed.  A *zero stress* [Fung1993]_ occurs when no
further strain occurs after cutting the tissue.  The residual stress that
defines the difference between the no-load and zero stress can be quantified
with the opening angle, the angle that results from cutting an artery
longitudinally [Fung1993]_.  When working with *in vivo* tissues,
it is difficult to infer the zero stress state, although Masson et al. obtained
reasonable results given a number of modeling assumptions for a healthy common
carotid artery [Masson2008]_.  For this reason, an end diastolic image state is
taken as the reference state.
