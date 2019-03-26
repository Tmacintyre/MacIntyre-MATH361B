# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 04:36:23 2019

@author: Tucker MacIntyre
"""

m = 8 # set to which Z sub m you would like to work in 
multInv = []

    

for ii in range (1, m ):
    for jj in range(1, m ):
        possible = ii * jj
        if possible % m == 1:
            multInv.append(jj)
            break
        

print("All of the elements which have a multiplicative inverse for Integer Modulus", m, "are:", multInv, ", which gives a total of", len(multInv),"elements.")
