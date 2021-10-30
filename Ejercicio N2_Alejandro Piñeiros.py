# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 14:38:43 2020

@author: Alejandro
"""
#Alejandro Piñeiros
#Ejercicio 2 
#25 de junio 2020

horatrabajada= input("Horas trabajadas: ")
tarifa=input("Tarifa por hora: ")

hora=int(horatrabajada)
tar=int(tarifa)

if hora<=40:
    S1=(hora*tar)
    print("Valor a pagar: ",S1)
else:
    A=(hora-40)#numero hora extras
    B=(tar/2)#tarifa a la mitad
    C=(A*B)# valor hora extra
    D=((hora-A)*tar)#valor horas de trabajo
    E=(D+C)#suma valor hora de trabajo y horas extras
    print("Valor a pagar: ",E)
    
