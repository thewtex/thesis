======================================================================
Recursive Bayesian Regularization Applied to Ultrasound Strain Imaging
======================================================================

This chapter describes how a recursive Bayesian regularization algorithm can be
applied during ultrasound displacement estimation to improve the quality of
carotid strain images.  First, we describe regularization's role in the block-
matching approach to deformable image registration.  Then we review
regularization algorithms that have been implemented in the literature.  Next,
we describe the iterative probabilistic approach taken in this work.  Finally,
we present results on simulations, phantoms, and carotid strain image case
studies.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Improvement of Strain Image Quality with Regularization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The deformable image registration problem is common in medical imaging
[Zitova2003, Crum2004]_.  It is used to monitor tumor growth, compensate for
patient motion, register to a common atlas, etc.  In the context of ultrasound
strain imaging, estimating local is the first step in a two stage process; in
the second step strains are calculated from the estimated displacements.  In
some cases strain is estimated iteratively along with the displacements in order
to improve the quality of strain estimation
[Brusseau2001,Maurice2004a,Brusseau2008]_, but all algorithms take this form.

In simple block-matching image registration methods, the registration of a block
is isolated to the given block.  Motion of the block is local, and motion of
surrounding regions is not considered in determination of the block's
displacement.  Regularization methods allow displacements and success in
tracking of surrounding regions to influence the local displacement estimate.

Most regularization routines fit into a cost function paradigm.  Without
regularization, the estimated displacement, :math:`\mathbf{\hat{u}_x}`, can
be formulated as

.. math:: \mathbf{\hat{u}_x} = \arg\min_{\mathbf{u_x}}  E_s( \mathbf{u_x} )

Where :math:`E_s` is a similarity metric term, e.g., sum of squared differences,
negative of the correlation coefficient, etc.  When regularization is performed
in a cost function paradigm, an additional term must be minimized.

.. math:: \mathbf{\hat{u}_x} = \arg\min_{\mathbf{u_x}} [ E_s( \mathbf{u_x} ) + \alpha \: E_c( \mathbf{u}_{\mathcal{N}_x}, E_s( \mathbf{u}_{\mathcal{N}_x} )  ) ]

Here :math:`E_c` is a continuity term that depends on the neighboring
displacements and the similarity metric at neighboring displacements.  The
parameter :math:`\alpha` determines the amount of regularization.  A higher
:math:`alpha` will given greater weight to the displacement of surrounding
displacements and increase the amount of regularization.  Different algorithms
will implement their choice of :math:`E_s`, :math:`E_c`, and optimization
technique to minimize the cost function.

The result of regularization is an improved displacement estimate since we can
incorporate our *a priori* knowledge that the displacement is continuous.
However, if the regularization parameter :math:`\alpha` is too large, excessive
smoothing may introduced causing a loss of features and dynamic range in the
strain images.  Regularization of this type is especially important for
block-matching deformable image registration techniques where the motion model
does not assume any continuity.  Motion is considered as a completely local
phenomena.  This contrasts with B-Spline, Elastic Body Spline, or Finite
Element Method (FEM) deformable image registration methods
[Zikic2006,Davis1997,Krucker2002,Craene2009,Zhong2007]_.  In these methods, the motion
model is such that a local point moves in concert with tissues.

While B-Spline deformable transform do not have the same difficulty the
block-matching methods have in enforcing local continuity, they both share a
related problem since the B-Spline deformation basis functions are compactly
supported.  Both block-matching and B-Spline deformable transforms do not
enforce diffeomorphic transform [Rueckert2006,Craene2009]_.  A displacement map that is
diffeomorphic must be continuous, differentiable, and invertible [Craene2009]_.
A diffeomorphic transformation be a one-to-one mapping between the pre and post
deformation image.  Consider the following B-spline grid from Schnabel et. al.
that illustrates non-diffeomorphic behavior [Schnabel2001]_

.. figure:: figures/folding.png
  :width: 7cm
  :height: 4.2cm
  :align: center

  B-spline grid demonstrating non-diffeomorphic folding.  Taken from
  [Schnabel2001]_.

.. |folding| replace:: Figure 1

Folding or tearing is not likely or possible in physical tissues, so
diffeomorphic behavior should be enforced.

Peak-hopping errors in block-matching methods will result in non-diffeomorphic
displacement maps.  Since regularization helps to enforce diffeomorphic behavior with
block-matching methods, it helps to remove peak-hopping errors in addition to
generally improving the motion estimates.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Prior Efforts in Regularization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Peak hopping errors and degradation in the quality of the strain image results
primarily from signal decorrelation [Varghese2001, Varghese1998]_.  The source
of signal decorrelation can be large axial deformations that distort the signal,
motion of tissue in the elevational direction relative to the probe, or
undesirable physiological motion [Kallel1997,Kallel1997a]_.

Most approaches to address signal decorrelation can be placed in two categories.
One strategy trys to reduce peak hopping be restricting the search region of a
matching kernel.  Tighter search regions are feasible when the center of the
search region is initialized appropriately.  Sometimes, *a priori* knowledge of
the type of motion expected is used to initialize search regions.  Hall et al.
described an implementation where the displacement is always assumed to be null
at the transducer surface [Hall2003]_.  This is a reasonable assumption since
the transducer must always remain in contact with the tissue to generate an
image and the stiffness of transducer is so much higher than the soft tissue, it
can be considered a rigid body.  Motion tracking starts from the transducer
surface, and the displacement estimates are used initialize search regions
deeper into tissue.  Basarab et al. describe a similar strategy [Basarab2008]_.
Search regions are propagated by displacement estimates starting from the center
of the transducer.  The points initialized are set in a "V" shaped front in
order to better initialize lateral displacements since lateral displacement is
often near zero at the transducer's center during freehand compression and
increases towards the edges of the transducer.

