import os
import sys

sys.path.append( '/home/matt/rs/progs' );

import numpy as np
from matplotlib import pyplot as plt
import matplotlib as mpl

sys.path.insert( 0, os.path.abspath( os.path.join( __file__, '..', '..' )))
import common.figure_settings as fs

mpl.rc( 'lines', linewidth=2.0,
        markersize=3 )

from sos_atten.common.average_trials import average_trials

examples = { '20MHz_water':
        ('/home/matt/rs/data/phantoms/ivus_phantom/speed_of_sound_attenuation/20090320/13Nov08TMBlood/13Nov08TMBlood-Water-20.00-',
            ( 41.9, 44.0 ),
            ( -50.0, 50.0 ) ),
    '40MHz_water': ('/home/matt/rs/data/phantoms/ivus_phantom/speed_of_sound_attenuation/20090320/13Nov08TMBlood/13Nov08TMBlood-Water-40.00-',
            ( 41.9, 44.0 ),
            ( -300.0, 300.0 ) ),
    '20MHz_sample': ('/home/matt/rs/data/phantoms/ivus_phantom/speed_of_sound_attenuation/20090320/13Nov08TMBlood/13Nov08TMBlood-Sample-20.00-',
            ( 41.9, 44.0 ),
            ( -50.0, 50.0 ) ),
    '40MHz_sample': ('/home/matt/rs/data/phantoms/ivus_phantom/speed_of_sound_attenuation/20090320/13Nov08TMBlood/13Nov08TMBlood-Sample-40.00-',
            ( 41.9, 44.0 ),
            ( -300.0, 300.0 ))
    }

for e, d in examples.items():
    meta, data = average_trials( d[0] )
    time = ( meta['horizontal offset'] + np.arange( len( data ) ) * meta['sampling interval'] ) * 10**6

    fig = plt.figure( 1, figsize=( 8, 6 ))
    fig.clf()
    ax = fig.add_subplot( 111 )
    ax.plot( time, data*10**3 )
    ax.set_xlim( d[1] )
    ax.set_ylim( d[2] )
    ax.set_xlabel( 'Time [$\mu s$]' )
    ax.set_ylabel( 'Voltage [$mV$]' )

    fig.savefig( '../../doc/images/substitution_pulse_' + e + '.eps', dpi=150 )
    fig.savefig( '../../doc/images/substitution_pulse_' + e + '.png', dpi=150 )

