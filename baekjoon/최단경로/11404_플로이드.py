# -*- coding: utf-8 -*-
import sys
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
distance = [[int(1e9)] * (n+1) for _ in range(n+1)]

for _ in range(m):
    a,b,c = map(int, sys.stdin.readline().split())
    if c < distance[a][b]:
        distance[a][b] = c
    
for i in range(1,n+1):
    distance[i][i] = 0


for k in range(1,n+1): #중간 지점
    for a in range(1,n+1): #시작 정점
        for b in range(1,n+1): #도착 정점
            distance[a][b] = min(distance[a][k] + distance[k][b], distance[a][b])
            
for i in range(1,n+1):
    for j in range(1,n+1):
        if distance[i][j] == int(1e9):
            print(0, end = " ")
        else:
            print(distance[i][j], end = " ")
    print()
