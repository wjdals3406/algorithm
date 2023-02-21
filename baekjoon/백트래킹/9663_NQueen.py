# -*- coding: utf-8 -*-
import sys
n = int(sys.stdin.readline())
cnt = 0
row = [0] * n #인덱스는 row를, value는 열을 의미함 / 즉, row[1] = 3은 1번째 행에는 3번째 열에 퀸이 있다는 것을 의미

def dfs(x):
    global cnt
    if x == n:
        cnt += 1
        return
    
    for i in range(n):
        row[x] = i
        flag = 0
        
        for i in range(x):
            if(row[x] == row[i]) or (x - i == abs(row[x] - row[i])):
                flag = 1
                break
        if not flag:
            dfs(x+1)
dfs(0)

print(cnt)     


# n = int(sys.stdin.readline()) -> 프로그래머스에서는 성공처리되는데 백준에서는 왜 NameError가 날까..?
# data = [[0] * n for _ in range(n)]
# cnt = 0
# def dfs(x,y,check_list):
#     global cnt
#     if x == n-1:
#         cnt += 1
#         return
    
#     for i in range(n):
#         nx = x + 1
#         ny = i
#         flag = 0
        
#         if not data[nx][ny]:
#             for x1,y1 in check_list:
#                 if x1 == nx or y1 == ny or (abs(x1-nx) == abs(y1-ny)): 
#                     flag = 1
#                     break
        
#             if not flag:
#                 data[nx][ny] = 1
#                 dfs(nx,ny,check_list + [(nx,ny)])
#                 data[nx][ny] = 0
    
# for j in range(n):
#     data[0][j] = 1
#     dfs(0,j,[[0,j]])
#     data[0][j] = 0
        
# print(cnt)