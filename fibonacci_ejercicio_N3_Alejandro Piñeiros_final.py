# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 14:37:45 2020

@author: Alejandro
"""


def fibonacci(n): 
    a,b=0,1
    while a < n:
        print(a,end=',')
        a,b=b,a+b
    print()
    
fibonacci(8)  
    

