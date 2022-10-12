# -*- coding: utf-8 -*-
import sys
import heapq
INF = int(1e9)
v,e = map(int,sys.stdin.readline().split())
start = int(sys.stdin.readline())
graph = [[] for _ in range(v+1)]
distance = [INF] * (v+1)
for _ in range(e):
    a,b,c = map(int,sys.stdin.readline().split())
    graph[a].append((b,c))

distance[start] = 0
def dijkstra():
    q = []
    heapq.heappush(q,(0,start))
    
    while q:
        dist, node = heapq.heappop(q)
        if distance[node] < dist: #이미 처리된 노드라면 무시
            continue
        for next_node, ndist in graph[node]:
            cost = dist + ndist
            if cost < distance[next_node]:
                distance[next_node] = cost
                heapq.heappush(q, (cost, next_node))
                
dijkstra()
for i in distance[1:]:
    if i == start:
        continue
    if i == INF:
        print("INF")
    else:
        print(i)
    

