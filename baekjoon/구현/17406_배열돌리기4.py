# -*- coding: utf-8 -*-
import sys
from itertools import permutations
import copy
n,m,k = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
computation = [list(map(int, sys.stdin.readline().split())) for _ in range(k)]
dx = [0,1,0,-1]
dy = [1,0,-1,0]
per= list(permutations(computation, len(computation)))

def copy_array():
    for i in range(n):
        for j in range(m):
            if new[i][j] > 0:
                data[i][j] = new[i][j]

res = int(1e9)
for com in per:
    data = copy.deepcopy(board)
    new = [[0] * m for _ in range(n)]
    for r,c,s in com:
        x,y = r-s-1, c-s-1
        for k in range(s):
            for i in range(4):
                for _ in range(2*s - 2*k): 
                    cur = data[x][y]
                    x = x + dx[i]
                    y = y + dy[i]
                    new[x][y] = cur
            x,y = x + 1, y + 1
            
        copy_array()
    res = min(res, min(map(sum, data)))
print(res)