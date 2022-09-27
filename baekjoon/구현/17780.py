# -*- coding: utf-8 -*-
import sys
# ü������ ũ�� N, ���� ���� K
n,k = map(int, sys.stdin.readline().split())
# 0�� ���, 1�� ������, 2�� �Ķ���
color = [[0] for _ in range(n+1)]
horse = [[0] for _ in range(k+1)]
for i in range(1,n+1):
    color[i].extend(list(map(int, sys.stdin.readline().split())))
for i in range(1,k+1):
    horse[i].extend(list(map(int, sys.stdin.readline().split())))

data = [[[] for _ in range(n+1)] for _ in range(n+1)]
dx = [0,0,0,-1,1]
dy = [0,1,-1,0,0]
#��, ��, ��, �� 1,2,3,4
for i in range(1,k+1):
    data[horse[i][1]][horse[i][2]].append(i)
cnt = 0

#�̵��� ĭ�� �Ͼ�� ĭ����, ������ ĭ����, �Ķ��� ĭ����
#���� ���� �ΰ�
flag = 0
while cnt <= 1000:
    cnt += 1
    for i in range(1,k+1):
        _,x,y,d = horse[i] #���� ��ġ �� ����
        if data[x][y][0] == i: #ü���� �� �ؿ� ���� ��
            nx = x + dx[d]
            ny = y + dy[d]
            if nx <= 0 or nx >n or ny <= 0 or ny > n or color[nx][ny] == 2: #�Ķ����� ���� ���
                #�̵� ���� �ݴ��
                if d % 2 == 0:
                    horse[i][3] = d - 1
                    nx = x + dx[d - 1]
                    ny = y + dy[d - 1]
                else:
                    horse[i][3] = d + 1
                    nx = x + dx[d + 1]
                    ny = y + dy[d + 1]
                if nx <= 0 or nx >n or ny <= 0 or ny > n or color[nx][ny] == 2:
                    continue
                
            if color[nx][ny] == 0: #�̵��ϴ� ĭ�� ���
                data[nx][ny].extend(data[x][y])
            elif color[nx][ny] == 1: #�̵��ϴ� ĭ�� ������
                data[nx][ny].extend(data[x][y][::-1])
            
            #horse ��ǥ �̵�
            for j in data[x][y]: 
                horse[j][1] = nx
                horse[j][2] = ny
            data[x][y] = []
                
            if len(data[nx][ny]) >=4:
                flag = 1
                break
    if flag:
        break
    
if cnt > 1000:
    print(-1)
else:print(cnt)