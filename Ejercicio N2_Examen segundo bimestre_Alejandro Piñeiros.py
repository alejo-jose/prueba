# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 11:04:11 2020

@author: Alejandro
"""

a=int(input("Contador inicial"))
b=int(input("Contador final "))

if b>=a:
    print("Impresora A COLOR o BLANCO Y NEGRO")
    c=int(input(" 1.B/N       2.Color   "))
    if c==1 :
        d=b-a
        print(" Impresiones totales: ",d)
        e=d*0.06
        print("Costo: ",e)
    if c==2:
        d=b-a
        print(" Impresiones totales: ",d)
        e=d*0.12
        print("Costo: ",e)
else:
        print("\n"*1)
        print("ERROR: El contador final es menor que el inicial")
        print("Ponga el valor inicial menor al final")
        b=0
        while b<a:
            b=int(input("Ingrese Contador final de nuevo "))
            
        print("Impresora A COLOR o BLANCO Y NEGRO")
        c=int(input(" 1.B/N       2.Color   "))
        if c==1 :
           d=b-a
           print(" Impresiones totales: ",d)
           e=d*0.06
           print("Costo: ",e)
        if c==2:
           d=b-a
           print(" Impresiones totales: ",d)
           e=d*0.12
           print("Costo: ",e)     