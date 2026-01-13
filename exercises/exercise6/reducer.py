#!/usr/bin/python
import sys
salesCount = 0
oldKey = None
for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2: continue
    thisKey, thisValue = data_mapped
    oldKey = thisKey
    salesCount += float(thisValue)
if oldKey != None: print(oldKey+"\t"+str(salesCount))
