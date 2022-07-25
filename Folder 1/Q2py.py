# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 16:14:26 2022

@author: karmh
"""
import matplotlib.pyplot as plt

def s(N):
    total = 0
    for n in range(N):
        total += ((-1)**(n+1))*(1/N)
    
        return total
print(s(1000))

plt.plot(s(1000))
plt.show()