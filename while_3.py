# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 12:22:07 2020

@author: Alejandro
"""


while True:
    x=input("Ingrese el numero de veces que contare: ")
    if x >='0':
        break
x=int(x)
y=1
while True:
    print(y,end=" ")
    y=y+1
    if y>x:
        break