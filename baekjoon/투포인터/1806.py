# -*- coding: utf-8 -*-
import sys
n,m = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))
s,e = 0,0
re = 100001
sumval = data[0]

while s < n and e < n and s <= e:
    if sumval >= m:
        re = min(re, e-s+1) 
        sumval -= data[s]
        s += 1
    else:
        e += 1
        if e > n-1:
            break
        sumval += data[e]
if re == 100001:
    print(0)
else: 
    print(re)