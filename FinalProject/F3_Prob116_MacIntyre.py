# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 10:46:00 2019

@author: Tucker MacIntyre
"""

N = 14 #Total number of spaces
red = 2 #Length of red tiles
green = 3 #Length of green tiles
blue = 4 #Length of blue tiles


def reds():
    amount = [1] * 2 + [0] * (N - red + 1)
    for ii in range(red, N + 1):
        amount[ii] += amount[ii - 1] + amount[ii - red]
    return amount[N] - 1

def greens():
    amount = [1] * 3 + [0] * (N - green + 1)
    for ii in range(green, N + 1):
        amount[ii] += amount[ii - 1] + amount[ii - green]
    return amount[N] - 1



def blues():
    amount = [1] * 4 + [0] * (N - blue + 1)
    for ii in range(blue, N + 1):
        amount[ii] += amount[ii - 1] + amount[ii - blue]
    return amount[N] - 1
    


print("The total number of ways to fill the spaces with red tiles are:", reds())
print()
print("The total number of ways to fill the spaces with green tiles are:", greens())
print()
print("The total number of ways to fill the spaces with blue tiles are:", blues())
print()
print("The total number of ways to fill the spaces in total are:", reds() + greens() + blues())
