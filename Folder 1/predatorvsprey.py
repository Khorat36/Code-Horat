# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 11:10:51 2022

@author: karmh
"""
import random
import math


class cats():
    
    def __init__(self, x,y):
        self.startpoints = 100
        self.x = x
        self.y = y
    def move(self,x_min,x_max, y_min, y_max):
        a = random.uniform(1,4)
        
        if a == 1:
            self.x += 1
        elif a == 2:
            self.y += 1
        elif a == 3:
            self.x -= 1
        elif a == 4: 
            self.y -= 1
        
        if self.x <= x_min:
            self.x + x_min
        if self.x >= x_max:
            self.x = x_max
        if self.y <= y_min:
            self.y = y_min
        if self.y >= y_max:
            self.y = y_max
    
class predator(cats):
    pass
    def predator(self,cats):
        distance = math.sqrt((self.x - cats.x)**2 +(self.y - cats.y)**2)
        
        #if distance < 1:
            
class prey(cats):
    pass
 
            