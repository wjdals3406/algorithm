# -*- coding: utf-8 -*-
import sys
from itertools import combinations

#3 2 1 1 9 -> 8
n = int(sys.stdin.readline())
money = list(map(int,sys.stdin.readline().split()))
money.sort()

d = [0] * (sum(money) + 1)
for k in range(1, n+1):
    for l in list(combinations(money, k)):
        d[sum(l)] = sum(l)

for i, v in enumerate(d):
    if i != 0 and v == 0:
        print(i)
        break
    