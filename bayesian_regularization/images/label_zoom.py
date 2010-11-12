#!/usr/bin/env python

import matplotlib as mpl
import matplotlib.pylab as plt
import numpy as np

import Image

import sys

mpl.rc( 'axes', linewidth= 2.0,
        labelsize= 26.0,
       titlesize= 20.0 )
mpl.rc( 'xtick', labelsize= 20.0 )
mpl.rc( 'ytick', labelsize= 20.0 )
mpl.rcParams['xtick.major.size'] = 5
mpl.rcParams['xtick.minor.size'] = 4
mpl.rcParams['ytick.major.size'] = 5
mpl.rcParams['ytick.minor.size'] = 4
mpl.rc( 'savefig', dpi= 150 )

if len( sys.argv ) < 2:
    print( 'usage: ' + sys.argv[0] + '  input_image.png' )
    sys.exit()

fig = plt.figure( figsize=(7, 7) )
img = Image.open( sys.argv[1] )
imsh = plt.imshow( img, cmap=mpl.cm.jet, origin='lower', extent=(0.0, 2.4, 0.0, 2.4) )
ax = imsh.get_axes()
ticks = [x for x in np.arange(0.5, 2.4, 0.5)]
ax.set_xticks( ticks )
ax.set_yticks( ticks )
ax.set_xlabel( 'Width [mm]' )
ax.set_ylabel( 'Height [mm]' )
plt.savefig( sys.argv[1][:-4] + '_labels.png' )

#plt.show()
