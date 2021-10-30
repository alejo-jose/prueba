# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 14:12:23 2020

@author: Alejandro
"""

def fibonacci(n):
    a=1
    b=0
    
    for i in range (n-2):
        b=b+a
        a=b-a
        print(a,end=',')
        
        
    return b
  
fibonacci(8)   