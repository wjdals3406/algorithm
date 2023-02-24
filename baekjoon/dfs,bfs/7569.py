# -*- coding: utf-8 -*-
#���� �� ó���� �õ��ߴ� ��� : 1�� �ִ� ����Ʈ�� �����ϰ� 1�� �����ϴ� ���� bfs �Լ� ���ÿ� �ǽ�
# => �ð��ʰ�
import sys
from collections import deque
m,n,z = map(int, sys.stdin.readline().split()) #n:��, m : ��, h:���� 
data = [[list(map(int, sys.stdin.readline().split())) for _ in range(n)] for _ in range(z)]
que = deque([])
#1: ���� �丶��, 0: ���� ���� �丶��, -1:�丶�� ����
dx = [1, 0, 0, -1, 0, 0] 
dy = [0, 1, -1, 0, 0, 0]
dh = [0, 0, 0, 0, 1, -1]

for i in range(z):
    for r in range(n):
        for c in range(m):
            if data[i][r][c] == 1:
                que.append((i,r,c))

def count_zero(): #���� ���� �丶�䰡 �ִ� �ε��� ����
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
