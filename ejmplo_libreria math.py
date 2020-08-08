# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 12:10:47 2020

@author: Alejandro
"""

#ejemplo libreria math

#1 manera
#import math
#print(math.sin(math.pi/2))

#2 manera
#from math import sin,pi
#print(sin(pi/2))

import math

def sin(x):
    if 2*x==pi:
        return 0.99999999
    else:
        return None
pi = 3.14
print(sin(pi/2))
print(math.sin(math.pi/2))

