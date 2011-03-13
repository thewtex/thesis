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

.. |ds_normal_dia| replace:: Fig. 4

.. |ds_normal_dia_long| replace:: **Figure 4**

.. |ds_perpendicular_dia| replace:: Fig. 5

.. |ds_perpendicular_dia_long| replace:: **Figure 5**

.. |ds_normal_eulerian_dia| replace:: Fig. 6

.. |ds_normal_eulerian_dia_long| replace:: **Figure 6**

~~~~~~~~~~~~~~~~~
The strain tensor
~~~~~~~~~~~~~~~~~

Mechanical model
================

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

Infinitesimal strain
--------------------

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

Lagrangian strain
-----------------

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

Eulerian strain
---------------

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
  :align: center
  :width: 9.5cm
  :height: 3.3cm


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
