# -*- coding: utf-8 -*-
import sys
n, m = map(int,sys.stdin.readline().split())

money = []
for _ in range(n):
    money.append(int(sys.stdin.readline()))

money.sort(reverse=True)
d = [0] * m

d[min(money)] = 1
for i in range(min(money)+1, m + 1):
    for j in money:
        d[i] = min(d[i], d[i]//j )
    
for i in money:
    d[i] = 1
