# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 10:45:55 2022

@author: karmh
"""
import finalpequations as eqtn
import math 
import matplotlib.pyplot as plt

n = 1001
i = 1
twocount = []
threecount = []
fourcount = []
while i < n :
    b = eqtn.deal(5)
    eqtn.count(b,twocount,threecount,fourcount)
    i = i + 1
    
print(twocount)
print(threecount)
print(fourcount)



#plt.hist(threecount, bins = [0,0,1])
#plt.show()

# plt.hist(threecount, bins = [0,0,1])
# plt.show()

plt.hist(fourcount, bins = [0,1])
plt.show()