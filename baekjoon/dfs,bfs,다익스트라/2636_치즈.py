# -*- coding: utf-8 -*-
import sys
from collections import deque
n,m = map(int, sys.stdin.readline().split())
data = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs():
    que = deque([(0,0)])
    visited = [[0] * m for _ in range(n)]
    melt = []
    while que:
        x,y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >=n or ny < 0 or ny >= m:
                continue
            if data[nx][ny] == 1 and not visited[nx][ny]:
                melt.append((nx,ny))
            elif data[nx][ny] == 0 and not visited[nx][ny]:
                que.append((nx,ny))
            visited[nx][ny] = 1
    return melt

melt = [0]
time = 0
while True:
    melt = dfs()
    for x,y in melt:
        data[x][y] = 0
    res = 0
    for i in data:
        res += sum(i)
    time += 1
    if res == 0:
        break
    
    
print(time)
print(len(melt))
    
    
