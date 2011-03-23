#!/usr/bin/python

import numpy as np

results_file = 'invivo_results_sorted.csv'

ids = np.loadtxt(results_file, usecols=(0,), delimiter=',',
    dtype=np.dtype('S64'))

strain_types = ['MaxAbsPrincipalStrain',
        'MaxShearStrain',
        'DistortionalEnergy',
        'TotalStrainEnergy',
        'LateralStrain',
        'ShearStrain',
        'AxialStrain']

measures = ['Peak-to-peak mean',
    'Peak-to-peak 90th percentile',
    'Peak-to-peak std. dev.',
    'Sum of absolute derivative mean',
    'Sum of absolute derivative 90th percentile',
    'Sum of absolute derivative std. dev.']

col_start = 1
for s in strain_types:
    with open(s + '.csv', 'w') as f:
        f.write('ROI identification, ')
        for m in measures[:-1]:
                f.write(m + ', ')
        f.write(measures[-1] + '\n')
        a = np.loadtxt(results_file, usecols=np.arange(col_start, col_start + 6),
                delimiter=',')
        for i in range(a.shape[0]):
            f.write(ids[i].strip().replace('_', ' ') + ', ')
            for j in range(a.shape[1] - 1):
                f.write('{0:.3}'.format(a[i,j]) + ', ')
            f.write('{0:.3}'.format(a[i,a.shape[1] - 1]) + '\n')

    col_start += 6

