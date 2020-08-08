# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 11:31:18 2020

@author: Alejandro
"""


import numpy as np
z=int(input("Ingrese la dimension del vector"))
n=1
p=0
x=np.random.random((z))
print("El vector original es ",x)
print("\n"*1)
for v in range(len(x)):#texto individual de valores
    print("El valor en la posicion ",n," es ",x[p])
    p=p+1#acumulador para el texto
    n=n+1
print("\n"*2)
a=False

while a==False: #mientras sea falso(no este ordenado) se ejecutara
    a=True #salir de bucle
    for i in range(len(x)-1):#rango= toda la longitud del vector menos 1 para que no marque error
        if x[i] < x[i+1]: #comparacion elemento a la derecha
            b=x[i] # guarda numero  y es menor
            x[i]=x[i+1] #guarda el intercambio
            x[i+1]=b #guarda a la derecha el numero menor
            a=False #para que se siga repetiendo hasta que este ordenado
print("El vector ordenado es ",x)
print("\n"*1)
u=1
t=0
for h in range(len(x)):
    print("El vector ordenado en la posicion  ",u," es ",x[t])
    t=t+1
    u=u+1