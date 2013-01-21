# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 17:07:04 2013

@author: othane
"""

from scipy import *
from scipy.signal import *

# load the shape file
fname = 'circ8.csv'
rshape = loadtxt(fname, delimiter=',')
x = rshape[:, 3]
y = rshape[:, 4]

# Calc the fd
z = x + sqrt(-1)*y
z -= mean(z) # remove as it contains no shape info
resample(rr, 2**12) # resample so we can compare shapes
Z = fftshift(fft(z)) / len(z)
ZMag = abs(Z)
ZPhs = arctan2(imag(Z), real(Z))
N = len(z)
f = arange(-N/2, N/2, 1);

# Show fd
figure()
subplot(211)
plot(x,y, '.')
subplot(413)
plot(f, ZMag)
subplot(414)
plot(f, ZPhs)