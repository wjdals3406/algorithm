# -*- coding: utf-8 -*-
#�ҿ� �ð� : 1�ð� 30�� / 1�ð� �̳��� �� Ǯ��, �Ǽ��ؼ� 30�� ���ȴ�...
#���� ���� : �Է����� �־����� ��ġ�� ��� �ٸ��ٰ� ����ؼ� sort�Լ� ����� �ʿ�X
#deque �̿��ؼ� appendleft�ϸ� ��

import sys
#K���� ���� �� ��Ƴ��� ������ ��
# ���� ó���� ����� ��� ĭ�� 5��ŭ ����ִ�.
# ���� 1��1 ũ���� ĭ�� ���� ���� ������ �ɾ��� ���� ���� �ִ�.
n, m, k = map(int, sys.stdin.readline().split())
winter_nutrient = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
nutrient_tree = [[[5,[]] for _ in range(n)] for _ in range(n)] #[�����, tree ����]
for _ in range(m):
    x,y,z = map(int, sys.stdin.readline().split())
    nutrient_tree[x-1][y-1][1].append(z) # r�� c�� 1���� ����
    
dir = (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)

while k > 0:
    #��, ����
    for i in range(n):
        for j in range(n):
            #��
            if len(nutrient_tree[i][j][1]) > 1: #� ������ ����
                nutrient_tree[i][j][1].sort()
                
            for index,age in enumerate(nutrient_tree[i][j][1]): 
                if age > nutrient_tree[i][j][0]:
                    dead = nutrient_tree[i][j][1][index:] #�� ���ĺ����� ������ ����
                    nutrient_tree[i][j][1] = nutrient_tree[i][j][1][:index]
                    #���� :  ���� ���� ������ ������� ����
                    for d in dead:
                        nutrient_tree[i][j][0] += (d // 2)
                    break #���� ����
                else:
                    nutrient_tree[i][j][0] -= age #�ڽ��� ���̸�ŭ ����� ����
                    nutrient_tree[i][j][1][index] += 1 #���� ����
    
    #���� : ���� ���� / �ܿ� : ��� �߰� => ���ÿ� ����
    for x in range(n):
        for y in range(n):
            nutrient_tree[x][y][0] += winter_nutrient[x][y]
            
            if len(nutrient_tree[x][y][1]) > 0:
                for age in nutrient_tree[x][y][1]:
                    if age % 5 == 0: #���̰� 5�� ���
                        for d in dir:
                            nx,ny = x + d[0], y + d[1]
                            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                                continue
                            nutrient_tree[nx][ny][1].append(1) #���̰� 1�� ���� ����
                            
    k -= 1

res = 0
for r in range(n):
    for c in range(n):
        res += len(nutrient_tree[r][c][1])
print(res)
                            

# deque �̿��� �ڵ�
# from collections import deque

# n, m, k = map(int, input().split(' '))

# a = [list(map(int, input().split(' '))) for _ in range(n)]
# graph = [[5] * n for _ in range(n)]
# trees = [[deque() for _ in range(n)] for _ in range(n)]
# dead_trees = [[list() for _ in range(n)] for _ in range(n)]
# for _ in range(m):
#     x, y, z = map(int, input().split(' '))
#     trees[x - 1][y - 1].append(z)

# dx = [-1, -1, 0, 1, 1, 1, 0, -1]
# dy = [0, 1, 1, 1, 0, -1, -1, -1]


# def spring_summer():
#     for i in range(n):
#         for j in range(n):
#             len_ = len(trees[i][j])
#             for k in range(len_):
#                 if graph[i][j] < trees[i][j][k]:
#                     for _ in range(k, len_):
#                         dead_trees[i][j].append(trees[i][j].pop())
#                     break
#                 else:
#                     graph[i][j] -= trees[i][j][k]
#                     trees[i][j][k] += 1

#     for i in range(n):
#         for j in range(n):
#             while dead_trees[i][j]:
#                 graph[i][j] += dead_trees[i][j].pop() // 2


# def fall_winter():
#     for i in range(n):
#         for j in range(n):
#             for k in range(len(trees[i][j])):
#                 if trees[i][j][k] % 5 == 0:
#                     for l in range(8):
#                         nx, ny, = i + dx[l], j + dy[l]

#                         if nx < 0 or nx >= n or ny < 0 or ny >= n:
#                             continue
#                         trees[nx][ny].appendleft(1)

#             graph[i][j] += a[i][j]


# for i in range(k):
#     spring_summer()
#     fall_winter()

# answer = 0
# for i in range(n):
#     for j in range(n):
#         answer += len(trees[i][j])

# print(answer)