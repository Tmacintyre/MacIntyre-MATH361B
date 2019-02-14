# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 10:46:00 2019

@author: Tucker MacIntyre
"""


F1 = 1
F0 = 0
N = 30

my_List = [F0, F1]
cat_List = []


for ii in range(N):
    F1 += 1
    x = my_List[F1 - 1] + my_List[F1 - 2]
    my_List.append(x)
    

for ii in range(len(my_List) - 1):
    if my_List[ii]**2 - my_List[ii-1] * my_List[ii + 1] == (-1)**(ii - 1):
        cat_List.append(True)
    
    else:
        cat_List.append(False)




print('The last 15 terms in the sequence are: ' , my_List[-15:])
