# -*- coding: utf-8 -*-
import sys
from itertools import combinations
import copy
input = sys.stdin.readline

def spread_virus(r, c, re):
    if re[r][c] == 2:
        if r < n-1 and re[r+1][c]==0:
           re[r+1][c] = 2
           re =  spread_virus(r+1, c, re)
        if r > 0 and re[r-1][c]==0:
           re[r-1][c] = 2
           re =  spread_virus(r-1, c, re)
        if c > 0 and re[r][c-1]==0:
           re[r][c-1] = 2
           re = spread_virus(r, c-1, re)
        if c < m-1 and re[r][c+1]==0:
           re[r][c+1] = 2
           re = spread_virus(r, c+1, re)
    return re

n, m= map(int, input().split())
re = []

for _ in range(n):
    re.append(list(map(int, input().split())))

#0, 2가 있는 위치
empty = [] 
virus = []
for r in range(n):
    for c in range(m):
        if re[r][c] == 0:
            empty.append((r,c))
        if re[r][c] == 2:
            virus.append((r,c))
   
maxval = 0

comb = list(combinations(empty, 3))
for i in comb:
    re_copy =copy.deepcopy(re)
    for j in i:
        re_copy[j[0]][j[1]] = 1
        
    sum = 0
    for k in virus: #바이러스 있는 곳 
        re_copy = spread_virus(k[0], k[1], re_copy)
        
    #0의 개수 count
    for v in re_copy:
        sum += v.count(0)
    if  sum > maxval: 
        maxval = sum
            
print(maxval)        
        