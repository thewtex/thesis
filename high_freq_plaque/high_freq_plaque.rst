======================================
High-frequency Plaque Characterization
======================================

High-frequency ultrasound imaging is useful for examining small objects -- it
has the advantage of high resolution at the expense of low penetration.  In this
chapter we explore new high frequency imaging techniques to interrogate the
excised plaques which result from endarterectomy.  Finally, we present initial
3D parametric images of the excised plaques.


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Parametric images of excised plaque
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

As mentioned in the background section, strain imaging holds promise because it is a direct measure of the local load the tissue is experiencing as opposed to approaches where measurements or assumptions of composition, geometry, and loading are used in a computational model or statistical classification to imply loading.
An advantage to this approach is that errors from modeling simplifications and parameter measurements do not accumulate as significantly.
The reference phantom method is analogous for ultrasonic tissue parameter characterization.
Diffraction effects are measured empirically in a phantom environment similar to that expected \textit{in situ} with minimal modeling or assumptions.

Approximately two weeks following the \textit{in vivo} carotid ultrasound examination and TCD recording, patients undergo surgery for plaque excision.
Endarterectomy specimens are retrieved immediately following surgery for scanning and returned the same day to pathology for analysis and histology preparation.
Samples are examined in a water bath and suspended between two catheter sheaths.
A picture of the experimental setup is shown in Figure~\ref{fig:apparatus}.
\begin{figure}[h]
  \begin{center}
    \includegraphics[width=6cm]{preliminary_results/figures/apparatus}
  \end{center}
  \begin{flushleft}
    \caption[High-frequency apparatus.]{\flushleft{High-frequency apparatus.  The transducer is fixed to a 3D motion table and lowered into the water bath.  A disposable transducer cover is covered with coupling gel and held to the transducer with a rubber band for safety reasons.  The plaque is suspended between two catheter sheaths and the stepper motor moves the transducer parallel to the longitudinal direction of the plaque.}}
\end{flushleft}
  \label{fig:apparatus}
\end{figure}
A commercially available VisualSonics Vevo 770 is used for ultrasound radiofrequency acquisition.  
This machine is not approved for clinical human use by the Federal Food and Drug Administration, and it is marketed primarily towards research on small animals (primarily mice and rats).  
A diagram of a 770 model transducer is shown in Figure~\ref{fig:apparatus}.
A 100\% bandwidth transducer rests at the end of a shaft whose pivot point is high within the body of the assembly.  
The angular position is measured with a rotary encoder and scan conversion is necessary for proper display.
\begin{figure}[h]
  \begin{center}
    \includegraphics[width=7cm]{preliminary_results/figures/transducer_diagram}
  \end{center}
  \caption[High-frequency transducer.]{\flushleft{A diagram of a VisualSonics 770 transducer.  A 100\% bandwidth single-element transducer is rotated on a shaft whose pivot point lies high within the transducer housing.  The transducer lies within a housing that needs to be filled with distilled water and is covered with a thin replaceable acoustic membrane.}}
  \label{fig:transducer}
\end{figure}

The transducer selected was a RMV710B that has a center frequency of 25 $MHz$, which is on the lower end the center frequency for available transducers.
This transducer outputs frequencies upto 37.5 $MHz$, with an axial resolution of 70 $\mu m$, lateral resolution of 140 $\mu m$, focal length 15 $mm$, and a maximum field of view of 20.0 $mm$.
The RMV710B was selected because the frequency was low enough to penetrate the plaque and the field of view was large enough to encompass the entire sample.

Acquisition of RF data necessary for more fundamental ultrasound physics research is a secondary feature of the system.
A BNC connector on the back of the machine was provided for collection of data with an oscilloscope or other external analog-to-digital system. 
More recent models are equipped with an optional internal Analog-to-Digital (A/D) card for collection of RF data, which was utilized in our study.
Data collection is well integrated into the user interface of the machine, but buffer limits on the A/D card limit the length of acquisition to a subset of the field of view, which is shown in Figure~\ref{fig:digital_acquisition}.
\begin{figure}[h]
  \begin{center}
    \includegraphics[width=11cm]{preliminary_results/figures/digital_acquisition}
  \end{center}
  \caption[Digital acquisition on the VisualSonics.]{\flushleft{Digital acquisition user interface on the VisualSonics.  Basic system settings are shown in the upper left.  The upper right displays the total transducer field of view with the limited portion where RF data can be captured in the red box.  The lower left scout window displays the location of collected RF lines along with displaying any points of saturation is cyan.  The lower right shows the RF signal along a selected line along with a power spectrum for the line.}}
  \label{fig:digital_acquisition}
