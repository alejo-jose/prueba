# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 11:29:56 2020

@author: Alejandro
"""
import numpy as np
f=int(input("Ingrese el numero de filas de la matriz"))
c=int(input("Ingrese el numero de columnas de la matriz"))

x=100*np.random.random((f,c))+1
print("\n"*1)
print("La matriz original es:")
print("\n"*1)
print(x)

print("\n"*2)
print("La diagonal principal es:")
for i in range(f):
    print(x[[i],[i]])
    
print("\n"*1)
print("La diagonal secundaria es:")   
for i in range(c):
    for j in range(c):
        if i+j==f-1:
            print(x[[i],[j]])
            5
            5
            