# -*- coding: utf-8 -*-
import sys
INF = int(1e9)
n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
graph = [[INF] * (n+1) for _ in range(n+1)]

#자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n+1):
    graph[a][a] = 0

for _ in range(m):
    a,b,c = map(int,sys.stdin.readline().split())
    if graph[a][b] > c: #중복된 값이 있을 수 있기 때문
        graph[a][b] = c
        
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
            
for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == INF:
            graph[a][b] = 0
        print(graph[a][b], end = ' ')
    print()
