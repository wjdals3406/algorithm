# -*- coding: utf-8 -*-
#�����ִ� ���� A[r][c]�� �� / �����ִ� ���� �� ���� ū ����� �����ϴ� ĭ�� ���� ���ϱ�
import sys
from collections import deque
n,q = map(int, sys.stdin.readline().split())
data = [list(map(int, sys.stdin.readline().split())) for _ in range(2**n)]
qlist = list(map(int, sys.stdin.readline().split()))
#1.�迭 90�� ȸ��
#2.�����ִ� ���� A[r][c]�� �� : sum(map(sum,data))
#3.�����ִ� ���� �� ���� ū ����� �����ϴ� ĭ�� ���� ���ϱ�
dx = [-1,1,0,0]
dy = [0,0,-1,1]
visited = [[0] * (2**n) for _ in range(2**n)]

def turn_90(l): #Li�� 0�� ���� �ƹ��͵� ���ϳ�..?
    
    

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

    
            




