#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 09:16:33 2021

@author: Josey
"""
#to move from the start to the end, the matrix will shrink whenever it moves a space to the
#right or down eg: 4x4 matrix > 4x3 when it moves right > 3x4 if it moves down 
#m = row | n = col
#define paths by (m-1,n) if travelling R and (m,n-1) if travelling down 
#set condition to break if: 
    #a) m=1 or n=1 since 1x1 matrix means either the start or the end
    #b) m or n = 0
#math is to use brute force
#eg: 1 + 1 (move right) or 1 + 2 (move down)
#unable to solve this question 

import numpy as np 
def findpath(m,n, path, matrix):
    if(m == 1 or n == 1):return 1
    if(m == 0 or n == 0 ):return 0
    
    (a,b) = (len(matrix), len(matrix[0]))
    if(a == m-1 and b == n-1):
        print(path + matrix[a][b])
        return
        # include the current cell in the path
    path.append(matrix[a][b])
 
    # move right
    if (0 <= a < m and 0 <= b + 1 < n):
        findpath(matrix, path, a, b + 1)
        print('R')
 
    # move down
    if (0 <= a + 1 < m and 0 <= b < n):
        findpath(matrix, path, a + 1, b)
        print('D')
 
    #remove the current cell from the path
    path.pop()
    

if __name__ == '__main__':
    matrix = np.zeros((4,4)) #create matrix
    values = [1,2,3,4] 
    # matrix[0,:] = '1'
    # matrix[1,:] = '2'
    # print(matrix)
    for i, value in enumerate(values):
        matrix[i] = [value]*len(matrix[i])
    print(matrix)
    path = []
    m = n = 0
    findpath(m,n,path,matrix)
    
