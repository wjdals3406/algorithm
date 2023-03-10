# -*- coding: utf-8 -*-
import sys
from collections import deque
n,m = map(int, sys.stdin.readline().split())

data = [[0] * (n+1)]
for _ in range(n):
    data.append([0]+list(map(int, sys.stdin.readline().split())))

dir = [list(map(int, sys.stdin.readline().split())) for _ in range(m)] #d,s
dx = [-1,1,0,0] #À§,¾Æ·¡,¿Þ,¿À
dy = [0,0,-1,1]

sx, sy = (n+1)//2, (n+1)//2 
res = 0
q = []

def make_magic(d,s):
    for i in range(1,s+1):
        data[sx+dx[d-1]*i][sy+dy[d-1]*i] = 0

def make_board():
    bx = [0,1,0,-1]
    by = [-1,0,1,0]
    
    x,y = sx,sy
    d = 0
    
    for i in range(1,n+1):
        for _ in range(2):
            if i == n:
                for _ in range(i-1):
                    x,y = x + bx[d], y + by[d]
                    q.append((x,y))
                break
            
            else:
                for _ in range(i):
                    x,y = x + bx[d], y + by[d]
                    q.append((x,y))
                
            d = (d+1)%4

def move():
    que = deque()
    
    for x,y in q:
        if data[x][y] == 0:
            que.append((x,y))
            
        elif len(que) > 0 and data[x][y] != 0:
            rx,ry = que.popleft()
            data[rx][ry], data[x][y] = data[x][y], data[rx][ry]
            que.append((x,y))
        
            
def bomb():
    global res
    pre_x, pre_y = sx,sy
    cnt = 1
    que = deque()
    is_bomb = False
    
    for x,y in q:

        if data[pre_x][pre_y] == data[x][y]:
            cnt += 1
        else:
            if cnt >= 4:
                is_bomb = True
                
                res += cnt * (data[que[0][0]][que[0][1]])
                
                while que:
                    rx,ry = que.popleft()
                    data[rx][ry] = 0
                    
            cnt = 1
            que = deque()
            
        que.append((x,y))
        pre_x,pre_y = x,y
    
    return is_bomb

def init_board():
    new_board = [[0] * (n+1) for _ in range(n+1)]
    pre_x, pre_y = sx,sy
    cnt = 1
    que = deque()
    
    for x,y in q:
    
        if data[pre_x][pre_y] == data[x][y]:
            cnt += 1
        else:
            if pre_x == sx and pre_y == sy:
                pre_x,pre_y = x,y
                continue
            
            que.append(cnt)
            que.append(data[pre_x][pre_y])
            
            if data[x][y] == 0:
                break
            cnt = 1
            
        pre_x,pre_y = x,y
    
    for x,y in q:
        if len(que) > 0:
            new_board[x][y] = que.popleft()
        else:
            break
    
    return new_board
    
make_board()
for i in range(m):
    make_magic(dir[i][0], dir[i][1])
    move()
    
    while bomb():
        move()
    
    data = init_board()
    
print(res)