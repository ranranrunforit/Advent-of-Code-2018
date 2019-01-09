# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 18:20:48 2018

@author: Chaoran
"""
f = open("2.txt", "r")

#for x in f:
    #array = list(x)
    #print(x)

import itertools
for s1, s2 in itertools.combinations(f, 2):
    count = 0
    for c1, c2 in zip(s1, s2):
        if c1 != c2:
            count = count +1
    if count == 1:
        print(s1,s2)
