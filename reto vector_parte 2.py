# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 13:02:58 2020

@author: Alejandro
"""


import numpy as np

print("Ingrese un valor del vector MAYOR a 3 y MENOR a 30")
z=int(input("Ingrese la dimension del vector"))
print("\n"*1)
print("Desea trabajar con caracteres o valores numericos")
print("\n"*1)
print("1. Ingrese 1 si desea con caracteres")
print("2. Ingrese 2 si desea con valores numericos")
print("\n"*1)
x=int(input("Ingrese 1 o 2 "))

if x==1:
    caracter=[]
    for i in range(z) :
        caracte=input("Caracter: ")
        caracter.append(caracte)
    print("\n"*1)
    print("El vector de caracteres original es",caracter)
    print("\n"*1)
    print("Desea ordenar de MAYOR  a menor o MENOR a mayor")
    print("\n"*1)
    print("1. Ingrese 1 si desea ordenar de MAYOR  a menor")
    print("2. Ingrese 2 si desea ordenar de MENOR a mayor")
    print("\n"*1)
    y=int(input("Ingrese 1 o 2 "))
    if x==1:
        a=False
        while a==False: #mientras sea falso(no este ordenado) se ejecutara
            
            a=True #salir de bucle
            for i in range(len(caracter)-1):#rango= toda la longitud del vector menos 1 para que no marque erro
                
                if caracter[i] < caracter[i+1]: #comparacion elemento a
                    
                    b=caracter[i] # guarda numero  y es menor
                    caracter[i]=caracter[i+1] #guarda el intercambio
                    caracter[i+1]=b #guarda a la derecha el numero menor
                    a=False #para que se siga repetiendo hasta que este ordenado
a=False
while a==False: #mientras sea falso(no este ordenado) se ejecutara
    a=True #salir de bucle
    for i in range(len(caracter)-1):#rango= toda la longitud del vector menos 1 para que no marque error
        if caracter[i] < caracter[i+1]: #comparacion elemento a
            b=caracter[i] # guarda numero  y es menor
            caracter[i]=caracter[i+1] #guarda el intercambio
            caracter[i+1]=b #guarda a la derecha el numero menor
            a=False #para que se siga repetiendo hasta que este ordenado
print(caracter)