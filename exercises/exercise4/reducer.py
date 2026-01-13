#!/usr/bin/python
import sys
paycount = 0
oldKey = None
for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2: continue
    thisKey, thisValue = data_mapped
    if oldKey and oldKey != thisKey:
        print(oldKey+"\t"+str(paycount))
        oldKey = thisKey;
        paycount = 0
    oldKey = thisKey
    paycount += 1
if oldKey != None: print(oldKey+"\t"+str(paycount))
