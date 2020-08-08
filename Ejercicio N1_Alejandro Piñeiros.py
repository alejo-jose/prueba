# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 14:06:16 2020

@author: Alejandro
"""
#Alejandro Piñeiros
#Ejercicio 1 
#25 de junio 2020

cantidad= input("Cantidad de llantas: ")
precio=input("Precio inicial de cada llanta: ")

can1=int(cantidad)
pre1=int(precio)

if can1<=4:
    total1=(can1*pre1)
   
    print("Valor a pagar",total1)
else:
   Au=((pre1*10)/100)
   Bu=(pre1-Au)
   total2=(can1*Bu)
     
   print("Valor a pagar",total2)