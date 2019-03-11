# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 12:22:13 2019

@author: tucker
"""

import numpy as np


a = 1
N = 100
n = 1 #larger than zero to avoid division by zero
b = 2
x = np.zeros(N)

a_n = lambda n: n**2 + 9*n - 7
#a_n = lambda n: 1 + ((1 + n**5)/(1 + n**2))
#a_n = lambda n: 1 + b**n # b must be larger than zero

for ii in range(N):
    x[ii] = a_n(n)
    a = x[ii] * a
    x[ii] = a
    n+=1
    m+=1

print(' The last 15 terms of the sequence are: ', x[-15:])






#%%