\end{figure}
RF acquisition is performed in M-mode and is considerably slower than B-mode rates.
The collection of a single 3D data set covering an entire plaque takes approximately two hours.
RF acquisition was previously limited to single 2D frames, but we worked with VisualSonics engineers such that RF acquisitions can be collected in 3D with the optional high-precision stepper motor.
Data is stored in a pair of non-standard plain text and binary files that contain system settings and raw data respectively with B-mode and saturation image of the scout window for the first frame along with the RF data.
A/D conversion is 12 bit with 71 $dB$ dynamic range, 410 $MS/s$ sampling rate, and 73 $dB$ gain.
Each acquisition consists of 250 beam lines separated by approximately 60 $\mu m$, 2128 samples (3.9 $mm$), and up to 250 frames separated by 200 $\mu m$ to 100 $\mu m$ depending on the length of the plaque specimen.
Some longer plaques may require larger inter-frame spacing because of memory limitations, although the resolution in the elevational direction is nominally 140 $\mu m$ for the RMV710B transducer.

Gross photographic images taken prior to ultrasound scanning, B-mode images derived from the RF, and integrated backscatter (IBS) images for two patients, (C and B) are shown in Figure~\ref{fig:vs_a} and Figure~\ref{fig:vs_b} respectively.
\begin{figure}[h]
  \begin{center}
    \subfigure[Gross photographic image.]{
      \includegraphics[height=4cm]{preliminary_results/figures/pat142_gross_out}
      \label{subfig:a_gross_out}
      }
    \subfigure[Close-up gross image.]{
      \includegraphics[height=4cm]{preliminary_results/figures/pat142_gross_in}
      \label{subfig:a_gross_in}
      }
      \\
    \subfigure[B-mode volume rendering.]{
      \includegraphics[height=6cm]{preliminary_results/figures/pat142_b_mode_volume}
      \label{subfig:a_bmode_v}
      }
    \subfigure[Integrated backscatter volume rendering.]{
      \includegraphics[height=6cm]{preliminary_results/figures/pat142_bsc_volume}
      \label{subfig:a_bsc_v}
      }
      \\
    \subfigure[B-mode scan.]{
      \includegraphics[width=6cm]{preliminary_results/figures/pat142_b_mode_slice}
      \label{subfig:a_bmode_s}
      }
    \subfigure[Integrated backscatter scan.]{
      \includegraphics[width=6cm]{preliminary_results/figures/pat142_bsc_slice}
      \label{subfig:a_bsc_s}
      }
  \end{center}
  \caption[Patient~C \textit{ex vivo} scan.]{
  \flushleft{
  Images of the excised plaque from Patient~C.  
  Slice images are taken from the plane indicated by the white box.  
  A large, diffuse hemorrhagic region shows decreased backscatter.
  }
  }
  \label{fig:vs_a}
\end{figure}
\begin{figure}[h]
  \begin{center}
    \subfigure[Gross photographic image.]{
      \includegraphics[height=4cm]{preliminary_results/figures/pat144_gross_out}
      \label{subfig:b_gross_out}
      }
    \subfigure[Close-up gross image.]{
      \includegraphics[height=4cm]{preliminary_results/figures/pat144_gross_in}
      \label{subfig:b_gross_in}
      }
      \\
    \subfigure[B-mode volume rendering.]{
      \includegraphics[height=6cm]{preliminary_results/figures/pat144_b_mode_volume}
      \label{subfig:b_bmode_v}
      }
    \subfigure[Integrated backscatter volume rendering.]{
      \includegraphics[height=6cm]{preliminary_results/figures/pat144_bsc_volume}
      \label{subfig:b_bsc_v}
      }
      \\
    \subfigure[B-mode scan.]{
      \includegraphics[width=6cm]{preliminary_results/figures/pat144_b_mode_slice}
      \label{subfig:b_bmode_s}
      }
    \subfigure[Integrated backscatter scan.]{
      \includegraphics[width=6cm]{preliminary_results/figures/pat144_bsc_slice}
      \label{subfig:b_bsc_s}
      }
  \end{center}
  \caption[Patient~A \textit{ex vivo} scan.]{
  \flushleft{
  Images of the excised plaque from Patient~A.  
  Slice images are taken from the plane indicated by the white box.  
  The gross photographs in \ref{subfig:b_gross_out} and \ref{subfig:b_gross_in} show a primarily fibrous plaque with some calcified areas.
  Segments from the catheter sheath are seen in the front and back of \ref{subfig:b_bmode_v} and \ref{subfig:b_bsc_v}.
  To reduce saturation from numerous calcified areas, data was collected with -10 dB gain relative to \ref{fig:vs_a}, which explains the larger impact of electronic noise in \ref{subfig:b_bmode_v} and \ref{subfig:b_bmode_s}.
  \ref{subfig:b_bsc_v} and \ref{subfig:b_bsc_s} show the presence of fibrous and calcified areas well.
  }}
  \label{fig:vs_b}
