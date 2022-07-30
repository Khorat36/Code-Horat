# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 10:49:02 2022

@author: karmh
"""
import random
from collections import Counter


def deal(numcard):
    deck = 4*[1,2,3,4,5,6,7,8,9,10,11,12,13]
    hand = []
    for i in range(numcard):
        a = random.choice(deck)
        hand.append(a)
        deck.remove(a)
        
    return hand
twocount = []
threecount = []
fourcount =[]
def count(hand,twocount,threecount,fourcount):
    count2 = Counter(hand)
    print(count2)
    two = 0
    three = 0
    four = 0
    for n in count2.values():
        if n == 2: 
            two = two + 1
        
        if n == 3:
            three = three + 1
            
        if n == 4:
            four = four + 1
    twocount.append(two)
    threecount.append(three)
    fourcount.append(four)
    