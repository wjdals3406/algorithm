# -*- coding: utf-8 -*-
#?????? ?? ?? ?? ??? ?? ??? ??
import sys
n,m = map(int, sys.stdin.readline().split())
data = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
res = 0

def dfs(x,y,cnt,total): #???? ?? ?,?,?,? ??? ?? ??
    global res
    if cnt == 4:
        res = max(res,total)
        return 
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if not visited[nx][ny]:
            visited[nx][ny] = 1
            dfs(nx,ny,cnt + 1, total + data[nx][ny])
            visited[nx][ny] = 0

checklist = [[(-1,1), (0,1), (1,1)], [(-1,-1),(0,-1),(1,-1)], [(1,-1), (1,0), (1,1)], [(-1,-1), (-1,0),(-1,1)]]
def check(x,y,value): #?,?,?,? ?? ??
    global res
    for i in checklist: #?/?/?/? ?? ??? ???
        total = 0
        flag = 0
        for xd,yd in i:
            nx = x + xd
            ny = y + yd
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                flag = 1
                break
            total += data[nx][ny]
        if not flag:
            res = max(res, total + value)
            
for i in range(n):
    for j in range(m):
        visited[i][j] = 1
        dfs(i,j,1,data[i][j])
        check(i,j,data[i][j])
        visited[i][j] = 0
print(res)
        