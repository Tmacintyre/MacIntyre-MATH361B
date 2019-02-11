# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 01:30:41 2019

@author: Tucker MacIntyre
"""
import numpy as np

N = 25000

x = np.zeros(N)
y = np.zeros(N)
z = np.zeros(N)
a = 1
b = 1
c = 1


for ii in range(2, N):
    x[ii] = ((ii**3) - 1)/ ((ii**3) + 1)
    a = x[ii] * a
    x[ii] = a
    
    
for ii in range(1, N):
    y[ii] = np.exp(ii/100) / (ii**10)
    b = y[ii] * b
    y[ii] = b
    
    
    z[ii] = (5 * (3 + ii**2))/ (3 + ii)
    c = z[ii] * c
    z[ii] = c
        
    
    
    
print(' The first 15 terms of the first sequence are: ', x[1:16])
print()
print(' While the last 15 terms of the first sequence are: ', x[-15:])
print()
print()
print(' The first 15 terms of the second sequence are: ', y[1:16])
print()
print(' While the last 15 terms of the second sequence are: ', y[-15:])
print()
print()
print(' The first 15 terms of the third sequence are: ', z[1:16])
print()
print(' While the last 15 terms of the third sequence are: ', z[-15:])
