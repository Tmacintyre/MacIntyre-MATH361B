# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 22:00:56 2019

@author: Tucker MacIntyre
"""
 #note: takes a few swconds to compute

def Goldconj(): #checks conjecture until we find the odd composite nu ber that proves false
    n = 2
    while True:
        if n % 2 == 1 and not primes(n): #if not a prime number and is odd
            answer = False
            for ii in range(2, n):
                if primes(ii):
                    for jj in range(1, n): #for loop that tests the conjecture
                        if n == ii + 2 * jj * jj: #conjecture
                            answer = True
                            break
                    if answer:
                        break
            if not answer: # for loop that prints statement and breaks all loops once the conjecture proves false
                print("The first number that proves this conjecture false is: ", n)
                break
        n += 1 # count to cycle through nymbers
        
        
def primes(n): #checks number to determine if prime 
    if n > 1:
        for i in range(2, n):
            if (n % i) == 0:
                return False
    return n > 1



Goldconj()