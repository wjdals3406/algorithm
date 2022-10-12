# -*- coding: utf-8 -*-
import sys
INF = int(1e9)
n, m = map(int,sys.stdin.readline().split())
graph = [[INF] * (n+1) for _ in range(n+1)]

for a in range(1,n+1):
    for b in range(1,n+1):
        if a == b:
            graph[a][b] = 0
            
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1
    
x, k = map(int,sys.stdin.readline().split())
 
 #A�� 1�� ��ġ���� K�� ȸ��� ����� ��� D1k�� ���ϸ� ��   
for t in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b] , graph[a][t] + graph[t][b])

if graph[1][k] + graph[k][x] >= INF:
    print(-1)
else:
    print(graph[1][k] + graph[k][x])
            
