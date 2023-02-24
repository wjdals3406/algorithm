# -*- coding: utf-8 -*-
import sys
from collections import deque
n,m = map(int, sys.stdin.readline().split())
data = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
visited = [[False]*(m+1) for _ in range(n+1)]

dx = [1, 0, 0,-1] 
dy = [0, 1,-1, 0]

def bfs():
    x,y = 1,1
    visited[x][y] = True
    que = deque([(x,y)])
    while que:
        x,y = que.popleft()
        visited[x][y] = True
        if x == n and y == m:
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx <= 0 or nx > n or ny <= 0 or ny > m:
                continue
            if data[nx-1][ny-1] == 1 and not visited[nx][ny]:
                data[nx-1][ny-1] = data[x-1][y-1] + 1
                que.append((nx,ny))
        
bfs()        
print(data[n-1][m-1])
  