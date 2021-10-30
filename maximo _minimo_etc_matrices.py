# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 11:45:24 2020

@author: Alejandro
"""


import numpy as np


a= np.array([[1,2,3,0],[4,6,8,1]], dtype=np.int64)
print(a.min())
print(a.max())
print(a.sum())
print(a.std())
print(np.sqrt(a))
print(np.std(a))


