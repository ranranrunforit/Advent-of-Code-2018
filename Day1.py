# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 15:24:49 2018

@author: Chaoran
"""

f = open("1.txt", "r")
a = 0
array = []
org = []
for x in f:
  org.append(x)
  a = a + int(x)
  array.append(a)
s = set(array)
end = 0
#print(s)
while True:
    for r in org:
        a = a + int(r)
        if a in s:
            print(a)
            end = -1
            break
        array.append(a)
    if end == -1:
        break