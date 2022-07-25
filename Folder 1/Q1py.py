# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 16:13:44 2022

@author: karmh
"""
import math
import numpy as np

A = np.array([[1,2],[3,4]])
b = np.array([[5],[8]])

x = np.linalg.solve(A,b)
print(x)