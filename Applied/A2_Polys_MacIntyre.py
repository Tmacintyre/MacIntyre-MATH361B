# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 15:50:56 2019

@author: Tucker MacIntyre
"""

import math

p = [4,-8,0,2,-9] # my polynomial is set up exactly how the polynomial is in your instructions. p(x) = 4x**2 - 8x**3 + 2x - 9
x = 2 # set to the given point you would like for calculations
a = 2 # the lower limit for the definate integral
b = 7 # the upper limit for the definate integral

def poly(lists,x): # Evaluates the polynomial at a given (x)
    sums = 0
    exp = len(p) - 1
    for ii in range(0,len(p)):
        while(exp > 0):
            sums = sums + (p[ii] * math.pow(x,exp))
            break
        exp = exp - 1
    sums = sums + p[ii]
    print("The value of the polynomial at p(x) is equal to:",sums)
    
    
def deriv(): # Calculates the derivitive of supplied polynomial at a given point (x), used instead of 'c'
    ith = len(p) - 1
    derivpoly = []
    for ii in range(0,len(p)):
        derivpoly.append((p[ii] * ith) * x**(ith - 1))
        ith -= 1
    print("The derivative of the polynomial evaluated at p(x) is equal to:", sum(derivpoly))
    
    

def integral(): # Calculates the definate integral of the polynomial from a to b.
    ith = len(p)
    integb = []
    intega = []
    for ii in range(0, len(p)):
        integb.append((p[ii] / ith) * b**(ith))
        intega.append((p[ii] / ith) * a**(ith))
        ith -= 1
        
    print("The definite integral of the polynomial from", a, "to", b, "is equal to:",sum(integb) - sum(intega))
    
    
    
    
poly(p,x)
print()
deriv()
print()
integral()
