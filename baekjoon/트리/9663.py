# -*- coding: utf-8 -*-
# https://velog.io/@inhwa1025/BOJ-9663%EB%B2%88-N-Queen-Python-%ED%8C%8C%EC%9D%B4%EC%8D%AC
import sys
n = int(sys.stdin.readline())
visited = [[0] * (n) for _ in range(n)] #2차원 배열로 하려면 어떻게 해야됨?
dx = [-1,1,0,0,-1,-1,1,1]
dy = [0,0,-1,1,-1,1,-1,1]
def chess(x,y):
    cnt = 0
    for i in range(n):
        
        if not visited[x][y]:
            cnt += 1
            for i in range(8):
                for j in range(1,n): # 상,하,좌,우,대각선 쭉 이동
                    nx = x + dx[i] * j
                    ny = y + dy[i] * j
                    if nx < 0 or nx >=n or ny < 0 or ny >= n:
                        break
                    visited[nx][ny] = 1
        
            chess(i+1,y)
            



