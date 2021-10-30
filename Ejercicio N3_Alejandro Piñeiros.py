# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 15:15:46 2020

@author: Alejandro
"""

#Alejandro Piñeiros
#Ejercicio 3 
#25 de junio 2020

cali1= input("Ingrese su primera calificación: ")
cali2= input("Ingrese su segunda calificación: ")
cali3= input("Ingrese su tercera calificación: ")
c1=int(cali1)
c2=int(cali2)
c3=int(cali3)
to=0
if c1>c2 or c1>c3:
    to=to+c1
if c2>c1 or c2>c3:
    to=to+c2
if c3>c1 or c3>c2:
    to=to+c3

print("Su calificacion total es: ",to)
 
