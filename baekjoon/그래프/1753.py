# -*- coding: utf-8 -*-
import sys
import heapq
INF = int(1e9)
V,E = map(int, sys.stdin.readline().split())
k = int(sys.stdin.readline())
graph = [[] for _ in range(V+1)]
distance = [INF] * (V+1)
for _ in range(E):
    u,v,w = map(int, sys.stdin.readline().split())
    graph[u].append((v,w))
    
def dijkstra():
    h = []
    heapq.heappush(h, (0, k))
    distance[k] = 0
    while h:
        dist, node = heapq.heappop(h)
        
        if distance[node] < dist:
            continue
        for i in graph[node]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(h, (cost, i[0]))

dijkstra()

for i in distance[1:]:
    if i == INF:
        print("INF")
    else:
        print(i)


                        
