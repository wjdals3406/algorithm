# -*- coding: utf-8 -*-
import sys
n,m = map(int, sys.stdin.readline().split())
x,y,d = map(int, sys.stdin.readline().split())
data = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
#빈칸 : 0, 벽 : 1

dx = [-1, 0, 1, 0] #북, 동, 남, 서
dy = [0, 1, 0, -1]

def turn_left(dir):
    return (dir - 1) % 4
def turn_back(dir):
    return (dir - 2) % 4

cnt = 0
flag = 1
flag2 = 1
while True:
    if flag: # 1번
        data[x][y] = -1 #현재 위치를 청소함
        cnt += 1
    for i in range(4): #2번
        flag = 1
        d = turn_left(d) #회전
        nx = x + dx[d]
        ny = y + dy[d]

        if data[nx][ny] == 0:
            flag2 = 0
            x,y = nx, ny
            break
    if flag2 == 0:
        flag2 = 1
        continue
    
    #네 방향 모두 청소가 이미 되어있거나 벽일 때
    nd = turn_back(d)
    nx = x + dx[nd]
    ny = y + dy[nd]
    if data[nx][ny] == -1 : #뒤의 방향이 빈 칸일때
        x,y = nx, ny #2번으로 돌아감
        flag = 0
    else:
        break
    
print(cnt)   