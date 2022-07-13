# -*- coding: utf-8 -*-
import sys
INF = int(1e9)
n, m, c = map(int,sys.stdin.readline().split())
graph = [[INF] * (n+1) for _ in range(n+1)]

for a in range(1,n+1):
    for b in range(1,n+1):
        if a == b:
            graph[a][b] = 0
            
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c
    
for t in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b] , graph[a][t] + graph[t][b])


count = 0
max_val = 0            
for a in range(2, n+1):
    if graph[1][a] != INF:
        count += 1
        if max_val < graph[1][a]:
            max_val = graph[1][a]

print(count, max_val)