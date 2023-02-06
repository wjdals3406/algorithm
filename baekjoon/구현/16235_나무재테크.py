# -*- coding: utf-8 -*-
#소요 시간 : 1시간 30분 / 1시간 이내에 다 풀고, 실수해서 30분 날렸다...
#개선 사항 : 입력으로 주어지는 위치는 모두 다르다고 명시해서 sort함수 사용할 필요X
#deque 이용해서 appendleft하면 됨

import sys
#K년이 지난 후 살아남은 나무의 수
# 가장 처음에 양분은 모든 칸에 5만큼 들어있다.
# 같은 1×1 크기의 칸에 여러 개의 나무가 심어져 있을 수도 있다.
n, m, k = map(int, sys.stdin.readline().split())
winter_nutrient = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
nutrient_tree = [[[5,[]] for _ in range(n)] for _ in range(n)] #[영양분, tree 정보]
for _ in range(m):
    x,y,z = map(int, sys.stdin.readline().split())
    nutrient_tree[x-1][y-1][1].append(z) # r과 c는 1부터 시작
    
dir = (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)

while k > 0:
    #봄, 여름
    for i in range(n):
        for j in range(n):
            #봄
            if len(nutrient_tree[i][j][1]) > 1: #어린 순서로 정렬
                nutrient_tree[i][j][1].sort()
                
            for index,age in enumerate(nutrient_tree[i][j][1]): 
                if age > nutrient_tree[i][j][0]:
                    dead = nutrient_tree[i][j][1][index:] #이 이후부터의 나무는 죽음
                    nutrient_tree[i][j][1] = nutrient_tree[i][j][1][:index]
                    #여름 :  봄에 죽은 나무가 양분으로 변함
                    for d in dead:
                        nutrient_tree[i][j][0] += (d // 2)
                    break #나무 죽음
                else:
                    nutrient_tree[i][j][0] -= age #자신의 나이만큼 양분을 먹음
                    nutrient_tree[i][j][1][index] += 1 #나이 증가
    
    #가을 : 나무 번식 / 겨울 : 양분 추가 => 동시에 진행
    for x in range(n):
        for y in range(n):
            nutrient_tree[x][y][0] += winter_nutrient[x][y]
            
            if len(nutrient_tree[x][y][1]) > 0:
                for age in nutrient_tree[x][y][1]:
                    if age % 5 == 0: #나이가 5의 배수
                        for d in dir:
                            nx,ny = x + d[0], y + d[1]
                            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                                continue
                            nutrient_tree[nx][ny][1].append(1) #나이가 1인 나무 생성
                            
    k -= 1

res = 0
for r in range(n):
    for c in range(n):
        res += len(nutrient_tree[r][c][1])
print(res)
                            

# deque 이용한 코드
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