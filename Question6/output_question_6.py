#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 22:11:48 2021

@author: Josey
"""
# shapely library allows manipulation and analysis of geometrical object
from shapely.geometry import Polygon, Point

# #creat points
# points = [(7,11),(10,14),(11,4),(12,21),(16,3),(16,10),(17,4),(18,7),(18,17),(20,7)]

 #create polygon (insert the coordinates from input file)
coord = [(4,3),(2,6),(3,12),(2,17),(5,20),(9,21),(14,19),(20,14),(18,3),(11,7)] 
poly = Polygon(coord) #contructs the polygon 

# #check polygon
# # print(poly)

# # print(p1)
# # print(point2)
# # print(point3)

# for p in range(points):
#     if poly.contains(points):
#         print(points + 'inside')
#     else: print(points + 'outside')

#create points (coordinates from input file) 
p1 = Point(7,11)
p2 = Point(10,14)
p3 = Point(11,4)
p4 = Point(12,21)
p5 = Point(16,3)
p6 = Point(16,10)
p7 = Point(17,4)
p8 = Point(18,7)
p9 = Point(18,17)
p10 = Point(20,7)

#poly.contains() checks if the polygon contains the chosen point within it
if poly.contains(p1):
    print('7 11 inside')
else: 
    print('7 11 outside')

if poly.contains(p2):
    print('10 14 inside')
else: 
    print('10 14 outside')
    
if poly.contains(p3):
    print('11 4 inside')
else: 
    print('11 4 outside')
    
if poly.contains(p4):
    print('12 21 inside')
else: 
    print('12 21 outside')
    
if poly.contains(p5):
    print('16 3 inside')
else: 
    print('16 3 outside')
    
if poly.contains(p6):
    print('16 10 inside')
else: 
    print('16 10 outside')
    
if poly.contains(p7):
    print('17 4 inside')
else: 
    print('17 4 outside')
    
if poly.contains(p8):
    print('18 7 inside')
else: 
    print('18 7 outside')
    
if poly.contains(p9):
    print('18 17 inside')
else: 
    print('18 17 outside')
    
if poly.contains(p10):
    print('20 7 inside')
else: 
    print('20 7 outside')
