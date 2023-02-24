# -*- coding: utf-8 -*-
import sys
from collections import deque
n,m = map(int, sys.stdin.readline().split())
data = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

time = 0

def count_cheese():
    return sum(map(sum, data))

def bfs():
    que = deque([[0,0]])
    visited = [[0] * m for _ in range(n)]
    visited[0][0] = 1
    melt = []
    
    while que:
        x,y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            
            if not visited[nx][ny] and data[nx][ny] == 0:
                que.append([nx,ny])
                visited[nx][ny] = 1
            
            elif not visited[nx][ny] and data[nx][ny] == 1:
                melt.append((nx,ny))
                visited[nx][ny] = 1
                
    for x,y in melt: #어차피 visited로 값을 바꾸니까 따로 뺄 필요가 없음
        data[x][y] = 0
        
while count_cheese():
    cnt = count_cheese()
    bfs()
    time += 1
    

print(time)
print(cnt)
    
    