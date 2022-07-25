# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 16:16:11 2022

@author: karmh
"""
import math 
import sympy as sp
sp.init_printing()
x = 2.0
def f(x):
    return (x**3) - ((sp.cos(sp.pi*x))**2) * (1/2*(x**2))+ ((11/3)*(x**2)) -1 

display(sp.diff(f(x)))