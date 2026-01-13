#!/usr/bin/python
import sys
from datetime import datetime
nitem= 5

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != nitem: continue
    timestamp, store, item, cost, payment = data
    dt = datetime.strptime(timestamp, "%Y-%m-%d %H:%M")
    print(dt.strftime("%H")+"\t"+cost)