Search region initialization strategies that do not depend on the presence of
locations of zero displacement somewhere in the image use points or lines of
high displacement estimation confidence.  Instead of propagating search region
centers axially from the transducer, estimates can be propagated from an A-line
of high confidence [Jiang2007,Rivaz2010]_ or diagonally [Zahiri-Azar2006]_.
Chen, Treece, Lindop, Gee, and Prager have described a quality-guided algorithm
that uses multiple seed points [Chen2009]_.  The initial seed points required a
large search region.  After initialization, search regions are kept small.
Displacements are estimated from neighbors adjacent to the seed with the search
region centered at the seed's displacement.  Among these neighbors and the other
seed's neighbors, the location with the best quality metric is used to
initialize the next set of search regions.  The process proceeds iteratively
until the entire image has been tracked, and search region initialization
propagates from location of highest tracking quality.  The quality metric used
was normalized cross correlation.

A weakness of the other search region initialization algorithms that the seeds
algorithm overcomes is the presence of discontinuous locations.  This can occur
with a slip boundary along a tumor or the vessel wall of the carotid artery, for
example.  This weakness is also overcome by a coarse-to-fine scheme where
displacements from a large kernel or low-pass filtered and sub-sampled kernel
initializes the conter of the search region at progressively smaller kernel
sizes to achieve a high resolution strain image [Pellot-Barakat2004, Shi2007,
Yeung1998, Chen2007, Bai1999, Basarab2008, Lopata2009]_.  This multi-resolution
pyramid approach is commonly employed in many different types of registration
problems.  Since tracking in the coarse image can be performed on subsample
data, initialized is performed quickly.  Also, robustness is improved because
initializition occurs near the final solution and local minima in the high
frequency speckle are avoided.

The second strategy to address decorrelation noise in ultrasound displacement
estimation incorporates displacements from neighboring blocks into the
displacement estimation equation.  Filtering approaching remove noise but come
at the cost of reduced strain dynamic range and spatial resolution.  For
example, a median filter can be used to remove outliers, [Thitaikumar2008a]_.
During estimation of strains from estimated displacement, a least squares fit to
the displacement can be used estimate the local slope in displacement, i.e. the
strain [Kallel1997a]_.  A statistical model of the displacements can be taken
and the Kalman filter used during estimation for the strain [Rivaz2010]_.
Alternatively, as mentioned previously, a cost function optimization approach
can be taken involving a similarity metric term and a displacement continuity
term.  Both Jiang and Rivaz describe implementations of this approach that use
dynamic programming, sometimes called the Viterbi algorithm, to solve the
optimization problem [Jiang2009,Rivaz2008]_.  Dynamic programming is a global, non-iterative
optimization strategy that finds the shortest path through transitioning states
given a cost to go from one state to the next set of states.  In the context of
block-matching motion tracking, each state represents the displacement of a
kernel.  The next set of states is the displacement of the next kernel along an
A-line.  The transition cost is the chosen cost function that has a similarity
and a continuity term.  In Jiang's paper, normalized cross correlation was used
as a similarity metric and a number of continuity terms were examined
[Jiang2009]_,

.. math:: S = \sqrt{ \left( \frac{\delta \overrightarrow{u}}{\delta x} \right)^2 + \left( \frac{\delta \overrightarrow{u}}{\delta y} \right)^2 }

.. math:: E_{c,a} = \frac{S}{ \sqrt{|S|^2 + \beta}}

.. math:: E_{c,b} = \left\lbrace{ \begin{tabular}{ll} $e^S - 1,$ & $S < 2$ \\ $\frac{S}{ \sqrt{|S|^2 + \beta}} + e^2 - 1,$ & $S \geq 2 $ \end{tabular} } \right.

.. math:: E_{c,c} = 2 \, (e^S - 1)

In Rivaz's article, he examined sum of absolute differences as a similarity
metric and the following continuity term[Rivaz2008]_,

.. math:: E_c = ( d_i - d_{i-1} )^2

where d\ :sub:`i` is the displacement at sample *i*.

Brusseau used a sequential quadratic programming strategy to solve the
optimization problem.  This is a Newton like optimization technique that allows
for constrained parameters.  She applied normalized cross correlation as the
similarity metric and used the following as a continuity term [Brusseau2008]_,

.. math:: E_c = \left( \frac{ \alpha - \alpha_{average} }{ \alpha_{max} - \alpha_{min}} \right)^2 + \left( \frac{u - u_{average}}{ u_{max} - u_{min} } \right) ^2

Where *α* is a scaling factor related to the local strain and *u* is the local
displacement.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Recursive Bayesian Regularization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

~~~~~~~
Results
~~~~~~~

Uniform Strain Simulations and Phantoms
=======================================


Circular Inclusion Simulations and Phantoms
===========================================


Addressing a Carotid Reverberation
==================================


Improvement of Carotid Strain Images
====================================


~~~~~~~~~~
References
~~~~~~~~~~

.. sectnum::


