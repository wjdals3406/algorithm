# -*- coding: utf-8 -*-
import sys
import heapq
n,m = map(int, sys.stdin.readline().split())
INF = int(1e9)
graph = [[] for _ in range(n+1)]
distance = [INF] *(n+1)
res = 0 
#양방향, 거리는 모두 1
#k회사를 거쳐 x회사로 감
for _ in range(m):
    b,c = map(int, sys.stdin.readline().split())
    graph[b].append(c)
    graph[c].append(b)
    
x,k = map(int, sys.stdin.readline().split())

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    
    while q:
        dist, node = heapq.heappop(q)
        if distance[node] < dist:
            continue
        for next_node in graph[node]:
            if distance[next_node] > dist + 1 :
                distance[next_node] = dist + 1 
            heapq.heappush(q,(dist + 1, next_node))

def make_distance(dest):
    for i in range(len(distance)):
        if i == dest:
            if distance[i] == INF:
                print(-1)
                exit()
            return distance[i]
        
    
 
dijkstra(1)   
res += make_distance(k)
distance = [INF] *(n+1)
dijkstra(k)
res += make_distance(x)
    
print(res)