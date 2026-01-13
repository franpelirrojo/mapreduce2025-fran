#!/usr/bin/python
import sys
nitem= 5

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != nitem: continue
    datetime, store, item, cost, payment = data
    print(payment+"\t"+payment)
