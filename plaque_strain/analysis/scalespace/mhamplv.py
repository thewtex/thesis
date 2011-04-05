#!/usr/bin/env python

import argparse

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

from mpl_toolkits.axes_grid1.inset_locator import mark_inset
from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes

parser = argparse.ArgumentParser( description='Display a MetaImageFile in a Matplotlib figure.' )

#mpl.rcParams['axes.edgecolor'] = 'white'
#mpl.rcParams['axes.labelcolor'] = 'white'
#mpl.rcParams['axes.facecolor'] = 'black'
#mpl.rcParams['figure.facecolor'] = 'black'
#mpl.rcParams['savefig.facecolor'] = 'black'
#mpl.rcParams['xtick.color'] = 'white'
#mpl.rcParams['ytick.color'] = 'white'
#ec="0.8"
ec="0.2"


parser.add_argument( 'input_file', type=argparse.FileType('rb') )
parser.add_argument( '-f', '--figure-size', nargs=2, type=float )
parser.add_argument( '-c', '--cmap', type=str, dest='cmap', default='gray' )
parser.add_argument( '-o', '--output-file', type=str )
parser.add_argument( '-p', '--vmin', type=float, default=None )
parser.add_argument( '-q', '--vmax', type=float, default=None )
parser.add_argument( '-l', '--labelsize', type=float )
parser.add_argument( '-i', '--interpolation', type=str, choices=['nearest',
'bilinear', 'bicubic', 'spline16', 'spline36', 'hanning', 'hamming', 'hermite',
'kaiser', 'quadric', 'catrom', 'gaussian', 'bessel', 'mitchell', 'sinc',
'lanczos'] )
args = parser.parse_args()

if args.figure_size:
    fig = plt.figure( 1, figsize=(args.figure_size[0], args.figure_size[1]) )
else:
    fig = plt.figure(1)

if args.labelsize:
    mpl.rc( 'axes', labelsize = args.labelsize )
    mpl.rc( 'xtick', labelsize = args.labelsize - 2 )
    mpl.rc( 'ytick', labelsize = args.labelsize - 2 )

l = args.input_file.readline()

element_spacing = [1.0, 1.0]
shape = None
offset = [0.0, 0.0]
while l.split('=')[0].rstrip() != 'ElementDataFile':
    l = args.input_file.readline()
    if l.split('=')[0].rstrip() == 'ElementSpacing':
        element_spacing = [ float(x) for x in l.split('=')[1].rstrip().split() ]
    elif l.split('=')[0].rstrip() == 'DimSize':
        shape = [ int(x) for x in l.split('=')[1].rstrip().split() ]
        shape = tuple( shape[::-1] )
    elif l.split('=')[0].rstrip() == 'Offset':
        offset = [ float(x) for x in l.split('=')[1].rstrip().split() ]

#img = np.fromfile( args.input_file, dtype=np.float64 )
img = np.fromfile( args.input_file, dtype=np.int16 )
args.input_file.close()
print( img.shape )
print( shape )
img.shape = shape
#img = img[:,20:-20]
#img = img[9:-9,56:-10]
#img = img.transpose()
shape = img.shape

ax = fig.add_subplot(111)
extent = (offset[0], offset[0] + shape[1]*element_spacing[0],
             offset[1] + shape[0]*element_spacing[1], offset[1])

ax.imshow( img,
        cmap=args.cmap,
        aspect='equal',
        #aspect=element_spacing[0]/element_spacing[1],
        vmin=args.vmin,
        vmax=args.vmax,
        interpolation=args.interpolation,
        origin='lower',
        extent=extent
        )
        #extent=(-offset[1]*1000, (-offset[1] + shape[1]*element_spacing[1])*1000,
             #(shape[0]*element_spacing[0])*1000, 0.0) )
             #(offset[0] + shape[0]*element_spacing[0])*1000, offset[0]*1000) )


plt.xlabel( 'Width [mm]' )
plt.ylabel( 'Depth [mm]' )
class cbFormatter( mpl.ticker.ScalarFormatter ):

    def __call__( self, x, pos=None ):
        return '{0}'.format( 100.* x )

#cb_formatter = cbFormatter()
##cb = plt.colorbar( ticks=[-0.03, -0.02, -0.01, 0.0], format=cb_formatter,
#cb = plt.colorbar( format=cb_formatter,
    #shrink=0.8, drawedges=False )
##cb = plt.colorbar( shrink=0.8, drawedges=False )
#cb.outline.set_marker( '' )
#cb.set_label( 'Strain [%]' )

axins = zoomed_inset_axes(ax, 4, loc=1)
axins.imshow(img, extent=extent, origin='lower',
        vmin = args.vmin,
        vmax = args.vmax,
        interpolation = args.interpolation,
        cmap = args.cmap,
        aspect='equal')

x1, x2, y1, y2 = 10.0, 15.0, 30.0, 25.0
axins.set_xlim(x1, x2)
axins.set_ylim(y1, y2)

plt.xticks(visible=False)
plt.yticks(visible=False)

mark_inset(ax, axins, loc1=2, loc2=4, fc='none', ec=ec)

if args.output_file:
    plt.savefig( args.output_file, dpi=150 )
else:
    plt.show()
