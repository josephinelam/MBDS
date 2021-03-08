#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 17:51:41 2021

@author: Josey
"""
#part a
import numpy as np 
import sys
from itertools import cycle, islice

np.set_printoptions(threshold =  sys.maxsize)
l = np.zeros((5,5),str) #5x5 array of zeros
#print(l)
# ll = [0,5]*5
# ll

ll = list(islice(cycle(['R', 'B']), 5)) #repeat the 'r' and 'b' alternatively in a row of 5
#print(ll)

for i in range(5):
    l[i,:] = ll
    ll = ll[1:] + [ll[1]] #push 'r' back one 'space'

print(l)


#part b
# firstly, fill all 1451 Blue beads in alternatively eg [B 0 B 0 B 0 B]
# then fill all 1072 White beads ag: [B W B W B W B]
# fill up all the beads starting from the largest amount to the least 
# in the following order blue > white > green > yellow > red
# always fill them in alternative space 
# the combination should lead to 0 penalty 

## ====================================================
## b = np.zeros((64,64), str)
## print(b)

## bb = list(islice(cycle(['B','W','G','Y','R']),64))

## for j in range(64):
##     b[j,:] = bb
##     bb = bb[1:] + [bb[1]]
    
## print(b)
