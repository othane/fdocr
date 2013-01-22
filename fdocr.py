# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 17:07:04 2013

@author: othane
"""

from scipy import *
from scipy.signal import *

def calcfd(x, y):
    # pass in the raw shape x and y data and return Z 
    # the fourier descriptor of x and y [Z]
    z = x + sqrt(-1)*y
    z -= mean(z) # remove as it contains no shape info
    resample(z, 2**12) # resample so we can compare shapes
    Z = fftshift(fft(z)) / len(z)
    Zmag = abs(Z)
    Zphs = arctan2(imag(Z), real(Z))
    N = len(z)
    f = arange(-N/2, N/2, 1);
    return f, Z, Zmag, Zphs

    
def plot_shape(x, y):
    # get the fd for this shape
    f, Z, Zmag, Zphs = calcfd(x, y)
    # Show fd
    figure()
    subplot(211)
    plot(x,y, '.')
    subplot(413)
    plot(f, Zmag)
    subplot(414)
    plot(f, Zphs)    
    
    
def load_shape(fname):
    rshape = loadtxt(fname, delimiter=',')
    x = rshape[:, 3]
    y = rshape[:, 4]    
    return x, y

# scripts
x,y = load_shape('data/cross0.csv')
plot_shape(x,y)



