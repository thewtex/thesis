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
displacement maps.  Since regularization helps to enforce diffeomorphic behavior
with block-matching methods, it helps to remove peak-hopping errors in addition
to generally improving the motion estimates.  The motion estimates are improved
by addressing quantization and decorrelation noise as well as addressing the
"aperture" problem [Horn1981]_.  The aperture problem recognizes that a block
may not have derivatives in the image intensity in all directions, and it is
difficult to determine displacement in directions where gradients are small.

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

We will examine a regularization approach that attempts to optimize the
displacement using both the block similarity metric and the motion of
neighboring blocks.   However, unlike the aforementioned algorithms, we do not
explicitly formulate the problem as the minimization of a cost function.
Instead, we follow the approach proposed by Hayton et al. [Hayton1999]_ where
the similarity metric is viewed in a probabilistic framework.  Iterative
Bayesian regularization is applied based on the similarity metric observed in
neighboring blocks.  Hayton et al.[Hayton1999]_ originally applied this method
for deformable image registration of magnetic resonance images obtained during
breast imaging.  The purpose of the algorithm was to register MR breast images
taken before and after injection of a contrast agent, Gd-DTPA.  Without
registration, patient motion due to breathing and other motion would interfere
with effective analysis of the images.  A mutual information similarity metric
was used and a multi-scale implementation was generated.  After the
block-matching displacement estimates were obtained, they were used as initial
values for a deformable cubic B-spline motion model that was regularized by a
smoothing term

.. math:: \rho \int \int u_{xx}^2 + 2 u_{xy}^2 + u_{yy}^2

and optimization performed with the conjugate gradient descent method.

The paper by Hayton has been referenced many times in the literature, but the
author has not found a paper the reimplemented and applied the algorithm.
However, another paper that describes application of the algorithm to an
ultrasound registration case was published from the same Michael Brady Oxford
University group.  Xiao et al. applied this method to the registration of 3D
B-Mode ultrasound subvolumes[Xiao2002]_.  B-Mode breast ultrasound volumes were
collected by free-hand sweeping of a 2D ultrasound transducer.  Multiple sweeps
are obtained to obtain a larger area and reduce speckle noise through spatial
compounding.  Differing sweep speeds, angles, and tissue deformation require
deformable registration of the sub-volumes.  In contrast to the Hayton MR paper,
normalized cross correlation was used as a similarity metric and single-level
searching was performed.  Like the Hayton experiment, the resulting
displacements where input into a cubic B-spline parameter optimization with a
smoothing term consisting of squares of the second derivatives of displacement
and solved with the conjugate gradient descent method.

Algorithm
=========

In block-matching methods, a small kernel from the pre-deformation image is
compared to the post-deformation image using a similarity metric
[Ophir1991,Ophir2001]_.  We assume the comparison is made on a regular grid of
points by translating the kernel within a specified search region.  The grid of
similarity metric values located at the kernel's center define a similarity
metric image associated with the kernel utilized for displacement estimation.
Examples of similarity metrics include sum of absolute difference, sum of
squared differences, normalized cross correlation, phase correlation, or mutual
information [Zitova2003,Crum2004]_.

We can treat the similarity metric image as a probability image for the
displacement of the kernel by applying a few basic transformations.  First, the
similarity must be inverted, if necessary, such that the maximum value
corresponds the region with the greatest similarity.  For normalized cross
correlation or mutual information this is not required, but it is required for
most other similarity metrics.  Next, the metric must be shifted by the negative
of the metric's theoretical minimum so the smallest resulting value is zero.  In
the case of normalized cross correlation, 1.0 is added to the similarity metric
since its bounds are :math:`[-1, 1]`.  In the case of an inverted sum of squared
differences, the theoretical minimum is negative infinity, but real world
limited bit depth integer data and with finite signal length allow the use of a
reasonable finite lower bound.  Finally, the similarity metric values are
normalized by their sum such that integral of all values is unity.  The
similarity metric image can now be treated as a probability image for
displacement estimation using the kernel.  A value of zero in the probability
image occurs at the metric's theoretical minimum with the sum of probabilities
being unity.

The probability images obtained are prior probability estimates, :math:`Pr( \mathbf{u_x} )`, in
a Bayesian framework.

