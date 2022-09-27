# -*- coding: utf-8 -*-
# import sys
# from collections import deque
# n = int(sys.stdin.readline())
# data = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]

# dx = [1, 0, 0,-1] 
# dy = [0, 1,-1, 0]

# def bfs(x,y):
#     if data[x][y] != 1:
#         return 0
#     que = deque([(x,y)])
#     data[x][y] = -1
#     cnt = 1
#     while que:
#         x,y = que.popleft()

#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if nx < 0 or nx >= n or ny < 0 or ny >= n:
#                 continue
#             if data[nx][ny] == 1:
#                 cnt += 1
#                 data[nx][ny] = cnt
#                 que.append((nx,ny))
#     return cnt
    
# value = []
# result = 0
# for i in range(n):
#     for j in range(n):
#         count = bfs(i,j)
#         if count > 0:
#             result += 1
#             value.append(count)
            
# value.sort()
# print(result)
# for i in value:
#     print(i)

import sys
n = int(sys.stdin.readline())
data = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]

dx = [1, 0, 0,-1] 
dy = [0, 1,-1, 0]

cnt = 0
def dfs(x,y):
    global cnt
    if data[x][y] != 1:
        return 0
    cnt -= 1
    data[x][y] = cnt
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        dfs(x+dx[i], y+dy[i])    
    return cnt
    
value = []
result = 0
for i in range(n):
    for j in range(n):
        count = -dfs(i,j)
        if count > 0:
            result += 1
            cnt = 0
            value.append(count)
            
value.sort()
print(result)
for i in value:
    print(i)