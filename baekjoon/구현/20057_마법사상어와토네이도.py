# -*- coding: utf-8 -*-
#����̵��� �Ҹ�Ǿ��� ��, ������ ������ ���� ���� �� ���ϱ�
import sys
n = int(sys.stdin.readline())
data = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dx = [0, 1, 0, -1] #left, down, right, up
dy = [-1, 0, 1, 0]
left = [(1, 1, 0.01), (-1, 1, 0.01), (1, 0, 0.07), (-1, 0, 0.07), (1, -1, 0.1),
         (-1, -1, 0.1), (2, 0, 0.02), (-2, 0, 0.02), (0, -2, 0.05), (0, -1, 0)]
right = [(x, -y, z) for x,y,z in left]
down = [(-y, x, z) for x,y,z in left]
up = [(y, x, z) for x,y,z in left]

dict = {0: left, 1: down, 2: right, 3: up}

def move_sand(x,y,sand):
    throw = 0
    total_sand = 0
    for sx,sy,ratio in sand:
        nx = x + sx
        ny = y + sy
        
        if ratio == 0:
            s = data[x][y] - total_sand
        else:
            s = int(data[x][y] * ratio)
            total_sand += s
            
        if nx < 0 or nx >=n or ny < 0 or ny >= n:
            throw += s #�������� ��
            continue
        data[nx][ny] += s
        
    data[x][y] = 0 #y ��ġ�� �� ����
    return throw
        
    
#����̵� ����
def make_direction():
    total = 0
    x,y  = n//2, n//2 #������
    d, cnt = 0, 1
    
    while True:
        if x == 0:
            for _ in range(n):
                x = x + dx[d] #��ǥ �̵�
                y = y + dy[d]
                total += move_sand(x,y,dict[d])
            break
        else:            
            for _ in range(2):
                for _ in range(cnt):
                    x = x + dx[d] #��ǥ �̵�
                    y = y + dy[d]
                    total += move_sand(x,y,dict[d])
                    
                d += 1
                d = d % 4
            cnt += 1
    return total

print(make_direction())        
    