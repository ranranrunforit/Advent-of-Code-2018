# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 20:07:53 2018

@author: Chaoran
"""
f = open("5.txt", "r")
A=[]
A2 = []
from LinkedList import LinkedList
for x in f:
    A = x
    print(A)


from LinkedList import LinkedList

def remove_dups(ll):
    if ll.head is None:
        return

    current = ll.head
    while current and current.next:
        runner = current
        prevNode = current.prev#store current.next
        nextNode = current.next.next
        if runner.next.value != current.value:
            if runner.next.value == current.value.lower() or runner.next.value == current.value.upper():
                current = prevNode
                current.next = nextNode      
        current = current.next
        
    return ll.head


ll = LinkedList(A)
current = ll.head
prev = None
while current:
    current.prev = prev
    prev = current
    current = current.next
#ll.generate(100, 0, 9)
#print(ll)
print(ll.__len__())
#print(ll)
remove_dups(ll)
print(ll.__len__())
#print(ll)
