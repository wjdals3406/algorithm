# -*- coding: utf-8 -*-
import sys
from collections import deque
import copy
n = int(sys.stdin.readline())
data = []
for _ in range(n):
    data.append(list(map(int,sys.stdin.readline().split())))
fish = [[] for _ in range(7)]
shark = 2
start = (0,0)
for i in range(n):
    for j in range(n):
        if data[i][j] == 9:
            start = (i,j)
            data[i][j] = 0
        elif data[i][j] == 1:
            fish[1].append((i,j))
        elif data[i][j] == 2:
            fish[2].append((i,j))
        elif data[i][j] == 3:
            fish[3].append((i,j))
        elif data[i][j] == 4:
            fish[4].append((i,j))
        elif data[i][j] == 5:
            fish[5].append((i,j))
        elif data[i][j] == 6:
            fish[6].append((i,j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    que= deque()
    que.append((x,y))
    dis = copy.deepcopy(data)
    
    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if dis[nx][ny] > shark:
                continue
            if dis[nx][ny] > 0 or dis[nx][ny] == 0:
                dis[nx][ny] = dis[x][y] - 1
                que.append((nx,ny))
    return dis

up = 0   
result = 0 
checklist = deque(fish[shark-1])
while checklist:
    data[start[0]][start[1]] = 0
    dis = bfs(start[0], start[1])
    distance = dict()
    for v in checklist:
        if dis[v[0]][v[1]] > 0:
            continue
        d = -dis[v[0]][v[1]]
        if d in distance:
            distance[d].append(v)
        else:
            distance[d] = [v]
    if len(distance) == 0:
        break
    min_distance = min(distance.keys())
    result += min_distance
    min_list = deque(sorted(distance[min_distance], key = lambda x : (x[0], x[1])))
    start = min_list[0]
    checklist.remove(min_list.popleft())
    up += 1

    if up == shark:
        shark += 1
        up = 0
        if shark > 7:
            continue
        checklist += deque(fish[shark-1])
        
print(result)