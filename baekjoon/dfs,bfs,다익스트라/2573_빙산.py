# -*- coding: utf-8 -*-
import sys
from collections import deque
n,m = map(int, sys.stdin.readline().split())
data = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(num,x,y): # 일년 뒤의 모습
    que = deque([[x,y]])
    visited[x][y] = num
    
    while que:
        x,y = que.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if not visited[nx][ny] and data[x][y] != 0 and data[nx][ny] == 0:
                data[x][y] -= 1
            
            if not visited[nx][ny] and data[nx][ny] > 0:
                que.append([nx,ny])
                visited[nx][ny] = num 
    
#dfs 한번 -> cnt += 1
#다 녹을 때까지 분리되지 않으면 0을 출력
coordinate = []
for i in range(1,n-1):
    for j in range(1,m-1):
        if data[i][j] > 0:
            coordinate.append((i,j))
cnt = 0
while True:
    visited = [[0] * m for _ in range(n)]
    flag = 0
    num = 1
    for x, y in coordinate:
        if not visited[x][y] and data[x][y] > 0:
            if num > 1:
                print(cnt)
                exit()
            dfs(num,x,y)    
            flag = 1
            num += 1
    cnt += 1
    if flag == 0:
        print(0)
        exit()
            
    coordinate = []
    for i in range(1,n-1):
        for j in range(1,m-1):
            if data[i][j] > 0:
                coordinate.append((i,j))
            
    
    #이건 코드는 간단하지만 시간초과남
    # for x in range(1,n-1):
    #     for y in range(1,m-1):
    #         if not visited[x][y] and data[x][y] > 0:
    #             dfs(num+1,x,y)
    #             num += 1
    #             if num > 1:
    #                 print(cnt)
    #                 exit()
    
    # if num == 0:
    #     print(0)
    #     break

    # cnt += 1
            

    