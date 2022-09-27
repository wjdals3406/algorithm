# -*- coding: utf-8 -*-
import sys
n,m = map(int, sys.stdin.readline().split())
data = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def check(x,y,cnt,sum):
    global maxval
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        
        cnt += 1
        sum += data[nx][ny]
        
    # if cnt == 4:
    #     maxval = max(maxval, sum)
    if cnt == 5:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            maxval = max(maxval, sum - data[nx][ny])

maxval = -1
def dfs(x,y,cnt,sum): #ㅏ, ㅓ, ㅗ, ㅜ 모양이 count가 안됨
    global visited
    global maxval
    cnt += 1
    sum += data[x][y]
    visited[x][y] = True
    if cnt == 4:
        return sum
    if cnt == 1:
        check(x,y,cnt,sum)   
        
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
            
        if not visited[nx][ny]:
            val = dfs(nx, ny, cnt, sum)
            maxval = max(maxval, val)
        
    return sum

for k in range(n):
    for l in range(m):
        dfs(k,l,0,0)
        visited = [[False] * m for _ in range(n)]
        
print(maxval)
        
        