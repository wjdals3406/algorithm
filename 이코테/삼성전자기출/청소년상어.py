# -*- coding: utf-8 -*-
import sys
import copy
data_original = [[] for _ in range(4)]
dir_original = [[] for _ in range(4)]
for i in range(4):
    info = list(map(int, sys.stdin.readline().split()))
    for j in range(0,8,2):
        data_original[i].append(info[j])
        dir_original[i].append(info[j+1])

dir_value = [0, (-1,0), (-1,-1), (0,-1), (1, -1), (1, 0), (1,1), (0, 1), (-1, 1)]

def find_direction(x,y, dir):
    nx, ny = dir_value[dir[x][y]] 
    nx, ny = nx + x, ny + y
    return nx, ny

def shark_find(x,y, dir): #그 방향에 있는 것들 모두 
    nx, ny = dir_value[dir[x][y]] 
    newx, newy = x,y
    alist = []
    for _ in range(3):
        newx = nx + newx
        newy = ny + newy
        if newx < 0 or newy < 0 or newx >= 4 or newy >= 4 :
            break
        alist.append((newx, newy))
    return alist
       
def fish_move(data, dir, sx, sy): #물고기가 움직이는 함수
    fish = dict()
    for i in range(4):
        for j in range(4):
            if data[i][j] == 0:
                continue
            fish[data[i][j]] = (i,j)
    del fish[data[sx][sy]] 
    data[sx][sy] = 0 #상어 이동
    
    for i in sorted(fish): 
        x,y = fish[i] 
        nx, ny = find_direction(x,y, dir)
        
        while nx < 0 or ny < 0 or nx >= 4 or ny >= 4 or (nx == sx and ny == sy):
            if dir[x][y] == 8:
                dir[x][y] = 1
            else:
                dir[x][y] += 1
            nx, ny = find_direction(x,y, dir)
        
        data[nx][ny], data[x][y] = data[x][y], data[nx][ny]
        dir[nx][ny], dir[x][y] = dir[x][y], dir[nx][ny]
        if data[x][y] == 0: #이동한 자리가 빈칸이었다면 
            fish[data[nx][ny]] = (nx,ny)
        else:
            fish[data[x][y]], fish[data[nx][ny]] = fish[data[nx][ny]], fish[data[x][y]]
    return data, dir

def dfs(sx, sy, data_ori, dir_ori, result):
    data = copy.deepcopy(data_ori)
    dir = copy.deepcopy(dir_ori)
    if sx < 0 or sy < 0 or sx >= 4 or sy >= 4 or data[sx][sy] == 0:
       return result
    result += data[sx][sy] 
    # data[sx][sy] = 0 #상어 이동
    data, dir = fish_move(data, dir, sx, sy) #물고기 이동
    
    shark_move = shark_find(sx,sy,dir) #상어가 이동할 곳
    dir[sx][sy] = 0
    maxval = -1
    for i in shark_move:
        maxval = max(maxval, dfs(i[0], i[1], data, dir, result))
        
    if not shark_move:
        return result
    
    return maxval
    
sx,sy = 0,0
nx,ny = sx, sy
count = 0
result = 0
print(dfs(sx, sy, data_original, dir_original, result))