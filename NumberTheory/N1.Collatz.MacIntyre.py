# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 20:51:43 2019

@author: Tucker MacIntyre
"""
a0 = 6    #set to first term wanted 
N = 100   #set to the total number of terms to compute in sequence
my_List = []


def collatzConj(a0):
    for ii in range(N):
        #while a0 != 1: use instead of for loop if not using an N variable
            if a0 % 2 == 0:
                a0 = a0/2
                my_List.append(int(a0))
            else:
                a0 = 3*a0+1
                my_List.append(int(a0))
            
            if my_List[ii] == 1:
                break # breaks for loop early if returns to 1
                
    if a0 != 1:
        print("You did not reach 1 after", N + 1, "terms.")
        
    else:
        print("It took", len(my_List)+1, "terms to reach 1.")
            
            
collatzConj(a0)

print("The initial term was", a0 , "while the following terms were:", my_List)   