\end{figure}
Patient~C shows a possible high-risk plaque with an extensive hemorrhagic area that may have been the result of recent rupture events.
There were strong indications of inflammation when this plaque was removed. 
The backscatter coefficient is consistently low throughout the hemorrhagic areas.
The result for Patient~B on the other hand, depicts a likely stable plaque with smooth, unulcerated walls and strong fibrous and calcified tissue throughout.
The tip of the flow divider, also known as the tuning fork, can be easily located in these images.
Note that with future software development these images will be augmented with the volumetric slices that are superior and inferior to the displayed images.
Identical dynamic ranges and color transform functions were used in all corresponding images.

IBS images were created with a reference phantom created by Dr. Ernest Madsen from UW-Madison that has been used in IVUS experiments.
This phantom had a reported attenuation of 1.3 $dB/cm/MHz$ and backscatter coefficient of 0.25 $sr^{-1}cm^{-1}$.
The reference phantom was scanned with the same transducer and system settings as utilized for scanning the plaque specimen.
Reference power spectra were obtained by averaging ten lines per plane over 147 planes.
Fourier spectra with 50\% overlap were calculated using a Fast Fourier Transform with 128 Hamming windowed points (240 $\mu m$), and the bandwidth used ranged from 6.6 $MHz$ to 29.6 $MHz$ where the spectrum was flat.
Since the glass beads in the reference phantom had a nominal diameter of 9 $\mu m$, which is much less than the center frequency and scatterers where randomly distributed with a sufficient density, Rayleigh scattering statistics were assumed, i.e. scattering had a form $BSC(f) = Af^4$.
Attenuation in the plaque was assumed to be the same as reference phantom, which is reasonable for arterial plaque specimens from values reported in the literature\cite{Hoskins2007,Lockwood1991}.
The backscatter was calculated using the expression\cite{Liu2007}:
% todo references
\begin{equation}
  BSC_s(f) = \frac{BSC_r(f) S_s(f)}{S_r(f)}
\end{equation}
Log compression and linear interpolation were applied to the displayed IBS in Figure~\ref{fig:vs_a} and Figure~\ref{fig:vs_b}.

\begin{figure}
  \begin{center}
    \subfigure[Histology image.]{
    \includegraphics[height=2.5cm]{preliminary_results/figures/pat143_histology_proximal2}
    \label{subfig:histology}
    }
    \subfigure[IBS image.]{
    \includegraphics[height=2.5cm]{preliminary_results/figures/pat143_bsc_proximal2}
    \label{subfig:bsc_histology}
    }
    \caption[Histology and IBS.]{
    \flushleft{
    Histology, \ref{subfig:histology}, and corresponding IBS, \ref{subfig:bsc_histology}.
    Full 3D imaging of the plaque allows identification of ultrasound images that correspond to histology images that come from isolated planes.
    }}
    \label{fig:histology}
  \end{center}
\end{figure}
Each
acquisition consists of 250 beam lines separated by approximately 60 μm, 2128
samples (3.9 mm), and up to 250 frames separated by 200 μm to 100 μm
depending on the length of the plaque specimen.  For the lengths of the plaques
we examined, which ranged from approximately 20 mm to 40 mm, this filled the
system limit on acquisition.  Resulting files are approximately 150 per
volumetric slice.  Three to five volumetric slices are required to encompass
the majority of an excised plaque's volume.  Some longer plaques may require
larger inter-frame spacing because of memory limitations, although the
resolution in the elevational direction is nominally 140 μm for the RMV710B
transducer.

new images

~~~~~~~~~~
References
~~~~~~~~~~
