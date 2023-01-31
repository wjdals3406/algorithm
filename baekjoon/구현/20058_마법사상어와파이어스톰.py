# -*- coding: utf-8 -*-
#남아있는 얼음 A[r][c]의 합 / 남아있는 얼음 중 가장 큰 덩어리가 차지하는 칸의 개수 구하기
import sys
from collections import deque
n,q = map(int, sys.stdin.readline().split())
data = [list(map(int, sys.stdin.readline().split())) for _ in range(2**n)]
qlist = list(map(int, sys.stdin.readline().split()))
#1.배열 90도 회전
#2.남아있는 얼음 A[r][c]의 합 : sum(map(sum,data))
#3.남아있는 얼음 중 가장 큰 덩어리가 차지하는 칸의 개수 구하기
dx = [-1,1,0,0]
dy = [0,0,-1,1]
visited = [[0] * (2**n) for _ in range(2**n)]

def turn_90(l): #Li가 0일 때는 아무것도 안하나..?
    
    

def bfs(x,y): 
    que = deque([[x,y]])
    cnt = 1
    visited[x][y] = cnt
    while que:
        x,y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= 2**n or ny < 0 or ny >= 2**n:
                continue
            if not visited[nx][ny] and data[nx][ny] > 0:
                visited[nx][ny] = cnt + 1
                cnt += 1
                que.append([nx,ny])


for i in range(2**n):
    for j in range(2**n):
        if not visited[i][j]:
            bfs(i,j)
print(sum(map(sum,data)))
print(max(map(max,visited)))

    
            




