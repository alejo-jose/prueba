# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 11:24:00 2020

@author: Alejandro
"""


import numpy as np


a= np.array([[1,2,3],[5,6,8]], dtype=np.int64)

print(a)
a=a.reshape(3,2)
print(a)