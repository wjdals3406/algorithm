# -*- coding: utf-8 -*-
import sys
n,m = map(int, sys.stdin.readline().split())
data = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
prefix_sum = [[0]  * n for _ in range(n)]
sum = 0
for i in range(n):
    for j in range(n):
        sum += data[i][j]
        prefix_sum[i][j] = sum
for _ in range(m):
    x1,y1,x2,y2 = map(int, sys.stdin.readline().split())
    