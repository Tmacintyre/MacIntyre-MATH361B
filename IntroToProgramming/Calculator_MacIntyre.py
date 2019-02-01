# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 22:27:02 2019

@author: Tucker MacIntyre
"""
# Enter number for each variable: x, y, z
x = 1
y = 2
z = 3

#List containing 5 elements to alter, could have also just created an empty list
numList = [0,0,0,0,0]

numList[0] = x + y
numList[1] = (y * z) + (3 * x)
numList[2] = numList[0]**2
numList[3] = ((2 * numList[1]) -  (x / 2)) / numList[0]
numList[4] = 7 % 3
numList[2] = numList[2] + 3
numList[4] = numList[4] * (3 / 4)
totalSum = sum(numList)

#rounded to 2 decimal points
print('The sum of all elements in the list is: ' + str("%0.2f" % (totalSum)))