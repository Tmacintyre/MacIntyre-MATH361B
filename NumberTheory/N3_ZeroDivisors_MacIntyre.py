# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 02:18:58 2019

@author: Tucker MacIntyre
"""

m = 20 # set to which Z sub m you would like to work in 
zeroDivs = []

    

for ii in range (1, m ):
    for jj in range(1, m ):
        possible = ii * jj
        if possible % m == 0:
            zeroDivs.append(ii)
            break
        

print("All of the zero divorsors for Integer Modulus", m, "are:", zeroDivs, " which gives a total of", len(zeroDivs),".")
