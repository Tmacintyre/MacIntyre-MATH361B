# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 13:29:28 2019

@author: Tucker MacIntyre
""" 

def divisors(N): #checks integer set to n for proper divisors
    i = 1 # used as a count and to check integers greater then 0 and less than n
    divList = []
    while i < N:
        if N % i == 0:
            divList.append(i)
        i += 1
    
    return sum(divList)



N = 2500  # change to which integer you would like to get proper divisors for
amicableList = []

for a in range(1,N + 1):
    b = divisors(a)
    
    if divisors(b) == a and divisors(a) == b:
        amicableList.append(a)

    

print('All the amicable numbers up to the upper bound of', N, 'are', amicableList)