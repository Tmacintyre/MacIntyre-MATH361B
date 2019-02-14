# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 20:54:32 2019

@author: tucke
"""



F0 = 0
F1 = 1
N = 100
m = 6
mult_List = []
my_List = [F0, F1]

for ii in range(N):
    
    F1 += 1
    x = my_List[F1 - 1] + my_List[F1 - 2]
    my_List.append(x)
    
    if x % m == 0:
        mult_List.append(x)
        
        
    
print('All of the terms that are divisible by ' , m, ' are: ' ,mult_List)
