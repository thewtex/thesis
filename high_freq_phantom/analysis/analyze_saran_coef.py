#!/usr/bin/env python
# Matt McCormick (thewtex)
# created 2008 March 28

from pylab import *

from common.parse_sample_set import parse_sample_set
from attenuation.saran_transmission_coef import saran_transmission_coef as stc
from attenuation.water_reference_method import saran_theoretical_trans_coef as sttc

#water = parse_sample_set()

noise_pts = 300;  # number of points at the start of the signal that are considered only noise
trans_coefs = []
#for i in xrange( len(water)):
  #setting_trans_coefs =[]
  #setting_freqs = []
  #for j in xrange( len(water[i]) ):
    
    #info = water[i][j]

    #water_meta = info[0][0]
    #water_data = info[0][1]
    #water_data = water_data - mean( water_data[:noise_pts] )

    #print water_meta['sample name'], ': ', water_meta['settings'], ' freq: ', water_meta['freq'], ' [Hz]'

    #sample_meta = info[1][0]
    #sample_data = info[1][1]
    #sample_data = sample_data - mean( sample_data[:noise_pts] )

    #tc = stc(water_meta, water_data, sample_meta, sample_data )
    
    #setting_trans_coefs.append( tc )
    #setting_freqs.append( sample_meta['freq'] )

  #trans_coefs.append( (setting_freqs, setting_trans_coefs) )


figure(1)
plt.clf()
#freqs = array(trans_coefs[0][0])
#plot( freqs/10**6, array(trans_coefs[0][1]), 'rs', label='function generator=600 [mV]')
#plot( freqs/10**6, array(trans_coefs[1][1]), 'co', label='function generator=300 [mV]')
xlabel('Frequency [MHz]')
ylabel('Transmission Coefficient')
#title('Saran Wrap Transmission Coefficient')


freqs = arange(15.0e6, 55.0e6, 1.0e6)
theoretical = sttc( freqs, 1.488e6, l_saran=25.0e-6 )
#plot( freqs/10**6, theoretical**0.5 , 'g--', label='theoretical, Wear et al 2005')

freqs = arange(15.0e6, 55.0e6, 1.0e6)
theoretical = sttc( freqs, 1.488e6, l_saran=12.2e-6 )
#plot( freqs/10**6, theoretical**0.5 , label='l = 12 micrometers')
plot( freqs/10**6, theoretical**0.5, 'g--', linewidth=3 )


#freqs = arange(15.0e6, 55.0e6, 1.0e6)
#theoretical = sttc( freqs, 1.488e6, l_saran=23.0e-6 )
#plot( freqs/10**6, theoretical**0.5 , label='l = 23 micrometers')

#freqs = arange(15.0e6, 55.0e6, 1.0e6)
#theoretical = sttc( freqs, 1.488e6, c_saran=2500.0 )
#plot( freqs/10**6, theoretical**0.5 , label='c_saran = 2500.0 micrometers')

#freqs = arange(15.0e6, 55.0e6, 1.0e6)
#theoretical = sttc( freqs, 1.488e6, rho_saran=1.8e3 )
#plot( freqs/10**6, theoretical**0.5 , label='rho_sara = 1.8 g/cc ')


#freqs = arange(15.0e6, 55.0e6, 1.0e6)
#theoretical = sttc( freqs, 1.488e6, alpha_a=7.0 )
#plot( freqs/10**6, theoretical**0.5 , label='alpha_a = 7.0 neper / m')

#freqs = arange(15.0e6, 55.0e6, 1.0e6)
#theoretical = sttc( freqs, 1.488e6, alpha_n=1.8 )
#plot( freqs/10**6, theoretical**0.5 , label='alpha_n = 1.8 ')

#l = legend( loc='upper left', shadow=True )
#ltext = l.get_texts()
#setp(ltext, fontsize='small')
axis(xmin=10, xmax=55)

#plt.show()
savefig('../images/saran_trans_coef.png', dpi=150)
savefig('../images/saran_trans_coef.eps')

