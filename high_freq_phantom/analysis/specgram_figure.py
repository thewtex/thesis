import os
import sys

sys.path.append( '/home/matt/rs/progs' );

import numpy as np
from matplotlib import pyplot as plt
import matplotlib as mpl
from matplotlib import mlab

sys.path.insert( 0, os.path.abspath( '/home/matt/rs/progs/sos_atten' ))

mpl.rc( 'lines', linewidth=3.0,
        markersize=10 )
mpl.rc( 'font', size= 6.0 )
mpl.rc( 'axes', linewidth= 2.0,
        labelsize= 18.0,
        titlesize= 20.0 )
mpl.rcParams['axes.formatter.limits'] = (-4,4)
mpl.rc( 'xtick', labelsize= 16.0 )
mpl.rc( 'ytick', labelsize= 16.0 )
mpl.rcParams['xtick.major.size'] = 5
mpl.rcParams['xtick.minor.size'] = 4
mpl.rcParams['ytick.major.size'] = 5
mpl.rcParams['ytick.minor.size'] = 4

mpl.rc( 'savefig', dpi= 150 )

#mpl.rc( 'image', cmap=mpl.cm.gray )

mpl.rc( 'legend', fontsize=16.0 )

mpl.rc( 'lines', linewidth=2.0,
        markersize=3 )

from sos_atten.common.average_trials import average_trials

filename = '/home/matt/rs/data/phantoms/ivus_phantom/speed_of_sound_attenuation/20090320/13Nov08TMBlood/13Nov08TMBlood-Water-40.00-'
time_range =      ( 41.9,   44.0 )
amplitude_range = ( -300.0, 300.0 )

meta, data = average_trials( filename )
time = ( meta['horizontal offset'] + np.arange( len( data ) ) * meta['sampling interval'] ) * 10**6

figsize = (12, 6 )
fig = plt.figure( 1, figsize=figsize)
fig.clf()
ax = fig.add_subplot( 111 )
ax.plot( time, data*10**3 )
ax.set_xlim( time_range )
ax.set_ylim( amplitude_range )
ax.set_xlabel( 'Time [$\mu s$]' )
ax.set_ylabel( 'Voltage [$mV$]' )
fig.savefig( '../images/spectrogram_time_signal' + '.eps', dpi=150 )
fig.savefig( '../images/spectrogram_time_signal' + '.png', dpi=150 )

Pxx, freqs, t = mlab.specgram( data, NFFT=64,
    Fs=1./(meta['sampling interval']*10**6), noverlap=32, pad_to=512 )
offset = meta['horizontal offset'] * 10**6
plt.figure(2, figsize = figsize)
plt.imshow( Pxx, aspect='auto', extent=(offset + t[0], offset + t[-1],
    freqs[-1], freqs[0]))
plt.xlabel( 'Time [$\mu s$]' )
plt.ylabel( 'Frequency [MHz]' )
plt.ylim( 0, 60.0 )
plt.xlim( time_range )
#plt.colorbar(orientation='horizontal' )
#plt.show()

plt.savefig( '../images/spectrogram' + '.eps', dpi=150 )
plt.savefig( '../images/spectrogram' + '.png', dpi=150 )
