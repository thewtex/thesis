#log# Automatic Logger file. *** THIS MUST BE THE FIRST LINE ***
#log# DO NOT CHANGE THIS LINE OR THE TWO BELOW
#log# opts = Struct({'__allownew': True, 'logfile': 'plot_frame_skip.py', 'pylab': 1})
#log# args = []
#log# It is safe to make manual edits below here.
#log#-----------------------------------------------------------------------
_ip.magic("logstart plot_frame_skip.py")

_ip.system("ls -F ")
a = np.loadtxt('pat157lefticalongcont_20100111092227_Cycle1_Version_4fa483a_SkipSequence.csv', delimiter = ',' )
a
skip = a[1:,0,0] - a[:-1,0,0]
a.shape
skip = a[1:,0] - a[:-1,0]
plot( a[:-1,0], skip )
plt.ylim(0, 7)
plt.xlabel( 'Frame number' )
plt.ylabel( 'Frame skip [frames]' )
plt.savefig( '../../images/frame_skip.png', dpi=150 )
