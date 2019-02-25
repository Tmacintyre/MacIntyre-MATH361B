# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 12:04:11 2019

@author: tucker
"""
n = 10  # Input a number to figure out the nth prime number
N = 300
primelist = [2]


def prime_check(x):
    if(x==2):
        return True
    if(x % 2 == 0):
        return False

    count = 2
    while(count < x**.5 + 1):
        if (x % count == 0):
            return False
        count += 1
    return True


for x in range(3, N+1):
    if prime_check(x) == True:
        primelist.append(x)
    else:
        False



print("The", n,"th prime number is: ", primelist[n - 1])