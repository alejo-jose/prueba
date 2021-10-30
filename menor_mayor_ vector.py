# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 15:06:20 2020

@author: Alejandro
"""


import numpy as np

z=int(input("Ingrese la dimension del vector"))

x=np.random.random((z))
print("El vector original es ",x)

a=False

while a==False:
    a=True
    for i in range(len(x)-1):
        if x[i] > x[i+1]:
            b=x[i]
            x[i]=x[i+1]
            x[i+1]=b
            a=False
print("El vector ordenado es ",x)