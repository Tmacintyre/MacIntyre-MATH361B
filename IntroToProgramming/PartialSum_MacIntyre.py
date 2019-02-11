# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 00:40:31 2019

@author: Tucker MacIntyre
"""

import numpy as np


N = 60000
x = np.zeros(N)
y = np.zeros(N)
z = np.zeros(N)
a = 0
b = 0
c = 0



for ii in range(1, N):
   x[ii] = (np.log(ii**4 + ii +3)) / (np.sqrt(ii) +3)
   a = x[ii] + a
   x[ii] = a
   
   y[ii] = (np.exp(ii / 100)) / ii**(10)
   b = y[ii] + b
   y[ii] = b
   
   z[ii] = (3 * ii) / (5**(ii + 1))
   c = z[ii] + c
   z[ii] = c
   
   

   
    
print(' The first 15 terms of the first sequence are: ', x[1:16])
print()
print('While the last 15 terms of the first sequence are: ', x[-15:])
print()
print()
print(' The first 15 terms of the second sequence are: ', y[1:16])
print()
print('While the last 15 terms of the second sequence are: ', y[-15:])
print()
print()
print(' The first 15 terms of the third sequence are: ', z[1:16])
print()
print('While the last 15 terms of the third sequence are: ', z[-15:])

