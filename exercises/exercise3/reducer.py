#!/usr/bin/python
import sys
salesMax = 0
oldKey = None
for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2: continue
    thisKey, thisValue = data_mapped
    if oldKey and oldKey != thisKey:
        print(oldKey+"\t"+str(salesMax))
        oldKey = thisKey;
        salesMax = 0
    oldKey = thisKey
    if thisValue > salesMax: salesMax = thisValue
# Escribe o ultimo par, unha vez rematado o bucle
if oldKey != None:
    print(oldKey+"\t"+str(salesMax))
