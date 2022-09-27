# -*- coding: utf-8 -*-
#�ش� �ڵ�� �ð��ʰ���
# '.'�� �� ����, 'X'�� ���� ����, 'L'�� ������ �ִ� ����
import sys
from collections import deque
n,m = map(int, sys.stdin.readline().split())
data = [list(map(str, sys.stdin.readline().rstrip())) for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

object = []
for r in range(n):
    for c in range(m):
        if data[r][c] == 'L':
            object.append((r,c))

def melt():
    #visited �迭 ����ؼ� ���⼭ �ٷ� data�� �ٲ��ַ��� ��� �ؾ�����?
    melt = []
    for r in range(n):
        for c in range(m):
            if data[r][c] == '.':
                for i in range(4):
                    nx = r + dx[i]
                    ny = c + dy[i]
                    if nx < 0 or nx >=n or ny < 0 or ny >= m:
                        continue
                    if data[nx][ny] == 'X':
                        melt.append((nx,ny))
                    
    return melt

def check_meet(x,y):
    que = deque([(x,y)])
    visited = [[0] * m for _ in range(n)]
    while que:
        x,y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >=n or ny < 0 or ny >= m:
                continue
            if nx == object[1][0] and ny == object[1][1]:
                return True
            if data[nx][ny] == '.' and not visited[nx][ny]:
                que.append((nx,ny))
                visited[nx][ny] = 1
    return False
                

cnt = 0
while not check_meet(object[0][0], object[0][1]):
    melt_position = melt()
    for x, y in melt_position:
        data[x][y] = '.' 
    cnt += 1

print(cnt)