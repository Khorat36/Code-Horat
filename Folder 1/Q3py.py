# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 16:15:10 2022

@author: karmh
"""
import matplotlib.pyplot as plt
import math 
import numpy as np
x = [1,2,3,4]
N = 0
def s(x,N):
    total = 0
    for n in range(N):
        total += (x**n)/n
plt.plot(x,s(x,3), color = 'r')
plt.show()
