# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 16:15:29 2022

@author: karmh
"""
import matplotlib.pyplot as plt
import math
import sympy as sp
import numpy as np
sp.init_printing()
def f(x):
    return (x**2)

def midpoint(f,a,b,n):
    x = np.arange(a,b,n)
    
    for i in x:
        h = (i + 1) - i
        return  sp.integrate(f((i + (i+1))/2) * h)
    
        
display(midpoint(f, 2, 4, 3))