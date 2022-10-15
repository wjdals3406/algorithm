# -*- coding: utf-8 -*-
import sys
from collections import deque
n = int(sys.stdin.readline())
data = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dx = [0,0,1,-1] #서,남,동,북
dy = [1,-1,0,0]
direction = [] #하나 popleft해서 그 값만큼 이동했다면 다음 값 popleft해서 이동
for i in range(1,n+1):
    if i==2:
        continue
    if i==n:
        direction.extend([n,n,n])
    else:
        direction.extend([i,i])
sand = [[0, 0, 0.02, 0, 0], #왼쪽방향으로 90도씩 회전
         [0, 0.1, 0.07, 0.01, 0],
         [0.05, 'a', 'y', 'x', 0],
         [0, 0.1, 0.07, 0.01, 0],
         [0, 0, 0.02, 0, 0]]

def rotate_sand(sand):
    ret = [[0] * n for _ in range(n)]
    for r in range(n):
        for c in range(n):
            ret[n - 1 - c][r] = sand[r][c]
    return ret
# def rotate_90(proportion):
#     new_proportion = list(reversed(list(zip(*proportion))))
#     return new_proportion

sand1 = rotate_sand(sand)
sand2 = rotate_sand(sand1)
sand3 = rotate_sand(sand2)