.. math:: Pr( \mathbf{u_x} | \mathbf{u}_{\mathcal{N}_x} ) = \frac {Pr( \mathbf{u}_{\mathcal{N}_x} | \mathbf{u_x} ) Pr( \mathbf{u_x} )} { Pr ( \mathbf{u}_{\mathcal{N}_x} ) }

where :math:`\mathbf{u_x}` is the displacement of the kernel at location :math:`\mathbf{x}` and
:math:`\mathbf{u}_{\mathcal{N}_x}` is the displacement at the neighboring kernels.  The
denominator, :math:`Pr ( \mathbf{u}_{\mathcal{N}_x} )` serves at as a normalizing
constant.  This factor is accounted for by re-normalization at the end of every
iteration of the algorithm.

We assume that :math:`Pr ( \mathbf{u}_{\mathcal{N}_x} | \mathbf{u_x} )` can be
modeled by the probabilities of the displacements estimated at immediate
neighbors, i.e. four neighbors in 2D.  In addition, we assume that these
probabilities are independent.

.. math:: Pr ( \mathbf{u}_{\mathcal{N}_x} | \mathbf{u_x} ) = \prod_{\mathbf{x'} \in \mathcal{N}_x} Pr( \mathbf{u_{x'}} | \mathbf{u_x} )

Here :math:`Pr( \mathbf{u_{x'}} | \mathbf{u_x} )` is the probability that a neighboring block at
:math:`\mathbf{x}'` has a displacement :math:`\mathbf{u_{x'}}` given a displacement :math:`\mathbf{u_x}` at
:math:`\mathbf{x}`.  The assumption of independence is usually invalid, but iterative
application of the algorithm is intended to account for some of the expected
correlation between neighboring displacement estimates.

We model :math:`P( \mathbf{u_{x'}} | \mathbf{u_x} )` as the maximum of the neighboring probability image modulated
by a Gaussian term.

