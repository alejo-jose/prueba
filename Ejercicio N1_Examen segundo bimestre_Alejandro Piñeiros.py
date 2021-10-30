# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 12:17:20 2020

@author: Alejandro
"""
temp=0
gaseoso=0
liquido=0
solido=0
a=int(input("Ingrese cantidad de temperaturas [1,10]: "))
if a>=1 and a<=10:
    print("hola")
    for i in range(a):
        b=(int(input("Ingrese temperatura")))
        if b>=100:
            gaseoso=gaseoso+1
            temp=temp+b
#            b=0
        if b>0 and b<100:
            liquido=liquido+1
            #b=0
            temp=temp+b
        if b<=0:
            solido=solido+1
           # b=0
            temp=temp+b
    print("\n"*1)
    print("Cantidad de muestras sólidas:",solido) 
    print("Cantidad de muestras liquidas:",liquido) 
    print("Cantidad de muestras gaseosas:",gaseoso) 
    print("\n"*1)
    w=(temp/a)
    h=((w*(9/5))+32)
    
    print("Temperatura Promedio °C:",w)
    print("Temperatura Promedio °F:",h)
else:
    print("Ingrese un rango adecuado")

    