#log# Automatic Logger file. *** THIS MUST BE THE FIRST LINE ***
#log# DO NOT CHANGE THIS LINE OR THE TWO BELOW
#log# opts = Struct({'__allownew': True, 'logfile': 'displacement_plot.py', 'pylab': 1})
#log# args = []
#log# It is safe to make manual edits below here.
#log#-----------------------------------------------------------------------
_ip.magic("run ./mhamplv.py pat157lefticalongcont_20100111092227_Cycle0_Version_4fa483a_DisplacementVectorSequenceComponent1Frame8.mha")
figure(2)
img.shape
_ip.magic("logstart displacement_plot.py")

_ip.magic("run ./mhamplv.py pat157lefticalongcont_20100111092227_Cycle0_Version_4fa483a_DisplacementVectorSequenceComponent1Frame8.mha")
figure(3)
img.shape
depth = np.linspace( 0.0, 35.0, 100 )
depth
plot( depth, img[:,20] )
plt.xlabel('Depth [mm]')
plt.ylabel('Axial Displacement [mm]')
#?plt.savefig
plt.savefig( '../../../images/lsq_vessel_displacement_plot.png', dpi=150 )
