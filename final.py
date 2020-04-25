# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 15:11:06 2020

@author: Feny
"""


name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
words = list()
for line in handle:
    if not line.startswith("From") : continue
    line = line.split()
    words.append(line[1])
counts = dict()
for word in words :
    counts[word] = counts.get(word,0) + 1
mval = None
mkey = None
for key,val in counts.items() :
    if val > mval :
        mval =val
        mkey = key
print(mkey,mval)        
    
