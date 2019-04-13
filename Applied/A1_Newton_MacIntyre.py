# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 12:01:38 2019

@author: Tucker MacIntyre
"""

import numpy as np
import math
import mpmath

N = 20
TOL = 1e-4
z0 = 0

#f = lambda x: math.tan(x) - x - 2 
f = lambda x: (x**4/100) + (x**3 * math.e /100) - (x**3/50) - (x**3 * math.sqrt(2)/100) + (x**2 * math.sqrt(2)/50) - (x**2 * math.sqrt(2 * math.e)/100) - (3 * x**2/100) - (x**2 * math.e/50) + (x * math.sqrt(2 * math.e)/50) + (3 * x * math.sqrt(2)/100) - (3 * x * math.e/100) + (3 * math.sqrt(2* math.e)/100)
#fprime = lambda x: -1 + mpmath.sec(x)**2 
fprime = lambda x: (x**3/25) + (3 * math.e * x**2/100) + (math.sqrt(2) * x/25) + (math.sqrt(2 * math.e)/50) + (3 * math.sqrt(2)/100) - (3 * x**2/50) - (3 * math.sqrt(2) * x**2/100) - (math.sqrt(2 * math.e)*x/50) - (3*x/50) - (math.e * x/25) - (3 * math.e/100)

approx = 0
iterations = np.zeros([0,2])

    
for ii in range(1, N + 1):
    z1 = z0 - f(z0)/fprime(z0)
    approx = abs(z1 - z0)
    iterations = np.vstack([iterations, np.array([z1, approx])])
    z0 = z1
    
    
    if(approx < TOL):
        print('Converges after', ii, "iterations with the following results.")
        print(iterations)
        break
    
    if(N == ii):
        print('Reached maximum iterations with no solution.')
        

        

        
        

        


#print(iterations)









#count = np.vstack([count, np.array( [x, len(new_list)])])