.. math:: Pr( \mathbf{u_{x'}} | \mathbf{u_x} ) = \max_{\mathbf{v}} \left[ Pr( \mathbf{v_{x'}} ) \exp( \frac{- || \mathbf{v_{x'}} - \mathbf{u_x} || ^2 } { 2 \mathbf{\sigma_u}^2 } ) \right]

Here :math:`\mathbf{v_{x'}}` is the displacement at :math:`\mathbf{x'}`.  We
restrict the above to :math:`|| \mathbf{v_{x'}} - \mathbf{u} || < \epsilon`,
where :math:`\epsilon` is a threshold.  The :math:`\mathbf{\sigma_u}`: is a vector that determines the width of Gaussian-like term for each direction.  If :math:`\delta_x` is the spacing
between kernels in one direction, then :math:`\sigma_\varepsilon = \sigma_u / \delta_x`, the strain regulation sigma (SRS),
represents the algorithm's parameter in terms of a factor related to the
expected strain.  Spacing between kernels can be decreased by increasing kernel
overlap or decreasing their dimension.

A likelihood term for the Bayesian model can then be written as,

.. math:: Pr( \mathbf{u}_{\mathcal{N}_x} | \mathbf{u_x} ) = \prod_{\mathbf{x'} \in  \mathcal{N}_x} Pr( \mathbf{u_{x'}} | \mathbf{u_x} ) = \prod_{\mathbf{x'} \in  \mathcal{N}_x} \max_{\mathbf{v}} \left[ Pr( \mathbf{v_{x'}} ) \exp( \frac{- || \mathbf{v_{x'}} - \mathbf{u} || ^2 } { 2 \mathbf{\sigma_u}^2 } ) \right]

The influence of neighbors beyond adjacent blocks can be achieved by
recursively applying the regularization.

The displacement of the kernel is taken according to the *maximum a posteriori*
principle.

.. math:: \mathbf{u_x} = \arg\max_{ \mathbf{u_x} } Pr( \mathbf{u_x} | \mathbf{u}_{\mathcal{N}_x} )

Subsample precision of the displacement is achieved using interpolation of the
posterior probability.

Implementation
==============

A multi-threaded version of the described algorithm was implemented with the
Insight Toolkit [Yoo2002]_ using normalized cross-correlation as the similarity
metric for the results presented in this article.

The search region was 17 A-lines in the lateral direction along with sufficient
data points along the axial direction to capture the maximum displacement for
the following analysis.  A simple unguided search was used, which is sufficient
for the following analysis but not computationally efficient.  The means to
provide a computationally efficient implementation is achieved with the
multi-resolution methods described in the other chapters.  For a 2D image, the
computational complexity scales with order :math:`\mathcal{O}(n^2)` for a search
region of side length *n*.  That is, the computational quadruples as the size of
the search region doubles.  The size of the search region can be significantly
reduced by using a coarse-to-fine or multi-scale approach.  Motion estimates
from sub-sampled images are used to initialize the center of the search region
in finer resolution images.

The quantity :math:`\epsilon`, where :math:`|| \mathbf{v_{x'}} -
\mathbf{u} || < \epsilon` was taken to be :math:`3 \sigma_u`.

We followed the recommendations described in [Hayton1999]_ and [Xiao2002]_ and applied the
natural logarithm operator before the exponential operator after computing
posterior probabilities.  The idea is that additions, which are not as
computationally expensive as multiplications, can be used in the
convolution-like operation used for computing posterior probabilities.  That is, the
log posterior probability is computed using

.. math:: Pr_{log} ( \mathbf{u_x} | \mathbf{u}_{\mathcal{N}_x} ) \propto \sum_{\mathbf{x'} \in  \mathcal{N}_x} \max_{\mathbf{v}} \left[ Pr_{log} ( \mathbf{v_{x'}} ) - \frac{ || \mathbf{v_{x'}} - \mathbf{u} || ^2 } { 2 \mathbf{\sigma_u}^2 } \right] + Pr_{log} ( \mathbf{u_x} )

The statement is only proportional because it does not contain the denominator
in Bayes' Theorem, which is accounted for by re-normalization after taking the
exponential of the posterior probability.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Experimental Methods and Results
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Uniform Strain Simulations and Phantoms
=======================================

A uniform elastic modulus tissue-mimicking ultrasound phantom was tested.
Frames of data were continuously collected as the unconstrained phantom was
deformed with an acrylic plate.  The plate was  fitted with a transducer at the
center and translated using a linear motion table.  The phantom was scanned
using a Siemen's S2000 (Siemens Ultrasound, Mountain View, CA, USA) clinical
ultrasound system equipped with a VFX9-4 transducer and the plane through the
center of the sphere imaged.  The transducer was excited at 8.9 MHz and
radiofrequency (RF) data was sampled at 40 MHz to a depth of 5.5 cm.

Twenty independent deformation experiments were performed by varying the
pre-deformation frame index within the continuous loop to obtain statistically
significant results.  The frame average strain was controlled by the frame skip
between pre-deformation and post-deformation frames.

Displacement estimation error was quantified using the elastographic
signal-to-noise (SNRe) ratio in the axial direction [Ophir2001]_

.. math:: SNR_e [dB] = 20 \log10 \; ( \frac {m_\varepsilon} {s_\varepsilon} )

where :math:`m_\epsilon` and :math:`s_\epsilon` are the mean and standard
deviation of the axial strain, respectively.  Calculation of the SNRe
was restricted to the area around the transducer's focus.

Numerical ultrasound simulations were designed to mimic the ultrasound physics
and solid body mechanics present in the phantom.  The RF data was generated
using an ultrasound frequency domain simulation program developed in our
laboratory [Li1999]_.  Uniformly distributed collections of randomly positioned
acoustic scatterers were generated and their response to a linear array
transducer over a range of frequencies calculated.  A particular ultrasound
transducer was simulated by multiplying the phantom response in the frequency
domain with the spectrum for the ultrasound transducer of interest.  A single
row of 128 elements was the aperture, with a spacing of 0.2 mm between elements.
An individual element had a size of 0.15 mm laterally and 10 mm elevationally.
The beamspacing was 0.2 mm, and the transmit focus was located at a depth of 20
mm.  This yielded the Fourier Transform of the RF data of interest.  For these
experiments, the simulated transducer's spectrum was modeled as Gaussian with a
center frequency of 8.0 MHz and a 40% fractional bandwidth. The simulated
transducer array had a channel count of 128 elements.  Displacements were
applied to the individual scatterers that made up each numerical phantom, to
produce a set of post-deformation numerical phantoms and the accompanying RF
data.  A 40mm×40mm×10mm volume of scatterers was simulated.

The deformation field for a uniform elastic modulus phantom undergoing
unconstrained compression along the axial direction is simply a linear increase
in displacement starting from zero at the transducer surface.  The slope of the
displacement is the amount of strain applied.  In the lateral direction the
displacement often starts from zero at the center of the phantom and increases
linearly towards the edge of the phantom.  The slope of the displacement is the
applied axial strain multiplied by Poisson's ratio.  If we assume an
incompressible material as is common for soft tissues and the gelatin phantoms,
the Poisson's ratio is near 0.5.

Deformation estimation statistics on n=30 randomly generated
collections of scatterers were collected.

The simulations of a uniformly elastic TM block were examined in a manner
similar to the uniform TM phantom and evaluated for variations in the SNRe with
applied deformation.

Circular Inclusion Simulations and Phantoms
===========================================

A TM ultrasound elastography phantom subject to uniform deformation was imaged
using a clinical ultrasound scanner.  The 10×10×10 cm gelatin phantom had a 1.0
cm spherical inclusion near its center.  This type of phantom is common in the
elastography literature because of its simple, well known behavior and
resemblance to a tumor within background tissue.

Displacement estimation error for comparison with the median filter and
optimization of SRS was computed as follows.  The estimated displacements were
interpolated with cubic B-spline interpolation such that the sampling of the
displacement image matched that of the RF data.  The inverse displacement was
applied to each pixel in the pre-deformation image, and windowed-sinc
interpolation applied to find the corresponding RF value in the post-deformation
image.  A mean absolute RF difference (MARD) is reported excluding the edges of
the image where edge effects or out-of-bounds conditions may occur.

.. math:: MARD = \frac{ \sum_{i=1}^n | I_m(\mathbf{x}_i - \mathbf{u}_{x,i}) - I_f(\mathbf{x}_i) | } { n }

Where :math:`I_m` is the interpolated RF value in the post-deformation (moving)
image and :math:`I_f` is the RF value in pre-deformation (fixed) image.

In order to simulate the circular inclusion, displacement fields were generated
by specifying the mechanical properties of interest, and applying uniform
displacements as boundary conditions using commercially available finite element
software, ANSYS (ANSYS Inc, Pittsburgh, PA, USA).  Displacement fields were
simulated for a simulation having a uniform background modulus of 2kPa and a
circular inclusion with a modulus of 8 kPa.  The inclusion's diameter was 8 mm.
Boundary conditions were as follows.  Uniform displacements were applied across
the tops of each simulation in the axial direction such that the nominal strain
produced in the simulation was equal to 0.5%,
1.0%, 3.0%, 5.0%, 7.0%, and 9.0%.  The bottom of the simulation was constrained to
have no axial displacement, and a single node was fixed in the lateral
direction at the bottom, central node to ensure uniqueness of the solution.
Displacement fields from a nearly incompressible (Poisson's ratio of 0.495)
material model in a plane stress state were simulated and applied to the
numerical phantoms.  The mechanical model represents a cylindrical inclusion
in an unconstrained background, which is similar in its deformation to the
spherical inclusion phantom [Skovorada1994]_.

Again, deformation estimation statistics on n=30 randomly generated
collections of scatterers were collected.

Displacement estimation error for comparison with the median filter and
optimization of SRS were computed as follows.  Output
displacements from the finite element simulation were interpolated with cubic
B-spline interpolation at locations where displacement estimation occurred.  A
mean absolute axial displacement difference (MADD) is reported excluding the edges of
the image, where edge effects may occur.

.. math:: MADD = \frac{ \sum_{i=1}^n | \hat{u}_a - u_a | } { n }

Where :math:`\hat{u}_a` is the estimated axial displacement and :math:`u_a` is
the known axial displacement.

Addressing a Carotid Reverberation
==================================


Improvement of Carotid Strain Images
====================================


~~~~~~~~~~
References
~~~~~~~~~~

.. sectnum::


