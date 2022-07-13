# -*- coding: utf-8 -*-
import sys
from itertools import combinations

#3 2 1 1 9 -> 8
n, m = map(int,sys.stdin.readline().split())
ball = list(map(int,sys.stdin.readline().split()))

perm = list(combinations(ball, 2))
for i in perm:
    if i[0] == i[1]:
        perm.remove(i)
        
print(len(perm))