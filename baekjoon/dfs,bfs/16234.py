# -*- coding: utf-8 -*-
#pypy3로는 정답처리되는데 python3로는 시간초과 뜸..
import sys
from collections import deque
n,l,r = map(int, sys.stdin.readline().split())
data = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,1,-1]

def bfs(x,y):
    que = deque([(x,y)])
    # cnt = 1
    # sum = data[x][y]
    move_list = [(x,y)]
    visited[x][y] = True
    while que:
        x,y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >=n or ny < 0 or ny >=n:
                continue
            if not visited[nx][ny]:
                if l <= abs(data[nx][ny] - data[x][y]) <= r:
                    # cnt += 1
                    # sum += data[nx][ny]
                    visited[nx][ny] = True
                    move_list.append((nx, ny))
                    que.append((nx, ny))
    # if cnt > 1:
    #     for i,j in move_list:
    #         data[i][j] = sum // cnt
    return move_list
  
res = 0
while True:  
    flag = 1
    for i in range(n):
        for j in range(n):
            if visited[i][j]:
                continue
            move_list = bfs(i,j)   
            if len(move_list) > 1:
                number = sum([data[x][y] for x, y in move_list]) // len(move_list) 
                flag = 0
                for x,y in move_list:
                    data[x][y] = number
    if flag == 1:
        break
    visited = [[False] * n for _ in range(n)]
    res += 1
print(res)
        