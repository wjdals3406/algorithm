# -*- coding: utf-8 -*-
import sys
n = int(sys.stdin.readline())
cnt = 0
row = [0] * n #�ε����� row��, value�� ���� �ǹ��� / ��, row[1] = 3�� 1��° �࿡�� 3��° ���� ���� �ִٴ� ���� �ǹ�

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


# n = int(sys.stdin.readline()) -> ���α׷��ӽ������� ����ó���Ǵµ� ���ؿ����� �� NameError�� ����..?
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