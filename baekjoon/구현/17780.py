# -*- coding: utf-8 -*-
import sys
# 체스판의 크기 N, 말의 개수 K
n,k = map(int, sys.stdin.readline().split())
# 0은 흰색, 1은 빨간색, 2는 파란색
color = [[0] for _ in range(n+1)]
horse = [[0] for _ in range(k+1)]
for i in range(1,n+1):
    color[i].extend(list(map(int, sys.stdin.readline().split())))
for i in range(1,k+1):
    horse[i].extend(list(map(int, sys.stdin.readline().split())))

data = [[[] for _ in range(n+1)] for _ in range(n+1)]
dx = [0,0,0,-1,1]
dy = [0,1,-1,0,0]
#→, ←, ↑, ↓ 1,2,3,4
for i in range(1,k+1):
    data[horse[i][1]][horse[i][2]].append(i)
cnt = 0

#이동한 칸이 하얀색 칸인지, 빨간색 칸인지, 파란색 칸인지
#종료 조건 두개
flag = 0
while cnt <= 1000:
    cnt += 1
    for i in range(1,k+1):
        _,x,y,d = horse[i] #현재 위치 및 방향
        if data[x][y][0] == i: #체스의 맨 밑에 있을 때
            nx = x + dx[d]
            ny = y + dy[d]
            if nx <= 0 or nx >n or ny <= 0 or ny > n or color[nx][ny] == 2: #파란색과 같은 경우
                #이동 방향 반대로
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
                
            if color[nx][ny] == 0: #이동하는 칸이 흰색
                data[nx][ny].extend(data[x][y])
            elif color[nx][ny] == 1: #이동하는 칸이 빨간색
                data[nx][ny].extend(data[x][y][::-1])
            
            #horse 좌표 이동
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