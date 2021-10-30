# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 12:38:21 2020

@author: Alejandro
"""


matrix=[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]




for i in range (0,5):
    for j in range (0,6):
        print( "ingrese posicion " ,i,j)
        matrix[i][j]=int(input())
print(matrix)