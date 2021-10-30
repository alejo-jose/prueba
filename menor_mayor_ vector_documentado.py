# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 15:27:33 2020

@author: Alejandro
"""
import numpy as np
z=int(input("Ingrese la dimension del vector"))

x=np.random.random((z))
print("El vector original es ",x)

a=False

while a==False: #mientras sea falso(no este ordenado) se ejecutara
    a=True #salir de bucle
    for i in range(len(x)-1):#rango= toda la longitud del vector menos 1 para que no marque error
        if x[i] > x[i+1]: #comparacion elemento a la derecha
            b=x[i] # guarda numero que no cambia por el momento y mayor
            x[i]=x[i+1] #guarda el intercambio, numero menor
            x[i+1]=b #vuelve el elemento original y mayor
            a=False #para que se siga repetiendo hasta que este ordenado
print("El vector ordenado es ",x)