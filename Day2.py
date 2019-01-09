# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 16:54:03 2018

@author: Chaoran
"""
from itertools import groupby
import collections

count2 = 0
count3 = 0
count4 = 0
count5 = 0

f = open("2.txt", "r")
a = []
for x in f:
    array = list(x)
    print(x)
    #print(array)
    counter=collections.Counter(array)
    print(counter)
    inv_map = {v: k for k, v in counter.items()}
    k = inv_map.keys()
    #print(len(inv_map))
    #a2 = [len(list(group)) for key, group in groupby(array)]
    #print(a2)
    #a3 = [len(list(group)) for key, group in groupby(a2)]
    #print(a3)
    #if len(inv_map)>1:
        #a.append(inv_map)
    if 2 in k:
        count2 = count2 +1
    if 3 in k:
        count3 = count3 +1


print(count2*count3)


