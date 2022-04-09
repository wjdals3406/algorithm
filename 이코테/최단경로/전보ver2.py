# -*- coding: utf-8 -*-
import heapq
import sys
INF = int(1e9)
n, m, c = map(int,sys.stdin.readline().split())
start = 1
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)


for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))
    
def dijkstra(start):
    q = []
    
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        
        if distance[now] < dist:
            continue
        
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
                
dijkstra(start)
        
count = 0
max_val = 0            
for i in range(1, n+1):
    if start == i:
        continue
    if distance[i] != INF:
        count += 1
        if max_val < distance[i]:
            max_val = distance[i]
            
print(count, max_val)