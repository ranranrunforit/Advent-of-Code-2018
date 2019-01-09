# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 18:53:57 2018

@author: Chaoran
"""


f = open("3.txt", "r")
w, h = 1000, 1000;
Matrix = [[0 for x in range(w)] for y in range(h)] 
for x in range(w):
    for y in range(h):
        Matrix[x][y] = "."
#print(Matrix)
count = 0
overlap = []
org = []
for x in f:
    #print(x)
    array = x.split()
    #print(array)
    num = array[0].replace("#", "")
    org.append(num)
    #print(num)
    array2 = array[2].split(',')
    #print(array2)
    leftn = int(array2[0])
    topn = int(array2[1].replace(":", ""))
    #print(leftn)
    #print(topn)
    array3 = array[3].split('x')
    wide = int(array3[0])
    high = int(array3[1])
    lw = leftn+wide
    th = topn+high
    #print(wide)
    #print(high)
    for l in range(topn,th):
        for i in range(leftn, lw):
            if Matrix[l][i] != ".":
                if Matrix[l][i] in org:
                    org.remove(Matrix[l][i])
                if num in org:
                    org.remove(num)
                Matrix[l][i] = "X" 
            else:
                Matrix[l][i] = num
                
          
print(org)
    
''' 
======                
part 1
======
   
    for l in range(topn,th):
        for i in range(leftn, lw):
            if Matrix[l][i] != ".":
                Matrix[l][i] = "X" 
            else:
                Matrix[l][i] = num

count1 = 0
for x in range(w):
    for y in range(h):
        if Matrix[x][y] == "X":
            count1 = count1 +1
print(count1)
'''
                    
#print(Matrix)