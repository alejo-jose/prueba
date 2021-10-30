# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 11:10:45 2020

@author: Alejandro
"""

x=input("Ingrese el numero de veces que contare: ")
x=int(x)
y=1
z=0
while y <=x:
    print(y,end=" ")
   
    z=z+y
    y+=1
u=(z/x)         
print("\n"*2)    
print("La suma de los numeros es: ",z)
print("El promedio es: ",u)