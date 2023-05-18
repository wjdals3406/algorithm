# -*- coding: utf-8 -*-
import sys
import heapq
INF = int(1e9)
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)
for _ in range(m):
    u,v,w = map(int, sys.stdin.readline().split())
    graph[u].append((v,w))
start,end = map(int, sys.stdin.readline().split())
    
def dijkstra():
    h = []
    heapq.heappush(h, (0, start))
    distance[start] = 0
    while h:
        dist, now = heapq.heappop(h)
        if distance[now] < dist :
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(h, (cost, i[0]))
dijkstra()
print(distance[end])