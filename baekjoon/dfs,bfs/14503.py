# -*- coding: utf-8 -*-
import sys
n,m = map(int, sys.stdin.readline().split())
x,y,d = map(int, sys.stdin.readline().split())
data = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
#��ĭ : 0, �� : 1

dx = [-1, 0, 1, 0] #��, ��, ��, ��
dy = [0, 1, 0, -1]

def turn_left(dir):
    return (dir - 1) % 4
def turn_back(dir):
    return (dir - 2) % 4

cnt = 0
flag = 1
flag2 = 1
while True:
    if flag: # 1��
        data[x][y] = -1 #���� ��ġ�� û����
        cnt += 1
    for i in range(4): #2��
        flag = 1
        d = turn_left(d) #ȸ��
        nx = x + dx[d]
        ny = y + dy[d]

        if data[nx][ny] == 0:
            flag2 = 0
            x,y = nx, ny
            break
    if flag2 == 0:
        flag2 = 1
        continue
    
    #�� ���� ��� û�Ұ� �̹� �Ǿ��ְų� ���� ��
    nd = turn_back(d)
    nx = x + dx[nd]
    ny = y + dy[nd]
    if data[nx][ny] == -1 : #���� ������ �� ĭ�϶�
        x,y = nx, ny #2������ ���ư�
        flag = 0
    else:
        break
    
print(cnt)   