# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 12:55:59 2019

@author: Tucker MacIntyre
"""

n = 182  # change to which integer you would like to get proper divisors for

def divisors(n): #checks integer set to n for proper divisors
    i = 1 # used as a count and to check integers greater then 1 and less than n
    divList = []
    while i < n:
        if n % i == 0:
            divList.append(i)
        i += 1
    return divList


print('All of the proper divisors of the integer', n, 'are:', divisors(n))