# -*- coding: utf-8 -*-
import sys
r,c,k = map(int, sys.stdin.readline().split())
data = [list(sys.stdin.readline().rstrip()) for _ in range(r)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
visited = [[0] * c for _ in range(r)]
visited[r-1][0] = 1
cnt = 0

def dfs(n, x, y):
    global cnt
    if n == k: #k번 돌았는데 목적지에 도착하지 않으면 바로 return
        return
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            continue
        
        if not visited[nx][ny] and data[nx][ny] != 'T':
            if n+1 == k and nx == 0 and ny == c-1: # 다음 도착지가 목적지이면 cnt += 1
                cnt += 1
                continue
            
            visited[nx][ny] = 1
            dfs(n+1, nx, ny)
            visited[nx][ny] = 0
        
dfs(1, r-1, 0)

print(cnt)