# -*- coding: utf-8 -*-
import sys
from itertools import combinations

n,m = map(int, sys.stdin.readline().split())
data = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

chicken = []
house = []
for i in range(n):
    for j in range(n):
        if data[i][j] == 2:
            chicken.append((i,j))
        elif data[i][j] == 1:
            house.append((i,j))
            
comb = list(combinations(chicken, m))

res = int(1e9)
for case in comb: #case 1
    casemin = 0
    for x2,y2 in house:
        minval = int(1e9)
        for x1,y1 in case: #각 집마다의 치킨 거리 구함(집과의 거리가 가장 작은 곳)
            minval = min(minval,abs(x1-x2) + abs(y1-y2))
        casemin += minval
    res = min(res, casemin)
    
print(res)
            