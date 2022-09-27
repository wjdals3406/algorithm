# -*- coding: utf-8 -*-
#내가 맨 처음에 시도했던 방식 : 1이 있는 리스트를 생성하고 1이 존재하는 곳에 bfs 함수 동시에 실시
# => 시간초과
import sys
from collections import deque
m,n,z = map(int, sys.stdin.readline().split()) #n:행, m : 열, h:높이 
data = [[list(map(int, sys.stdin.readline().split())) for _ in range(n)] for _ in range(z)]
que = deque([])
#1: 익은 토마토, 0: 익지 않은 토마토, -1:토마토 없음
dx = [1, 0, 0, -1, 0, 0] 
dy = [0, 1, -1, 0, 0, 0]
dh = [0, 0, 0, 0, 1, -1]

for i in range(z):
    for r in range(n):
        for c in range(m):
            if data[i][r][c] == 1:
                que.append((i,r,c))

def count_zero(): #익지 않은 토마토가 있는 인덱스 생성
    result = -1
    for i in range(z):
        for r in range(n):
            for c in range(m):
                if data[i][r][c] == 0:
                    return 0
            result = max(result, max(data[i][r]))
    return result

def bfs():
    while que:
        h,x,y = que.popleft()
        for j in range(6):
            nx = x + dx[j]
            ny = y + dy[j]
            nh = h + dh[j] 
            if nx < 0 or nx >= n or ny < 0 or ny >= m or nh < 0 or nh >= z: 
                continue
            if data[nh][nx][ny] == 0:
                data[nh][nx][ny] = data[h][x][y] + 1
                que.append((nh, nx, ny))

bfs()
res = count_zero()
if res == 0:
    print(-1)
else:
    print(res - 1)
