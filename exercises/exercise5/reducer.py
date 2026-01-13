#!/usr/bin/env python3
import sys

maxItem = None
maxTotal = 0.0
salesTotal = 0.0
oldKey = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2: continue
    thisKey, thisSale = data_mapped

    if oldKey is None: oldKey = thisKey

    if oldKey != thisKey:
        if salesTotal > maxTotal:
            maxTotal = salesTotal
            maxItem = oldKey
        oldKey = thisKey
        salesTotal = 0.0

    salesTotal += float(thisSale)

if oldKey is not None and salesTotal > maxTotal:
    maxTotal = salesTotal
    maxItem = oldKey

if maxItem is not None:
    print(str(maxItem)+"\t"+str(maxTotal))
