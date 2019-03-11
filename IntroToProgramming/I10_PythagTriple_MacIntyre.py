# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 12:08:59 2019

@author: tucker
"""

#takes a minute to compute

import numpy as np
my_array = np.zeros([0,4])


N = 1003

for a in range(N-1):
    for b in range(a+1,N):
        for c in range(b+1, N+1):
            if a*a + b*b == c*c:
                my_array = np.vstack([my_array, np.array( [a, b, c, a + b + c])])
            if(a*a + b*b == c*c and a + b + c == 1026):
                print("The pythagorean triples that sum to 1026 are:", a, b, c)
                break
            
# Takes a minute to compute 