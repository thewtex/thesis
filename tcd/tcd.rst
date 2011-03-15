=============================================================
Transcranial Doppler Monitoring of the Middle Cerebral Artery
=============================================================

In this chapter, we discuss how transcranial Doppler ultrasound (TCD) is used to
provide additional insight into the neurophysiology of patients prior to
endarterectomy.  First, a review is given of the ways TCD is applied in a
clinical monitoring and research setting.  Next, techniques to increase the
reliability of data collected in this are covered.  Finally, the microemboli and
peak velocity data collected as part of this study are presented.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Physiological insights from transcranial Doppler
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

TCD is a useful tool in research and clinical
situations where monitoring of intracranial blood flow is desired.  For example,
TCD is used in psychology experiments [Sorond2008]_, evaluating the potential
for sickle cell stroke [Melo2008]_, estimation of intracranial
pressure [Rasulo2008]_, and inpatient
monitoring [McDermid2008,Rasulo2008]_.  TCD can be brought bedside or in
surgery, is cost-effective, has very good temporal resolution, can collect data
for extended time periods, and is non-invasive.  However, there are limitations
associated with its use.  For 10% to 30% of patients, the acoustic window is
too thick to obtain adequate signals, it is sensitive to motion, and it can be
difficult to locate vessels with the single element transducer.  Collection and
analysis of TCD data is also labor intensive and time
consuming [Kwee2008,Rasulo2008]_.

The purpose of TCD in this study is to detect microemboli originating from
vulnerable carotid plaque.  A microemboli passing through the MCA will result in
what is termed a microembolic ultrasonic signals (MES) or high intensity
transient signals (HITS).  TCD provides a non-invasive *in vivo*
validation of the vulnerability assessment of plaque tissue obtained with strain
imaging.  Microemboli detected with TCD have been connected to peri-operative
symptoms of ipsilateral cerebral ischemia [Levi1997,Spencer1997]_.

Furthermore, MES predict future ischemic events such as episodic stroke, TIA, or
migraines [Ritter2008,Jesurum2008,Zuromskis2008,Siebler1995]_. In a typical
single one hour session, 43% of symptomatic cases and 10% of asymptomatic
cases will show one or more MES [Ritter2008]_.  If a MES is seen with an
asymptomatic case, the risk of stroke or TIA in the future increases
significantly [Markus2005,Ritter2008]_. In addition, recent evidence
reinforces the supposition that microemboli causes Alzheimer's disease and
vascular cognitive dementias or
impairment [Purandare2006a,Purandare2006,Purandare2007]_.

Microemboli may originate from locations other than the carotid, such as a PFO,
other types of right to left shunts other than a PFO, mechanical heart valves,
atrial fibrillation, or congestive heart disease.  However, for elderly
patients, the most common source is thought to be the carotid.  Unlike emboli of
cardiac origin, microemboli from the carotid should be unilateral and
ipsilateral to the vulnerable carotid.

TCD requires ultrasonic transmission through the cranium.  This can be achieved
via four acoustic windows, the transorbital, suboccipital,  transtemporal, or
retromandibular [Rasulo2008]_.  Interrogation of the middle cerebral artery
is achieved through the transtemporal window directly above the ear where there
is thinning of the cranial plate.  The MCA is by far the most common vessel
examined when searching for microemboli.  It is one of the main branches
extending from the Circle of Willis, and flow from the internal carotid artery
is directed at the MCA.  It is necessary to monitor for microemboli at the MCA,
a location distal to the plaque, because it would be difficult to monitor all of
the plaque and detect dislodging of the microemboli.  Clinical ultrasound
currently generates 2D planar images and the resolution is insufficient to
detect a microemboli *in vivo*.

Patients are typically monitored for an hour, with one or more microembolic
events considered significant [Ritter2008]_.  The identification criteria
for MES are transient signals, lasting less than 300 milliseconds, at least 3dB
higher than the background blood flow signal, unidirectional in velocity, and
accompanied by an audible 'snap', 'chirp', or 'moan' [CCNICHS1995]_.

