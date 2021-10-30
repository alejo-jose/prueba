# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 11:30:58 2020

@author: Alejandro
"""


import numpy as np


a= np.array([[1,2,3,0],[5,6,8,1]], dtype=np.int64)
print(a[1,1])
#para llamar deuna misma columna o fila se usa :
print(a[0:,1])