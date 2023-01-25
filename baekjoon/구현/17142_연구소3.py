# -*- coding: utf-8 -*-
import sys
from itertools import combinations
from collections import deque

n,m = map(int, sys.stdin.readline().split())
data = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

#연구소의 모든 빈 칸에 바이러스가 있게 되는 최소 시간
#0: 빈 칸, 1: 벽, 2 : 바이러스를 놓을 수 있는 위치

#바이러스를 높을 수 있는 위치 vlist에 담기
vlist = []
zero = []
for i in range(n):
    for j in range(n):
        if data[i][j] == 2:
            vlist.append((i,j))
        if data[i][j] == 0:
            zero.append((i,j))
        

def spread(vlist):
    que = deque(vlist) 
    visited = [[-1] * n for _ in range(n)]
    zero_cnt = 0
    for i in vlist: #((0, 0), (1, 5), (4, 3))
        visited[i[0]][i[1]] = 0
        
    while que:
        x,y = que.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >=n or ny < 0 or ny >= n:
                continue
            
            if visited[nx][ny] == -1 and data[nx][ny] != 1:
                que.append((nx,ny))
                visited[nx][ny] = visited[x][y] + 1
                
                if data[nx][ny] == 0: #빈칸
                    zero_cnt += 1
                
                if len(zero) == zero_cnt:
                    return visited[x][y] + 1
                
    return -1
                

#바이러스가 m개 놓일 수 있는 모든 경우
comb = list(combinations(vlist, m))
res = int(1e9)
if len(zero) == 0:
    print(0)
else:
    for i in comb:
        value = spread(i)
        if value== -1:
            continue
        else:
            res = min(res, value)

    if res == int(1e9):
        print(-1)
    else:
        print(res)
        
                
       