# -*- coding: utf-8 -*
import predatorvsprey as pvp
import matplotlib.pyplot as plt
import numpy as np
import random
from matplotlib import animation

num_prey = 50
num_predator = 10

x_max = 25
x_min = 0
y_max = 25
y_min = 0
pop = [pvp.prey(x_max*np.random.uniform(0,1),y_max*np.random.uniform(0,1)) for i in range(num_prey)] + [pvp.predator(x_max*np.random.uniform(0,1),y_max*np.random.uniform(0,1)) for i in range(num_predator)]

ax = plt.axes(xlim = (x_min,x_max), ylim = (y_min,y_max))
fig = plt.gcf()

pop_dead = []

def animate(frame_number):
    for an in pop: 
        an.move(x_min, x_max, y_min, y_max)
        
    d.set_data([animal.x for animal in pop if animal.__class__ is pvp.prey], [animal.y for animal in pop if animal.__class__ is pvp.prey])
    c.set_data([animal.x for animal in pop if animal.__class__ is pvp.predator], [animal.y for animal in pop if animal.__class__ is pvp.predator])
    e.set_data([animal.x for animal in pop_dead], [animal.y for animal in pop_dead])

d, = plt.plot([animal.x for animal in pop if animal.__class__ is pvp.prey], [animal.y for animal in pop if animal.__class__ is pvp.prey], 'bo', markersize = 5)
c, = plt.plot([animal.x for animal in pop if animal.__class__ is pvp.predator], [animal.y for animal in pop if animal.__class__ is pvp.predator], 'ro', markersize = 5)
e, = plt.plot([animal.x for animal in pop_dead], [animal.y for animal in pop_dead], 'o', color = 'black', markersize = 5)

amin = animation.FuncAnimation(fig, animate, frames = 500, interval=1, repeat = False)