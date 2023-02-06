# -*- coding: utf-8 -*-
#???? ?? A[r][c]? ? / ???? ?? ? ?? ? ???? ???? ?? ?? ???
import sys
from collections import deque
n,q = map(int, sys.stdin.readline().split())
data = [list(map(int, sys.stdin.readline().split())) for _ in range(2**n)]
qlist = list(map(int, sys.stdin.readline().split()))
size = 2**n
#1.?? 90? ??
#2.???? ?? A[r][c]? ? : sum(map(sum,data))
#3.???? ?? ? ?? ? ???? ???? ?? ?? ???
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def rotate_90(row,column,size): 
    temp = []
    #data[row:row+size][column:column+size]??? ?? ??? / ??? ??? ?? append ???
    for i in range(row,row+size):
        temp.append(data[i][column:column+size])
    
    for r in range(size):
        for c in range(size):
            data[row+c][column + size-r-1] = temp[r][c]
                    
def bfs(x,y): 
    que = deque([[x,y]])
    cnt = 1
    visited[x][y] = cnt
    while que:
        x,y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= size or ny < 0 or ny >= size:
                continue
            if not visited[nx][ny] and data[nx][ny] > 0:
                visited[nx][ny] = cnt + 1
                cnt += 1
                que.append([nx,ny])

for l in qlist: #?? ?? ?
    if l > 0:
        for r in range(0, size, 2**l):
            for c in range(0, size, 2**l):
                rotate_90(r,c,2**l) #??? ??(???, ??, ???? size)
    
    rmlist = set()
    for i in range(size):
        for j in range(size):
            if data[i][j] > 0:
                cnt = 0
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if nx < 0 or nx >= size or ny < 0 or ny >= size:
                        continue
                    if data[nx][ny] > 0:
                        cnt += 1
                if cnt <= 2:
                    rmlist.add((i,j))
        
    for x,y in rmlist:
        data[x][y] -= 1
                    

visited = [[0] * size for _ in range(size)]
for i in range(size):
    for j in range(size):
        if not visited[i][j] and data[i][j] > 0:
            bfs(i,j)
            
print(sum(map(sum,data)))
print(max(map(max,visited)))