A similar study was performed by Zuromskis et. al. [Zuromskis2008]_ where the
relationship between MES and traditional ultrasonic vulnerability metrics,
echogenicity and blood flow velocities, was examined.  The conclusion of that
study was as follows: Despite optimum standard anti-platelet therapy, cerebral
micro-embolization occurs in 30% of patients with symptomatic carotid artery
disease, which might therefore be a possible risk factor for recurrent
neurological symptoms. However, the presence of MES is independent of
intrastenotic blood flow disturbances and grey scale ultrasound plaque
characteristics. The conclusion of that study is that the presence of MES as an
indicator of unstable plaque and thereby a possible risk factor for stroke
should be evaluated prospectively using various algorithms for plaque
classifications [Zuromskis2008]_.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Methods to increase the robustness of unstable data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Transcranial Doppler has been performed thus far on a few patients using a Multidop-L2 2.54g system made by DWL (Germany).
One hour of data is collected immediately following acquisition of the carotid ultrasound data for strain imaging.
A pair of 2 $MHz$ transducers are focused on the right and left middle cerebral arteries (MCA) at the transtemporal acoustic windows and secured with the Marc600 Transcranial Fixation System head unit.
The Doppler gate is placed at a depth of 30 to 67 $mm$ depending on the size of the patient.

The system displays the power spectrum calculated with a 128 FFT with 67\% overlap and a sampling frequency of 1 $kHz$.  The pulse repetition frequency (PRF) is 3 $kHz$.
Additionally, the envelope of the peak velocity for both channels is displayed along with a histogram of High Intensity Transient Signal (HITS).  
A HITS is recorded whenever the signal exceeds 3 dB over the background signal.  
During acquisition there are multiple false-positive HITS detected because of motion artifacts.
To address false positives, marks are added to the data indicating a possible true micro-embolic signal or a known motion artifact.  

Post-processing is performed to provide further scrutiny to the collected data.
A custom application was developed to visualize and analyze the available data show in Figure~\ref{fig:tcd}.
Only the envelope of the peak velocities, HITS times, and marks could be retrieved from the recorded data.
To expedite analysis of the data collected over an hour time period, three plots of the peak velocity waveform are displayed at three time scales, i.e. the entire acquisition, a 100 second window, and a 5 second window.
Clicking on a time segment in the entire acquisition will display the indicated segment in the 100 second window, and clicking on a time segment in the 100 second will display the shaded region in the five second window. 
Time points where the DWL detected a HITS signal are displayed as a non-overlapping dot along with text indicating the magnitude in $dB$.
False and True marks are also displayed as non-overlapping dots, but in distinguishing colors.

TCD is notorious for difficulties when attempting to obtain useable, reliable
data.  While valuable physiological data can certainly be acquired, consistent
collection of this data is a challenge.  McMahon et al. examined the
reproducibility of TCD acquisition of MCA velocities [McMahon2007]_.
Intraobserver variablity was high, and interobserver variability was even
higher.  On the whole, and Bland-Altman analysis resulted in a 95% limit of
agreement of ±36.7 cm/s [McMahon2007]_.  The experience of ultrasonographer can
be critically important, and in that study inter-observer variance between
experienced practioners was ±22.1 cm/s.  Other factors that can compromise
success include environmental factors and patient compliance [McMahon2007]_. 

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Microemboli and peak velocity results
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Right MCA pulsitility index has been found to have a positive correlation with
a global cognative function test in patients with congestive heart failure
[Jesus2006]_.

Natural variations are also common.  Velocities in females is relatively higher
than males, and velocity on the left side is slightly higher than the right side
[Farhoudi2010]_.  Changes in the TCD measured MCA peak systolic velocity were
correlated with MCA stenosis in a study that validated its findings with
magnetic resonance angiography [Tang2005b]_.  In cases of focal MCA stenosis,
peak systolic velocities of 140 m/s or higher correlate with a 50% or higher
level of stenosis [Tang2005b]_.  When there is diffuse stenosis of 50% or
higher, peak systolic velocities exceeded 140 m/s in roughly a quarter of the
subjects, but in 54% of the subjects the peak systolic velocity was less than 50
cm/s [Tang2005b]_.
