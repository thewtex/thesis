====================================
Calculating Strain from Displacement
====================================

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

.. |points| replace:: Fig. 1

.. |points_long| replace:: **Figure 1**

.. |segments| replace:: Fig. 2

.. |segments_long| replace:: **Figure 2**

.. |two_segments| replace:: Fig. 3

.. |two_segments_long| replace:: **Figure 3**

~~~~~~~~~~~~~~~~~
The strain tensor
~~~~~~~~~~~~~~~~~

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

  If :math:`\mathbf{F} \equiv I + \nabla \mathbf{u}`, then

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

Mechanical model
================

Infinitesimal strain
--------------------

Lagrangian strain
-----------------

Eulerian strain
---------------

Application in ultrasound
=========================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Methods for estimating strain from displacement
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Finite difference based methods
===============================

The least squares strain estimator
==================================

B-spline fitting
================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Useful quantities derived from the strain tensor
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Principal strains
=================

Representation of the 2D strain tensor as an ellipse
====================================================

Combination of normal strains and shear strain into a single strain index
=========================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Generating acculated strain from a time series
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
