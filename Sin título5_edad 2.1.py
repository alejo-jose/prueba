# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 12:13:26 2020

@author: Alejandro
"""


nombre= input("Ingrese su Nombre: ")
ape= input("Ingrese su Apellido: ")
ubi= input("Ingrese su Ubicacion: ")
edad = int(input("¿Ingrese su edad "))
espacio=" "
eda=str(edad)
print("Hola "+nombre +espacio +ape +espacio +"estar en" +espacio +ubi +espacio +"es fantastico por que es un lugar maravilloso"+espacio +"y tener" +espacio +eda +espacio +"años" +espacio +"no te impide estar y conocer distintas ubicaciones.")


if edad > 0 and edad<10:
  print("es un niño")
    
elif edad <= 18:
    print("Es usted joven ")
  
elif edad>=19 and edad < 65:
    print("Es un adulto ")
    
elif edad >= 65:
    print("Es un adulto mayor ")


       
else:
  print("Edad incorrecta")