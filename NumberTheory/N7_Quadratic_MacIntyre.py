# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 23:46:31 2019

@author: Tucker MacIntyre
"""
import numpy as np
count = np.zeros([0, 2])
neg_one = np.zeros([0, 2])
P = 80

def primes(n): #checks number to determine if prime 
    if n > 1:
        for i in range(2, n):
            if (n % i) == 0:
                return False
    return n > 1



for x in range(3, P):
    if primes(x) == True:
        new_list = []
        for ii in range( 1, x):
            y = ii % x
            for kk in range(1, x):
                if( kk**2 % x == y):
                    if (y not in new_list):
                        new_list.append(y)
        count = np.vstack([count, np.array( [x, len(new_list)])])
        
    else:
        False
        
for x in range(3, P):
    if primes(x) == True:
        for ii in range( 1, x ):
            if(ii**2 % x  == x - 1):
                neg_one = np.vstack([neg_one, np.array( [x, 'True'])])
                break
                
        else:
            neg_one = np.vstack([neg_one, np.array( [x, 'False'])])
                        
            
                

    else:
        False
        
        


        

    
    

print('The numbers to the left are the prime numbers up to P, while the numbers to the right are the number of quadratic residues that each prime has:')
print(count)
print()
print()
print()
print('The numbers to the left are the prime numbers up to P, while the right portion tells you whether or not -1 is a residue for the aligned prime:')

print(neg_one)
