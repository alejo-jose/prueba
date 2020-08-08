# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 13:56:56 2020

@author: Alejandro
"""

def fibonacci(n):
    a=1
    b=0
    
    for i in range (0,n):
        b=b+a
        a=b-a
        print(a,end=',')
        
    return b
  
fibonacci(8)    