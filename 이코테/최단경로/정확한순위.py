# -*- coding: utf-8 -*-
import sys
n, m = map(int,sys.stdin.readline().split())
graph = [[0] * (n+1) for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,sys.stdin.readline().split())
    graph[a][b] = 1
        
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            if graph[a][k] + graph[k][b] == 2:
                graph[a][b] = 1

sumlist = [0] * (n+1)        

for a in range(1, n+1):
    sumlist[a] += sum(graph[a])
for b in range(1, n+1):
    for a in range(1, n+1):
        sumlist[b] += graph[a][b]
        
print(sumlist.count(n-1))